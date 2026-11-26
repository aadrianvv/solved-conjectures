"""Sufficient condition (S): Euler orientation of H=G-M with every M-pair aligned (both out or both in at its apex)."""
from itertools import combinations
def pairs(adj,m):
    n=len(adj)
    return [(x,y,z) for x in range(n) for y,z in combinations(sorted(w for w in adj[x] if w!=m[x]),2) if m[y]==z]
def aligned_orientation(adj,m):
    n=len(adj)
    H=[sorted(w for w in adj[v] if w!=m[v]) for v in range(n)]
    P=pairs(adj,m)
    doms=[]
    for v in range(n):
        prs=[(H[v].index(y),H[v].index(z)) for (x,y,z) in P if x==v]
        dom=[]
        for outs in combinations(range(4),2):
            a=tuple(i in outs for i in range(4))
            if all(a[i]==a[j] for i,j in prs): dom.append(a)
        doms.append(dom)
    assign=[None]*n; cur=[list(d) for d in doms]
    def ok(u,a,v,b):
        return a[H[u].index(v)]!=b[H[v].index(u)]
    def rec():
        best=None
        for v in range(n):
            if assign[v] is None and (best is None or len(cur[v])<len(cur[best])): best=v
        if best is None: return True
        v=best
        for a in cur[v]:
            assign[v]=a; saved=[]; good=True
            for w in H[v]:
                if assign[w] is None:
                    saved.append((w,cur[w])); cur[w]=[b for b in cur[w] if ok(v,a,w,b)]
                    if not cur[w]: good=False;break
            if good and rec(): return True
            for w,d in reversed(saved): cur[w]=d
            assign[v]=None
        return False
    if not rec(): return None
    return {(v,H[v][i]) for v in range(n) for i in range(4) if assign[v][i]}
