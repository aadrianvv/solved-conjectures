"""Barrier for the Lovasz (1,2)-partition route to PCF 5-colouring.

Route tested: split V = V1 + V2 with Delta(G[V1]) <= 1 and Delta(G[V2]) <= 2
(Lovasz partition, obtained by minimising Phi = 2 e(V1) + e(V2)), then colour
V1 from {0,1} and V2 from {2,3,4}.  The 8-vertex K4-free quartic graph below
has a unique Phi-minimising (1,2)-partition and that partition admits no
PCF colouring with these split palettes, although the graph itself is PCF
5-colourable.  Everything is checked exhaustively.

Run:  python pcf-lovasz-partition.py
"""
import itertools
from collections import Counter

ADJ = [[1, 3, 5, 6], [0, 2, 5, 7], [1, 4, 5, 6], [0, 4, 6, 7],
       [2, 3, 6, 7], [0, 1, 2, 7], [0, 2, 3, 4], [1, 3, 4, 5]]
N = len(ADJ)


def pcf(col):
    if any(col[u] == col[v] for v in range(N) for u in ADJ[v]):
        return False
    return all(1 in Counter(col[u] for u in ADJ[v]).values() for v in range(N))


def phi(side):
    return sum((2 if side[v] else 1) for v in range(N) for u in ADJ[v]
               if u > v and side[u] == side[v])


def main():
    assert all(len(set(a)) == 4 and v not in a for v, a in enumerate(ADJ))
    assert all(v in ADJ[u] for v in range(N) for u in ADJ[v])
    assert not any(all(b in ADJ[a] for a, b in itertools.combinations(q, 2))
                   for q in itertools.combinations(range(N), 4)), "K4 present"
    partitions = []
    for side in itertools.product([0, 1], repeat=N):
        if any(sum(side[u] for u in ADJ[v]) > 1 for v in range(N) if side[v]):
            continue
        if any(sum(1 - side[u] for u in ADJ[v]) > 2 for v in range(N) if not side[v]):
            continue
        pal = [[0, 1] if side[v] else [2, 3, 4] for v in range(N)]
        works = any(pcf(col) for col in itertools.product(*pal))
        partitions.append((phi(side), side, works))
    best = min(p[0] for p in partitions)
    minimisers = [p for p in partitions if p[0] == best]
    print("(1,2)-partitions:", len(partitions),
          "with a split-palette PCF colouring:", sum(p[2] for p in partitions))
    print("Phi minimum:", best, "minimisers:", [(p[1], p[2]) for p in minimisers])
    assert all(not p[2] for p in minimisers)
    witness = next(col for col in itertools.product(range(5), repeat=N) if pcf(col))
    print("graph is PCF 5-colourable, e.g.", witness)


if __name__ == "__main__":
    main()
