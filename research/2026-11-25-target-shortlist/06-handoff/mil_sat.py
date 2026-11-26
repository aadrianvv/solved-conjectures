"""SAT tools for MIL partitions and designations in cubic graphs (third session).

Needs python-sat and networkx on PYTHONPATH (install with pip --target into a
scratch directory; nothing system-wide).  See 06-revised-local-irregularity.md,
section "Fifth pass".

MIL partition: Y independent, X = V - Y induces a linear forest, every x in X has a
Y-neighbour.  Designation: s(y) in N(y); p(x)=#designations, r(x)=#Y-neighbours,
t(x)=r-p.  Conditions: t proper on G[X]; p(x)>=1 => t(x)<=1; (F2w) no component of
the multigraph H (edge between the two non-designated neighbours of each y) is an
odd cycle.
"""
import itertools
import random
import sys
from collections import defaultdict

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical153


def random_cubic(n, seed):
    import networkx as nx
    while True:
        g = nx.random_regular_graph(3, n, seed=seed)
        if nx.is_connected(g):
            return [sorted(g[v]) for v in range(n)]
        seed += 10**6


def edges_of(adj):
    return [(u, v) for u in range(len(adj)) for v in adj[u] if u < v]


def components_cycles(adj, X):
    """Return a cycle (vertex list) in G[X] if any, else None."""
    Xs = set(X)
    parent = {}
    for root in X:
        if root in parent:
            continue
        parent[root] = None
        stack = [(root, None)]
        while stack:
            v, par = stack.pop()
            for w in adj[v]:
                if w not in Xs or w == par:
                    continue
                if w in parent:
                    # found cycle: reconstruct path v ... w via parents
                    pv = [v]
                    while pv[-1] is not None:
                        pv.append(parent[pv[-1]])
                    pw = [w]
                    while pw[-1] is not None:
                        pw.append(parent[pw[-1]])
                    pv = pv[:-1]
                    pw = pw[:-1]
                    sw = set(pw)
                    cyc = []
                    for a in pv:
                        cyc.append(a)
                        if a in sw:
                            break
                    lca = cyc[-1]
                    tail = []
                    for b in pw:
                        if b == lca:
                            break
                        tail.append(b)
                    return cyc + tail[::-1]
                parent[w] = v
                stack.append((w, v))
    return None


def max_mil(adj, extra=None, maximise=True, size=None):
    """Return a maximum-size MIL partition Y (list) via SAT with lazy cycle cuts.
    If size is given, find one with |Y| >= size.  extra: list of clauses over vars y_v=v+1."""
    n = len(adj)
    pool = IDPool(start_from=n + 1)
    base = []
    for u, v in edges_of(adj):
        base.append([-(u + 1), -(v + 1)])
    for v in range(n):
        base.append([v + 1] + [w + 1 for w in adj[v]])  # v in Y or has a Y-neighbour
    if extra:
        base += extra
    cuts = []
    best = None
    lo = size if size is not None else (n + 2) // 4
    while True:
        card = CardEnc.atleast([v + 1 for v in range(n)], bound=lo, vpool=pool, encoding=EncType.seqcounter)
        with Cadical153(bootstrap_with=base + cuts + card.clauses) as s:
            found = None
            while s.solve():
                m = s.get_model()
                Y = [v for v in range(n) if m[v] > 0]
                X = [v for v in range(n) if m[v] <= 0]
                cyc = components_cycles(adj, X)
                if cyc is None:
                    found = Y
                    break
                cl = [c + 1 for c in cyc]
                cuts.append(cl)
                s.add_clause(cl)
        if found is None:
            return best
        best = found
        if not maximise:
            return best
        lo = len(found) + 1


def all_max_mil(adj, limit=10**6):
    """Enumerate all MIL partitions of maximum size (blocking clauses)."""
    n = len(adj)
    Y0 = max_mil(adj)
    k = len(Y0)
    pool = IDPool(start_from=n + 1)
    base = []
    for u, v in edges_of(adj):
        base.append([-(u + 1), -(v + 1)])
    for v in range(n):
        base.append([v + 1] + [w + 1 for w in adj[v]])
    card = CardEnc.equals([v + 1 for v in range(n)], bound=k, vpool=pool, encoding=EncType.seqcounter)
    out = []
    with Cadical153(bootstrap_with=base + card.clauses) as s:
        while s.solve() and len(out) < limit:
            m = s.get_model()
            X = [v for v in range(n) if m[v] <= 0]
            cyc = components_cycles(adj, X)
            if cyc is not None:
                s.add_clause([c + 1 for c in cyc])
                continue
            Y = [v for v in range(n) if m[v] > 0]
            out.append(Y)
            s.add_clause([-(v + 1) for v in Y])
    return out


def h_bad_component(adj, Y, s):
    """Return list of y forming an odd-cycle component of H, or None."""
    Ys = set(Y)
    hedges = []
    for y in Y:
        tn = [x for x in adj[y] if x != s[y]]
        hedges.append((tn[0], tn[1], y))
    inc = defaultdict(list)
    for a, b, y in hedges:
        inc[a].append((b, y))
        inc[b].append((a, y))
    seen = set()
    for v in list(inc):
        if v in seen:
            continue
        comp = []
        stack = [v]
        seen.add(v)
        while stack:
            a = stack.pop()
            comp.append(a)
            for b, y in inc[a]:
                if b not in seen:
                    seen.add(b)
                    stack.append(b)
        if all(len(inc[a]) == 2 for a in comp) and len(comp) % 2 == 1:
            ys = sorted({y for a in comp for _, y in inc[a]})
            return ys
    return None


