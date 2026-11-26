"""(R0): directed 2-factor R of H=G-M with r(x) outside the cherry fibres of every singly-paired apex x,
and at each D2 apex R uses one edge to each cherry fibre; then T-demands x -> m(r(x)) at D2 apexes must be
consistent on T-cycles.  (Omega-form; equivalent to (P5) feasibility restricted to such R.)"""
from itertools import combinations
def r0(adj,m,node_limit=2*10**6):
    n=len(adj)
    H=[sorted(w for w in adj[v] if w!=m[v]) for v in range(n)]
    fib=[{y,m[y]} for y in range(n)]
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
                if nf[x]==1 and o in B[x]: continue
                if nf[x]==2 and m[i]==o: continue
                d.append((i,o))
        doms.append(d)
    asg=[None]*n; cnt=[0]
    def consistent(x,a):
        i,o=a
        for y in H[x]:
            b=asg[y]
            if b is None: continue
            # edge xy is R iff y in a; must agree
            xr = y in a; yr = x in b
            if xr!=yr: return False
            if xr:
                if (o==y) != (b[0]==x): return False
        return True
    def tcheck():
        # T-successor demands at D2 apexes
        T={x:[y for y in H[x] if y not in asg[x]] for x in range(n)}
        dem={}
        for x in range(n):
            if nf[x]==2:
                w=m[asg[x][1]]
                if w not in T[x]: return False
                dem[x]=w
        seen=set()
        for s in range(n):
            if s in seen: continue
            cyc=[s]; prev=None; cur=s
            while True:
                nx=T[cur][0] if T[cur][0]!=prev else T[cur][1]
                if prev is None: nx=T[cur][0]
                if nx==s: break
                cyc.append(nx); prev,cur=cur,nx
            seen|=set(cyc)
            L=len(cyc); pos={v:k for k,v in enumerate(cyc)}
            dirs=set()
            for v in cyc:
                if v in dem:
                    dirs.add(cyc[(pos[v]+1)%L]==dem[v])
            if len(dirs)>1: return False
        return True
    def rec():
        cnt[0]+=1
        if cnt[0]>node_limit: raise TimeoutError
        best=None;bd=None
        for x in range(n):
            if asg[x] is None:
                c=[a for a in doms[x] if consistent(x,a)]
                if best is None or len(c)<len(bd): best,bd=x,c
                if not c: return False
        if best is None: return tcheck()
        for a in bd:
            asg[best]=a
            if rec(): return True
            asg[best]=None
        return False
    return rec()
