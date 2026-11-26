import sys
from random import Random
from collections import Counter
sys.argv = ["x", "1", "8", "0"]
exec(open("p5small.py").read().replace("main()\n", ""))
rng = Random(5)
for N, cnt in ((8, 40), (10, 60), (12, 40)):
    tally = Counter()
    for g in range(cnt):
        adj = random_5reg(N, rng)
        ok = 0; tot = 0
        for m in matchings(adj):
            tot += 1
            res = solve(adj, m, rng=rng, node_limit=500000)
            if res is not None:
                ok += 1
        tally["graphs"] += 1
        tally["no good M"] += (ok == 0)
        if ok == 0:
            print("no M works:", N, [sorted(a) for a in adj], "matchings", tot)
    print(N, dict(tally))
