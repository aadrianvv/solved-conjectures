"""Theorem C windows: the X2 (D-rule) sweep under property (P5).

(P5)  m(r^{-1}(x)) != r(x) for every vertex x; equivalently no R-path u -> x -> y with uy in M.

The engine of check_regular_path_label_engine.py is used with diamond-freeness switched off
and with (P5) added as an extra axiom: an identification is rejected as soon as known facts
give r(u)=x, r(x)=y and m(u)=y.  Every axiom is a necessary condition, so the enumeration is
a superset of the realizable identifications and a pass is sound.

The audited engine file is not modified; it is patched at import time.
"""

import sys
from collections import Counter

import check_regular_path_label_engine as engine
from check_regular_path_label_engine import Scenario, simple, groups


class P5State(engine._State):
    def __init__(self, diamond_free):
        super().__init__(False)

    def add(self, fn, X, Y):
        if not super().add(fn, X, Y):
            return False
        R, Ri, M = self.F["r"], self.Fi["r"], self.F["m"]
        if fn == "r":
            if Y in R and X in M and M[X] == R[Y]:          # X -> Y -> Z, m(X) = Z
                return False
            if X in Ri and Ri[X] in M and M[Ri[X]] == Y:     # W -> X -> Y, m(W) = Y
                return False
        elif fn == "m":
            if X in R and R[X] in R and R[R[X]] == Y:
                return False
            if Y in R and R[Y] in R and R[R[Y]] == X:
                return False
        return True


_orig_enum = engine.enumerate_partitions


def enumerate_partitions(sc, *a, **k):
    sc.diamond_free = False
    old = engine._State
    engine._State = P5State
    try:
        yield from _orig_enum(sc, *a, **k)
    finally:
        engine._State = old


def _edges(pieces, cls):
    return Counter(frozenset((cls[u], cls[v])) for p in pieces for u, v in zip(p, p[1:]))


class Sc(Scenario):
    """Scenario that records source c-labels, X2 d-labels and 'plain' ends.

    A plain pendant at a b-label x, or a plain terminal at a red-head end x, means that no
    first-sweep source has c-label x and no X2 source has d-label x (the two ways in which the
    terminal edge {x, s(x)} is replaced).  finish() turns this into inequalities."""

    def __init__(self, name):
        super().__init__(name)
        self.src_c, self.x2_d, self.plain = [], [], []

    def finish(self):
        for x in self.plain:
            for y in self.src_c + self.x2_d:
                self.ne(x, y)


def run(sc, pieces, tally, name, allow=None, before=None, show=3):
    sc.finish()
    n = bad = 0
    for cls in enumerate_partitions(sc):
        n += 1
        if before is not None:
            assert _edges(pieces, cls) == _edges(before, cls), "not an exchange"
        if all(simple(p, cls) for p in pieces):
            continue
        if allow is not None and allow(cls):
            tally[(name, "excluded case")] += 1
            continue
        bad += 1
        if bad <= show:
            print("  FAIL", name, groups(cls), [p for p in pieces if not simple(p, cls)], flush=True)
    tally[(name, "identifications")] += n
    tally[(name, "failures")] += bad
    print(f"{name}: {n} identifications, {bad} failures", flush=True)
    return bad


# ---------------------------------------------------------------------------
# fact blocks

def x2(sc, k=""):
    """X2 source T=(a,b,c,d,e,b) with s(c)=e; D-partner W_d = tau(delta mu), r(delta)=d."""
    c, d, b, e, a, dl, mu, u = (x + k for x in ("c", "d", "b", "e", "a", "dl", "mu", "u"))
    sc.m(c, d); sc.r(c, b); sc.r(d, e); sc.s(e, b); sc.s(b, a); sc.s(c, e)
    sc.r(dl, d); sc.m(dl, mu); sc.r(mu, u)
    sc.s(d, "sd" + k)
    sc.src_c.append(c); sc.x2_d.append(d)
    return c, d, b, e, a, dl, mu, u


def source_at(sc, x, k):
    """First-sweep source with c-label x (tau(x m(x)) defective, c-label x); returns r(x)."""
    bs, ds, es = "bs" + k, "ds" + k, "es" + k
    sc.r(x, bs); sc.m(x, ds); sc.r(ds, es); sc.s(es, bs)
    sc.src_c.append(x)
    return bs


