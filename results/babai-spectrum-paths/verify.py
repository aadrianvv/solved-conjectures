#!/usr/bin/env python3
"""Brute-force check of the Babai k-spectrum of the path P_n (Johnson-Kaya-Matzke, Conjecture 2.1).

For every n <= NMAX, every k in 1..n-1 and every D subset of {1..n-1} with |D| = k, compute the chromatic number of
the graph on {1..n} in which u ~ v iff |u - v| is in D, and compare the set of values with
{ceil(n/(n-k)), ..., k+1}.  Also checks the independence bound |S| <= n - k and the description of m used in the paper.
Standard library only.  Usage: python3 verify.py [NMAX]   (default 14, a few seconds)."""
import sys
from itertools import combinations

def chromatic_number(n, D):
    adj = [[u for u in range(n) if u != v and abs(u - v) in D] for v in range(n)]
    def colourable(c):
        col = [-1] * n
        def go(v):
            if v == n: return True
            used = {col[u] for u in adj[v] if u < v}
            top = max(col[:v], default=-1)
            for x in range(min(c, top + 2)):          # symmetry breaking: first use of colours in order
                if x not in used:
                    col[v] = x
                    if go(v + 1): return True
            col[v] = -1
            return False
        return go(0)
    c = 1
    while not colourable(c): c += 1
    return c

def max_independent(n, D):
    best = 0
    def go(v, chosen):
        nonlocal best
        if len(chosen) + (n - v) <= best: return
        if v == n: best = len(chosen); return
        if all(v - u not in D for u in chosen): go(v + 1, chosen + [v])
        go(v + 1, chosen)
    go(0, [])
    return best

def paper_m(n, k):
    """the m of Theorem 2.3: n - ceil(n/m) < k <= n - ceil(n/(m+1)), for floor(n/2) < k <= n-1"""
    ms = [m for m in range(2, n) if n - -(-n // m) < k <= n - -(-n // (m + 1))]
    assert len(ms) == 1, (n, k, ms)
    return ms[0]

def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    total = 0
    for n in range(2, nmax + 1):
        for k in range(1, n):
            lo = -(-n // (n - k)); hi = k + 1
            if k > n // 2: assert paper_m(n, k) + 1 == lo, (n, k)
            else: assert lo == 2
            spec = set()
            for D in combinations(range(1, n), k):
                Dset = set(D); chi = chromatic_number(n, Dset); spec.add(chi); total += 1
                assert lo <= chi <= hi, (n, D, chi)
                if n <= 10: assert max_independent(n, Dset) <= n - k, (n, D)
            assert spec == set(range(lo, hi + 1)), (n, k, sorted(spec), lo, hi)
        print("n = %2d: Spec(P_n, k) = {ceil(n/(n-k)), ..., k+1} for every k in 1..%d" % (n, n - 1), flush=True)
    print("All checks passed (%d distance sets)." % total)

if __name__ == "__main__":
    main()
