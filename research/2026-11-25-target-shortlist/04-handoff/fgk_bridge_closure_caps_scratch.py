from argparse import ArgumentParser
from collections import Counter
from itertools import combinations
from random import Random

from fgk_cut_scratch import build_solver, find_matching


def starting_core(copies):
    bridge_roots = []
    edges = set()
    matching = set()
    for i in range(copies):
        offset = 11 * i
        hub = offset
        for j in (1, 6):
            block = tuple(range(offset + j, offset + j + 5))
            edges.update(combinations(block, 2))
            edges.update((hub, port) for port in block[:2])
            matching.add(block[:2])
            bridge_roots.extend(block[2:])
        bridge_roots.append(hub)
    return edges, matching, tuple(sorted(bridge_roots))


def all_closures(edges, roots):
    if len(roots) < 2:
        yield (), roots
        return
    a, *rest = roots
    for new, roots in all_closures(edges, tuple(rest)):
        yield new, (a,) + roots
    for j, b in enumerate(rest):
        if (a, b) not in edges:
            for new, roots in all_closures(edges, tuple(rest[:j] + rest[j+1:])):
                yield ((a, b),) + new, roots


def sample_closures(edges, roots, rng, count):
    for _ in range(count):
        available = list(roots)
        rng.shuffle(available)
        pairs = []
        for budget in range(rng.randint(2, 7)):
            for a, b in combinations(available, 2):
                choice = tuple(sorted((a,b)))
                if choice not in edges:
                    pairs.append(choice)
                    available.remove(a)
                    available.remove(b)
                    break
        yield tuple(pairs), tuple(sorted(available))


def scan(order, old, matching, added, roots, cuts):
    graph_edges = old | set(added)
    all_possibilities = tuple(sorted(graph_edges - matching - set(added)))
    for cut in (all_possibilities if cuts is None else cuts(all_possibilities)):
        edges = graph_edges - {cut}
        adj = [0]*order
        for u,v in edges:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
        port_set = roots + cut
        assert all(adjacency.bit_count() + port_set.count(v) == 5 for v, adjacency in enumerate(adj))
        assert sorted(v for e in matching | set(added) for v in e) == sorted(set(range(order)) - set(roots))
        solve = build_solver(tuple(adj), port_set, len(roots))
        for i in (0, 1, 3, 4):
            if solve((2,) * len(roots) + (i, 4-i)) is None:
                print("MISSING", order, "ports", cut, "arm", i, "bridge roots", roots,
                      "pair closure", added, "native edges", sorted(edges), flush=True)
                raise RuntimeError("Counterexample candidate")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--copies", type=int, choices=(1,2), default=1)
    parser.add_argument("--samples", type=int, default=100)
    args = parser.parse_args()
    rng = Random(10025)
    old, matching, roots = starting_core(args.copies)
    cases = (all_closures(old, roots) if args.copies == 1
             else sample_closures(old, roots, rng, args.samples))
    ends = lambda options: rng.sample(options, 8)
    count = 0
    for added, retained in cases:
        scan(11*args.copies, old, matching, added, retained, None if args.copies == 1 else ends)
        count += 1
        if count % 10 == 0:
            print("checked closure cases",args.copies,count,flush=True)
    print("finished closure cases",args.copies,count,flush=True)
