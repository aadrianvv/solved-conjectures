"""Referee scratch: build the 408-vertex example of 04 and run the independent sweep on it."""
import sys
from collections import Counter
from random import Random
sys.path.insert(0, ".")
import check_regular_path_theoremA_independent as C

N = 68
idx = lambda t, j: "uvabcd".index(t) * N + (j % N)
adj = {v: set() for v in range(6 * N)}
def add(x, y):
    adj[x].add(y); adj[y].add(x)
mate = {}
for j in range(N):
    for p, q in ("ua", "vb", "vc", "ab", "ac", "bc"):
        add(idx(p, j), idx(q, j))
    add(idx("u", j), idx("v", j)); mate[idx("u", j)] = idx("v", j); mate[idx("v", j)] = idx("u", j)
    for (p, q), sh in ((("u", "a"), 6), (("u", "b"), 8), (("u", "d"), 9), (("v", "c"), 10), (("v", "d"), 11), (("d", "d"), 7)):
        add(idx(p, j), idx(q, j + sh))
    for t in "abcd":
        x, y = idx(t, j), idx(t, j + 34)
        add(x, y); mate[x] = y; mate[y] = x
assert all(len(adj[v]) == 5 for v in adj), Counter(len(a) for a in adj.values())
assert all(mate[mate[v]] == v and mate[v] in adj[v] for v in adj)
print("M-triangles", C.m_triangle_count(adj, mate), "M-squares", C.m_square_count(adj, mate),
      "bad pairs", len(C.bad_pairs(adj, mate)))
rng = Random(1)
st = Counter()
for _ in range(20):
    r, s = C.lemma1(adj, mate, rng)
    C.check_P(adj, mate, r, s)
    stats = Counter()
    pieces = C.sweep(adj, mate, r, s, rng, stats, True)
    assert not C.verify_decomposition(adj, pieces)
    st.update(stats)
print("20 constructions verified", dict(st))
