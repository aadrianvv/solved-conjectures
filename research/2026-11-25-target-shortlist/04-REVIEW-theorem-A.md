# Referee report: Theorem A of 04d

**Reviewed:** [04d-regular-path-matching-relative-theorem.md](04d-regular-path-matching-relative-theorem.md), Sections 1–3, plus the parts of [04-regular-path-decomposition.md](04-regular-path-decomposition.md) they reuse, and [check_regular_path_sweep_pipeline.py](check_regular_path_sweep_pipeline.py). Section 4 (diamond-free case) was not in scope.
**Reviewer role:** an independent, adversarial referee. I rederived each step and wrote my own checker, [check_regular_path_theoremA_independent.py](check_regular_path_theoremA_independent.py), from the written text only. It does not import the author's code.
**Date:** 2026-11-25.

## Verdict: ACCEPT WITH FIXES

I found no fatal or major mathematical error in the proof of Theorem A. Every existence claim, every case of Lemma 3, facts (o1)–(o5), the pair replacement, Lemma 4 and the odd-cycle completion check out line by line. The finite enumeration is complete for constraints (o1)–(o5), and both my independent enumeration and my end-to-end tests agree with it. The fixes below are about exposition, a vacuous branch, a mismatch between the text and the author's code, and an **unfinished novelty gate**. The FGK full text still has not been read, by the author or by me, so the result is not ready for publication as a new theorem until that is done.

## 1. Line-by-line check of the proof

### Definitions

An \(M\)-triangle has exactly one \(M\)-edge, automatically, because \(M\) is a matching. An \(M\)-square has exactly one \(M\)-edge, and a bad pair is a triangle–square pair sharing an edge. The definitions are consistent with their use in the proof. Every exceptional case the proof excludes does yield such a pair.

### Lemma 1: correct

- The prescribed pairs at \(w\) are disjoint because each \(x\) has one mate, so a pairing of the four \(H\)-edges exists.
- The split graph is 2-regular and simple: two parallel edges would need two edges \(wx\). Orienting its cycles gives an Eulerian orientation in which each pair has one in-arc and one out-arc.
- The out-copy/in-copy bipartite graph is 2-regular, so it splits into two perfect matchings. Hence \(r,s\) are permutations and (P1) holds, since \(R,S\) each have \(n\) arcs and together they account for all \(2n=|E(H)|\) edges.
- (P2) holds because a 2-cycle would orient one edge both ways. (P3) holds because the arcs \(u\to w\) (P1) and \(v\to w\) (P2) both enter \(w\), although \(wu,wv\) is a prescribed pair.
- The listed consequences, including \(r(v)\ne s(v)\), \(s(r(v))\ne v\) and \(r(s(v))\ne v\), each follow from disjointness of \(M,R,S\).

### Lemma 2: correct

I checked all 15 position pairs of \(\tau(uv)\). Of the cross-arm pairs, (0,3) and (2,5) are excluded by (P3), (1,4) by injectivity of \(r\), and (0,5) by injectivity of \(s\circ r\). Pairs (1,3) and (2,4) are excluded by \(r(v)\ne m(v)\), and pairs (0,2) and (3,5) by \(s(r(v))\ne v\). That leaves (0,4) and (1,5), which cannot both hold by (P2). In the defective labelling, \(a\ne e\) holds by (P2), and \((b,c,d,e)\) is an \(M\)-square with edges \(R,M,R,S\).

### Sweep: correct

