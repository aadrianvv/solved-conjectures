"""End-to-end evidence for Theorem C (04g): (P1)-(P3)+(P5) => decomposition.

For random 5-regular graphs with a perfect matching M, find (r,s) with (P1)-(P3) and (P5)
by the CSP of 04-handoff/p5_scratch/p5solve.py, then apply the first sweep (04d) and the X2
second sweep of 04g §3 exactly as written (D-rule, D-pendant, absorption, Gamma_D, rule F,
D-chain alternation, D-rotation), and verify the result exactly.  Evidence only.
"""

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from random import Random

sys.path.insert(0, "04-handoff/p5_scratch")
from p5solve import solve as p5solve                               # noqa: E402
from check_regular_path_sweep_pipeline import (                     # noqa: E402
    random_matched_graph, solve_cluster, verify, kind)


class Fail(Exception):
    pass


def decompose(adj, mate, r, s, stats):
    n = len(adj)
    rinv = {v: u for u, v in r.items()}
    key = {}
    canon = {}
    for u in range(n):
        v = mate[u]
        if u < v:
            k = (u, v)
            key[u] = key[v] = k
            canon[k] = (s[r[u]], r[u], u, v, r[v], s[r[v]])
    defect = {}
    for k, t in canon.items():
        if kind(t) == "square":
            o = t if t[1] == t[5] else t[::-1]
            defect[k] = o                       # (a,b,c,d,e,b)
    lab = {k: dict(zip("abcde", t[:5])) for k, t in defect.items()}
    # links
    target, link = {}, {}
    for k, L in lab.items():
        tk = key[rinv[L["c"]]]
        target[k] = tk
        if tk in defect:
            link[k] = 1 if lab[tk]["b"] == L["c"] else 2
            assert link[k] == 1 or lab[tk]["e"] == L["c"]
        else:
            link[k] = 0
    succ = {k: target[k] for k in defect if link[k] == 2}
    pred = {t: k for k, t in succ.items()}
    sources, oddcycles, seen = set(), [], set()
    for k in defect:
        if k in seen:
            continue
        st, here = k, {k}
        while st in pred and pred[st] not in here:
            st = pred[st]; here.add(st)
        if st in pred:
            cyc = [st]; x = succ[st]
            while x != st:
                cyc.append(x); x = succ[x]
            seen.update(cyc)
            if len(cyc) % 2 == 0:
                sources.update(cyc[0::2])
            else:
                oddcycles.append(cyc)
        else:
            ch = [st]; x = st
            while x in succ:
                x = succ[x]; ch.append(x)
            seen.update(ch)
            sources.update(ch[0::2])
    in_odd = {k for c in oddcycles for k in c}
    recipients = {k for k in defect if k not in sources and k not in in_odd}
    # X2 sources
    X2 = {k for k in sources if s[lab[k]["c"]] == lab[k]["e"]}
    for k in X2:
        assert link[k] != 2, "X2 with a type-2 link"
    part = {}
    for k in X2:
        d = lab[k]["d"]
        W = key[rinv[d]]
        if W not in defect:
            part[k] = ("alpha", W)
        elif lab[W]["b"] == d:
            part[k] = ("beta", W)
        else:
            assert lab[W]["e"] == d
            part[k] = ("gamma", W)
    # D-chain graph and its resolution
    dnext = {k: W for k, (cs, W) in part.items() if cs == "gamma" and W in X2}
    dprev = {W: k for k, W in dnext.items()}
    assert len(dprev) == len(dnext)
    cancelled, rotation, dseen = set(), set(), set()
    for k in dnext:
        if k in dseen:
            continue
        st, here = k, {k}
        while st in dprev and dprev[st] not in here:
            st = dprev[st]; here.add(st)
        if st in dprev:                              # cycle: D-rotation
            cyc = [st]; x = dnext[st]
            while x != st:
                cyc.append(x); x = dnext[x]
            dseen.update(cyc); rotation.update(cyc)
            stats["D-cycles"] += 1
        else:
            ch = [st]; x = st
            while x in dnext:
                x = dnext[x]; ch.append(x)
            dseen.update(ch)
            cancelled.update(ch[1::2])
            stats["D-paths"] += 1
    existing = X2 - cancelled
    # decide rules of existing X2 and which trades are removed
    rule, removed = {}, set(cancelled)
    for k in existing:
        cs, W = part[k]
        if k in rotation:
            rule[k] = "rot"
        elif cs != "gamma":
            rule[k] = cs
        elif W in cancelled:
            rule[k] = "absorb"
        else:
            assert W in sources, "gamma partner not a source"
            if link[W] in (0, 1):
                rule[k] = "absorb"; removed.add(W)
            else:
                mu = lab[W]["c"]
                rule[k] = "F" if s[mu] == lab[k]["c"] else "GammaD"
        stats["rule " + rule[k]] += 1
    active = sources - removed
    # first-sweep pieces with the active trades
    act_c = {lab[k]["c"]: k for k in active}
    pieces = {}
    for k, t in canon.items():
        if k in defect:
            L = lab[k]
            b = L["b"]
            A = r[b] if b in act_c and link[act_c[b]] == 1 and target[act_c[b]] == k else s[b]
            if k in active:
                pieces[k] = [A, b, L["e"], L["d"], L["c"], s[L["c"]]]
            elif k in recipients:
                pieces[k] = [A, b, L["c"], L["d"], L["e"], r[L["e"]]]
            else:
                pieces[k] = [A, b, L["c"], L["d"], L["e"], b]     # odd cycle or untraded
        else:
            p = list(t)
            for end in (1, 4):
                x = p[end]
                if x in act_c and link[act_c[x]] == 0 and target[act_c[x]] == k:
                    p[0 if end == 1 else 5] = r[x]
            pieces[k] = p
    # D-pendants (case beta), applied before odd cycles
    for k in existing:
        if rule[k] == "beta":
            W = part[k][1]; d = lab[k]["d"]
            p = pieces[W]
            assert p[1] == d and p[0] == s[d]
            p[0] = lab[k]["e"]
    # odd type-2 cycles (04d Section 3)
    out = []
    for cyc in oddcycles:
        L = len(cyc)
        T = [(pieces[k][0], lab[k]["b"], lab[k]["c"], lab[k]["d"], lab[k]["e"]) for k in cyc]
        done = False
        for st in range(L):
            idx = [(st + i) % L for i in range(3)]
            tri = [(T[i][0], T[i][1], T[i][2], T[i][3], T[i][4], T[i][1]) for i in idx]
            sol = solve_cluster(tri, require_simple=True)
            if sol is not None:
                out.extend(sol)
                for i in range(3, L, 2):
                    a, b = T[(st + i) % L], T[(st + i + 1) % L]
                    out.append((a[0], a[1], a[4], a[3], a[2], b[1]))
                    out.append((b[0], b[1], b[2], b[3], a[2], a[1]))
                done = True
                stats["odd cycle block"] += 1
                break
        if not done:
            raise Fail("odd cycle needs rotation (not implemented here)")
        for k in cyc:
            del pieces[k]
    # X2 rules
    for k in existing:
        Lb = lab[k]; A = pieces[k][0]
        a, b, c, d, e = (Lb[x] for x in "abcde")
        cs, W = part[k]
        if rule[k] == "rot":
            continue
        if rule[k] in ("alpha", "beta"):
            pieces[k] = [s[d], d, c, e, b, A]
            if rule[k] == "alpha":
                p = pieces[W]
                if p[1] == d:
                    assert p[0] == s[d]; p[0] = e
                else:
                    assert p[4] == d and p[5] == s[d]; p[5] = e
        elif rule[k] == "absorb":
            u = s[d]
            LW = lab[W]; A2 = pieces[W][0]
            assert LW["b"] == u and LW["e"] == d
            pieces[k] = [u, d, c, e, b, A]
            pieces[W] = [A2, u, LW["c"], LW["d"], d, e]
        else:
            u = s[d]; LW = lab[W]; A2 = pieces[W][0]
            mu, dl = LW["c"], LW["d"]
            assert pieces[W][1:5] == [u, d, dl, mu]
            if rule[k] == "GammaD":
                pieces[k] = [s[mu], mu, dl, d, c, e]
                pieces[W] = [A, b, e, d, u, A2]
            else:
                X = target[W]; LX = lab[X]
                f, dX = LX["c"], LX["d"]
                assert X == target[k] and LX["b"] == c and LX["e"] == mu
                assert pieces[X] == [b, c, f, dX, mu, u]
                pieces[k] = [A, b, c, d, u, A2]
                pieces[W] = [b, e, d, dl, mu, c]
                pieces[X] = [e, c, f, dX, mu, u]
    for k in rotation:
        Lb = lab[k]
        W = part[k][1]
        pieces[k] = [pieces[k][0], Lb["b"], Lb["e"], Lb["c"], Lb["d"], lab[W]["d"]]
    out.extend(tuple(p) for p in pieces.values())
    return [("x", p) for p in out]