def designate(adj, Y, want_all=False, extra_fn=None):
    """Find s: Y -> X satisfying the designation conditions (incl. F2w); None if infeasible."""
    n = len(adj)
    Ys = set(Y)
    X = [v for v in range(n) if v not in Ys]
    pool = IDPool()
    z = {}
    cls = []
    for y in Y:
        lits = []
        for x in adj[y]:
            z[(y, x)] = pool.id(('z', y, x))
            lits.append(z[(y, x)])
        cls.append(lits)
        for a, b in itertools.combinations(lits, 2):
            cls.append([-a, -b])
    r = {x: sum(1 for w in adj[x] if w in Ys) for x in X}
    # p(x) = k indicator variables
    pv = {}
    for x in X:
        ins = [z[(w, x)] for w in adj[x] if w in Ys]
        R = len(ins)
        for k in range(R + 1):
            pv[(x, k)] = pool.id(('p', x, k))
        # exactly one k
        cls.append([pv[(x, k)] for k in range(R + 1)])
        for a, b in itertools.combinations(range(R + 1), 2):
            cls.append([-pv[(x, a)], -pv[(x, b)]])
        # link: for each subset pattern
        for pat in itertools.product([0, 1], repeat=R):
            k = sum(pat)
            cls.append([(-ins[i] if pat[i] else ins[i]) for i in range(R)] + [pv[(x, k)]])
        # allowed p: p>=1 => t=r-p<=1
        for k in range(1, R + 1):
            if R - k > 1:
                cls.append([-pv[(x, k)]])
    for u, v in edges_of(adj):
        if u in Ys or v in Ys:
            continue
        for ku in range(r[u] + 1):
            for kv in range(r[v] + 1):
                if r[u] - ku == r[v] - kv:
                    cls.append([-pv[(u, ku)], -pv[(v, kv)]])
    if extra_fn:
        cls += extra_fn(pool, z, pv, X, r)
    sols = []
    with Cadical153(bootstrap_with=cls) as s:
        while s.solve():
            m = set(l for l in s.get_model() if l > 0)
            sd = {y: x for (y, x), var in z.items() if var in m}
            bad = h_bad_component(adj, Y, sd)
            if bad is not None:
                s.add_clause([-z[(y, sd[y])] for y in bad])
                continue
            if not want_all:
                return sd
            sols.append(sd)
            s.add_clause([-z[(y, sd[y])] for y in Y])
    return sols if want_all else None


def verify_frame(adj, Y, sd):
    """Independent check: build the Lemma 2 / Lemma 1' colouring and verify local irregularity."""
    n = len(adj)
    Ys = set(Y)
    T = set()
    for y in Y:
        for x in adj[y]:
            if x != sd[y]:
                T.add(frozenset((x, y)))
    E = [frozenset(e) for e in edges_of(adj)]
    dT = [sum(1 for w in adj[v] if frozenset((v, w)) in T) for v in range(n)]
    for e in E:
        if e not in T:
            a, b = tuple(e)
            if dT[a] == dT[b]:
                return False, 'S not irregular'
    # Lemma 1' thread colouring of the subdivision: colour T edges with 2 colours by brute force-ish
    # (exact search on T, components of max degree 3; T is a subdivision so DFS is fine)
    Tl = sorted(tuple(sorted(e)) for e in T)
    col = {}
    tadj = defaultdict(list)
    for a, b in Tl:
        tadj[a].append(b)
        tadj[b].append(a)
    order = Tl

    def deg(v, c):
        return sum(1 for w in tadj[v] if col.get(frozenset((v, w))) == c)

    def done(v):
        return all(frozenset((v, w)) in col for w in tadj[v])

    def ok_edge(a, b):
        c = col[frozenset((a, b))]
        if done(a) and done(b):
            return deg(a, c) != deg(b, c)
        return True

    sys.setrecursionlimit(100000)
    # simple backtracking ordered by BFS for locality
    idx = {e: i for i, e in enumerate(order)}

    def rec(i):
        if i == len(order):
            return True
        a, b = order[i]
        for c in (0, 1):
            col[frozenset((a, b))] = c
            good = True
            for v in (a, b):
                if done(v):
                    for w in tadj[v]:
                        if not ok_edge(v, w):
                            good = False
            if good and rec(i + 1):
                return True
            del col[frozenset((a, b))]
        return False

    # order edges by BFS
    seen = set()
    bfs = []
    for st in sorted(tadj):
        if st in seen:
            continue
        q = [st]
        seen.add(st)
        while q:
            v = q.pop(0)
            for w in tadj[v]:
                e = tuple(sorted((v, w)))
                if e not in bfs:
                    bfs.append(e)
                if w not in seen:
                    seen.add(w)
                    q.append(w)
    order = bfs
    if not rec(0):
        return False, 'T not 2-colourable'
    return True, 'ok'


if __name__ == '__main__':
    pass
