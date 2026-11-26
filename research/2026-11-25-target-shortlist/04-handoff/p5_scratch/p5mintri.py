import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
exec(open("p5census.py", encoding="utf-8-sig").read().split("for order in")[0])
from itertools import combinations
from collections import Counter
def ntri(adj, m):
    return sum(1 for c in range(len(adj)) for x, y in combinations([w for w in adj[c] if w != m[c]], 2) if m[x] == y)
stats = Counter()
for order in (8, 10):
    classes = []
    for g in regular_graphs(order, 5):
        lab = label_graph(g); key = tuple(sorted(lab))
        if any(k == key and isomorphic(g, h, lab, hl) for k, h, hl in classes):
            continue
        classes.append((key, g, lab))
    for _, g, _ in classes:
        adj = [set(list_bits(a)) for a in g]
        ms = list(matchings(adj))
        byt = Counter(); okt = Counter()
        for m in ms:
            t = ntri(adj, m); byt[t] += 1
            if solve(adj, m, rng=rng, node_limit=10**6) is not None:
                okt[t] += 1
        tmin = min(byt)
        stats[(order, "min-tri M all P5")] += okt[tmin] == byt[tmin]
        stats[(order, "min-tri M some P5")] += okt[tmin] > 0
        stats[(order, "graphs")] += 1
        unsat_ts = sorted(t for t in byt if okt[t] < byt[t])
        if unsat_ts and unsat_ts[0] == tmin:
            print(order, "UNSAT at min tri", tmin, dict(byt), dict(okt))
print(dict(stats))

