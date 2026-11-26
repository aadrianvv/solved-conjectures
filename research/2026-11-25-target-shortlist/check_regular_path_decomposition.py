"""Bounded exact-cover check for five-edge path decompositions."""

from argparse import ArgumentParser
from collections import Counter
from hashlib import sha256
from itertools import combinations
from random import Random


def regular_graphs(order, degree):
    """An exhaustive orderly generator that may repeat isomorphism classes."""
    adjacency = [0] * order
    remaining = [degree] * order

    def visit(v):
        if v == order:
            yield tuple(adjacency)
            return
        groups = {}
        for w in range(v + 1, order):
            if remaining[w]:
                groups.setdefault(adjacency[w], []).append(w)
        groups = list(groups.values())
        room = sum(map(len, groups))
        if remaining[v] > room or any(d > order - v - 1 for d in remaining[v + 1:]):
            return

        def choices(k, needed, room):
            if not needed:
                yield ()
                return
            group = groups[k]
            for take in range(max(0, needed - room + len(group)), min(needed, len(group)) + 1):
                for rest in choices(k + 1, needed - take, room - len(group)):
                    yield tuple(group[:take]) + rest

        for neighbors in choices(0, remaining[v], room):
            for w in neighbors:
                adjacency[v] ^= 1 << w
                adjacency[w] ^= 1 << v
                remaining[w] -= 1
            yield from visit(v + 1)
            for w in neighbors:
                adjacency[v] ^= 1 << w
                adjacency[w] ^= 1 << v
                remaining[w] += 1
    yield from visit(0)


def list_bits(bits):
    while bits:
        low = bits & -bits
        yield low.bit_length() - 1
        bits ^= low


def label_graph(graph):
    neighborhoods = [list(list_bits(adjacent)) for adjacent in graph]
    labels = []
    for v, neighbors in enumerate(neighborhoods):
        triangles = sum(bool(graph[x] & (1 << y)) for x, y in combinations(neighbors, 2))
        squares = sum((graph[x] & graph[y]).bit_count() - 1
                      for x, y in combinations(neighbors, 2))
        labels.append((triangles, squares))
    return tuple((labels[v], tuple(sorted(labels[w] for w in neighbors)))
                 for v, neighbors in enumerate(neighborhoods))


def isomorphic(g, h, g_labels, h_labels):
    candidates = [sum(1 << w for w, label in enumerate(h_labels) if label == g_label)
                  for g_label in g_labels]
    all_vertices = (1 << len(g)) - 1

    def match(left, right, candidates):
        if not left:
            return True
        v = min(list_bits(left), key=lambda w: (candidates[w] & right).bit_count())
        other = left ^ (1 << v)
        for target in list_bits(candidates[v] & right):
            reduced = [candidates[w] & (h[target] if g[v] & (1 << w) else ~h[target])
                       for w in range(len(g))]
            if match(other, right ^ (1 << target), reduced):
                return True
        return False
    return match(all_vertices, all_vertices, candidates)


def find_matching(graph):
    def match(remaining):
        if not remaining:
            return ()
        v = min(list_bits(remaining), key=lambda w: (graph[w] & remaining).bit_count())
        for w in list_bits(remaining & graph[v]):
            rest = match(remaining ^ (1 << v) ^ (1 << w))
            if rest is not None:
                return ((v, w),) + rest
        return None
    return match((1 << len(graph)) - 1)


def edge_set(graph):
    return {(v, w) for v, neighbors in enumerate(graph) for w in list_bits(neighbors) if v < w}


def exact_cover(graph):
    edges = sorted(edge_set(graph))
    adj = [[] for v in graph]
    for i, (v, w) in enumerate(edges):
        adj[v].append((w, i))
        adj[w].append((v, i))
    paths = []
    rows = [0] * (len(edges) + len(graph))

    def grow(vertices, used_vertices, used_edges):
        if len(vertices) == 6:
            if vertices[0] < vertices[-1]:
                columns = used_edges | (1 << (len(edges) + vertices[0]))
                columns |= 1 << (len(edges) + vertices[-1])
                paths.append((vertices, columns))
                flag = 1 << (len(paths) - 1)
                for i in list_bits(columns):
                    rows[i] |= flag
            return
        for v, i in adj[vertices[-1]]:
            if not used_vertices & (1 << v):
                grow(vertices + (v,), used_vertices | (1 << v), used_edges | (1 << i))

    for v in range(len(graph)):
        grow((v,), 1 << v, 0)

    impossible = set()
    def solve(remaining, available):
        if not remaining:
            return ()
        if remaining in impossible:
            return None
        options = min((rows[i] & available for i in list_bits(remaining)), key=int.bit_count)
        for j in list_bits(options):
            path, columns = paths[j]
            conflicts = 0
            for i in list_bits(columns):
                conflicts |= rows[i]
            rest = solve(remaining ^ columns, available & ~conflicts)
            if rest is not None:
                return (path,) + rest
        impossible.add(remaining)
        return None
    return solve((1 << len(rows)) - 1, (1 << len(paths)) - 1)


