"""Reverse-BFS greedy with insertion bans and soft rainbow preferences.

Experiment only (evidence, not proof).  Colour the BFS layers from the
deepest one up to the root r.  At each vertex x the hard constraints are the
colours of coloured neighbours and the (at most one) insertion ban of every
neighbour u whose neighbourhood is completed by x.  The soft constraints ask
x to avoid the colours already present around each neighbour u that x does
not complete, so that N(u) minus its last neighbour stays rainbow.  A colour
avoiding hard and soft constraints is preferred; otherwise any colour
avoiding the hard constraints is used.  The run fails if no such colour exists.

Usage: python pcf-bfs-greedy.py SEED TRIALS COLOURS [quartic|subquartic]
"""
import random
import sys
from collections import Counter


def random_quartic(n, rng):
    """Union of two random Hamiltonian cycles, rejecting repeated edges."""
    while True:
        adj = [set() for _ in range(n)]
        ok = True
        for _ in range(2):
            p = list(range(n))
            rng.shuffle(p)
            for i in range(n):
                a, b = p[i], p[(i + 1) % n]
                if b in adj[a]:
                    ok = False
                    break
                adj[a].add(b)
                adj[b].add(a)
            if not ok:
                break
        if ok:
            return [sorted(s) for s in adj]


def random_subquartic(n, m, rng):
    adj = [set() for _ in range(n)]
    tries = 0
    while sum(len(a) for a in adj) // 2 < m and tries < 50 * m:
        tries += 1
        a, b = rng.randrange(n), rng.randrange(n)
        if a != b and b not in adj[a] and len(adj[a]) < 4 and len(adj[b]) < 4:
            adj[a].add(b)
            adj[b].add(a)
    return [sorted(s) for s in adj]


def is_pcf(adj, col):
    for v in range(len(adj)):
        if any(col[u] == col[v] for u in adj[v]):
            return False
        if adj[v] and 1 not in Counter(col[u] for u in adj[v]).values():
            return False
    return True


def greedy(adj, k, rng):
    n = len(adj)
    col = [-1] * n
    seen = [False] * n
    for s in range(n):
        if seen[s]:
            continue
        comp = [s]
        seen[s] = True
        for v in comp:
            for u in adj[v]:
                if not seen[u]:
                    seen[u] = True
                    comp.append(u)
        r = rng.choice(comp)
        dist = {r: 0}
        queue = [r]
        for v in queue:
            for u in adj[v]:
                if u not in dist:
                    dist[u] = dist[v] + 1
                    queue.append(u)
        order = list(comp)
        rng.shuffle(order)
        order.sort(key=lambda v: -dist[v])
        pos = {v: i for i, v in enumerate(order)}
        last = {u: max(adj[u], key=lambda w: pos[w]) for u in comp if adj[u]}
        for x in order:
            hard = {col[u] for u in adj[x] if col[u] >= 0}
            for u in adj[x]:
                if last.get(u) == x:
                    old = Counter(col[w] for w in adj[u] if w != x)
                    for b in range(k):
                        trial = old.copy()
                        trial[b] += 1
                        if 1 not in trial.values():
                            hard.add(b)
            soft = set()
            for u in adj[x]:
                if last.get(u) != x:
                    soft |= {col[w] for w in adj[u] if w != x and col[w] >= 0}
            options = [c for c in range(k) if c not in hard and c not in soft]
            options = options or [c for c in range(k) if c not in hard]
            if not options:
                return None
            col[x] = options[0]
    return col


def main():
    seed, trials, k = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    family = sys.argv[4] if len(sys.argv) > 4 else "quartic"
    rng = random.Random(seed)
    fails = 0
    for _ in range(trials):
        if family == "quartic":
            adj = random_quartic(rng.randrange(6, 150), rng)
        else:
            n = rng.randrange(5, 80)
            adj = random_subquartic(n, rng.randrange(n, 2 * n + 1), rng)
        col = greedy(adj, k, rng)
        if col is None or not is_pcf(adj, col):
            fails += 1
    print({"seed": seed, "trials": trials, "colours": k, "family": family, "failures": fails})


if __name__ == "__main__":
    main()
