from itertools import combinations
from collections import Counter
from p5solve import solve
adj = [set(x) for x in [[1,2,3,4,7],[0,3,4,5,6],[0,3,5,6,7],[0,1,2,4,5],[0,1,3,6,7],[1,2,3,6,7],[1,2,4,5,7],[0,2,4,5,6]]]
def matchings(free):
    if not free: yield {}; return
    u = min(free)
    for v in adj[u]:
        if v in free:
            for m in matchings(free - {u, v}):
                m = dict(m); m[u] = v; m[v] = u; yield m
def ntri(m):
    return sum(1 for c in range(8) for x, y in combinations([w for w in adj[c] if w != m[c]], 2) if m[x] == y)
t = Counter()
for m in matchings(frozenset(range(8))):
    t[(ntri(m), solve(adj, m) is not None)] += 1
print(sorted(t.items()))
