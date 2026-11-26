from argparse import ArgumentParser
from collections import Counter
from itertools import combinations, product
from random import Random

from check_fgk_small import edge_set, list_bits
from fgk_cut_scratch import find_matching


FAKE_WEIGHTS = (1, 2, 4, 5)


def weight_cover(order, native, fake, bridge_roots, prescribed=()):
    adj = [[] for _ in range(order)]
    for idx, (u, v) in enumerate(native):
        adj[u].append((v, idx))
        adj[v].append((u, idx))
    end_base = len(native)
    stub_base = end_base + order
    boundary_base = len(native) + order + 2 * len(fake) + len(bridge_roots)
    true_columns = boundary_base + len(prescribed)
    edges_and_roles = [0] * true_columns
    weights_used = [{} for _ in fake]
    options = [[] for _ in range(order)]
    for i in range(order):
        options[i].append((0, end_base + i, None))
    for i, (u, v) in enumerate(fake):
        for weight in FAKE_WEIGHTS:
            options[u].append((weight, stub_base + 2 * i, (i, weight)))
            options[v].append((weight, stub_base + 2 * i + 1, (i, 6 - weight)))
    for i, v in enumerate(bridge_roots):
        options[v].append((3, stub_base + 2 * len(fake) + i, None))
    for i, (v, length) in enumerate(prescribed):
        options[v].append((length, boundary_base + i, None))
    paths = []

    def add(path, used_edges, length):
        for l, r in product(options[path[0]], options[path[-1]]):
            left_weight, left_col, left_assign = l
            right_weight, right_col, right_assign = r
            if length + left_weight + right_weight != 5:
                continue
            if length == 0 and left_col >= right_col:
                continue
            if left_col == right_col:
                continue
            if left_assign is not None and right_assign is not None:
                if left_assign[0] == right_assign[0]:
                    continue
            assigns = tuple(x for x in (left_assign, right_assign) if x is not None)
            columns = used_edges | (1 << left_col) | (1 << right_col)
            flag = 1 << len(paths)
            paths.append((columns, assigns, path, l, r))
            for i in list_bits(columns):
                edges_and_roles[i] |= flag
            for fake_index, weight in assigns:
                weights_used[fake_index][weight] = weights_used[fake_index].get(weight, 0) | flag

    def grow(path, used_v, used_edges):
        length = len(path) - 1
        if length == 0 or path[0] < path[-1]:
            add(path, used_edges, length)
        if length < 5:
            for v, i in adj[path[-1]]:
                if not used_v & (1 << v):
                    grow(path + (v,), used_v | (1 << v), used_edges | (1 << i))

    for v in range(order):
        grow((v,), 1 << v, 0)

    incompatible = [{w: sum(mask for other, mask in weights.items() if w != other)
                     for w in weights} for weights in weights_used]
    dead = set()
    def search(remaining, available):
        if not remaining:
            return ()
        key = remaining, available
        if key in dead:
            return None
        rows = min((edges_and_roles[i] & available for i in list_bits(remaining)), key=int.bit_count)
        for j in list_bits(rows):
            columns, assigns, *_ = paths[j]
            conflicts = 0
            for i in list_bits(columns):
                conflicts |= edges_and_roles[i]
            for fake_index, weight in assigns:
                conflicts |= incompatible[fake_index][weight]
            tail = search(remaining ^ columns, available & ~conflicts)
            if tail is not None:
                return (paths[j],) + tail
        dead.add(key)
        return None
    result = search((1 << true_columns) - 1, (1 << len(paths)) - 1)
    if result is not None:
        verify(order, native, fake, bridge_roots, prescribed, result)
    return result


def verify(order, native, fake, bridge_roots, prescribed, result):
    used_edges = Counter()
    roles = Counter()
    weights = {}
    end_base = len(native)
    stub_base = end_base + order
    for _, _, path, left, right in result:
        assert len(set(path)) == len(path)
        assert len(path) - 1 + left[0] + right[0] == 5
        used_edges.update(tuple(sorted(pair)) for pair in zip(path, path[1:]))
        for v, (weight, column, assignment) in ((path[0], left), (path[-1], right)):
            roles[column] += 1
            if column < stub_base:
                assert column == end_base + v and weight == 0 and assignment is None
            elif column < stub_base + 2 * len(fake):
                i, side = divmod(column - stub_base, 2)
                assert fake[i][side] == v and weight in FAKE_WEIGHTS
                assert assignment == (i, weight if side == 0 else 6 - weight)
                old = weights.setdefault(i, assignment[1])
                assert old == assignment[1]
            elif column < stub_base + 2 * len(fake) + len(bridge_roots):
                assert v == bridge_roots[column - stub_base - 2 * len(fake)]
                assert weight == 3 and assignment is None
            else:
                assert (v, weight) == prescribed[column - stub_base - 2 * len(fake) - len(bridge_roots)]
                assert assignment is None
    assert used_edges == Counter(native)
    assert roles == Counter(range(end_base, stub_base + 2 * len(fake) + len(bridge_roots) + len(prescribed)))


def classify(order, actual_edges, matching, split, pretend):
    removed_matching = {matching[i] for i in list_bits(split)}
    bridge_roots = tuple(sorted(v for pair in removed_matching for v in pair))
    native = tuple(sorted(set(actual_edges) - set(pretend) - removed_matching))
    fake = tuple(sorted(pretend))
    result = weight_cover(order, native, fake, bridge_roots)
    if result is None:
        residual = [0] * order
        for v, w in native:
            residual[v] |= 1 << w
            residual[w] |= 1 << v
        native_matching = find_matching(residual, bridge_roots)
        assert native_matching is not None
        print("COUNTEREXAMPLE CANDIDATE", order, native, fake, bridge_roots, native_matching, flush=True)
        raise RuntimeError