def x2_at_d(sc, x, k):
    """An X2 source with d-label x (tau(c3 x) defective, c-label c3=m(x), s(c3)=e3);
    its D-rule gives the piece with red head x the terminal e3 = r(x).  Returns e3."""
    c3, b3, e3 = "c" + k, "b" + k, "e" + k
    sc.m(c3, x); sc.r(c3, b3); sc.r(x, e3); sc.s(e3, b3); sc.s(c3, e3)
    sc.src_c.append(c3); sc.x2_d.append(x)
    return e3


def pendant(sc, b, opt, k, plain_name=None):
    """Final pendant at a b-label b: plain s(b), type-1 changed r(b), or D-pendant r(b)."""
    if opt == "plain":
        p = plain_name or "pa" + k
        sc.s(b, p)
        sc.plain.append(b)
        return p
    if opt == "type1":
        return source_at(sc, b, "P" + k)
    if opt == "Dpend":
        return x2_at_d(sc, b, "Q" + k)
    raise ValueError(opt)


def far_end(sc, u, opt, k):
    """Final terminal at a red-head end u of a non-defective piece: plain s(u), received r(u)
    from a first-sweep source with c-label u, or D-linked r(u) from an X2 with d-label u."""
    if opt == "plain":
        sc.s(u, "z" + k)
        sc.plain.append(u)
        return "z" + k
    if opt == "received":
        return source_at(sc, u, "Z" + k)
    if opt == "Dlinked":
        return x2_at_d(sc, u, "L" + k)
    raise ValueError(opt)


PEND = ("plain", "type1", "Dpend")
FAR = ("plain", "received", "Dlinked")


def window_S(tally):
    """S' = (s(d), d, c, e, b, A): cases alpha, beta and gamma-absorbed."""
    total = 0
    for aopt in PEND:
        sc = Sc("S")
        c, d, b, e, a, dl, mu, u = x2(sc)
        pendant(sc, b, aopt, "", plain_name=a)
        A = a if aopt == "plain" else ("bsP" if aopt == "type1" else "eQ")
        # in case gamma with a type-1 link into T (mu = b) W_d is absorbed and does not
        # trade, so T keeps its plain pendant; that identification belongs to A=plain
        allow = ((lambda cls: cls["sd"] == cls[u] and cls[mu] == cls[b]) if aopt == "type1" else None)
        total += run(sc, [("sd", d, c, e, b, A)], tally, f"S' A={aopt}", allow=allow)
    return total


def window_alpha(tally):
    """alpha: W_d non-defective; W' = (e, d, delta, mu, u, Z)."""
    total = 0
    for zopt in FAR:
        sc = Sc("Walpha")
        c, d, b, e, a, dl, mu, u = x2(sc)
        sc.s(u, "su"); sc.ne("su", d); sc.ne("sd", u)
        Z = "su" if zopt == "plain" else far_end(sc, u, zopt, "")
        if zopt == "plain":
            sc.plain.append(u)
        total += run(sc, [(e, d, dl, mu, u, Z)], tally, f"D alpha W' Z={zopt}")
    return total


def window_beta(tally):
    """beta: W_d = (s(d), d, delta, mu, u, d) defective with b'=d, pendant becomes e."""
    total = 0
    for role in ("source", "recipient"):
        sc = Sc("Wbeta")
        c, d, b, e, a, dl, mu, u = x2(sc)
        sc.s(u, d)
        if role == "source":
            sc.s(dl, "sdl"); sc.ne("sdl", u)        # not itself X2 (that is window_S)
            piece = (e, d, u, mu, dl, "sdl")
        else:
            ru = source_at(sc, u, "R")
            piece = (e, d, dl, mu, u, ru)
        total += run(sc, [piece], tally, f"D beta {role}")
    return total


def gamma_base(sc):
    c, d, b, e, a, dl, mu, u = x2(sc)
    sc.same("sd", u)                 # gamma: e' = d, so b' = s(d) = r(mu) = u
    sc.s(u, "su")                    # canonical pendant of W_d
    return c, d, b, e, a, dl, mu, u


def window_gamma_absorbed(tally):
    """gamma, W_d's link of type 0 or 1: W_d does not trade and becomes (A', u, mu, delta, d, e).
    (S' = (u, d, c, e, b, A) is window_S.)"""
    total = 0
    for a2opt in PEND:
        sc = Sc("Wabs")
        c, d, b, e, a, dl, mu, u = gamma_base(sc)
        pendant(sc, u, a2opt, "2", plain_name="su")
        A2 = "su" if a2opt == "plain" else ("bsP2" if a2opt == "type1" else "eQ2")
        total += run(sc, [(A2, u, mu, dl, d, e)], tally, f"D gamma absorbed A'={a2opt}")
    return total


