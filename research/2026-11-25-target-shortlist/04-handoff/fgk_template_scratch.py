from argparse import ArgumentParser
from collections import Counter

from fgk_pair_scratch import identifications, undirected, valid_canonical
from fgk_local_repair_scratch import solve_cluster


def compatible(trails):
    edges = tuple(edge for trail in trails for edge in undirected(trail))
    if len(edges) != len(set(edges)) or any(u == v for u, v in edges):
        return False
    centers = tuple(v for trail in trails for v in trail[2:4])
    if len(centers) != len(set(centers)):
        return False
    for pos in (2, 1):
        arcs = tuple((path[pos], path[pos-1]) for path in trails)
        arcs += tuple((path[5-pos], path[6-pos]) for path in trails)
        for i in (0, 1):
            if len({a[i] for a in arcs}) != len(arcs):
                return False
    return True


def main():
    t = (0, 1, 2, 3, 4, 1)
    counts = Counter()
    for x, f, g, h, y in identifications("xfghy", 5):
        q = (x, 2, f, g, h, y)
        if len(set(q)) != 6 or not valid_canonical(t, q):
            continue
        initial = solve_cluster((t, q), (0, 1))
        if initial is not None:
            continue
        counts["pair blocked"] += 1
        vertices = max(t + q) + 1
        assert vertices == len(set(t + q))
        for s, v, j, k, l in identifications("svjkl", vertices):
            r = (s, v, 4, j, k, l)
            if len(set(r)) != 6 or not compatible((t, q, r)):
                continue
            after = solve_cluster((t, q, r), (0, 2))
            if after is not None:
                counts["other pair worked"] += 1
                continue
            after = solve_cluster((t, q, r), (0, 1, 2))
            if after is not None:
                counts["triple worked"] += 1
                continue
            counts["triple blocked"] += 1
            print("blocked", t, q, r, flush=True)
        print("processed pair", q, counts, flush=True)
    print(counts, flush=True)


if __name__ == "__main__":
    main()
