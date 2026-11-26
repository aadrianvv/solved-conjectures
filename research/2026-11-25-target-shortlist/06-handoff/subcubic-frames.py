"""Subdivision frames for locally irregular 3-edge-colourings of subcubic graphs.

Standalone, standard library only (Python 3.12+).  See the section
"Subdivision frames" in ../06-revised-local-irregularity.md.

A frame of a graph G is an independent set Y of vertices of degree 2 or 3,
together with a chosen neighbour s(y) for every y in Y of degree 3.
T = edges yx with x a neighbour of y other than s(y);  S = E(G) - T.
H = multigraph on X = V - Y with one edge x1x2 for every y (its two T-neighbours).
Conditions:
  (F1) S is locally irregular (d_S differs at the ends of every S-edge);
  (F2*) E(H) has a 2-colouring in which every H-vertex of degree 2 sees two
        colours and every H-vertex of degree 3 sees one colour.
       (forest mode: H is a forest, a special case of F2*.)
Frame Lemma: a frame gives an explicit locally irregular 3-edge-colouring
(S in colour 1, both T-edges of y in colour 2 + c(e_y)).

Every frame found below is converted into that explicit colouring and the
colouring is checked directly, independently of the search code.

Usage:
  python subcubic-frames.py exhaustive N [forest]   all connected subcubic graphs, orders 1..N
  python subcubic-frames.py cubic NMIN NMAX STEP SAMPLES SEED   random connected cubic graphs
  python subcubic-frames.py control
"""
import itertools
import random
import sys
from collections import Counter, defaultdict

sys.setrecursionlimit(100000)

# ---------------------------------------------------------------- graphs

def refine(adj, col):
    n = len(adj)
    while True:
        sig = [(col[v], tuple(sorted(col[u] for u in adj[v]))) for v in range(n)]
        keys = sorted(set(sig))
        index = {k: i for i, k in enumerate(keys)}
        new = [index[s] for s in sig]
        if len(keys) == len(set(col)):
            return new
        col = new


def canon(adj):
    """Canonical edge list by individualisation-refinement (exact, small n)."""
    n = len(adj)
    best = [None]

    def rec(col):
        col = refine(adj, col)
        if len(set(col)) == n:
            pos = {v: col[v] for v in range(n)}
            code = tuple(sorted(tuple(sorted((pos[u], pos[v])))
                                for u in range(n) for v in adj[u] if u < v))
            if best[0] is None or code < best[0]:
                best[0] = code
            return
        cnt = Counter(col)
        cell = min((c for c in cnt if cnt[c] > 1), key=lambda c: (cnt[c], c))
        for v in [v for v in range(n) if col[v] == cell]:
            c2 = [2 * x for x in col]
            c2[v] -= 1
            rec(c2)

    rec([len(a) for a in adj])
    return best[0]


def to_adj(code, n):
    adj = [[] for _ in range(n)]
    for a, b in code:
        adj[a].append(b)
        adj[b].append(a)
    return adj


def connected_subcubic(N):
    """Yield (n, adj) for all connected graphs of maximum degree <= 3, orders 1..N.

    Every connected graph on n vertices arises from a connected graph on n-1
    vertices by adding a vertex (delete a non-cut vertex), so augmentation by a
    new vertex joined to 1..3 vertices of degree < 3 is exhaustive."""
    cur = {canon([[]])}
    yield 1, [[]]
    for n in range(2, N + 1):
        nxt = set()
        for code in cur:
            adj = to_adj(code, n - 1)
            low = [v for v in range(n - 1) if len(adj[v]) < 3]
            for k in (1, 2, 3):
                for S in itertools.combinations(low, k):
                    a2 = [list(x) for x in adj] + [list(S)]
                    for v in S:
                        a2[v].append(n - 1)
                    nxt.add(canon(a2))
        cur = nxt
        for code in sorted(cur):
            yield n, to_adj(code, n)


def rand_cubic(n, rng):
    while True:
        stubs = [v for v in range(n) for _ in range(3)]
        rng.shuffle(stubs)
        E = set()
        ok = True
        for i in range(0, 3 * n, 2):
            a, b = sorted(stubs[i:i + 2])
            if a == b or (a, b) in E:
                ok = False
                break
            E.add((a, b))
        if not ok:
            continue
        adj = [[] for _ in range(n)]
        for a, b in E:
            adj[a].append(b)
            adj[b].append(a)
        seen = {0}
        stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        if len(seen) == n:
            return adj

