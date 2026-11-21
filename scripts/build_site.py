#!/usr/bin/env python3
"""Build the public reading site from the repository's current Markdown.

Requires Python 3.12+ and Pandoc 3.x. Uses no network and no Python packages.
Mathematics is emitted as native MathML, including the original TeX annotation.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
import html
import json
import os
from pathlib import Path, PurePosixPath
import posixpath
import re
import shutil
import subprocess
import sys
import unicodedata
from urllib.parse import quote, unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/1337isnot1337/solved-conjectures"
DEFAULT_URL = "https://1337isnot1337.github.io/solved-conjectures/"
SITE_NAME = "Solved conjectures"
READER = "markdown+gfm_auto_identifiers+autolink_bare_uris+tex_math_single_backslash+tex_math_dollars+task_lists-smart"
STATUS_LABELS = {
    "full": "Lean: formalized stated result",
    "partial": "Lean: partial formalization",
    "none": "Lean: not formalized",
}
EXTERNAL_CREDIT = {
    "graffiti-pc-318": (
        "@JesterInABarrel",
        "https://x.com/JesterInABarrel/status/2123233964827812334",
    ),
}
PARTIAL_CATEGORIES = {
    "frankl-generator-families": "Combinatorics",
    "lonely-runner-two-insertions": "Lonely runners",
    "erdos-gyarfas-abelian-covers": "Graph theory and discrete geometry",
    "hadamard-2396": "Combinatorics",
}
SOURCE_TITLES = {
    "CONTENTS.md": "Mathematical conjectures: full catalogue",
    "HISTORY.md": "Research history",
    "docs/verification.md": "Verification and reproducible checks",
    "docs/lean-status.md": "Lean formalization status",
    "docs/formalization.md": "Lean formalization guide",
}
STATUS_LABEL_SLUGS = {
    "Baricz–Pogány's asymptotic-coefficient positivity conjecture": "baricz-pogany-coefficients",
    "Malek's conjecture": "malek-subpermanent",
    "Pula–Song–Wanless conjecture": "pula-song-wanless",
    "Perron root of permanental compounds": "perron-root-permanental-compounds",
    "Karp–Vishnyakova–Zhang's Bessel-ratio unimodality conjecture": "kvz-bessel-unimodality",
    "Ferreira–Simon's Wright log-concavity conjecture": "ferreira-simon-wright",
    "Karp–Vishnyakova–Zhang's gamma-quotient conjecture": "kvz-gamma-quotient",
    "Alexandersson's Fuss–Catalan conjecture": "alexandersson-fuss-catalan",
    "Sagan–Swanson conjecture": "sagan-swanson-normality",
    "Bernardi–Morales's delta-process conjecture": "bernardi-morales-delta",
    "Gilmore's crossing–nesting conjecture": "gilmore-crossing-nesting",
    "Chow's conjecture": "chow-conjecture",
    "Németh–Seberry–Shu conjecture": "nemeth-seberry-shu",
    "Sonntag–Teichert conjecture": "sonntag-teichert",
    "Horňák–Woźniak conjecture": "hornak-wozniak",
    "L-solitaire": "l-solitaire-limit-shapes",
    "Three-player War": "spivey-multiplayer-war",
    "Pham denominator degree": "pham-denominator-degree",
    "Batista Egyptian fractions": "batista-egyptian-fractions",
    "CUT Family B": "cut-family-b",
    "CUT arithmetic periodicity": "cut-arithmetic-periodicity",
    "Loneliness on a fixed hyperplane": "loneliness-on-a-hyperplane",
    "Graffiti.pc Conjecture 318": "graffiti-pc-318",
    "Li coefficient sign": "li-coefficient-sign",
    "Frankl generating families": "frankl-generator-families",
    "Hadamard order-2396 automorphism obstruction": "hadamard-2396",
    "Hadamard order-2396 partial results": "hadamard-2396",
    "Lonely-runner two insertions": "lonely-runner-two-insertions",
    "Zhang's Question 8.4: deletion values of the lonely runner": "zhang-deletion-values",
    "Erdős–Gyárfás abelian covers": "erdos-gyarfas-abelian-covers",
    "Erdős 607 line sizes": "erdos-607-line-sizes",
    "Growing rectangles": "rectangle-partition-asymptotics",
    "Distance graphs with three missing differences": "distance-graph-densities",
    "Oravcová–Soták conjecture for five to eight distances": "oravcova-sotak",
    "Johnson–Kaya–Matzke conjecture on Babai spectra of paths": "babai-spectrum-paths",
    "Two-difference Motzkin theorem": "two-difference-motzkin",
    "Tight six speeds and critical planes": "tight-six-speeds",
    "Six-speed spectrum": "six-speed-spectrum",
    "Eight-runner equality cases": "tight-seven-speeds",
    "Nine-runner equality case": "tight-eight-speeds",
    "Symmetric four-point density": "symmetric-four-point-density",
    "Packing with two nonmixed gaps": "nonmixed-gap-packing",
    "Haralambis three-difference theorem": "haralambis-three-differences",
    "Five-speed spectrum": "five-speed-spectrum",
    "Tight nine-speed sets": "tight-nine-speeds",
    "Seven-speed spectrum": "seven-speed-spectrum",
    "Eight-speed spectrum": "eight-speed-spectrum",
    "Eleven-through-fourteen-runner equality": "tight-eleven-to-fourteen",
}


def landing_lean_status(source_text: str) -> str:
    """Mathematical scope and formalization status are independent axes."""
    explicit = re.search(r"(?im)^\*\*Lean status:\*\*\s*(\w+)\b", source_text)
    if explicit:
        status = explicit.group(1).lower()
        if status not in STATUS_LABELS:
            raise ValueError(f"Unknown landing-page Lean status: {status}")
        return status
    if re.search(r"(?:no Lean formalization|not (?:yet )?formalized|pending Lean formalization)", source_text, re.I):
        return "none"
    raise ValueError("Landing page needs an explicit Lean status")


def escape(value: object) -> str:
    return html.escape(str(value), quote=True)


def nodes(value):
    if isinstance(value, dict):
        yield value
        yield from nodes(value.get("c", []))
    elif isinstance(value, list):
        for item in value:
            yield from nodes(item)


def plain(value, *, skip_links=False) -> str:
    if isinstance(value, list):
        return "".join(plain(item, skip_links=skip_links) for item in value)
    if not isinstance(value, dict):
        return ""
    kind = value.get("t")
    content = value.get("c", [])
    if kind == "Str":
        return content
    if kind in {"Space", "SoftBreak", "LineBreak"}:
        return " "
    if kind in {"Code", "CodeBlock", "Math"}:
        return content[-1]
    if kind in {"Link", "Image"}:
        return "" if skip_links else plain(content[1])
    if kind == "Header":
        return plain(content[2])
    if kind in {"RawInline", "RawBlock"}:
        return ""
    result = plain(content, skip_links=skip_links)
    if kind in {"Para", "Plain", "BlockQuote"}:
        return result + " "
    return result


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def excerpt(value: str, limit=185) -> str:
    value = clean_text(value)
    if len(value) <= limit:
        return value
    return value[: limit - 1].rsplit(" ", 1)[0].rstrip(".,;:") + "…"


def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def git(*args: str) -> str:
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else ""


def pandoc(arguments, *, text=None) -> str:
    result = subprocess.run(["pandoc", *arguments], input=text, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or "Pandoc failed")
    if result.stderr.strip():
        if "Could not convert TeX math" in result.stderr:
            raise RuntimeError("A formula could not be rendered as MathML:\n" + result.stderr.strip())
        print(result.stderr.strip(), file=sys.stderr)
    return result.stdout


def read_markdown(arguments, *, text=None) -> dict:
    ast = json.loads(pandoc(["--from", READER, "--to", "json", *arguments], text=text))
    for node in nodes(ast["blocks"]):
        if node.get("t") == "CodeBlock" and node["c"][0][1] == ["math"]:
            tex = node["c"][1]
            node.update(t="Para", c=[{"t": "Math", "c": [{"t": "DisplayMath"}, tex]}])
        elif node.get("t") == "Math" and node["c"][0]["t"] == "InlineMath":
            tex = node["c"][1]
            if tex.startswith("`") and tex.endswith("`"):
                node["c"][1] = tex[1:-1]
    return ast


@dataclass
class Document:
    source: str
    route: str
    ast: dict
    title: str
    lastmod: str


@dataclass
class Result:
    slug: str
    title: str
    category: str
    status: str
    summary: str
    summary_blocks: list = field(default_factory=list)
    scope: str = "result"
    search: str = ""
    checked_scope: str = ""


class Builder:
    def __init__(self, output: Path, base_url: str, workers: int):
        self.output = output.resolve()
        self.base_url = base_url.rstrip("/") + "/"
        self.base_path = urlsplit(self.base_url).path
        self.workers = workers
        self.documents: dict[str, Document] = {}
        self.results: list[Result] = []
        self.result_map: dict[str, Result] = {}
        self.pages: list[dict] = []
        self.copied_files: set[str] = set()
        self.commit = git("rev-parse", "HEAD")
        self.commit_date = git("show", "-s", "--format=%cI", "HEAD")
        self.source_dirty = bool(git("status", "--porcelain", "--untracked-files=normal"))

    def url(self, route="") -> str:
        return self.base_path + route

    def canonical(self, route="") -> str:
        return self.base_url + route

    @staticmethod
    def route_for(source: str) -> str:
        if source == "README.md":
            return ""
        if source == "CONTENTS.md":
            return "catalogue/"
        if source == "HISTORY.md":
            return "history/"
        path = PurePosixPath(source)
        if path.name.lower() == "readme.md":
            return str(path.parent).lower() + "/"
        return str(path.with_suffix("")).lower() + "/"

    def read_document(self, source: str) -> Document:
        ast = read_markdown([str(ROOT / source)])
        title = next((plain(node) for node in ast["blocks"] if node.get("t") == "Header"), PurePosixPath(source).stem)
        lastmod = git("log", "-1", "--format=%cI", "--", source)
        return Document(source, self.route_for(source), ast, SOURCE_TITLES.get(source, clean_text(title)), lastmod)

    def read_sources(self):
        sources = {"README.md", "CONTENTS.md", "HISTORY.md"}
        sources.update(path.relative_to(ROOT).as_posix() for path in (ROOT / "results").rglob("*.md"))
        sources.update(path.relative_to(ROOT).as_posix() for path in (ROOT / "docs").rglob("*.md"))
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            for document in pool.map(self.read_document, sorted(sources)):
                self.documents[document.source] = document
        routes = [document.route for document in self.documents.values()]
        if len(routes) != len(set(routes)):
            raise ValueError("Two source documents produce the same public route")

    @staticmethod
    def result_slug(value) -> str | None:
        for node in nodes(value):
            if node.get("t") == "Link":
                match = re.match(r"results/([^/]+)(?:/|$)", node["c"][2][0])
                if match:
                    return match.group(1)
        return None

    def read_results(self):
        category = "Mathematics"
        found: dict[str, Result] = {}
        for block in self.documents["CONTENTS.md"].ast["blocks"]:
            if block.get("t") == "Header" and block["c"][0] == 2:
                category = clean_text(plain(block))
            elif block.get("t") == "Table":
                for body in block["c"][4]:
                    for row in body[3]:
                        cells = row[1]
                        if len(cells) < 3:
                            continue
                        slug = self.result_slug(cells[0][-1])
                        if not slug:
                            continue
                        status_text = plain(cells[2][-1])
                        if "◐" in status_text or "🟡" in status_text or "Partial" in status_text:
                            status = "partial"
                        elif "☑" in status_text or "✅" in status_text or "Formalized" in status_text or "Complete" in status_text:
                            status = "full"
                        elif "☐" in status_text or "⬜" in status_text or "Not formalized" in status_text:
                            status = "none"
                        else:
                            raise ValueError(f"Unrecognized Lean status for {slug}: {status_text!r}")
                        found[slug] = Result(
                            slug, clean_text(plain(cells[0][-1])), category, status,
                            clean_text(plain(cells[1][-1])), cells[1][-1],
                        )
            elif block.get("t") == "BulletList" and "partial" in category.lower():
                for item in block["c"]:
                    slug = self.result_slug(item)
                    if not slug:
                        continue
                    landing = self.documents.get(f"results/{slug}/README.md")
                    if not landing:
                        raise ValueError(f"No landing page for {slug}")
                    source_text = (ROOT / landing.source).read_text()
                    try:
                        status = landing_lean_status(source_text)
                    except ValueError as error:
                        raise ValueError(f"Partial result {slug} needs an explicit Lean status in its README") from error
                    summary_item = json.loads(json.dumps(item))
                    utility_links = {"Local proof", "Frequency proof", "Replay", "Proof", "Reproduce", "Automorphism proof"}
                    for node in nodes(summary_item):
                        if node.get("t") == "Link" and clean_text(plain(node)) in utility_links:
                            node.clear()
                            node.update({"t": "Str", "c": ""})
                    summary = clean_text(plain(summary_item))
                    summary = re.sub(r"(?:\s*·\s*)+$", "", summary)
                    found[slug] = Result(
                        slug, landing.title, PARTIAL_CATEGORIES.get(slug, category), status,
                        summary, scope="partial",
                    )
        landing_slugs = {PurePosixPath(source).parts[1] for source in self.documents if re.fullmatch(r"results/[^/]+/README\.md", source)}
        if set(found) != landing_slugs:
            raise ValueError(f"Catalogue/landing-page mismatch: missing {sorted(landing_slugs - set(found))}, extra {sorted(set(found) - landing_slugs)}")
        self.check_authoritative_statuses(found)
        alias_file = ROOT / "site" / "search-aliases.json"
        aliases = json.loads(alias_file.read_text()) if alias_file.exists() else {}
        if not isinstance(aliases, dict) or any(not isinstance(value, list) or any(not isinstance(alias, str) for alias in value) for value in aliases.values()):
            raise ValueError("Search aliases must map result slugs to arrays of strings")
        unknown_aliases = set(aliases) - set(found)
        if unknown_aliases:
            raise ValueError(f"Search aliases reference unknown results: {sorted(unknown_aliases)}")
        order: list[str] = []
        for node in self.documents["README.md"].ast["blocks"]:
            for link in nodes(node):
                if link.get("t") == "Link":
                    slug = self.result_slug(link)
                    if slug in found and slug not in order:
                        order.append(slug)
        for slug in found:
            if slug not in order:
                order.append(slug)
        for slug in order:
            result = found[slug]
            search_parts = [result.title, result.category, result.summary, slug.replace("-", " ")]
            search_parts.extend(aliases.get(slug, []))
            search_parts.append(result.checked_scope)
            for source, document in self.documents.items():
                if source.startswith(f"results/{slug}/"):
                    search_parts.append(clean_text(plain(document.ast["blocks"])))
            result.search = clean_text(" ".join(search_parts))
        self.results = [found[slug] for slug in order]
        self.result_map = found

    def check_authoritative_statuses(self, results: dict[str, Result]):
        table = next((block for block in self.documents["docs/lean-status.md"].ast["blocks"] if block.get("t") == "Table"), None)
        if table is None:
            raise ValueError("The Lean status report has no summary table")
        checked = set()
        for body in table["c"][4]:
            for row in body[3]:
                cells = row[1]
                label = clean_text(plain(cells[0][-1]))
                slug = next((slug for name, slug in STATUS_LABEL_SLUGS.items() if label == name or label.startswith(name + " (")), None)
                if slug is None or slug not in results:
                    raise ValueError(f"Map the Lean summary label to its result slug: {label!r}")
                if slug in checked:
                    raise ValueError(f"Duplicate authoritative Lean summary row for {slug}")
                text = clean_text(plain(cells[1][-1]))
                status = "full" if text.startswith("Complete") else "partial" if text.startswith("Partial") else "none" if text == "Not formalized" else None
                if status is None:
                    raise ValueError(f"Unknown authoritative Lean status: {label}: {text}")
                if results[slug].status != status:
                    raise ValueError(f"Stale catalogue status for {slug}: {results[slug].status}; docs/lean-status.md says {status}. Reconcile the source indexes before publishing.")
                results[slug].checked_scope = clean_text(plain(cells[2][-1]))
                checked.add(slug)
        required = {slug for slug, result in results.items() if result.scope != "partial"}
        # Partial progress on an open mathematical problem can itself have
        # a partial or complete Lean formalization. Require an authoritative
        # receipt for every formalized claim, without promoting its math scope.
        summary_required = required | {slug for slug, result in results.items() if result.status != "none"}
        if not summary_required <= checked:
            raise ValueError(f"Lean status summary mismatch: missing {sorted(summary_required - checked)}")
        readme_checked = set()
        for block in self.documents["README.md"].ast["blocks"]:
            if block.get("t") != "Table":
                continue
            for body in block["c"][4]:
                for row in body[3]:
                    cells = row[1]
                    slug = self.result_slug(cells[0][-1])
                    if slug not in results:
                        continue
                    if len(cells) != 2:
                        raise ValueError(f"README result row needs two columns: {slug}")
                    text = clean_text(plain(cells[1][-1]))
                    status = {"✅": "full", "🟢": "partial", "🟡": "partial", "⬜": "none"}.get(text)
                    if status != results[slug].status:
                        raise ValueError(f"Stale README Lean status for {slug}: {text!r}; expected {results[slug].status}")
                    readme_checked.add(slug)
        if readme_checked != required:
            raise ValueError(f"README result table does not match current catalogue: {sorted(readme_checked ^ required)}")

    def resolve_link(self, raw: str, source: str, *, image=False) -> str:
        if not raw or raw.startswith(("#", "mailto:", "tel:", "data:", "//")):
            return raw
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc:
            return raw
        path = unquote(parsed.path)
        target = posixpath.normpath(posixpath.join(posixpath.dirname(source), path)) if not path.startswith("/") else path.lstrip("/")
        if target.startswith("../"):
            raise ValueError(f"Source link escapes repository: {source}: {raw}")
        if path.endswith("/") or (ROOT / target).is_dir():
            landing = target.rstrip("/") + "/README.md"
            if landing in self.documents:
                target = landing
        suffix = ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")
        if target in self.documents:
            return self.url(self.documents[target].route) + suffix
        target_path = ROOT / target
        if not target_path.exists():
            # Existing source notes sometimes use repository-root links from
            # nested documents. Accept only a real, unambiguous root target.
            root_target = path.lstrip("/")
            if (ROOT / root_target).exists():
                target, target_path = root_target, ROOT / root_target
                if target in self.documents:
                    return self.url(self.documents[target].route) + suffix
            else:
                raise ValueError(f"Broken source link: {source}: {raw}")
        if target_path.suffix.lower() in {".pdf", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}:
            self.copied_files.add(target)
            return self.url("files/" + quote(target)) + suffix
        kind = "tree" if target_path.is_dir() else "blob"
        return f"{REPOSITORY}/{kind}/main/{quote(target)}" + suffix

    def render_blocks(self, blocks: list, source: str, *, strip_title=False) -> tuple[str, list]:
        ast = json.loads(json.dumps(self.documents[source].ast))
        ast["blocks"] = json.loads(json.dumps(blocks))
        if strip_title and ast["blocks"] and ast["blocks"][0].get("t") == "Header" and ast["blocks"][0]["c"][0] == 1:
            ast["blocks"].pop(0)
        toc = []
        for node in nodes(ast["blocks"]):
            if node.get("t") in {"Link", "Image"}:
                node["c"][2][0] = self.resolve_link(node["c"][2][0], source, image=node["t"] == "Image")
            elif node.get("t") == "Header":
                node["c"][0] = max(2, node["c"][0])
                if node["c"][0] <= 3:
                    toc.append((node["c"][0], node["c"][1][0], clean_text(plain(node))))
            elif node.get("t") == "Math":
                # Pandoc's math reader accepts modern \mathrm, while the
                # source notes also use TeX's equivalent scoped \rm form.
                node["c"][1] = re.sub(r"\{\\rm\s+([^{}]+)\}", lambda match: "{\\mathrm{" + match.group(1) + "}}", node["c"][1])
        rendered = pandoc(["--from", "json", "--to", "html5", "--mathml", "--wrap=none"], text=json.dumps(ast))
        return rendered, toc

    def head(self, title: str, description: str, route: str, *, noindex=False) -> str:
        structured = {
            "@context": "https://schema.org",
            "@type": "CollectionPage" if not route else "WebPage",
            "name": title,
            "description": description,
            "url": self.canonical(route),
            "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": self.base_url},
        }
        if route.startswith("results/"):
            slug = route.split("/")[1]
            if slug in EXTERNAL_CREDIT:
                name, url = EXTERNAL_CREDIT[slug]
                structured["creditText"] = f"Result and proof credited to {name}; original report: {url}"
        json_ld = json.dumps(structured, ensure_ascii=False).replace("<", "\\u003c")
        return f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="theme-color" content="#f7f9f8">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta name="robots" content="{'noindex,follow' if noindex else 'index,follow'}">
<link rel="canonical" href="{escape(self.canonical(route))}">
<meta property="og:type" content="{'website' if not route else 'article'}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{escape(self.canonical(route))}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(description)}">
<link rel="icon" type="image/svg+xml" href="{escape(self.url('assets/favicon.svg'))}">
<link rel="stylesheet" href="{escape(self.url('assets/site.css'))}">
<script type="application/ld+json">{json_ld}</script>
<script src="{escape(self.url('assets/site.js'))}" defer></script>'''

    def shell(self, content: str, *, title: str, description: str, route: str, source: str | None = None, noindex=False, page_class="detail-page") -> str:
        source_link = f'<a href="{REPOSITORY}/blob/main/{quote(source)}">View source</a>' if source else f'<a href="{REPOSITORY}">Source repository</a>'
        revision = f'<a href="{REPOSITORY}/commit/{self.commit}">Source {self.commit[:7]}</a>' if self.commit else ""
        if self.source_dirty:
            revision += '<span class="source-local-note">Local changes</span>'
        return f'''<!doctype html>
<html lang="en">
<head>
{self.head(title, description, route, noindex=noindex)}
</head>
<body class="{page_class}">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="{self.url()}"><img src="{self.url('assets/favicon.svg')}" alt="" width="28" height="28"><span>{SITE_NAME}</span></a>
    <nav class="site-nav" aria-label="Main navigation">
      <a href="{self.url()}">Results</a>
      <a href="{self.url('docs/verification/')}">Verification</a>
      <a href="{self.url('docs/lean-status/')}">Lean status</a>
      <a href="{REPOSITORY}">GitHub</a>
    </nav>
  </div>
</header>
<main id="main" class="container">
{content}
</main>
<footer class="site-footer">
  <div class="container footer-inner">
    <p>Maintained by <a href="https://1337isnot1337.github.io/">Cinna Davis</a>. Research with GPT-6.2 Astra. External contributions are credited individually.</p>
    <nav aria-label="Footer navigation">{source_link}<a href="{self.url('catalogue/#primary-sources')}">Primary sources</a><a href="{self.url('history/')}">History</a>{revision}</nav>
  </div>
</footer>
</body>
</html>
'''

    def save_page(self, route: str, rendered: str, title: str, description: str, source=None, *, lastmod="", noindex=False):
        relative = route + "index.html" if route.endswith("/") or not route else route
        path = self.output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
        self.pages.append({"route": route, "file": relative, "title": title, "description": description, "canonical": self.canonical(route), "source": source, "lastmod": lastmod, "noindex": noindex})

    def build_index(self):
        categories = sorted({result.category for result in self.results})
        options = ''.join(f'<option value="{slugify(category)}">{escape(category)}</option>' for category in categories)
        counts = {status: sum(result.status == status for result in self.results) for status in STATUS_LABELS}
        rows = []
        search_entries = []
        for result in self.results:
            route = f"results/{result.slug}/"
            proof = f"results/{result.slug}/PROOF.md"
            if result.summary_blocks:
                summary, _ = self.render_blocks(result.summary_blocks, "CONTENTS.md")
            else:
                summary = f"<p>{escape(result.summary)}</p>"
            scope_label = '<span class="scope-label">Partial result on an open problem</span>' if result.scope == "partial" else ""
            proof_link = f'<a href="{self.url(self.documents[proof].route)}">Proof</a>' if proof in self.documents else ""
            rows.append(f'''<article class="result-row" data-result="{result.slug}" data-search="{escape(result.search)}" data-category="{slugify(result.category)}" data-status="{result.status}" data-scope="{result.scope}">
  <div class="result-main">
    <div class="result-meta"><span>{escape(result.category)}</span>{scope_label}</div>
    <h2 class="result-title"><a href="{self.url(route)}">{escape(result.title)}</a></h2>
    <div class="result-summary">{summary}</div>
  </div>
  <div class="result-side"><span class="status" data-status="{result.status}">{STATUS_LABELS[result.status]}</span><div class="result-links"><a href="{self.url(route)}">Read result</a>{proof_link}</div></div>
</article>''')
            search_entries.append({"slug": result.slug, "title": result.title, "url": self.url(route), "summary": result.summary, "category": result.category, "status": result.status, "scope": result.scope, "search": result.search})
        intro = "Proofs, counterexamples, and partial results in combinatorics and number theory, with reproducible checks and Lean 4 formalizations."
        content = f'''<section class="intro" aria-labelledby="collection-title">
  <h1 id="collection-title" class="intro-title">Solved conjectures</h1>
  <p class="intro-description">{intro}</p>
  <p class="intro-meta">{len(self.results)} research entries · {counts['full']} stated results formalized in Lean · {counts['partial']} partial formalizations · {counts['none']} not formalized</p>
</section>
<section class="catalogue" aria-label="Research catalogue">
  <form class="catalogue-tools" role="search" method="get" action="{self.url()}">
    <div class="search-field"><label for="search">Search results</label><input type="search" id="search" name="q" placeholder="Problem, author, or OEIS number" autocomplete="off" aria-controls="result-list"></div>
    <div class="filter-field"><label for="category">Subject</label><select id="category" name="category"><option value="">All subjects</option>{options}</select></div>
    <div class="filter-field"><label for="lean-status">Lean status</label><select id="lean-status" name="lean"><option value="">All statuses</option><option value="full">Formalized stated result</option><option value="partial">Partial formalization</option><option value="none">Not formalized</option></select></div>
    <button id="clear-filters" class="clear-filters" type="button">Clear filters</button>
  </form>
  <noscript><style>.catalogue-tools{{display:none}}</style><p class="collection-note">All results are listed below. Search and filters require JavaScript.</p></noscript>
  <div class="catalogue-summary"><p id="results-count" aria-live="polite">{len(self.results)} results</p><a href="{self.url('catalogue/')}">Full catalogue and sources</a></div>
  <div id="result-list" class="result-list">{''.join(rows)}</div>
  <div id="empty-state" class="empty-state" hidden><h2>No matching results</h2><p>Try a shorter search or clear the filters.</p></div>
</section>
<aside class="collection-note"><p>These notes are unrefereed. A Lean status describes the stated result and its documented scope. <a href="{self.url('docs/lean-status/')}">Read the exact formalized statements and remaining dependencies.</a></p></aside>'''
        title = "Solved mathematical conjectures: proofs and Lean 4 formalizations"
        self.save_page("", self.shell(content, title=title, description=intro, route="", source="README.md", page_class="index-page"), title, intro, "README.md", lastmod=self.documents["README.md"].lastmod)
        (self.output / "search.json").write_text(json.dumps(search_entries, ensure_ascii=False, separators=(",", ":")) + "\n")

    def sidebar(self, document: Document, result: Result | None, toc: list) -> str:
        sections = []
        if result:
            items = []
            prefix = f"results/{result.slug}/"
            for filename, label in [("README.md", "Result overview"), ("PROOF.md", "Proof"), ("LEAN.md", "Lean details")]:
                source = prefix + filename
                if source in self.documents:
                    current = ' aria-current="page"' if source == document.source else ""
                    items.append(f'<li><a href="{self.url(self.documents[source].route)}"{current}>{label}</a></li>')
            sections.append('<nav class="article-nav" aria-label="Result pages"><h2>Result</h2><ul>' + ''.join(items) + '</ul></nav>')
            other = [doc for source, doc in self.documents.items() if source.startswith(prefix) and PurePosixPath(source).name not in {"README.md", "PROOF.md", "LEAN.md"}]
            if other:
                items = ''.join(f'<li><a href="{self.url(doc.route)}"{chr(32) + "aria-current=\"page\"" if doc.source == document.source else ""}>{escape(doc.title)}</a></li>' for doc in other)
                sections.append('<nav class="article-nav" aria-label="Supporting notes"><h2>Supporting notes</h2><ul>' + items + '</ul></nav>')
        if toc:
            items = ''.join(f'<li class="toc-level-{level}"><a href="#{escape(anchor)}">{escape(title)}</a></li>' for level, anchor, title in toc)
            sections.append('<nav class="page-toc" aria-label="On this page"><h2>On this page</h2><ul>' + items + '</ul></nav>')
        return '<aside class="article-sidebar">' + ''.join(sections) + '</aside>'

    def build_document(self, document: Document):
        if document.source == "README.md":
            return
        parts = PurePosixPath(document.source).parts
        result = self.result_map.get(parts[1]) if parts[0] == "results" and len(parts) > 1 else None
        body, toc = self.render_blocks(document.ast["blocks"], document.source, strip_title=True)
        display_title = result.title if result and parts[-1] == "README.md" else document.title
        role = ""
        if result and parts[-1] != "README.md":
            role = "Proof" if parts[-1] == "PROOF.md" else "Lean details" if parts[-1] == "LEAN.md" else PurePosixPath(document.source).stem.replace("-", " ").capitalize()
        title = (f"{result.title}: {role}" if result and role else display_title) + f" | {SITE_NAME}"
        if result:
            credit_prefix = f"Proof credited to {EXTERNAL_CREDIT[result.slug][0]}. " if result.slug in EXTERNAL_CREDIT else ""
            scope_prefix = "Partial result on an open problem. " if result.scope == "partial" else ""
            role_prefix = role + ". " if role else ""
            snippet = result.summary
            if result.scope == "partial":
                snippet = re.sub(r"^[^.]+\((?:partial|open)\)\.\s*", "", snippet)
            if result.slug in EXTERNAL_CREDIT:
                snippet = re.sub(r"\s*Credited to @JesterInABarrel\.?\s*$", "", snippet)
            description = excerpt(credit_prefix + scope_prefix + role_prefix + snippet)
            parent = f'<a href="{self.url()}">All results</a><span aria-hidden="true">/</span><a href="{self.url(f"results/{result.slug}/")}">{escape(result.title)}</a>'
            status = f'<p class="article-meta"><span class="status" data-status="{result.status}">{STATUS_LABELS[result.status]}</span><a href="{self.url("docs/lean-status/")}">Exact checked scope</a></p>'
            if result.checked_scope:
                status += f'<details class="scope-details"><summary>What Lean checks</summary><p>{escape(result.checked_scope)}</p></details>'
            scope = '<p class="scope-note">This entry is a partial result on an open problem. It does not claim a solution of the general conjecture.</p>' if result.scope == "partial" else ""
            credit = ""
            if result.slug in EXTERNAL_CREDIT:
                name, url = EXTERNAL_CREDIT[result.slug]
                credit = f'<p class="credit-note">Result and proof credited to <a href="{url}">{name}</a>. This is an external contribution.</p>'
        else:
            description = excerpt(f"{display_title} for the solved-conjectures research collection. Read source statements, reproducible checks, and the precise scope of formalization.")
            parent = f'<a href="{self.url()}">All results</a><span aria-hidden="true">/</span><span>{escape(display_title)}</span>'
            status = scope = credit = ""
        original_heading = next((node["c"][1][0] for node in document.ast["blocks"] if node.get("t") == "Header" and node["c"][0] == 1), "page-title")
        content = f'''<nav class="breadcrumbs" aria-label="Breadcrumb">{parent}</nav>
<header class="article-header"><h1 id="{escape(original_heading)}">{escape(display_title)}</h1>{status}{scope}{credit}</header>
<div class="article-layout">{self.sidebar(document, result, toc)}<article class="prose">{body}</article></div>'''
        rendered = self.shell(content, title=title, description=description, route=document.route, source=document.source)
        self.save_page(document.route, rendered, title, description, document.source, lastmod=document.lastmod)

    def build_404(self):
        title = "Page not found | Solved conjectures"
        description = "Find a result, proof, or verification note in the solved-conjectures catalogue."
        content = f'<section class="intro error-page"><h1>Page not found</h1><p>This address does not match a published page.</p><p><a href="{self.url()}">Browse and search the catalogue</a></p></section>'
        self.save_page("404.html", self.shell(content, title=title, description=description, route="404.html", noindex=True), title, description, noindex=True)

    def write_sitemap(self):
        ns = "http://www.sitemaps.org/schemas/sitemap/0.9"
        ET.register_namespace("", ns)
        root = ET.Element(f"{{{ns}}}urlset")
        for page in sorted(self.pages, key=lambda page: page["route"]):
            if page["noindex"]:
                continue
            node = ET.SubElement(root, f"{{{ns}}}url")
            ET.SubElement(node, f"{{{ns}}}loc").text = page["canonical"]
            if page["lastmod"]:
                ET.SubElement(node, f"{{{ns}}}lastmod").text = page["lastmod"]
        ET.indent(root, space="  ")
        ET.ElementTree(root).write(self.output / "sitemap.xml", encoding="utf-8", xml_declaration=True)

    def build(self):
        if not shutil.which("pandoc"):
            raise RuntimeError("Pandoc 3.x is required. Install pandoc before building the site.")
        if self.output == ROOT or ROOT in self.output.parents and self.output.parts[-1] in {"results", "docs", "scripts", "site", "lean"}:
            raise ValueError("Refusing to use a source directory as the build output")
        self.output.mkdir(parents=True, exist_ok=True)
        # Only remove a previous output bearing this builder's manifest.
        previous_manifest = self.output / "build-manifest.json"
        if previous_manifest.exists() and json.loads(previous_manifest.read_text()).get("source_repository") != REPOSITORY:
            raise ValueError("Output belongs to a different source repository")
        if previous_manifest.exists() or (self.output / ".site-build-in-progress").exists():
            shutil.rmtree(self.output)
            self.output.mkdir(parents=True)
        elif any(self.output.iterdir()):
            raise ValueError(f"Output must be empty or contain a prior build-manifest.json: {self.output}")
        (self.output / ".site-build-in-progress").write_text("solved-conjectures static site build\n")
        self.read_sources()
        self.read_results()
        self.build_index()
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            list(pool.map(self.build_document, self.documents.values()))
        self.build_404()
        shutil.copytree(ROOT / "site" / "assets", self.output / "assets", dirs_exist_ok=True)
        for source in sorted(self.copied_files):
            target = self.output / "files" / source
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / source, target)
        (self.output / ".nojekyll").write_text("")
        self.write_sitemap()
        manifest = {
            "source_repository": REPOSITORY,
            "source_commit": self.commit,
            "source_commit_date": self.commit_date,
            "source_dirty": self.source_dirty,
            "base_url": self.base_url,
            "math_renderer": "Pandoc native MathML",
            "results": [{"slug": result.slug, "title": result.title, "status": result.status, "scope": result.scope, "category": result.category} for result in self.results],
            "pages": sorted(self.pages, key=lambda page: page["route"]),
        }
        (self.output / "build-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        (self.output / ".site-build-in-progress").unlink()
        print(f"Built {len(self.results)} result pages and {len(self.pages)} HTML pages in {self.output}")
        print(f"Canonical site: {self.base_url}")
        print(f"Source commit: {self.commit or 'unavailable'}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    parser.add_argument("--base-url", default=DEFAULT_URL, help="Absolute public site URL including its project path")
    parser.add_argument("--workers", type=int, default=min(8, os.cpu_count() or 2))
    args = parser.parse_args()
    if urlsplit(args.base_url).scheme not in {"http", "https"}:
        parser.error("--base-url must be an absolute HTTP(S) URL")
    if args.workers < 1:
        parser.error("--workers must be positive")
    Builder(args.output, args.base_url, args.workers).build()


if __name__ == "__main__":
    main()

