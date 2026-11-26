import ast,sys
from circ import min_matchings
from loc4 import improving
from p5solve import solve
def cnt(adj,m): return sum(len(adj[u]&adj[m[u]]) for u in range(len(adj)))//2
cases=[
("[[1, 2, 11, 12, 13], [0, 2, 3, 12, 13], [0, 1, 3, 4, 9], [1, 2, 4, 5, 6], [2, 3, 5, 6, 7], [3, 4, 6, 7, 8], [3, 4, 5, 7, 8], [4, 5, 6, 8, 9], [5, 6, 7, 9, 10], [2, 7, 8, 10, 11], [8, 9, 11, 12, 13], [0, 9, 10, 12, 13], [0, 1, 10, 11, 13], [0, 1, 10, 11, 12]]","{12: 13, 13: 12, 8: 10, 10: 8, 6: 7, 7: 6, 4: 5, 5: 4, 2: 9, 9: 2, 1: 3, 3: 1, 0: 11, 11: 0}"),
("[[1, 2, 3, 12, 13], [0, 2, 3, 4, 13], [0, 1, 3, 4, 13], [0, 1, 2, 4, 5], [1, 2, 3, 5, 6], [3, 4, 6, 7, 12], [4, 5, 7, 8, 9], [5, 6, 8, 9, 10], [6, 7, 9, 10, 11], [6, 7, 8, 10, 11], [7, 8, 9, 11, 12], [8, 9, 10, 12, 13], [0, 5, 10, 11, 13], [0, 1, 2, 11, 12]]","{11: 13, 13: 11, 8: 9, 9: 8, 7: 10, 10: 7, 5: 12, 12: 5, 4: 6, 6: 4, 2: 3, 3: 2, 0: 1, 1: 0}")]
for a,b in cases:
    adj=[set(x) for x in ast.literal_eval(a)]; m=ast.literal_eval(b)
    t,ms=min_matchings(adj,200)
    print("count",cnt(adj,m),"min",t,"#min(capped)",len(ms),"feasible mins",sum(solve(adj,mm,node_limit=10**6) is not None for mm in ms))
