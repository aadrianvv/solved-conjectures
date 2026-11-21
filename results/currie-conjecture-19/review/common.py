"""Independent review helpers (written from scratch, not derived from verify.py)."""
from fractions import Fraction

GAMMA = {'0': '01', '1': '2', '2': '02'}


def apply(h, w):
    return ''.join(h[c] for c in w)


def mor(lst):
    return {str(i): lst[i] for i in range(3)}


def rev_m(h):
    return {c: v[::-1] for c, v in h.items()}


def compose(h, g):
    """h o g (apply g first)."""
    return {c: apply(h, g[c]) for c in '012'}


def fixed_point(h, start, n):
    w = start
    while len(w) < n:
        w2 = apply(h, w)
        assert w2.startswith(w)
        w = w2
    return w[:n]


def factors(s, n):
    return {s[i:i + n] for i in range(len(s) - n + 1)}


def exact_factors_G(N, prefix_len=None):
    """Exact L_N(G): take length-N factors of a prefix and certify by closure:
    (a) all length-N factors of gamma^k(0) for the k with |gamma^{k-1}(0)| < N are in S,
    (b) every length-N factor of gamma(v), v in S, is in S.
    Then every length-N factor of every gamma^k(0) is in S (induction), so S = L_N(G)."""
    if prefix_len is None:
        prefix_len = 40 * N + 1000
    P = fixed_point(GAMMA, '0', prefix_len)
    S = factors(P, N)
    # (a)
    k = 0
    w = '0'
    while True:
        prev_len = len(w)
        w2 = apply(GAMMA, w)
        # w2 = gamma^{k+1}(0); condition for k+1: |gamma^k(0)| < N
        if prev_len >= N:
            break
        assert factors(w2, N) <= S
        w = w2
    # (b)
    for v in S:
        assert factors(apply(GAMMA, v), N) <= S, 'closure fails'
    return S, P


def image_factors(h, LG, n):
    out = set()
    for v in LG:
        out |= factors(apply(h, v), n)
    return out


def parikh(w):
    return (w.count('0'), w.count('1'), w.count('2'))


# ---------- exact arithmetic for lambda ----------
def lam_enclosure(bits=400):
    """Rational interval [lo,hi] containing the real root of x^3-2x^2+x-1 (increasing on [3/2,2])."""
    p = lambda x: x ** 3 - 2 * x ** 2 + x - 1
    lo, hi = Fraction(3, 2), Fraction(2)
    assert p(lo) < 0 < p(hi)
    for _ in range(bits):
        mid = (lo + hi) / 2
        if p(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo, hi
