# Arithmetic identities used in PROOF.md, for h = 3..20
from math import comb
for h in range(3, 21):
    n = 2*h - 1; d = n - 1; N = comb(n, 2) - 1
    assert N == h*(2*h-3) == 2*h*(h-2) + h
    assert N == n*(h-1) - 1 == (n-2)*h
    assert n - 2*(h-2) == 3                       # M_0 misses 3 vertices
    assert N - 1 - (n-2) == n*(h-2)               # Lemma 4(3)
    assert (n-2) - (h-2 - 1) == h and (n-2) - (h-1-1) == h-1   # g_max
    assert (n-1)*(h-1) + (h-2) == N               # Lemma 3 count
    assert (n-2) + n*(h-2) == N - 1               # max level colour n-1, w = h-2
    # rows/columns
    left = [c for c in range(h)]; right = [c for c in range(h, 2*h)]
    for c in range(2*h):
        rows = [r for r in range(h) if 2*h*r + c <= N-1]
        assert rows == list(range(h-1 if c < h else h-2)), (h, c, rows)
    assert (N - 2*h) % (2*h) == h                 # last position column alpha + h
    # Lemma 5(1): sigma1*(h-1) + sigma2*(h-2) = 2(n-2), 0<=sigma_i<=h
    sols = [(s1, s2) for s1 in range(h+1) for s2 in range(h+1) if s1*(h-1) + s2*(h-2) == 2*(n-2)]
    assert all((h-2)*(s1+s2-4) == 2 - s1 for s1, s2 in sols)
    print(h, "N=%d" % N, "special-column solutions:", sols)