def window_gamma_D(tally):
    """gamma, W_d's link of type 2 (target X with e_X = mu): Gamma_D rule
    N1 = (s(mu), mu, delta, d, c, e), N2 = (A, b, e, d, u, A')."""
    total = 0
    for aopt in PEND:
        for a2opt in PEND:
            sc = Sc("Wgamma")
            c, d, b, e, a, dl, mu, u = gamma_base(sc)
            # type-2 link: X = (aX, bX, cX, dX, mu, bX), r(dX)=mu, m(dX)=cX, r(cX)=s(mu)
            sc.s(mu, "smu"); sc.r("dX", mu); sc.m("dX", "cX"); sc.r("cX", "smu")
            sc.ne("smu", d)          # W_d not itself X2 (separate window)
            pendant(sc, b, aopt, "1", plain_name=a)
            A = a if aopt == "plain" else ("bsP1" if aopt == "type1" else "eQ1")
            pendant(sc, u, a2opt, "2", plain_name="su")
            A2 = "su" if a2opt == "plain" else ("bsP2" if a2opt == "type1" else "eQ2")
            before = [(A, b, e, d, c, e), (A2, u, d, dl, mu, "smu")]
            N1 = ("smu", mu, dl, d, c, e)
            N2 = (A, b, e, d, u, A2)
            allow = (lambda cls: cls["smu"] == cls["c"]) if GAMMA_ALLOW_F1 else None
            total += run(sc, [N1, N2], tally, f"D gamma type2 A={aopt} A'={a2opt}",
                         before=before, allow=allow)
    return total


GAMMA_ALLOW_F1 = True     # s(mu) = c is treated separately





# ---------------------------------------------------------------------------
# generic search for symbolic re-partitions (used to design rules for residual cases)

def symbolic_partitions(before, interfaces=()):
    """All partitions of the symbolic edges of `before` into len(before) five-edge trails on
    distinct symbols (paths at the symbolic level), in which every interface (x, y) occurs as a
    terminal edge with x at the end and y next to it."""
    from itertools import permutations
    edges = [frozenset((u, v)) for p in before for u, v in zip(p, p[1:])]
    idx = {}
    for e in edges:
        idx.setdefault(e, []).append(len(idx) and None)
    E = Counter(edges)
    nb = {}
    for e in E:
        u, v = tuple(e)
        nb.setdefault(u, set()).add(v); nb.setdefault(v, set()).add(u)
    k = len(before)
    out = []

    def paths(start, used):
        res = []
        def ext(p, used):
            if len(p) == 6:
                res.append(p); return
            for w in nb[p[-1]]:
                e = frozenset((p[-1], w))
                if w not in p and used[e] < E[e]:
                    used[e] += 1
                    ext(p + (w,), used)
                    used[e] -= 1
        ext((start,), used)
        return res

    def ok_iface(pieces):
        for x, y in interfaces:
            if not any((p[0] == x and p[1] == y) or (p[-1] == x and p[-2] == y) for p in pieces):
                return False
        return True

    def rec(pieces, used):
        if len(pieces) == k:
            if all(used[e] == E[e] for e in E) and ok_iface(pieces):
                out.append(tuple(pieces))
            return
        # first unused edge must be covered by the next piece
        rem = [e for e in E if used[e] < E[e]]
        if not rem:
            return
        e0 = min(rem, key=lambda e: sorted(e))
        for s in sorted(nb):
            for p in paths(s, used):
                if p[0] > p[-1]:
                    continue
                pe = Counter(frozenset((u, v)) for u, v in zip(p, p[1:]))
                if e0 not in pe:
                    continue
                if any(used[e] + c > E[e] for e, c in pe.items()):
                    continue
                for e, c in pe.items():
                    used[e] += c
                rec(pieces + [p], used)
                for e, c in pe.items():
                    used[e] -= c

    rec([], Counter())
    return out