def verify(graph, matching, paths):
    assert all(adjacent.bit_count() == 5 for adjacent in graph)
    assert sorted(v for pair in matching for v in pair) == list(range(len(graph)))
    edges = edge_set(graph)
    assert all(tuple(sorted(pair)) in edges for pair in matching)
    assert paths is not None
    covered = Counter()
    for path in paths:
        assert len(path) == len(set(path)) == 6
        covered.update(tuple(sorted(pair)) for pair in zip(path, path[1:]))
    assert covered == Counter(edges)
    assert sorted(v for path in paths for v in (path[0], path[-1])) == list(range(len(graph)))


def shared_triangle_square_edge(graph):
    return any((graph[v] & graph[w]) and
               any(graph[x] & graph[w] & ~(1 << v)
                   for x in list_bits(graph[v] & ~(1 << w)))
               for v, w in edge_set(graph))


def run_bounded(order):
    all_vertices = (1 << order) - 1
    isomorphism_bins = {}
    counts = Counter()
    digest = sha256()
    for complement in regular_graphs(order, order - 6):
        graph = tuple(all_vertices ^ (1 << v) ^ adj for v, adj in enumerate(complement))
        labels = label_graph(graph)
        bucket = isomorphism_bins.setdefault(tuple(sorted(labels)), [])
        counts["generated"] += 1
        if any(isomorphic(graph, prev, labels, prev_labels) for prev, prev_labels in bucket):
            continue
        bucket.append((graph, labels))
        counts["classes"] += 1
        matching = find_matching(graph)
        if matching is None:
            continue
        counts["matched"] += 1
        counts["overlap"] += shared_triangle_square_edge(graph)
        paths = exact_cover(graph)
        verify(graph, matching, paths)
        digest.update(repr((graph, matching, paths)).encode("ascii"))
        counts["verified"] += 1
    print(order, dict(counts), digest.hexdigest(), flush=True)


def sample_graphs(order, count):
    random = Random(20261125 + order)
    halves = order // 2
    matching = tuple((v, v + halves) for v in range(halves))
    matching_set = set(matching)
    cycle_edges = {tuple(sorted((v, (v + difference) % order)))
                   for v in range(order) for difference in (1, 2)}
    observed = set()
    for sample in range(count):
        edges = cycle_edges.copy()
        for unused in range(sample % (2 * order)):
            (a,b),(c,d) = random.sample(sorted(edges), 2)
            if len({a,b,c,d}) != 4:
                continue
            if random.randrange(2):
                c,d = d,c
            replacement = {tuple(sorted((a,c))), tuple(sorted((b,d)))}
            if replacement & edges or replacement & matching_set:
                continue
            edges = (edges - {tuple(sorted((a,b))), tuple(sorted((c,d)))}) | replacement
        graph = [0] * order
        for v,w in edges | matching_set:
            graph[v] |= 1 << w
            graph[w] |= 1 << v
        graph = tuple(graph)
        if graph not in observed:
            observed.add(graph)
            yield graph, matching


def run_sample(order, count):
    counts = Counter()
    digest = sha256()
    for graph, matching in sample_graphs(order, count):
        counts["overlap"] += shared_triangle_square_edge(graph)
        paths = exact_cover(graph)
        verify(graph, matching, paths)
        digest.update(repr((graph, matching, paths)).encode("ascii"))
        counts["verified"] += 1
    print(order, dict(counts), digest.hexdigest(), flush=True)


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--orders", nargs="+", type=int, default=[6, 8, 10])
    parser.add_argument("--sample", type=int)
    options = parser.parse_args()
    for order in options.orders:
        if options.sample:
            run_sample(order, options.sample)
        else:
            run_bounded(order)
