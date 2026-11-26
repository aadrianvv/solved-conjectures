from functools import cache
from itertools import permutations
from pathlib import Path
import time

import full_cactus as check


def k4_cube_certificate(caps, witnesses):
    """Check each spanning cube then verify that their union covers every choice."""
    port_count = 3 * check.W
    support = [
        [sum(1 << m for m in check.MODES if check.permits(m, x, y))
         for y in range(port_count)]
        for x in range(port_count)
    ]
    assert all(support[x][y] == support[y][x]
               for x in range(port_count) for y in range(port_count))

    cap_masks = {}
    for i, (domain, _) in enumerate(caps):
        for state in domain:
            cap_masks[state] = cap_masks.get(state, 0) | (1 << i)

    edges = tuple((a, b) for a in range(4) for b in range(a + 1, 4))
    edge_indices = {edge: i for i, edge in enumerate(edges)}
    neighbors = [tuple(b for b in range(4) if a != b) for a in range(4)]
    changes = [
        (p, tuple(edge_indices[tuple(sorted((p[a], p[b])))] for a, b in edges))
        for p in permutations(range(4))
    ]
    cubes = set()
    for encoded in witnesses:
        states = tuple(tuple(state >> (6*i) & 63 for i in range(3)) for state in encoded)
        allowed_caps = tuple(cap_masks[state] for state in states)
        allowed_edges = tuple(
            support[states[a][neighbors[a].index(b)]][states[b][neighbors[b].index(a)]]
            for a, b in edges
        )
        assert 0 not in allowed_edges
        for vertices, links in changes:
            cubes.add(tuple(allowed_caps[i] for i in vertices) +
                      tuple(allowed_edges[i] for i in links))

    caps_count = len(caps)
    widths = (caps_count,) * 4 + (len(check.MODES),) * 6
    accepts = [[0] * n for n in widths]
    for j, cube in enumerate(sorted(cubes)):
        flag = 1 << j
        for dim, values in enumerate(cube):
            while values:
                bit = values & -values
                accepts[dim][bit.bit_length() - 1] |= flag
                values ^= bit

    @cache
    def complete(depth, candidates):
        if candidates == 0:
            return False
        if depth == len(widths):
            return True
        choices = {candidates & subset for subset in accepts[depth]}
        return all(complete(depth + 1, subset) for subset in choices)

    @cache
    def ordered_caps(depth, minimum, candidates):
        if candidates == 0:
            return False
        if depth == 4:
            return complete(depth, candidates)
        return all(ordered_caps(depth + 1, i, candidates & accepts[depth][i])
                   for i in range(minimum, caps_count))

    print('K4 distinct certified cubes', len(cubes), flush=True)
    assert ordered_caps(0, 0, (1 << len(cubes)) - 1)
    print('K4 mode coverage checked', complete.cache_info(),flush=True)


if __name__=='__main__':
    start = time.time()
    file = Path(__file__).with_name('k4-cactus-witnesses.txt')
    witnesses = [tuple(map(int, line.split(','))) for line in file.read_text().splitlines()]
    assert len(witnesses) == 692
    check.normalize_arcs(check.cap_domains_with_petals(2))
    k4_cube_certificate(check.cap_domains_with_petals(3), witnesses)
    print('seconds',time.time()-start,flush=True)
