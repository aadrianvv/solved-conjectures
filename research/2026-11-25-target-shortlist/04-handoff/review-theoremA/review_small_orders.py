"""Referee scratch: random 5-regular graphs of orders 8-16, ALL perfect matchings, hypothesis filter,
then the independent construction + sweep (several constructions each)."""
import sys
from collections import Counter
from random import Random
sys.path.insert(0, ".")
import check_regular_path_theoremA_independent as C

def all_pms(adj):
    out = []
    def go(free, m):
        if not free:
            out.append(dict(m)); return
        u = min(free)
        for v in adj[u]:
            if v in free:
                m[u], m[v] = v, u
                go(free - {u, v}, m)
                del m[u], m[v]
    go(frozenset(adj), {})
    return out

def rand5(n, rng):
    while True:
        stubs = [v for v in range(n) for _ in range(5)]
        rng.shuffle(stubs)
        es = {C.E(stubs[2*i], stubs[2*i+1]) for i in range(len(stubs)//2)}
        if len(es) == 5*n//2 and all(a != b for a, b in es):
            adj = {v: set() for v in range(n)}
            for a, b in es:
                adj[a].add(b); adj[b].add(a)
            return adj

rng = Random(11)
st = Counter()
seen = set()
for n, reps in ((8, 300), (10, 600), (12, 300), (14, 150), (16, 80)):
    for _ in range(reps):
        adj = rand5(n, rng)
        key = (n, tuple(sorted(Counter(len(adj[u] & adj[v]) for u in adj for v in adj[u]).items())))
        pms = all_pms(adj) if n <= 14 else [C.random_pm(adj, rng) for _ in range(40)]
        for m in pms:
            if m is None:
                continue
            st[(n, "matchings")] += 1
            if C.bad_pairs(adj, m):
                continue
            st[(n, "hypothesis matchings")] += 1
            st[(n, "with M-triangles")] += C.m_triangle_count(adj, m) > 0
            for _ in range(3):
                r, s = C.lemma1(adj, m, rng)
                C.check_P(adj, m, r, s)
                stats = Counter()
                pieces = C.sweep(adj, m, r, s, rng, stats, True)
                assert not C.verify_decomposition(adj, pieces)
                st[(n, "verified")] += 1
                st[(n, "defects")] += stats["defects"]
                st[(n, "odd cycles")] += stats["odd cycles"]
for k in sorted(st): print(k, st[k])
