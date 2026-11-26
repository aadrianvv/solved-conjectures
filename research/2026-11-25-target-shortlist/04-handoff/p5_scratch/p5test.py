import sys, time
from random import Random
from collections import Counter
from itertools import combinations
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
import check_regular_path_sweep_pipeline as P
import os, p5solve
from p5solve import solve, check
p5solve.VARIANT = int(os.environ.get('VARIANT', '0'))


def k6_union(k):
    n = 6 * k
    adj = [set() for _ in range(n)]
    for b in range(0, n, 6):
        for u, v in combinations(range(b, b + 6), 2):
            adj[u].add(v); adj[v].add(u)
    mate = {}
    for b in range(0, n, 6):
        for i in (0, 2, 4):
            mate[b + i], mate[b + i + 1] = b + i + 1, b + i
    return adj, mate


def classify(out):
    c = Counter()
    for tag, p in out:
        k = P.kind(p)
        if k != "path":
            c[(tag, k)] += 1
    return c


def main():
    rng = Random(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
    tally = Counter()
    graphs = []
    graphs.append(("K6", k6_union(1)))
    graphs.append(("K6x3", k6_union(3)))
    for style in ("random", "square", "dense", "k5"):
        for n in (10, 12, 16, 20, 30, 40, 60):
            if style == "k5" and n % 10:
                continue
            for _ in range(6):
                graphs.append((style, P.random_matched_graph(n, rng, style)))
    for name, (adj, mate) in graphs:
        t = time.time()
        try:
            res = solve(adj, mate, rng=rng, node_limit=200000, p6=(len(sys.argv) > 2))
        except TimeoutError:
            tally[(name, "timeout")] += 1
            continue
        if res is None:
            tally[(name, "UNSAT")] += 1
            print("UNSAT", name, len(adj))
            continue
        r, s = res
        check(adj, mate, r, s)
        tally[(name, "sat")] += 1
        trails = {}
        for u in range(len(adj)):
            v = mate[u]
            if u < v:
                trails[(u, v)] = (s[r[u]], r[u], u, v, r[v], s[r[v]])
        out, ndef, nodd = P.sweep(adj, mate, r, s, trails)
        tally[(name, "defects")] += ndef
        tally[(name, "odd cycles")] += nodd
        for k, v in classify(out).items():
            tally[(name,) + k] += v
    for k in sorted(tally):
        print(k, tally[k])


main()


