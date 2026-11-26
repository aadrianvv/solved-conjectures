"""Random check of Lemma 1-prime (thread construction) in 06-revised-local-irregularity.md."""
# Check Lemma 1': H loopless multigraph, max degree <=3, connected, not an odd cycle => S(H) has a
# locally irregular 2-edge-colouring given by the explicit thread construction.
import itertools, random
def verify(adj,col):
    n=len(adj)
    E=[frozenset((u,v)) for u in range(n) for v in adj[u] if u<v]
    def d(v,c): return sum(1 for u in adj[v] if col[frozenset((u,v))]==c)
    return all(d(tuple(e)[0],col[e])!=d(tuple(e)[1],col[e]) for e in E) and len(set(col.values()))<=2
def construct(nv, edges):
    # edges: list of (a,b) multigraph; returns colouring of S(H) edges: dict frozenset((x,('m',i)))->colour
    deg=[0]*nv
    for a,b in edges: deg[a]+=1; deg[b]+=1
    inc=[[] for _ in range(nv)]
    for i,(a,b) in enumerate(edges): inc[a].append(i); inc[b].append(i)
    col={}  # (vertex, edge index) -> colour of half-edge
    big=[v for v in range(nv) if deg[v]==3]
    seen=set()
    def walk(start,e):
        # traverse thread from vertex start along edge e until reaching deg!=2 vertex
        seq=[]; v=start
        while True:
            seq.append(e); a,b=edges[e]; w=b if a==v else a
            if a==b: w=v
            if deg[w]!=2 or w==start and False: return seq,w
            nxt=[f for f in inc[w] if f!=e]
            if not nxt: return seq,w
            # if w has the same edge twice (digon in thread) handle
            f=nxt[0]
            v,e=w,f
            if e in seq: return seq,w
    threads=[]
    for v in range(nv):
        if deg[v]!=2:
            for e in inc[v]:
                if e in seen: continue
                seq,w=walk(v,e)
                for f in seq: seen.add(f)
                threads.append((v,seq,w))
    # remaining edges lie on cycles of degree-2 vertices
    rest=[i for i in range(len(edges)) if i not in seen]
    cyc_comps=[]
    while rest:
        e=rest[0]; a,b=edges[e]
        seq,w=walk(a,e)
        for f in seq: seen.add(f)
        cyc_comps.append((a,seq))
        rest=[i for i in range(len(edges)) if i not in seen]
    edgecol={}  # S(H) edge (x, i) colour
    c={v:0 for v in range(nv)}
    def realize(x,seq,x2,cx,cx2,force_M=False):
        L=len(seq)
        mode='M' if force_M or (cx2-cx-(L-1))%2==0 else 'D'
        v=x; cur=cx
        for k,e in enumerate(seq):
            a,b=edges[e]; w=b if a==v else a
            if mode=='M':
                colr=(cx+k)%2
                edgecol[(v,e)]=colr; edgecol[(w,e)]=colr
            else:
                edgecol[(v,e)]=cur; cur=1-cur; edgecol[(w,e)]=cur
            v=w
    for (x,seq,x2) in threads:
        force=deg[x]==1 or deg[x2]==1
        cx=c[x]; cx2=c[x2]
        if deg[x]==1 and deg[x2]==3: x,x2=x2,x; seq=seq[::-1]; cx,cx2=c[x],c[x2]
        realize(x,seq,x2,cx,cx2,force)
    for (a,seq) in cyc_comps:
        L=len(seq)
        if L%2==1: return None
        realize(a,seq,a,0,0,False)  # even: choose M alternating
    return edgecol
def check(nv,edges):
    ec=construct(nv,edges)
    if ec is None: return None
    # build S(H) adjacency
    N=nv+len(edges); adj=[[] for _ in range(N)]
    colour={}
    for i,(a,b) in enumerate(edges):
        m=nv+i
        for x in (a,b):
            adj[x].append(m); adj[m].append(x); colour[frozenset((x,m))]=2+ec[(x,i)]
    return verify(adj,colour)
rng=random.Random(1); tested=0
for trial in range(20000):
    nv=rng.randint(1,7)
    edges=[]
    deg=[0]*nv
    for t in range(rng.randint(0,11)):
        a,b=rng.randrange(nv),rng.randrange(nv)
        if a==b or deg[a]>=3 or deg[b]>=3: continue
        edges.append((a,b)); deg[a]+=1; deg[b]+=1
    # connected & nonempty
    used=[v for v in range(nv) if deg[v]>0]
    if not edges: continue
    par={v:v for v in used}
    def f(x):
        while par[x]!=x: x=par[x]
        return x
    for a,b in edges: par[f(a)]=f(b)
    if len({f(v) for v in used})!=1: continue
    vs=sorted(used); idx={v:i for i,v in enumerate(vs)}
    E=[(idx[a],idx[b]) for a,b in edges]; n2=len(vs)
    oddcycle = all(deg[v]==2 for v in used) and len(edges)%2==1
    r=check(n2,E)
    if oddcycle: assert r is None
    else: assert r is True,(n2,E)
    tested+=1
print("Lemma 1' construction verified on",tested,"random connected subcubic multigraphs")
