"""Generate all connected simple cubic graphs of order n (third session tool).

Method: edge insertion on connected cubic multigraphs with loops, starting from the
theta graph and the dumbbell (order 2).  Insertion subdivides two edge slots (possibly
the same edge twice) and joins the two new vertices.  One insertion removes at most two
defects (a defect is a loop or an extra parallel copy), so a multigraph of order m is
kept only if its defect count is at most min(N - m, CAP).  Deduplication: walk-count and distance
invariant buckets and networkx (multi)graph isomorphism.  Completeness is certified only by the
counts of OEIS A002851 (1, 2, 5, 19, 85, 509, 4060, 41301 for n = 4, ..., 18), which
the script asserts.

Usage: python cubic_gen.py N -> writes cubic-n.txt for even n <= N into the current
directory (one graph per line, edge list "a-b a-b ...").
"""
import sys

import networkx as nx

CAP = 2  # defect cap for intermediate multigraphs; completeness is certified only by the counts
KNOWN = {4: 1, 6: 2, 8: 5, 10: 19, 12: 85, 14: 509, 16: 4060, 18: 41301, 20: 510489}


def defects(g):
    d = 0
    for a, b in set(tuple(sorted(e)) for e in g.edges()):
        m = g.number_of_edges(a, b)
        d += m if a == b else m - 1
    return d


def insertions(g):
    n = g.number_of_nodes()
    E = list(g.edges(keys=True))
    for i in range(len(E)):
        for j in range(i, len(E)):
            h = g.copy()
            u, v = n, n + 1
            a, b, k = E[i]
            if i == j:
                h.remove_edge(a, b, key=k)
                h.add_edges_from([(a, u), (u, v), (v, b), (u, v)])
            else:
                c, d, l = E[j]
                h.remove_edge(a, b, key=k)
                h.remove_edge(c, d, key=l)
                h.add_edges_from([(a, u), (u, b), (c, v), (v, d), (u, v)])
            yield h


def key_of(h):
    """Isomorphism invariant: sorted per-vertex closed-walk counts (multigraph adjacency
    matrix powers 2..9) together with BFS distance profiles.  (WL hashing is useless here:
    it cannot separate regular graphs.)"""
    import numpy as np
    nodes = list(h.nodes())
    idx = {v: i for i, v in enumerate(nodes)}
    n = len(nodes)
    A = np.zeros((n, n), dtype=np.int64)
    for a, b in h.edges():
        if a == b:
            A[idx[a], idx[a]] += 2
        else:
            A[idx[a], idx[b]] += 1
            A[idx[b], idx[a]] += 1
    P = A.copy()
    walks = []
    for _ in range(8):
        P = P @ A
        walks.append(np.diag(P).tolist())
    prof = []
    for v in nodes:
        dist = nx.single_source_shortest_path_length(h, v)
        cnt = [0] * n
        for d in dist.values():
            cnt[d] += 1
        prof.append((tuple(w[idx[v]] for w in walks), tuple(cnt)))
    return str(sorted(prof))


def generate(N):
    cur = [nx.MultiGraph([(0, 1), (0, 1), (0, 1)]), nx.MultiGraph([(0, 0), (0, 1), (1, 1)])]
    for n in range(4, N + 1, 2):
        buckets = {}
        out = []
        for g in cur:
            for h in insertions(g):
                if defects(h) > min(N - n, CAP):
                    continue
                key = key_of(h)
                lst = buckets.setdefault(key, [])
                if any(nx.is_isomorphic(h, k) for k in lst):
                    continue
                lst.append(h)
                out.append(nx.convert_node_labels_to_integers(h))
        cur = out
        simple = [g for g in cur if defects(g) == 0]
        print(n, 'kept', len(cur), 'simple', len(simple), 'A002851', KNOWN.get(n), flush=True)
        assert KNOWN.get(n) is None or len(simple) == KNOWN[n]
        with open(f'cubic-{n}.txt', 'w') as fh:
            for g in simple:
                fh.write(' '.join(f'{a}-{b}' for a, b in g.edges()) + chr(10))


def load(n, path='.'):
    out = []
    with open(f'{path}/cubic-{n}.txt') as fh:
        for line in fh:
            g = nx.Graph()
            for tok in line.split():
                a, b = map(int, tok.split('-'))
                g.add_edge(a, b)
            out.append([sorted(g[v]) for v in range(n)])
    return out


if __name__ == '__main__':
    generate(int(sys.argv[1]))
