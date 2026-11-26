"""P5** / P5* on dense 5-regular graphs: complements of random (n-6)-regular graphs, n=12,14 (evidence only)."""
import sys
from random import Random
from collections import Counter
from p5solve import solve
from circ import min_matchings
rng=Random(int(sys.argv[1]))
def random_reg(n,d):
    while True:
        pts=[v for v in range(n) for _ in range(d)]; rng.shuffle(pts)
        adj=[set() for _ in range(n)]; ok=True
        for i in range(0,len(pts),2):
            u,v=pts[i],pts[i+1]
            if u==v or v in adj[u]: ok=False;break
            adj[u].add(v);adj[v].add(u)
        if ok: return adj
tal=Counter()
for n,cnt in ((12,int(sys.argv[2])),(14,int(sys.argv[2])//2)):
    for g in range(cnt):
        comp=random_reg(n,n-6)
        adj=[set(range(n))-comp[v]-{v} for v in range(n)]
        t,ms=min_matchings(adj,40)
        ok=0
        for m in ms:
            try: r=solve(adj,m,rng=rng,node_limit=400000)
            except TimeoutError: tal['to']+=1; continue
            ok+= r is not None
            if r is None: tal[(n,'minM UNSAT')]+=1; print("minM UNSAT",n,[sorted(a) for a in adj],m,flush=True)
        tal[(n,'graphs')]+=1; tal[(n,'minM')]+=len(ms); tal[(n,'minM sat')]+=ok
        if ok==0: print("NO FEASIBLE MIN M",n,[sorted(a) for a in adj],flush=True)
print(sorted(tal.items()))
