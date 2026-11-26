from collections import Counter, defaultdict
from functools import cache
from itertools import product
from math import prod

# Connector lengths 1-4 and private cycle lengths 3-4 suffice by the
# endpoint-transfer argument in 06-revised-local-irregularity.md.
COLORS = range(3)
SYMBOL_WIDTH = 9
SYMBOL_COUNT = len(COLORS) * SYMBOL_WIDTH


def encode(color, degree):
    return color * SYMBOL_WIDTH + degree - 1


def build_transfers():
    transfers = [None]
    for length in range(1, 5):
        allowed = [0] * SYMBOL_COUNT
        path_states = set()
        if length > 1:
            for colors in product(COLORS, repeat=length):
                matches = tuple(a == b for a, b in zip(colors, colors[1:]))
                if any(a == b for a, b in zip(matches, matches[1:])):
                    continue
                path_states.add((colors[0], colors[-1], 1 + matches[0], 1 + matches[-1]))
        for first, second in product(range(SYMBOL_COUNT), repeat=2):
            a, x = divmod(first, SYMBOL_WIDTH)
            b, y = divmod(second, SYMBOL_WIDTH)
            x += 1
            y += 1
            if length == 1:
                valid = a == b and x != y
            else:
                valid = any(
                    c == a and d == b and u != x and v != y
                    for c, d, u, v in path_states
                )
            if valid:
                allowed[first] |= 1 << second
        transfers.append(tuple(allowed))
    return tuple(transfers)


TRANSFER = build_transfers()


def permits(length, first, second):
    return TRANSFER[length][first] & (1 << second)


@cache
def local_states(ports, cycles):
    degree = ports + 2 * len(cycles)
    assert degree <= SYMBOL_WIDTH
    found = set()
    for coloring in product(COLORS, repeat=degree):
        counts = tuple(coloring.count(color) for color in COLORS)
        symbols = tuple(encode(color, counts[color]) for color in coloring)
        if all(
            permits(length, symbols[ports + 2 * i], symbols[ports + 2 * i + 1])
            for i, length in enumerate(cycles)
        ):
            found.add(symbols[:ports])
    return tuple(sorted(found))


@cache
def supports(length, possible):
    accepted = 0
    while possible:
        bit = possible & -possible
        possible ^= bit
        accepted |= TRANSFER[length][bit.bit_length() - 1]
    return accepted


def solve(adjacency, domains, queue):
    while queue:
        bit = queue & -queue
        queue ^= bit
        vertex = bit.bit_length() - 1
        if not domains[vertex]:
            return
        for port, (other, other_port, length) in enumerate(adjacency[vertex]):
            possible = 0
            for state in domains[vertex]:
                possible |= 1 << state[port]
            accepted = supports(length, possible)
            kept = tuple(
                state for state in domains[other] if accepted & (1 << state[other_port])
            )
            if not kept:
                return
            if len(kept) < len(domains[other]):
                domains[other] = kept
                queue |= 1 << other

    choices = [(len(domain), v) for v, domain in enumerate(domains) if len(domain) > 1]
    if not choices:
        return tuple(domain[0] for domain in domains)

    _, vertex = min(choices)
    for state in domains[vertex]:
        branch = list(domains)
        branch[vertex] = (state,)
        solution = solve(adjacency, branch, 1 << vertex)
        if solution is not None:
            return solution


def hub_coloring(connectors, lengths, cycles):
    adjacency = [[] for _ in cycles]
    links = []
    for (u, v), length in zip(connectors, lengths):
        a, b = len(adjacency[u]), len(adjacency[v])
        adjacency[u].append((v, b, length))
        adjacency[v].append((u, a, length))
        links.append((u, a, v, b))
    domains = [local_states(len(ports), petals) for ports, petals in zip(adjacency, cycles)]
    domains[0] = tuple(state for state in domains[0] if state[0] < SYMBOL_WIDTH)
    solution = solve(adjacency, domains, (1 << len(cycles)) - 1)
    if solution is None:
        return
    symbols = [(solution[u][a], solution[v][b]) for u, a, v, b in links]
    assert all(permits(length, a, b) for length, (a, b) in zip(lengths, symbols))
    return symbols


