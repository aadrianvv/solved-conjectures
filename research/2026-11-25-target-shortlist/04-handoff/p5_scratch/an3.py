import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from p5solve import solve
from check_regular_path_sweep_pipeline import random_matched_graph
from random import Random
from collections import Counter
from itertools import combinations
from an1 import random_5reg, matchings
rng=Random(int(sys.argv[1]))
def maxt(adj,m): return max(len(adj[u]&adj[m[u]]) for u in range(len(adj)))
tal=Counter()
for N,cnt in ((12,int(sys.argv[2])),(14,int(sys.argv[2])//2)):
    for g in range(cnt):
        if g%2==0: adj=random_5reg(N,rng)
        else: adj,_=random_matched_graph(N,rng,rng.choice(["square","dense"]))
        k=0
        for m in matchings(adj):
            k+=1
            if k>200: break
            if maxt(adj,m)>2: continue
            try: ok=solve(adj,m,rng=rng,node_limit=300000) is not None
            except TimeoutError: tal['to']+=1; continue
            tal[(N,ok)]+=1
            if not ok: print("COUNTER",[sorted(a) for a in adj],m,flush=True)
print(tal)
