"""Exhaustive window checks for the second (G-configuration) sweep of 04e.

Each window lists the named vertices of one final piece produced by the second sweep,
the facts r(x)=y, s(x)=y, m(x)=y known about them, and the scenario inequalities.
`check_regular_path_label_engine.enumerate_partitions` enumerates every identification of
the names compatible with the axioms of the canonical construction (injective r, s,
involution m, disjoint edge classes, (P2), (P3)) and with diamond-freeness of the known
edges.  The window passes if the final piece is a simple path in every identification.
"""

import sys
from collections import Counter
from check_regular_path_label_engine import Scenario, enumerate_partitions, simple, groups


# ---------------------------------------------------------------------------
# fact blocks

def gconfig(sc, k=""):
    """G-configuration with apex c: source T=(a,b,c,d,e,b), target Q=tau(fb) type-0."""
    c, d, b, e, a, f, h = (x + k for x in "cdbeafh")
    sc.m(c, d); sc.r(c, b); sc.r(d, e); sc.s(e, b); sc.s(b, a)
    sc.r(f, c); sc.m(f, b); sc.r(b, h)
    sc.s(c, "sc" + k); sc.s(h, "sh" + k)
    sc.ne("sc" + k, h); sc.ne("sh" + k, c)          # Q = tau(fb) is not defective
    sc.s(f, "g" + k)                                 # g = s(f)
    return c, d, b, e, a, f, h


def apex_at(sc, f, k):
    """A further G-configuration whose f-vertex is the existing vertex f.

    Only the facts r(f)=c*, r(c*)=b*, m(f)=b* and the defective source tau(c* m(c*))
    are recorded; this is a superset of the realizable configurations.  Returns b*."""
    c, b, d, e = "c" + k, "b" + k, "d" + k, "e" + k
    sc.r(f, c); sc.r(c, b); sc.m(f, b)
    sc.m(c, d); sc.r(d, e); sc.s(e, b)
    return b


def source_at(sc, x, k):
    """A source T* with c-label x (T* = tau(x m(x)) defective, b* = r(x)); returns b*."""
    bs, ds, es = "bs" + k, "ds" + k, "es" + k
    sc.r(x, bs); sc.m(x, ds); sc.r(ds, es); sc.s(es, bs)
    return bs


def w0(sc, k=""):
    """W0 = tau(pq) with r(p) = f."""
    f, p, q, u = "f" + k, "p" + k, "q" + k, "u" + k
    sc.r(p, f); sc.m(p, q); sc.r(q, u)
    return p, q, u


def y_end(sc, opt, k=""):
    """Final terminal at the h-end of Q_c."""
    h = "h" + k
    if opt == "plain":
        return "sh" + k
    if opt == "received":           # a first-sweep source at h gave r(h)
        return source_at(sc, h, "Y" + k)
    if opt == "linked":             # a G-configuration c3 with f3 = h used Q_c as partner
        return apex_at(sc, h, "3" + k)     # its partner edge {h, s(h)} is Q_c's terminal
    raise ValueError(opt)


def _edges(pieces, cls):
    return Counter(frozenset((cls[u], cls[v])) for p in pieces for u, v in zip(p, p[1:]))


def run(sc, pieces, tally, name, allow=None, alternatives=(), before=None):
    """Every identification must make all `pieces` simple, or all pieces of one of the
    `alternatives`.  An alternative counts only if, in that identification, it uses
    exactly the edges of the pieces `before` the rule (it is then a valid re-partition)."""
    n = bad = 0
    for cls in enumerate_partitions(sc):
        n += 1
        if all(simple(p, cls) for p in pieces):
            continue
        if any(all(simple(p, cls) for p in alt) and _edges(alt, cls) == _edges(before, cls)
               for alt in alternatives):
            tally[(name, "alternative used")] += 1
            continue
        if allow is not None and allow(cls):
            tally[(name, "excluded case")] += 1
            continue
        bad += 1
        if bad <= 3:
            print("  FAIL", name, groups(cls), pieces, flush=True)
    tally[(name, "identifications")] += n
    tally[(name, "failures")] += bad
    print(f"{name}: {n} identifications, {bad} failures", flush=True)
    return bad


# ---------------------------------------------------------------------------
# windows

