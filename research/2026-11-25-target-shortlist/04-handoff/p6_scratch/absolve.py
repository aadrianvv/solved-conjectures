"""Abstract (P3)+(P5) solver (original orientation).  H: list of edges (u,v) (internal) ; half-edges (u,None) with
fixed role.  cherries: list of (x, e1, e2) edge ids at apex x.  Roles at a vertex: Ri,Ro,Si,So exactly once.
Bad cherry role sets: {Ri,Si}, {Ri,Ro}."""
from itertools import permutations
BAD = {frozenset(('Ri','Si')), frozenset(('Ri','Ro'))}
COMP = {'Ri':'Ro','Ro':'Ri','Si':'So','So':'Si'}
def solve(nv, edges, cherries, fixed=None, node_limit=10**6, want_all=False):
    inc = [[] for _ in range(nv)]
    for i,(u,v) in enumerate(edges):
        inc[u].append(i)
        if v is not None: inc[v].append(i)
    assert all(len(l)==4 for l in inc), [len(l) for l in inc]
    chx = [[] for _ in range(nv)]
    for x,e1,e2 in cherries: chx[x].append((e1,e2))
    fixed = fixed or {}
    doms = []
    for x in range(nv):
        d = []
        for p in permutations(('Ri','Ro','Si','So')):
            a = dict(zip(inc[x], p))
            if any(frozenset((a[e1],a[e2])) in BAD for e1,e2 in chx[x]): continue
            if any(e in fixed and edges[e][1] is None and a[e]!=fixed[e] for e in inc[x]): continue
            d.append(a)
        doms.append(d)
    other = lambda e,x: edges[e][1] if edges[e][0]==x else edges[e][0]
    asg=[None]*nv; cur=[list(d) for d in doms]; nodes=[0]; sols=[]
    def rec():
        nodes[0]+=1
        if nodes[0]>node_limit: raise TimeoutError
        best=None
        for v in range(nv):
            if asg[v] is None and (best is None or len(cur[v])<len(cur[best])): best=v
        if best is None:
            sols.append(list(asg)); return not want_all
        v=best
        for a in cur[v]:
            asg[v]=a; saved=[]; ok=True
            for e in inc[v]:
                w=other(e,v)
                if w is None or asg[w] is not None: continue
                saved.append((w,cur[w])); cur[w]=[b for b in cur[w] if b[e]==COMP[a[e]]]
                if not cur[w]: ok=False; break
            if ok and rec(): return True
            for w,d in reversed(saved): cur[w]=d
            asg[v]=None
        return False
    rec()
    return sols
