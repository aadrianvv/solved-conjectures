"""Which features accompany transcross failure (abstract class instances)?"""
import sys
from random import Random
from collections import Counter
from gadget import rand_gadget
from abstract_rand import cherry_system
from absolve import solve
import absolve
ALLOWED_TC={frozenset(('Ri','So')),frozenset(('Ro','Si'))}
def solve_tc(k,es,ch,node_limit=3*10**5):
    old=absolve.BAD
    absolve.BAD={frozenset(p) for p in [('Ri','Si'),('Ri','Ro'),('Ro','So'),('Si','So'),('Ri','So','x')]}
    # transcross: forbid everything except {Ri,So},{Ro,Si}
    absolve.BAD={frozenset(('Ri','Si')),frozenset(('Ri','Ro')),frozenset(('Ro','So')),frozenset(('Si','So'))}
    try: return bool(solve(k,es,ch,node_limit=node_limit))
    finally: absolve.BAD=old
def feats(k,es,ch):
    apex=Counter(x for x,_,_ in ch)
    d2=sum(1 for v in apex.values() if v==2)
    karcs=set()
    for x,e1,e2 in ch:
        for e in (e1,e2):
            a,b=es[e]; y=b if a==x else a; karcs.add((x,y))
    mutual=sum(1 for (x,y) in karcs if (y,x) in karcs)//2
    return d2, mutual
rng=Random(int(sys.argv[1])); tal=Counter()
for t in range(int(sys.argv[2])):
    k=rng.choice([8,10,12,14]); es=rand_gadget(k,rng,ports=0)
    if es is None: continue
    ch=cherry_system(k,es,rng)
    d2,mu=feats(k,es,ch)
    try: ok=solve_tc(k,es,ch)
    except TimeoutError: tal['TO']+=1; continue
    tal[('d2>0',d2>0,'mut>0',mu>0,ok)]+=1
print(sorted(tal.items(),key=str))
