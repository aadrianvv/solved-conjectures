"""Counterexample to Conjecture P5* (04g section 4): a 30-vertex 5-regular graph G with a perfect matching
such that NO perfect matching M of G admits permutations r, s with (P1)-(P3) and (P5).

Construction.  Block B on {0,...,8}:
    0:3456  1:3478  2:3478  3:01256  4:01256  5:03478  6:03478  7:12568  8:12567
Vertices 0,1,2 have degree 4 in B; each is joined by a bridge to the root of a 7-vertex cap
K7 - {root u1, root u2, u3u4, u5u6} (root degree 4 in the cap).  G is simple and 5-regular on 9 + 3*7 = 30 vertices.

Checks (all exhaustive, independent of the CSP solver p5solve.py):
  1. G is simple and 5-regular; it has a perfect matching.
  2. Every perfect matching of G contains the three bridges and meets B in {35,46,78} or {36,45,78}.
  3. For each of these two, brute force over ALL Euler orientations of the B-part of H = G - M and ALL
     choices of the R 2-factor finds no (r,s) satisfying (P1)-(P3) and (P5) on B, using the definitions
       (P2) r(r(v)) != v, s(s(v)) != v;  (P3) s(r(u)) != m(u);  (P5) m(r^{-1}(x)) != r(x).
     Since every bridge lies in M, H has no edge leaving B, so r and s restrict to permutations of B and the
     conditions at B-vertices involve only B and the mates; hence no (r,s) exists for G.
  4. G itself satisfies Conjecture 1: the exact-cover solver of check_regular_path_decomposition.py finds
     15 simple five-edge paths, verified independently here.  So G is NOT a counterexample to Conjecture 1;
     only the (P5) route (Theorem C + P5*) fails on it.
  5. Cross-check with p5solve.solve on the whole graph G for every perfect matching (optional, --full).
"""
import sys
from itertools import combinations, product

B = {0: [3, 4, 5, 6], 1: [3, 4, 7, 8], 2: [3, 4, 7, 8], 3: [0, 1, 2, 5, 6], 4: [0, 1, 2, 5, 6],
     5: [0, 3, 4, 7, 8], 6: [0, 3, 4, 7, 8], 7: [1, 2, 5, 6, 8], 8: [1, 2, 5, 6, 7]}


def build():
    adj = {v: set(B[v]) for v in B}
    nxt = 9
    bridges = []
    for a in (0, 1, 2):
        cap = list(range(nxt, nxt + 7)); nxt += 7
        root, u1, u2, u3, u4, u5, u6 = cap
        missing = {frozenset(e) for e in ((root, u1), (root, u2), (u3, u4), (u5, u6))}
        for x, y in combinations(cap, 2):
            if frozenset((x, y)) not in missing:
                adj.setdefault(x, set()).add(y); adj.setdefault(y, set()).add(x)
        adj[a].add(root); adj[root].add(a)
        bridges.append(frozenset((a, root)))
    return adj, bridges


def perfect_matchings(adj, verts):
    verts = frozenset(verts)

    def go(free):
        if not free:
            yield []
            return
        u = min(free)
        for v in sorted(adj[u]):
            if v in free:
                for rest in go(free - {u, v}):
                    yield [frozenset((u, v))] + rest
    yield from go(verts)


def brute_force_block(mate):
    """All (r,s) on the B-part of H = G - M; mate maps 0,1,2 to outside vertices ('X0' etc.)."""
    H = {v: [w for w in B[v] if mate[v] != w] for v in B}
    assert all(len(H[v]) == 4 for v in H)
    edges = sorted({(min(v, w), max(v, w)) for v in H for w in H[v]})
    assert len(edges) == 18
    found = 0
    orientations = 0
    for bits in product((0, 1), repeat=len(edges)):
        arcs = [(u, w) if b else (w, u) for (u, w), b in zip(edges, bits)]
        outd = {v: 0 for v in H}
        for u, w in arcs:
            outd[u] += 1
        if any(outd[v] != 2 for v in H):
            continue
        orientations += 1
        outs = {v: [w for (u, w) in arcs if u == v] for v in H}
        # r(v) is one of the two out-neighbours of v; s is then determined: s(w) = tail of the non-R arc into w
        for choice in product((0, 1), repeat=len(H)):
            r = {v: outs[v][c] for v, c in zip(sorted(H), choice)}
            if len(set(r.values())) != len(H):
                continue  # r must be a permutation (one R-arc into every vertex)
            s = {}
            for v in H:
                other = outs[v][1 - choice[sorted(H).index(v)]]
                s[other] = v  # non-R arc v -> other, so s(other) = v
            assert len(s) == len(H)
            rinv = {w: v for v, w in r.items()}
            ok = all(r[r[v]] != v and s[s[v]] != v for v in H)
            ok = ok and all(s[r[u]] != mate[u] for u in H)            # (P3)
            ok = ok and all(mate[rinv[x]] != r[x] for x in H)          # (P5)
            if ok:
                found += 1
    return orientations, found


def main():
    adj, bridges = build()
    n = len(adj)
    assert n == 30 and all(len(adj[v]) == 5 for v in adj) and all(v not in adj[v] for v in adj)
    print("G: 30 vertices, simple, 5-regular")
    restrictions = set()
    count = 0
    for pm in perfect_matchings(adj, adj.keys()):
        count += 1
        assert all(b in pm for b in bridges), "a perfect matching misses a bridge"
        restrictions.add(frozenset(e for e in pm if all(x in B for x in e)))
    print("perfect matchings of G:", count, "; restrictions to B:", [sorted(map(sorted, r)) for r in restrictions])
    assert count > 0
    for res in restrictions:
        mate = {0: 'X0', 1: 'X1', 2: 'X2'}
        for e in res:
            x, y = tuple(e); mate[x] = y; mate[y] = x
        orient, found = brute_force_block(mate)
        print("B-part with M_B =", sorted(map(sorted, res)), ": Euler orientations", orient, "; valid (r,s):", found)
        assert found == 0
    from check_regular_path_decomposition import exact_cover
    order = sorted(adj)
    idx0 = {v: i for i, v in enumerate(order)}
    bits = [sum(1 << idx0[w] for w in adj[v]) for v in order]
    paths = exact_cover(bits)
    assert paths is not None and len(paths) == 15
    used = set()
    for path in paths:
        assert len(set(path)) == 6
        for x, y in zip(path, path[1:]):
            e = frozenset((x, y)); assert e not in used and bits[x] >> y & 1; used.add(e)
    assert len(used) == 75
    print("G decomposes into 15 simple five-edge paths (Conjecture 1 holds for G):", [list(p) for p in paths])
    if "--full" in sys.argv:
        sys.path.insert(0, "04-handoff/p5_scratch")
        from p5solve import solve
        idx = {v: i for i, v in enumerate(sorted(adj))}
        A = [set(idx[w] for w in adj[v]) for v in sorted(adj)]
        k = 0
        for pm in perfect_matchings(adj, adj.keys()):
            m = {}
            for e in pm:
                x, y = tuple(e); m[idx[x]] = idx[y]; m[idx[y]] = idx[x]
            assert solve(A, m, node_limit=10**7) is None
            k += 1
        print("p5solve: all", k, "perfect matchings of G infeasible")
    print("P5* FAILS for G: no perfect matching admits (P1)-(P3)+(P5).")


if __name__ == "__main__":
    main()
