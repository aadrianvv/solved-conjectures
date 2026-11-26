from functools import cache
from itertools import permutations, product
from pathlib import Path
import time

import full_cactus as check


def kernel_cubes(caps_by_arity, connectors, witnesses, verify_order):
    order = 1 + max(b for _, b in connectors)
    neighbors = tuple(tuple(i for i, edge in enumerate(connectors) if v in edge)
                      for v in range(order))
    arities = tuple(map(len, neighbors))
    port_count = 3 * check.W
    support = [
        [sum(1 << m for m in check.MODES if check.permits(m, x, y))
         for y in range(port_count)]
        for x in range(port_count)
    ]
    assert all(support[x][y] == support[y][x]
               for x in range(port_count) for y in range(port_count))
    cap_masks = {}
    for arity in set(arities):
        masks = {}
        for i, (domain, _) in enumerate(caps_by_arity[arity]):
            for state in domain:
                masks[state] = masks.get(state, 0) | 1 << i
        cap_masks[arity] = masks

    edge_indices = {}
    for i, edge in enumerate(connectors):
        edge_indices.setdefault(edge, []).append(i)
    changes = []
    for vertices in permutations(range(order)):
        images = [tuple(sorted((vertices[a],vertices[b]))) for a,b in connectors]
        if sorted(images) != list(connectors):
            continue
        choices = [tuple(permutations(edge_indices[image])) for image in sorted(set(images))]
        for permutation_blocks in product(*choices):
            assignment = dict(zip(sorted(set(images)), map(iter,permutation_blocks)))
            links = tuple(next(assignment[image]) for image in images)
            changes.append(tuple(vertices) + tuple(order+i for i in links))

    seen = set()
    for encoded in witnesses:
        states = tuple(tuple(state >> (6*i) & 63 for i in range(arity))
                       for state, arity in zip(encoded, arities, strict=True))
        allowed_caps = tuple(cap_masks[arity][state] for arity, state in zip(arities,states))
        allowed_edges = tuple(
            support[states[a][neighbors[a].index(i)]][states[b][neighbors[b].index(i)]]
            for i,(a,b) in enumerate(connectors)
        )
        assert 0 not in allowed_edges
        cube = allowed_caps + allowed_edges
        for mapping in changes:
            permuted = tuple(cube[i] for i in mapping)
            if permuted not in seen:
                seen.add(permuted)
                yield tuple(permuted[i] for i in verify_order)


def check_kernel_cover(caps_by_arity, connectors, witnesses, sorted_caps):
    order = 1 + max(b for _, b in connectors)
    arities = tuple(sum(v in e for e in connectors) for v in range(order))
    verify_order = tuple(range(order, order+len(connectors))) + tuple(range(order))
    cap_widths = tuple(len(caps_by_arity[d]) for d in arities)
    widths = (len(check.MODES),)*len(connectors) + cap_widths
    parallel = tuple(a == b for a,b in zip(connectors,connectors[1:])) + (False,)
    dimensions = len(widths)
    tables = [[None] for _ in widths]
    known = [{} for _ in widths]
    flags = tuple(tuple(1<<i for i in range(d)) for d in widths)

    def intern(depth, children):
        if not any(children):
            return 0
        old = known[depth].get(children)
        if old is not None:
            return old
        args = tables[depth]
        result = len(args)
        args.append(children)
        known[depth][children] = result
        return result

    @cache
    def seed(depth, minimum):
        if depth == dimensions:
            return 1
        if depth < len(connectors) and parallel[depth]:
            tail = (seed(depth+1,max(i,1)) for i in range(minimum, widths[depth]))
        elif depth >= len(connectors) and sorted_caps and depth < dimensions-1:
            tail = (seed(depth+1,i) for i in range(minimum, widths[depth]))
        else:
            fallthrough = seed(depth+1,0)
            tail = (fallthrough,) * (widths[depth] - minimum)
        return intern(depth,(0,)*minimum + tuple(tail))

    root = seed(0,0)
    full = tuple((1<<d)-1 for d in widths)
    for index, cube in enumerate(kernel_cubes(caps_by_arity, connectors,witnesses,verify_order),1):
        compact = dimensions
        while compact > 0 and cube[compact-1] == full[compact-1]:
            compact -= 1

        @cache
        def subtract(depth, node):
            if node == 0 or depth == compact:
                return 0
            children = tables[depth][node]
            mask = cube[depth]
            remainder = tuple(subtract(depth+1,child) if flag & mask else child
                              for child, flag in zip(children,flags[depth]))
            if remainder == children:
                return node
            return intern(depth,remainder)

        root = subtract(0,root)
        subtract.cache_clear()
        if root == 0:
            print('kernel certification passed at cube',index,flush=True)
            return
        if index % 5000 == 0:
            print('kernel coverage status',index,sum(map(len,tables)),flush=True)
    raise AssertionError('certificate did not cover all cases')


def run():
    check.normalize_arcs(check.cap_domains_with_petals(2))
    caps = {d: check.cap_domains_with_petals(d) for d in [3,4]}
    folder = Path(__file__).parent
    shapes = [
        ('k4-cactus',((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)),True,692),
        ('rank3-triangle',((0,1),(0,1),(0,2),(0,2),(1,2)),False,484),
        ('rank3-double-square',((0,1),(0,1),(0,2),(1,3),(2,3),(2,3)),False,1366),
    ]
    for name, edges, cap_order, count in shapes:
        started = time.time()
        witnesses = [tuple(map(int,line.split(','))) for line in (folder/(name+'-witnesses.txt')).read_text().splitlines()]
        assert len(witnesses) == count
        print('checking',name,flush=True)
        check_kernel_cover(caps, edges, witnesses, cap_order)
        print('seconds',time.time()-started,flush=True)


if __name__=='__main__':
    run()