def window_Q(tally):
    """Q*_c = (g,f,c,b,h,Y*) for c in case alpha or beta, every Y* option."""
    total = 0
    for case in ("alpha", "beta"):
        for yopt in ("plain", "received", "linked"):
            sc = Scenario("Q")
            gconfig(sc)
            p, q, u = w0(sc)
            if case == "alpha":
                sc.s(u, "su"); sc.ne("g", u); sc.ne("su", "f")
            else:
                sc.s(u, "f")
            Y = y_end(sc, yopt)
            name = f"Q* {case} Y={yopt}"
            total += run(sc, [("g", "f", "c", "b", "h", Y)], tally, name)
    return total


def window_P_alpha(tally):
    """P* = (b,f,p,q,u,Z*) for W0 a non-defective path."""
    total = 0
    for zopt in ("plain", "received", "linked"):
        sc = Scenario("Palpha")
        gconfig(sc)
        p, q, u = w0(sc)
        sc.s(u, "su"); sc.ne("g", u); sc.ne("su", "f")
        if zopt == "plain":
            Z = "su"
        elif zopt == "received":
            Z = source_at(sc, u, "Z")
            sc.ne(Z, p)     # Z = p is the G-configuration at apex u, checked by window_Q
        else:
            Z = apex_at(sc, u, "2")
        total += run(sc, [("b", "f", p, q, u, Z)], tally, f"P* alpha Z={zopt}")
    return total


def window_P_beta(tally):
    """beta: W0 = (g,f,p,q,u,f) defective with b'=f; source or recipient piece."""
    total = 0
    for role in ("source", "recipient"):
        sc = Scenario("Pbeta")
        gconfig(sc)
        p, q, u = w0(sc)
        sc.s(u, "f")
        if role == "source":
            sc.s(p, "sp")
            piece = ("b", "f", u, q, p, "sp")
        else:
            ru = source_at(sc, u, "R")      # incoming type-2 source has c-label u
            piece = ("b", "f", p, q, u, ru)
        total += run(sc, [piece], tally, f"P* beta {role}")
    return total


def window_Gamma_source(tally, link, yopts=("plain", "received", "linked"),
                        aopts=("plain", "type1", "linked")):
    """gamma with W0 kept as a source: Gamma-rule pieces N1, N2.

    link == "type2": W0's target X has e_X = q, so s(q) = b_X = r(c_X), r(d_X) = q.
    link == "Gtarget": W0 is the source of a G-configuration with apex q:
        r(f*) = q, m(f*) = r(q) = g, and Q* = tau(f* g) is not defective.
    """
    total = 0
    for yopt in yopts:
        for aopt in aopts:
            sc = Scenario("GammaSrc")
            gconfig(sc)
            p, q, u = w0(sc)
            sc.same("g", u)
            if link == "type2":
                sc.s(q, "sq"); sc.r("dX", q); sc.m("dX", "cX"); sc.r("cX", "sq")
                # X is not the source T = tau(cd): T has no incoming type-2 link from a
                # source, because T is itself a source
                sc.ne(q, "e")
            else:
                sc.r("fs", q); sc.m("fs", "g")
                sc.s(q, "sq"); sc.r("g", "hs"); sc.s("hs", "shs")
                sc.ne("sq", "hs"); sc.ne("shs", q)
            sc.s("g", "sg")
            Y = y_end(sc, yopt)
            if link == "Gtarget" and yopt == "linked":
                # Gamma is used only at a node of an odd Gtarget cycle, so the next
                # configuration c* (apex q) is itself a gamma-configuration and has no
                # alpha-partner; the configuration linked at h is therefore not c*.
                sc.ne("c3", q)
            if aopt == "plain":
                A = "sg"
            elif aopt == "type1":
                A = source_at(sc, "g", "A")
            else:
                A = apex_at(sc, "g", "2")
            N1 = ("sq", q, p, "f", "c", "b")
            N2 = (Y, "h", "b", "f", "g", A)
            alts = []
            if aopt == "plain":     # Gamma': used when the pendant s(g) equals h
                alts.append([(Y, "h", "g", "f", "c", "b"), ("h", "b", "f", p, q, "sq")])
            before = [("b", "c", "f", "b", "h", Y), (A, "g", "f", p, q, "sq")]
            # W7: at a Gtarget node the Gamma rules may fail only under (F1) s(q) = c with a
            # plain pendant different from h; such nodes are handled by the cycle choice
            allow = ((lambda cls, A=A: cls["sq"] == cls["c"] and A == "sg" and cls["sg"] != cls["h"])
                     if link == "Gtarget" else None)
            total += run(sc, [N1, N2], tally, f"Gamma {link} Y={yopt} A={aopt}",
                         alternatives=alts, before=before, allow=allow)
    return total


