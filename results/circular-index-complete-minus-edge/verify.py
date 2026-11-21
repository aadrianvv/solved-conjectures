#!/usr/bin/env python3
"""Checks for PROOF.md: circular chromatic index of K_{d+1} minus an edge (Mazak-Zrubak, Conjecture 2).

Part A (d = 4, exhaustive over all proper 5-edge-colourings of K_5 - e): finds every colouring whose tight digraph is
        acyclic and checks on each of them the statements of Lemmas 2, 3, 4 and 5 that do not need d >= 6.
Part B (d = 4, 6): exhaustive search for orderings s_0, ..., s_{N-1} of the edges of K_{d+1} - e such that consecutive
        edges share a vertex and, for edges e before f sharing a vertex, pos(f) - pos(e) is not 0 or -1 modulo d+1
        (the conclusion of Lemma 3), up to automorphisms of the graph. For d = 4 the number found, times 12 automorphisms
        and 5 colour rotations, must be the number of acyclic colourings; for d = 6 there must be none.
Standard library only. Usage: python3 verify.py [d ...]   (default d = 6, about 10 seconds; d = 8 was not completed).
The file verify_sat.py checks d = 6 directly from the definition with a SAT solver (needs python-sat)."""
import sys, itertools, time

def graph(d):
    n = d + 1
    edges = [(a, b) for a in range(n) for b in range(a + 1, n) if (a, b) != (0, 1)]   # u = 0, v = 1
    return n, edges

def tight_digraph(n, edges, col):
    out = {e: [] for e in edges}
    for e in edges:
        for f in edges:
            if e != f and set(e) & set(f) and col[f] == (col[e] + 1) % n: out[e].append(f)
    return out

def longest_levels(edges, out):
    """levels by longest path, or None if there is a directed cycle"""
    indeg = {e: 0 for e in edges}
    for e in edges:
        for f in out[e]: indeg[f] += 1
    lev = {e: 0 for e in edges}; stack = [e for e in edges if indeg[e] == 0]; seen = 0
    while stack:
        e = stack.pop(); seen += 1
        for f in out[e]:
            lev[f] = max(lev[f], lev[e] + 1); indeg[f] -= 1
            if indeg[f] == 0: stack.append(f)
    return lev if seen == len(edges) else None

def part_a():
    d = 4; n, edges = graph(d); N = len(edges); h = d // 2 + 1
    acyclic = []; total = 0
    col = {}
    def rec(k):
        nonlocal total
        if k == N:
            total += 1
            out = tight_digraph(n, edges, col); lev = longest_levels(edges, out)
            if lev is not None: acyclic.append((dict(col), lev, out))
            return
        e = edges[k]
        used = {col[f] for f in edges[:k] if set(e) & set(f)}
        for c in range(n):
            if c not in used:
                col[e] = c; rec(k + 1); del col[e]
    rec(0)
    assert acyclic, "expected acyclic colourings for d = 4"
    for col_, lev, out in acyclic:
        classes = [[e for e in edges if col_[e] == i] for i in range(n)]
        small = [i for i in range(n) if len(classes[i]) == h - 2]
        assert len(small) == 1 and all(len(classes[i]) == h - 1 for i in range(n) if i != small[0])       # Lemma 2(i)
        i0 = small[0]; A = set(range(n)) - {x for e in classes[i0] for x in e}; assert len(A) == 3
        src = [e for e in edges if not any(e in out[f] for f in edges)]; snk = [e for e in edges if not out[e]]
        assert len(src) == 1 and len(snk) == 1 and set(src[0]) <= A and set(snk[0]) <= A                    # Lemma 2(ii)
        assert col_[src[0]] == (i0 + 1) % n and col_[snk[0]] == (i0 - 1) % n
        assert sorted(lev.values()) == list(range(N))                                                       # Lemma 3
        s = sorted(edges, key=lambda e: lev[e])
        assert all(col_[e] == (lev[e] + 1 + i0) % n for e in edges)
        assert all(set(s[l]) & set(s[l + 1]) for l in range(N - 1))
        for e, f in itertools.combinations(s, 2):
            if set(e) & set(f): assert (lev[f] - lev[e]) % n not in (0, n - 1)
        pos = {x: [l for l in range(N) if x in s[l]] for x in range(n)}
        runs = {x: 1 + sum(1 for a, b in zip(pos[x], pos[x][1:]) if b != a + 1) for x in range(n)}
        common = set(s[0]) & set(s[-1]); assert len(common) == 1
        b = common.pop(); assert b not in (0, 1) and runs[b] == h - 1                                       # Lemma 4
        for x in range(2, n):
            assert all((q - p) in (1, 2 * h) for p, q in zip(pos[x], pos[x][1:]))
            if x != b: assert runs[x] == h - 2 and pos[x][0] + (N - 1 - pos[x][-1]) == n
        assert runs[0] == runs[1] == n - 2
        special = sorted(set(pos[0]) | set(pos[1]))                                                         # Lemma 5
        cols = sorted({l % (2 * h) for l in special})
        assert special == [l for l in range(N) if l % (2 * h) in cols] and len(cols) == 4
        assert sorted(c % h for c in cols) == sorted(2 * [c for c in cols if c < h])
    print("Part A, d = 4: %d proper 5-edge-colourings of K_5 - e, %d with acyclic tight digraph; Lemmas 2-5 hold on all of them." % (total, len(acyclic)))
    return len(acyclic)

def part_b(d):
    """number of orderings up to the automorphisms of K_{d+1} - uv (swap u, v; permute the other vertices):
    vertices are introduced in canonical order (u = 0 before v = 1, normal vertices 2, 3, ... in increasing order)"""
    n, edges = graph(d); N = len(edges)
    adj = {e: [f for f in edges if f != e and set(e) & set(f)] for e in edges}
    pos = {}; count = 0; order = []
    seen = set()
    def canonical_new(x):
        if x in (0, 1): return x == 0 or 0 in seen
        return all(y in seen for y in range(2, x))
    def ok(e, l):
        for f in adj[e]:
            if f in pos and (l - pos[f]) % n in (0, n - 1): return False
        return True
    def rec(l):
        nonlocal count
        if l == N: count += 1; return
        cands = adj[order[-1]] if order else [(0, 2), (2, 3)]
        for e in cands:
            if e in pos: continue
            new = [x for x in e if x not in seen]
            if len(new) == 2 and order: continue
            if l == 1 and order[0] == (2, 3) and 2 not in e: continue      # tie-break for the two vertices of s_0
            if new and order and not canonical_new(new[0]): continue
            if not ok(e, l): continue
            pos[e] = l; order.append(e); seen.update(new)
            rec(l + 1)
            order.pop(); del pos[e]; seen.difference_update(new)
    rec(0)
    return count

if __name__ == "__main__":
    t0 = time.time(); na = part_a()
    c4 = part_b(4); assert 5 * 12 * c4 == na, (c4, na)        # 12 automorphisms, 5 rotations of the colours
    print("Part B, d = 4: %d edge orderings with property (P) up to automorphisms; 5 x 12 x %d = %d acyclic colourings, as in Part A." % (c4, c4, na))
    for d in [int(x) for x in sys.argv[1:]] or [6]:           # further even d may be given as arguments (d = 8 is slow)
        c = part_b(d); assert c == 0, (d, c)
        print("Part B, d = %d: no edge ordering of K_%d - e with property (P)  (%.0fs)" % (d, d + 1, time.time() - t0), flush=True)
    print("All checks passed.")
