"""Check the forced-matching construction for Favaron–Genest–Kouider Problem 5."""

from argparse import ArgumentParser
from collections import Counter
from dataclasses import dataclass
from itertools import combinations


class GraphBuilder:
    def __init__(self):
        self.order = 0
        self.edges = set()

    def vertices(self, count):
        result = tuple(range(self.order, self.order + count))
        self.order += count
        return result

    def add(self, u, v):
        edge = tuple(sorted((u, v)))
        assert u != v and edge not in self.edges
        self.edges.add(edge)


@dataclass(frozen=True)
class Gadget:
    hubs: tuple
    blocks: tuple
    ports: tuple
    matching: tuple

    @property
    def vertices(self):
        return set(self.hubs).union(*self.blocks)


def forced_gadget(graph, degree):
    hubs = graph.vertices(degree - 2)
    blocks = [graph.vertices(degree + 2) for _ in range(degree)]
    matching = []
    for block in blocks:
        root, p, q, x, y, *rest = block
        for u, v in combinations(block[1:], 2):
            if (u, v) != (p, q):
                graph.add(u, v)
        graph.add(root, p)
        graph.add(root, q)
        matching.extend(((p, x), (q, y)))
        matching.extend(zip(rest[::2], rest[1::2]))
    for i, block in enumerate(blocks):
        for j, hub in enumerate(hubs):
            if (i, j) not in ((0, 0), (1, 1)):
                graph.add(block[0], hub)
    graph.add(hubs[0], hubs[1])
    matching.extend((block[0], hub) for block, hub in zip(blocks[2:], hubs))
    return Gadget(hubs, tuple(blocks), (blocks[0][0], blocks[1][0]), tuple(matching))


def build(degree):
    k = (degree - 1) // 2
    graph = GraphBuilder()
    u, v = graph.vertices(2)
    left = [graph.vertices(degree) for _ in range(k)]
    right = [graph.vertices(degree) for _ in range(k)]
    cliques = tuple((u, block) for block in left) + tuple((v, block) for block in right)
    for hub, block in cliques:
        for a, b in combinations(block, 2):
            graph.add(a, b)
        for port in block[:2]:
            graph.add(hub, port)
    matching = [block[:2] for _, block in cliques]
    replacements = [(u, v)]
    replacements.extend((a, b) for block_u, block_v in zip(left, right)
                        for a, b in zip(block_u[2:], block_v[2:]))
    gadgets = []
    for a, b in replacements:
        gadget = forced_gadget(graph, degree)
        connectors = tuple(zip((a, b), gadget.ports))
        for x, y in connectors:
            graph.add(x, y)
        matching.extend(connectors)
        matching.extend(gadget.matching)
        gadgets.append((connectors, gadget))
    return graph, (u, v), cliques, tuple(gadgets), tuple(matching)


def components(adjacency, vertices):
    remaining = set(vertices)
    while remaining:
        initial = remaining.pop()
        reached = {initial}
        queue = [initial]
        while queue:
            for v in adjacency[queue.pop()] & remaining:
                remaining.remove(v)
                reached.add(v)
                queue.append(v)
        yield reached


def bridges(adjacency):
    """Tarjan's discovery and low-link calculation with an explicit stack."""
    seen = {}
    low = {}
    parent = {}
    found = []
    for initial in adjacency:
        if initial in seen:
            continue
        seen[initial] = low[initial] = len(seen)
        stack = [(initial, iter(adjacency[initial]))]
        while stack:
            u, rest = stack[-1]
            v = next(rest, None)
            if v is None:
                stack.pop()
                if u in parent:
                    p = parent[u]
                    low[p] = min(low[p], low[u])
                    if low[u] > seen[p]:
                        found.append(tuple(sorted((u, p))))
            elif v != parent.get(u):
                if v in seen:
                    low[u] = min(low[u], seen[v])
                else:
                    parent[v] = u
                    seen[v] = low[v] = len(seen)
                    stack.append((v, iter(adjacency[v])))
    return found


def verify_matching(edges, matching, vertices):
    incidence = Counter(v for edge in matching for v in edge)
    assert incidence == Counter(set(vertices))
    assert all(tuple(sorted(edge)) in edges for edge in matching)


