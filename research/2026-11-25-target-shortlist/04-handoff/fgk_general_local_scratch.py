from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from random import Random

from fgk_adversarial_scratch import check
from fgk_cut_scratch import find_matching
from fgk_local_repair_scratch import path_edges, solve_cluster


def mixed_cover(order, fixed, random, extra_bad=0):
    degree = Counter(v for p in fixed for e in path_edges(p) for v in e)
    placed_endpoints = {v for p in fixed for v in (p[0], p[-1])}
    ends = sorted(set(range(order)) - placed_endpoints)
    pieces = len(ends) // 2
    while True:
        random.shuffle(ends)
        part = ends[:2 * extra_bad]
        end_degrees = {v: 1 for v in ends}
        for v in part[1::2]:
            end_degrees[v] = 3
        if any(degree[v] + d > 5 for v, d in end_degrees.items()):
            continue
        used_middle = [v for v in range(order) for _ in range((5 - degree[v] - end_degrees.get(v, 0)) // 2)]
        assert len(used_middle) == 4 * pieces - extra_bad
        random.shuffle(used_middle)
        generated = []
        pos = 0
        for i in range(pieces):
            a, b = ends[2 * i: 2 * i + 2]
            if i < extra_bad:
                c, d, e = used_middle[pos:pos + 3]
                path = a, b, c, d, e, b
                pos += 3
                if len(set(path)) != 5:
                    break
            else:
                v = tuple(used_middle[pos:pos + 4])
                path = (a,) + v + (b,)
                pos += 4
                if len(set(path)) != 6:
                    break
            generated.append(path)
        if len(generated) != pieces:
            continue
        trails = fixed + tuple(generated)
        edges = tuple(e for p in trails for e in path_edges(p))
        if len(set(edges)) != len(edges):
            continue
        graph = [0] * order
        for v, w in edges:
            graph[v] |= 1 << w
            graph[w] |= 1 << v
        assert all(a.bit_count() == 5 for a in graph)
        if find_matching(graph) is not None:
            return trails


def target_repairs(trails, max_size=3):
    near = {i for i, p in enumerate(trails[1:], 1) if set(trails[0]) & set(p)}
    shell = {i for i, p in enumerate(trails[1:], 1) if any(set(trails[j]) & set(p) for j in near)} | near
    found = []
    for size in range(2, max_size + 1):
        for neighbors in combinations(sorted(shell if size >= 3 else near), size - 1):
            if not near.intersection(neighbors):
                continue
            cluster = (0,) + neighbors
            if solve_cluster(trails, cluster) is not None:
                found.append(cluster)
    return found


def main():
    parser = ArgumentParser()
    parser.add_argument("--orders", type=int, nargs="+", default=[20, 30, 40])
    parser.add_argument("--samples", type=int, default=200)
    parser.add_argument("--fixed", choices=["one", "triple", "pair"], default="one")
    parser.add_argument("--bad", type=int, default=0)
    args = parser.parse_args()
    t = 0, 1, 2, 3, 4, 1
    q = 4, 2, 5, 6, 7, 8
    p = 2, 0, 4, 7, 9, 10
    fixed = {"one": (t,), "triple": (t, q, p), "pair": (t, q)}[args.fixed]
    rng = Random(20261201)
    for order in args.orders:
        counts = Counter()
        for run in range(args.samples):
            system = mixed_cover(order, fixed, rng, args.bad)
            result = check(system)
            counts[result] += 1
            if result is None:
                print("FAILED up to three", order, system, flush=True)
                print("repairs up to four", target_repairs(system, 4), flush=True)
                return
            if (run + 1) % 100 == 0:
                print("processed", order, run + 1, counts, flush=True)
        print("finished", order, counts, flush=True)


if __name__ == "__main__":
    main()
