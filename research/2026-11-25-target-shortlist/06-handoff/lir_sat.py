"""SAT encoder for locally irregular k-edge-colourings of a graph, with optional
structural restrictions on colour class 0 (third session experiments).

restrictions (strings):
  'star0'      colour class 0 is a star forest (no path with three class-0 edges, no triangle)
  'span0'      every vertex has a class-0 edge
  'hubind'     vertices with no class-0 edge are pairwise non-adjacent
"""
import itertools

from pysat.formula import IDPool
from pysat.solvers import Cadical153


def edges_of(adj):
    return [(u, v) for u in range(len(adj)) for v in adj[u] if u < v]


def encode(adj, k=3, restrictions=()):
    n = len(adj)
    E = edges_of(adj)
    eid = {}
    for i, (u, v) in enumerate(E):
        eid[(u, v)] = eid[(v, u)] = i
    pool = IDPool()
    x = lambda i, c: pool.id(('x', i, c))
    cls = []
    for i in range(len(E)):
        cls.append([x(i, c) for c in range(k)])
        for a, b in itertools.combinations(range(k), 2):
            cls.append([-x(i, a), -x(i, b)])
    # degree indicators deg[v][c][d]
    dv = lambda v, c, d: pool.id(('d', v, c, d))
    for v in range(n):
        inc = [eid[(v, w)] for w in adj[v]]
        for c in range(k):
            D = len(inc)
            cls.append([dv(v, c, d) for d in range(D + 1)])
            for a, b in itertools.combinations(range(D + 1), 2):
                cls.append([-dv(v, c, a), -dv(v, c, b)])
            for pat in itertools.product([0, 1], repeat=D):
                cls.append([(-x(inc[j], c) if pat[j] else x(inc[j], c)) for j in range(D)] + [dv(v, c, sum(pat))])
    for i, (u, v) in enumerate(E):
        for c in range(k):
            for d in range(1, 4):
                cls.append([-x(i, c), -dv(u, c, d), -dv(v, c, d)])
    if 'star0' in restrictions:
        for b in range(n):
            for c_ in adj[b]:
                if b < c_:
                    for a in adj[b]:
                        for d in adj[c_]:
                            if a != c_ and d != b and a != d:
                                cls.append([-x(eid[(a, b)], 0), -x(eid[(b, c_)], 0), -x(eid[(c_, d)], 0)])
        for u in range(n):
            for v, w in itertools.combinations(adj[u], 2):
                if w in adj[v]:
                    cls.append([-x(eid[(u, v)], 0), -x(eid[(u, w)], 0), -x(eid[(v, w)], 0)])
    if 'span0' in restrictions:
        for v in range(n):
            cls.append([x(eid[(v, w)], 0) for w in adj[v]])
    if 'hubind' in restrictions:
        for u, v in E:
            cls.append([x(eid[(u, w)], 0) for w in adj[u]] + [x(eid[(v, w)], 0) for w in adj[v]])
    return E, x, cls


def solve(adj, k=3, restrictions=()):
    E, x, cls = encode(adj, k, restrictions)
    with Cadical153(bootstrap_with=cls) as s:
        if not s.solve():
            return None
        m = set(l for l in s.get_model() if l > 0)
        return {E[i]: c for i in range(len(E)) for c in range(k) if x(i, c) in m}


def check(adj, col):
    from collections import Counter
    deg = Counter()
    for (u, v), c in col.items():
        deg[(u, c)] += 1
        deg[(v, c)] += 1
    return all(deg[(u, c)] != deg[(v, c)] for (u, v), c in col.items())