def generic_instance(n, rng, steps=5000):
    """Generic (M, r, s) with (P1)-(P3) and (P5) on a simple graph (no 5-regular graph is
    fixed in advance: the graph is whatever M, R, S span).  Annealing rewards defects, X2
    configurations and gamma-partners.  Returns (adj, mate, r, s) or None."""
    import math
    perm = list(range(n)); rng.shuffle(perm)
    m = {}
    for i in range(0, n, 2):
        m[perm[i]], m[perm[i + 1]] = perm[i + 1], perm[i]
    r = list(range(n)); rng.shuffle(r)
    sv = list(range(n)); rng.shuffle(sv)

    def score():
        bad = 0
        E = Counter()
        for v in range(n):
            if r[v] == v or sv[v] == v:
                bad += 1
            E[frozenset((v, r[v]))] += 1
            E[frozenset((v, sv[v]))] += 1
            if v < m[v]:
                E[frozenset((v, m[v]))] += 1
        bad += sum(c - 1 for c in E.values() if c > 1)
        rinv = [0] * n
        for v in range(n):
            rinv[r[v]] = v
        for u in range(n):
            if sv[r[u]] == m[u]:
                bad += 1                       # (P3)
            if m[rinv[u]] == r[u]:
                bad += 1                       # (P5)
        good = 0
        for c in range(n):
            d = m[c]
            if sv[r[d]] == r[c]:               # defect (a,b,c,d,e,b) with this c
                good += 1
                e = r[d]
                if sv[c] == e:                 # X2
                    good += 2
                    dl = rinv[d]; mu = m[dl]
                    if sv[d] == r[mu]:         # gamma partner
                        good += 3
        return bad, good

    bad, good = score()
    T = 2.0
    for it in range(steps):
        arr = r if rng.random() < 0.5 else sv
        x, y = rng.randrange(n), rng.randrange(n)
        arr[x], arr[y] = arr[y], arr[x]
        nb, ng = score()
        delta = (nb - bad) * 10 - (ng - good)
        if delta <= 0 or rng.random() < math.exp(-delta / T):
            bad, good = nb, ng
        else:
            arr[x], arr[y] = arr[y], arr[x]
        T = max(0.05, T * 0.999)
    if bad:
        return None
    adj = [set() for _ in range(n)]
    for v in range(n):
        for w in (r[v], sv[v], m[v]):
            adj[v].add(w); adj[w].add(v)
    if any(len(a) != 5 for a in adj):
        return None
    rr = {v: r[v] for v in range(n)}
    ss = {v: sv[v] for v in range(n)}
    return adj, m, rr, ss


