# Enumerate "relaxed configurations" for given h: everything that Lemmas 4-5 assert about positions of normal vertices
# (first positions, steps 1/2h, junction counts, no junction in a special column), plus: every non-special position holds
# exactly 2 normal vertices, every special one exactly 1, and consecutive positions share exactly one normal vertex.
# (M) is NOT imposed. Then test the implications:
#   (B) holds always;  b meets each x at most once  => Lemma 6 conclusion;
#   b meets each x exactly once => Lemma 7(1);   additionally x_{p_m}, x_{p_m+h} meet once => Lemma 7(2) for that m;
#   count configurations where all normal pairs meet exactly once (Step 8 says none for h >= 4).
import sys, itertools
from collections import Counter
def main(h):
    n = 2*h-1; N = 2*h*(h-2)+h; W = 2*h
    tot = Counter()
    for r1, r2 in itertools.combinations(range(h), 2):
        scol = {r1, r2, r1+h, r2+h}; P = [c for c in range(h) if c not in {r1, r2}]
        special = [l % W in scol for l in range(N)]
        def cells(alpha, gmax, J):
            pos = []; i = 0; cnt = Counter(J)
            for g in range(gmax+1):
                for k in range(cnt[g]+1): pos.append(alpha+g+W*(i+k))
                i += cnt[g]
            return pos
        def opts(alpha, gmax, nj):
            allowed = [g for g in range(gmax+1) if (alpha+g) % W not in scol]
            return [(J, cells(alpha, gmax, J)) for J in itertools.combinations_with_replacement(allowed, nj)]
        verts = [('b', 0, opts(0, h-1, h-2))] + [('x', a, opts(a, h, h-3)) for a in P + [p+h for p in P]]
        cap = [1 if special[l] else 2 for l in range(N)]
        occ = [0]*N; chosen = []
        def rec(k):
            if k == len(verts):
                if occ != cap: return
                at = [[] for _ in range(N)]
                for idx, (J, pos) in enumerate(chosen):
                    for l in pos: at[l].append(idx)
                for l in range(N-1):
                    if len(set(at[l]) & set(at[l+1])) != 1: return
                analyse(chosen, at)
                return
            for J, pos in verts[k][2]:
                if all(occ[l] < cap[l] for l in pos):
                    for l in pos: occ[l] += 1
                    chosen.append((J, pos)); rec(k+1); chosen.pop()
                    for l in pos: occ[l] -= 1
        def analyse(chosen, at):
            tot['configs'] += 1
            names = ['b'] + ['x%d' % a for a in P] + ['x%d' % (p+h) for p in P]
            posof = [set(pos) for J, pos in chosen]
            idx = {nm: i for i, nm in enumerate(names)}
            # rho_c for c = 0..h-2
            rho = {}
            for c in range(h-1):
                for i in range(len(chosen)):
                    rr = [r for r in range(h-1) if W*r+c in posof[i] and W*r+c+1 in posof[i]]
                    assert len(rr) <= 1
                    if rr: rho[(c, i)] = rr[0]
                lst = {0} | {idx['x%d' % p] for p in P if p <= c} | {idx['x%d' % (p+h)] for p in P if p > c}
                got = {i for (cc, i) in rho if cc == c}
                assert got == lst and sorted(rho[(c, i)] for i in got) == list(range(h-1)), "(B) fails"
            meet = lambda i, j: len(posof[i] & posof[j])
            bm = [meet(0, i) for i in range(1, len(chosen))]
            pi = lambda c: sum(1 for p in P if p <= c)
            if max(bm) <= 1:
                tot['b meets each <=1'] += 1
                for c in range(h-1):
                    assert rho[(c, 0)] == pi(c), "Lemma 6 fails"
                    for p in P:
                        if p <= c: assert rho[(c, idx['x%d' % p])] < rho[(c, 0)]
                        else: assert rho[(c, idx['x%d' % (p+h)])] > rho[(c, 0)]
            if min(bm) == 1 and max(bm) == 1:
                tot['b meets each exactly once'] += 1
                for m, pm in enumerate(P, 1):
                    x, y = idx['x%d' % pm], idx['x%d' % (pm+h)]
                    Rx = sorted(l // W for l in posof[x] if l % W == pm); Ry = sorted(l // W for l in posof[y] if l % W == pm)
                    assert Rx == list(range(m)) and Ry == list(range(m, h-1)), "Lemma 7(1) fails"
                    if meet(x, y) == 1:
                        tot['7(2) instances'] += 1
                        J = Counter(chosen[x][0]); assert J[0] == m-1 and J[h] == h-2-m, "Lemma 7(2) fails"
            if all(meet(i, j) == 1 for i, j in itertools.combinations(range(len(chosen)), 2)):
                tot['all normal pairs meet once'] += 1
        rec(0)
    print("h=%d:" % h, dict(tot), flush=True)
for h in map(int, sys.argv[1:]): main(h)
