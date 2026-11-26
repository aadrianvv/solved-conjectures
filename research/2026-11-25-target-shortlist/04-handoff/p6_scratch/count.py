import sys
from random import Random
from collections import Counter
from plant import planted
from absolve import solve
from itertools import combinations
def abstract(adj, m):
    n=len(adj); H=[sorted(w for w in adj[v] if w!=m[v]) for v in range(n)]
    es=sorted({(min(u,v),max(u,v)) for u in range(n) for v in H[u]}); eid={e:i for i,e in enumerate(es)}
    E=lambda a,b: eid[(min(a,b),max(a,b))]
    ch=[(x,E(x,y),E(x,z)) for x in range(n) for y,z in combinations(H[x],2) if m[y]==z]
    return n, es, ch
rng=Random(int(sys.argv[1])); tal=Counter()
for t in range(int(sys.argv[2])):
    N=rng.choice([10,12])
    res=planted(N,rng,p=0.7,tries=20000)
    if not res: continue
    n,es,ch=abstract(*res)
    full=len(solve(n,es,ch,want_all=True,node_limit=10**8))
    free=len(solve(n,es,[],want_all=True,node_limit=10**8))
    tal[(len(ch),full%2,free%2)]+=1
    print(N,len(ch),full,free,flush=True)
print(tal)
