from argparse import ArgumentParser
from collections import Counter
from itertools import product
from random import Random

from check_fgk_small import edge_set, isomorphic, label_graph, list_bits


def degree_sequence_graphs(degrees, marks):
    order = len(degrees)
    adjacency = [0] * order
    remaining = list(degrees)
    all_vertices = (1 << order) - 1

    def visit(v):
        if v == order:
            yield tuple(all_vertices ^ (1 << x) ^ a for x, a in enumerate(adjacency))
            return
        groups = {}
        for w in range(v + 1, order):
            if remaining[w]:
                groups.setdefault((marks[w], degrees[w], adjacency[w]), []).append(w)
        groups = list(groups.values())
        room = sum(map(len, groups))
        if remaining[v] > room or any(d > order - v - 1 for d in remaining[v + 1:]):
            return

        def choices(k, needed, room):
            if not needed:
                yield ()
                return
            group = groups[k]
            for take in range(max(0, needed - room + len(group)), min(needed, len(group)) + 1):
                for rest in choices(k + 1, needed - take, room - len(group)):
                    yield tuple(group[:take]) + rest

        for neighbors in choices(0, remaining[v], room):
            for w in neighbors:
                adjacency[v] ^= 1 << w
                adjacency[w] ^= 1 << v
                remaining[w] -= 1
            yield from visit(v + 1)
            for w in neighbors:
                adjacency[v] ^= 1 << w
                adjacency[w] ^= 1 << v
                remaining[w] += 1
    yield from visit(0)


def distinct_cap_graphs(order, roots, ordered, degree=5):
    counts = Counter(roots)
    marks = tuple((roots.index(v) + 1 if ordered else 1) if v in counts else 0
                  for v in range(order))
    degrees = tuple(order - degree - 1 + counts[v] for v in range(order))
    bins = {}
    for graph in degree_sequence_graphs(degrees, marks):
        labels = tuple(zip(marks, label_graph(graph)))
        bucket = bins.setdefault(tuple(sorted(labels)), [])
        if not any(isomorphic(graph, old, labels, old_labels) for old, old_labels in bucket):
            bucket.append((graph, labels))
            yield graph


def find_matching(graph, excluded=()):
    def match(remaining):
        if not remaining:
            return ()
        v = min(list_bits(remaining), key=lambda w: (graph[w] & remaining).bit_count())
        for w in list_bits(remaining & graph[v]):
            rest = match(remaining ^ (1 << v) ^ (1 << w))
            if rest is not None:
                return ((v, w),) + rest
        return None
    if len(set(excluded)) != len(excluded):
        return None
    return match(((1 << len(graph)) - 1) ^ sum(1 << v for v in excluded))