def main_generic(count, seed):
    rng = Random(seed)
    stats = Counter()
    for _ in range(count):
        n = rng.choice([12, 14, 16, 18, 20, 24])
        g = generic_instance(n, rng)
        if g is None:
            stats["annealing failed"] += 1
            continue
        adj, mate, r, s = g
        try:
            out = decompose(adj, mate, r, s, stats)
        except Fail as ex:
            stats["skipped: " + str(ex)] += 1; continue
        kinds = verify(adj, mate, out)
        if kinds["triangle"]:
            raise SystemExit(f"non-path piece left: {adj} {mate} {r} {s}")
        stats["verified generic decompositions"] += 1
    for k in sorted(stats):
        print(k, stats[k])


def main():
    if "--generic" in sys.argv:
        i = sys.argv.index("--generic")
        main_generic(int(sys.argv[i + 1]), int(sys.argv[i + 2]) if len(sys.argv) > i + 2 else 1)
        return
    ap = ArgumentParser()
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--graphs", type=int, default=20)
    ap.add_argument("--orders", type=int, nargs="*", default=[12, 16, 20, 30, 40])
    args = ap.parse_args()
    rng = Random(args.seed)
    stats = Counter()
    for style in ("square", "dense", "k5", "random"):
        for n in args.orders:
            if style == "k5" and n % 10:
                continue
            for _ in range(args.graphs):
                adj, mate = random_matched_graph(n, rng, style)
                try:
                    res = p5solve(adj, mate, rng=rng, node_limit=300000)
                except TimeoutError:
                    stats["P5 timeout"] += 1; continue
                if res is None:
                    stats["P5 infeasible for this M"] += 1; continue
                r, s = res
                try:
                    out = decompose(adj, mate, r, s, stats)
                except Fail as ex:
                    stats["skipped: " + str(ex)] += 1; continue
                kinds = verify(adj, mate, out)
                if kinds["triangle"]:
                    raise SystemExit(f"non-path piece left: {adj} {mate} {r} {s}")
                stats["verified decompositions"] += 1
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()
