import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_sweep_pipeline import random_matched_graph
from random import Random
from collections import Counter
from an1 import random_5reg, matchings
from r0 import r0
rng=Random(int(sys.argv[1])); T=int(sys.argv[2])
def maxt(adj,m): return max(len(adj[u]&adj[m[u]]) for u in range(len(adj)))
tal=Counter()
for N in (10,12,14,16):
    for g in range(int(sys.argv[3])):
        if rng.random()<0.3: adj=random_5reg(N,rng)
        else: adj,_=random_matched_graph(N,rng,rng.choice(["square","dense"]))
        k=0
        for m in matchings(adj):
            k+=1
            if k>100: break
            if maxt(adj,m)>T: continue
            try: ok=r0(adj,m)
            except TimeoutError: tal['to']+=1; continue
            tal[(N,ok)]+=1
            if not ok and tal[(N,False)]<=2: print("FAIL",[sorted(a) for a in adj],m,flush=True)
print(tal)
