import sys
from random import Random
from collections import Counter
from gen import graph, class_matchings, ncherries
from strat import solve, STRATS, to_rs, verify
rng = Random(int(sys.argv[1])); G = int(sys.argv[2])
names = sys.argv[3].split(',')
tal = Counter()
for N in (10, 12, 14, 16, 18, 20):
    for g in range(G):
        adj = graph(N, rng)
        for m in class_matchings(adj, rng, limit=15):
            if ncherries(adj, m) == 0: continue
            tal[(N,'inst')] += 1
            for nm in names:
                try: a = solve(adj, m, STRATS[nm], node_limit=200000, rng=rng)
                except TimeoutError: tal[(nm,'TO')] += 1; continue
                if a is None:
                    tal[(nm,'fail')] += 1
                    if tal[(nm,'fail')] <= 1: print('FAIL', nm, [sorted(x) for x in adj], m, flush=True)
                else:
                    r, s = to_rs(adj, m, a); verify(adj, m, r, s); tal[(nm,'ok')] += 1
print(sorted(tal.items(), key=str))
