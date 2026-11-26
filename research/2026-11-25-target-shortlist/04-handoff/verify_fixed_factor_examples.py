"""Verify the two restricted-position obstructions in 04-HANDOFF.md."""

from collections import Counter
from itertools import combinations, product


def edge(u, v):
    return tuple(sorted((u, v)))


def path_edges(path):
    return [edge(u, v) for u, v in zip(path, path[1:])]


def verify_fixed_pairings():
    r = (1, 5, 0, 4, 6, 2, 7, 3)
    s = (7, 3, 1, 2, 5, 6, 0, 4)
    m = (5, 7, 4, 6, 2, 0, 3, 1)
    swept = ((3, 1, 0, 5, 2, 0), (6, 5, 1, 7, 3, 4),
             (7, 0, 6, 4, 2, 1), (5, 4, 7, 6, 3, 2))
    vertices = range(8)
    graph = {edge(u, table[u]) for table in (r, s, m) for u in vertices}
    assert len(graph) == 20
    assert Counter(item for path in swept for item in path_edges(path)) == dict.fromkeys(graph, 1)
    center, inner_in, inner_out, outer = ([[] for _ in vertices] for _ in range(4))
    for a, b, c, d, e, f in swept:
        center[c].append(d)
        center[d].append(c)
        for u, v, w in ((c, b, a), (d, e, f)):
            inner_out[u].append(v)
            inner_in[v].append(u)
            outer[v].append(w)
    variables = [u for u in vertices if len(center[u]) != 1]
    tested = 0
    for bits in product((0, 1), repeat=len(variables)):
        choice = dict(zip(variables, bits))

        def arm(u, v):
            head = inner_out[u][center[u].index(v) ^ choice.get(u, 0)]
            end = outer[head][inner_in[head].index(u) ^ choice.get(head, 0)]
            return head, end

        paths = []
        for _, _, u, v, _, _ in swept:
            a, b = arm(u, v)
            c, d = arm(v, u)
            paths.append((b, a, u, v, c, d))
        assert Counter(item for path in paths for item in path_edges(path)) == dict.fromkeys(graph, 1)
        assert any(len(set(path)) < 6 for path in paths)
        tested += 1
    print("8-vertex fixed pairing obstruction", tested, "assignments")


def verify_fixed_factor():
    core_factor = path_edges((0, 4, 2, 3, 1, 5, 0))
    graph = set(core_factor) | set(combinations((0, 1, 2), 2)) | set(combinations((3, 4, 5), 2))
    factor = set(core_factor) | set(path_edges((12, 6, 8, 9, 10, 11, 7, 12)))
    matching = {edge(0, 1), edge(6, 9), edge(7, 10), edge(8, 11)}
    graph.update(e for e in combinations(range(6, 12), 2) if e != (6, 7))
    graph.update(edge(12, u) for u in (0, 1, 6, 7))
    arms = {}
    paths = []
    for i, root in enumerate((2, 3, 4, 5, 12)):
        start = 13 + 7 * i
        graph.add(edge(root, start))
        matching.add(edge(root, start))
        for v in range(7):
            for step in (1, 2):
                item = edge(start + v, start + (v + step) % 7)
                graph.add(item)
                if step == 1:
                    factor.add(item)

        def arm(v):
            return (start + v, start + (v + 1) % 7, start + (v - 1) % 7)

        for u, v in ((3, 6), (2, 5), (1, 4)):
            item = edge(start + u, start + v)
            graph.add(item)
            matching.add(item)
            paths.append(arm(u)[::-1] + arm(v))
        arms[root] = arm(0)
    paths.extend(arms[u][::-1] + (u, v, w) for u, v, w in ((4, 0, 5), (2, 4, 3), (3, 1, 2)))
    paths.extend(((1, 0, 2, 3, 5, 4), arms[5][::-1] + (5, 1, 12),
                  (6, 9, 8, 11, 7, 10), (7, 8, 10, 6, 11, 9),
                  arms[12][::-1] + (12, 6, 8), (11, 10, 9, 7, 12, 0)))
    vertices = range(48)
    assert len(graph) == 120 and all(u < v for u, v in graph)
    assert matching <= graph and factor <= graph and not matching & factor
    for items, degree in ((graph, 5), (matching, 1), (factor, 2)):
        assert Counter(v for item in items for v in item) == dict.fromkeys(vertices, degree)
    assert all(len(path) == len(set(path)) == 6 for path in paths)
    assert Counter(item for path in paths for item in path_edges(path)) == dict.fromkeys(graph, 1)
    print("48-vertex fixed factor example", len(paths), "unrestricted paths")


if __name__ == "__main__":
    verify_fixed_pairings()
    verify_fixed_factor()
