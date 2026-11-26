"""Scratch: run the AUTHOR's end-to-end code on the referee's planted generic instances."""
import sys
sys.path.insert(0, ".")
from collections import Counter
from random import Random
import check_regular_path_theoremB_independent as B
import check_regular_path_diamond_free as D

rng = Random(int(sys.argv[1]) if len(sys.argv) > 1 else 9)
N = int(sys.argv[2]) if len(sys.argv) > 2 else 600
st = Counter()
for _ in range(N):
    P = B.plant_random(rng, rng.randint(1, 5))
    if P is None:
        continue
    inst = B.complete_and_repair(P, rng, rng.choice((4, 8, 14, 24)))
    if inst is None:
        continue
    adj, m, r, s = inst
    n = len(adj)
    trails = {}
    for u in range(n):
        v = m[u]
        if u < v:
            trails[(u, v)] = (s[r[u]], r[u], u, v, r[v], s[r[v]])
    a = [set(adj[v]) for v in range(n)]
    probe = Counter()
    try:
        D.solve_one(a, m, r, s, trails, probe)
        st["author ok"] += 1
    except Exception as ex:
        st["author FAIL " + str(ex)[:60]] += 1
    for k, v in probe.items():
        st[k] += v
for k in sorted(st):
    print(k, st[k])