def degree_vectors(size, total, lower=3):
    if size == 1:
        if total >= lower:
            yield (total,)
        return
    for first in range(lower, total // size + 1):
        for rest in degree_vectors(size - 1, total - first, first):
            yield (first,) + rest


def multigraphs(degrees):
    size = len(degrees)
    remaining = list(degrees)
    upper = [[0] * size for _ in range(size)]

    def fill(row, col):
        if row == size:
            yield tuple(tuple(line) for line in upper)
        elif col == size:
            if remaining[row] == 0:
                yield from fill(row + 1, row + 1)
        else:
            if row == col:
                limit = remaining[row] // 2
            else:
                limit = min(remaining[row], remaining[col])
            for count in range(limit + 1):
                upper[row][col] = upper[col][row] = count
                remaining[row] -= count
                remaining[col] -= count
                yield from fill(row, col + 1)
                remaining[col] += count
                remaining[row] += count
            upper[row][col] = upper[col][row] = 0

    yield from fill(0, 0)


def connected_edges(size, edges):
    neighbors = [set() for _ in range(size)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    found = {0}
    work = [0]
    while work:
        vertex = work.pop()
        added = neighbors[vertex] - found
        found.update(added)
        work.extend(added)
    return len(found) == size


def noncactus_kernel(size, edges):
    neighbors = [[] for _ in range(size)]
    for index, (u, v) in enumerate(edges):
        neighbors[u].append((v, index))
        neighbors[v].append((u, index))

    def paths(at, target, removed, visited):
        if at == target:
            return 1
        total = 0
        for other, edge in neighbors[at]:
            if edge != removed and not visited & (1 << other):
                total += paths(other, target, removed, visited | (1 << other))
                if total >= 2:
                    return 2
        return total

    return any(paths(u, v, edge, 1 << u) >= 2 for edge, (u, v) in enumerate(edges))


def kernels(size, rank):
    from itertools import permutations

    positions = tuple((u, v) for u in range(size) for v in range(u, size))
    for degrees in degree_vectors(size, 2 * (size + rank - 1)):
        groups = defaultdict(list)
        for i, degree in enumerate(degrees):
            groups[degree].append(i)
        subgroup = tuple(tuple(permutations(group)) for group in groups.values())
        seen = set()
        for matrix in multigraphs(degrees):
            raw = tuple(matrix[u][v] for u, v in positions)
            if raw in seen:
                continue
            edges = tuple(
                (u, v)
                for u, v in positions
                if u != v
                for _ in range(matrix[u][v])
            )
            if not connected_edges(size, edges):
                continue
            for combination in product(*subgroup):
                order = tuple(v for group in combination for v in group)
                seen.add(tuple(matrix[order[u]][order[v]] for u, v in positions))
            if noncactus_kernel(size, edges):
                yield edges, tuple(matrix[v][v] for v in range(size))


def loop_lengths(counts):
    for triangle_counts in product(*(range(count + 1) for count in counts)):
        yield tuple(
            (3,) * tri + (4,) * (count - tri) for count, tri in zip(counts, triangle_counts)
        )


def check_kernel(edges, cycles):
    covered = bytearray(1 << (2 * len(edges)))
    shifts = tuple(range(2 * (len(edges) - 1), -1, -2))
    parallel_pairs = tuple(i for i in range(1, len(edges)) if edges[i] == edges[i - 1])
    solves = 0
    for word in range(len(covered)):
        if covered[word]:
            continue
        lengths = tuple(1 + ((word >> shift) & 3) for shift in shifts)
        if any(lengths[i] == 1 or lengths[i] < lengths[i - 1] for i in parallel_pairs):
            continue
        symbols = hub_coloring(edges, lengths, cycles)
        if symbols is None:
            raise ValueError(f"Uncovered candidate: {edges=}, {lengths=}, {cycles=}")
        solves += 1
        words = (0,)
        for a, b in symbols:
            allowed = tuple(length - 1 for length in range(1, 5) if permits(length, a, b))
            words = tuple((old << 2) + length for old in words for length in allowed)
        for proved in words:
            covered[proved] = 1
        assert covered[word]
    return solves


def controls():
    bridge = ((0, 1),)
    bow_tie = ((3, 3), (3, 3))
    assert hub_coloring(bridge, (1,), bow_tie) is None
    assert hub_coloring(bridge, (2,), bow_tie) is not None


def check_rank_four():
    controls()
    kernel_count = 0
    configuration_count = 0
    solves = 0
    for rank in range(2, 5):
        for size in range(2, 2 * (rank - 1) + 1):
            for edges, loops in kernels(size, rank):
                kernel_count += 1
                per_layout = prod((count + 1) ** 2 for count in Counter(edges).values())
                configuration_count += per_layout * prod(count + 1 for count in loops)
                for cycles in loop_lengths(loops):
                    solves += check_kernel(edges, cycles)
            print(rank, size, kernel_count, configuration_count, solves, flush=True)
    assert (kernel_count, configuration_count) == (87, 1_781_720)
    print("Verified all normalized noncactus cases through cycle rank four.")


if __name__ == "__main__":
    check_rank_four()

