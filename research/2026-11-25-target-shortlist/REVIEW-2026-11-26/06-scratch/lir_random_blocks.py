"""Referee scratch: random subcubic block trees for Corollary B.

Blocks are subdivided K4, subdivided theta3 or doubled-square kernels (all with
subcubic kernels), joined by bridges at block vertices of block-degree two;
plus pendant paths and pendant triangles (via bridges) at free degree-2 slots.
Usage: python lir_random_blocks.py SEED COUNT
"""
import random, sys
from lir_random_check import lir3, subdivide, KERNELS

def build(rng):
    n = 0; edges = []; slots = []  # slots: vertices of degree 2 with a free incidence
    def add_block():
        nonlocal n
        name = rng.choice(['K4', 'K4', 'theta3', 'dsq'])
        kn, ke = KERNELS[name]
        while True:
            bn, be = subdivide(rng, kn, ke, 3)
            if bn > kn: break
        off = n
        edges.extend((a+off, b+off) for a, b in be)
        n += bn
        deg = [0]*bn
        for a, b in be: deg[a] += 1; deg[b] += 1
        new = [v+off for v in range(bn) if deg[v] == 2]
        return new
    slots = add_block()
    for _ in range(rng.randint(1, 3)):
        if not slots: break
        s = slots.pop(rng.randrange(len(slots)))
        new = add_block()
        t = new.pop(rng.randrange(len(new)))
        L = rng.randint(1, 3)  # bridge path length
        prev = s
        for _ in range(L-1):
            edges.append((prev, n)); prev = n; n += 1
        edges.append((prev, t))
        slots.extend(new)
    for _ in range(rng.randint(0, 3)):
        if not slots: break
        s = slots.pop(rng.randrange(len(slots)))
        if rng.random() < 0.5:
            L = rng.randint(1, 3); prev = s
            for _ in range(L):
                edges.append((prev, n)); prev = n; n += 1
        else:  # bridge to a triangle
            edges.append((s, n)); a = n; n += 1
            edges += [(a, n), (n, n+1), (a, n+1)]; n += 2
    return n, edges

def main():
    seed, count = map(int, sys.argv[1:3])
    rng = random.Random(seed)
    done = 0
    for _ in range(count):
        n, edges = build(rng)
        deg = [0]*n
        for a, b in edges: deg[a] += 1; deg[b] += 1
        assert max(deg) <= 3
        if len(edges) > 60: continue
        done += 1
        if not lir3(n, edges):
            print('COUNTEREXAMPLE', n, edges, flush=True); return 1
    print('no counterexample among', done, 'block-tree graphs', flush=True)
    return 0

if __name__ == '__main__':
    sys.exit(main())
