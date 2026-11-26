"""Experiment: the abstract cycle step of the Kashima-Skrekovski-Xu reduction
with six colours.  Each cycle vertex v_i has a list L_i of two colours and a
blocked unordered pair P_i of two colours outside L_i (its two outside
neighbour colours).  A solution picks c_i in L_i, proper along the cycle, with
{c_(i-1), c_(i+1)} != P_i for all i.  Random instances with k = 5, 6, 7.
Output keys: (k odd, all lists identical, solvable).
Usage: python pcf-cycle-two-lists.py SEED TRIALS
"""
import random, itertools, sys
from collections import Counter
def solvable(L, P):
    k=len(L)
    for c in itertools.product(*L):
        if any(c[i]==c[(i+1)%k] for i in range(k)): continue
        if any({c[i-1],c[(i+1)%k]}==P[i] for i in range(k)): continue
        return True
    return False
rng=random.Random(int(sys.argv[1])); stats=Counter(); examples=[]
for t in range(int(sys.argv[2])):
    k=rng.choice([5,6,7])
    # bias towards few distinct colours to hit hard cases
    pal=list(range(6))
    L=[]; P=[]
    for i in range(k):
        Li=set(rng.sample(pal if rng.random()<0.5 else pal[:3],2)) if True else None
        rest=[x for x in pal if x not in Li]
        P.append(set(rng.sample(rest,2))); L.append(sorted(Li))
    s=solvable(L,P)
    ident=all(l==L[0] for l in L)
    stats[(k%2, ident, s)]+=1
    if not s and not ident and len(examples)<5: examples.append((L,[sorted(p) for p in P]))
print(stats); print(examples)
