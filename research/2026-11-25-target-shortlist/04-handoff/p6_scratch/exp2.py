import sys
from random import Random
from collections import Counter
from plant import planted
from gen import ncherries
from strat import solve, STRATS, to_rs, verify
rng = Random(int(sys.argv[1])); G = int(sys.argv[2]); names = sys.argv[3].split(',')
Ns = [int(x) for x in sys.argv[4].split(',')] if len(sys.argv) > 4 else [10,12,14,16,18,20,24]
tal = Counter()
for N in Ns:
    for g in range(G):
        res = planted(N, rng, p=rng.choice([0.6, 0.8, 1.0]))
        if res is None: tal['nogen'] += 1; continue
        adj, m = res
        tal[('cherries', N)] += ncherries(adj, m); tal[('inst', N)] += 1
        for nm in names:
            try: a = solve(adj, m, STRATS[nm], node_limit=300000, rng=rng)
            except TimeoutError: tal[(nm,'TO')] += 1; continue
            if a is None:
                tal[(nm,'fail')] += 1
                if tal[(nm,'fail')] <= 2: print('FAIL', nm, [sorted(x) for x in adj], m, flush=True)
            else:
                r, s = to_rs(adj, m, a); verify(adj, m, r, s); tal[(nm,'ok')] += 1
print(sorted(tal.items(), key=str))
