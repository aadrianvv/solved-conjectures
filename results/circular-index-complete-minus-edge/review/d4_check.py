# Independent check of the statements of PROOF.md on all acyclic proper 5-edge-colourings of K_5 - uv (h = 3).
import itertools, sys
from collections import Counter

def graph(n):
    E = [(a, b) for a in range(n) for b in range(a+1, n) if (a, b) != (0, 1)]   # u=0, v=1
    return E

def proper_colourings(n, E):
    col = {}
    def rec(k):
        if k == len(E):
            yield dict(col); return
        e = E[k]
        used = {col[f] for f in E[:k] if set(e) & set(f)}
        for c in range(n):
            if c not in used:
                col[e] = c
                yield from rec(k+1)
                del col[e]
    yield from rec(0)

def arcs(n, E, col):
    return {e: [f for f in E if f != e and set(e) & set(f) and col[f] == (col[e]+1) % n] for e in E}

def levels(E, out):
    indeg = Counter(f for e in E for f in out[e])
    order = []; st = [e for e in E if indeg[e] == 0]; ind = dict((e, indeg[e]) for e in E)
    while st:
        e = st.pop(); order.append(e)
        for f in out[e]:
            ind[f] -= 1
            if ind[f] == 0: st.append(f)
    if len(order) < len(E): return None
    L = {e: 0 for e in E}
    for e in order:
        for f in out[e]: L[f] = max(L[f], L[e]+1)
    return L

