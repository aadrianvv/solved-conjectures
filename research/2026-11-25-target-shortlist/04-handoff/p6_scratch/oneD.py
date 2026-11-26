"""When transcross (AB) fails, is ABD at a single apex (AB elsewhere) enough?  Count min #D-apexes needed (<=3)."""
import sys
from random import Random
from collections import Counter
from itertools import combinations
from gadget import rand_gadget
from abstract_rand import cherry_system
import absolve
from absolve import permutations
ALL={'A':('Ri','So'),'B':('Ro','Si'),'C':('Ro','So'),'D':('Si','So')}
def solve_per(k,es,ch,optsof,node_limit=3*10**5):
    # per-cherry allowed option sets
    edges=es; inc=[[] for _ in range(k)]
    for i,(u,v) in enumerate(edges): inc[u].append(i); inc[v].append(i)
    doms=[]
    for x in range(k):
        d=[]
        for p in permutations(('Ri','Ro','Si','So')):
            a=dict(zip(inc[x],p)); good=True
            for j,(y,e1,e2) in enumerate(ch):
                if y!=x: continue
                if frozenset((a[e1],a[e2])) not in {frozenset(ALL[o]) for o in optsof(j)}: good=False;break
            if good: d.append(a)
        doms.append(d)
    COMP=absolve.COMP
    other=lambda e,x: edges[e][1] if edges[e][0]==x else edges[e][0]
    asg=[None]*k; cur=[list(d) for d in doms]
    def rec():
        best=None
        for v in range(k):
            if asg[v] is None and (best is None or len(cur[v])<len(cur[best])): best=v
        if best is None: return True
        v=best
        for a in cur[v]:
            asg[v]=a; saved=[]; ok=True
            for e in inc[v]:
                w=other(e,v)
                if asg[w] is not None: continue
                saved.append((w,cur[w])); cur[w]=[b for b in cur[w] if b[e]==COMP[a[e]]]
                if not cur[w]: ok=False;break
            if ok and rec(): return True
            for w,d in reversed(saved): cur[w]=d
            asg[v]=None
        return False
    return rec()
rng=Random(int(sys.argv[1])); tal=Counter()
for t in range(int(sys.argv[2])):
    k=rng.choice([8,10,12]); es=rand_gadget(k,rng,ports=0)
    if es is None: continue
    ch=cherry_system(k,es,rng)
    apexcnt=Counter(x for x,_,_ in ch)
    single=[j for j,(x,_,_) in enumerate(ch) if apexcnt[x]==1]
    if solve_per(k,es,ch,lambda j:'AB'): tal['AB ok']+=1; continue
    found=None
    for r in (1,2,3):
        for S in combinations(single,r):
            if solve_per(k,es,ch,lambda j:'ABD' if j in S else 'AB'): found=r;break
        if found: break
    tal[('minD',found)]+=1
print(sorted(tal.items(),key=str))
