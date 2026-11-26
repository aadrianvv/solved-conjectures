import sys, pickle
from random import Random
from itertools import product
from collections import Counter
from absolve import solve
from gadget import rand_gadget, rand_cherries
ROLES=('Ri','Ro','Si','So')
BAL=[t for t in product(ROLES,repeat=4) if t.count('Ri')==t.count('Ro') and t.count('Si')==t.count('So')]
def interface4(k, es, ch):
    edges=list(es)+[(i,None) for i in range(4)]
    ne=len(es); F=set()
    for t in BAL:
        if solve(k, edges, ch, fixed={ne+i:t[i] for i in range(4)}, node_limit=2*10**4): F.add(t)
    return frozenset(F)
if __name__=="__main__":
    rng=Random(int(sys.argv[1])); T=int(sys.argv[2]); K=int(sys.argv[3])
    tal=Counter(); out=[]
    for t in range(T):
        k=rng.choice(range(6,K+1))
        es=rand_gadget(k,rng,ports=4)
        if es is None: continue
        ch=rand_cherries(k,es,rng,p=1.0)
        try: F=interface4(k,es,ch)
        except TimeoutError: tal['TO']+=1; continue
        tal[len(F)]+=1
        out.append((k,es,ch,F))
    print(sorted(tal.items(),key=str))
    pickle.dump(out,open(sys.argv[4],'wb'))