def find_rules(sc, before, interfaces, tally, name, show=3):
    """For every identification find which symbolic re-partitions are simple; report a small
    set of candidates covering all identifications (greedy), and the uncovered ones."""
    sc.finish()
    cands = symbolic_partitions(before, interfaces)
    print(f"{name}: {len(cands)} symbolic candidates", flush=True)
    good = []
    n = 0
    for cls in enumerate_partitions(sc):
        n += 1
        good.append(frozenset(i for i, ps in enumerate(cands) if all(simple(p, cls) for p in ps)))
    uncovered = [i for i, g in enumerate(good) if not g]
    chosen = []
    left = set(i for i, g in enumerate(good) if g)
    while left:
        best = max(range(len(cands)), key=lambda c: sum(1 for i in left if c in good[i]))
        chosen.append(best)
        left = {i for i in left if best not in good[i]}
    print(f"  {n} identifications, {len(uncovered)} with no candidate; cover uses {len(chosen)} rules:", flush=True)
    for c in chosen:
        print("   ", cands[c], flush=True)
    tally[(name, "uncovered")] += len(uncovered)
    return cands, chosen, len(uncovered)


# ---------------------------------------------------------------------------
# rule F, D-chains and the D-rotation

def window_F(tally):
    """gamma, type-2 link with (F1) s(mu)=c: W_d's recipient is X = Q_T with b_X=c, e_X=mu.
    Rule F: (A,b,c,d,u,A'), (b,e,d,delta,mu,c), (e,c,f,dX,mu,u)."""
    total = 0
    for aopt in PEND:
        for a2opt in PEND:
            sc = Sc("F")
            c, d, b, e, a, dl, mu, u = gamma_base(sc)
            sc.s(mu, c); sc.r("f", c); sc.m("f", "dX"); sc.r("dX", mu)
            pendant(sc, b, aopt, "1", plain_name=a)
            A = a if aopt == "plain" else ("bsP1" if aopt == "type1" else "eQ1")
            pendant(sc, u, a2opt, "2", plain_name="su")
            A2 = "su" if a2opt == "plain" else ("bsP2" if a2opt == "type1" else "eQ2")
            before = [(A, b, e, d, c, e), (A2, u, d, dl, mu, c), (b, c, "f", "dX", mu, u)]
            new = [(A, b, c, d, u, A2), (b, e, d, dl, mu, c), (e, c, "f", "dX", mu, u)]
            total += run(sc, new, tally, f"rule F A={aopt} A'={a2opt}", before=before)
    return total


def dchain(sc, k, closed=False):
    """X2 sources T_0 -> T_1 -> ... where T_{j+1} is the gamma-partner of T_j and is X2:
    b_{j+1} = s(d_j) = r(mu_j), c_{j+1} = mu_j, d_{j+1} = delta_j, e_{j+1} = d_j."""
    for j in range(k):
        x2(sc, str(j))
    links = [(j, j + 1) for j in range(k - 1)] + ([(k - 1, 0)] if closed else [])
    for x, y in links:
        a, b = str(x), str(y)
        sc.same("sd" + a, "b" + b); sc.same("u" + a, "b" + b)
        sc.same("mu" + a, "c" + b); sc.same("dl" + a, "d" + b); sc.same("e" + b, "d" + a)


def window_D_rotation(tally):
    """D-cycle T_0 -> ... -> T_{L-1} -> T_0 (L >= 3): every S_j = (A_j,b_j,d_{j-1},d_j,c_j,d_{j-1})
    becomes P_j = (A_j, b_j, d_{j-1}, c_j, d_j, d_{j+1}).  Checked on three consecutive nodes
    (open: L >= 4) and on the closed cycle L = 3.  Endpoint uniqueness: d_{j+1} = e_{j+2} is the
    endpoint of S_{j+2} != S_j, so A_j != d_{j+1}."""
    total = 0
    for closed in (False, True):
        for opt in PEND:
            sc = Sc("Drot")
            dchain(sc, 3, closed)
            pendant(sc, "b1", opt, "p", plain_name="a1")
            A = "a1" if opt == "plain" else ("bsPp" if opt == "type1" else "eQp")
            sc.ne(A, "d2")
            total += run(sc, [(A, "b1", "d0", "c1", "d1", "d2")], tally,
                         f"D-rotation {'L=3' if closed else 'open'} A={opt}")
    return total


