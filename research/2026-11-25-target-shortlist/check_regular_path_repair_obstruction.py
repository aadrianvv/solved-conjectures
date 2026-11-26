"""Verify a bounded repair obstruction and the cases for an odd defect cycle."""

from collections import Counter
from functools import cache
from itertools import combinations, product


def path_edges(path):
    return tuple(tuple(sorted(pair)) for pair in zip(path, path[1:]))


def solve_cluster(trails, indices, directed=(), allow_triangles=False):
    edges = sorted(edge for index in indices for edge in path_edges(trails[index]))
    neighbors = {}
    for index, (u, v) in enumerate(edges):
        neighbors.setdefault(u, []).append((v, index))
        neighbors.setdefault(v, []).append((u, index))
    possible = [[] for edge in edges]

    def eligible(path):
        if not allow_triangles:
            return len(set(path)) == 6
        return all(path[i] != path[j] or (i, j) in {(0, 3), (2, 5)}
                   for i, j in combinations(range(6), 2))

    def add_paths(path, used):
        if len(path) == 6:
            if (eligible(path) and path[0] < path[-1] and (path[0], path[1]) not in directed
                    and (path[-1], path[-2]) not in directed):
                for index in range(len(edges)):
                    if used & (1 << index):
                        possible[index].append((used, path))
            return
        for vertex, index in neighbors[path[-1]]:
            if not used & (1 << index) and (allow_triangles or vertex not in path):
                add_paths(path + (vertex,), used | (1 << index))

    for vertex in neighbors:
        add_paths((vertex,), 0)
    complete = (1 << len(edges)) - 1

    @cache
    def search(used):
        if used == complete:
            return ()
        next_edge = next(index for index in range(len(edges)) if not used & (1 << index))
        for candidate, path in possible[next_edge]:
            if candidate & used:
                continue
            rest = search(used | candidate)
            if rest is not None:
                return (path,) + rest
        return None

    solution = search(0)
    if solution is not None:
        assert all(len(path) == 6 and eligible(path) and path[0] != path[-1] for path in solution)
        assert Counter(edge for path in solution for edge in path_edges(path)) == Counter(edges)
        assert all((p[0], p[1]) not in directed and (p[-1], p[-2]) not in directed for p in solution)
    return solution


def compatible_gluing(trails):
    edges = [edge for trail in trails for edge in path_edges(trail)]
    if len(set(edges)) != len(edges) or any(u == v for u, v in edges):
        return False
    centers = [vertex for trail in trails for vertex in trail[2:4]]
    if len(set(centers)) != len(centers):
        return False
    for left, right in (((2, 1), (3, 4)), ((1, 0), (4, 5))):
        arcs = [(trail[i], trail[j]) for trail in trails for i, j in (left, right)]
        if any(len({arc[end] for arc in arcs}) != len(arcs) for end in (0, 1)):
            return False
    return True


def verify_cycle_triples():
    for short_cycle in (True, False):
        counts = Counter()
        # A 3-cycle has no coincidences between d_i and any b_j. In a longer
        # cycle the only possible coincidences in three consecutive pieces
        # are d_0 = b_2 and d_2 = b_0.
        assignments = ((7, 9),) if short_cycle else product((2, 7), (0, 9))
        for d_0, d_2 in assignments:
            b = (0, 1, 2)
            c = (3, 4, 5)
            d = (d_0, 8, d_2)
            e = (5 if short_cycle else 6, 3, 4)
            possible_a = []
            for i in range(3):
                known = set(c + d + e) - set(b) - {c[i], d[i], e[i]}
                possible_a.append(sorted(known) + [10 + i])
            for a in product(*possible_a):
                if len(set(a)) != 3:
                    continue
                trails = tuple((a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3))
                if not compatible_gluing(trails):
                    continue
                blue = {(p[i], p[j]) for p in trails for i, j in ((1, 0), (4, 5))}
                solution = solve_cluster(trails, (0, 1, 2), blue)
                counts[solution is not None] += 1
                if solution is None:
                    assert not short_cycle and d[1] in (a[0], a[2])
        assert counts == (Counter({True: 52}) if short_cycle else Counter({True: 169, False: 4}))
        print("cycle triple cases", "length 3" if short_cycle else "length at least 5", counts)


class Builder:
    def __init__(self):
        self.last = 0
        self.trails = []

    def new(self):
        label = self.last
        self.last += 1
        return label

    def defect(self, b=None):
        a = self.new()
        if b is None:
            b = self.new()
        c, d, e = (self.new() for _ in range(3))
        self.trails.append((a, b, c, d, e, b))
        return a, b, c, d, e

    def companion(self, root, position):
        path = tuple(root if i == position else self.new() for i in range(6))
        self.trails.append(path)
        return path


