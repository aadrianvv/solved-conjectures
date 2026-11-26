"""Independent check of the order-11 Kempe example found by pcf-kempe (Rust).
A 4-regular K4-free graph with a proper 5-colouring having exactly one defect
from which every sequence of simultaneous Kempe swaps (any proper subset of
the components of one colour pair) needs three moves to reach a PCF colouring,
even when intermediate states may have up to two defects.
Run: python pcf-kempe-distance3.py
"""
from collections import Counter
N=[[1,2,3,4],[0,2,5,6],[0,1,7,8],[0,4,5,7],[0,3,6,8],[1,3,9,10],[1,4,9,10],[2,3,9,10],[2,4,9,10],[5,6,7,8],[5,6,7,8]]
C0=[0,1,2,3,2,0,0,4,0,2,2]
n=len(N)
assert all(len(set(r))==4 and v not in r and all(v in N[u] for u in r) for v,r in enumerate(N))
def defects(c):
    assert all(c[u]!=c[v] for v in range(n) for u in N[v])
    return sum(1 for v in range(n) if 1 not in Counter(c[u] for u in N[v]).values())
def norm(c):
    m={};out=[]
    for x in c:
        if x not in m: m[x]=len(m)
        out.append(m[x])
    return tuple(out)
def moves(c):
    for a in range(5):
        for b in range(a+1,5):
            seen=set();comps=[]
            for v in range(n):
                if v in seen or c[v] not in (a,b): continue
                q=[v];seen.add(v)
                for x in q:
                    for o in N[x]:
                        if o not in seen and c[o] in (a,b): seen.add(o);q.append(o)
                comps.append(q)
            k=len(comps)
            for mask in range(1,1<<k):
                if mask==(1<<k)-1: continue
                d=list(c)
                for i,comp in enumerate(comps):
                    if mask>>i&1:
                        for v in comp: d[v]=a+b-d[v]
                yield tuple(d)
print('defects of start', defects(C0))
for cap in (1,2):
    frontier={norm(C0)}; seen=set(frontier); step=0; found=None
    while frontier and found is None:
        step+=1; nxt=set()
        for s in frontier:
            for d in moves(s):
                k=defects(d)
                if k>cap: continue
                nd=norm(d)
                if nd in seen: continue
                seen.add(nd); nxt.add(nd)
                if k==0: found=step
        frontier=nxt
    print('cap',cap,'fewest simultaneous Kempe moves to a PCF colouring:',found)