- The target is \(\tau(f\,m(f))\) with \(f=r^{-1}(c)\ne c,d\), so the target is never \(T\).
- Type-2 in-degree is at most 1, since the source must contain \(e'\) as its \(c\)-label. The type-2 links therefore form paths and cycles of length at least 2.
- Under the alternating source choice, every non-source outside an odd cycle has a source predecessor, and no source has a source predecessor.
- A defective trail receives at most one type-1 input (from the trail containing \(b'\)) and at most one type-2 input. The two inputs take different \(S\)-edges, \(\{b',a'\}\) and \(\{e',b'\}\).
- Given edges are distinct \(R\)-edges \(\{c,r(c)\}\), and taken edges are distinct \(S\)-edges \(\{c,s(c)\}\). The trade table is correct. I rederived each new sequence from the edge lists.

### Lemma 3: correct, all cases

**Source piece \((A,b,e,d,c,x)\).**
- \(A=a\) avoids \(b\), \(c\) (by \(R\cap S=\emptyset\)), \(e\) (by (P2)) and \(d\) (by (P3)).
- \(A=r(b)\) avoids \(b\), \(c\) (by (P2)) and \(e\) (by injectivity). It can equal \(d\), which gives the bad pair \(bcd\)/\((b,c,d,e)\).
- \(x=s(c)\) avoids \(b=s(e)\), \(d\) and \(c\). It can equal \(e\), which gives the bad pair \(cde\).
- \(s(c)\ne a\) by injectivity of \(s\).
- I traced the subtle endpoint case \(s(c)=r(b)\). It gives \(c=e''\), so \(T\to T''\) is type 2 out of a source, contradicting the trade of \(T''\). The argument is correct.
- A mutual type-1 pair, with \(c=b'\) and \(c'=b\), would make \(r(b)=c\), a 2-cycle. So it cannot arise.

**Recipient piece \((A,b,c,d,e,r(e))\).**
- \(r(e)\) avoids \(e\), \(d\) (by (P2)) and \(b\) (by injectivity). It can equal \(c\), which gives a bad pair.
- \(r(e)=b''\) is a canonical terminal of \(T''\ne T\), so it differs from \(a\). If \(A=r(b)\), injectivity separates the two ends.

**Type-0 target \((b,c,f,g,h,y)\).**
- \(b\) avoids \(c\), \(f\) (by (P2)) and \(h\). The case \(b=h\) forces \(f=d\), which contradicts \(r(d)=e\).
- \(b\) avoids \(y\), since \(b=y\) forces \(h=e\), \(g=d\) and \(f=c\).
- \(b=g\) gives the bad pair \(bcf\).
- Opposite-end receipt: \(b\ne\tilde b\). The exception is \(\tilde b=f\). The case \(\tilde b=x\) forces \(\tilde c=g\), a contradiction.

One remark. The first bullet of Lemma 3 says that a source or recipient "can have \(A=d\)". This is possible **only for a changed pendant** \(A=r(b)\), because an unchanged \(a=s(r(c))\ne m(c)\) by (P3). This is issue m1 below.

### Section 3: correct

**(o1)–(o3) and (o5)** are each correctly justified. In (o3), \(d_i=b_{i+1}=s(c_i)\) would put \(c_id_i\) in \(S\), and \(d_i=b_{i-1}=r(e_i)\) would create an \(r\) 2-cycle.

**(o4)** is correctly justified, with one wording issue. The unchanged case \(b_i=e_j\) is excluded by injectivity of \(r\) (\(c_i\ne d_j\)), or equivalently by (o2) since \(e_j=c_{j-1}\). It is not excluded by "(o1)", as the text says. In the changed case, \(b_i\) is a matching endpoint of the external source. This excludes \(r(b_i)\in\{b_j\}\cup\{e_j\}=\{b_j\}\cup\{c_j\}\).

**Pair replacement.** I rederived both pieces. The ten edges are re-partitioned. In the first piece, \(b_{i+1}\) avoids \(b_i\), \(e_i\), \(c_i\) and \(d_i\) by (o1), (o2), (o2) and (o3). In the second piece, \(b_i\) avoids \(d_{i+1}\) by (o3). The only remaining equalities are \(A_i=d_i\) and \(A_{i+1}=d_{i+1}\), which are bad chords.

**Odd-cycle completion.** \(\varphi\) is well defined by (o5) and injective by (o1). A step of \(+1\) at \(i\) forces \(+1\) at \(i+2\), and \(i\mapsto i+2\) is transitive for odd \(L\). Both rotations re-partition the edges. I checked simplicity directly:
- \(+1\) rotation: \(d_{i-1}\ne b_i,b_{i-2}\) by (o3), and \(d_{i+1}\ne d_{i-1}\) for \(L\ge3\).
- \(-1\) rotation: \(d_{i+1}\ne b_i,b_{i+2}\) by (o3).

The "vertex inequality" \(A_i\ne b_{i-2}\) holds by (o4).

**Lemma 4 enumeration.** It is complete for (o1)–(o5). The local labels are the five per-trail roles. The only identifications that (o1)–(o5) permit among non-pendant labels are \(e_0=c_2\) (\(L=3\)) and, for \(L\ge5\), \(d_0=b_2\) and/or \(d_2=b_0\). A pendant ranges over the fresh label or the present non-\(b\) labels other than its own \(c_i,e_i\). The changed/unchanged restrictions are exactly the ones the proof justifies. The 15-distinct-edges filter is sound, since real trails are edge-disjoint. The local exclusion test is implied by the global hypothesis, because the three squares are genuine \(M\)-squares and any local triangle on \(c_id_i\) is a genuine \(M\)-triangle. The author's code enumerates exactly this set; I read `verify_odd_triples` against the list above.

### Final assembly

Every piece is a 6-vertex sequence along edges of \(G\). The pieces partition \(E(G)\), since trades move each edge once and the odd-cycle replacements re-partition each cycle's edges. Under the hypothesis, every piece is simple. **Theorem A follows.**

### Corollaries

1. No 4-cycle implies no \(M\)-square.
2. Triangle-free implies no \(M\)-triangle.
3. No triangle sharing an edge with any 4-cycle implies no bad pair.
4. No \(M\)-edge in a triangle implies no \(M\)-triangle.

All four implications are immediate. I rebuilt the 408-vertex example in the scratch script [review_408_example.py](04-handoff/review-theoremA/review_408_example.py). It has 0 \(M\)-triangles, 136 \(M\)-square incidences in my count and no bad pair, and 20 random constructions all gave verified decompositions.

## 2. Issues

| # | Location | Severity | Issue and fix |
|---|---|---|---|
| M1 | 04d "Self-review: Novelty"; 04 "Source and eligibility" | **major (publication gate, not mathematical)** | The FGK 2010 full text has not been read. Its abstract defines \(M\)-triangles, \(M\)-squares, "bad pairs of \(M\)-cycles" and "balanced" \(M\)-triangles and \(M\)-squares, which is exactly Theorem A's vocabulary. Theorems 6–7 are known only second-hand. A theorem of the form "no bad pair implies a decomposition" in FGK would make Theorem A, or Corollary 1-style special cases, prior work. Every secondary source I found (Botler–Hoffmann 2022, BMW Eurocomb 2015, DMGT 2022, and the abstracts of CFHZ 2024 and Montgomery et al.) credits FGK only with the \(C_4\)-free degree-five case and \(M\)-centred extendability. That is suggestive but not a certificate. **Fix: obtain the FGK PDF through a library or the authors and record the exact statements of Theorems 6–7 and their definition of a bad pair before promotion.** |
| m1 | Lemma 3, bullet 1 | minor | "A source or a recipient can have \(A=d\)" holds only when \(A=r(b)\) is changed. For \(A=a\), (P3) excludes it. State this. |
| m2 | Section 3, odd-cycle completion and Lemma 4 | minor (simplification) | Under the hypothesis, \(A_i=d_{i-1}\) **always** gives a bad pair, changed or not. Since \(b_i=s(e_i)=s(c_{i-1})\), the chord \(b_id_{i-1}\) closes the \(M\)-triangle \(b_ic_{i-1}d_{i-1}\), which shares \(c_{i-1}d_{i-1}\) with the square of \(T_{i-1}\). So the \(-1\) rotation is vacuous, and the Lemma 4 exception is exactly \(d_1=A_0\). My enumeration confirms that all 12 failures have \(d_1=A_0\), and planted \(A_i=d_{i-1}\) instances never satisfy the hypothesis. This is harmless, but the text could say it. |
| m3 | Section 3, (o4) | minor | "contrary to (o1) and (o2) applied to red heads" should read "\(b_i=r(c_i)=r(d_j)=e_j\) would give \(c_i=d_j\)", or should cite (o2) directly via \(e_j=c_{j-1}\). |
| m4 | Lemma 4 statement | minor | "\(d_0=b_2\) or \(d_2=b_0\)" should be "and/or". The code also enumerates both together. |
| m5 | Section 2, last sentence before "Trades" | minor | "Every remaining defective trail is a recipient" should read "every remaining **non-source** defective trail". |
| m6 | `check_regular_path_sweep_pipeline.py`, `sweep()` odd-cycle branch vs. 04d Section 3 | minor (checker/text discrepancy) | The code does not implement the written completion. It always uses block (0,1,2) and calls `solve_cluster(..., require_simple=False)`, which accepts triangle pieces and may return a triangle cover even when a simple one exists. It never searches other blocks and never applies the rotations. |
| m7 | 04d "Verification" | minor (evidence overstated) | In the author's default run (which I reran), **no hypothesis-satisfying run contained an odd type-2 cycle**. The 8 odd cycles occurred only in "small" runs, and none of those 30,000 runs satisfied the hypothesis. Only `far3` (300 runs, no \(M\)-triangle) and 9 `k5` runs satisfied it, and the `random`, `square`, `dense` and `small` families had 0. So the author's end-to-end runs give no evidence for Section 3 or for \(M\)-triangle-rich inputs. The proof does not rely on them, but the Verification paragraph should say so. My checker now supplies that evidence (Section 3 below). |
| m8 | 04d Statement, closing paragraph | minor | The clause about "dense clusters such as \(K_4\) or \(K_6\) minus a perfect matching" is vague. Either give a precise example graph in which every perfect matching has a bad pair, or drop it. |

No fatal issues were found.

## 3. Reruns and independent checks

**Author's checker** (`python check_regular_path_sweep_pipeline.py`, Python 3.12) passed in about 92 s. Lemma 4 gave the following counts:

| Family | Excluded | Closed covers | Open covers | Open failures with \(d_1\in\{A_0,A_2\}\) |
|---|---:|---:|---:|---:|
| Bad-pair hypothesis | 766 | 125 | 386 | 12 |
| Diamond-free | 442 | 259 | 564 | 24 |

The log is in `04-handoff/review-theoremA/author_pipeline_run.txt`.

**My checker** (`check_regular_path_theoremA_independent.py`) has three parts.

1. **My own Lemma 4 enumeration**, built from (o1)–(o5) as stated in the text, with my own exact cover. It reproduces the counts exactly: 766 excluded, 125 closed covers, 386 open covers and 12 open failures. It finds no closed failure, and every failure has \(d_1=A_0\).
2. **Graph families with a hypothesis-satisfying matching.** The families are the square of a cycle, circulants, octahedra and \(K_5\) blocks with switches, line graphs of cubic graphs, and random graphs. A local search over perfect matchings of \(G\) removes bad pairs, and about 65% of runs bias the search toward many \(M\)-triangles. The script then runs my own Lemma 1 construction with random pairings, orientations and factor phases, followed by the sweep, and verifies an exact partition into simple 5-edge paths.
3. **Generic \((M,r,s)\) data satisfying only (P1)–(P3).** The sweep and Section 3 use nothing else, so this is a strictly broader test. The script plants odd type-2 cycles of length 3, 5, 7 and 9, with unchanged pendants, planted type-1 sources, and forced rotation patterns \(A_i=d_{i\pm1}\). A swap search removes bad pairs while keeping the planting. Every block of every odd cycle is also checked against Lemma 4's claim, and every uniform rotation pattern is verified directly.

The scratch script [review_small_orders.py](04-handoff/review-theoremA/review_small_orders.py) ran **all** perfect matchings of random 5-regular graphs of orders 8–14, plus 40 random matchings each at order 16. It found 68 hypothesis matchings, all verified, 34 of them with \(M\)-triangles. A further 2,000 small generic instances are included in the full run.

Results of the full run (`--seed 7`) are below; the log is in `04-handoff/review-theoremA/indep_full.txt`.

The full run took 11 min 20 s and ended with `ALL CHECKS PASSED`.

| Part | Runs | Hypothesis holds | Verified P5 decompositions | Notes |
|---|---:|---:|---:|---|
| Graph families: 287 graphs, 10 constructions each | 2,870 | 2,870 | 2,870 | 2,180 square defects and 131 type-1 trades. Only 7 graphs had \(M\)-triangles, and only 1 odd cycle arose. |
| Planted odd type-2 cycles, \(L=3,5,7,9\) | 2,219 | 1,600 | 1,600 | 2,219 odd cycles. 1,922 \(M\)-triangles occurred across the hypothesis runs. The rotation branch ran 742 times, 616 of them in the \(A_i=d_{i+1}\) patterns, which satisfy the hypothesis in about 80% of runs. |
| Generic small \((M,r,s)\), orders 10–30 | 1,950 | 1,348 | 1,348 | 468 \(M\)-triangles occurred across the hypothesis runs. |

Across all planted blocks, Lemma 4 held whenever it was tested on a real block. 6,099 blocks had a cover, 5,858 failed with \(d_1\in\{A_0,A_2\}\), and **0** failed in any other way. **No** closed block failed. Every one of the 1,010 uniform rotation patterns re-partitioned the edges into simple paths. The planted patterns with \(A_i=d_{i-1}\), changed or unchanged, satisfied the hypothesis in **0** of 206 runs, which confirms m2.

One caveat applies to coverage. My graph-family local search rarely found hypothesis-satisfying matchings that contain \(M\)-triangles. The \(M\)-triangle-rich and odd-cycle coverage comes from the generic and planted \((M,r,s)\) instances and the small-order exhaustive-matching runs. That data satisfies only (P1)–(P3), which is exactly what Sections 2–3 use. Lemma 1 itself was tested on every graph-family instance by checking (P1)–(P3) directly.

**No discrepancy was found between the written proof and an implementation written from it.** Every hypothesis-satisfying instance produced a verified P5-decomposition. In particular, Lemma 4's realized blocks never failed outside the stated exception, and the rotation branch was exercised and correct.

## 4. Novelty search (bounded)

- **FGK 2010** (doi:10.1002/jgt.20413). The full text was **not obtained**. Academia.edu returned 403, the publisher is paywalled, Semantic Scholar lists no open-access PDF, and HAL has no copy. The abstract snippet, seen through an aggregator, confirms that FGK define \(M\)-triangles, \(M\)-squares and bad pairs of \(M\)-cycles, and that it states the \(C_4\)-free extendability theorem. All secondary descriptions of FGK give only the \(C_4\)-free theorem and the conjecture: Botler–Hoffmann ([arXiv:2012.05145](https://arxiv.org/abs/2012.05145)), BMW at Eurocomb 2015 ([ENDM abstract](https://eurocomb2015.w.uib.no/files/2015/08/endm1963.pdf)), and DMGT 42 (2022), the 10-regular paper. This leaves issue M1 open.
- **Chu–Fan–Hong–Zhou 2024** (Sci. Sin. Math. 54(11) 1787–1794, doi:10.1360/SSM-2023-0316). The SciEngine PDF returned "Bandwidth Limit Exceeded". The abstract, via a search index, states the graph-level hypothesis that 3-cycles and 4-cycles share no edge. Nothing indicates a matching-relative statement.
- **Papers citing FGK or CFHZ, 2024–2026.** The Semantic Scholar citation list shows only Montgomery–Müyesser–Pokrovskiy–Sudakov ([arXiv:2406.02514](https://arxiv.org/abs/2406.02514)) after 2022. That paper is approximate and treats FGK as open. Web searches for 2025–2026 P5-decomposition results on 5-regular graphs found nothing new.
- **Conclusion.** I found no source stating Theorem A or Corollary 4. Novelty is plausible but **unconfirmed** until the FGK text is read.
