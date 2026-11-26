import sys
from random import Random
from collections import Counter
from gadget import rand_gadget
from abstract_rand import cherry_system
from absolve import solve
import absolve
ALL={'A':('Ri','So'),'B':('Ro','Si'),'C':('Ro','So'),'D':('Si','So')}
def solve_opts(k,es,ch,opts,node_limit=3*10**5):
    old=absolve.BAD
    allowed={frozenset(ALL[o]) for o in opts}
    from itertools import combinations
    absolve.BAD={frozenset(p) for p in combinations(('Ri','Ro','Si','So'),2)}-allowed
    try: return bool(solve(k,es,ch,node_limit=node_limit))
    finally: absolve.BAD=old
rng=Random(int(sys.argv[1])); tal=Counter(); strats=sys.argv[3].split(',')
for t in range(int(sys.argv[2])):
    k=rng.choice([8,10,12,14]); es=rand_gadget(k,rng,ports=0)
    if es is None: continue
    ch=cherry_system(k,es,rng)
    for s in strats:
        try: ok=solve_opts(k,es,ch,s)
        except TimeoutError: tal[(s,'TO')]+=1; continue
        tal[(s,ok)]+=1
print(sorted(tal.items(),key=str))
