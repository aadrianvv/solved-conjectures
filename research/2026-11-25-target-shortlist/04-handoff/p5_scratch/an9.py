import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
from core import solve_pairs, allpairs, mincore
from an1 import matchings
from collections import Counter
def signature(adj,m,core):
    # describe core: for each core pair (apex,y,z): number of apexes on fibre {y,z} within core, whether apex's own fibre is a core fibre, etc.
    fibres=Counter(frozenset((y,z)) for x,y,z in core)
    apexes=[x for x,y,z in core]
    desc=[]
    for x,y,z in core:
        F=frozenset((y,z))
        own=frozenset((x,m[x]))
        desc.append((fibres[F], own in fibres, sum(1 for a in apexes if a==x)))
    return tuple(sorted(desc)), len(core)
tal=Counter()
for order in (8,10):
    classes=[]
    for g in regular_graphs(order,5):
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(k==key and isomorphic(g,h,lab,hl) for k,h,hl in classes): continue
        classes.append((key,g,lab))
    for _,g,_ in classes:
        adj=[set(list_bits(a)) for a in g]
        for m in matchings(adj):
            if solve_pairs(adj,m,set(allpairs(adj,m))): continue
            c=mincore(adj,m)
            tal[signature(adj,m,c)]+=1
for k,v in sorted(tal.items(),key=lambda t:-t[1]): print(v,k)
