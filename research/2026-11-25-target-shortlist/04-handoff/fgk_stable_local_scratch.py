from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from random import Random

from check_fgk_small import sample_graphs
from fgk_local_repair_scratch import canonical_trails, path_edges, solve_cluster


def all_defective(pieces, rng):
    while True:
        middle = list(range(2 * pieces))
        rng.shuffle(middle)
        corner = list(range(0, 2 * pieces, 2))
        rng.shuffle(corner)
        trails = tuple((2 * i, 2 * i + 1, middle[2 * i], middle[2 * i + 1], corner[i], 2 * i + 1)
                       for i in range(pieces))
        if any(len(set(p)) != 5 for p in trails):
            continue
        if len({e for p in trails for e in path_edges(p)}) != 5 * pieces:
            continue
        return trails


def candidate_clusters(trails, limit):
    sets = [set(p) for p in trails]
    bad_indices = {i for i, p in enumerate(trails) if len(set(p)) == 5}
    neighbors = {i: {j for j, t in enumerate(sets) if i != j and s & t}
                 for i, s in enumerate(sets)}
    memo = set()
    for size in range(2, limit + 1):
        for bad in sorted(bad_indices):
            zone = set(neighbors[bad])
            for _ in range(size - 2):
                zone = zone | {i for j in zone for i in neighbors[j]}
            zone.discard(bad)
            for others in combinations(sorted(zone), size - 1):
                cluster = tuple(sorted((bad,) + others))
                if cluster in memo:
                    continue
                memo.add(cluster)
                connected = {bad}
                while next_set := {i for j in connected for i in neighbors[j]
                                   if i in cluster and i not in connected}:
                    connected.update(next_set)
                if len(connected) == size:
                    yield cluster
        memo.clear()


def repair(initial, limit, constrain):
    blue = {(p[i], p[j]) for p in initial for i, j in ((1, 0), (4, 5))} if constrain else ()
    trails = list(initial)
    updates = Counter()
    while any(len(set(p)) == 5 for p in trails):
        for cluster in candidate_clusters(trails, limit):
            updated = solve_cluster(trails, cluster, blue)
            if updated is None:
                continue
            for i, p in zip(cluster, updated):
                trails[i] = p
            updates[len(cluster)] += 1
            break
        else:
            return None, updates, trails
    return True, updates, trails


def main():
    parser = ArgumentParser()
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--pieces", type=int, nargs="+", default=[10])
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--colored", action="store_true")
    parser.add_argument("--all-defective", action="store_true")
    args = parser.parse_args()
    rng = Random(2033)
    counts = Counter()
    for pieces in args.pieces:
        if args.all_defective:
            systems = (all_defective(pieces, rng) for _ in range(args.samples))
        else:
            systems = (canonical_trails(graph, matching, rng)
                       for graph, matching in sample_graphs(2 * pieces, args.samples))
        for index, initial in enumerate(systems, 1):
            outcome, sizes, terminal = repair(initial, args.limit, args.colored)
            counts.update(sizes)
            if outcome is None:
                counts["failed"] += 1
                print("blocked", "pieces", pieces, "order", 2 * pieces, "trial", index, "counts", counts,
                      "\ninitial:", initial, "\nremaining:", terminal, flush=True)
                return
            if index % 100 == 0:
                print("processed", pieces, index, counts, flush=True)
        print("finished", pieces, counts, flush=True)


if __name__ == "__main__":
    main()
