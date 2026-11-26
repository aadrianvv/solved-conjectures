from collections import Counter
from itertools import combinations
from random import Random

from fgk_local_repair_scratch import glue, solve_cluster
from fgk_pair_scratch import identifications, valid_canonical
from fgk_template_scratch import compatible


def complete(trails, rng):
    width = max(v for p in trails for v in p) + 1
    order = 10 * width
    red = tuple(arc for a, b, c, d, e, f in trails for arc in ((c, b), (d, e)))
    blue = tuple(arc for a, b, c, d, e, f in trails for arc in ((b, a), (e, f)))
    base_match = tuple((c, d) for a, b, c, d, e, f in trails)
    graph = [0] * order
    def at(v, copy):
        return v + width * (copy % 10)
    factors = []
    for base, shift in ((red, 1), (blue, 3)):
        arcs = {at(v, j): at(w, j) for j in range(10) for v, w in base}
        tails = sorted(set(range(width)) - {v for v, _ in base})
        heads = sorted(set(range(width)) - {w for _, w in base})
        rng.shuffle(heads)
        arcs.update({at(v, j): at(w, j + shift) for j in range(10) for v, w in zip(tails, heads)})
        factors.append(arcs)
        for v, w in arcs.items():
            graph[v] |= 1 << w
            graph[w] |= 1 << v
    m = tuple((at(v, j), at(w, j)) for j in range(10) for v, w in base_match)
    unused = set(range(width)) - {v for edge in base_match for v in edge}
    m += tuple((at(v, j), at(v, j + 5)) for j in range(5) for v in sorted(unused))
    for v, w in m:
        graph[v] |= 1 << w
        graph[w] |= 1 << v
    assert all(adj.bit_count() == 5 for adj in graph)
    return glue(tuple(graph), m, *factors)


def check(trails):
    set_t = set(trails[0])
    near = {i for i, p in enumerate(trails[1:], 1) if set_t.intersection(p)}
    if any(solve_cluster(trails, (0, i)) is not None for i in near):
        return 2
    shell = near | {i for i, p in enumerate(trails[1:], 1)
                    if any(set(trails[j]).intersection(p) for j in near)}
    if any(solve_cluster(trails, (0, i, j)) is not None
           for i, j in combinations(sorted(shell), 2) if i in near or j in near):
        return 3
    return None


def main():
    t = (0, 1, 2, 3, 4, 1)
    rng = Random(20261125)
    counts = Counter()
    for x, f, g, h, y in identifications("xfghy", 5):
        q = (x, 2, f, g, h, y)
        if len(set(q)) != 6 or not valid_canonical(t, q):
            continue
        if solve_cluster((t, q), (0, 1)) is not None:
            continue
        for s, v, j, k, l in identifications("svjkl", max(t + q) + 1):
            r = (s, v, 4, j, k, l)
            if len(set(r)) != 6 or not compatible((t, q, r)):
                continue
            if solve_cluster((t, q, r), (0, 1, 2)) is not None:
                continue
            for run in range(20):
                full = complete((t, q, r), rng)
                kind = check(full)
                counts[kind] += 1
                if kind is None:
                    print("failed all pairs and triples", full, flush=True)
                    raise RuntimeError
        print("finished initial", q, counts, flush=True)
    print(counts, flush=True)


if __name__ == "__main__":
    main()