def create():
    b = Builder()
    root = b.defect()
    first_child = b.defect(root[2])
    second_child = b.defect(root[4])
    for child in (first_child, second_child):
        for position in (2, 4):
            b.defect(child[position])
    for a, _, _, d, _ in (root, first_child, second_child):
        b.companion(a, 2)
        b.companion(a, 2)
        b.companion(d, 1)
        b.companion(d, 0)
    b.companion(root[1], 2)
    return saturate_builder(b)


def saturate_builder(b):
    old_end = b.last
    degree = Counter(v for p in b.trails for edge in path_edges(p) for v in edge)
    endpoints = {v for p in b.trails for v in (p[0], p[-1])}
    sat = sorted(v for v, d in degree.items() if d == 5)
    edges = set(e for p in b.trails for e in path_edges(p))
    neighbors = {v: {w for w in range(old_end) if tuple(sorted((v, w))) in edges} for v in sat}
    def saturate(required, used):
        if not required:
            return ()
        v = min(required, key=lambda x: len(neighbors[x] - used))
        for w in sorted(neighbors[v] - used):
            more = saturate(required - {v, w}, used | {v, w})
            if more is not None:
                return ((v, w),) + more
        return None
    first = saturate(set(sat), set())
    assert first is not None
    matching = list(first)
    matched = {v for pair in matching for v in pair}
    for v in range(old_end):
        room = 5 - degree[v]
        while room:
            position = 0 if v not in endpoints else 2
            p = b.companion(v, position)
            if position == 0:
                endpoints.add(v)
                room -= 1
            else:
                room -= 2
            if v not in matched:
                w = p[position + 1]
                assert w not in matched
                matching.append((v, w))
                matched.update((v, w))
    assert set(range(old_end)) <= matched
    return tuple(b.trails), tuple(matching), old_end, b.last


def check_local(trails, target_id=0):
    target = set(trails[target_id])
    neighbor = {i for i, p in enumerate(trails) if i != target_id and target.intersection(p)}
    shell = {i for i, p in enumerate(trails) if i != target_id and
             any(set(trails[j]).intersection(p) for j in neighbor)}
    shell |= neighbor
    sizes = Counter()
    solutions = []
    for size in (2, 3):
        for other in combinations(sorted(shell if size == 3 else neighbor), size - 1):
            if not neighbor.intersection(other):
                continue
            cluster = (target_id,) + other
            sizes[size] += 1
            solution = solve_cluster(trails, cluster)
            if solution is not None:
                solutions.append((cluster, solution))
    for cluster, solution in solutions:
        print("repair", [trails[i] for i in cluster], solution)
    print("local", target_id, sizes, "repairs", len(solutions))
    assert not solutions