# Paths for the 22-vertex starting graph and port certificates for the
# 38-vertex gadget, in order of the first rooted arm's length.
BASE_FIVE_PATHS = (
    (0, 2, 3, 4, 5, 6), (1, 0, 3, 5, 2, 4), (2, 6, 4, 14, 12, 15),
    (3, 6, 16, 13, 15, 14), (5, 15, 16, 14, 13, 12), (16, 12, 1, 17, 18, 19),
    (13, 1, 18, 20, 17, 21), (7, 0, 8, 9, 10, 11), (8, 7, 10, 20, 21, 18),
    (9, 7, 11, 21, 19, 17), (10, 8, 11, 9, 19, 20),
)
GADGET_FIVE_CERTIFICATES = (
    (
        ((3,), (10, 12, 13, 16, 14)),
        (
            (0, 1, 3, 4, 6, 7), (8, 9, 5, 3, 2, 10), (4, 7, 8, 5, 6, 9),
            (5, 7, 9, 4, 8, 6), (11, 13, 14, 12, 15, 16), (12, 16, 11, 14, 15, 13),
            (1, 17, 0, 10, 11, 15), (18, 17, 2, 24, 0, 31), (17, 19, 20, 21, 22, 23),
            (19, 21, 23, 18, 20, 22), (20, 23, 19, 22, 18, 21), (25, 24, 1, 31, 32, 34),
            (2, 31, 33, 35, 36, 37), (32, 35, 34, 37, 33, 36), (33, 34, 36, 32, 37, 35),
            (24, 26, 27, 28, 29, 30), (26, 28, 30, 25, 27, 29), (27, 30, 26, 29, 25, 28),
        ),
    ),
    (
        ((3, 1), (10, 0, 1, 17)),
        (
            (4, 3, 2, 24, 1, 31), (3, 5, 6, 7, 8, 9), (5, 7, 9, 4, 6, 8),
            (6, 9, 5, 8, 4, 7), (0, 17, 18, 20, 21, 22), (18, 23, 21, 19, 22, 20),
            (19, 20, 23, 22, 18, 21), (11, 10, 2, 17, 19, 23), (10, 12, 13, 14, 15, 16),
            (12, 14, 16, 11, 13, 15), (13, 16, 12, 15, 11, 14), (25, 24, 0, 31, 32, 34),
            (2, 31, 33, 35, 36, 37), (32, 35, 34, 37, 33, 36), (33, 34, 36, 32, 37, 35),
            (24, 26, 27, 28, 29, 30), (26, 28, 30, 25, 27, 29), (27, 30, 26, 29, 25, 28),
        ),
    ),
    (
        ((3, 1, 0), (10, 0, 17)),
        (
            (4, 3, 2, 24, 0, 31), (3, 5, 6, 7, 8, 9), (5, 7, 9, 4, 6, 8),
            (6, 9, 5, 8, 4, 7), (1, 17, 18, 20, 21, 22), (18, 23, 21, 19, 22, 20),
            (19, 20, 23, 22, 18, 21), (11, 10, 2, 17, 19, 23), (10, 12, 13, 14, 15, 16),
            (12, 14, 16, 11, 13, 15), (13, 16, 12, 15, 11, 14), (25, 24, 1, 31, 32, 34),
            (2, 31, 33, 35, 36, 37), (32, 35, 34, 37, 33, 36), (33, 34, 36, 32, 37, 35),
            (24, 26, 27, 28, 29, 30), (26, 28, 30, 25, 27, 29), (27, 30, 26, 29, 25, 28),
        ),
    ),
)


def certificate_for_lengths(first_length):
    if first_length <= 2:
        return GADGET_FIVE_CERTIFICATES[first_length]
    arms, paths = GADGET_FIVE_CERTIFICATES[4 - first_length]
    # Interchange the marked hubs and the two marked blocks.
    image = list(range(38))
    image[0], image[1] = 1, 0
    image[3:10], image[10:17] = image[10:17], image[3:10]
    return (tuple(tuple(image[v] for v in arm) for arm in reversed(arms)),
            tuple(tuple(image[v] for v in path) for path in paths))


