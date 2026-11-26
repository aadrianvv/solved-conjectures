import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_sweep_pipeline import random_matched_graph
from random import Random
from collections import Counter
from an1 import random_5reg, matchings
from aligned import aligned_orientation
from modes import solve
rng=Random(int(sys.argv[1]))
def tris(adj,m):
    return [(x,u,m[u]) for u in range(len(adj)) if u<m[u] for x in adj[u]&adj[m[u]]]
def classK(adj,m):
    T=tris(adj,m); seen=set()
    for t in T:
        if seen&set(t): return False
        seen|=set(t)
    return True
tal=Counter()
for N in (10,12,14,16,18):
    for g in range(int(sys.argv[2])):
        if rng.random()<0.3: adj=random_5reg(N,rng)
        else: adj,_=random_matched_graph(N,rng,rng.choice(["square","dense"]))
        k=0
        for m in matchings(adj):
            k+=1
            if k>150: break
            if not classK(adj,m) or not tris(adj,m): continue
            S=aligned_orientation(adj,m) is not None
            tal[(N,'S',S)]+=1
            if not S:
                for mode in ('TC','R0'):
                    try: tal[(N,mode,solve(adj,m,mode,node_limit=300000) is not None)]+=1
                    except TimeoutError: tal['to']+=1
print(sorted(tal.items()))
