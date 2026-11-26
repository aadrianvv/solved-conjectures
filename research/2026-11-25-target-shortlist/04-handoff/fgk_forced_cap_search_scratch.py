from argparse import ArgumentParser
from collections import Counter
from functools import cache
from itertools import combinations, product
from random import Random

from check_fgk_small import edge_set, list_bits
from fgk_cut_scratch import build_solver, distinct_cap_graphs, find_matching


def local_blocks():
    result = []
    for roots in ((0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 2)):
        for graph in distinct_cap_graphs(7, roots, True):
            if find_matching(graph, roots[:1]) is not None:
                result.append((tuple(sorted(edge_set(graph))), roots))
    return tuple(result)


def quotient(size, rng, star):
    pairs = list(combinations(range(size), 2))
    if star:
        local = [(0, v) for v in rng.sample(range(1, size), size - 2)]
    else:
        local = rng.sample(pairs, size - 2)
    degree = Counter(v for e in local for v in e)
    if max(degree.values(), default=0) > 4:
        return None
    stubs = [v for v in range(size) for _ in range(4 - degree[v])]
    for _ in range(500):
        rng.shuffle(stubs)
        rows = tuple(tuple(sorted(pair)) for pair in zip(stubs[::2], stubs[1::2]))
        if any(a == b or (i >= 2 and i - 2 in (a,b)) for i, (a,b) in enumerate(rows)):
            continue
        return local, rows
    return None


def build(size, local, rows, blocks):
    vertices = size + 7 * (size + 2)
    edges = set(local)
    ports = []
    matching = []
    for i, (pair, (native, points)) in enumerate(zip(rows, blocks)):
        offset = size + 7 * i
        edges.update((u + offset, v + offset) for u, v in native)
        edges.update((v, w + offset) for v, w in zip(pair, points[1:]))
        if i < 2:
            ports.append(points[0] + offset)
        else:
            edges.add((i - 2, points[0] + offset))
            matching.append((i - 2, points[0] + offset))
        small = [0] * 7
        for u,v in native:
            small[u] |= 1 << v
            small[v] |= 1 << u
        matching.extend((u + offset, v + offset) for u,v in find_matching(tuple(small), points[:1]))
    a = [0] * vertices
    for u,v in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    assert all(bits.bit_count() + (v in ports) == 5 for v, bits in enumerate(a))
    assert sorted(v for e in matching for v in e) == sorted(set(range(vertices)) - set(ports))
    assert all(a[u] & (1 << v) for u,v in matching)
    return tuple(a), tuple(ports)


@cache
def signatures(edges, ports):
    graph = [0] * 7
    for u, v in edges:
        graph[u] |= 1 << v
        graph[v] |= 1 << u
    solve = build_solver(tuple(graph), ports)
    return tuple(state for state in product(range(5), repeat=3)
                 if sum(state) == 6 and solve(state) is not None)


def all_rooted_network(size, local, pairs, blocks, lengths):
    """Sufficient cover using three rooted arms at each 3-edge cut."""
    states = tuple(tuple(s for s in signatures(*block) if s[0] == lengths[i] or i >= 2)
                   if i < 2 else signatures(*block) for i, block in enumerate(blocks))
    if not all(states):
        return False
    edges = tuple(sorted(local))
    adjacent = [[] for _ in range(size)]
    for i, (u, v) in enumerate(edges):
        adjacent[u].append((v, i))
        adjacent[v].append((u, i))
    options = [[(0, len(edges) + v, None)] for v in range(size)]
    next_column = len(edges) + size
    allowed = {}
    rows_by_weight = {}
    for i, pair in enumerate(pairs):
        attached = (i - 2,) + pair if i >= 2 else (None,) + pair
        for j, v in enumerate(attached):
            if v is None:
                continue
            for length in range(5):
                mask = sum(1 << k for k, state in enumerate(states[i]) if state[j] == length)
                if mask:
                    key = i, j, length
                    allowed[key] = mask
                    options[v].append((length + 1, next_column, key))
                    rows_by_weight[key] = 0
            next_column += 1
    columns = [0] * next_column
    rows = []

    def enumerate_paths(path, used):
        length = len(path) - 1
        if length == 0 or path[0] < path[-1]:
            for (a, p, x), (b, q, y) in product(options[path[0]], options[path[-1]]):
                if a + b + length != 5 or p == q or (length == 0 and p > q):
                    continue
                if x is not None and y is not None and x[0] == y[0]:
                    continue
                cover = used | (1 << p) | (1 << q)
                flag = 1 << len(rows)
                keys = tuple(z for z in (x, y) if z is not None)
                rows.append((cover, keys))
                for col in list_bits(cover):
                    columns[col] |= flag
                for key in keys:
                    rows_by_weight[key] |= flag
        if length < 5:
            for neighbor, i in adjacent[path[-1]]:
                if neighbor not in path:
                    enumerate_paths(path + (neighbor,), used | (1 << i))

    for v in range(size):
        enumerate_paths((v,), 0)
    keys_at_block = [[] for _ in blocks]
    for key in allowed:
        keys_at_block[key[0]].append(key)
    visited = set()

    def solve(remaining, free, active):
        if not remaining:
            return True
        state = remaining, free, active
        if state in visited:
            return False
        options = min((columns[i] & free for i in list_bits(remaining)), key=int.bit_count)
        for i in list_bits(options):
            covered, keys = rows[i]
            update = list(active)
            conflicts = 0
            for j in list_bits(covered):
                conflicts |= columns[j]
            for key in keys:
                block = key[0]
                update[block] &= allowed[key]
                if not update[block]:
                    break
                for other in keys_at_block[block]:
                    if not allowed[other] & update[block]:
                        conflicts |= rows_by_weight[other]
            else:
                if solve(remaining ^ covered, free & ~conflicts, tuple(update)):
                    return True
        visited.add(state)
        return False

    return solve((1 << len(columns)) - 1, (1 << len(rows)) - 1,
                 tuple((1 << len(word)) - 1 for word in states))


def search(size, attempts, rng, use_star, all_lengths, use_macro):
    options = local_blocks()
    seen = set()
    count = 0
    while count < attempts:
        skeleton = quotient(size, rng, use_star)
        if skeleton is None:
            continue
        local, rows = skeleton
        blocks = tuple(rng.choice(options) for _ in rows)
        a, ports = build(size, local, rows, blocks)
        if (a, ports) in seen:
            continue
        seen.add((a, ports))
        count += 1
        print("check",size,count,ports,flush=True)
        solve = None
        for i in ((2, 0, 1, 3, 4) if all_lengths else (2,)):
            if use_macro and all_rooted_network(size, local, rows, blocks, (i,4-i)):
                continue
            if solve is None:
                print("whole-graph fallback",i,flush=True)
                solve = build_solver(a, ports)
            if solve((i,4-i)) is None:
                print("RESTRICTED", i, size, count, sorted(edge_set(a)), ports, flush=True)
                if i == 2:
                    return
        print("passed",size,count,flush=True)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--hubs", type=int, default=4)
    parser.add_argument("--cases", type=int, default=40)
    parser.add_argument("--star", action="store_true")
    parser.add_argument("--all-lengths", action="store_true")
    parser.add_argument("--macro", action="store_true")
    args = parser.parse_args()
    search(args.hubs, args.cases, Random(20261125 + args.hubs), args.star, args.all_lengths, args.macro)
