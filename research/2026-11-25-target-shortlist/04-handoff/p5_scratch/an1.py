import sys
from random import Random
from itertools import combinations
from collections import Counter
from p5solve import solve
def random_5reg(n, rng):
    while True:
        pts = [v for v in range(n) for _ in range(5)]
        rng.shuffle(pts)
        adj = [set() for _ in range(n)]
        ok = True
        for i in range(0, len(pts), 2):
            u, v = pts[i], pts[i + 1]
            if u == v or v in adj[u]:
                ok = False; break
            adj[u].add(v); adj[v].add(u)
        if ok: return adj
def matchings(adj):
    n=len(adj)
    def go(free):
        if not free: yield {}; return
        u=min(free)
        for v in adj[u]:
            if v in free:
                for m in go(free-{u,v}):
                    m=dict(m); m[u]=v; m[v]=u; yield m
    yield from go(frozenset(range(n)))
def pairs_at(adj,m,c):
    nb=[w for w in adj[c] if w!=m[c]]
    return [(x,y) for x,y in combinations(nb,2) if m[x]==y]
def blocks(adj,m):
    n=len(adj); fib={}
    for v in range(n): fib[v]=min(v,m[v])
    cnt=Counter()
    for v in range(n):
        for w in adj[v]:
            if w!=m[v] and v<w: cnt[(min(fib[v],fib[w]),max(fib[v],fib[w]))]+=1
    return cnt
if __name__=="__main__":
  rng=Random(int(sys.argv[1])); N=int(sys.argv[2]); G=int(sys.argv[3])
  found=0
  for g in range(G):
      adj=random_5reg(N,rng)
      for k,m in enumerate(matchings(adj)):
          if k>60: break
          mp=max(len(pairs_at(adj,m,c)) for c in range(N))
          if mp>1: continue
          if solve(adj,m,rng=rng,node_limit=10**6) is None:
              print("UNSAT", [sorted(a) for a in adj], {u:m[u] for u in range(N) if u<m[u]}, "blocks", sorted(blocks(adj,m).items()), flush=True)
              found+=1
              if found>=3: sys.exit()
