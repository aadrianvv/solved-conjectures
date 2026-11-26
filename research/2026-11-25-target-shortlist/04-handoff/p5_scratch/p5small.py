"""Stress test: (P1)-(P3)+(P5) feasibility on many small random 5-regular graphs, all perfect matchings tried."""
import sys, os
from random import Random
from collections import Counter
from itertools import combinations
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
import p5solve
from p5solve import solve, check
p5solve.VARIANT = int(os.environ.get('VARIANT', '0'))


def random_5reg(n, rng):
    # configuration model with rejection
    while True:
        pts = [v for v in range(n) for _ in range(5)]
        rng.shuffle(pts)
        adj = [set() for _ in range(n)]
        ok = True
        for i in range(0, len(pts), 2):
            u, v = pts[i], pts[i + 1]
            if u == v or v in adj[u]:
                ok = False; break
            adj[u].add(v); adj[v].add(u)
        if ok:
            return adj


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


def main():
    rng = Random(int(sys.argv[1]))
    N = int(sys.argv[2]); count = int(sys.argv[3])
    maxm = int(sys.argv[4]) if len(sys.argv) > 4 else 50
    tally = Counter()
    for g in range(count):
        adj = random_5reg(N, rng)
        ms = []
        for m in matchings(adj):
            ms.append(m)
            if len(ms) >= maxm:
                break
        for m in ms:
            try:
                res = solve(adj, m, rng=rng, node_limit=500000)
            except TimeoutError:
                tally["timeout"] += 1; continue
            if res is None:
                tally["UNSAT"] += 1
                print("UNSAT", [sorted(a) for a in adj], m)
            else:
                check(adj, m, *res)
                tally["sat"] += 1
    print(dict(tally))


main()
