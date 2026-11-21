"""Reduction identities R3, R5, decompositions, R4 conjugacy for arXiv rows, L2 sets, complexity of all 20 images."""
import sys
from common import *

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400

gR = rev_m(GAMMA)
G = fixed_point(GAMMA, '0', 200000)
Gp = fixed_point(gR, '2', 200000)
perm = lambda s: {str(i): s[i] for i in range(3)}  # [pi(0)pi(1)pi(2)]

# R3
c1 = mor(['0', '2', '01']); c2 = mor(['2', '1', '01']); tau = perm('102')
assert compose(c1, c2) == GAMMA
assert compose(c2, c1) == mor(['2', '01', '21']) == compose(tau, compose(gR, tau))
assert apply(mor(['2', '0', '10']), G)[:100000] == Gp[:100000]
assert apply(mor(['2', '0', '01']), Gp)[:100000] == G[:100000]
print('R3 identities hold on prefixes of length 1e5')

a = {1: mor(['210', '20', '21']), 2: mor(['02', '021', '02121']), 3: mor(['2', '0', '1']), 4: mor(['102', '2', '1'])}
b = {1: mor(['2', '0', '1']), 2: mor(['0', '2', '21']), 3: mor(['1', '0', '2']), 4: mor(['12', '012', '01012']),
     5: mor(['201', '21', '01']), 6: mor(['102', '1', '2'])}
pi0 = perm('201'); sigma = perm('210'); rho = perm('021')
assert a[3] == b[1] == pi0 and b[3] == tau
assert b[6] == compose(rho, rev_m(a[4]))
assert b[5] == compose(pi0, rev_m(a[1]))
assert b[4] == compose(pi0, rev_m(a[2]))
assert b[2] == compose(sigma, mor(['2', '0', '01']))
assert compose(rev_m(a[2]), mor(['2', '0', '10'])) == mor(['12120', '20', '12020'])
assert compose(compose(tau, a[1]), GAMMA) == mor(['20121', '20', '20120'])


def r4(h, hp):
    """find u with hp(c)u = u h(c), u prefix of all hp(c), suffix of all h(c)."""
    m = min(min(len(h[c]) for c in '012'), min(len(hp[c]) for c in '012'))
    for k in range(0, m + 1):
        u = hp['0'][:k]
        if all(hp[c] + u == u + h[c] and hp[c].startswith(u) and h[c].endswith(u) for c in '012'):
            return u
    return None


assert r4(mor(['12120', '20', '12020']), mor(['20121', '20', '20120'])) == '20'
print('R5 identities OK')


# decompositions
def lam(a_, b_):
    return {c: (a_ + b_ if c == b_ else c) for c in '012'}


def rh(a_, b_):
    return {c: (b_ + a_ if c == b_ else c) for c in '012'}


assert compose(perm('120'), compose(lam('2', '0'), rh('1', '2'))) == GAMMA
assert compose(perm('021'), compose(rh('1', '0'), lam('2', '0'))) == a[4]
assert compose(perm('021'), compose(lam('1', '2'), compose(rh('0', '1'), lam('2', '0')))) == a[1]
print('elementary decompositions OK')

ax1 = [['1210202', '12102', '1210202102'], ['1210202102', '1210202', '121020210202'],
       ['021201212', '0212012', '021201212012'], ['21021102211021102', '2102110221102', '2102110221102110221102']]
ax2 = [['10212', '0212', '0210212'], ['2120210', '20210', '202120210'], ['121201210', '1201210', '120121201210'],
       ['1201212010', '1212010', '121201212010'], ['1212010', '12010', '1201212010'],
       ['221102210', '21102210', '2110221102210']]


def gpow(g, k):
    h = mor(['0', '1', '2'])
    for _ in range(k):
        h = compose(h, g)
    return h


arx_match = {}
for fig, rows, base, g in [(1, ax1, a, GAMMA), (2, ax2, b, gR)]:
    for i, row in enumerate(rows):
        h = mor(row)
        found = []
        for j in base:
            for k in range(0, 7):
                hk = compose(base[j], gpow(g, k))
                if all(len(hk[c]) == len(h[c]) for c in '012'):
                    for (x, y, lab) in [(h, hk, 'h=h,hk=h\''), (hk, h, 'hk=h,h=h\'')]:
                        u = r4(x, y)
                        if u is not None:
                            found.append((j, k, u, lab))
        arx_match[(fig, i + 1)] = found
        print('arXiv fig', fig, 'row', i + 1, found)

# complexity of all 20 images via exact factor sets
LG, P = exact_factors_G(NMAX + 1)
LGs = {n: {f[:n] for f in LG} for n in range(NMAX + 2)}
LGp = {n: {f[::-1] for f in LGs[n]} for n in LGs}  # L(G') = L(G)^R
# check L(G')^R claim directly on prefix
for n in [1, 2, 5, 17, 40]:
    assert factors(Gp[:100000], n) == LGp[n], n
words = []
for j in a: words.append(('a%d(G)' % j, a[j], LGs))
for j in b: words.append(('b%d(G\')' % j, b[j], LGp))
for i, row in enumerate(ax1): words.append(('arXiv1.%d(G)' % (i + 1), mor(row), LGs))
for i, row in enumerate(ax2): words.append(('arXiv2.%d(G\')' % (i + 1), mor(row), LGp))
words.append(('G', mor(['0', '1', '2']), LGs)); words.append(("G'", mor(['0', '1', '2']), LGp))
bad = []
for name, h, L in words:
    ml = min(len(h[c]) for c in '012')
    m = min(NMAX, (NMAX - 1) // ml + 2)
    Fbig = set()
    for v in {f[:m] for f in L[NMAX]}:
        Fbig |= factors(apply(h, v), NMAX)
    for n in range(0, NMAX + 1):
        Fn = {f[:n] for f in Fbig}
        if len(Fn) != 2 * n + 1:
            bad.append((name, n, len(Fn)))
            break
print('complexity: checked n<=%d for %d words; failures:' % (NMAX, len(words)), bad)
# L2 of images
for name, h, L in words[:10]:
    print(name, sorted(image_factors(h, L[2], 2)))
