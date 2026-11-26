import sys, ast
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/04-handoff/p5_scratch")
from core import mincore, allpairs
from collections import Counter
for l in open(sys.argv[1]):
    if not l.startswith("COUNTER"): continue
    a, b = l[8:].split("] {")
    adj = [set(x) for x in ast.literal_eval(a + "]")]; m = ast.literal_eval("{" + b)
    P = allpairs(adj, m)
    fib = Counter(frozenset((y, z)) for x, y, z in P)
    c = mincore(adj, m)
    print("pairs", len(P), "fibres with 2 apexes", [tuple(f) for f, k in fib.items() if k >= 2])
    print("  core", c, "core-fibre apex counts", [fib[frozenset((y, z))] for x, y, z in c])
