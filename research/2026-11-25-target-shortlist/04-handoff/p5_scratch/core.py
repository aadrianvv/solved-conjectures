import sys, ast
from itertools import combinations
def solve_pairs(adj,m,active):
    """active: set of (apex,y,z). CSP like p5solve but only active pairs constrained."""
    n=len(adj)
    H=[sorted(w for w in adj[v] if w!=m[v]) for v in range(n)]
    doms=[]
    for v in range(n):
        prs=[(y,z) for (x,y,z) in active if x==v]
        dom=[]
        for Rset in combinations(range(4),2):
            if any({H[v].index(y),H[v].index(z)}==set(Rset) for y,z in prs): continue
            Sset=[i for i in range(4) if i not in Rset]
            for rin in Rset:
                for sin in Sset:
                    a=tuple((i in Rset, i==rin or i==sin) for i in range(4))
                    if any(a[H[v].index(y)][1] and a[H[v].index(z)][1] for y,z in prs): continue
                    dom.append(a)
        doms.append(dom)
    assign=[None]*n
    cur=[list(d) for d in doms]
    def ok(u,a,v,b):
        iu=H[u].index(v); iv=H[v].index(u)
        return a[iu][0]==b[iv][0] and a[iu][1]!=b[iv][1]
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
    return rec()
def allpairs(adj,m):
    n=len(adj)
    return [(x,y,z) for x in range(n) for y,z in combinations(sorted(w for w in adj[x] if w!=m[x]),2) if m[y]==z]
def mincore(adj,m):
    P=allpairs(adj,m)
    assert not solve_pairs(adj,m,set(P))
    core=list(P)
    for p in P:
        trial=[q for q in core if q!=p]
        if not solve_pairs(adj,m,set(trial)): core=trial
    return core
if __name__=="__main__":
    adj=[set(x) for x in ast.literal_eval(sys.argv[1])]
    mm=ast.literal_eval(sys.argv[2]); m={}
    for u,v in mm.items(): m[u]=v; m[v]=u
    print("pairs",allpairs(adj,m))
    print("core",mincore(adj,m))
