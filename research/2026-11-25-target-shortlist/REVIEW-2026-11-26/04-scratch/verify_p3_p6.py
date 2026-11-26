"""Referee's own re-implementation of the 04c constructions (Problems 3 and 6).
Written from the text of 04c only.  Stdlib only."""
import sys
from collections import defaultdict


def E(u, v):
    return (u, v) if repr(u) < repr(v) else (v, u)


def check_pd(paths, d, label):
    """paths: list of vertex lists. Check: simple paths of d edges, edge-disjoint, graph simple d-regular."""
    edges = set()
    deg = defaultdict(int)
    for p in paths:
        assert len(p) == d + 1, (label, "length", p)
        assert len(set(p)) == d + 1, (label, "not simple", p)
        for a, b in zip(p, p[1:]):
            e = E(a, b)
            assert a != b
            assert e not in edges, (label, "edge reused", e)
            edges.add(e)
            deg[a] += 1
            deg[b] += 1
    assert set(deg.values()) == {d}, (label, "degrees", set(deg.values()))
    return edges, deg


def bridges_side_orders(edges, root):
    """for each edge at root, if it is a bridge return the order of the far side."""
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    out = []
    for nb in sorted(adj[root], key=str):
        # BFS from nb avoiding edge (root,nb)
        seen = {nb}
        st = [nb]
        bridge = True
        while st:
            x = st.pop()
            for y in adj[x]:
                if x == nb and y == root:
                    continue
                if y == root:
                    bridge = False
                    continue
                if y not in seen:
                    seen.add(y)
                    st.append(y)
        out.append((nb, bridge, len(seen) if bridge else None))
    return out, len(adj)


def connected(edges):
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    s = next(iter(adj))
    seen = {s}
    st = [s]
    while st:
        x = st.pop()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                st.append(y)
    return len(seen) == len(adj)


def alt(k):
    p = [0]
    for j in range(1, k + 1):
        p.append(p[-1] + (j if j % 2 == 1 else -j))
    return p


def problem3(d):
    k = (d - 1) // 2
    N = 8 * k + 1
    P = alt(k)
    core = {v: [(v + q) % N for q in P] for v in range(N)}
    x, y = 0, 4 * k
    a = core[(-1) % N]
    assert a[1] == x
    b = core[y]
    a[1], b[0] = y, x
    # core paths: check simple and edge sets
    cedges = set()
    for p in core.values():
        assert len(set(p)) == k + 1
        for u, w in zip(p, p[1:]):
            e = E(u, w)
            assert e not in cedges
            cedges.add(e)
    assert connected(cedges), "core not connected"
    paths = []
    capn = 2 * k + 3
    Q = alt(k)
    tag = 0
    for v, p in core.items():
        root = p[0]
        tag += 1
        lab = lambda i, t=tag: ("c", t, i % capn)
        # cap: attachment vertex 0
        arms = {u: [lab(u + q) for q in Q] for u in range(capn)}
        # complement cycle: step k+1; vertices in cycle order 0, k+1, 2(k+1), ...
        order = [(i * (k + 1)) % capn for i in range(capn)]
        assert len(set(order)) == capn
        i0 = order.index(0)
        rest = [order[(i0 + j) % capn] for j in range(1, capn)]  # path on 2k+2 vertices
        for j in range(0, len(rest), 2):
            u, w = rest[j], rest[j + 1]
            paths.append(list(reversed(arms[u])) + arms[w])
        # core arm reversed from terminal to root, bridge, cap arm at 0
        paths.append(list(reversed(p)) + arms[0])
    edges, deg = check_pd(paths, d, f"P3 d={d}")
    assert connected(edges)
    info, n = bridges_side_orders(edges, x)
    odd_bridges = [t for t in info if t[1] and t[2] % 2 == 1]
    return n, len(edges), len(odd_bridges)


def problem6(d):
    base = [[0, 2, 1, 4, 5, 6, 3, 7], [2, 4, 0, 7, 6, 1, 3, 5], [3, 4, 7, 1, 0, 5, 2, 6], [1, 5, 7, 2, 3, 0, 6, 4]]
    h = (d - 7) // 2
    if h == 0:
        L = 1
    else:
        L = max(2 * h, h * (h + 1) // 2) + 1
    paths = []
    for c in range(L):
        for p in base:
            q = [(v, c) for v in p]
            left = []
            right = []
            cl = cr = c
            for j in range(1, h + 1):
                cl = (cl + j) % L
                cr = (cr + j) % L
                left.append((p[0], cl))
                right.append((p[-1], cr))
            paths.append(list(reversed(left)) + q + right)
    edges, deg = check_pd(paths, d, f"P6 d={d}")
    # middle edges perfect matching
    mid = [E(p[d // 2], p[d // 2 + 1]) for p in paths]
    cov = defaultdict(int)
    for a, b in mid:
        cov[a] += 1
        cov[b] += 1
    assert set(cov.values()) == {1} and len(cov) == len(deg)
    # type-1 edges
    t1 = defaultdict(int)
    for p in paths:
        for i in (d // 2 - 1, d // 2 + 1):
            a, b = p[i], p[i + 1]
            t1[a] += 1
            t1[b] += 1
    bad = [v for v in deg if t1[v] != 2]
    return len(deg), len(edges), len(bad), max(t1.values())


if __name__ == "__main__":
    for d in (5, 7, 9, 11, 13, 15, 17, 19):
        n, m, ob = problem3(d)
        print(f"P3 d={d}: n={n} m={m} path-decomposition OK; odd-side bridges at x: {ob} (>=2 => no PM)")
    for d in (7, 9, 11, 13, 15, 17):
        print("P6 d=%d: n=%d m=%d vertices-with-type1-deg!=2: %d max %d" % ((d,) + problem6(d)))
