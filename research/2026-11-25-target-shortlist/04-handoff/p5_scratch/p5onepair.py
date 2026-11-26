import sys
from random import Random
from collections import Counter
from itertools import combinations
sys.argv = ["x", "1", "8", "0"]
exec(open("p5small.py").read().replace("main()\n", ""))
rng = Random(11)
def maxpairs(adj, m):
    best = 0
    for c in range(len(adj)):
        nb = [w for w in adj[c] if w != m[c]]
        best = max(best, sum(1 for x, y in combinations(nb, 2) if m[x] == y))
    return best
for N, cnt in ((8, 400), (10, 400), (12, 300), (14, 200)):
    tally = Counter()
    for g in range(cnt):
        adj = random_5reg(N, rng)
        for k, m in enumerate(matchings(adj)):
            if k > 40: break
            mp = maxpairs(adj, m)
            try:
                res = solve(adj, m, rng=rng, node_limit=300000)
            except TimeoutError:
                tally[(mp, "timeout")] += 1; continue
            tally[(mp, "sat" if res else "UNSAT")] += 1
            if res is None and mp <= 1:
                print("UNSAT with maxpairs<=1", N, [sorted(a) for a in adj], m)
    print(N, sorted(tally.items()))
