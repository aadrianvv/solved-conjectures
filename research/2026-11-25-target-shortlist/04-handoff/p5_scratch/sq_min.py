"""P5** on square-of-cycle-based dense graphs (random_matched_graph 'square'/'dense'), n=14..22: all minimum
matchings (capped) tested exactly.  Evidence only."""
import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_sweep_pipeline import random_matched_graph
from random import Random
from collections import Counter
from p5solve import solve
from circ import min_matchings
rng=Random(int(sys.argv[1])); cap=int(sys.argv[3])
tal=Counter()
for N in (14,16,18,20,22):
    for g in range(int(sys.argv[2])):
        adj,_=random_matched_graph(N,rng,rng.choice(["square","dense"]))
        t,ms=min_matchings(adj,cap)
        ok=0
        for m in ms:
            try: r=solve(adj,m,rng=rng,node_limit=400000)
            except TimeoutError: tal['to']+=1; continue
            ok+=r is not None
            if r is None: print("P5** FAIL",N,t,[sorted(a) for a in adj],m,flush=True)
        tal[(N,'graphs')]+=1; tal[(N,'minM')]+=len(ms); tal[(N,'sat')]+=ok; tal[(N,'mincount>0')]+=t>0
print(sorted(tal.items()),flush=True)