def complete_six():
    order = 6
    actual_edges = tuple(combinations(range(order), 2))
    matching = ((0, 1), (2, 3), (4, 5))
    eligible = tuple(edge for edge in actual_edges if edge not in matching)
    for mask in range(1 << len(eligible)):
        fake = tuple(eligible[i] for i in list_bits(mask))
        for broken in (0, 1, 3, 7):
            classify(order, actual_edges, matching, broken, fake)
        if (mask + 1) % 250 == 0:
            print("completed", order, 4 * (mask + 1), flush=True)
    print("completed all", order, 4 * (1 << len(eligible)), flush=True)


def test_cap(order, actual_edges, matching, split, fake, cut_edge, ordered):
    if cut_edge in fake or cut_edge in matching:
        raise ValueError
    removed_matching = {matching[i] for i in list_bits(split)}
    bridge_roots = tuple(sorted(v for pair in removed_matching for v in pair))
    native = tuple(sorted(set(actual_edges) - {cut_edge} - set(fake) - removed_matching))
    fake = tuple(sorted(fake))
    u, v = cut_edge
    types = (((0, 4), (4, 0)), ((1, 3), (3, 1)))
    signatures = tuple((pair,) for choices in types for pair in choices) if ordered else types
    for lengths in signatures:
        if any(weight_cover(order, native, fake, bridge_roots, ((u, 5 - i), (v, 5 - j)))
               is not None for i, j in lengths):
            continue
        print("MISSING PORT SIGNATURE", order, native, fake, bridge_roots, cut_edge, lengths, flush=True)
        raise RuntimeError("Potential counterexample")


def complete_six_caps(ordered):
    order = 6
    edges = tuple(combinations(range(order), 2))
    matching = ((0, 1), (2, 3), (4, 5))
    cut = (0, 2)
    candidates = tuple(e for e in edges if e != cut and e not in matching)
    for mask in range(1 << len(candidates)):
        fake = tuple(candidates[i] for i in list_bits(mask))
        for split in range(8):
            test_cap(order, edges, matching, split, fake, cut, ordered)
        if (mask + 1) % 125 == 0:
            print("checked", 8 * (mask + 1), flush=True)
    print("checked all six vertex caps", 8 * (1 << len(candidates)), flush=True)


def sample(order, samples, caps=False, ordered=False):
    rng = Random(2026112501 + order)
    matching = tuple((v, v + order // 2) for v in range(order // 2))
    residual = {tuple(sorted((u, (u + step) % order))) for u in range(order) for step in (1, 2)}
    for attempt in range(samples):
        current = residual.copy()
        for _ in range(attempt % (5 * order)):
            (a, b), (c, d) = rng.sample(sorted(current), 2)
            if len({a, b, c, d}) != 4:
                continue
            if rng.randrange(2):
                c, d = d, c
            replacement = {tuple(sorted((a, c))), tuple(sorted((b, d)))}
            if replacement & (current | set(matching)):
                continue
            current.difference_update((tuple(sorted((a, b))), tuple(sorted((c, d)))))
            current.update(replacement)
        number_fake = 1 + attempt % len(current)
        selected = rng.sample(sorted(current), number_fake)
        split = rng.randrange(1 << len(matching))
        if caps:
            test_cap(order, current | set(matching), matching, split, tuple(selected[1:]), selected[0],
                     ordered)
        else:
            classify(order, current | set(matching), matching, split, tuple(selected))
        if (attempt + 1) % 100 == 0:
            print("completed sample", order, attempt + 1, flush=True)


def sample_multigraph_caps(order, samples):
    rng = Random(2083741 + order)
    matching = tuple((v, v + 1) for v in range(0, order, 2))
    stubs = [v for v in range(order) for _ in range(4)]
    for attempt in range(samples):
        rng.shuffle(stubs)
        residual = [tuple(sorted(pair)) for pair in zip(stubs[::2], stubs[1::2])]
        cut = residual.pop(rng.randrange(len(residual)))
        keep = set()
        fake = []
        for u, v in residual:
            edge = u, v
            if u != v and edge not in keep and edge not in matching and rng.random() > 0.3:
                keep.add(edge)
            else:
                fake.append(edge)
        split = rng.randrange(1 << len(matching))
        bridge_roots = tuple(sorted(v for i in list_bits(split) for v in matching[i]))
        native = tuple(sorted(keep | {edge for i, edge in enumerate(matching) if not split & (1 << i)}))
        fake = tuple(sorted(fake))
        u, v = cut
        for i in (0, 1, 3, 4):
            if weight_cover(order, native, fake, bridge_roots, ((u, 5-i), (v, 1+i))) is None:
                print("MULTIGRAPH MISSING SIGNATURE", order, native, fake, bridge_roots, cut, i, flush=True)
                raise RuntimeError("Potential counterexample")
        if (attempt + 1) % 100 == 0:
            print("checked decorated caps", order, attempt + 1, flush=True)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--samples", type=int)
    parser.add_argument("--orders", type=int, nargs="+", default=[8, 10, 12])
    parser.add_argument("--caps", action="store_true")
    parser.add_argument("--ordered", action="store_true")
    parser.add_argument("--multigraph", action="store_true")
    args = parser.parse_args()
    if args.samples:
        for order in args.orders:
            if args.multigraph:
                sample_multigraph_caps(order, args.samples)
            else:
                sample(order, args.samples, args.caps, args.ordered)
    elif args.caps:
        complete_six_caps(args.ordered)
    else:
        complete_six()
