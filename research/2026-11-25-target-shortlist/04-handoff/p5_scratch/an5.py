import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
from p5solve import solve
from aligned import aligned_orientation
from an1 import matchings
from random import Random
from collections import Counter
rng=Random(1)
def cnt(adj,m): return sum(len(adj[u]&adj[m[u]]) for u in range(len(adj)))//2
tal=Counter()
for order in (8,10):
    classes=[]
    for g in regular_graphs(order,5):
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(k==key and isomorphic(g,h,lab,hl) for k,h,hl in classes): continue
        classes.append((key,g,lab))
    gi=0
    for _,g,_ in classes:
        adj=[set(list_bits(a)) for a in g]
        ms=list(matchings(adj)); tmin=min(cnt(adj,m) for m in ms)
        anyS=False; minS=True
        for m in ms:
            S=aligned_orientation(adj,m) is not None
            ok=solve(adj,m,rng=rng,node_limit=10**6) is not None
            tal[(order,'S',S,'feas',ok,'min',cnt(adj,m)==tmin)]+=1
            anyS|=S
            if cnt(adj,m)==tmin and not S: minS=False
        tal[(order,'graph has S-matching',anyS)]+=1
        tal[(order,'all min matchings S',minS)]+=1
for k,v in sorted(tal.items()): print(k,v)