# ------------------------------------------------------- H conditions

def h_edges(adj, st):
    out = []
    for y in range(len(adj)):
        if st[y] != -1:
            tn = [x for k, x in enumerate(adj[y]) if k != st[y]]
            out.append((tn[0], tn[1], y))
    return out


def h_two_colouring(edges):
    """Spanning-forest propagation; returns {y: 0/1} or None.  Exact: by the
    fundamental-cycle argument in the note, a colouring exists iff this
    propagation is consistent."""
    inc = defaultdict(list)
    for a, b, y in edges:
        inc[a].append((b, y))
        inc[b].append((a, y))
    col = {}
    tree = set()
    seen = set()
    for r in list(inc):
        if r in seen:
            continue
        seen.add(r)
        queue = [(r, None)]
        for x, parent_y in queue:
            kids = [(z, y) for z, y in inc[x] if y != parent_y and z not in seen]
            # mark tree edges, avoid taking two parallel copies to the same child
            chosen = []
            used = set()
            for z, y in kids:
                if z not in used and z not in seen:
                    used.add(z)
                    chosen.append((z, y))
            d = len(inc[x])
            pc = col.get(parent_y) if parent_y is not None else None
            for i, (z, y) in enumerate(chosen):
                if d == 2:
                    c = (1 - pc) if pc is not None else i % 2
                else:
                    c = pc if pc is not None else 0
                col[y] = c
                tree.add(y)
                seen.add(z)
                queue.append((z, y))
    # non-tree edges: colour forced at each end by a tree edge there
    def forced(x, y):
        es = inc[x]
        tree_cols = [col[yy] for _, yy in es if yy in tree]
        if not tree_cols:
            return None
        if len(es) == 2:
            return 1 - tree_cols[0]
        return tree_cols[0]
    for a, b, y in edges:
        if y in tree:
            continue
        fa, fb = forced(a, y), forced(b, y)
        if fa is None or fb is None or fa != fb:
            return None
        col[y] = fa
    for x, es in inc.items():
        cs = [col[y] for _, y in es]
        if len(es) == 2 and cs[0] == cs[1]:
            return None
        if len(es) >= 3 and len(set(cs)) != 1:
            return None
    return col


def h_is_forest(edges):
    par = {}

    def find(a):
        while par.setdefault(a, a) != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    for a, b, _ in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        par[ra] = rb
    return True

# ------------------------------------------------------------- search

def find_frame(adj, forest=False):
    """Backtracking search.  state[v]: -1 means v in X; k >= 0 means v in Y and
    s(v) = adj[v][k]; -2 means v in Y of degree 2."""
    n = len(adj)
    deg = [len(a) for a in adj]
    order = []
    mark = [False] * n
    for s in range(n):
        if mark[s]:
            continue
        mark[s] = True
        q = [s]
        for x in q:
            order.append(x)
            for y in adj[x]:
                if not mark[y]:
                    mark[y] = True
                    q.append(y)
    st = [None] * n

    def t_of(x):
        t = 0
        for y in adj[x]:
            s = st[y]
            if s is None:
                return None
            if s != -1 and (s == -2 or adj[y][s] != x):
                t += 1
        return t

    def sdeg(v):
        s = st[v]
        if s is None:
            return None
        if s == -1:
            t = t_of(v)
            return None if t is None else deg[v] - t
        return deg[v] - 2

    def local_ok(v):
        for u in [v] + adj[v]:
            if st[u] is None:
                continue
            su = sdeg(u)
            for w in adj[u]:
                if st[w] is None:
                    continue
                if st[u] != -1 and st[w] != -1:
                    return False
                s_edge = (st[u] == -1 and st[w] == -1) or \
                    (st[u] >= 0 and adj[u][st[u]] == w) or \
                    (st[w] >= 0 and adj[w][st[w]] == u)
                if s_edge and su is not None:
                    sw = sdeg(w)
                    if sw is not None and sw == su:
                        return False
        return True

    def final():
        E = h_edges(adj, st)
        return h_is_forest(E) if forest else h_two_colouring(E) is not None

    def rec(i):
        if i == n:
            return final()
        v = order[i]
        opts = [-1]
        if all(st[u] is None or st[u] == -1 for u in adj[v]):
            if deg[v] == 3:
                opts += [0, 1, 2]
            elif deg[v] == 2:
                opts += [-2]
        for o in opts:
            st[v] = o
            if local_ok(v) and rec(i + 1):
                return True
        st[v] = None
        return False

    return list(st) if rec(0) else None

