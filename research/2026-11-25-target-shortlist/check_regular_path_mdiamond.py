"""Theorem B' check: rerun the 04e windows with a weaker local hypothesis.

Hypothesis (matching-relative): no diamond of G contains an edge of the perfect matching M.
Equivalently every triangle through an M-edge shares no edge with another triangle, and no
M-edge is the chord of a diamond.

The label engine of check_regular_path_label_engine.py is used unchanged except that its
diamond test is replaced by: the known edges contain no diamond one of whose five edges is a
known M-edge.  This is a necessary condition under the hypothesis, so the enumeration is still
a superset of the realizable identifications and a pass is sound.

The audited files check_regular_path_label_engine.py and check_regular_path_gsweep.py are not
modified; this script patches them at import time.

Run:  python check_regular_path_mdiamond.py            (windows W1-W8, Lemma 4 and Lemma 4')
"""

import sys
from collections import Counter
from itertools import combinations, product

import check_regular_path_label_engine as engine
import check_regular_path_gsweep as G
from check_regular_path_sweep_pipeline import solve_cluster, path_edges, edge


class MState(engine._State):
    """Engine state whose diamond test only rejects diamonds through a known M-edge."""

    def __init__(self, diamond_free):
        super().__init__(False)
        self.mode = diamond_free

    def _is_m(self, X, Y):
        return self.edges.get(frozenset((X, Y))) == ("M",)

    def m_diamond_through(self, X, Y):
        adj = self.adj
        common = adj[X] & adj[Y]
        for Z1, Z2 in combinations(sorted(common), 2):
            if any(self._is_m(*e) for e in ((X, Y), (X, Z1), (Y, Z1), (X, Z2), (Y, Z2))):
                return True
        for Z in common:
            for P, Q in ((X, Y), (Y, X)):
                # chord P-Z, triangles P Q Z and P W Z
                for W in (adj[P] & adj[Z]) - {Q}:
                    if any(self._is_m(*e) for e in ((P, Z), (P, Q), (Q, Z), (P, W), (Z, W))):
                        return True
        return False

    def add(self, fn, X, Y):
        existed = frozenset((X, Y)) in self.edges
        if not super().add(fn, X, Y):
            return False
        if existed or X == Y:
            return True
        if self.mode == "M":
            return not self.m_diamond_through(X, Y)
        return True


_orig_enum = engine.enumerate_partitions


def enumerate_partitions_m(sc, *a, **k):
    sc.diamond_free = "M"
    old = engine._State
    engine._State = MState
    try:
        yield from _orig_enum(sc, *a, **k)
    finally:
        engine._State = old


def local_m_diamond(trails, m_edges):
    """Local edges contain a diamond with one of the known M-edges."""
    es = {e for t in trails for e in path_edges(t)}
    adj = {}
    for u, v in es:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    M = {edge(*e) for e in m_edges}
    for u, v in es:
        for z in adj[u] & adj[v]:
            for w in (adj[u] & adj[z]) - {v}:
                if {edge(u, z), edge(u, v), edge(v, z), edge(u, w), edge(z, w)} & M:
                    return True
            for w in (adj[v] & adj[z]) - {u}:
                if {edge(v, z), edge(u, v), edge(u, z), edge(v, w), edge(z, w)} & M:
                    return True
    return False


def odd_triples_m():
    """Lemma 4 of 04d with the hypothesis "no local diamond through a known M-edge".

    Same label scheme and admissibility as verify_odd_triples() in the pipeline checker.
    The known M-edges of the triple are c_i d_i.  Claim: every admissible triple has a
    simple cover unless the block is open and d_1 is A_0 or A_2."""
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
                    if local_m_diamond(trails, [(c[i], d[i]) for i in range(3)]):
                        counts["excluded (local M-diamond)"] += 1
                        continue
                    sol = solve_cluster(trails, require_simple=True)
                    if sol is not None:
                        assert Counter(x for q in sol for x in path_edges(q)) == \
                            Counter(x for t in trails for x in path_edges(t))
                        counts[("closed" if closed else "open", "simple cover")] += 1
                    elif not closed and d[1] in (a[0], a[2]):
                        counts[("open", "no cover, d1 in {A0,A2}")] += 1
                    else:
                        counts["UNEXPECTED FAILURE"] += 1
                        if counts["UNEXPECTED FAILURE"] <= 5:
                            print("  FAIL triple", trails, changed, flush=True)
    print("Lemma 4 (M-diamond hypothesis):", dict(counts), flush=True)
    return counts["UNEXPECTED FAILURE"]