def symbolic_rotation():
    """The D-rotation re-partitions the edges of the whole cycle (telescoping), L = 3..9."""
    for L in range(3, 10):
        A = [("A", j) for j in range(L)]
        B = [("b", j) for j in range(L)]
        C = [("c", j) for j in range(L)]
        D = [("d", j) for j in range(L)]
        old = Counter(frozenset(e) for j in range(L)
                      for e in zip(*(lambda p: (p, p[1:]))((A[j], B[j], D[j - 1], D[j], C[j], D[j - 1]))))
        new = Counter(frozenset(e) for j in range(L)
                      for e in zip(*(lambda p: (p, p[1:]))((A[j], B[j], D[j - 1], C[j], D[j], D[(j + 1) % L]))))
        assert old == new, L
    print("D-rotation telescopes for L = 3..9")


def symbolic_exchanges_c():
    """Every Theorem C rule exchanges exactly the edges of the pieces it rebuilds."""
    def E(ps):
        return Counter(frozenset(e) for p in ps for e in zip(p, p[1:]))
    S = ("A", "b", "e", "d", "c", "e")
    W = ("sd", "d", "dl", "mu", "u", "Z")
    assert E([S, W]) == E([("sd", "d", "c", "e", "b", "A"), ("e", "d", "dl", "mu", "u", "Z")])  # D-rule
    # absorption: W_d's own trade is undone first (it returns to canonical (A2,u,mu,dl,d,u));
    # then it receives ed in place of its closing edge du, and T takes du.
    Wg = ("A2", "u", "mu", "dl", "d", "u")
    assert E([S, Wg]) == E([("u", "d", "c", "e", "b", "A"), ("A2", "u", "mu", "dl", "d", "e")])
    Wsrc = ("A2", "u", "d", "dl", "mu", "smu")
    assert E([S, Wsrc]) == E([("smu", "mu", "dl", "d", "c", "e"), ("A", "b", "e", "d", "u", "A2")])  # Gamma_D
    print("Theorem C exchanges re-partition their pieces")


def lemma4_p5():
    """Proposition C1: the 04d odd-cycle triple lemma (Lemma 4) rerun under (P5).

    Same label scheme as 04d Lemma 4 (pendants unchanged or changed, A_i = r(b_i) when
    changed), with diamond-freeness off and (P5) as the only extra restriction: a changed
    pendant A_i = d_i would give the R-path c_i -> b_i -> d_i with c_i d_i in M.  Expected:
    259 closed and 720 open simple covers, 24 open exceptions with d_1 in {A_0, A_2}, and no
    other failure.  (Moved here from 04-handoff/p5_scratch/l4p5.py, referee fix m1.)
    """
    from itertools import product
    from check_regular_path_sweep_pipeline import solve_cluster, path_edges
    b, c = (0, 1, 2), (3, 4, 5)
    counts = Counter()
    for closed in (True, False):
        e = (c[2] if closed else 6, c[0], c[1])
        corners = set(c + e)
        for first, last in product((7,) if closed else (7, b[2]), (9,) if closed else (9, b[0])):
            d = (first, 8, last)
            terminals = (corners | set(d)) - set(b)
            options = [sorted((terminals - {c[i], e[i]}) | {10 + i}) for i in range(3)]
            for a in product(*options):
                if len(set(a)) != 3:
                    continue
                trails = [(a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                if len({x for t in trails for x in path_edges(t)}) != 15:
                    continue
                for changed in product((False, True), repeat=3):
                    if any(a[i] in corners if changed[i] else a[i] == d[i] for i in range(3)):
                        continue
                    if any(changed[i] and a[i] == d[i] for i in range(3)):
                        counts["excluded by (P5)"] += 1
                        continue
                    if solve_cluster(trails, require_simple=True) is not None:
                        counts[("closed" if closed else "open") + " cover"] += 1
                    elif not closed and d[1] in (a[0], a[2]):
                        counts["open exception d1 in {A0,A2}"] += 1
                    else:
                        counts["OTHER FAIL"] += 1
    print("Lemma 4 under (P5):", dict(counts))
    expected = {"closed cover": 259, "open cover": 720, "open exception d1 in {A0,A2}": 24}
    bad = counts["OTHER FAIL"] + sum(counts[k] != v for k, v in expected.items())
    print("  failures", bad)
    return bad


def main():
    symbolic_exchanges_c()
    symbolic_rotation()
    tally = Counter()
    fails = lemma4_p5()
    for w in (window_S, window_alpha, window_beta, window_gamma_absorbed, window_gamma_D,
              window_F, window_D_rotation):
        fails += w(tally)
    print("total failures", fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
