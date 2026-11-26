"""Bridgeless P5* counterexample blocks: B with attachment set A (degree 4 in B) such that
 (i) for every proper subset S of A with |S| = |B| mod 2, B - S has NO perfect matching (so any perfect matching of a
     host graph in which A's external edges form the cut delta(B) uses all |A| cut edges), and
 (ii) every perfect matching of B - A gives an infeasible (P5) instance on B.
Two copies glued along A then form a graph with no bridge in which P5* fails."""
import sys
from itertools import combinations
from collections import Counter
from blocks import degseq_graphs, matchings
from check_regular_path_decomposition import label_graph, isomorphic, list_bits
from p5solve import solve
def has_pm(adj, verts):
    for _ in matchings(adj, verts): return True
    return False
def run(nB,k):
    degs=[4]*k+[5]*(nB-k); classes=[]; tal=Counter()
    for g in degseq_graphs(degs):
        if any(bin(g[v]).count('1')!=degs[v] for v in range(nB)): continue
        adj=[set(list_bits(a)) for a in g]
        A=[v for v in range(nB) if len(adj[v])==4]
        forced=True
        for j in range(k):
            if (j-nB)%2: continue
            for S in combinations(A,j):
                if has_pm(adj,[v for v in range(nB) if v not in S]): forced=False;break
            if not forced: break
        if not forced: continue
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(kk==key and isomorphic(g,h,lab,hl) for kk,h,hl in classes): continue
        classes.append((key,g,lab)); tal['forced blocks']+=1
        nm=feas=0
        for mm in matchings(adj,[v for v in range(nB) if v not in A]):
            nm+=1; mate=dict(mm)
            for a in A: mate[a]=a
            if solve(adj,mate,node_limit=10**6) is not None: feas+=1; break
        if nm and not feas:
            tal['COUNTEREXAMPLE BLOCK']+=1; print("BRIDGELESS BLOCK",nB,k,[sorted(a) for a in adj],flush=True)
    print(nB,k,dict(tal),flush=True)
for spec in sys.argv[1:]:
    run(*map(int,spec.split(',')))