def window_Gamma(tally):
    """gamma: s(f)=g=r(q); W=(A*,g,f,p,q,s(q)) source; pieces N1, N2."""
    total = 0
    for yopt in ("plain", "received", "linked"):
        for aopt in ("plain", "type1", "linked"):
            sc = Scenario("Gamma")
            gconfig(sc)
            p, q, u = w0(sc)
            sc.eq.append(("g", u))          # gamma: s(f) = r(q)
            sc.s(q, "sq")
            sc.s("g", "sg")                 # a' = s(g)
            Y = y_end(sc, yopt)
            if aopt == "plain":
                A = "sg"
            elif aopt == "type1":            # source T'' with c'' = g
                A = source_at(sc, "g", "A")
            else:                            # beta-configuration c2 with f2 = g
                A = apex_at(sc, "g", "2")
            N1 = ("sq", q, p, "f", "c", "b")
            N2 = (Y, "h", "b", "f", "g", A)
            total += run(sc, [N1, N2], tally, f"Gamma Y={yopt} A={aopt}")
    return total


def window_absorbed(tally):
    """gamma with W0 absorbed: W0=(A*,g,q,p,f,g) receives fb, Q gives (g,f,c,b,h,Y*)."""
    total = 0
    for aopt in ("plain", "type1", "Gpendant"):
        sc = Scenario("Abs")
        gconfig(sc)
        p, q, u = w0(sc)
        sc.same("g", u)
        sc.s("g", "sg")
        if aopt == "plain":
            A = "sg"
        elif aopt == "type1":
            A = source_at(sc, "g", "A")
        else:                               # g is the f-vertex of a beta-configuration
            A = apex_at(sc, "g", "2")
        total += run(sc, [(A, "g", q, p, "f", "b")], tally, f"W0 absorbed A={aopt}")
    for yopt in ("plain", "received", "linked"):
        sc = Scenario("Qgamma")
        gconfig(sc)
        p, q, u = w0(sc)
        sc.same("g", u)
        Y = y_end(sc, yopt)
        # an absorbed W0 is not a source: the first-sweep source at h (c-label h) and the
        # source of a linked configuration at h (c-label c3) are not W0 = tau(pq)
        if yopt == "received":
            sc.ne("h", q)
        if yopt == "linked":
            sc.ne("c3", q)
        total += run(sc, [("g", "f", "c", "b", "h", Y)], tally, f"Q* gamma Y={yopt}")
    return total


