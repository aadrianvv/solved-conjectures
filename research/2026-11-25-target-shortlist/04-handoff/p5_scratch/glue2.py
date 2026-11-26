"""Bridgeless attempt: two copies of the counterexample block glued along A by 3 edges (18 vertices)."""
from itertools import permutations
from collections import Counter
from p5solve import solve
from blocks import matchings
Bk={0:[3,4,5,6],1:[3,4,7,8],2:[3,4,7,8],3:[0,1,2,5,6],4:[0,1,2,5,6],5:[0,3,4,7,8],6:[0,3,4,7,8],7:[1,2,5,6,8],8:[1,2,5,6,7]}
for perm in [(0,1,2),(1,0,2),(1,2,0)]:
    adj=[set() for _ in range(18)]
    for v,ns in Bk.items():
        for w in ns: adj[v].add(w); adj[v+9].add(w+9)
    for a,b in zip((0,1,2),perm): adj[a].add(b+9); adj[b+9].add(a)
    assert all(len(x)==5 for x in adj)
    tal=Counter()
    for m in matchings(adj,range(18)):
        ok=solve(adj,m,node_limit=10**6) is not None
        cross=sum(1 for a in (0,1,2) if m[a]>=9)
        tal[(cross,ok)]+=1
    print(perm,dict(tal))