def build_solver(graph, roots, bridge_count=0, path_length=5):
    edges = sorted(edge_set(graph))
    adj = [[] for v in graph]
    for i, (v, w) in enumerate(edges):
        adj[v].append((w, i))
        adj[w].append((v, i))
    end_base = len(edges)
    port_base = end_base + len(graph)
    all_columns = (1 << (port_base + len(roots))) - 1
    paths = []
    rows = [0] * (port_base + len(roots))
    native_rows = 0
    port_rows = {}
    link_rows = {}
    vertices_at_port = {}
    half = path_length // 2

    def add(path, columns, kind):
        flag = 1 << len(paths)
        paths.append((path, columns, kind))
        for i in list_bits(columns):
            rows[i] |= flag
        if kind != -1:
            key = kind[0] if isinstance(kind, tuple) else kind
            for v in path:
                vertices_at_port[key, v] = vertices_at_port.get((key, v), 0) | flag
        return flag

    def grow(vertices, used_vertices, used_edges, max_vertices):
        if len(vertices) == max_vertices:
            yield vertices, used_edges
            return
        for v, i in adj[vertices[-1]]:
            if not used_vertices & (1 << v):
                yield from grow(vertices + (v,), used_vertices | (1 << v),
                                 used_edges | (1 << i), max_vertices)

    for v in range(len(graph)):
        for path, used_edges in grow((v,), 1 << v, 0, path_length + 1):
            if path[0] < path[-1]:
                columns = used_edges | (1 << (end_base + path[0]))
                columns |= 1 << (end_base + path[-1])
                native_rows |= add(path, columns, -1)

    def solve(signature, transit=None):
        if (len(edges) - sum(signature)) % path_length:
            return None
        if transit is not None and not isinstance(transit, dict):
            left, right = transit
            transit = {left: right, right: left}
        available = native_rows
        for index, (root, length) in enumerate(zip(roots, signature)):
            key = index, length
            if key not in port_rows:
                port_rows[key] = 0
                for path, used_edges in grow((root,), 1 << root, 0, length + 1):
                    columns = used_edges | (1 << (end_base + path[-1])) | (1 << (port_base + index))
                    port_rows[key] |= add(path, columns, index)
            available |= port_rows[key]
            if index >= bridge_count and bridge_count and length >= half + 1:
                if key not in link_rows:
                    link_rows[key] = 0
                    for root_index, bridge_root in enumerate(roots[:bridge_count]):
                        for path, used_edges in grow((root,), 1 << root, 0, length - half):
                            if path[-1] == bridge_root:
                                columns = used_edges | (1 << (port_base + index))
                                columns |= 1 << (port_base + root_index)
                                link_rows[key] |= add(path, columns, (index, root_index))
                available |= link_rows[key]
        impossible = set()

        def dfs(remaining, available):
            if not remaining:
                return ()
            state = (remaining, available) if transit is not None else remaining
            if state in impossible:
                return None
            options = min((rows[i] & available for i in list_bits(remaining)), key=int.bit_count)
            for j in list_bits(options):
                path, columns, kind = paths[j]
                conflicts = 0
                for i in list_bits(columns):
                    conflicts |= rows[i]
                key = kind[0] if isinstance(kind, tuple) else kind
                if transit is not None and key in transit:
                    partner = transit[key]
                    for v in path:
                        conflicts |= vertices_at_port.get((partner, v), 0)
                tail = dfs(remaining ^ columns, available & ~conflicts)
                if tail is not None:
                    return ((kind, path),) + tail
            impossible.add(state)
            return None

        result = dfs(all_columns, available)
        if result is None:
            return None
        used = Counter()
        terminals = []
        ports = []
        for kind, path in result:
            assert len(path) == len(set(path))
            used.update(tuple(sorted(edge)) for edge in zip(path, path[1:]))
            if isinstance(kind, tuple):
                connector, bridge = kind
                assert connector >= bridge_count and bridge < bridge_count
                assert len(path) + half == signature[connector]
                assert path[0] == roots[connector] and path[-1] == roots[bridge]
                ports.extend(kind)
            elif kind == -1:
                assert len(path) == path_length + 1
                terminals.append(path[-1])
                terminals.append(path[0])
            else:
                assert len(path) == signature[kind] + 1 and path[0] == roots[kind]
                ports.append(kind)
                terminals.append(path[-1])
        assert used == Counter(edges)
        assert sorted(terminals) == list(range(len(graph)))
        assert sorted(ports) == list(range(len(roots)))
        return result
    return solve


def pairings(vertices):
    if not vertices:
        yield ()
        return
    u, *rest = vertices
    for v in rest:
        for pairing in pairings([x for x in rest if x != v]):
            yield ((u, v),) + pairing


def hub_signatures(degree, bridge_count):
    vertices = tuple(range(degree - 1))
    half = degree // 2
    lengths = sorted(range(degree - 1), key=lambda l: abs(l - (half - 0.5)))
    for u in vertices:
        for v in vertices:
            if v == u:
                continue
            for partners in pairings([x for x in vertices if x not in (u, v)]):
                transit = {bridge_count + x: bridge_count + y for a, b in partners
                           for x, y in ((a, b), (b, a))}
                for left_lengths in product(lengths, repeat=len(partners)):
                    signature = [0] * len(vertices)
                    signature[u] = degree - 1
                    signature[v] = half - 1
                    for (a, b), l in zip(partners, left_lengths):
                        signature[a] = l
                        signature[b] = degree - 2 - l
                    yield (half,) * bridge_count + tuple(signature), transit


