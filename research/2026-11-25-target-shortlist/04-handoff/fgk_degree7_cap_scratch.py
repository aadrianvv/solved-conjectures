from collections import defaultdict
from random import Random
import sys

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def core(n, rng):
    edges = {tuple(sorted((u, (u + j) % n))) for u in range(n) for j in (1, 2, 3)}
    listing = sorted(edges)
    for _ in range(60 * n):
        i, j = rng.sample(range(len(listing)), 2)
        u, v = listing[i]
        x, y = listing[j]
        if rng.randrange(2):
            x, y = y, x
        a, b = tuple(sorted((u, x))), tuple(sorted((v, y)))
        if len({u, v, x, y}) == 4 and a not in edges and b not in edges:
            edges.difference_update((listing[i], listing[j]))
            edges.update((a, b))
            listing[i], listing[j] = a, b
    return listing


def generate(n, edges, u, v, compound):
    adj = defaultdict(list)
    num_edges = len(edges)
    markers = {x: num_edges + i for i, x in enumerate([u, v, *[w for w in range(n) if w not in (u, v)]])}
    for i, (x, y) in enumerate(edges):
        adj[x].append((y, i))
        adj[y].append((x, i))
    base, arms = set(), defaultdict(set)

    def search(path, used, stop):
        start, end = path[0], path[-1]
        length = len(used)
        if length == 7 and start < end:
            base.add(tuple(sorted(used)))
        if start in (u, v) and length <= 6:
            arms[start, length].add(tuple(sorted((*used, markers[start]))))
            if compound and end not in (u, v) and length <= 2:
                arms[start, length + 4].add(tuple(sorted((*used, markers[start], markers[end]))))
        if start not in (u, v) and length == 3:
            base.add(tuple(sorted((*used, markers[start]))))
        if length < stop:
            for x, edge in adj[end]:
                if x not in path:
                    search((*path, x), (*used, edge), stop)

    for x in range(n):
        search((x,), (), 7 if compound else 6 if x in (u, v) else 3)
    return base, arms


def check(num_columns, rows):
    rows = tuple(rows)
    pos = [x for row in rows for x in row]
    which = [i for i, row in enumerate(rows) for x in row]
    matrix = coo_matrix((np.ones(len(pos)), (pos, which)), shape=(num_columns, len(rows))).tocsc()
    result = milp(np.zeros(len(rows)), integrality=np.ones(len(rows)), bounds=Bounds(0, 1),
                  constraints=LinearConstraint(matrix, 1, 1), options={"time_limit": 4})
    if result.x is None:
        return result.status
    assert sorted(x for i, row in enumerate(rows) if result.x[i] > 0.5 for x in row) == list(range(num_columns))
    return True


def main():
    rng = Random(76311)
    quota = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    for n in map(int, sys.argv[2:] or range(7, 13)):
        incomplete = 0
        for trial in range(quota):
            e = core(n, rng)
            u, v = rng.choice(e)
            base, arms = generate(n, e, u, v, False)
            full = None
            for r in (0, 1, 2, 4, 5, 6):
                result = check(n + len(e), base | arms[u, r] | arms[v, 6-r])
                if result is not True and n >= 8:
                    if full is None:
                        full = generate(n, e, u, v, True)
                    full_base, full_arms = full
                    result = check(n + len(e), full_base | full_arms[u, r] | full_arms[v, 6-r])
                if result is not True:
                    print("unresolved", n, trial, u, v, r, result, e, flush=True)
                    incomplete += 1
            print("checked", n, trial + 1, incomplete, flush=True)


if __name__ == "__main__":
    main()
