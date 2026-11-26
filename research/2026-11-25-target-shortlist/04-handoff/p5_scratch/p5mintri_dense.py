import sys
sys.path.insert(0, "../..")
from random import Random
from collections import Counter
from itertools import combinations
from p5solve import solve
from check_regular_path_sweep_pipeline import random_matched_graph
def matchings(adj, cap=20000):
    n = len(adj); out = []
    def go(free, m):
        if len(out) >= cap: return
        if not free:
            out.append(dict(m)); return
        u = min(free)
        for v in adj[u]:
            if v in free:
                m[u] = v; m[v] = u
                go(free - {u, v}, m)
                del m[u], m[v]
    go(frozenset(range(n)), {})
    return out
def ntri(adj, m):
    return sum(1 for c in range(len(adj)) for x, y in combinations([w for w in adj[c] if w != m[c]], 2) if m[x] == y)
rng = Random(9); st = Counter()
for style, n in [("k5", 10), ("k5", 20), ("square", 12), ("square", 16), ("dense", 12), ("dense", 16)]:
    for _ in range(15):
        adj, _m = random_matched_graph(n, rng, style)
        ms = matchings(adj)
        t = min(ntri(adj, m) for m in ms)
        mins = [m for m in ms if ntri(adj, m) == t]
        rng.shuffle(mins)
        okc = 0
        for m in mins[:10]:
            try:
                res = solve(adj, m, rng=rng, node_limit=300000)
            except TimeoutError:
                st[(style, "timeout")] += 1; continue
            okc += res is not None
            st[(style, "minM sat" if res is not None else "minM UNSAT")] += 1
        st[(style, "graphs")] += 1
        st[(style, "mintri>0")] += t > 0
        st[(style, "graph with no feasible min M")] += okc == 0
print(sorted(st.items()))
