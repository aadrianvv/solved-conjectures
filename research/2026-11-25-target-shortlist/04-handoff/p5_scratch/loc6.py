import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_sweep_pipeline import random_matched_graph
from random import Random
from collections import Counter
from an1 import random_5reg, matchings
from p5solve import solve
from loc4 import improving
rng=Random(int(sys.argv[1]))
tal=Counter()
for N in (12,14):
    for g in range(int(sys.argv[2])):
        if rng.random()<0.3: adj=random_5reg(N,rng)
        else: adj,_=random_matched_graph(N,rng,rng.choice(["square","dense"]))
        k=0
        for m in matchings(adj):
            k+=1
            if k>120: break
            if improving(adj,m,3): continue   # only matchings with no improving cycle of length <= 6
            try: ok=solve(adj,m,rng=rng,node_limit=300000) is not None
            except TimeoutError: tal['to']+=1; continue
            tal[(N,ok)]+=1
            if not ok: print("LOCAL6 FAIL",N,[sorted(a) for a in adj],m,"imp8",improving(adj,m,4),flush=True)
print(sorted(tal.items()))
