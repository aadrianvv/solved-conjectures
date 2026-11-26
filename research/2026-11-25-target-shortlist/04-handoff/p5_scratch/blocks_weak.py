"""Weak (P5): cherry constraints dropped at apexes that are bridge ends (vertices of A).
Search bridge-forced blocks in which every perfect matching of B - A is still infeasible."""
import sys
from collections import Counter
from blocks import degseq_graphs, matchings
from check_regular_path_decomposition import label_graph, isomorphic, list_bits
from core import solve_pairs, allpairs
def run(nB,k):
    degs=[4]*k+[5]*(nB-k); classes=[]; tal=Counter()
    for g in degseq_graphs(degs):
        if any(bin(g[v]).count('1')!=degs[v] for v in range(nB)): continue
        lab=label_graph(g); key=tuple(sorted(lab))
        if any(kk==key and isomorphic(g,h,lab,hl) for kk,h,hl in classes): continue
        classes.append((key,g,lab))
        adj=[set(list_bits(a)) for a in g]; A=[v for v in range(nB) if len(adj[v])==4]
        nm=feas=0
        for mm in matchings(adj,[v for v in range(nB) if v not in A]):
            nm+=1; mate=dict(mm)
            for a in A: mate[a]=a
            P=[p for p in allpairs(adj,mate) if p[0] not in A]
            if solve_pairs(adj,mate,set(P)): feas+=1; break
        tal['blocks']+=1
        if nm and not feas: tal['WEAK-P5 COUNTEREXAMPLE BLOCK']+=1; print("WEAK BLOCK",nB,k,[sorted(a) for a in adj],flush=True)
    print(nB,k,dict(tal),flush=True)
for spec in sys.argv[1:]: run(*map(int,spec.split(',')))
