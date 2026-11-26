from argparse import ArgumentParser
from collections import Counter
from itertools import product
from random import Random

from fgk_local_repair_scratch import solve_cluster
from fgk_template_scratch import compatible


def generic_ring(types):
    n = len(types)
    a = tuple(range(n))
    b = tuple(range(n, 2 * n))
    d = tuple(range(2 * n, 3 * n))
    c = tuple(b[(i + 1) % n] if types[i] == 1 else 3 * n + i for i in range(n))
    e = tuple(c[i - 1] if types[i - 1] == 2 else 4 * n + i for i in range(n))
    return tuple((a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(n))


def add_aliases(trails, rng, samples):
    for _ in range(samples):
        values = sorted({v for p in trails for v in p})
        if len(values) <= 6:
            break
        old, new = rng.sample(values, 2)
        attempt = tuple(tuple(new if v == old else v for v in p) for p in trails)
        if all(len(set(p)) == 5 for p in attempt) and compatible(attempt):
            trails = attempt
    return trails


def check(trails):
    blue = {(p[i], p[j]) for p in trails for i, j in ((1, 0), (4, 5))}
    return solve_cluster(trails, tuple(range(len(trails))), blue)


def main():
    parser = ArgumentParser()
    parser.add_argument("--lengths", type=int, nargs="+", default=[3,4,5,6,7,8])
    parser.add_argument("--attempts", type=int, default=10)
    args = parser.parse_args()
    rng = Random(20261125)
    for n in args.lengths:
        stats = Counter()
        for tail in product((1, 2), repeat=n-1):
            types = (2,) + tail
            if set(types) != {1, 2}:
                continue
            if any((types[i:] + types[:i]) > types for i in range(n)):
                continue
            base = generic_ring(types)
            if not compatible(base):
                stats["invalid"] += 1
                continue
            sample = check(base)
            stats["generic"] += 1
            if sample is None:
                print("blocked generic", types, base, flush=True)
                return
            if types.count(2) == 1:
                print("single type 2", types, "trails", base, "repair", sample, flush=True)
            for rep in range(args.attempts):
                actual = add_aliases(base, rng, 4 * n + rep)
                if check(actual) is None:
                    stats["blocked alias"] += 1
                    if stats["blocked alias"] == 1:
                        print("blocked alias", types, actual, "uncolored",
                              solve_cluster(actual, tuple(range(n))), flush=True)
                else:
                    stats["aliases"] += 1
        print(n, stats, flush=True)


if __name__ == "__main__":
    main()
