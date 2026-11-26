"""Independent referee checker for Theorem B' (04g-regular-path-p5-and-m-diamond.md, section 2).

Theorem B': G finite simple 5-regular with a perfect matching M such that no diamond of G
contains an edge of M (as a side or as the chord).  Then E(G) partitions into P5's.

This checker imports nothing from 04g (check_regular_path_mdiamond.py is not used).  It reuses
  * the audited Lemma 1 construction, (P1)-(P3) check, path cover and first sweep of the
    Theorem A referee (check_regular_path_theoremA_independent.py);
  * the full first+second sweep `procedure` and the planting routine of the Theorem B referee
    (check_regular_path_theoremB_independent.py), which assert the intermediate claims of 04e;
  * the audited label engine and the unchanged 04e windows (check_regular_path_label_engine.py,
    check_regular_path_gsweep.py), with the engine's diamond axiom switched OFF and replaced by
    this file's own M-diamond test (a different algorithm from 04g's MState).

Parts (all run by default; select with --parts):
  lemma4   own enumeration of Lemma 4 / Lemma 4' with the local hypothesis "no local diamond
           through a known M-edge"; also lists the cases where full diamond-freeness and the
           M-diamond hypothesis differ.
  exact    on the small 04e windows: own incremental M-diamond filter == unpatched engine +
           brute-force global post-filter (identical identification sets).
  windows  all 04e windows W1-W8 rerun with the own M-diamond filter.
  graphs   5-regular graphs with many diamonds avoiding M (annealed from C_n(a,b)+M and from
           K5-blocks+M), several Lemma 1 constructions each: Proposition B' (first-sweep
           defects are only G-configurations) and the full procedure, exact verification.
  planted  generic (M,r,s) data with (P1)-(P3) + M-diamond hypothesis, planted G-configurations
           of every case (Theorem B referee's planter) plus planted non-M diamonds near them.
  control  the same generators with the hypothesis switched off (M may lie in diamonds), to
           show the end-to-end check is sensitive.
Random runs are evidence, not proof.

Usage: python -B check_regular_path_theoremBprime_independent.py [--quick] [--seed N] [--parts ...]
"""

import sys
import time
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import combinations, product
from random import Random

from check_regular_path_theoremA_independent import lemma1, check_P, path_cover
from check_regular_path_theoremA_independent import sweep as first_sweep, SweepFailure
from check_regular_path_theoremB_independent import procedure, Failure, plant_random


def E(u, v):
    return (u, v) if u < v else (v, u)


def edges_of(seq):
    return [E(seq[i], seq[i + 1]) for i in range(len(seq) - 1)]


# ----------------------------------------------------------------------------------------
# hypothesis predicates (own code)

def diamond_stats(adj, m):
    """(#diamonds through an M-edge, #diamonds avoiding M, #triangles through an M-edge).
    A diamond is counted by its chord xy and the pair of common neighbours {z1, z2}."""
    md = nd = 0
    for x in adj:
        for y in adj[x]:
            if x > y:
                continue
            com = adj[x] & adj[y]
            for z1, z2 in combinations(sorted(com), 2):
                es = ((x, y), (x, z1), (y, z1), (x, z2), (y, z2))
                if any(m.get(a) == b for a, b in es):
                    md += 1
                else:
                    nd += 1
    mt = sum(len(adj[x] & adj[m[x]]) for x in adj if x < m[x])
    return md, nd, mt


def has_m_diamond(adj, m):
    return diamond_stats(adj, m)[0] > 0


def nonm_diamonds_near_mtriangles(adj, m):
    """Non-M diamonds sharing a vertex with an M-triangle (adversarial-coverage measure)."""
    tv = set()
    for x in adj:
        if x < m[x]:
            for z in adj[x] & adj[m[x]]:
                tv |= {x, m[x], z}
    cnt = 0
    for x in adj:
        for y in adj[x]:
            if x > y:
                continue
            for z1, z2 in combinations(sorted(adj[x] & adj[y]), 2):
                es = ((x, y), (x, z1), (y, z1), (x, z2), (y, z2))
                if not any(m.get(a) == b for a, b in es) and {x, y, z1, z2} & tv:
                    cnt += 1
    return cnt