def odd_triples_g_pendants_m():
    """Lemma 4' (G-pendants allowed) with the M-diamond hypothesis.  A G-pendant a_i = m(b_i)
    adds the known M-edge b_i a_i.  Label scheme of check_regular_path_gsweep."""
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
                        continue
                    if any(kinds[i] != "G" and kinds[j] != "G" and a[i] == a[j] for i in range(3) for j in range(i)):
                        continue
                    if any(kinds[i] == "G" and kinds[j] == "G" and a[i] == a[j] for i in range(3) for j in range(i)):
                        continue
                    if any(kinds[i] == "c" and a[i] in corners or kinds[i] == "u" and a[i] == d[i] for i in range(3)):
                        continue
                    trails = [(a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                    if len({x for t in trails for x in path_edges(t)}) != 15:
                        continue
                    medges = [(c[i], d[i]) for i in range(3)] + [(b[i], a[i]) for i in range(3) if kinds[i] == "G"]
                    if local_m_diamond(trails, medges):
                        counts["excluded (local M-diamond)"] += 1
                        continue
                    sol = solve_cluster(trails, require_simple=True)
                    if sol is not None:
                        counts[("closed" if closed else "open", "simple cover")] += 1
                    elif not closed and d[1] in (a[0], a[2]):
                        counts[("open", "no cover, d1 in {A0,A2}")] += 1
                    else:
                        counts["UNEXPECTED FAILURE"] += 1
                        if counts["UNEXPECTED FAILURE"] <= 5:
                            print("  FAIL triple (G-pendants)", trails, kinds, flush=True)
    print("Lemma 4' (M-diamond hypothesis):", dict(counts), flush=True)
    return counts["UNEXPECTED FAILURE"]


def selftest():
    """The patch rejects a diamond through an M-edge (as chord or side) and nothing else."""
    from check_regular_path_label_engine import Scenario

    def count(build, patched):
        sc = Scenario("t"); build(sc); sc.distinct(*sc.syms)
        if patched:
            return sum(1 for _ in enumerate_partitions_m(sc))
        sc.diamond_free = False
        return sum(1 for _ in engine.enumerate_partitions(sc))
    tests = {
        "M chord": (lambda sc: (sc.m("x", "y"), sc.r("x", "a"), sc.r("a", "y"), sc.s("x", "b"), sc.s("b", "y")), 0),
        "M side": (lambda sc: (sc.m("x", "y"), sc.r("y", "a"), sc.r("a", "x"), sc.s("x", "b"), sc.s("b", "a")), 0),
        "no M": (lambda sc: (sc.r("x", "y"), sc.r("a", "x"), sc.r("y", "b"), sc.s("y", "a"), sc.s("b", "x")), 1),
        "M outside": (lambda sc: (sc.r("x", "y"), sc.r("a", "x"), sc.r("y", "b"), sc.s("y", "a"), sc.s("b", "x"),
                                  sc.m("a", "z")), 1),
    }
    for name, (build, want) in tests.items():
        assert count(build, False) == 1, name
        assert count(build, True) == want, name
    print("engine patch self-test passed")


def main():
    selftest()
    G.enumerate_partitions = enumerate_partitions_m
    G.symbolic_exchanges()
    tally = Counter()
    fails = 0
    fails += odd_triples_m()
    fails += odd_triples_g_pendants_m()
    for w in (G.window_Q, G.window_P_alpha, G.window_P_beta, G.window_absorbed):
        fails += w(tally)
    fails += G.window_Gamma_source(tally, "type2")
    fails += G.window_Gamma_source(tally, "Gtarget")
    fails += G.window_rotation(tally)
    for k in sorted(tally):
        print(k, tally[k])
    print("total failures", fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
