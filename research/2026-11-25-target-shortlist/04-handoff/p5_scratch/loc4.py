"""Is (P5) feasible for every matching M with no incidence-reducing alternating 4-cycle (resp. 6-cycle)?"""
import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from collections import Counter
def w(adj,u,v): return len(adj[u]&adj[v])
def improving(adj,m,L):
    n=len(adj)
    # alternating cycles of length 2L: M-edges e1..eL, non-M edges between consecutive
    def dfs(start,cur,used,gain,depth):
        # cur: vertex at end of an M-edge traversal; next take non-M edge cur->v, then M-edge v->m[v]
        for v in adj[cur]:
            if v==m[cur]: continue
            if v==start and depth>=2:
                if gain + w(adj,cur,v) < 0: return True
                continue
            if v in used or m[v] in used: continue
            if depth>=L: continue
            g=gain+w(adj,cur,v)-w(adj,v,m[v])
            if dfs(start,m[v],used|{v,m[v]},g,depth+1): return True
        return False
    for s in range(n):
        # start at s, first M-edge s-m[s] traversed from s to m[s]
        if dfs(s,m[s],{s,m[s]},-w(adj,s,m[s]),1): return True
    return False
if __name__=="__main__":
    from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
    from p5solve import solve
    from an1 import matchings
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
                ok=solve(adj,m,node_limit=10**6) is not None
                i2=improving(adj,m,2); i3=improving(adj,m,3)
                tal[(order,'feas',ok,'imp4',i2,'imp<=6',i3)]+=1
    for k,v in sorted(tal.items()): print(k,v)
