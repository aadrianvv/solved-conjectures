"""Abstract instances: random 4-regular H, maximal cherry system with pairwise disjoint target pairs
(targets non-adjacent).  Variant flag 'shared' allows target sharing (control)."""
import sys
from random import Random
from collections import Counter
from itertools import combinations
from absolve import solve
from gadget import rand_gadget
def cherry_system(k, es, rng, disjoint=True, nonadj=True):
    adj=[set() for _ in range(k)]; eid={}
    for i,(a,b) in enumerate(es): adj[a].add(b); adj[b].add(a); eid[frozenset((a,b))]=i
    used=Counter(); ch=[]; pairs=set()
    cands=[(x,y,z) for x in range(k) for y,z in combinations(sorted(adj[x]),2) if (z not in adj[y] or not nonadj)]
    rng.shuffle(cands)
    busy=Counter()
    for x,y,z in cands:
        if busy[(x,y)] or busy[(x,z)]: continue
        if disjoint and (used[y] or used[z]): continue
        if not disjoint and (used[y] and frozenset((y,z)) not in pairs or used[z] and frozenset((y,z)) not in pairs): continue
        used[y]+=1; used[z]+=1; pairs.add(frozenset((y,z))); busy[(x,y)]=busy[(x,z)]=1
        ch.append((x,eid[frozenset((x,y))],eid[frozenset((x,z))]))
    return ch
if __name__=="__main__":
    rng=Random(int(sys.argv[1])); T=int(sys.argv[2]); Ns=[int(a) for a in sys.argv[3].split(',')]
    disjoint = sys.argv[4]=='disjoint'
    tal=Counter()
    for t in range(T):
        k=rng.choice(Ns); es=rand_gadget(k,rng,ports=0)
        if es is None: continue
        ch=cherry_system(k,es,rng,disjoint=disjoint)
        try: ok=bool(solve(k,es,ch,node_limit=3*10**5))
        except TimeoutError: tal['TO']+=1; continue
        tal[(k,ok)]+=1
        if not ok and tal[(k,False)]<=3: print("INFEASIBLE",k,es,ch,flush=True)
    print(sorted(tal.items(),key=str))
