"""(TC): directed 2-factor T of H (permutation t, t(v)~v, no 2-cycles) with t(x) in a cherry fibre of x for every apex x
(and at D2 apexes t^{-1}(x) in the other cherry fibre)."""
from itertools import combinations
def tc(adj,m,node_limit=10**6):
    n=len(adj)
    H=[sorted(w for w in adj[v] if w!=m[v]) for v in range(n)]
    B=[set() for _ in range(n)]; nf=[0]*n
    for x in range(n):
        for y,z in combinations(H[x],2):
            if m[y]==z: B[x]|={y,z}; nf[x]+=1
    doms=[]
    for x in range(n):
        d=[]
        for i in H[x]:
            for o in H[x]:
                if i==o: continue
                if nf[x]>=1 and o not in B[x]: continue
                if nf[x]==2 and m[i]==o: continue
                d.append((i,o))
        doms.append(d)
    asg=[None]*n; cnt=[0]
    def cons(x,a):
        i,o=a
        for y in H[x]:
            b=asg[y]
            if b is None: continue
            if (o==y)!=(b[0]==x): return False
            if (i==y)!=(b[1]==x): return False
        return True
    def rec():
        cnt[0]+=1
        if cnt[0]>node_limit: raise TimeoutError
        best=None;bd=None
        for x in range(n):
            if asg[x] is None:
                c=[a for a in doms[x] if cons(x,a)]
                if best is None or len(c)<len(bd): best,bd=x,c
                if not c: return False
        if best is None: return True
        for a in bd:
            asg[best]=a
            if rec(): return True
            asg[best]=None
        return False
    return rec()
