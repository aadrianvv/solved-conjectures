"""Independent referee checker for Theorem A of 04d-regular-path-matching-relative-theorem.md.

Written from the text of 04d (Lemma 1, the sweep, Lemma 3, Section 3, Lemma 4) only.
It does not import or copy check_regular_path_sweep_pipeline.py.

Parts
  1. lemma4      -- own enumeration of the triple configurations allowed by (o1)-(o5),
                    own exact cover by three simple five-edge paths.
  2. graphs      -- random simple 5-regular graphs G with a perfect matching M chosen by
                    local search so that M has no bad pair (M-triangle sharing an edge with
                    an M-square).  Several triangle-rich families.  Runs the Lemma 1
                    construction (own implementation) many times per graph, then the sweep.
  3. perms       -- generic data (M, r, s) satisfying only (P1)-(P3), which is all that the
                    sweep and Section 3 use.  Odd type-2 cycles of lengths 3..9 are planted,
                    with planted type-1 pendant changes and planted rotation patterns
                    A_i = d_{i+1} or A_i = d_{i-1}.  Graph = M u R u S (automatically 5-regular).
Every output is checked to be an exact partition of E(G) into simple paths with five edges
whenever the hypothesis holds.  Random runs are evidence, not proof.

Usage: python check_regular_path_theoremA_independent.py [--quick] [--seed N]
"""

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import product
from random import Random


def E(u, v):
    return (u, v) if u < v else (v, u)


def edges_of(seq):
    return [E(seq[i], seq[i + 1]) for i in range(len(seq) - 1)]


# ----------------------------------------------------------------------------------------
# simple five-edge path exact cover of a small edge set (used for Lemma 4 and Section 3)

def simple_paths5(edge_list):
    nb = defaultdict(list)
    for u, v in edge_list:
        nb[u].append(v)
        nb[v].append(u)
    out = set()

    def dfs(p):
        if len(p) == 6:
            q = tuple(p) if p[0] < p[-1] else tuple(reversed(p))
            out.add(q)
            return
        for w in nb[p[-1]]:
            if w not in p:
                p.append(w)
                dfs(p)
                p.pop()

    for v in list(nb):
        dfs([v])
    return out


def path_cover(edge_list, k):
    """Partition edge_list (distinct edges) into k simple five-edge paths, or None."""
    es = sorted(set(edge_list))
    assert len(es) == len(edge_list) == 5 * k
    idx = {e: i for i, e in enumerate(es)}
    by_min = defaultdict(list)
    for p in simple_paths5(es):
        mask = 0
        for e in edges_of(p):
            mask |= 1 << idx[e]
        low = (mask & -mask).bit_length() - 1
        by_min[low].append((mask, p))
    full = (1 << len(es)) - 1

    def go(used):
        if used == full:
            return []
        free = ~used & full
        low = (free & -free).bit_length() - 1
        for mask, p in by_min[low]:
            if mask & used == 0:
                rest = go(used | mask)
                if rest is not None:
                    return [p] + rest
        return None

    return go(0)


# ----------------------------------------------------------------------------------------
# Part 1: Lemma 4, own enumeration

