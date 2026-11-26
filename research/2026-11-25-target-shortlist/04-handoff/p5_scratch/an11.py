import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
from modes import solve
from an1 import matchings
from collections import Counter
def cnt(adj,m): return sum(len(adj[u]&adj[m[u]]) for u in range(len(adj)))//2
tal=Counter()
for order in (8,10):
    classes=[]
    for g in regular_graphs(order,5):
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(k==key and isomorphic(g,h,lab,hl) for k,h,hl in classes): continue
        classes.append((key,g,lab))
    for _,g,_ in classes:
        adj=[set(list_bits(a)) for a in g]
        ms=list(matchings(adj)); tmin=min(cnt(adj,m) for m in ms)
        has={'TC':False,'R0':False}; minall={'TC':True,'R0':True}
        for m in ms:
            for mode in ('TC','R0'):
                ok=solve(adj,m,mode) is not None
                has[mode]|=ok
                if cnt(adj,m)==tmin and not ok: minall[mode]=False
        for mode in ('TC','R0'):
            tal[(order,mode,'graph has M',has[mode])]+=1
            tal[(order,mode,'all min M ok',minall[mode])]+=1
for k,v in sorted(tal.items()): print(k,v)
