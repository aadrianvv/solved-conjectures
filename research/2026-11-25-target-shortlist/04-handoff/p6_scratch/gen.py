import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_sweep_pipeline import random_matched_graph
from random import Random
def random_5reg(n, rng):
    while True:
        pts = [v for v in range(n) for _ in range(5)]
        rng.shuffle(pts)
        adj = [set() for _ in range(n)]
        ok = True
        for i in range(0, len(pts), 2):
            u, v = pts[i], pts[i + 1]
            if u == v or v in adj[u]: ok = False; break
            adj[u].add(v); adj[v].add(u)
        if ok: return adj
def graph(n, rng):
    t = rng.random()
    if t < 0.2: return random_5reg(n, rng)
    sty = rng.choice(["square", "dense"] + (["k5"] if n % 5 == 0 else []))
    return random_matched_graph(n, rng, sty)[0]
def class_matchings(adj, rng, limit=50, maxt=1):
    n = len(adj)
    ok = lambda u, v: len(adj[u] & adj[v]) <= maxt
    out = []
    def go(free, m):
        if len(out) >= limit: return
        if not free: out.append(dict(m)); return
        u = min(free, key=lambda x: sum(1 for y in adj[x] if y in free and ok(x, y)))
        c = [v for v in adj[u] if v in free and ok(u, v)]
        rng.shuffle(c)
        for v in c:
            m[u] = v; m[v] = u
            go(free - {u, v}, m)
            del m[u], m[v]
            if len(out) >= limit: return
    go(frozenset(range(n)), {})
    return out
def ncherries(adj, m):
    return sum(len(adj[u] & adj[m[u]]) for u in range(len(adj))) // 2