def finish(trails, partial_matching, order):
    assert order % 2 == 0
    degree = Counter(v for p in trails for edge in path_edges(p) for v in edge)
    old_ends = {v for p in trails for v in (p[0], p[-1])}
    terminals = Counter(v for v in range(order) if v not in old_ends)
    interiors = Counter({v: (5 - degree[v] - terminals[v]) // 2 for v in range(order)})
    matched = {v for pair in partial_matching for v in pair}
    unmatched = [v for v in range(order) if v not in matched]
    interior_vertex = [v for v in unmatched if v not in old_ends]
    terminal_vertex = [v for v in unmatched if v in old_ends]
    templates = [[None] * 6 for _ in range(sum(terminals.values()) // 2)]
    reserved = {}

    def place(i, j, v):
        assert templates[i][j] is None
        templates[i][j] = v
        pool = terminals if j in (0, 5) else interiors
        pool[v] -= 1
        assert pool[v] >= 0

    def reserve(i, j, v):
        place(i, j, v)
        place(i, j + 1, v)
        reserved[i, j] = v

    for ix, v in enumerate(interior_vertex):
        reserve(ix // 2, (0, 4)[ix % 2], v)
    possible = []
    for i, p in enumerate(templates):
        free = [j for j in range(1, 5) if p[j] is None]
        possible.extend((i, left) for left, right in zip(free[::2], free[1::2]) if left + 1 == right)
    assert len(possible) >= len(terminal_vertex)
    for (i, j), v in zip(possible, terminal_vertex):
        reserve(i, j, v)
    left_end = iter(terminals.elements())
    left_internal = iter(interiors.elements())
    for i, p in enumerate(templates):
        for j in range(6):
            if p[j] is None:
                p[j] = next(left_end if j in (0, 5) else left_internal)
    assert next(left_end, None) is None
    assert next(left_internal, None) is None

    shifts_used = Counter()
    offsets = []
    match_shift = {}
    for i, p in enumerate(templates):
        offsets.append([0])
        for j, edge in enumerate(path_edges(p)):
            shift = 1 + 2 * shifts_used[edge]
            shifts_used[edge] += 1
            offsets[-1].append(offsets[-1][-1] + shift)
            if (i, j) in reserved:
                match_shift[reserved[i, j]] = shift
    assert set(match_shift) == set(unmatched)
    width = 1 << max(4 * max(shifts_used.values()), max(p[-1] for p in offsets)).bit_length()
    def at(v, i):
        return v + (i % width) * order
    whole = tuple(tuple(at(v, i) for v in p) for i in range(width) for p in trails)
    whole += tuple(tuple(at(v, i + s) for v, s in zip(p, off)) for i in range(width)
                   for p, off in zip(templates, offsets))
    matching = tuple((at(v, i), at(w, i)) for i in range(width) for v, w in partial_matching)
    matching += tuple((at(v, k * step), at(v, (k + 1) * step))
                      for v, step in match_shift.items() for k in range(0, width, 2))
    return whole, matching, width * order


def verify_square_to_triangle_triples():
    b, c = (0, 1, 2), (3, 4, 5)
    for closed, expected in ((True, 344), (False, 945)):
        e = (c[2] if closed else 6, c[0], c[1])
        corners = set(c + e)
        count = 0
        for first, last in product((7,) if closed else (7, b[2]), (9,) if closed else (9, b[0])):
            d = (first, 8, last)
            possible_terminals = (corners | set(d)) - set(b)
            options = [sorted((possible_terminals - {c[i], e[i]}) | {10 + i}) for i in range(3)]
            for a in product(*options):
                if len(set(a)) != 3:
                    continue
                trails = [(a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                edges = [edge for trail in trails for edge in path_edges(trail)]
                if len(set(edges)) != 15:
                    continue
                for changed in product((False, True), repeat=3):
                    if any(a[i] in corners if changed[i] else a[i] == d[i] for i in range(3)):
                        continue
                    directed = {(e[i], b[i]) for i in range(3)}
                    directed.update((b[i], a[i]) for i in range(3) if not changed[i])
                    result = solve_cluster(trails, range(3), directed, allow_triangles=True)
                    assert result is not None, (trails, changed)
                    assert Counter(edge for path in result for edge in path_edges(path)) == Counter(edges)
                    count += 1
        assert count == expected, (closed, count)
        print("square-to-triangle cycle triples", "closed" if closed else "open", count)


def verify_canonical_obstruction():
    seed = (
        (0, 1, 2, 3, 4, 1),
        (4, 2, 5, 6, 7, 2),
        (14, 3, 10, 11, 12, 13),
        (17, 0, 15, 1, 17, 18),
        (24, 20, 4, 0, 18, 15),
        (3, 40, 41, 42, 43, 44),
    )
    red, blue, matching = {}, {}, {}
    red_inverse, blue_inverse = {}, {}
    next_vertex = max(max(path) for path in seed) + 1

    def fresh():
        nonlocal next_vertex
        vertex = next_vertex
        next_vertex += 1
        return vertex

    def arc(forward, inverse, u, v):
        assert forward.get(u, v) == v and inverse.get(v, u) == u
        forward[u], inverse[v] = v, u

    for a, b, c, d, e, f in seed:
        arc(red, red_inverse, c, b)
        arc(red, red_inverse, d, e)
        arc(blue, blue_inverse, b, a)
        arc(blue, blue_inverse, e, f)
        arc(matching, matching, c, d)

    def image(forward, inverse, vertex):
        if vertex not in forward:
            arc(forward, inverse, vertex, fresh())
        return forward[vertex]

    def trail(centre):
        other = image(matching, matching, centre)
        near = image(red, red_inverse, centre)
        far = image(red, red_inverse, other)
        return (image(blue, blue_inverse, near), near, centre, other, far,
                image(blue, blue_inverse, far))

    def through(vertex):
        return (
            trail(vertex),
            trail(image(red_inverse, red, vertex)),
            trail(image(red_inverse, red, image(blue_inverse, blue, vertex))),
        )

    def unoriented(path):
        return min(path, path[::-1])

    assert {unoriented(path) for path in seed} == {
        unoriented(path) for vertex in set(seed[0]) for path in through(vertex)
    }
    for vertex in sorted({vertex for path in seed for vertex in path}):
        through(vertex)
    labels = sorted(set(red) | set(red_inverse) | set(blue) | set(blue_inverse) | set(matching))
    label_index = {vertex: index for index, vertex in enumerate(labels)}
    width = len(labels)

    def lift(vertex, copy=0):
        return width * (copy % 10) + label_index[vertex]

    def complete(forward, inverse, shift):
        free_sources = [v for v in labels if v not in forward]
        free_targets = [v for v in labels if v not in inverse]
        assert len(free_sources) == len(free_targets)
        return {
            source: target
            for copy in range(10)
            for source, target in (
                [(lift(u, copy), lift(v, copy)) for u, v in forward.items()]
                + [(lift(u, copy), lift(v, copy + shift))
                   for u, v in zip(free_sources, free_targets)]
            )
        }

    r, s = complete(red, red_inverse, 1), complete(blue, blue_inverse, 3)
    m = complete(matching, matching, 5)
    order = 10 * width
    vertices = set(range(order))
    assert all(set(table) == set(table.values()) == vertices for table in (r, s, m))
    assert all(m[v] != v and m[m[v]] == v for v in vertices)
    assert all(s[r[v]] != m[v] for v in vertices)
    edges = {tuple(sorted((u, v))) for table in (r, s, m) for u, v in table.items()}
    assert all(u != v for u, v in edges)
    assert Counter(vertex for edge in edges for vertex in edge) == dict.fromkeys(vertices, 5)
    trails = [(s[r[u]], r[u], u, v, r[v], s[r[v]]) for u, v in sorted(m.items()) if u < v]
    assert Counter(edge for path in trails for edge in path_edges(path)) == dict.fromkeys(edges, 1)
    assert all(len(set(path)) == 6 or (len(set(path)) == 5 and
               (path[1] == path[5] or path[0] == path[4])) for path in trails)
    trail_id = {unoriented(path): index for index, path in enumerate(trails)}

    def local_id(path):
        return trail_id[unoriented(tuple(lift(vertex) for vertex in path))]

    target = local_id(seed[0])
    incident = {vertex: set() for vertex in vertices}
    for i, path in enumerate(trails):
        for vertex in path:
            incident[vertex].add(i)

    def neighbors(i):
        return set().union(*(incident[vertex] for vertex in trails[i])) - {i}

    pairs = {(target, i) for i in neighbors(target)}
    triples = {
        tuple(sorted((target, i, j)))
        for _, i in pairs for j in neighbors(i) | neighbors(target) if j not in (i, target)
    }
    assert solve_cluster(trails, (target,)) is None
    assert all(solve_cluster(trails, indices) is None for indices in pairs | triples)
    four_pieces = tuple(local_id(path) for path in (*seed[:3], trail(red_inverse[5])))
    repair = solve_cluster(trails, four_pieces, set(s.items()))
    assert repair is not None and all(len(path) == len(set(path)) == 6 for path in repair)
    assert Counter(edge for path in repair for edge in path_edges(path)) == Counter(
        edge for index in four_pieces for edge in path_edges(trails[index])
    )
    print("canonical obstruction", order, "vertices", len(pairs), "pairs", len(triples), "triples")


def main():
    verify_square_to_triangle_triples()
    verify_canonical_obstruction()
    verify_cycle_triples()
    trails, matching, old_end, order = create()
    degree = Counter(v for p in trails for edge in path_edges(p) for v in edge)
    ends = Counter(v for p in trails for v in (p[0], p[-1]))
    assert all(degree[v] == 5 for v in range(old_end))
    assert all(degree[v] in (1, 2) for v in range(old_end, order))
    assert len({e for p in trails for e in path_edges(p)}) == 5 * len(trails)
    assert all(ends[v] <= 1 for v in range(order))
    assert len({v for pair in matching for v in pair}) == 2 * len(matching)
    assert {v for pair in matching for v in pair} >= set(range(old_end))
    print("finite radius", "trails", len(trails), "vertices", order, "saturated", old_end, "partial matching", len(matching))
    whole, complete_matching, final_order = finish(trails, matching, order)
    all_edges = tuple(edge for p in whole for edge in path_edges(p))
    assert all(len(set(p)) == 6 or (len(set(p)) == 5 and p[1] == p[-1]) for p in whole)
    edges = set(all_edges)
    assert len(edges) == len(all_edges) == 5 * final_order // 2
    assert Counter(v for edge in all_edges for v in edge) == Counter({v: 5 for v in range(final_order)})
    assert sorted(v for p in whole for v in (p[0], p[-1])) == list(range(final_order))
    assert sorted(v for pair in complete_matching for v in pair) == list(range(final_order))
    assert all(tuple(sorted(pair)) in edges for pair in complete_matching)
    print("full graph", final_order, "trails", len(whole), "matching", len(complete_matching))
    check_local(whole)


if __name__ == "__main__":
    main()
