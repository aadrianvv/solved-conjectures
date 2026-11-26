import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
from p5solve import solve
from random import Random
from collections import Counter
from itertools import combinations
rng=Random(1)
def matchings(adj):
    n=len(adj)
    def go(free):
        if not free: yield {}; return
        u=min(free)
        for v in adj[u]:
            if v in free:
                for m in go(free-{u,v}):
                    m=dict(m); m[u]=v; m[v]=u; yield m
    yield from go(frozenset(range(n)))
def feats(adj,m):
    n=len(adj)
    t=[len((adj[u]&adj[m[u]])) for u in range(n)]  # triangles on M-edge at u
    maxt=max(t)
    d2=sum(1 for c in range(n) if sum(1 for x,y in combinations([w for w in adj[c] if w!=m[c]],2) if m[x]==y)==2)
    return maxt,d2,sum(t)//2
tal=Counter()
for order in (8,10):
    classes=[]
    for g in regular_graphs(order,5):
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(k==key and isomorphic(g,h,lab,hl) for k,h,hl in classes): continue
        classes.append((key,g,lab))
    for _,g,_ in classes:
        adj=[set(list_bits(a)) for a in g]
        ms=list(matchings(adj))
        tmin=min(feats(adj,m)[2] for m in ms)
        for m in ms:
            maxt,d2,tot=feats(adj,m)
            ok=solve(adj,m,rng=rng,node_limit=10**6) is not None
            tal[(order,'maxt',maxt,'d2>0',d2>0,'min',tot==tmin,ok)]+=1
for k,v in sorted(tal.items()): print(k,v)
