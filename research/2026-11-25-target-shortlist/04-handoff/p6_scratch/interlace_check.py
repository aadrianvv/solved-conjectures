"""Check: for an Euler circuit W of a 4-regular graph (oriented along W), an arc colouring that changes colour at
pass k iff t[v(k)]=1 is a directed 2-factorization iff (A_I + I) t = 1 over GF(2) (I = interlace graph of W).
Exhaustive over all t for random small instances."""
import sys
from random import Random
from itertools import product
from gadget import rand_gadget
def euler_circuit(k, es, rng):
    inc=[[] for _ in range(k)]
    for i,(a,b) in enumerate(es): inc[a].append(i); inc[b].append(i)
    used=[False]*len(es); stack=[(0,None)]; circ=[]
    # Hierholzer on vertices with edge ids
    ptr=[0]*k
    for l in inc: rng.shuffle(l)
    st=[(0,-1)]; out=[]
    while st:
        v,e=st[-1]
        while ptr[v]<4 and used[inc[v][ptr[v]]]: ptr[v]+=1
        if ptr[v]==4: out.append(st.pop())
        else:
            f=inc[v][ptr[v]]; used[f]=True; a,b=es[f]; st.append((b if a==v else a, f))
    out.reverse()  # sequence of (vertex, edge used to arrive)
    verts=[v for v,_ in out][:-1]; arcs=[e for _,e in out][1:]
    return verts, arcs  # arc j goes verts[j] -> verts[j+1]
rng=Random(int(sys.argv[1])); bad=0; tested=0
for t in range(int(sys.argv[2])):
    k=rng.choice([5,6,7,8]); es=rand_gadget(k,rng,ports=0)
    if es is None: continue
    verts,arcs=euler_circuit(k,es,rng); L=len(arcs)
    if L!=2*k: continue
    pos={}
    for j,v in enumerate(verts): pos.setdefault(v,[]).append(j)
    inter=lambda u,v: (pos[u][0]<pos[v][0]<pos[u][1]) != (pos[u][0]<pos[v][1]<pos[u][1])
    for tv in product((0,1),repeat=k):
        lin=all((tv[x]+sum(tv[v] for v in range(k) if v!=x and inter(x,v)))%2==1 for x in range(k))
        # colour: arc j has colour c_j; pass at verts[j] (between arc j-1 and arc j)
        c=[0]*L
        for j in range(1,L): c[j]=(c[j-1]+tv[verts[j]])%2
        closes=(c[L-1]+tv[verts[0]])%2==c[0]
        valid=False
        if closes:
            inn={v:[] for v in range(k)}; out={v:[] for v in range(k)}
            for j in range(L): out[verts[j]].append(c[j]); inn[verts[(j+1)%L]].append(c[j])
            valid=all(sorted(inn[v])==[0,1] and sorted(out[v])==[0,1] for v in range(k))
        tested+=1
        if valid!=lin: bad+=1
print("tested",tested,"mismatches",bad)