def lemma4_enumeration():
    """Enumerate triples (T0,T1,T2) of an odd type-2 cycle as allowed by (o1)-(o5).

    Labels: b_i, c_i, d_i distinct symbols, e_1=c_0, e_2=c_1, e_0=c_2 (closed, L=3) or a
    fresh symbol c_{-1} (open block, L>=5).  Open blocks also allow d_0=b_2 and/or d_2=b_0.
    Pendant A_i: a fresh symbol, or any present non-b label other than c_i, e_i; distinct.
    A changed pendant avoids every c/e label; an unchanged pendant differs from d_i.
    Excluded: fewer than 15 distinct edges; local M-triangle through some c_i d_i sharing an
    edge with one of the three squares (b_j,c_j,d_j,e_j).
    """
    res = Counter()
    failures = []
    for closed in (True, False):
        for d0b2, d2b0 in ([(False, False)] if closed else list(product((False, True), repeat=2))):
            b = ["b0", "b1", "b2"]
            c = ["c0", "c1", "c2"]
            e = ["c2" if closed else "cm1", "c0", "c1"]
            d = ["b2" if d0b2 else "d0", "d1", "b0" if d2b0 else "d2"]
            ce = set(c) | set(e)
            present = (set(c) | set(e) | set(d)) - set(b)
            opts = [sorted(present - {c[i], e[i]}) + ["A%d" % i] for i in range(3)]
            for A in product(*opts):
                if len(set(A)) < 3:
                    continue
                trails = [(A[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                el = [x for t in trails for x in edges_of(t)]
                if len(set(el)) != 15:
                    continue
                adj = defaultdict(set)
                for u, v in el:
                    adj[u].add(v)
                    adj[v].add(u)
                squares = [set(edges_of((b[j], c[j], d[j], e[j], b[j]))) for j in range(3)]
                viol = False
                for i in range(3):
                    for w in adj[c[i]] & adj[d[i]]:
                        tri = {E(c[i], d[i]), E(c[i], w), E(d[i], w)}
                        if any(tri & sq for sq in squares):
                            viol = True
                for changed in product((False, True), repeat=3):
                    if any((A[i] in ce) if changed[i] else (A[i] == d[i]) for i in range(3)):
                        continue
                    if viol:
                        res["excluded"] += 1
                        continue
                    cov = path_cover(el, 3)
                    kind = "closed" if closed else "open"
                    if cov is not None:
                        assert sorted(x for p in cov for x in edges_of(p)) == sorted(el)
                        assert all(len(set(p)) == 6 for p in cov)
                        res[(kind, "cover")] += 1
                    else:
                        res[(kind, "no cover")] += 1
                        ok = (not closed) and d[1] in (A[0], A[2])
                        res[(kind, "no cover, d1 in {A0,A2}" if ok else "no cover, OTHER")] += 1
                        res[(kind, "no cover, d1 == A0" if d[1] == A[0] else "no cover, d1 != A0")] += 1
                        if not ok:
                            failures.append((trails, changed))
    return res, failures


# ----------------------------------------------------------------------------------------
# hypothesis: bad pairs

def bad_pairs(adj, mate):
    """Return list of (M-triangle, edge) with the edge lying on an M-square."""
    out = []

    def on_msquare(x, y):
        for p in adj[y]:
            if p == x:
                continue
            for q in adj[p] & adj[x]:
                if q in (x, y) or q == p:
                    continue
                cyc = [(x, y), (y, p), (p, q), (q, x)]
                if sum(1 for a, bb in cyc if mate[a] == bb) == 1:
                    return True
        return False

    seen = set()
    for u in adj:
        v = mate[u]
        if u > v:
            continue
        for w in adj[u] & adj[v]:
            for x, y in ((u, v), (u, w), (v, w)):
                if on_msquare(x, y):
                    t = frozenset((u, v, w))
                    if (t, E(x, y)) not in seen:
                        seen.add((t, E(x, y)))
                        out.append((t, E(x, y)))
    return out


def m_triangle_count(adj, mate):
    return sum(len(adj[u] & adj[mate[u]]) for u in adj if u < mate[u])


def m_square_count(adj, mate):
    cnt = 0
    for u in adj:
        v = mate[u]
        if u > v:
            continue
        for p in adj[v] - {u}:
            if mate[v] == p:
                continue
            for q in adj[p] & adj[u]:
                if q in (u, v) or mate[p] == q or mate[q] == u:
                    continue
                cnt += 1
    return cnt


# ----------------------------------------------------------------------------------------
# Lemma 1 construction (own implementation)

def lemma1(adj, mate, rng):
    n = len(adj)
    H = {v: [w for w in adj[v] if w != mate[v]] for v in adj}
    pair_id = {}
    for w in adj:
        nb = H[w][:]
        forced = []
        used = set()
        for x in nb:
            y = mate[x]
            if y in nb and x not in used and y not in used:
                forced.append((x, y))
                used |= {x, y}
        rest = [x for x in nb if x not in used]
        rng.shuffle(rest)
        pairs = forced + [(rest[i], rest[i + 1]) for i in range(0, len(rest), 2)]
        assert sorted(x for p in pairs for x in p) == sorted(nb)
        for k, (x, y) in enumerate(pairs):
            pair_id[(w, x)] = k
            pair_id[(w, y)] = k
    # split graph nodes (w,k); each has two incident H-edges; orient each cycle
    inc = defaultdict(list)
    for w in adj:
        for x in H[w]:
            inc[(w, pair_id[(w, x)])].append(x)
    arcs = []
    done = set()
    for start in list(inc):
        if start in done:
            continue
        # walk: at node (w,k), leave through one of its two edges
        node = start
        x_out = inc[start][rng.randrange(2)]
        while True:
            done.add(node)
            w = node[0]
            arcs.append((w, x_out))
            nxt = (x_out, pair_id[(x_out, w)])
            if nxt == start:
                break
            a, bb = inc[nxt]
            x_out = bb if a == w else a
            if a == bb:
                raise AssertionError("multi-edge")
            node = nxt
    assert len(arcs) == 2 * n and len(set(arcs)) == 2 * n
    outs = defaultdict(list)
    ins = defaultdict(list)
    for u, v in arcs:
        outs[u].append(v)
        ins[v].append(u)
    for w in adj:
        assert len(outs[w]) == 2 and len(ins[w]) == 2
        # prescribed pairs oppositely directed
        for x in H[w]:
            y = mate[x]
            if y in H[w]:
                assert (x in outs[w]) != (y in outs[w])
    # 2-factorise the bipartite out/in multigraph (2-regular): alternate along its cycles
    col = {}
    for a0 in arcs:
        if a0 in col:
            continue
        c = rng.randrange(2)
        cur, side = a0, 0
        while cur not in col:
            col[cur] = c
            u, v = cur
            if side == 0:   # through head's in-copy
                o = ins[v][0] if ins[v][1] == u else ins[v][1]
                cur = (o, v)
            else:           # through tail's out-copy
                o = outs[u][0] if outs[u][1] == v else outs[u][1]
                cur = (u, o)
            side ^= 1
            c ^= 1
    r, s = {}, {}
    for (u, v), c in col.items():
        if c == 0:
            assert u not in r
            r[u] = v
        else:
            assert v not in s
            s[v] = u      # s(w) = tail of the P2 arc entering w
    assert len(r) == n and len(s) == n
    return r, s


def check_P(adj, mate, r, s):
    n = len(adj)
    assert sorted(r.values()) == sorted(adj) and sorted(s.values()) == sorted(adj)
    R = {E(v, r[v]) for v in adj}
    S = {E(v, s[v]) for v in adj}
    Mset = {E(v, mate[v]) for v in adj}
    allE = {E(u, v) for u in adj for v in adj[u]}
    assert len(R) == n and len(S) == n and not (R & S) and not (R & Mset) and not (S & Mset)
    assert R | S | Mset == allE
    for v in adj:
        assert r[v] != v and s[v] != v
        assert r[r[v]] != v and s[s[v]] != v           # (P2)
        assert s[r[v]] != mate[v]                      # (P3)


# ----------------------------------------------------------------------------------------
# the sweep and Section 3 (own implementation from the text)

class SweepFailure(Exception):
    pass


def sweep(adj, mate, r, s, rng, stats, hyp):
    rinv = {v: u for u, v in r.items()}
    trails = {}
    owner = {}
    for u in adj:
        v = mate[u]
        if u < v:
            t = (s[r[u]], r[u], u, v, r[v], s[r[v]])
            trails[(u, v)] = t
            owner[u] = owner[v] = (u, v)
    # Lemma 2
    ends = Counter(x for t in trails.values() for x in (t[0], t[-1]))
    assert all(ends[v] == 1 for v in adj)
    defect = {}
    for k, t in trails.items():
        x1, x2 = t[1] == t[5], t[0] == t[4]
        assert not (x1 and x2)
        rest_dup = len(set(t)) < 6 and not (x1 or x2)
        assert not rest_dup, ("Lemma 2 violated", t)
        if x1 or x2:
            o = t if x1 else tuple(reversed(t))
            a, b, c, d, e, b2 = o
            assert b == b2 and len({a, b, c, d, e}) == 5
            assert b == r[c] and e == r[d] and a == s[b] and s[e] == b and mate[c] == d
            defect[k] = o
    stats["defects"] += len(defect)
    # links
    target, ltype = {}, {}
    for k, (a, b, c, d, e, _) in defect.items():
        f = rinv[c]
        tk = owner[f]
        assert tk != k
        target[k] = tk
        if tk in defect:
            bb, ee = defect[tk][1], defect[tk][4]
            assert c in (bb, ee)
            ltype[k] = 1 if c == bb else 2
        else:
            ltype[k] = 0
    succ = {k: target[k] for k in defect if ltype[k] == 2}
    pred = {}
    for k, t in succ.items():
        assert t not in pred, "two incoming type-2 links"
        pred[t] = k
    sources, oddcyc = set(), []
    seen = set()
    for k in defect:
        if k in seen:
            continue
        x = k
        walk = {x}
        while x in pred and pred[x] not in walk:
            x = pred[x]
            walk.add(x)
        if x in pred:  # on a cycle
            cyc = [x]
            y = succ[x]
            while y != x:
                cyc.append(y)
                y = succ[y]
            seen.update(cyc)
            if len(cyc) % 2 == 0:
                off = rng.randrange(2)
                sources.update(cyc[off::2])
            else:
                oddcyc.append(cyc)
        else:
            ch = [x]
            while ch[-1] in succ:
                ch.append(succ[ch[-1]])
            seen.update(ch)
            sources.update(ch[0::2])
    inodd = {k for cy in oddcyc for k in cy}
    for k in defect:
        if k not in sources and k not in inodd:
            assert k in pred and pred[k] in sources
    for k in sources:
        assert not (k in pred and pred[k] in sources)
    stats["odd cycles"] += len(oddcyc)
    for cy in oddcyc:
        stats["odd cycle length %d" % len(cy)] += 1
    # trades
    A = {k: defect[k][0] for k in defect}
    good_recv = defaultdict(dict)
    closing_taken = set()
    for k in sources:
        a, b, c, d, e, _ = defect[k]
        tk = target[k]
        if ltype[k] == 0:
            good_recv[tk][c] = b
        elif ltype[k] == 1:
            assert defect[tk][0] == s[c]
            A[tk] = r[defect[tk][1]]
            assert A[tk] == b
            stats["type-1 trades"] += 1
        else:
            assert defect[tk][1] == s[c] and r[defect[tk][4]] == b
            closing_taken.add(tk)
    pieces = []
    for k, t in trails.items():
        if k in defect:
            a, b, c, d, e, _ = defect[k]
            if k in sources:
                pieces.append(("source", (A[k], b, e, d, c, s[c])))
            elif k in inodd:
                continue
            else:
                assert k in closing_taken
                pieces.append(("recipient", (A[k], b, c, d, e, r[e])))
        else:
            p = list(t)
            for c, b in good_recv.get(k, {}).items():
                if p[1] == c:
                    assert p[0] == s[c]
                    p[0] = b
                else:
                    assert p[4] == c and p[5] == s[c]
                    p[5] = b
            pieces.append(("good" if k in good_recv else "plain", tuple(p)))
    # Section 3
    for cy in oddcyc:
        L = len(cy)
        lab = [(A[k],) + defect[k][1:5] for k in cy]   # (A,b,c,d,e)
        for i in range(L):
            assert lab[i][2] == lab[(i + 1) % L][4], "c_i != e_{i+1}"
        Ai = [x[0] for x in lab]
        bi = [x[1] for x in lab]
        ci = [x[2] for x in lab]
        di = [x[3] for x in lab]
        ei = [x[4] for x in lab]
        # (o1)-(o5) as checked facts on this instance
        assert len(set(bi)) == L and len(set(ci + di)) == 2 * L and len(set(Ai)) == L
        assert not set(bi) & set(ci)
        for i in range(L):
            assert di[i] not in (bi[i - 1], bi[i], bi[(i + 1) % L])
            assert Ai[i] not in bi and Ai[i] not in (ci[i], ei[i])

        def tri(i):
            i %= L
            return (Ai[i], bi[i], ci[i], di[i], ei[i], bi[i])

        def block_cover(k):
            el = [x for j in range(k, k + 3) for x in edges_of(tri(j))]
            return path_cover(el, 3)

        def pair(i):
            j = (i + 1) % L
            i %= L
            return [(Ai[i], bi[i], ei[i], di[i], ci[i], bi[j]),
                    (Ai[j], bi[j], ci[j], di[j], ci[i], bi[i])]

        covers = {k: block_cover(k) for k in (range(L) if L > 3 else [0])}
        # realized Lemma 4 check
        for k, cov in covers.items():
            if cov is None:
                if L == 3:
                    stats["Lemma4 realized: closed block without cover"] += 1
                    if hyp:
                        raise SweepFailure("closed odd cycle without cover under hypothesis")
                else:
                    mid = (k + 1) % L
                    if di[mid] in (Ai[k % L], Ai[(k + 2) % L]):
                        stats["Lemma4 realized: open block failing with d1 in {A0,A2}"] += 1
                    else:
                        stats["Lemma4 realized: open block failing OTHER"] += 1
                        if hyp:
                            raise SweepFailure("open block fails outside the exception")
            else:
                stats["Lemma4 realized: block with cover"] += 1
        # extra: if a uniform rotation pattern holds, verify the rotation pieces regardless
        for sign in (+1, -1):
            if L >= 3 and all(Ai[i] == di[(i + sign) % L] for i in range(L)):
                if sign == 1:
                    rot = [(Ai[i], bi[i], ci[(i - 1) % L], di[(i - 1) % L], ci[(i - 2) % L], bi[(i - 2) % L])
                           for i in range(L)]
                else:
                    rot = [(Ai[i], bi[i], ci[i], di[(i + 1) % L], ci[(i + 1) % L], bi[(i + 2) % L])
                           for i in range(L)]
                oldE = sorted(x for i in range(L) for x in edges_of(tri(i)))
                assert sorted(x for p in rot for x in edges_of(p)) == oldE
                assert all(len(set(p)) == 6 for p in rot), ("rotation not simple", rot)
                stats["uniform rotation pattern present (rotation verified)"] += 1
        good_blocks = [k for k, cov in covers.items() if cov is not None]
        if good_blocks:
            k = rng.choice(good_blocks)
            for p in covers[k]:
                pieces.append(("odd-triple", p))
            for t in range(3, L, 2):
                for p in pair(k + t):
                    pieces.append(("odd-pair", p))
        else:
            if L == 3:
                raise SweepFailure("no cover for closed triple")
            sgn = None
            for sign in (+1, -1):
                if all(Ai[i] == di[(i + sign) % L] for i in range(L)):
                    sgn = sign
            if sgn is None:
                raise SweepFailure("all blocks fail but no uniform rotation")
            stats["rotation used"] += 1
            if sgn == 1:
                rot = [(Ai[i], bi[i], ci[(i - 1) % L], di[(i - 1) % L], ci[(i - 2) % L], bi[(i - 2) % L])
                       for i in range(L)]
            else:
                rot = [(Ai[i], bi[i], ci[i], di[(i + 1) % L], ci[(i + 1) % L], bi[(i + 2) % L])
                       for i in range(L)]
            for p in rot:
                pieces.append(("rotation", p))
    return pieces


def verify_decomposition(adj, pieces):
    allE = Counter(E(u, v) for u in adj for v in adj[u] if u < v)
    used = Counter()
    nonsimple = []
    for tag, p in pieces:
        assert len(p) == 6
        for u, v in zip(p, p[1:]):
            assert v in adj[u], ("non-edge", tag, p)
        used.update(edges_of(p))
        if len(set(p)) != 6:
            nonsimple.append((tag, p))
    assert used == allE, "not an exact edge partition"
    return nonsimple


# ----------------------------------------------------------------------------------------
# Part 2: graph families with a hypothesis-satisfying matching

def switch(adj, rng, times):
    es = [E(u, v) for u in adj for v in adj[u] if u < v]
    for _ in range(times):
        (a, b), (c, d) = rng.sample(es, 2)
        if len({a, b, c, d}) < 4:
            continue
        if rng.random() < 0.5:
            c, d = d, c
        if c in adj[a] or d in adj[b]:
            continue
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        es.remove(E(a, b)); es.remove(E(c, d)); es += [E(a, c), E(b, d)]


def four_regular(n, rng, fam):
    adj = {v: set() for v in range(n)}

    def add(u, v):
        adj[u].add(v); adj[v].add(u)

    if fam == "cycle-square":
        for u in range(n):
            add(u, (u + 1) % n); add(u, (u + 2) % n)
        switch(adj, rng, rng.randrange(0, n // 6 + 1))
    elif fam == "circulant":
        while True:
            j = rng.randrange(3, n // 2)
            if j != n // 2:
                break
        for u in range(n):
            add(u, (u + 1) % n); add(u, (u + j) % n)
        switch(adj, rng, rng.randrange(0, n // 8 + 1))
    elif fam == "octahedra":
        assert n % 6 == 0
        for base in range(0, n, 6):
            for i in range(6):
                for j in range(i + 1, 6):
                    if j != i + 3:
                        add(base + i, base + j)
        switch(adj, rng, rng.randrange(1, n // 6 + 2))
    elif fam == "k5":
        assert n % 5 == 0
        for base in range(0, n, 5):
            for i in range(5):
                for j in range(i + 1, 5):
                    add(base + i, base + j)
        switch(adj, rng, rng.randrange(1, n // 5 + 2))
    elif fam == "line-cubic":
        # line graph of a random cubic multigraph-free graph on 2n/3 vertices: n edges
        m = 2 * n // 3
        while True:
            stubs = [v for v in range(m) for _ in range(3)]
            rng.shuffle(stubs)
            es = [E(stubs[2 * i], stubs[2 * i + 1]) for i in range(len(stubs) // 2)]
            if all(a != b for a, b in es) and len(set(es)) == len(es):
                break
        inc = defaultdict(list)
        for i, (a, b) in enumerate(es):
            inc[a].append(i); inc[b].append(i)
        for v in range(m):
            x, y, z = inc[v]
            add(x, y); add(y, z); add(x, z)
        switch(adj, rng, rng.randrange(0, n // 10 + 1))
    elif fam == "random":
        for _ in range(2):
            perm = list(range(n))
            rng.shuffle(perm)
            for i in range(n):
                add(perm[i], perm[(i + 1) % n])
        if any(len(adj[v]) != 4 for v in adj):
            return None
    else:
        raise ValueError(fam)
    if any(len(adj[v]) != 4 for v in adj):
        return None
    return adj


def random_pm(adj, rng, avoid=None):
    """Random perfect matching of the graph adj (avoid: optional set of forbidden pairs)."""
    def go(free, mate):
        if not free:
            return True
        u = min(free, key=lambda x: (sum(1 for y in adj[x] if y in free), rng.random()))
        cand = [y for y in adj[u] if y in free]
        rng.shuffle(cand)
        for y in cand[:4]:
            mate[u], mate[y] = y, u
            if go(free - {u, y}, mate):
                return True
            del mate[u], mate[y]
        return False

    mate = {}
    if go(frozenset(adj), mate):
        return mate
    return None


def matching_local_search(adj, mate, rng, steps, want_tri):
    """Alternating 4-cycle moves minimizing bad pairs (and optionally favouring M-triangles)."""
    def score(m):
        return len(bad_pairs(adj, m)) * 100 - (m_triangle_count(adj, m) if want_tri else 0)

    cur = dict(mate)
    sc = score(cur)
    best, bsc = None, None
    for _ in range(steps):
        if sc < 100 and (bsc is None or sc < bsc):
            best, bsc = dict(cur), sc
            if not want_tri:
                break
        u = rng.choice(list(adj))
        v = cur[u]
        x = rng.choice([w for w in adj[u] if w != v])
        y = cur[x]
        if y == u or y not in adj[v] or y == v:
            continue
        new = dict(cur)
        new[u], new[x], new[v], new[y] = x, u, y, v
        ns = score(new)
        if ns <= sc or rng.random() < 0.02:
            cur, sc = new, ns
    if best is None and sc < 100:
        best = cur
    return best if best is not None else cur


def graph_instance(n, rng, fam):
    """Return (adj5, mate) with no bad pair, or None."""
    for _ in range(30):
        H = four_regular(n, rng, fam)
        if H is None:
            continue
        # matching among non-H pairs
        comp = {v: {w for w in H if w != v and w not in H[v]} for v in H}
        mode = rng.random()
        if mode < 0.35:
            # far mode: matched ends without common H-neighbour (no M-triangle)
            comp = {v: {w for w in comp[v] if not (H[v] & H[w])} for v in comp}
        mate = random_pm(comp, rng)
        if mate is None:
            continue
        adj = {v: set(H[v]) | {mate[v]} for v in H}
        # now choose a perfect matching M of the 5-regular G by local search
        want_tri = mode >= 0.35
        best = matching_local_search(adj, mate, rng, 400, want_tri)
        if not bad_pairs(adj, best):
            return adj, best
        # try fresh matchings of G
        for _ in range(5):
            m2 = random_pm(adj, rng)
            if m2 is None:
                continue
            m2 = matching_local_search(adj, m2, rng, 400, want_tri)
            if not bad_pairs(adj, m2):
                return adj, m2
    return None


# ----------------------------------------------------------------------------------------
# Part 3: generic (M, r, s) with (P1)-(P3), planted odd type-2 cycles

def complete_perm(dom, cod, bad, rng, tries=4000):
    """Random bijection dom->cod avoiding bad(v, image)."""
    dom = list(dom)
    cod = list(cod)
    assert len(dom) == len(cod)
    rng.shuffle(cod)
    f = dict(zip(dom, cod))
    for _ in range(tries):
        viol = [v for v in dom if bad(v, f[v], f)]
        if not viol:
            return f
        v = rng.choice(viol)
        w = rng.choice(dom)
        f[v], f[w] = f[w], f[v]
    return None


def build_adj(V, mate, r, s):
    adj = {v: set() for v in V}
    for v in V:
        for w in (mate[v], r[v], s[v]):
            adj[v].add(w)
            adj[w].add(v)
    return adj


def valid_rsm(V, mate, r, s):
    adj = build_adj(V, mate, r, s)
    if any(len(adj[v]) != 5 for v in V):
        return None
    try:
        check_P(adj, mate, r, s)
    except AssertionError:
        return None
    return adj


def repair_bad_pairs(V, mate, r, s, free_r, free_s, rng, iters=800):
    """Swap non-planted r/s values to remove bad pairs (keeps (P1)-(P3) and the planting)."""
    adj = valid_rsm(V, mate, r, s)
    if adj is None:
        return None
    bp = bad_pairs(adj, mate)
    free_r, free_s = list(free_r), list(free_s)
    for _ in range(iters):
        if not bp:
            return adj
        tri, _e = rng.choice(bp)
        near = set(tri) | {w for x in tri for w in adj[x]}
        perm, keys = (r, free_r) if rng.random() < 0.5 else (s, free_s)
        cand = [x for x in near if x in set(keys)]
        if not cand or len(keys) < 2:
            continue
        x = rng.choice(cand)
        y = rng.choice(keys)
        if x == y:
            continue
        perm[x], perm[y] = perm[y], perm[x]
        adj2 = valid_rsm(V, mate, r, s)
        bp2 = bad_pairs(adj2, mate) if adj2 is not None else None
        if bp2 is not None and (len(bp2) <= len(bp) or rng.random() < 0.03):
            adj, bp = adj2, bp2
        else:
            perm[x], perm[y] = perm[y], perm[x]
    return adj if not bp else None


def planted_rsm(n_extra, rng, L, pattern, repair=True):
    """Plant an odd type-2 cycle of length L and complete (M, r, s) at random.

    pattern: 'fresh' (pendants random), 'plus' (A_i = d_{i+1}), 'minus' (A_i = d_{i-1}),
             'changed' (type-1 sources planted into random cycle members),
             'changed-plus' (changed pendants with r(b_i) = d_{i+1} for all i).
    """
    vid = iter(range(10 ** 6))
    c = [next(vid) for _ in range(L)]
    d = [next(vid) for _ in range(L)]
    b = [next(vid) for _ in range(L)]
    mate, r, s = {}, {}, {}
    for i in range(L):
        mate[c[i]], mate[d[i]] = d[i], c[i]
        r[c[i]] = b[i]
        r[d[i]] = c[(i - 1) % L]       # e_i = c_{i-1}
        s[c[(i - 1) % L]] = b[i]        # s(e_i) = b_i
    if pattern == "plus":
        for i in range(L):
            s[b[i]] = d[(i + 1) % L]
    elif pattern == "minus":
        for i in range(L):
            s[b[i]] = d[(i - 1) % L]
    elif pattern in ("changed", "changed-plus", "changed-minus"):
        members = range(L) if pattern != "changed" else [i for i in range(L) if rng.random() < 0.6]
        for i in members:
            # external source T'' = (a'', b'', b_i, d'', e'', b'') with b'' = r(b_i)
            dd, ee = next(vid), next(vid)
            bb = {"changed-plus": d[(i + 1) % L], "changed-minus": d[(i - 1) % L]}.get(pattern)
            bb = next(vid) if bb is None else bb
            mate[b[i]], mate[dd] = dd, b[i]
            r[b[i]] = bb
            r[dd] = ee
            s[ee] = bb
    base = set(mate) | set(r) | set(r.values()) | set(s) | set(s.values())
    V = sorted(base)
    while len(V) < len(base) + n_extra or len(V) % 2:
        V.append(next(vid))
    # matching completion
    free = [v for v in V if v not in mate]
    rng.shuffle(free)
    for i in range(0, len(free), 2):
        mate[free[i]], mate[free[i + 1]] = free[i + 1], free[i]
    # r completion
    rdom = [v for v in V if v not in r]
    rcod = [v for v in V if v not in set(r.values())]

    def rbad(v, w, f):
        full = lambda x: r.get(x, f.get(x))
        return w == v or w == mate[v] or full(w) == v

    fr = complete_perm(rdom, rcod, rbad, rng)
    if fr is None:
        return None
    r.update(fr)
    rinv = {w: v for v, w in r.items()}
    sdom = [v for v in V if v not in s]
    scod = [v for v in V if v not in set(s.values())]

    def sbad(v, w, f):
        full = lambda x: s.get(x, f.get(x))
        return (w == v or w == mate[v] or r[v] == w or r[w] == v or full(w) == v
                or w == mate[rinv[v]])

    fs = complete_perm(sdom, scod, sbad, rng)
    if fs is None:
        return None
    s.update(fs)
    adj = valid_rsm(V, mate, r, s)
    if adj is None:
        return None
    if repair:
        adj = repair_bad_pairs(V, mate, r, s, fr.keys(), fs.keys(), rng)
        if adj is None:
            return None
    return adj, mate, r, s


def planted_rsm_none(n, rng, repair=False):
    V = list(range(n))
    rng.shuffle(V)
    mate = {}
    for i in range(0, n, 2):
        mate[V[i]], mate[V[i + 1]] = V[i + 1], V[i]
    r = complete_perm(range(n), range(n), lambda v, w, f: w == v or w == mate[v] or f[w] == v, rng)
    if r is None:
        return None
    rinv = {w: v for v, w in r.items()}
    s = complete_perm(range(n), range(n), lambda v, w, f: (w == v or w == mate[v] or r[v] == w or r[w] == v
                                                          or f[w] == v or w == mate[rinv[v]]), rng)
    if s is None:
        return None
    adj = valid_rsm(list(range(n)), mate, r, s)
    if adj is None:
        return None
    if repair:
        adj = repair_bad_pairs(list(range(n)), mate, r, s, list(range(n)), list(range(n)), rng)
        if adj is None:
            return None
    return adj, mate, r, s


# ----------------------------------------------------------------------------------------

def run_instance(adj, mate, r, s, rng, stats, tag):
    hyp = not bad_pairs(adj, mate)
    stats[(tag, "runs")] += 1
    stats[(tag, "hypothesis holds")] += hyp
    st = Counter()
    try:
        pieces = sweep(adj, mate, r, s, rng, st, hyp)
    except SweepFailure as ex:
        stats[(tag, "SWEEP FAILURE: " + str(ex))] += 1
        if hyp:
            raise
        return
    for k, v in st.items():
        stats[(tag, k)] += v
    ns = verify_decomposition(adj, pieces)
    if hyp:
        assert not ns, ("non-simple piece under the hypothesis", ns[:3])
        stats[(tag, "verified P5-decompositions (hypothesis)")] += 1
        stats[(tag, "M-triangles in hypothesis runs")] += m_triangle_count(adj, mate)
    else:
        stats[(tag, "non-simple pieces (hypothesis fails)")] += len(ns)


def main():
    ap = ArgumentParser()
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--quick", action="store_true")
    args = ap.parse_args()
    rng = Random(args.seed)
    q = args.quick

    print("== Part 1: own Lemma 4 enumeration ==")
    res, fails = lemma4_enumeration()
    for k in sorted(res, key=str):
        print("  ", k, res[k])
    assert not fails, fails[:3]
    assert res[("closed", "no cover")] == 0

    stats = Counter()
    print("== Part 2: graph families, own Lemma 1 construction + sweep ==")
    fams = [("cycle-square", (12, 18, 24, 36)), ("circulant", (14, 20, 30, 40)),
            ("octahedra", (12, 18, 24, 36)), ("k5", (10, 20, 30, 40)),
            ("line-cubic", (12, 18, 24, 30, 36)), ("random", (16, 24, 40, 60))]
    per = 4 if q else 12
    constructions = 5 if q else 10
    for fam, orders in fams:
        for n in orders:
            for _ in range(per):
                inst = graph_instance(n, rng, fam)
                if inst is None:
                    stats[(fam, "no hypothesis matching found")] += 1
                    continue
                adj, mate = inst
                stats[(fam, "graphs")] += 1
                stats[(fam, "graphs with M-triangles")] += m_triangle_count(adj, mate) > 0
                stats[(fam, "graphs with M-squares")] += m_square_count(adj, mate) > 0
                for _ in range(constructions):
                    r, s = lemma1(adj, mate, rng)
                    check_P(adj, mate, r, s)
                    run_instance(adj, mate, r, s, rng, stats, fam)
    print("== Part 3: generic (M,r,s) data with planted odd type-2 cycles ==")
    reps = 30 if q else 150
    for L in (3, 5, 7, 9):
        for pattern in ("fresh", "plus", "minus", "changed", "changed-plus", "changed-minus"):
            for _ in range(reps):
                inst = planted_rsm(rng.choice((10, 20, 40)), rng, L, pattern, repair=rng.random() < 0.8)
                if inst is None:
                    stats[("planted", "generation failures")] += 1
                    continue
                adj, mate, r, s = inst
                run_instance(adj, mate, r, s, rng, stats, "planted L=%d %s" % (L, pattern))
    for _ in range(300 if q else 2000):
        inst = planted_rsm_none(rng.choice((10, 12, 14, 16, 20, 30)), rng, repair=rng.random() < 0.7)
        if inst is None:
            continue
        adj, mate, r, s = inst
        run_instance(adj, mate, r, s, rng, stats, "generic small")
    for k in sorted(stats, key=str):
        print("  ", k, stats[k])
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