def check_structure(n, E, col0, L, log):
    """Check Lemmas 2-7, (M), (C), (B), (R), (O), on one acyclic colouring. Returns dict of facts."""
    h = (n+1)//2; N = len(E); u, v = 0, 1; normal = list(range(2, n))
    out = arcs(n, E, col0)
    # Lemma 2
    sizes = Counter(col0.values())
    small = [i for i in range(n) if sizes[i] == h-2]
    assert len(small) == 1 and all(sizes[i] == h-1 for i in range(n) if i != small[0])
    shift = (-small[0]) % n
    col = {e: (col0[e] + shift) % n for e in E}
    M = {i: [e for e in E if col[e] == i] for i in range(n)}
    A = set(range(n)) - {x for e in M[0] for x in e}; assert len(A) == 3
    src = [e for e in E if all(e not in out[f] for f in E)]; snk = [e for e in E if not out[e]]
    assert len(src) == 1 and len(snk) == 1
    fs, gs = src[0], snk[0]
    assert col[fs] == 1 and col[gs] == n-1 and set(fs) <= A and set(gs) <= A
    # (E1),(E2)
    def Nplus(S, i):
        return {f for f in M[(i+1) % n] if any(set(f) & set(e) for e in S)}
    for i in range(n):
        cls = M[i] if i != n-1 else [e for e in M[i] if e != gs]
        for k in range(len(cls)+1):
            for S in itertools.combinations(cls, k):
                assert len(Nplus(S, i)) >= len(S)
    # Lemma 3
    assert sorted(L.values()) == list(range(N))
    assert all(col[e] == (L[e]+1) % n for e in E)
    s = sorted(E, key=lambda e: L[e])
    for l in range(N-1): assert set(s[l]) & set(s[l+1])
    for e, f in itertools.combinations(E, 2):
        if set(e) & set(f):
            a, b = (e, f) if L[e] < L[f] else (f, e)
            assert (L[b]-L[a]) % n not in (0, n-1)
    w = {e: L[e]//n for e in E}
    for i in range(n):
        for j in range(h):
            a = sum(1 for e in M[i] if w[e] >= j)
            exp = 0 if j == h-1 else (h-1-j if i != 0 else h-2-j)
            assert a == exp, (i, j, a, exp)
    # (M)
    pos = {x: [l for l in range(N) if x in s[l]] for x in range(n)}
    for x, y in itertools.combinations(range(n), 2):
        c = len(set(pos[x]) & set(pos[y]))
        assert c == (0 if {x, y} == {u, v} else 1)
    # Lemma 4
    runs = {x: 1 + sum(1 for a, b in zip(pos[x], pos[x][1:]) if b != a+1) for x in range(n)}
    for x in normal: assert all((b-a) % n == 1 for a, b in zip(pos[x], pos[x][1:]))
    for l in range(N-1): assert len(set(s[l]) & set(s[l+1])) == 1
    assert sum(runs.values()) == N+1
    com = set(s[0]) & set(s[N-1]); assert len(com) == 1; b = com.pop()
    assert b in normal and runs[b] == h-1
    for x in normal:
        assert all(q-p in (1, 2*h) for p, q in zip(pos[x], pos[x][1:]))
        if x != b:
            assert runs[x] == h-2 and pos[x][-1] == pos[x][0] + N - 2*h and 0 <= pos[x][0] <= 2*h-1
    assert runs[u] == runs[v] == n-2
    # (C)
    for l in range(N-1):
        c = (set(s[l]) & set(s[l+1])).pop(); assert c in normal
    # Lemma 5(1)
    special = sorted(set(pos[u]) | set(pos[v]))
    for l in special:
        if l+2*h <= N-1: assert l+2*h in special
        if l-2*h >= 0: assert l-2*h in special
    scols = sorted({l % (2*h) for l in special})
    s1 = sum(1 for c in scols if c < h); s2 = len(scols) - s1
    facts = {'sigma': (s1, s2)}
    if (s1, s2) != (2, 2):
        facts['L5_1'] = False
        return facts
    r = [c for c in scols if c < h]
    assert sorted(c for c in scols if c >= h) == [c+h for c in r]
    facts['L5_1'] = True
    P = [c for c in range(h) if c not in r]
    # Lemma 5(2)
    first = {x: pos[x][0] for x in normal if x != b}
    assert sorted(first.values()) == sorted(P + [p+h for p in P])
    xa = {first[x]: x for x in first}
    # Lemma 5(3)
    def junctions(x):
        g = 0; i = 0; res = Counter(); gmax = h if x != b else h-1
        for p, q in zip(pos[x], pos[x][1:]):
            if q-p == 1: g += 1
            else: res[g] += 1; i += 1
        assert g == gmax
        return res
    for x in normal:
        jx = junctions(x)
        alpha = pos[x][0]
        for g in jx: assert (alpha+g) % (2*h) not in scols
    # (B), (R) and rho_c
    def row(l): return l // (2*h)
    rho = {}  # rho[(c, z)]
    for c in range(h-1):
        lst = {b} | {xa[p] for p in P if p <= c} | {xa[p+h] for p in P if p > c}
        got = {}
        for z in normal:
            rr = [rw for rw in range(h-1) if 2*h*rw+c in pos[z] and 2*h*rw+c+1 in pos[z]]
            assert len(rr) <= 1
            if rr: got[z] = rr[0]
        assert set(got) == lst and sorted(got.values()) == list(range(h-1))
        for z in got: rho[(c, z)] = got[z]
    for p in P:
        x = xa[p]; rr = [rw for rw in range(h-1) if 2*h*rw+h-1 in pos[x] and 2*h*rw+h in pos[x]]
        assert len(rr) == 1 and rr[0] <= h-3; rho[(h-1, x)] = rr[0]
        y = xa[p+h]; rr = [rw for rw in range(1, h-1) if 2*h*rw-1 in pos[y] and 2*h*rw in pos[y]]
        assert len(rr) == 1; rho[(-1, y)] = rr[0]
        rho[(p-1, x)] = 0 if (p-1, x) not in rho else rho[(p-1, x)]
        assert rho[(p-1, x)] == 0
        if (p, y) in rho: raise AssertionError("conflict")
        rho[(p, y)] = h-2
    rho[(-1, b)] = 0; rho[(h-1, b)] = h-2
    assert len({rho[(h-1, xa[p])] for p in P}) == len(P)
    assert len({rho[(-1, xa[p+h])] for p in P}) == len(P)
    for z in normal:
        for c in range(h):
            R = sorted({row(l) for l in pos[z] if l % (2*h) == c})
            if R: assert R == list(range(rho[(c-1, z)], rho[(c, z)]+1)), (z, c, R)
    # Lemma 6
    pi = lambda c: sum(1 for p in P if p <= c)
    for c in range(h-1):
        assert rho[(c, b)] == pi(c)
        for p in P:
            if p <= c: assert rho[(c, xa[p])] < rho[(c, b)]
            else: assert rho[(c, xa[p+h])] > rho[(c, b)]
    # Lemma 7
    for m, pm in enumerate(P, 1):
        x, y = xa[pm], xa[pm+h]
        Rx = sorted({row(l) for l in pos[x] if l % (2*h) == pm}); Ry = sorted({row(l) for l in pos[y] if l % (2*h) == pm})
        assert Rx == list(range(0, m)) and Ry == list(range(m, h-1))
        jx = junctions(x)
        assert jx[0] == m-1 and jx[h] == h-2-m and sum(jx.values()) == h-3
    facts['full'] = True
    return facts

if __name__ == "__main__":
    n = 5; E = graph(n); tot = 0; acyc = []
    for col in proper_colourings(n, E):
        tot += 1
        L = levels(E, arcs(n, E, col))
        if L is not None: acyc.append((col, L))
    print("proper colourings:", tot, "acyclic:", len(acyc))
    stats = Counter()
    for col, L in acyc:
        f = check_structure(n, E, col, L, None)
        stats[(f['sigma'], f.get('full', False))] += 1
    print("sigma distribution / full checks passed:", dict(stats))
    # The order in the Remark
    u, v, b, x, y = 0, 1, 2, 3, 4
    order = [(u,b),(x,b),(v,x),(u,x),(x,y),(v,y),(u,y),(y,b),(v,b)]
    cols = [1,2,3,4,0,1,2,3,4]
    col = {tuple(sorted(e)): c for e, c in zip(order, cols)}
    assert sorted(col) == sorted(E)
    for e, f in itertools.combinations(E, 2):
        if set(e) & set(f): assert col[e] != col[f]
    L = levels(E, arcs(n, E, col))
    print("Remark colouring acyclic:", L is not None, "levels:", [L[tuple(sorted(e))] for e in order])
