"""Step 4 check, independent: exact integer lengths of bispecial factors and return words along the orbits,
sign of |w| - alpha |r| with certified rational enclosures of lambda; limits m0 computed exactly by own derivation."""
import sys
from fractions import Fraction as F
from common import lam_enclosure

KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
lo, hi = lam_enclosure(1500)
# alpha = 1 + 1/(lam^2-1) = lam^2/(lam^2-1), decreasing in lam for lam>1
alo, ahi = hi * hi / (hi * hi - 1), lo * lo / (lo * lo - 1)
assert alo < ahi and ahi - alo < F(1, 10 ** 400)
# check alpha = (3 - lam + 2 lam^2)/5 numerically to 400 digits
a2lo, a2hi = (3 - hi + 2 * lo * lo) / 5, (3 - lo + 2 * hi * hi) / 5
assert max(alo, a2lo) <= min(ahi, a2hi)
print('alpha ~', float(alo), ' mu ~', float(alo) + 1)

M = [[1, 0, 1], [1, 0, 0], [0, 1, 1]]
mv = lambda A, v: [sum(A[i][j] * v[j] for j in range(3)) for i in range(3)]
Ma1 = [[1, 1, 0], [1, 0, 1], [1, 1, 1]]  # columns Parikh(210),(20),(21)
Ma4 = [[1, 0, 0], [1, 0, 1], [1, 1, 0]]  # columns Parikh(102),(2),(1)
# check those matrices
for Mh, h in [(Ma1, ['210', '20', '21']), (Ma4, ['102', '2', '1'])]:
    for c in range(3):
        assert [h[c].count(str(i)) for i in range(3)] == [Mh[i][c] for i in range(3)]

# orbit data from Proposition 1 (own derivation): seeds, (E-,E+) types, additive vectors
seeds = {'A': ([1, 0, 1], [[1, 0, 1], [1, 1, 1], [2, 1, 1]], 0),  # 20 ; Ret 20, 201, 2010
         'B': ([1, 0, 0], [[1, 1, 0], [1, 0, 1], [1, 1, 1]], 1)}  # 0 ; Ret 01, 02, 012
# types: (Em, Ep) for k even/odd
types = {'A': [('01', '12'), ('12', '02')], 'B': [('12', '12'), ('01', '02')]}


def cvec(Em, Ep):
    v = [0, 0, 0]
    if Em == '12': v[2] += 1  # prefix 2
    if Ep == '02': v[0] += 1  # suffix 0
    return v


def kappa(word, Em, Ep):
    if word == 'G': return 0
    if word == 'V': return (1 if Em == '01' else 0) + (1 if Ep == '02' else 0)
    if word == 'U': return (1 if Em == '01' else 0) + (2 if Ep == '02' else 1)


def length_vec(word):
    if word == 'G': return [1, 1, 1]
    Mh = Ma1 if word == 'U' else Ma4
    return [sum(Mh[i][j] for i in range(3)) for j in range(3)]


worst = {}
limits = {}
for word in ['G', 'U', 'V']:
    g = length_vec(word)
    for orb in 'AB':
        P, Qs, _ = seeds[orb]
        P = list(P); Qs = [list(q) for q in Qs]
        for k in range(KMAX + 1):
            Em, Ep = types[orb][k % 2]
            lw = kappa(word, Em, Ep) + sum(g[i] * P[i] for i in range(3))
            for qi, Q in enumerate(Qs):
                lr = sum(g[i] * Q[i] for i in range(3))
                # D = lw - alpha lr ; certified sign
                Dhi = lw - alo * lr
                Dlo = lw - ahi * lr
                assert Dhi < 0, ('VIOLATION', word, orb, k, qi)
                key = (word, orb, k % 4, qi)
                if k > KMAX - 8:
                    limits.setdefault(key, []).append(float(Dhi))
                ratio = F(lw, lr)
                if word not in worst or ratio > worst[word][0]:
                    worst[word] = (ratio, orb, k, qi, lw, lr)
            c = cvec(Em, Ep)
            P = [x + y for x, y in zip(mv(M, P), c)]
            Qs = [mv(M, q) for q in Qs]
print('all D_k < 0 for k <=', KMAX, '(lengths up to ~10^%d)' % len(str(lw)))
for wd in worst: print(wd, 'max ratio', float(worst[wd][0]), worst[wd][1:4])
for key in sorted(limits):
    v = limits[key]
    if abs(v[-1]) < 100:
        print('bounded family', key, ['%.6f' % x for x in v[-2:]])


# exact m0 via own derivation: residue r, N = M^4, C = sum_{i=0}^{3} M^{3-i} c_{r+i}
def matmul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def matpow(A, n):
    R = [[int(i == j) for j in range(3)] for i in range(3)]
    for _ in range(n): R = matmul(R, A)
    return R


def solve(A, b):
    A = [[F(A[i][j]) for j in range(3)] + [F(b[i])] for i in range(3)]
    for i in range(3):
        p = next(r for r in range(i, 3) if A[r][i] != 0); A[i], A[p] = A[p], A[i]
        A[i] = [x / A[i][i] for x in A[i]]
        for r in range(3):
            if r != i: A[r] = [x - A[r][i] * y for x, y in zip(A[r], A[i])]
    return [A[i][3] for i in range(3)]


N4 = matpow(M, 4)
print('exact m0 = kappa + g.(I-N)^{-1} C per (word, orbit, residue):')
for word in ['G', 'U', 'V']:
    g = length_vec(word)
    row = []
    for orb in 'AB':
        for r in range(4):
            C = [0, 0, 0]
            for i in range(4):
                Em, Ep = types[orb][(r + i) % 2]
                C = [x + y for x, y in zip(C, mv(matpow(M, 3 - i), cvec(Em, Ep)))]
            X = solve([[int(i == j) - N4[i][j] for j in range(3)] for i in range(3)], C)
            Em, Ep = types[orb][r % 2]
            row.append(kappa(word, Em, Ep) + sum(g[i] * X[i] for i in range(3)))
    print(word, 'A:', [str(x) for x in row[:4]], 'B:', [str(x) for x in row[4:]])
