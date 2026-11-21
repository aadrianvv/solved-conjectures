#!/usr/bin/env python3
"""Direct SAT check, independent of the proof: is there a proper (d+1)-edge-colouring of K_{d+1} - e whose tight
digraph (arc e -> f iff e, f share a vertex and colour(f) = colour(e) + 1 mod d+1) is acyclic?
By Guichard's theorem this is equivalent to chi'_c(K_{d+1} - e) < d + 1.
Encoding: x[e][c] (edge e has colour c); t[e][f] for e != f (e precedes f in a linear order; antisymmetric, transitive);
for adjacent e, f: x[e][c] and x[f][c+1] imply t[e][f].  Needs python-sat.  Usage: python3 verify_sat.py 4 6   (d = 6 takes about 40 s; d = 8 did not finish in 15 minutes)"""
import sys, time, itertools
from pysat.solvers import Solver
def instance(d):
    n = d + 1
    edges = [(a, b) for a in range(n) for b in range(a + 1, n) if (a, b) != (0, 1)]
    E = len(edges); idx = {}
    def X(e, c): return 1 + e * n + c
    base = E * n
    def T(e, f): return base + 1 + e * E + f
    cl = []
    for e in range(E):
        cl.append([X(e, c) for c in range(n)])
        for c1 in range(n):
            for c2 in range(c1 + 1, n): cl.append([-X(e, c1), -X(e, c2)])
    adj = [(e, f) for e in range(E) for f in range(E) if e != f and set(edges[e]) & set(edges[f])]
    for e, f in adj:
        if e < f:
            for c in range(n): cl.append([-X(e, c), -X(f, c)])
        for c in range(n): cl.append([-X(e, c), -X(f, (c + 1) % n), T(e, f)])
    for e in range(E):
        for f in range(e + 1, E):
            cl.append([T(e, f), T(f, e)]); cl.append([-T(e, f), -T(f, e)])
    for e, f, g in itertools.permutations(range(E), 3):
        cl.append([-T(e, f), -T(f, g), T(e, g)])
    # symmetry breaking: the edge (0,2) has colour 0
    cl.append([X(edges.index((0, 2)), 0)])
    return cl, edges, X
for d in [int(a) for a in sys.argv[1:]]:
    t0 = time.time(); cl, edges, X = instance(d)
    s = Solver(name='cadical153', bootstrap_with=cl); res = s.solve()
    if res:
        m = set(v for v in s.get_model() if v > 0)
        col = {edges[e]: next(c for c in range(d + 1) if X(e, c) in m) for e in range(len(edges))}
        print("d=%d: an acyclic (d+1)-edge-colouring EXISTS, so chi'_c < d+1. Example: %s (%.1fs)" % (d, col, time.time() - t0), flush=True)
    else:
        print("d=%d: no (d+1)-edge-colouring of K_%d - e has an acyclic tight digraph, so chi'_c = d+1 (%d clauses, %.1fs)" % (d, d + 1, len(cl), time.time() - t0), flush=True)
