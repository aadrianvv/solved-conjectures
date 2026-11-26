"""Search 2-port gadgets (2-edge-cut sides) with class cherries whose interface set is restricted."""
import sys
from random import Random
from itertools import product, combinations
from collections import Counter
from absolve import solve
ROLES=('Ri','Ro','Si','So')
def rand_gadget(k, rng, ports=2):
    deg=[3]*ports+[4]*(k-ports)
    for _ in range(500):
        stubs=[v for v in range(k) for _ in range(deg[v])]; rng.shuffle(stubs)
        es=[(stubs[i],stubs[i+1]) for i in range(0,len(stubs),2)]
        if all(a!=b for a,b in es) and len({frozenset(e) for e in es})==len(es): return es
    return None
def rand_cherries(k, es, rng, p=1.0):
    adj=[set() for _ in range(k)]; eid={}
    for i,(a,b) in enumerate(es): adj[a].add(b); adj[b].add(a); eid[frozenset((a,b))]=i
    used=set(); ch=[]
    cands=[(x,y,z) for x in range(k) for y,z in combinations(sorted(adj[x]),2) if z not in adj[y]]
    rng.shuffle(cands)
    for x,y,z in cands:
        if y in used or z in used or rng.random()>p: continue
        used|={y,z}; ch.append((x,eid[frozenset((x,y))],eid[frozenset((x,z))]))
    return ch
def interface(k, es, ch):
    edges=list(es)+[(0,None),(1,None)]
    ne=len(es); F=set()
    for r1,r2 in product(ROLES,ROLES):
        if solve(k, edges, ch, fixed={ne:r1, ne+1:r2}, node_limit=10**5): F.add((r1,r2))
    return frozenset(F)
if __name__=="__main__":
    rng=Random(int(sys.argv[1])); T=int(sys.argv[2])
    tal=Counter()
    for t in range(T):
        k=rng.choice(range(5,int(sys.argv[3])+1))
        es=rand_gadget(k,rng)
        if es is None: continue
        ch=rand_cherries(k,es,rng,p=rng.choice([0.5,1.0]))
        try: F=interface(k,es,ch)
        except TimeoutError: tal['TO']+=1; continue
        tal[len(F)]+=1
        if len(F)<4: print(k, es, ch, sorted(F), flush=True)
    print(tal)
