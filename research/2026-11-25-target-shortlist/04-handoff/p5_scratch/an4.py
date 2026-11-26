import sys, ast
from itertools import combinations
from an1 import matchings
def info(adj,m):
    n=len(adj)
    tot=sum(len(adj[u]&adj[m[u]]) for u in range(n))//2
    d2=[c for c in range(n) if sum(1 for x,y in combinations([w for w in adj[c] if w!=m[c]],2) if m[x]==y)==2]
    return tot,d2
cases=[l for l in open(sys.argv[1]) if l.startswith("COUNTER")]
for l in cases:
    a,b=l[8:].split("] {")
    adj=[set(x) for x in ast.literal_eval(a+"]")]; m=ast.literal_eval("{"+b)
    tot,d2=info(adj,m)
    mn=min(info(adj,mm)[0] for mm in matchings(adj))
    print("count",tot,"min",mn,"D2",d2)