def verify_unrestricted_five(graph, gadgets):
    replacements = {tuple(sorted(u for u, _ in connectors)): (connectors, gadget)
                    for connectors, gadget in gadgets}
    decomposition = []
    for base_path in BASE_FIVE_PATHS:
        current = (base_path[0],)
        for position, (u, v) in enumerate(zip(base_path, base_path[1:])):
            replaced = tuple(sorted((u, v)))
            if replaced not in replacements:
                current += (v,)
                continue
            connectors, gadget = replacements.pop(replaced)
            at_first_port = u == connectors[0][0]
            first_length = 4 - position if at_first_port else position
            arms, paths = certificate_for_lengths(first_length)
            assert tuple(len(arm) - 1 for arm in arms) == (first_length, 4 - first_length)
            offset = min(gadget.vertices)
            decomposition.extend(tuple(offset + w for w in path) for path in paths)
            left, right = arms if at_first_port else arms[::-1]
            decomposition.append(current + tuple(offset + w for w in left))
            current = tuple(offset + w for w in reversed(right)) + (v,)
        decomposition.append(current)
    assert not replacements
    assert all(len(set(path)) == len(path) == 6 for path in decomposition)
    covered = Counter(tuple(sorted((u, v))) for path in decomposition for u, v in zip(path, path[1:]))
    assert covered == Counter(graph.edges)
    print("unrestricted five-edge paths", len(decomposition))


def verify(degree):
    graph, hubs, cliques, gadgets, matching = build(degree)
    adjacency = {v: set() for v in range(graph.order)}
    for u, v in graph.edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    assert all(len(neighbors) == degree for neighbors in adjacency.values())
    assert len(list(components(adjacency, adjacency))) == 1
    assert not bridges(adjacency)
    verify_matching(graph.edges, matching, adjacency)

    forced = set()
    for connectors, gadget in gadgets:
        vertices = gadget.vertices
        assert len(vertices) == degree * degree + 3 * degree - 2
        assert len(vertices) % 2 == 0
        assert set(gadget.ports).issubset(vertices)
        boundary = {(u, v) for v in vertices for u in adjacency[v] - vertices}
        assert boundary == set(connectors)
        blocks = list(components(adjacency, vertices - set(gadget.hubs)))
        assert len(blocks) == degree
        assert all(len(block) == degree + 2 and len(block) % 2 for block in blocks)
        assert len(gadget.hubs) == degree - 2
        verify_matching(graph.edges, gadget.matching, vertices - set(gadget.ports))
        # The odd components outnumber the hubs. The even gadget order and
        # its two-edge boundary therefore force both connectors in any PM.
        forced.update(tuple(sorted(edge)) for edge in connectors)

    for hub, block in cliques:
        vertices = set(block)
        assert all(len(adjacency[v] & vertices) == degree - 1 for v in vertices)
        boundary = [(u, v) for u in vertices for v in adjacency[u] - vertices]
        assert len(boundary) == degree
        assert {(u, v) for u, v in boundary if v == hub} == {(u, hub) for u in block[:2]}
        plugs = {tuple(sorted(edge)) for edge in boundary if edge[1] != hub}
        assert len(plugs) == degree - 2 and plugs <= forced
        assert {u for u,v in boundary if v != hub} == set(block[2:])
    for hub in hubs:
        assert sum(tuple(sorted((hub, v))) in forced for v in adjacency[hub]) == 1
        assert adjacency[hub] == ({v for h, block in cliques if h == hub for v in block[:2]} |
                                  {v for v in adjacency[hub] if tuple(sorted((hub, v))) in forced})
    print("degree", degree, "vertices", graph.order, "edges", len(graph.edges),
          "bridges", 0, "matching", len(matching), "forced connector edges", len(forced))
    if degree == 5:
        verify_unrestricted_five(graph, gadgets)


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--degrees", type=int, nargs="+", default=[5, 7, 9])
    args = parser.parse_args()
    for degree in args.degrees:
        if degree < 5 or degree % 2 == 0:
            parser.error("each degree must be an odd integer at least five")
        verify(degree)
