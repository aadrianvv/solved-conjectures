# Compute FGK (2010) bad pairs of M-cycles for the 408-vertex example and for K_{5,5}.
from itertools import combinations
from collections import Counter
def build408():
    N=68; idx=lambda t,j:"uvabcd".index(t)*N+(j%N)
    adj={v:set() for v in range(6*N)}; mate={}
    def add(x,y): adj[x].add(y); adj[y].add(x)
    for j in range(N):
        for p,q in ("ua","vb","vc","ab","ac","bc"): add(idx(p,j),idx(q,j))
        add(idx("u",j),idx("v",j)); mate[idx("u",j)]=idx("v",j); mate[idx("v",j)]=idx("u",j)
        for (p,q),sh in ((("u","a"),6),(("u","b"),8),(("u","d"),9),(("v","c"),10),(("v","d"),11),(("d","d"),7)):
            add(idx(p,j),idx(q,j+sh))
        for t in "abcd":
            x,y=idx(t,j),idx(t,j+34); add(x,y); mate[x]=y; mate[y]=x
    return adj,mate
def k55():
    adj={v:set() for v in range(10)}; mate={}
    for i in range(5):
        for j in range(5): adj[i].add(5+j); adj[5+j].add(i)
        mate[i]=5+i; mate[5+i]=i
    return adj,mate
E=lambda x,y: frozenset((x,y))
def mcycles(adj,mate):
    isM=lambda x,y: mate[x]==y
    cyc=set()
    for u in adj:
        v=mate[u]
        if u>v: continue
        for a in adj[u]&adj[v]:   # M-triangle u v a
            cyc.add(('T',frozenset([E(u,v),E(v,a),E(a,u)])))
        for a in adj[u]-{v}:      # M-square u v b a : u-v (M), v-b, b-a, a-u ; exactly one M edge
            for b in adj[v]-{u,a}:
                if a in adj[b] and a!=b:
                    es=[E(u,v),E(v,b),E(b,a),E(a,u)]
                    if sum(isM(*tuple(e)) for e in es)==1:
                        cyc.add(('S',frozenset(es)))
    return list(cyc)
def fgk_bad(adj,mate):
    cy=mcycles(adj,mate); Mset={E(u,mate[u]) for u in adj}
    byedge={}
    for i,(_,es) in enumerate(cy):
        for e in es: byedge.setdefault(e,[]).append(i)
    pairs=set()
    for lst in byedge.values():
        for i,j in combinations(lst,2): pairs.add((min(i,j),max(i,j)))
    bad=[]
    for i,j in pairs:
        U=(cy[i][1]|cy[j][1])-Mset; deg=Counter(x for e in U for x in e)
        if max(deg.values())>=3: bad.append((i,j))
    kinds=Counter(cy[i][0]+cy[j][0] for i,j in bad)
    # Theorem 7: graph H on M-cycles in bad pairs is a star?
    H={}
    for i,j in bad: H.setdefault(i,set()).add(j); H.setdefault(j,set()).add(i)
    star = len(H)==0 or any(len(H[c])==len(H)-1 and all(H[x]=={c} for x in H if x!=c) for c in H)
    ours=sum(1 for i,j in pairs if {cy[i][0],cy[j][0]}=={'T','S'})
    return Counter(t for t,_ in cy), len(bad), dict(kinds), star, ours
for name,(adj,mate) in (("408-vertex example",build408()),("K_{5,5}",k55())):
    c,nb,kinds,star,ours=fgk_bad(adj,mate)
    print(f"{name}: M-cycles {dict(c)}; FGK bad pairs {nb} {kinds}; FGK Thm7 star? {star}; our triangle-square conflicts {ours}")