def odd_triples_with_g_pendants():
    """Lemma 4 (diamond-free form) when some pendants are G-pendants m(b_i).

    Label scheme of verify_odd_triples() in check_regular_path_sweep_pipeline.py.  A
    G-pendant (the beta-case G-rule applied before the odd-cycle replacement) avoids every
    local b-, c-, d- and e-label (04e, Lemma 7), so it is a fresh label 20+i, or it equals
    another trail's fresh unchanged pendant 10+k.  Claim: every admissible triple has a
    simple cover unless the block is open and d_1 is A_0 or A_2 (as in Lemma 4).
    """
    from itertools import product
    from check_regular_path_sweep_pipeline import solve_cluster, path_edges, local_diamond
    b, c = (0, 1, 2), (3, 4, 5)
    counts = Counter()
    for closed in (True, False):
        e = (c[2] if closed else 6, c[0], c[1])
        corners = set(c + e)
        for first, last in product((7,) if closed else (7, b[2]), (9,) if closed else (9, b[0])):
            d = (first, 8, last)
            terminals = (corners | set(d)) - set(b)
            base = [sorted((terminals - {c[i], e[i]}) | {10 + i}) for i in range(3)]
            for kinds in product(("u", "c", "G"), repeat=3):
                if "G" not in kinds:
                    continue
                opts = []
                for i in range(3):
                    if kinds[i] == "G":
                        opts.append([20 + i] + [10 + k for k in range(3) if k != i])
                    else:
                        opts.append(base[i])
                for a in product(*opts):
                    if any(kinds[i] == "G" and a[i] < 20 and not (kinds[a[i] - 10] == "u" and a[a[i] - 10] == a[i])
                           for i in range(3)):
                        continue        # a G-pendant may only equal another fresh unchanged pendant
                    if any(kinds[i] != "G" and kinds[j] != "G" and a[i] == a[j] for i in range(3) for j in range(i)):
                        continue        # (o5) for ordinary pendants
                    if any(kinds[i] == "G" and kinds[j] == "G" and a[i] == a[j] for i in range(3) for j in range(i)):
                        continue        # distinct G-pendants
                    if any(kinds[i] == "c" and a[i] in corners or kinds[i] == "u" and a[i] == d[i] for i in range(3)):
                        continue
                    trails = [(a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                    if len({x for t in trails for x in path_edges(t)}) != 15:
                        continue        # two pendants equal at the same b would repeat an edge
                    if local_diamond(trails):
                        counts["excluded (local diamond)"] += 1
                        continue
                    sol = solve_cluster(trails, require_simple=True)
                    if sol is not None:
                        counts[("closed" if closed else "open", "simple cover")] += 1
                    else:
                        assert not closed and d[1] in (a[0], a[2]), (trails, kinds)
                        counts[("open", "no cover, d1 in {A0,A2}")] += 1
    print("odd triples with G-pendants:", dict(counts), flush=True)
    return counts


def gtarget_chain(sc, nodes):
    """Consecutive configurations 0 -> 1 -> ... of a Gtarget cycle in which every node
    fails the Gamma rules (F1: s(c_{k+1}) = c_k).  W0(c_k) = T_{c_{k+1}}, so
    e_{k+1} = f_k, b_{k+1} = g_k = s(f_k), p_k = d_{k+1}, q_k = c_{k+1}."""
    for k in range(nodes):
        gconfig(sc, str(k))
    for k in range(nodes - 1):
        a, b = str(k), str(k + 1)
        sc.same("e" + b, "f" + a)
        sc.same("b" + b, "g" + a)
        sc.same("sc" + b, "c" + a)


def window_rotation(tally):
    """Rotation rule for an odd Gtarget cycle where every node has F1 and A'_k != h_k:
    R_k = (b_k, c_k, f_k, d_{k+1}, c_{k+1}, c_{k+2}),  P_k = (Y*_k, h_k, b_k, f_k, b_{k+1}, a_{k+1})."""
    total = 0
    sc = Scenario("rotR")
    gtarget_chain(sc, 3)
    total += run(sc, [("b0", "c0", "f0", "d1", "c1", "c2")], tally, "rotation R_k")
    for yopt in ("plain", "received", "linked"):
        sc = Scenario("rotP")
        gtarget_chain(sc, 2)
        sc.ne("a1", "h0")                   # otherwise Gamma' applies at this node
        Y = y_end(sc, yopt, "0")
        if yopt == "linked":
            sc.ne("c30", "c1")               # c1 is a gamma-configuration, not alpha-linked
        total += run(sc, [(Y, "h0", "b0", "f0", "b1", "a1")], tally, f"rotation P_k Y={yopt}")
    return total


def symbolic_exchanges():
    """The G-rule and the Gamma-rule exchange exactly the same edges."""
    def E(ps):
        return Counter(frozenset(e) for p in ps for e in zip(p, p[1:]))
    Q = ("b", "c", "f", "b", "h", "Y")
    W = ("g", "f", "p", "q", "u", "Z")
    assert E([Q, W]) == E([("g", "f", "c", "b", "h", "Y"), ("b", "f", "p", "q", "u", "Z")])
    W = ("A", "g", "f", "p", "q", "sq")
    assert E([Q, W]) == E([("sq", "q", "p", "f", "c", "b"), ("Y", "h", "b", "f", "g", "A")])
    print("G-rule and Gamma-rule are edge exchanges")


def main():
    symbolic_exchanges()
    tally = Counter()
    fails = 0
    fails += window_Q(tally)
    fails += window_P_alpha(tally)
    fails += window_P_beta(tally)
    fails += window_absorbed(tally)
    fails += window_Gamma_source(tally, "type2")
    fails += window_Gamma_source(tally, "Gtarget")
    fails += window_rotation(tally)
    odd_triples_with_g_pendants()
    if "--gamma-rule" in sys.argv:
        fails += window_Gamma(tally)
    for k in sorted(tally):
        print(k, tally[k])
    print("total failures", fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