# ------------------------------------------- independent verification

def colouring_from_frame(adj, st):
    n = len(adj)
    E = h_edges(adj, st)
    hc = h_two_colouring(E)
    assert hc is not None
    col = {}
    for u in range(n):
        for v in adj[u]:
            if st[u] == -1 and st[v] == -1:
                col[frozenset((u, v))] = 1
    for y in range(n):
        if st[y] != -1:
            for k, x in enumerate(adj[y]):
                col[frozenset((x, y))] = 1 if k == st[y] else 2 + hc[y]
    return col


def is_locally_irregular_colouring(adj, col, k=3):
    n = len(adj)
    edges = [frozenset((u, v)) for u in range(n) for v in adj[u] if u < v]
    if any(e not in col for e in edges) or len(set(col.values())) > k:
        return False

    def d(v, c):
        return sum(1 for u in adj[v] if col[frozenset((u, v))] == c)
    for e in edges:
        u, v = tuple(e)
        if d(u, col[e]) == d(v, col[e]):
            return False
    return True


def lir_at_most(adj, k=3):
    """Exact backtracking: does G have a locally irregular k-edge-colouring?"""
    n = len(adj)
    E = sorted({tuple(sorted((a, b))) for a in range(n) for b in adj[a]})
    if not E:
        return True
    inc = [[i for i, e in enumerate(E) if v in e] for v in range(n)]
    last = [max(x) if x else -1 for x in inc]
    col = [None] * len(E)

    def mult(v, c):
        return sum(1 for i in inc[v] if col[i] == c)

    def ok(i):
        for v in E[i]:
            if last[v] == i:
                for j in inc[v]:
                    u = E[j][0] + E[j][1] - v
                    if last[u] <= i and mult(u, col[j]) == mult(v, col[j]):
                        return False
        return True

    def rec(i, used):
        if i == len(E):
            return True
        for c in range(min(k, used + 1)):
            col[i] = c
            if ok(i) and rec(i + 1, max(used, c + 1)):
                return True
        col[i] = None
        return False
    return rec(0, 0)

# ---------------------------------------------------------------- drivers

def exhaustive(N, forest):
    counts = defaultdict(lambda: [0, 0, 0, []])
    for n, adj in connected_subcubic(N):
        rec = counts[n]
        rec[0] += 1
        st = find_frame(adj, forest)
        if st is not None:
            col = colouring_from_frame(adj, st)
            assert is_locally_irregular_colouring(adj, col), adj
            rec[1] += 1
        elif not lir_at_most(adj, 3):
            rec[2] += 1
        else:
            rec[3].append(adj)
    for n in sorted(counts):
        total, framed, no3, exc = counts[n]
        print(f"order {n}: graphs {total}, framed+verified {framed}, "
              f"no locally irregular 3-colouring {no3}, 3-colourable without frame {len(exc)} {exc}")


def cubic(nmin, nmax, step, samples, seed):
    rng = random.Random(seed)
    for n in range(nmin, nmax + 1, step):
        for _ in range(samples):
            adj = rand_cubic(n, rng)
            st = find_frame(adj)
            assert st is not None, adj
            assert is_locally_irregular_colouring(adj, colouring_from_frame(adj, st))
        print(f"cubic order {n}: {samples} random graphs framed and verified")


def control():
    k4 = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    w5 = [[3, 4], [2, 3, 4], [1, 3, 4], [0, 1, 2], [0, 1, 2]]
    b10 = [[4, 5], [4, 5], [6, 7], [6, 7], [0, 1, 8], [0, 1, 8], [2, 3, 9], [2, 3, 9],
           [4, 5, 9], [6, 7, 8]]
    print("K4: F2* frame", find_frame(k4) is not None, "| 3-colourable", lir_at_most(k4))
    for name, g in [("W5", w5), ("B10", b10)]:
        print(name, ": forest frame", find_frame(g, True) is not None,
              "| F2* frame", find_frame(g) is not None, "| 3-colourable", lir_at_most(g))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "control"
    if mode == "exhaustive":
        exhaustive(int(sys.argv[2]), len(sys.argv) > 3 and sys.argv[3] == "forest")
    elif mode == "cubic":
        cubic(*map(int, sys.argv[2:7]))
    else:
        control()
