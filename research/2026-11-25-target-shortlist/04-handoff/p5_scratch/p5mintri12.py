import sys
from random import Random
from collections import Counter
from itertools import combinations
sys.argv = ["x", "1", "8", "0"]
exec(open("p5small.py", encoding="utf-8-sig").read().replace("main()\n", ""))
def ntri(adj, m):
    return sum(1 for c in range(len(adj)) for x, y in combinations([w for w in adj[c] if w != m[c]], 2) if m[x] == y)
rng = Random(77)
stats = Counter()
for N, cnt in ((12, 150), (14, 60)):
    for g in range(cnt):
        adj = random_5reg(N, rng)
        ms = list(matchings(adj))
        tmin = min(ntri(adj, m) for m in ms)
        mins = [m for m in ms if ntri(adj, m) == tmin]
        ok = 0
        for m in mins[:30]:
            try:
                res = solve(adj, m, rng=rng, node_limit=300000)
            except TimeoutError:
                stats[(N, "timeout")] += 1; continue
            ok += res is not None
            stats[(N, "minM sat" if res else "minM UNSAT")] += 1
            if res is None:
                print("UNSAT at min-tri", N, tmin, [sorted(a) for a in adj], m, flush=True)
        stats[(N, "graphs")] += 1
        stats[(N, "graphs with no P5 among checked min M")] += ok == 0
print(sorted(stats.items()))
