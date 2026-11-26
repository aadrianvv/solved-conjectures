"""P5** on 5-regular circulants C_n(a,b,n/2): all min-incidence matchings (capped)."""
import sys
from p5solve import solve
from random import Random
from collections import Counter
rng=Random(5)
def cnt(adj,m): return sum(len(adj[u]&adj[m[u]]) for u in range(len(adj)))//2
def min_matchings(adj,cap):
    # branch and bound enumeration of min-weight perfect matchings
    n=len(adj); w={}
    for u in range(n):
        for v in adj[u]: w[(u,v)]=len(adj[u]&adj[v])
    best=[10**9]; sols=[]
    def go(free,m,cost):
        if cost>best[0]: return
        if not free:
            if cost<best[0]: best[0]=cost; sols.clear()
            if len(sols)<cap: sols.append(dict(m))
            return
        u=min(free)
        for v in sorted(adj[u],key=lambda v:w[(u,v)]):
            if v in free:
                m[u]=v;m[v]=u
                go(free-{u,v},m,cost+w[(u,v)])
                del m[u],m[v]
    go(frozenset(range(n)),{},0)
    return best[0],sols
def _main():
  tal=Counter()
  for n in range(12,25,2):
      for a in range(1,n//2):
          for b in range(a+1,n//2):
              adj=[{(i+a)%n,(i-a)%n,(i+b)%n,(i-b)%n,(i+n//2)%n} for i in range(n)]
              if any(len(x)!=5 for x in adj): continue
              t,ms=min_matchings(adj,int(sys.argv[1]))
              ok=0
              for m in ms:
                  try: r=solve(adj,m,rng=rng,node_limit=500000)
                  except TimeoutError: tal['timeout']+=1; continue
                  ok+= r is not None
                  if r is None: print("P5** FAIL",n,a,b,m,flush=True)
              tal['graphs']+=1; tal['minM']+=len(ms); tal['minM sat']+=ok
              if t>0: tal['mincount>0']+=1
  print(tal)

if __name__=="__main__":
  _main()
