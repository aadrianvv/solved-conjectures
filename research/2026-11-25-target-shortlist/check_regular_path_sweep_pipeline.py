"""Run the matched-triangle construction and the square-to-triangle sweep.

For random simple 5-regular graphs with a perfect matching M this script

1. builds the canonical partition of 04-regular-path-decomposition.md
   (matched-triangle pairing, Euler orientation, two cycle covers),
2. applies the simultaneous square-to-triangle sweep, including the odd
   type-2 cycles, exactly as described in that note,
3. verifies that the output is an edge partition into five-edge trails each of
   which is a simple path or has its only repetition between an endpoint and
   the vertex three edges away, and
4. records whether every triangle in a remaining defective trail is an
   M-triangle sharing an edge with an M-square (Theorem A of 04d).

Finite random runs are evidence only.
"""

from argparse import ArgumentParser
from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, product
from random import Random


def edge(u, v):
    return (u, v) if u < v else (v, u)


def path_edges(p):
    return [edge(u, v) for u, v in zip(p, p[1:])]


# ---------------------------------------------------------------------------
# graph generation


def random_matched_graph(n, rng, style):
    """Return (adjacency sets, matching dict) of a simple 5-regular graph."""
    for _ in range(1000):
        adj = [set() for _ in range(n)]
        if style == "random":
            # two random Hamilton cycles plus a random matching, rejected if not simple
            ok = True
            for _ in range(2):
                perm = list(range(n))
                rng.shuffle(perm)
                for i in range(n):
                    u, v = perm[i], perm[(i + 1) % n]
                    if v in adj[u]:
                        ok = False
                    adj[u].add(v)
                    adj[v].add(u)
            if not ok:
                continue
        elif style in ("square", "dense", "far3"):
            # square of a cycle (triangle-rich), optionally with local switches
            for u in range(n):
                for j in (1, 2):
                    adj[u].add((u + j) % n)
                    adj[(u + j) % n].add(u)
            switches = n // 12 if style == "dense" else n // 4
            for _ in range(switches):
                es = sorted({edge(u, v) for u in range(n) for v in adj[u]})
                (a, b), (c, d) = rng.sample(es, 2)
                if len({a, b, c, d}) < 4:
                    continue
                if rng.random() < 0.5:
                    c, d = d, c
                if c in adj[a] or d in adj[b]:
                    continue
                adj[a].discard(b); adj[b].discard(a)
                adj[c].discard(d); adj[d].discard(c)
                adj[a].add(c); adj[c].add(a)
                adj[b].add(d); adj[d].add(b)
        elif style == "k5":
            # disjoint K5's joined later by the matching, then switched a little
            assert n % 5 == 0
            for base in range(0, n, 5):
                for u, v in combinations(range(base, base + 5), 2):
                    adj[u].add(v)
                    adj[v].add(u)
            for _ in range(n // 5):
                es = sorted({edge(u, v) for u in range(n) for v in adj[u]})
                (a, b), (c, d) = rng.sample(es, 2)
                if len({a, b, c, d}) < 4 or c in adj[a] or d in adj[b]:
                    continue
                adj[a].discard(b); adj[b].discard(a)
                adj[c].discard(d); adj[d].discard(c)
                adj[a].add(c); adj[c].add(a)
                adj[b].add(d); adj[d].add(b)
        # perfect matching avoiding H, preferring short distances for local styles
        mate = {}
        order = list(range(n))
        rng.shuffle(order)
        local = style != "random"

        def place(free):
            if not free:
                return True
            u = min(free, key=lambda x: (sum(1 for y in free if y != x and y not in adj[x]), x))
            cands = [y for y in free if y != u and y not in adj[u]]
            if style == "far3":
                # no common neighbour (no M-triangle); prefer residual distance three
                cands = [y for y in cands if not adj[u] & adj[y]]
                two = set().union(*(adj[w] for w in adj[u]))
                cands.sort(key=lambda y: (not any(adj[w] & adj[y] for w in adj[u]), rng.random()))
            elif local:
                cands.sort(key=lambda y: (min((u - y) % n, (y - u) % n) + rng.random() * 3))
            else:
                rng.shuffle(cands)
            for y in cands[:6]:
                mate[u], mate[y] = y, u
                if place(free - {u, y}):
                    return True
                del mate[u], mate[y]
            return False

        if not place(frozenset(order)):
            continue
        for u, v in mate.items():
            adj[u].add(v)
        if all(len(a) == 5 for a in adj):
            return adj, mate
    raise RuntimeError("generation failed")


# ---------------------------------------------------------------------------
# canonical construction


def canonical(adj, mate, rng):
    n = len(adj)
    H = [sorted(w for w in adj[v] if w != mate[v]) for v in range(n)]
    # pairing at each vertex, forced by matched triangles
    pair_of = {}
    for w in range(n):
        nb = H[w][:]
        forced = [(x, y) for x, y in combinations(nb, 2) if mate[x] == y]
        rest = [x for x in nb if all(x not in p for p in forced)]
        rng.shuffle(rest)
        pairs = forced + [tuple(rest[i:i + 2]) for i in range(0, len(rest), 2)]
        assert sorted(x for p in pairs for x in p) == nb
        for k, (x, y) in enumerate(pairs):
            pair_of[(w, x)] = (w, k)
            pair_of[(w, y)] = (w, k)
    # split graph: node (w,k); edge for each H-edge
    inc = defaultdict(list)
    for w in range(n):
        for x in H[w]:
            if w < x:
                inc[pair_of[(w, x)]].append((w, x))
                inc[pair_of[(x, w)]].append((w, x))
    arcs = set()
    seen = set()
    for start in list(inc):
        if start in seen:
            continue
        # walk the cycle
        node = start
        prev_edge = None
        orient = rng.random() < 0.5
        cyc = []
        while True:
            seen.add(node)
            e0, e1 = inc[node]
            nxt = e1 if e0 == prev_edge else e0
            if prev_edge is None and orient:
                nxt = e1
            w = node[0]
            other = nxt[1] if nxt[0] == w else nxt[0]
            cyc.append((w, other))
            prev_edge = nxt
            node = pair_of[(other, w)]
            if node == start:
                break
        for a in cyc:
            arcs.add(a)
    assert len(arcs) == 2 * n
    outs = defaultdict(list)
    ins = defaultdict(list)
    for u, v in arcs:
        outs[u].append(v)
        ins[v].append(u)
    assert all(len(outs[v]) == 2 and len(ins[v]) == 2 for v in range(n))
    # 2-factorise bipartite out/in graph
    colour = {}
    for a in sorted(arcs):
        if a in colour:
            continue
        c = 0 if rng.random() < 0.5 else 1
        cur = a
        side = "out"
        while cur not in colour:
            colour[cur] = c
            u, v = cur
            if side == "out":
                # move through head's in-copy to the other in-arc
                other = [w for w in ins[v] if w != u][0]
                cur = (other, v)
                side = "in"
            else:
                other = [w for w in outs[u] if w != v][0]
                cur = (u, other)
                side = "out"
            c ^= 1
    r = {}
    sinv = {}
    for (u, v), c in colour.items():
        if c == 0:
            assert u not in r
            r[u] = v
        else:
            sinv[u] = v  # second cover arc u->v ; s is the reverse
    s = {v: u for u, v in sinv.items()}
    assert len(r) == n and len(s) == n
    trails = {}
    for u in range(n):
        v = mate[u]
        if u < v:
            trails[(u, v)] = (s[r[u]], r[u], u, v, r[v], s[r[v]])
    return r, s, trails


# ---------------------------------------------------------------------------
# classification


def kind(p):
    reps = [(i, j) for i, j in combinations(range(6), 2) if p[i] == p[j]]
    if not reps:
        return "path"
    if all(x in ((0, 3), (2, 5)) for x in reps):
        return "triangle"
    if reps in ([(1, 5)], [(0, 4)]):
        return "square"
    return "bad"


def sweep(adj, mate, r, s, trails):
    """Apply the simultaneous sweep. Returns list of final trails."""
    n = len(adj)
    rinv = {v: u for u, v in r.items()}
    # orient defective trails as (a,b,c,d,e,b)
    defect = {}
    pieces = {}
    for key, t in trails.items():
        k = kind(t)
        assert k in ("path", "square"), (t, k)
        if k == "square":
            if t[1] == t[5]:
                o = t
            else:
                o = t[::-1]
            assert o[1] == o[5]
            defect[key] = o
        pieces[key] = t
    key_of_vertex = {}
    for key in trails:
        key_of_vertex[key[0]] = key
        key_of_vertex[key[1]] = key
    # target and link type
    target = {}
    link = {}
    for key, (a, b, c, d, e, _) in defect.items():
        f = rinv[c]
        tk = key_of_vertex[f]
        target[key] = tk
        if tk in defect:
            a2, b2, c2, d2, e2, _ = defect[tk]
            if c == b2:
                link[key] = 1
            else:
                assert c == e2, "red head must be b or e"
                link[key] = 2
        else:
            link[key] = 0
    # type-2 graph
    succ = {k: target[k] for k in defect if link[k] == 2}
    pred = {}
    for k, t in succ.items():
        assert t not in pred
        pred[t] = k
    # components
    sources = set()
    oddcycles = []
    visited = set()
    for k in defect:
        if k in visited:
            continue
        # walk back to start
        start = k
        seen_here = {start}
        while start in pred and pred[start] not in seen_here:
            start = pred[start]
            seen_here.add(start)
        if start in pred:  # cycle
            cyc = [start]
            x = succ[start]
            while x != start:
                cyc.append(x)
                x = succ[x]
            visited.update(cyc)
            if len(cyc) % 2 == 0:
                sources.update(cyc[0::2])
            else:
                oddcycles.append(cyc)
        else:
            chain = [start]
            x = start
            while x in succ:
                x = succ[x]
                chain.append(x)
            visited.update(chain)
            sources.update(chain[0::2])
    in_odd = {k for cyc in oddcycles for k in cyc}
    for k in defect:
        assert k in sources or k in in_odd or (k in pred and pred[k] in sources)
    # build new trails
    newA = {}  # pendant change for defects receiving type-1 trade
    recv_good = defaultdict(dict)  # good path key -> {vertex c: new terminal b}
    for k in sources:
        a, b, c, d, e, _ = defect[k]
        if link[k] == 1:
            tk = target[k]
            newA[tk] = r[defect[tk][1]]
            assert newA[tk] == b
        elif link[k] == 0:
            recv_good[target[k]][c] = b
    out = []
    for k in pieces:
        if k in defect:
            a, b, c, d, e, _ = defect[k]
            A = newA.get(k, a)
            if k in sources:
                out.append(("source", (A, b, e, d, c, s[c])))
            elif k in in_odd:
                continue
            else:
                out.append(("recipient", (A, b, c, d, e, r[e])))
        else:
            p = list(pieces[k])
            if k in recv_good:
                for c, b in recv_good[k].items():
                    if p[1] == c:
                        p[0] = b
                    else:
                        assert p[4] == c
                        p[5] = b
                out.append(("good", tuple(p)))
            else:
                out.append(("plain", tuple(p)))
    for cyc in oddcycles:
        L = len(cyc)
        T = []
        for k in cyc:
            a, b, c, d, e, _ = defect[k]
            T.append((newA.get(k, a), b, c, d, e))
        # check c_i = e_{i+1}
        for i in range(L):
            assert T[i][2] == T[(i + 1) % L][4]
        # choose triple 0,1,2 ; pair (3,4),(5,6),...
        triple = [(T[i][0], T[i][1], T[i][2], T[i][3], T[i][4], T[i][1]) for i in range(3)]
        sol = solve_cluster(triple)
        assert sol is not None, triple
        for p in sol:
            out.append(("oddtriple", p))
        for i in range(3, L, 2):
            Ai, bi, ci, di, ei = T[i]
            Aj, bj, cj, dj, ej = T[i + 1]
            out.append(("oddpair", (Ai, bi, ei, di, ci, bj)))
            out.append(("oddpair", (Aj, bj, cj, dj, ci, bi)))
    return out, len(defect), len(oddcycles)


def solve_cluster(trails, require_simple=False):
    edges = sorted({e for t in trails for e in path_edges(t)})
    assert len(edges) == 5 * len(trails)
    idx = {e: i for i, e in enumerate(edges)}
    nb = defaultdict(list)
    for u, v in edges:
        nb[u].append(v)
        nb[v].append(u)
    cands = defaultdict(list)

    def ok(p):
        k = kind(p)
        return k == "path" or (k == "triangle" and not require_simple)

    def ext(p, used):
        if len(p) == 6:
            if p[0] < p[-1] or (p[0] == p[-1]):
                if ok(p):
                    first = min(i for i in range(len(edges)) if used >> i & 1)
                    cands[first].append((used, p))
            return
        for w in nb[p[-1]]:
            b = 1 << idx[edge(p[-1], w)]
            if not used & b:
                ext(p + (w,), used | b)

    for v in list(nb):
        ext((v,), 0)
    full = (1 << len(edges)) - 1
    # prefer simple paths: sort candidates
    for k in cands:
        cands[k].sort(key=lambda x: kind(x[1]) != "path")

    @cache
    def go(used):
        if used == full:
            return ()
        first = min(i for i in range(len(edges)) if not used >> i & 1)
        for m, p in cands[first]:
            if m & used:
                continue
            rest = go(used | m)
            if rest is not None:
                return (p,) + rest
        return None

    return go(0)


def bad_pairs(adj, mate):
    """All M-triangles (as frozensets) that share an edge with an M-square
    (triangle-square conflicts of 04d; not FGK's "bad pairs")."""
    n = len(adj)
    out = set()
    for u in range(n):
        v = mate[u]
        if u > v:
            continue
        for w in adj[u] & adj[v]:
            tri = (u, v, w)
            tedges = [edge(u, v), edge(v, w), edge(u, w)]
            hit = False
            for x, y in tedges:
                for w2 in adj[y] - {x}:
                    for q in (adj[w2] & adj[x]) - {x, y, w2}:
                        cyc = [edge(x, y), edge(y, w2), edge(w2, q), edge(q, x)]
                        if sum(mate[a] == b for a, b in cyc) == 1:
                            hit = True
            if hit:
                out.add(frozenset(tri))
    return out


def triangle_ok(adj, mate, p, bad):
    """Classify a defective trail by nearby triangle-square conflicts."""
    vs = set(p)
    if any(t & vs for t in bad):
        return ["near triangle-square conflict"]
    return ["no triangle-square conflict nearby"]


def verify(adj, mate, out):
    n = len(adj)
    allE = Counter(edge(u, v) for u in range(n) for v in adj[u] if u < v)
    used = Counter(e for _, p in out for e in path_edges(p))
    assert used == allE, "not an edge partition"
    ends = Counter(v for _, p in out for v in (p[0], p[-1]))
    assert all(ends[v] == 1 for v in range(n))
    kinds = Counter()
    for tag, p in out:
        k = kind(p)
        assert k in ("path", "triangle"), (tag, p, k)
        kinds[k] += 1
    return kinds


# ---------------------------------------------------------------------------
# exact finite lemmas used in 04d


def local_m_triangle_on_square(trails):
    """Local edges contain an M-triangle sharing an edge with one of the squares.

    In a triple (a_i,b_i,c_i,d_i,e_i,b_i) the only known matching edges are c_i d_i.
    """
    es = {e for t in trails for e in path_edges(t)}
    adj = defaultdict(set)
    for u, v in es:
        adj[u].add(v)
        adj[v].add(u)
    squares = [set(path_edges(t[1:])) for t in trails]
    for t in trails:
        c, d = t[2], t[3]
        for w in adj[c] & adj[d]:
            tri = {edge(c, d), edge(c, w), edge(d, w)}
            if any(tri & sq for sq in squares):
                return True
    return False


def local_diamond(trails):
    es = {e for t in trails for e in path_edges(t)}
    adj = defaultdict(set)
    for u, v in es:
        adj[u].add(v)
        adj[v].add(u)
    return any(len(adj[u] & adj[v]) >= 2 for u, v in es)


def verify_odd_triples():
    """Lemma 4 of 04d: triples of an odd type-2 cycle under each hypothesis.

    Label scheme of 04-regular-path-decomposition.md: b=(0,1,2), c=(3,4,5),
    e_i=c_{i-1}; d_1 is fresh, d_0 may be b_2 and d_2 may be b_0 in an open block;
    pendants A_i avoid all b-labels and their own c_i,e_i; a changed pendant avoids
    every c/e label and an unchanged one differs from its own d_i.
    Each case must have a cover by three simple paths unless its local edges violate
    the hypothesis, or the block is open and d_1 is A_0 or A_2.
    """
    b, c = (0, 1, 2), (3, 4, 5)
    result = {}
    for name, violates in (("no M-triangle on an M-square", local_m_triangle_on_square),
                           ("diamond-free", local_diamond)):
        counts = Counter()
        for closed in (True, False):
            e = (c[2] if closed else 6, c[0], c[1])
            corners = set(c + e)
            for first, last in product((7,) if closed else (7, b[2]), (9,) if closed else (9, b[0])):
                d = (first, 8, last)
                terminals = (corners | set(d)) - set(b)
                options = [sorted((terminals - {c[i], e[i]}) | {10 + i}) for i in range(3)]
                for a in product(*options):
                    if len(set(a)) != 3:
                        continue
                    trails = [(a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                    if len({x for t in trails for x in path_edges(t)}) != 15:
                        continue
                    for changed in product((False, True), repeat=3):
                        if any(a[i] in corners if changed[i] else a[i] == d[i] for i in range(3)):
                            continue
                        if violates(trails):
                            counts["excluded by hypothesis"] += 1
                            continue
                        sol = solve_cluster(trails, require_simple=True)
                        if sol is not None:
                            assert Counter(x for q in sol for x in path_edges(q)) == \
                                Counter(x for t in trails for x in path_edges(t))
                            counts[("closed" if closed else "open", "simple cover")] += 1
                        else:
                            assert not closed and d[1] in (a[0], a[2]), (trails, changed)
                            counts[("open", "no cover, d1 in {A0,A2}")] += 1
        result[name] = counts
        print("odd-cycle triples,", name, dict(counts))
    return result


def verify_pair_and_rotations():
    """Symbolic check that the pair and rotation replacements re-partition the edges."""
    for L in (3, 5, 7, 9):
        A = [("A", i) for i in range(L)]
        B = [("b", i) for i in range(L)]
        C = [("c", i) for i in range(L)]
        D = [("d", i) for i in range(L)]
        E = [C[(i - 1) % L] for i in range(L)]
        old = [e for i in range(L) for e in path_edges((A[i], B[i], C[i], D[i], E[i], B[i]))]
        for sign in (+1, -1):
            if sign == +1:   # A_i = d_{i+1}
                new = [(D[(i + 1) % L], B[i], C[(i - 1) % L], D[(i - 1) % L],
                        C[(i - 2) % L], B[(i - 2) % L]) for i in range(L)]
                ren = {A[i]: D[(i + 1) % L] for i in range(L)}
            else:            # A_i = d_{i-1}
                new = [(D[(i - 1) % L], B[i], C[i], D[(i + 1) % L], C[(i + 1) % L],
                        B[(i + 2) % L]) for i in range(L)]
                ren = {A[i]: D[(i - 1) % L] for i in range(L)}
            oldr = Counter(edge(ren.get(u, u), ren.get(v, v)) for u, v in old)
            assert Counter(e for q in new for e in path_edges(q)) == oldr
            assert all(len(set(q)) == 6 for q in new)
        for i in range(L - 1):
            j = i + 1
            pair = [(A[i], B[i], E[i], D[i], C[i], B[j]), (A[j], B[j], C[j], D[j], C[i], B[i])]
            two = Counter(e for k in (i, j) for e in path_edges((A[k], B[k], C[k], D[k], E[k], B[k])))
            assert Counter(e for q in pair for e in path_edges(q)) == two
    print("pair replacement and both uniform rotations re-partition the cycle edges")


def g_rule(pieces):
    """Post-sweep rule for good-target triangle trails (b,c,f,b,h,Y); see 04d."""
    pieces = list(pieces)
    while True:
        bad = [i for i, q in enumerate(pieces) if kind(q) != "path"]
        if not bad:
            return pieces, "fixed"
        i = bad[0]
        q = pieces[i] if pieces[i][0] == pieces[i][3] else pieces[i][::-1]
        if q[0] != q[3] or q[2] == q[5]:
            return pieces, "not a single-end triangle"
        b, c, f, _, h, Y = q
        cand = [(j, ww) for j, w in enumerate(pieces) if j != i
                for ww in (w, w[::-1]) if ww[1] == f]
        if len(cand) != 1:
            return pieces, "f not at a position adjacent to a terminal"
        j, w = cand[0]
        newq, neww = (w[0], f, c, b, h, Y), (b,) + w[1:]
        if kind(newq) != "path" or kind(neww) != "path":
            return pieces, "rule creates a repetition"
        pieces[i], pieces[j] = newq, neww


def diamond_free_graph(n, rng, ptri=0.6):
    def creates_diamond(adj, u, v):
        common = adj[u] & adj[v]
        if len(common) >= 2:
            return True
        return any(adj[u] & adj[w] or adj[v] & adj[w] for w in common)

    for _ in range(500):
        adj = [set() for _ in range(n)]
        stuck = 0
        while stuck <= 50:
            low = [v for v in range(n) if len(adj[v]) < 5]
            if not low:
                break
            u = rng.choice(low)
            cand = [v for v in low if v != u and v not in adj[u]]
            two = [v for v in cand if adj[u] & adj[v]]
            pool = two if two and rng.random() < ptri else cand
            rng.shuffle(pool)
            for v in pool[:20]:
                if not creates_diamond(adj, u, v):
                    adj[u].add(v)
                    adj[v].add(u)
                    break
            else:
                stuck += 1
        if all(len(a) == 5 for a in adj):
            # perfect matching preferring triangle edges (many M-triangles)
            tri = {edge(u, v) for u in range(n) for v in adj[u] if adj[u] & adj[v]}
            mate = {}

            def go(free):
                if not free:
                    return True
                u = min(free, key=lambda x: (len(adj[x] & free), rng.random()))
                for v in sorted((v for v in adj[u] if v in free),
                                key=lambda v: (edge(u, v) not in tri, rng.random())):
                    mate[u], mate[v] = v, u
                    if go(free - {u, v}):
                        return True
                    del mate[u], mate[v]
                return False

            if go(frozenset(range(n))):
                return adj, mate
    return None


def main():
    ap = ArgumentParser()
    ap.add_argument("--trials", type=int, default=300)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--orders", type=int, nargs="*", default=[16, 20, 30, 60])
    ap.add_argument("--small-runs", type=int, default=1500,
                    help="small dense graphs x 20 constructions, to exercise odd type-2 cycles")
    ap.add_argument("--diamond-free", type=int, default=0,
                    help="number of random diamond-free graphs per order (slow)")
    args = ap.parse_args()
    verify_pair_and_rotations()
    verify_odd_triples()
    rng = Random(args.seed)
    totals = Counter()
    tri_reasons = Counter()

    def run(adj, mate, style):
        r, s, trails = canonical(adj, mate, rng)
        out, ndef, nodd = sweep(adj, mate, r, s, trails)
        kinds = verify(adj, mate, out)
        bad = bad_pairs(adj, mate)
        totals[(style, "runs")] += 1
        totals[(style, "square defects")] += ndef
        totals[(style, "odd type-2 cycles")] += nodd
        totals[(style, "remaining triangle trails")] += kinds["triangle"]
        totals[(style, "runs satisfying Theorem A hypothesis")] += not bad
        if not bad:
            assert kinds["triangle"] == 0
        for tag, p in out:
            if kind(p) == "triangle":
                for reason in triangle_ok(adj, mate, p, bad):
                    tri_reasons[(tag, reason)] += 1
        return out

    for style in ("random", "square", "dense", "k5", "far3"):
        for n in args.orders:
            if style == "k5" and n % 10:
                continue
            for _ in range(args.trials // len(args.orders)):
                adj, mate = random_matched_graph(n, rng, style)
                run(adj, mate, style)
    for _ in range(args.small_runs):
        n = rng.choice([10, 12, 14, 16])
        adj, mate = random_matched_graph(n, rng, rng.choice(["random", "square", "dense"]))
        for _ in range(20):
            run(adj, mate, "small")
    for n in (20, 30, 40, 60) if args.diamond_free else ():
        for _ in range(args.diamond_free):
            g = diamond_free_graph(n, rng)
            if g is None:
                totals[("diamond-free", "generation failures")] += 1
                continue
            adj, mate = g
            out = run(adj, mate, "diamond-free")
            tags = Counter(tag for tag, p in out if kind(p) != "path")
            assert set(tags) <= {"good"}, tags
            pieces, status = g_rule([p for _, p in out])
            totals[("diamond-free", "G-rule " + status)] += 1
            if status == "fixed":
                verify(adj, mate, [("x", p) for p in pieces])
    for k in sorted(totals):
        print(k, totals[k])
    for k in sorted(tri_reasons):
        print("triangle trail", k, tri_reasons[k])
    assert all(reason == "near triangle-square conflict" for _, reason in tri_reasons)


if __name__ == "__main__":
    main()
