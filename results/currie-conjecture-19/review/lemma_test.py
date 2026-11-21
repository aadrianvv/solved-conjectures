"""Brute-force test of the general Lemmas 4 and 5 (left/right insertion) on several uniformly recurrent words
(fixed points of primitive morphisms), including words with non-ordinary bispecial factors.
Uses long prefixes (a test, not a certificate)."""
import random
from common import *

PL = 120000
NMAX = 14


def lang_data(s, nmax):
    """bispecials with extension graphs for lengths <= nmax, from a prefix (dropping a margin)."""
    s = s[:PL]
    E = {}
    for n in range(0, nmax + 1):
        for f in factors(s[100:], n + 2):
            E.setdefault(f[1:-1], set()).add((f[0], f[-1]))
    return E


def rets(s, w, cap=4000):
    occ = []
    i = s.find(w, 100)
    while i != -1 and len(occ) < cap:
        occ.append(i); i = s.find(w, i + 1)
    return {s[occ[k]:occ[k + 1]] for k in range(len(occ) - 1)}


def bisp(E):
    return {w: ed for w, ed in E.items() if len({e for e, d in ed}) >= 2 and len({d for e, d in ed}) >= 2}


def ordinary(ed):
    return len({e for e, d in ed}) == 2 and len({d for e, d in ed}) == 2 and len(ed) == 3


def lam(a, b): return {c: (a + b if c == b else c) for c in '012'}
def rh(a, b): return {c: (b + a if c == b else c) for c in '012'}


def test(x, name):
    Ex = lang_data(x, NMAX)
    Bx = bisp(Ex)
    nt = 0
    for a in '012':
        for b in '012':
            if a == b: continue
            f = lambda c: a if c == b else c
            for kind in 'LR':
                ext = {d for e, d in Ex[''] if e == a} if kind == 'L' else {e for e, d in Ex[''] if d == a}
                if len(ext) != 1: continue
                ex = ext.pop()
                h = lam(a, b) if kind == 'L' else rh(a, b)
                y = apply(h, x[:PL])
                Ey = lang_data(y, NMAX // 2)
                By = {w: ed for w, ed in bisp(Ey).items() if w}
                pred = {}
                for u, ed in Bx.items():
                    if kind == 'L':
                        if u and len({f(d) for e, d in ed}) >= 2:
                            pred[apply(h, u)] = frozenset((e, f(d)) for e, d in ed)
                        if {a, b} <= {d for e, d in ed}:
                            E2 = frozenset([(e, f(ex)) for e, d in ed if d == a] + [(e, b) for e, d in ed if d == b])
                            if len({e for e, d in E2}) >= 2:
                                pred[apply(h, u) + a] = E2
                    else:
                        if u and len({f(e) for e, d in ed}) >= 2:
                            pred[apply(h, u)] = frozenset((f(e), d) for e, d in ed)
                        if {a, b} <= {e for e, d in ed}:
                            E2 = frozenset([(f(ex), d) for e, d in ed if e == a] + [(b, d) for e, d in ed if e == b])
                            if len({d for e, d in E2}) >= 2:
                                pred[a + apply(h, u)] = E2
                pred = {w: e for w, e in pred.items() if len(w) <= NMAX // 2}
                got = {w: frozenset(e) for w, e in By.items()}
                assert pred == got, (name, kind, a, b, set(pred) ^ set(got))
                # (b) return words for ordinary u: Parikh(Ret(Lambda u)) = M_h Parikh(Ret u)
                for u, ed in Bx.items():
                    if u and ordinary(ed) and len(u) <= 4:
                        Ep = {d for e, d in ed}; Em = {e for e, d in ed}
                        if kind == 'L':
                            Lu = apply(h, u) + (a if Ep == {a, b} else '')
                        else:
                            Lu = (a if Em == {a, b} else '') + apply(h, u)
                        assert Lu in got and ordinary(got[Lu])
                        R1 = sorted(parikh(apply(h, r)) for r in rets(x[:PL], u))
                        R2 = sorted(parikh(r) for r in rets(y[:PL], Lu))
                        assert R1 == R2, (name, kind, a, b, u)
                nt += 1
    nonord = sorted(w for w, ed in Bx.items() if w and not ordinary(ed))[:5]
    print('%-12s lemma 4/5 predictions agree for %d (kind,a,b) cases; sample non-ordinary bispecials: %s' % (name, nt, nonord))


tests = [('G', GAMMA, '0'), ('tribonacci', mor(['01', '02', '0']), '0')]
random.seed(1)
while len(tests) < 9:
    h = mor([''.join(random.choice('012') for _ in range(random.randint(1, 4))) for _ in range(3)])
    # primitive and prolongable on 0, growing
    if not h['0'].startswith('0') or len(h['0']) < 2: continue
    M = [[h[c].count(a) for c in '012'] for a in '012']
    P = M
    for _ in range(3):
        P = [[sum(P[i][k] * M[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    if not all(P[i][j] > 0 for i in range(3) for j in range(3)): continue
    tests.append(('rand' + str(len(tests)), h, '0'))
for name, h, s in tests:
    x = fixed_point(h, s, PL + 10)
    test(x, name + str([h[c] for c in '012']) if name.startswith('rand') else name)
