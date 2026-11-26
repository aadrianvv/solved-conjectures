"""Experiment (evidence only): PCF 6-colourings obtained by splitting two
classes of a proper 4-colouring.  For random quartic graphs, sample random
proper 4-colourings and test every pair of classes (i, j): each vertex of
class i or j either keeps its colour or moves to a new colour (4 or 5).  By
the splitting lemma no singleton is lost; the search decides whether all
defects can be repaired.  Output: Counter of (some colouring tried,
some colouring splittable) and the summed fraction of splittable colourings.
Usage: python pcf-two-class-split.py SEED GRAPHS
"""
import random
def random_quartic(n, rng):
    # union of two random Hamiltonian cycles, reject multi-edges
    while True:
        adj = [set() for _ in range(n)]
        ok = True
        for _ in range(2):
            p = list(range(n)); rng.shuffle(p)
            for i in range(n):
                a, b = p[i], p[(i+1) % n]
                if b in adj[a]:
                    ok = False; break
                adj[a].add(b); adj[b].add(a)
            if not ok: break
        if ok:
            return [sorted(s) for s in adj]

import sys
from collections import Counter
sys.setrecursionlimit(10000)
def rand_col(adj, k, rng):
    n=len(adj); col=[-1]*n; order=list(range(n)); rng.shuffle(order)
    nodes=[0]
    def rec(i):
        nodes[0]+=1
        if nodes[0]>200000: raise TimeoutError
        if i==n: return True
        v=order[i]; cs=list(range(k)); rng.shuffle(cs)
        for c in cs:
            if all(col[u]!=c for u in adj[v]):
                col[v]=c
                if rec(i+1): return True
        col[v]=-1; return False
    return col if rec(0) else None
def splittable(adj, col, pair):
    n=len(adj); var=[v for v in range(n) if col[v] in pair]
    pos={v:i for i,v in enumerate(var)}
    x={}
    # check vertex w when all its variable nbrs assigned
    lastvar={}
    for w in range(n):
        vs=[u for u in adj[w] if u in pos]
        lastvar[w]=max(vs,key=lambda u:pos[u]) if vs else None
    checks={}
    for w in range(n): checks.setdefault(lastvar[w],[]).append(w)
    def good(w):
        cnt=Counter((col[u],x.get(u,0)) for u in adj[w])
        return 1 in cnt.values()
    if not all(good(w) for w in checks.get(None,[])): return False
    def rec(i):
        if i==len(var): return True
        v=var[i]
        for b in (0,1):
            x[v]=b
            if all(good(w) for w in checks.get(v,[])) and rec(i+1): return True
        del x[v]; return False
    return rec(0)
rng=random.Random(int(sys.argv[1])); T=int(sys.argv[2])
stats=Counter()
for t in range(T):
    n=rng.randrange(8,40); adj=random_quartic(n,rng)
    good_cols=0; tried=0
    for s in range(10):
        try: col=rand_col(adj,4,rng)
        except TimeoutError: continue
        if col is None: continue
        tried+=1
        if any(splittable(adj,col,(i,j)) for i in range(4) for j in range(i+1,4)): good_cols+=1
    stats[(tried>0, good_cols>0)]+=1
    stats['frac_sum']+=good_cols/max(tried,1)
print(stats)
