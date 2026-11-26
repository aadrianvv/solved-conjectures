"""Exhaustive abstract check: all 4-regular simple graphs of order n (iso classes), all maximal cherry systems with
K-in-degree <= 1 (target pairs pairwise disjoint; optionally targets non-adjacent).  Each instance solved by absolve."""
import sys, time
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
from itertools import combinations
from collections import Counter
from absolve import solve
def classes(n):
    cl=[]
    for g in regular_graphs(n,4):
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(k==key and isomorphic(g,h,lab,hl) for k,h,hl in cl): continue
        cl.append((key,g,lab))
    return [g for _,g,_ in cl]
def maximal_systems(n, adj, nonadj):
    cands=[(x,y,z) for x in range(n) for y,z in combinations(sorted(adj[x]),2) if (not nonadj or z not in adj[y])]
    out=[]
    def compatible(sys_, c):
        x,y,z=c
        tg=set(); ends=set()
        for (a,b,d) in sys_:
            tg|={b,d}; ends|={(a,b),(a,d)}
        return y not in tg and z not in tg and (x,y) not in ends and (x,z) not in ends
    def rec(i, cur):
        if i==len(cands):
            if all(c in cur or not compatible(cur,c) for c in cands): out.append(list(cur))
            return
        c=cands[i]
        if compatible(cur,c):
            cur.append(c); rec(i+1,cur); cur.pop()
        rec(i+1,cur)
    rec(0,[])
    return out
if __name__=="__main__":
    nonadj = sys.argv[2]=='nonadj'
    for n in [int(a) for a in sys.argv[1].split(',')]:
        t0=time.time(); tal=Counter()
        for g in classes(n):
            adj=[set(list_bits(a)) for a in g]
            es=sorted({(min(u,v),max(u,v)) for u in range(n) for v in adj[u]}); eid={e:i for i,e in enumerate(es)}
            E=lambda a,b: eid[(min(a,b),max(a,b))]
            for S in maximal_systems(n,adj,nonadj):
                ch=[(x,E(x,y),E(x,z)) for x,y,z in S]
                ok=bool(solve(n,es,ch,node_limit=10**7))
                tal[ok]+=1
                if not ok: print("INFEASIBLE n=%d"%n, es, S, flush=True)
            tal['graphs']+=1
        print(n, dict(tal), "%.1fs"%(time.time()-t0), flush=True)
