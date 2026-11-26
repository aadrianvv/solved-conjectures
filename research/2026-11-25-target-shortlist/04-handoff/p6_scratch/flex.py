"""Flexibility tests on abstract class instances (K-in-degree <= 1):
(1) for edges e,f: is there a solution with colour(e) != colour(f)?  (2) same colour?"""
import sys
from random import Random
from collections import Counter
from gadget import rand_gadget
from abstract_rand import cherry_system
from absolve import solve
import absolve
def solve_pair(k, es, ch, e, f, same):
    # add constraint via post-filter: brute force using want_all would be slow; instead add as extra check in domain? do enumeration limited
    sols = solve(k, es, ch, want_all=True, node_limit=5*10**5)
    def col(asg, e):
        u = es[e][0]; return asg[u][e][0]
    return any((col(s, e) == col(s, f)) == same for s in sols), len(sols)
rng=Random(int(sys.argv[1])); tal=Counter()
for t in range(int(sys.argv[2])):
    k=rng.choice([8,9,10]); es=rand_gadget(k,rng,ports=0)
    if es is None: continue
    ch=cherry_system(k,es,rng)
    try: sols=solve(k,es,ch,want_all=True,node_limit=10**6)
    except TimeoutError: tal['TO']+=1; continue
    col=lambda s,e: s[es[e][0]][e][0]
    ne=len(es)
    for e in range(ne):
        for f in range(e+1,ne):
            diff=any(col(s,e)!=col(s,f) for s in sols); same=any(col(s,e)==col(s,f) for s in sols)
            tal[('diff',diff)]+=1; tal[('same',same)]+=1
            if not diff and tal[('diff',False)]<=3: print('NODIFF',k,es,ch,e,f,len(sols))
print(sorted(tal.items(),key=str))