def verify_partition(adj, pieces):
    """Own exact verification: pieces are simple 5-edge paths of G partitioning E(G)."""
    allE = Counter(E(u, v) for u in adj for v in adj[u] if u < v)
    used = Counter()
    for p in pieces:
        if len(p) != 6 or len(set(p)) != 6:
            raise Failure("piece not a simple 5-edge path: %r" % (p,))
        for u, v in zip(p, p[1:]):
            if v not in adj[u]:
                raise Failure("non-edge in %r" % (p,))
        used.update(edges_of(p))
    if used != allE:
        raise Failure("not an exact edge partition")


# ----------------------------------------------------------------------------------------
# Part lemma4: own enumeration, M-diamond hypothesis

def local_diamonds(edge_list, medges):
    """Return (has any diamond, has a diamond through one of medges)."""
    nb = defaultdict(set)
    for u, v in edge_list:
        nb[u].add(v); nb[v].add(u)
    M = {E(*e) for e in medges}
    anyd = md = False
    for u, v in edge_list:
        for z1, z2 in combinations(sorted(nb[u] & nb[v]), 2):
            anyd = True
            if {E(u, v), E(u, z1), E(v, z1), E(u, z2), E(v, z2)} & M:
                md = True
    return anyd, md


def lemma4_m():
    """Three consecutive trails of an odd type-2 cycle.  Pendant kinds: u (unchanged s(b_i)),
    c (changed r(b_i)), G (G-pendant m(b_i); 04e Lemma 7).  Labels as in 04d (o1)-(o5).
    Known local M-edges: c_i d_i and, for a G-pendant, b_i A_i.  A case is excluded iff the
    15 local edges contain a diamond through a known M-edge.  Claim: every other case has a
    cover by three simple paths unless the block is open and d_1 in {A_0, A_2}."""
    res = Counter()
    bad = []
    diff = []
    for closed in (True, False):
        for d0b2, d2b0 in ([(False, False)] if closed else list(product((False, True), repeat=2))):
            b = ["b0", "b1", "b2"]
            c = ["c0", "c1", "c2"]
            e = ["c2" if closed else "cm1", "c0", "c1"]
            d = ["b2" if d0b2 else "d0", "d1", "b0" if d2b0 else "d2"]
            ce = set(c) | set(e)
            present = (ce | set(d)) - set(b)
            for kinds in product("ucG", repeat=3):
                opts = []
                for i in range(3):
                    if kinds[i] == "u":       # s(b_i): not c_i, e_i (P1/inj.), not d_i (P3)
                        opts.append(sorted(present - {c[i], e[i], d[i]}) + ["F%d" % i])
                    elif kinds[i] == "c":     # r(b_i): avoids every c-, e-label (o4)
                        opts.append(sorted(present - ce) + ["F%d" % i])
                    else:                     # m(b_i): fresh, or another trail's fresh u-pendant
                        opts.append(["N%d" % i] + ["F%d" % j for j in range(3) if j != i])
                for A in product(*opts):
                    ok = True
                    for i in range(3):
                        if A[i].startswith("F"):
                            j = int(A[i][1])
                            if j != i and not (kinds[i] == "G" and kinds[j] == "u" and A[j] == A[i]):
                                ok = False
                    for i, j in combinations(range(3), 2):
                        if A[i] == A[j] and not ({kinds[i], kinds[j]} == {"G", "u"} and A[i].startswith("F")):
                            ok = False
                    if not ok:
                        continue
                    trails = [(A[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                    el = [x for t in trails for x in edges_of(t)]
                    if len(set(el)) != 15:
                        continue
                    medges = [(c[i], d[i]) for i in range(3)] + [(b[i], A[i]) for i in range(3) if kinds[i] == "G"]
                    anyd, md = local_diamonds(el, medges)
                    hasG = "G" if "G" in kinds else "noG"
                    kind = "closed" if closed else "open"
                    if md:
                        res[(hasG, "excluded (local M-diamond)")] += 1
                        continue
                    if anyd:
                        res[(hasG, "local diamond avoiding M (not excluded under B')")] += 1
                    cov = path_cover(el, 3)
                    if cov is not None:
                        assert sorted(x for p in cov for x in edges_of(p)) == sorted(el)
                        assert all(len(set(p)) == 6 for p in cov)
                        res[(hasG, kind, "cover")] += 1
                        if anyd:
                            diff.append((trails, kinds, "covered"))
                    else:
                        okx = (not closed) and d[1] in (A[0], A[2])
                        res[(hasG, kind, "no cover, d1 in {A0,A2}" if okx else "NO COVER OTHER")] += 1
                        if anyd:
                            diff.append((trails, kinds, "exception" if okx else "BAD"))
                        if not okx:
                            bad.append((trails, kinds))
    return res, bad, diff


# ----------------------------------------------------------------------------------------
# Parts exact / windows: own M-diamond filter for the 04e label engine

import check_regular_path_label_engine as engine


class OwnMState(engine._State):
    """Engine state with the engine's own diamond axiom OFF; after each NEW edge XY the state
    is rejected iff some 4-set {X,Y,Z,W} spans >= 5 known edges (a diamond, or a K4 = all
    diamonds) one of which is a known M-edge.  Every diamond through XY has its other two
    vertices in N(X) | N(Y), so this test is complete; it is sound because it only rejects
    real diamonds of known edges containing a known M-edge."""

    def __init__(self, _flag):
        super().__init__(False)

    def add(self, fn, X, Y):
        key = frozenset((X, Y))
        new = key not in self.edges
        if not super().add(fn, X, Y):
            return False
        if not new:
            return True
        S = sorted((self.adj[X] | self.adj[Y]) - {X, Y})
        for Z, W in combinations(S, 2):
            quad = (X, Y, Z, W)
            es = [frozenset(p) for p in combinations(quad, 2) if frozenset(p) in self.edges]
            if len(es) >= 5 and any(self.edges[k] == ("M",) for k in es):
                # 5 edges: a diamond; 6 edges: a K4, every edge of which is in a diamond
                return False
        return True


def own_enum(sc, *a, **k):
    sc.diamond_free = False                 # disable the engine's own (full) diamond test
    old = engine._State
    engine._State = OwnMState
    try:
        yield from engine.enumerate_partitions(sc, *a, **k)
    finally:
        engine._State = old


def quotient_has_m_diamond(sc, cls):
    """Brute force on the final quotient: any diamond with a known M-edge among known edges."""
    lab = {}
    for fn, x, y in sc.facts:
        lab[frozenset((cls[x], cls[y]))] = (fn == "m")
    nb = defaultdict(set)
    for k in lab:
        u, v = tuple(k)
        nb[u].add(v); nb[v].add(u)
    for k in lab:
        u, v = tuple(k)
        for z1, z2 in combinations(sorted(nb[u] & nb[v]), 2):
            if any(lab[frozenset(p)] for p in ((u, v), (u, z1), (v, z1), (u, z2), (v, z2))):
                return True
    return False


def unpatched_postfilter_enum(sc, *a, **k):
    sc.diamond_free = False
    for cls in engine.enumerate_partitions(sc, *a, **k):
        if not quotient_has_m_diamond(sc, cls):
            yield cls


def windows_part(exact_only=False):
    import check_regular_path_gsweep as GS
    orig_run = GS.run
    fails = 0
    if True:
        # exactness: own incremental filter == unpatched engine + brute force, on small windows
        mismatch = 0
        captured = {}

        def capture(sc, pieces, tally, name, **kw):
            A = set(tuple(sorted(cls.items())) for cls in own_enum(sc))
            B = set(tuple(sorted(cls.items())) for cls in unpatched_postfilter_enum(sc))
            captured[name] = (len(A), len(B))
            nonlocal mismatch
            if A != B:
                mismatch += 1
                print("  EXACTNESS MISMATCH", name, len(A), len(B), flush=True)
            # the filter is genuinely weaker than diamond-freeness: count the difference
            sc.diamond_free = True
            nd = sum(1 for _ in engine.enumerate_partitions(sc))
            print(f"  exact {name}: own-filter {len(A)} = postfilter {len(B)}; full diamond-free {nd}", flush=True)
            return 0

        GS.run = capture
        t = Counter()
        GS.window_Q(t); GS.window_P_alpha(t); GS.window_P_beta(t); GS.window_absorbed(t)
        GS.run = orig_run
        print("exactness mismatches:", mismatch, flush=True)
        fails += mismatch
        # selftest on hand-made scenarios
        from check_regular_path_label_engine import Scenario

        def cnt(build, enum):
            sc = Scenario("t"); build(sc); sc.distinct(*sc.syms)
            return sum(1 for _ in enum(sc))
        cases = {
            "M chord (diamond)": (lambda sc: (sc.m("x", "y"), sc.r("x", "a"), sc.r("a", "y"), sc.s("x", "b"), sc.s("b", "y")), 0),
            "M side (diamond)": (lambda sc: (sc.m("x", "y"), sc.r("y", "a"), sc.r("a", "x"), sc.s("x", "b"), sc.s("b", "a")), 0),
            "no M (diamond)": (lambda sc: (sc.r("x", "y"), sc.r("a", "x"), sc.r("y", "b"), sc.s("y", "a"), sc.s("b", "x")), 1),
            "K4 without M": (lambda sc: (sc.r("x", "y"), sc.r("y", "z"), sc.r("z", "w"), sc.r("w", "x"),
                                         sc.s("x", "z"), sc.s("y", "w")), 1),
            "M edge pendant to diamond": (lambda sc: (sc.r("x", "y"), sc.r("a", "x"), sc.r("y", "b"), sc.s("y", "a"),
                                                      sc.s("b", "x"), sc.m("a", "z")), 1),
            "M side added last": (lambda sc: (sc.r("y", "a"), sc.r("a", "x"), sc.s("x", "b"), sc.s("b", "a"), sc.m("x", "y")), 0),
            "M-triangle only": (lambda sc: (sc.m("x", "y"), sc.r("x", "a"), sc.r("a", "y")), 1),
        }
        for name, (build, want) in cases.items():
            got = cnt(build, own_enum)
            if got != want:
                print("  OWN FILTER SELFTEST FAIL", name, got, want); fails += 1
        print("own filter self-test done", flush=True)
    if exact_only:
        return fails
    # full rerun of W1-W8 with the own filter
    GS.enumerate_partitions = own_enum
    try:
        GS.symbolic_exchanges()
        tally = Counter()
        for w in (GS.window_Q, GS.window_P_alpha, GS.window_P_beta, GS.window_absorbed):
            fails += w(tally)
        fails += GS.window_Gamma_source(tally, "type2")
        fails += GS.window_Gamma_source(tally, "Gtarget")
        fails += GS.window_rotation(tally)
        for k in sorted(tally, key=str):
            if k[1] != "identifications":
                print("  ", k, tally[k])
        # Gamma' interface: with a changed or G-pendant, no alternative and no exclusion was used
        for k in tally:
            if k[0].startswith("Gamma") and ("A=type1" in k[0] or "A=linked" in k[0]) and k[1] in ("alternative used", "excluded case"):
                print("  GAMMA' INTERFACE VIOLATION", k, tally[k]); fails += 1
    finally:
        GS.enumerate_partitions = engine.enumerate_partitions
    print("windows total failures", fails, flush=True)
    return fails


# ----------------------------------------------------------------------------------------
# instance generators

def random_matching_on(nonadj_ok, V, rng, tries=200):
    for _ in range(tries):
        free = list(V)
        rng.shuffle(free)
        m = {}
        okk = True
        while free:
            x = free.pop()
            cand = [y for y in free if nonadj_ok(x, y)]
            if not cand:
                okk = False
                break
            y = rng.choice(cand)
            free.remove(y)
            m[x], m[y] = y, x
        if okk:
            return m
    return None


def anneal_graph(adj, m, rng, steps, hyp=True, wtri=2.0):
    """Degree-preserving switches of non-M edges; M fixed.  Objective: no M-diamond (if hyp),
    many diamonds avoiding M and many M-triangles."""
    def cost(a):
        md, nd, mt = diamond_stats(a, m)
        return (100 * md if hyp else 0) - min(nd, 4 * len(a)) - wtri * min(mt, len(a))
    cur = cost(adj)
    H = [E(u, v) for u in adj for v in adj[u] if u < v and m[u] != v]
    for _ in range(steps):
        i, j = rng.randrange(len(H)), rng.randrange(len(H))
        (a, b), (c, d) = H[i], H[j]
        if rng.random() < 0.5:
            c, d = d, c
        if len({a, b, c, d}) < 4 or c in adj[a] or d in adj[b]:
            continue
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        nc = cost(adj)
        if nc <= cur or rng.random() < 0.03:
            cur = nc
            H[i], H[j] = E(a, c), E(b, d)
        else:
            adj[a].discard(c); adj[c].discard(a); adj[b].discard(d); adj[d].discard(b)
            adj[a].add(b); adj[b].add(a); adj[c].add(d); adj[d].add(c)
    return adj


def graph_instance(n, rng, fam, hyp=True, quick=False):
    V = list(range(n))
    if fam == "circulant":
        while True:
            a, b = rng.sample(range(1, n // 2), 2)
            if len({a, b, n - a, n - b}) == 4:
                break
        adj = {v: {(v + a) % n, (v - a) % n, (v + b) % n, (v - b) % n} for v in V}
        if rng.random() < 0.5:   # C_n(1,2): every edge in a diamond
            adj = {v: {(v + 1) % n, (v - 1) % n, (v + 2) % n, (v - 2) % n} for v in V}
    else:  # K5 blocks (n divisible by 10)
        adj = {v: {w for w in range(5 * (v // 5), 5 * (v // 5) + 5) if w != v} for v in V}
    m = random_matching_on(lambda x, y: y not in adj[x], V, rng)
    if m is None:
        return None
    for x in V:
        adj[x].add(m[x])
    adj = anneal_graph(adj, m, rng, (20 if quick else 60) * n, hyp=hyp, wtri=rng.choice((0.5, 2.0, 4.0)))
    if any(len(adj[v]) != 5 for v in V):
        return None
    if hyp and has_m_diamond(adj, m):
        return None
    return adj, m


def plant_nonm_diamonds(P, rng, k):
    """Add diamonds whose five edges are R/S edges, on a mix of existing and new vertices."""
    for _ in range(k):
        vs = []
        for _ in range(4):
            if P.nv and rng.random() < 0.7:
                vs.append(rng.randrange(P.nv))
            else:
                vs.append(P.new())
        if len(set(vs)) < 4:
            continue
        x, y, z, w = vs
        pairs = [(x, z), (x, y), (y, z), (x, w), (z, w)]
        if rng.random() < 0.2:
            pairs.append((y, w))         # a K4
        if any(P.m.get(u) == v for u, v in pairs):
            continue
        for u, v in pairs:
            if P.r.get(u) == v or P.r.get(v) == u or P.s.get(u) == v or P.s.get(v) == u:
                continue
            opts = [("r", u, v), ("r", v, u), ("s", u, v), ("s", v, u)]
            rng.shuffle(opts)
            for fn, a, b in opts:
                try:
                    (P.setr if fn == "r" else P.sets)(a, b)
                    break
                except ValueError:
                    pass
    return P


def complete_and_repair_m(P, rng, extra, iters, hyp=True):
    """Complete the planted partial (m, r, s) and anneal (free r, s values and free M-edges)
    to (P1)-(P3) and, if hyp, no diamond through an M-edge; reward diamonds avoiding M."""
    n = P.nv + extra
    if n % 2:
        n += 1
    V = list(range(n))
    m, r, s = dict(P.m), dict(P.r), dict(P.s)
    free = [v for v in V if v not in m]
    rng.shuffle(free)
    for i in range(0, len(free), 2):
        m[free[i]], m[free[i + 1]] = free[i + 1], free[i]
    mfree = [E(free[i], free[i + 1]) for i in range(0, len(free), 2)]
    rdom = [v for v in V if v not in r]
    rcod = [v for v in V if v not in set(r.values())]
    rng.shuffle(rcod)
    r.update(zip(rdom, rcod))
    sdom = [v for v in V if v not in s]
    scod = [v for v in V if v not in set(s.values())]
    rng.shuffle(scod)
    s.update(zip(sdom, scod))

    def score():
        bad = 0
        cnt = Counter()
        for v in V:
            if r[v] == v or s[v] == v:
                bad += 3
            cnt[E(v, r[v])] += 1
            cnt[E(v, s[v])] += 1
            if v < m[v]:
                cnt[E(v, m[v])] += 1
            if r[r[v]] == v or s[s[v]] == v:
                bad += 1
            if s[r[v]] == m[v]:
                bad += 1
        bad += sum(x - 1 for x in cnt.values()) * 2
        adj = defaultdict(set)
        for u, v in cnt:
            if u != v:
                adj[u].add(v); adj[v].add(u)
        md, nd, mt = diamond_stats(adj, m)
        if hyp:
            bad += md
        return bad, 8 * bad - min(nd, 40) - min(mt, 20)

    bad, cur = score()
    for _ in range(iters):
        x = rng.random()
        if x < 0.42 and len(rdom) > 1:
            a, b = rng.sample(rdom, 2)
            r[a], r[b] = r[b], r[a]
            undo = lambda: r.__setitem__(a, r[b]) or r.__setitem__(b, r[a]) if False else None
            nb_, nc = score()
            if nc <= cur or rng.random() < 0.01:
                bad, cur = nb_, nc
            else:
                r[a], r[b] = r[b], r[a]
        elif x < 0.84 and len(sdom) > 1:
            a, b = rng.sample(sdom, 2)
            s[a], s[b] = s[b], s[a]
            nb_, nc = score()
            if nc <= cur or rng.random() < 0.01:
                bad, cur = nb_, nc
            else:
                s[a], s[b] = s[b], s[a]
        elif len(mfree) > 1:
            i, j = rng.sample(range(len(mfree)), 2)
            (a, b), (c, d) = mfree[i], mfree[j]
            if rng.random() < 0.5:
                c, d = d, c
            m[a], m[c], m[b], m[d] = c, a, d, b
            nb_, nc = score()
            if nc <= cur or rng.random() < 0.01:
                bad, cur = nb_, nc
                mfree[i], mfree[j] = E(a, c), E(b, d)
            else:
                m[a], m[b], m[c], m[d] = b, a, d, c
        if bad == 0 and rng.random() < 0.002:
            break
    if bad:
        return None
    adj = {v: set() for v in V}
    for v in V:
        for w in (m[v], r[v], s[v]):
            adj[v].add(w); adj[w].add(v)
    if any(len(adj[v]) != 5 for v in V):
        return None
    if hyp and has_m_diamond(adj, m):
        return None
    check_P(adj, m, r, s)
    return adj, m, r, s


# ----------------------------------------------------------------------------------------
# Proposition B' (first sweep) and the full procedure on one instance

def is_g_configuration(p, m, r, s):
    for q in (p, tuple(reversed(p))):
        b, c, f, b2, h, Y = q
        if b == b2 and r[c] == b and r[f] == c and m[f] == b and r[b] == h and Y in (s[h], r[h]) \
                and len(set(q)) == 5:
            return True
    return False


def check_instance(adj, m, r, s, rng, stats, tag):
    """Raises Failure on any violated claim."""
    check_P(adj, m, r, s)
    # Proposition B': after the first sweep only G-configurations are non-simple
    st1 = Counter()
    try:
        pcs = first_sweep(adj, m, r, s, rng, st1, False)
    except (SweepFailure, AssertionError) as ex:
        raise Failure("first sweep: %s" % (ex,))
    if st1["Lemma4 realized: closed block without cover"] or st1["Lemma4 realized: open block failing OTHER"]:
        raise Failure("Lemma 4 (realized) fails outside the exception")
    allE = Counter(E(u, v) for u in adj for v in adj[u] if u < v)
    used = Counter(x for _, p in pcs for x in edges_of(p))
    if used != allE:
        raise Failure("first sweep not a partition")
    for tg, p in pcs:
        if len(set(p)) != 6:
            if not (tg == "good" and is_g_configuration(p, m, r, s)):
                raise Failure("Prop B': non-simple first-sweep piece %s %r is not a G-configuration" % (tg, p))
            stats[(tag, "first-sweep G-configurations")] += 1
    # full procedure (first + second sweep), own verification
    st = Counter()
    out = procedure(adj, m, r, s, rng, st)
    verify_partition(adj, [p for _, p in out])
    stats[(tag, "verified decompositions")] += 1
    for k, v in st.items():
        stats[(tag, k)] += v
        stats[("ALL", k)] += v


def run_instances(args, rng, hyp, stats, fails):
    tag0 = "" if hyp else "CONTROL "
    q = args.quick
    # graphs
    fams = (("circulant", (12, 14, 16, 20, 24, 30)), ("K5blocks", (10, 20, 30, 40)))
    per = args.graphs if args.graphs is not None else (3 if q else 12)
    for fam, orders in fams:
        for n in orders:
            for _ in range(per):
                inst = graph_instance(n, rng, fam, hyp=hyp, quick=q)
                tag = tag0 + "graph-" + fam
                if inst is None:
                    stats[(tag, "generation failed")] += 1
                    continue
                adj, m = inst
                md, nd, mt = diamond_stats(adj, m)
                stats[(tag, "graphs")] += 1
                stats[(tag, "diamonds avoiding M")] += nd
                stats[(tag, "diamonds through M")] += md
                stats[(tag, "M-triangles")] += mt
                stats[(tag, "non-M diamonds touching an M-triangle")] += nonm_diamonds_near_mtriangles(adj, m)
                for _ in range(3 if q else 8):
                    try:
                        r, s = lemma1(adj, m, rng)
                        check_instance(adj, m, r, s, rng, stats, tag)
                    except (Failure, AssertionError, SweepFailure) as ex:
                        stats[(tag, "FAILURE " + str(ex)[:70])] += 1
                        fails.append((tag, adj, m, str(ex)))
    # planted generic data
    npl = args.planted if args.planted is not None else (150 if q else 1500)
    for _ in range(npl):
        tag = tag0 + "planted"
        P = plant_random(rng, rng.randint(1, 5))
        plant_nonm_diamonds(P, rng, rng.randint(1, 6))
        inst = complete_and_repair_m(P, rng, rng.choice((4, 8, 14)), 2500 if q else 5000, hyp=hyp)
        if inst is None:
            stats[(tag, "repair failed (skipped)")] += 1
            continue
        adj, m, r, s = inst
        md, nd, mt = diamond_stats(adj, m)
        stats[(tag, "instances")] += 1
        stats[(tag, "diamonds avoiding M")] += nd
        stats[(tag, "diamonds through M")] += md
        stats[(tag, "instances with a diamond avoiding M")] += nd > 0
        stats[(tag, "non-M diamonds touching an M-triangle")] += nonm_diamonds_near_mtriangles(adj, m)
        try:
            check_instance(adj, m, r, s, rng, stats, tag)
        except (Failure, AssertionError, SweepFailure) as ex:
            stats[(tag, "FAILURE " + str(ex)[:70])] += 1
            fails.append((tag, adj, m, str(ex)))


def main():
    ap = ArgumentParser()
    ap.add_argument("--seed", type=int, default=5)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--parts", nargs="*", default=["lemma4", "exact", "graphs", "control", "windows"])
    ap.add_argument("--graphs", type=int, default=None)
    ap.add_argument("--planted", type=int, default=None)
    args = ap.parse_args()
    rng = Random(args.seed)
    total_fail = 0
    t0 = time.time()
    if "lemma4" in args.parts:
        print("== Lemma 4 / 4' under the M-diamond hypothesis (own enumeration) ==", flush=True)
        res, bad, diff = lemma4_m()
        for k in sorted(res, key=str):
            print("  ", k, res[k])
        print("   cases with a local diamond avoiding M:", len(diff),
              Counter(x[2] for x in diff), flush=True)
        if bad:
            print("  LEMMA 4 COUNTEREXAMPLES:", bad[:5]); total_fail += len(bad)
    if "exact" in args.parts and "windows" not in args.parts:
        print("== exactness of the own M-diamond filter ==", flush=True)
        total_fail += windows_part(exact_only=True)
    if "graphs" in args.parts or "planted" in args.parts:
        print("== end-to-end: graphs and planted generic data under the hypothesis ==", flush=True)
        stats, fails = Counter(), []
        run_instances(args, rng, True, stats, fails)
        for k in sorted(stats, key=str):
            print("  ", k, stats[k])
        print("  failures:", len(fails), flush=True)
        total_fail += len(fails)
        if fails:
            import pickle
            with open("04-handoff/review-theoremBprime/failures.pkl", "wb") as fh:
                pickle.dump(fails[:50], fh)
    if "control" in args.parts:
        print("== control: hypothesis OFF (M may lie in diamonds) ==", flush=True)
        stats, fails = Counter(), []
        a2 = ArgumentParser().parse_args([])
        a2.quick, a2.graphs, a2.planted = True, 2, (60 if args.quick else 200)
        run_instances(a2, rng, False, stats, fails)
        nm = sum(1 for f in fails)
        for k in sorted(stats, key=str):
            if "FAILURE" in str(k) or "verified" in str(k) or "diamonds through M" in str(k):
                print("  ", k, stats[k])
        print("  control failures (expected > 0):", nm, flush=True)
    if "windows" in args.parts:
        print("== 04e windows W1-W8 with the own M-diamond filter ==", flush=True)
        total_fail += windows_part()
    print("elapsed %.0fs" % (time.time() - t0))
    print("ALL CHECKS PASSED" if total_fail == 0 else "FAILURES: %d" % total_fail)
    return 1 if total_fail else 0


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    sys.exit(main())