def sample_bridge_cores(order, num_ports, samples):
    rng = Random(20261125 + order * 20 + num_ports)
    base_edges = {tuple(sorted((v, (v + difference) % order)))
                  for v in range(order) for difference in (1, 2)}
    seen = set()
    for i in range(samples):
        possible_pairs = [(v, (v + order // 2) % order) for v in range(order)]
        rng.shuffle(possible_pairs)
        matching = set()
        matched = set()
        requested = (order - num_ports) // 2
        for v, w in possible_pairs:
            if len(matching) == requested:
                break
            if v not in matched and w not in matched:
                matching.add(tuple(sorted((v, w))))
                matched.update((v, w))
        if len(matching) < requested:
            continue
        roots = tuple(sorted(set(range(order)) - matched))
        residual = base_edges.copy()
        for _ in range(i % (4 * order)):
            (a, b), (c, d) = rng.sample(sorted(residual), 2)
            if len({a, b, c, d}) < 4:
                continue
            if rng.randrange(2):
                c, d = d, c
            replacement = {tuple(sorted((a, c))), tuple(sorted((b, d)))}
            if replacement & (residual | matching):
                continue
            residual.difference_update((tuple(sorted((a, b))), tuple(sorted((c, d)))))
            residual.update(replacement)
        graph = [0] * order
        for v, w in residual | matching:
            graph[v] |= 1 << w
            graph[w] |= 1 << v
        graph = tuple(graph)
        if graph not in seen:
            seen.add(graph)
            yield graph, roots
    

def main():
    parser = ArgumentParser()
    parser.add_argument("--orders", nargs="+", type=int, required=True)
    parser.add_argument("--ports", type=int, required=True)
    parser.add_argument("--cut", action="store_true")
    parser.add_argument("--shared", action="store_true")
    parser.add_argument("--samples", type=int)
    parser.add_argument("--maximum", type=int)
    parser.add_argument("--bridges", type=int, default=0)
    parser.add_argument("--overlap", type=int, default=1)
    parser.add_argument("--three", action="store_true")
    parser.add_argument("--hub", action="store_true")
    parser.add_argument("--degree", type=int, default=5)
    parser.add_argument("--target-arm", action="store_true")
    parser.add_argument("--composed-arm", action="store_true")
    args = parser.parse_args()
    for order in args.orders:
        roots = (0, 0) if args.shared else tuple(range(args.ports))
        if args.bridges:
            bridge_roots = tuple(range(args.bridges))
            first_connector = args.bridges - args.overlap
            if args.shared:
                roots = bridge_roots + (first_connector,) * args.ports
            else:
                roots = bridge_roots + tuple(range(first_connector, first_connector + args.ports))
        if any(v not in range(order) for v in roots):
            continue
        if args.samples:
            cases = sample_bridge_cores(order, args.ports, args.samples)
        else:
            ordered = args.cut or args.target_arm or args.composed_arm or ((args.three or args.hub) and args.bridges)
            cases = ((graph, roots) for graph in distinct_cap_graphs(order, roots, ordered, args.degree))
        seen = Counter()
        for graph, roots in cases:
            assert all(bits.bit_count() + roots.count(v) == args.degree for v, bits in enumerate(graph))
            if args.composed_arm:
                prefix = roots[:args.bridges]
                ports = roots[args.bridges:]
                witness = tuple(find_matching(graph, prefix + (v,)) for v in ports)
                eligible = []
                for target, exterior in enumerate(ports):
                    others = [i for i in range(3) if i != target]
                    if any(ports[x] == exterior or graph[exterior] & (1 << ports[x]) for x in others):
                        continue
                    if not any(witness[i] is not None for i in others):
                        continue
                    eligible.append((target, others))
                if not eligible:
                    continue
                solve = build_solver(graph, roots, args.bridges)
                for target, others in eligible:
                    for exterior_length in (0, 1, 3, 4):
                        inside_length = 6 - exterior_length
                        for a in range(max(inside_length-4, 0), min(inside_length, 4)+1):
                            b = inside_length - a
                            lengths = [exterior_length] * 3
                            lengths[others[0]], lengths[others[1]] = a,b
                            transit = None
                            if exterior_length == 3 and a and b:
                                transit = tuple(args.bridges + ix for ix in others)
                            if solve((2,) * args.bridges + tuple(lengths), transit):
                                break
                        else:
                            print("COMPOSED CAP HOLE", order, roots, target, exterior_length,
                                  sorted(edge_set(graph)), witness, flush=True)
                            raise RuntimeError("Potential counterexample")
                    seen["eligible port"] += 1
                counter = sum(seen.values())
                if counter % 100 == 0:
                    print("processed", order, roots, counter, flush=True)
                if args.maximum and counter >= args.maximum:
                    break
                continue
            if args.target_arm:
                prefix = roots[:args.bridges]
                ports = roots[args.bridges:]
                target = next((i for i,v in enumerate(ports) if v not in prefix), None)
                if target is None:
                    continue
                port = ports[target]
                if any(i != target and (v == port or graph[v] & (1 << port))
                       for i,v in enumerate(ports)):
                    continue
                witnesses = tuple(find_matching(graph, prefix + (v,)) for v in ports)
                if witnesses[target] is None or not any(w for i,w in enumerate(witnesses) if i != target):
                    continue
                solve = build_solver(graph, roots, args.bridges)
                selected = None
                other = [i for i in range(3) if i != target]
                for length in (2, 1, 0):
                    signature = [4] * 3
                    signature[other[0]] = length
                    signature[other[1]] = 2 - length
                    if solve((2,) * args.bridges + tuple(signature)):
                        selected = tuple(signature)
                        break
                if selected is None:
                    print("NO DESIGNATED ARM", order, roots, target, sorted(edge_set(graph)),
                          witnesses, flush=True)
                    raise RuntimeError("Potential counterexample")
                seen[selected] += 1
                total = sum(seen.values())
                if total % 100 == 0:
                    print("processed", order, roots, total, flush=True)
                if args.maximum and total >= args.maximum:
                    break
                continue
            if args.hub:
                matching = find_matching(graph, roots[:args.bridges])
                if matching is None:
                    continue
                solve = build_solver(graph, roots, args.bridges, args.degree)
                result = next((sig for sig, transit in hub_signatures(args.degree, args.bridges)
                               if solve(sig, transit) is not None), None)
                if result is None:
                    print("NO HUB ATTACHMENT", args.degree, order, roots, sorted(edge_set(graph)), matching,
                          flush=True)
                    raise RuntimeError("Potential counterexample")
                seen[result] += 1
                total = sum(seen.values())
                if total % 50 == 0:
                    print("processed", args.degree, order, roots, total, flush=True)
                if args.maximum and total >= args.maximum:
                    break
                continue
            if args.three:
                prefix = roots[:args.bridges]
                usable_matching = [find_matching(graph, prefix + (v,)) for v in roots[args.bridges:]]
                if all(matching is None for matching in usable_matching):
                    continue
                solve = build_solver(graph, roots, args.bridges)
                prefix_lengths = (2,) * args.bridges
                choices = ((4, 2, 0), (4, 0, 2), (2, 4, 0), (2, 0, 4), (0, 4, 2), (0, 2, 4),
                           (4, 1, 1), (1, 4, 1), (1, 1, 4))
                result = next((signature for signature in choices if solve(prefix_lengths + signature)), None)
                if result is None:
                    from itertools import permutations
                    trials = product(((0, 3, 3), (1, 2, 3)), permutations(range(3)))
                    for lengths, order_of_indices in trials:
                        signatures = [0] * 3
                        for ix, l in zip(order_of_indices, lengths):
                            signatures[ix] = l
                        transit = tuple(args.bridges + ix for ix in order_of_indices[:2])
                        if solve(prefix_lengths + tuple(signatures), transit):
                            result = (tuple(signatures), transit)
                            break
                if result is None:
                    print("NO SHARED 3-CAP ATTACHMENT", order, roots, sorted(edge_set(graph)), usable_matching,
                          flush=True)
                    raise RuntimeError("Potential counterexample")
                seen[result] += 1
                total = sum(seen.values())
                if total % 100 == 0:
                    print("processed", order, roots, total, flush=True)
                if args.maximum and total >= args.maximum:
                    break
                continue
            if args.cut:
                m0 = find_matching(graph, roots[:args.bridges])
                m2 = find_matching(graph, roots)
                if m0 is None and m2 is None:
                    continue
                signatures = {(2,) * args.bridges + (i, 4 - i) for i in range(5)}
            else:
                m0 = None
                m2 = find_matching(graph, roots)
                if m2 is None:
                    continue
                signatures = {(2,) * len(roots)}
            solve = build_solver(graph, roots, args.bridges)
            results = frozenset(signature for signature in sorted(signatures) if solve(signature) is not None)
            if args.cut:
                results = frozenset(signature[-2:] for signature in results)
            seen[m0 is not None, m2 is not None, tuple(sorted(results))] += 1
            if not results or (args.cut and len(results) != 5 and
                               seen[m0 is not None, m2 is not None, tuple(sorted(results))] == 1):
                print("restricted", order, roots, graph, sorted(edge_set(graph)), m0, m2, results, flush=True)
            if not results:
                raise RuntimeError("Counterexample to extendability across these boundary ports")
            counter = sum(seen.values())
            if args.maximum and counter >= args.maximum:
                break
            if counter % 100 == 0:
                print("processed", order, roots, counter, flush=True)
        print(order, roots, seen, flush=True)


if __name__ == "__main__":
    main()
