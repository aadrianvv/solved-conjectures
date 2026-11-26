from argparse import ArgumentParser

from check_fgk_small import edge_set
from fgk_cut_scratch import build_solver, distinct_cap_graphs


def scan(order, maximum):
    count = 0
    for graph in distinct_cap_graphs(order, (), False, degree=4):
        edges = sorted(edge_set(graph))
        for u,v in edges:
            bridges = tuple(x for x in range(order) if x not in (u,v))
            ports = bridges + (u,v)
            solve = build_solver(graph, ports, len(bridges))
            for i in (1, 3, 0, 4):
                if solve((2,) * len(bridges) + (i, 4-i)) is None:
                    print("MISSING", order, edges, u, v, i, "bridge roots", bridges, flush=True)
                    raise RuntimeError("Candidate")
            count += 1
            if count % 100 == 0:
                print("checked", order, count, flush=True)
            if maximum and count >= maximum:
                return count
    return count


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--orders", nargs="+", type=int, default=[5, 6, 7, 8, 9, 10, 11, 12])
    parser.add_argument("--maximum", type=int)
    args = parser.parse_args()
    for order in args.orders:
        print("order and passed port pairs", order, scan(order, args.maximum), flush=True)
