import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import regular_graphs, label_graph, isomorphic, list_bits
from p5solve import solve
from random import Random
rng = Random(1)
def matchings(adj):
    n = len(adj)
    def go(free):
        if not free:
            yield {}
            return
        u = min(free)
        for v in adj[u]:
            if v in free:
                for m in go(free - {u, v}):
                    m = dict(m); m[u] = v; m[v] = u
                    yield m
    yield from go(frozenset(range(n)))
for order in (8, 10):
    classes = []
    for g in regular_graphs(order, 5):
        lab = label_graph(g)
        key = tuple(sorted(lab))
        if any(k == key and isomorphic(g, h, lab, hl) for k, h, hl in classes):
            continue
        classes.append((key, g, lab))
    print(order, "classes", len(classes), flush=True)
    worst = []
    for _, g, _ in classes:
        adj = [set(list_bits(a)) for a in g]
        tot = ok = 0
        for m in matchings(adj):
            tot += 1
            if solve(adj, m, rng=rng, node_limit=10**6) is not None:
                ok += 1
        worst.append((ok, tot))
        if ok == 0:
            print("NO M WITH P5:", [sorted(a) for a in adj], flush=True)
    print(order, "min feasible fraction", min(o / t for o, t in worst), "graphs with none:", sum(o == 0 for o, t in worst), flush=True)
