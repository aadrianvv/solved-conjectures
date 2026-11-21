"""Brute-force bispecial factors, extension graphs and return words of G, U, V from exact factor sets,
and comparison with the formulas of Propositions 1 and 2 of PROOF.md."""
import sys
from common import *

NB = int(sys.argv[1]) if len(sys.argv) > 1 else 400
N = int(sys.argv[2]) if len(sys.argv) > 2 else 1300

a1 = mor(['210', '20', '21'])
a4 = mor(['102', '2', '1'])

LG, P = exact_factors_G(N)
assert len(LG) == 2 * N + 1, len(LG)
LU = image_factors(a1, LG, N)
LV = image_factors(a4, LG, N)
print('sizes', len(LG), len(LU), len(LV))


def bispecials(LN, nmax):
    LN = list(LN)
    res = {}
    for n in range(0, nmax + 1):
        Ln2 = {f[:n + 2] for f in LN}
        E = {}
        for s in Ln2:
            E.setdefault(s[1:-1], set()).add((s[0], s[-1]))
        for w, ed in E.items():
            L = {e for e, d in ed}
            R = {d for e, d in ed}
            if len(L) >= 2 and len(R) >= 2:
                # return words
                rets = set()
                for F in LN:
                    if F.startswith(w):
                        j = F.find(w, 1) if w else 1
                        assert j > 0, ('return word longer than N', len(w))
                        rets.add(F[:j])
                res[w] = (frozenset(ed), rets)
    return res


def ordinary(ed):
    L = {e for e, d in ed}
    R = {d for e, d in ed}
    return len(L) == 2 and len(R) == 2 and len(ed) == 3


def EmEp(ed):
    return frozenset(e for e, d in ed), frozenset(d for e, d in ed)


def Phi(w, ed):
    Em, Ep = EmEp(ed)
    s = '2' if Em == frozenset('12') else ''
    t = '0' if Ep == frozenset('02') else ''
    return s + apply(GAMMA, w) + t


def PsiV(w, ed):
    Em, Ep = EmEp(ed)
    return ('2' if Em == frozenset('01') else '') + apply(a4, w) + ('1' if Ep == frozenset('02') else '')


def PsiU(w, ed):
    Em, Ep = EmEp(ed)
    return ('0' if Em == frozenset('01') else '') + apply(a1, w) + ('21' if Ep == frozenset('02') else '2')


BG = bispecials(LG, NB)
print('G bispecial lengths', sorted(len(w) for w in BG))
# Proposition 1
orbit = {}
for s in ['20', '0']:
    w = s
    k = 0
    while len(w) <= NB:
        assert w in BG, (s, k, w)
        orbit[w] = (s, k)
        ed = BG[w][0]
        w = Phi(w, ed)
        k += 1
nonempty = [w for w in BG if w]
assert set(nonempty) == set(orbit), (set(nonempty) ^ set(orbit))
for w in nonempty:
    assert ordinary(BG[w][0]), w
# empty word
assert len(BG['']) and len(BG[''][0]) == 5
print('Prop 1 orbits OK up to', NB, ':', len(nonempty), 'nonempty bispecials, all ordinary')
# graphs period, (E-,E+) alternation, return words correspond with M
M = [[1, 0, 1], [1, 0, 0], [0, 1, 1]]
mv = lambda A, v: tuple(sum(A[i][j] * v[j] for j in range(3)) for i in range(3))
for w in nonempty:
    s, k = orbit[w]
    ed, rets = BG[w]
    assert len(rets) == 3
    Em, Ep = EmEp(ed)
    exp = {('20', 0): ('01', '12'), ('20', 1): ('12', '02'), ('0', 0): ('12', '12'), ('0', 1): ('01', '02')}[(s, k % 2)]
    assert (Em, Ep) == (frozenset(exp[0]), frozenset(exp[1])), (w, Em, Ep)
    w2 = Phi(w, ed)
    if w2 in BG:
        assert sorted(mv(M, parikh(r)) for r in rets) == sorted(parikh(r) for r in BG[w2][1])
    # period 4 of graphs
    if k >= 4:
        # find the element 4 steps before
        prev = [v for v in orbit if orbit[v] == (s, k - 4)][0]
        assert BG[prev][0] == ed
print('Prop 1 (3) and return-word correspondence OK')
print('seed data', sorted(BG['20'][0]), sorted(BG['20'][1]), sorted(BG['0'][0]), sorted(BG['0'][1]))
# table
for w in sorted(nonempty, key=len)[:14]:
    s, k = orbit[w]
    ed, rets = BG[w]
    Em, Ep = EmEp(ed)
    rl = sorted(len(r) for r in rets)
    print(len(w), s, k, ''.join(sorted(Em)), ''.join(sorted(Ep)), rl, round(len(w) / rl[0], 4), w if len(w) < 20 else '')

for name, L, Psi, h, extra in [('V', LV, PsiV, a4, {'1', '2', '21'}), ('U', LU, PsiU, a1, {'2', '02', '21', '021'})]:
    B = bispecials(L, NB)
    imgs = {}
    for w in nonempty:
        v = Psi(w, BG[w][0])
        assert v not in imgs
        imgs[v] = w
    nonemptyX = {w for w in B if w}
    got_extra = nonemptyX - set(imgs)
    assert got_extra == extra, (name, got_extra)
    assert not (extra & set(imgs))
    # every image of length <= NB present
    for v, w in imgs.items():
        if len(v) <= NB:
            assert v in B, (name, v, w)
            ed, rets = B[v]
            Mh = [[sum(1 for c in h[d] if c == a) for d in '012'] for a in '012']
            assert sorted(mv(Mh, parikh(r)) for r in BG[w][1]) == sorted(parikh(r) for r in rets), (name, v)
    for v in nonemptyX:
        assert ordinary(B[v][0]), (name, v)
    print(name, 'Prop 2 OK up to', NB, ':', len(nonemptyX), 'nonempty bispecials; L2 size', len(B[''][0]))
    for v in sorted(extra, key=lambda t: (len(t), t)):
        ed, rets = B[v]
        print('  extra', v, sorted(ed), sorted(parikh(r) for r in rets), 'max ratio', max(len(v) / len(r) for r in rets))
