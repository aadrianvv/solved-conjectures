from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import combinations
from random import Random

from check_fgk_small import edge_set, list_bits, sample_graphs


def path_edges(path):
    return tuple(tuple(sorted(pair)) for pair in zip(path, path[1:]))


def canonical_trails(graph, matching, rng):
    mate = {u: v for pair in matching for u, v in (pair, pair[::-1])}
    residual = {edge for edge in edge_set(graph) if edge[1] != mate[edge[0]]}
    partners = []
    for v, adjacent in enumerate(graph):
        neighbors = list(list_bits(adjacent & ~(1 << mate[v])))
        rng.shuffle(neighbors)
        pairs = [(x, mate[x]) for x in neighbors if x < mate[x] and mate[x] in neighbors]
        used = {x for pair in pairs for x in pair}
        filler = [x for x in neighbors if x not in used]
        pairs.extend(zip(filler[::2], filler[1::2]))
        partners.append({x: y for pair in pairs for x, y in (pair, pair[::-1])})
    outgoing = defaultdict(list)
    incoming = defaultdict(list)
    while residual:
        u, v = min(residual)
        if rng.randrange(2):
            u, v = v, u
        while tuple(sorted((u, v))) in residual:
            edge = tuple(sorted((u, v)))
            residual.remove(edge)
            arc = (u, v)
            outgoing[u].append(arc)
            incoming[v].append(arc)
            u, v = v, partners[v][u]

    colors = {}
    arcs = sorted(arc for values in outgoing.values() for arc in values)
    for arc in arcs:
        if arc in colors:
            continue
        colors[arc] = rng.randrange(2)
        component = [arc]
        while component:
            edge = component.pop()
            u, v = edge
            other = [a for a in outgoing[u] + incoming[v] if a != edge]
            for neighbor in other:
                c = 1 - colors[edge]
                if neighbor in colors:
                    assert colors[neighbor] == c
                else:
                    colors[neighbor] = c
                    component.append(neighbor)
    first = {u: v for (u, v), c in colors.items() if c == 0}
    second = {v: u for (u, v), c in colors.items() if c == 1}
    return glue(graph, matching, first, second)


def glue(graph, matching, first, second):
    result = []
    for u, v in matching:
        a, b = first[u], first[v]
        path = (second[a], a, u, v, b, second[b])
        if len(set(path)) == 5:
            if path[-1] != path[1]:
                path = path[::-1]
            assert path[-1] == path[1]
        else:
            assert len(set(path)) == 6
        result.append(path)
    assert Counter(e for path in result for e in path_edges(path)) == Counter(edge_set(graph))
    assert sorted(v for path in result for v in (path[0], path[-1])) == list(range(len(graph)))
    return tuple(result)


def solve_cluster(trails, available, directed=()):
    selected = tuple(trails[i] for i in available)
    edges = sorted(e for p in selected for e in path_edges(p))
    adj = defaultdict(list)
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    terminals = sorted(v for v, neighbors in adj.items() if len(neighbors) % 2)
    assert len(terminals) == 2 * len(selected)
    terminal_bits = {v: 1 << (len(edges) + i) for i, v in enumerate(terminals)}
    columns = [0] * (len(edges) + len(terminals))
    paths = []

    def build(p, emask):
        if len(p) == 6:
            if (p[0] < p[-1] and p[-1] in terminal_bits and
                    (p[0], p[1]) not in directed and (p[-1], p[-2]) not in directed):
                mask = emask | terminal_bits[p[0]] | terminal_bits[p[-1]]
                flag = 1 << len(paths)
                paths.append((p, mask))
                for ix in list_bits(mask):
                    columns[ix] |= flag
            return
        for u, i in adj[p[-1]]:
            if u not in p:
                build(p + (u,), emask | (1 << i))

    for u in terminals:
        build((u,), 0)
    dead = set()
    def recurse(uncovered, free):
        if not uncovered:
            return ()
        if uncovered in dead:
            return None
        options = min((columns[j] & free for j in list_bits(uncovered)), key=int.bit_count)
        for j in list_bits(options):
            p, mask = paths[j]
            conflicting = 0
            for ix in list_bits(mask):
                conflicting |= columns[ix]
            tail = recurse(uncovered ^ mask, free & ~conflicting)
            if tail is not None:
                return (p,) + tail
        dead.add(uncovered)
        return None
    result = recurse((1 << len(columns)) - 1, (1 << len(paths)) - 1)
    if result is not None:
        assert all(len(set(p)) == len(p) == 6 for p in result)
        assert Counter(e for p in result for e in path_edges(p)) == Counter(edges)
        assert sorted(v for p in result for v in (p[0], p[-1])) == terminals
    return result


def classify(trails, counts, only_single=False, report=False):
    defects = [i for i, p in enumerate(trails) if len(set(p)) == 5]
    if only_single and len(defects) != 1:
        return
    for i in defects:
        trail = trails[i]
        near = {j for j, p in enumerate(trails) if i != j and set(trail) & set(p)}
        latest = set(near)
        second_ring = {j for j, p in enumerate(trails) if j != i and
                       any(set(trails[k]) & set(p) for k in near)}
        for size in (2, 3, 4):
            rings = near if size == 2 else second_ring
            successful = None
            for others in combinations(sorted(rings), size - 1):
                if not near.intersection(others):
                    continue
                successful = solve_cluster(trails, (i,) + others)
                if successful is not None:
                    break
            if successful is not None:
                counts[size] += 1
                break
        else:
            counts["beyond_four"] += 1
            if report:
                print("DEFECT", i, "total bad", len(defects), "trail system", trails, flush=True)
            if only_single and report:
                raise RuntimeError("Four-trail repair fails for a single defect")


def obstructing_gluing():
    n = 90
    idx = lambda v, c: v + 9 * (c % 10)
    first_arcs = ((2, 1), (3, 4), (5, 2), (6, 7))
    second_arcs = ((1, 0), (4, 1), (2, 4), (7, 8))
    graph = [0] * n
    factors = []
    for base, shift in ((first_arcs, 1), (second_arcs, 3)):
        arcs = {idx(v, c): idx(w, c) for c in range(10) for v, w in base}
        tails = sorted(set(range(9)) - {v for v, _ in base})
        heads = sorted(set(range(9)) - {w for _, w in base})
        arcs.update({idx(v, c): idx(w, c + shift) for c in range(10) for v, w in zip(tails, heads)})
        factors.append(arcs)
        for v, w in arcs.items():
            graph[v] |= 1 << w
            graph[w] |= 1 << v
    matching = tuple((idx(v, c), idx(w, c)) for c in range(10) for v, w in ((2, 3), (5, 6)))
    matching += tuple((idx(v, c), idx(v, c + 5)) for c in range(5) for v in (0, 1, 4, 7, 8))
    for v, w in matching:
        graph[v] |= 1 << w
        graph[w] |= 1 << v
    return glue(tuple(graph), matching, *factors)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--orders", type=int, nargs="+", default=[12, 14, 16, 20])
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--seeds", type=int, default=3)
    parser.add_argument("--single", action="store_true")
    args = parser.parse_args()
    counts = Counter()
    classify(obstructing_gluing(), counts)
    print("constructed obstruction seed", counts, flush=True)
    for order in args.orders:
        counts = Counter()
        for j, (graph, matching) in enumerate(sample_graphs(order, args.samples)):
            for seed in range(args.seeds):
                rng = Random(1009 * j + seed)
                trials = canonical_trails(graph, matching, rng)
                classify(trials, counts, args.single, report=True)
        print("sampled", order, counts, flush=True)
