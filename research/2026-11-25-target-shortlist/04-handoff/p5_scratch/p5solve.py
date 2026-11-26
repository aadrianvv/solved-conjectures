"""CSP search for (r,s) with (P1)-(P3) and (P5) in a 5-regular graph with perfect matching.

Vertex-local domains: for each vertex, the 4 H-edges get (inR, dir) with dir in {in,out};
exactly 2 R-edges (1 in, 1 out), 2 S-edges (1 in, 1 out); (P5) no M-pair both R;
(P3) no M-pair both in. Edge consistency between endpoints. Backtracking with MRV + forward checking.
"""
import sys, random
from itertools import combinations, product
from collections import defaultdict

sys.setrecursionlimit(100000)
VARIANT = 0


def local_domain(w, nb, mate, p5=True, p3=True):
    pairs = [(x, y) for x, y in combinations(nb, 2) if mate[x] == y]
    dom = []
    for Rset in combinations(range(4), 2):
        if p5 and any({nb.index(x), nb.index(y)} == set(Rset) for x, y in pairs):
            continue
        Sset = [i for i in range(4) if i not in Rset]
        for rin in Rset:
            for sin in Sset:
                a = []
                for i in range(4):
                    a.append((i in Rset, i == rin or i == sin))  # (inR, incoming)
                if p3 and any(a[nb.index(x)][1] and a[nb.index(y)][1] for x, y in pairs):
                    continue
                if VARIANT >= 1 and any(a[nb.index(x)][1] == a[nb.index(y)][1] for x, y in pairs):
                    continue
                if VARIANT >= 2 and any(a[nb.index(x)][0] == a[nb.index(y)][0] for x, y in pairs):
                    continue
                dom.append(tuple(a))
    return dom


def roles(v, H, a):
    """(r(v), Rin(v), s(v), Sout(v)) from local assignment a."""
    out = [None] * 4
    for i, w in enumerate(H[v]):
        inR, inc = a[i]
        out[(0 if inR else 3) if not inc else (1 if inR else 2)] = w
    return out


def solve(adj, mate, rng=None, p5=True, p3=True, node_limit=10**7, p6=False, extra=None):
    n = len(adj)
    H = [sorted(w for w in adj[v] if w != mate[v]) for v in range(n)]
    # triple constraints (P6): M-edge cd, e common H-neighbour: not (r(d)=e and s(e)=r(c))
    tri = defaultdict(list)
    if p6:
        for c in range(n):
            d = mate[c]
            for e in set(H[c]) & set(H[d]):
                con = (c, d, e)
                for x in con:
                    tri[x].append(con)

    def tri_ok(v, assign):
        for c, d, e in tri[v]:
            if assign[c] is None or assign[d] is None or assign[e] is None:
                continue
            rc = roles(c, H, assign[c])[0]
            rd = roles(d, H, assign[d])[0]
            se = roles(e, H, assign[e])[2]
            if rd == e and se == rc:
                return False
        return True
    doms = [local_domain(v, H[v], mate, p5, p3) for v in range(n)]
    if rng:
        for d in doms:
            rng.shuffle(d)
    cur = [list(d) for d in doms]
    assign = [None] * n
    nodes = [0]

    def compatible(u, au, v, iv, iu):
        # u's edge index iu to v; v's edge index iv to u
        return True

    def ok_pair(u, a, v, b):
        iu = H[u].index(v); iv = H[v].index(u)
        return a[iu][0] == b[iv][0] and a[iu][1] != b[iv][1]

    def rec():
        nodes[0] += 1
        if nodes[0] > node_limit:
            raise TimeoutError
        best = None
        for v in range(n):
            if assign[v] is None:
                if best is None or len(cur[v]) < len(cur[best]):
                    best = v
                    if len(cur[v]) <= 1:
                        break
        if best is None:
            return True
        v = best
        for a in list(cur[v]):
            assign[v] = a
            if not tri_ok(v, assign):
                assign[v] = None
                continue
            saved = []
            okk = True
            for w in H[v]:
                if assign[w] is None:
                    newd = [b for b in cur[w] if ok_pair(v, a, w, b)]
                    saved.append((w, cur[w]))
                    cur[w] = newd
                    if not newd:
                        okk = False
                        break
            if okk and rec():
                return True
            for w, d in reversed(saved):
                cur[w] = d
            assign[v] = None
        return False

    if not rec():
        return None
    r = {}; s = {}
    for v in range(n):
        for i, w in enumerate(H[v]):
            inR, incoming = assign[v][i]
            if inR and not incoming:
                r[v] = w
            if (not inR) and incoming:
                s[v] = w  # S arc w->v, so s(v)=w
    assert len(r) == n and len(s) == n
    return r, s


def check(adj, mate, r, s):
    n = len(adj)
    rinv = {v: u for u, v in r.items()}
    for v in range(n):
        assert r[r[v]] != v and s[s[v]] != v
        assert s[r[v]] != mate[v]  # P3
        assert mate[rinv[v]] != r[v]  # P5
    E = set()
    for v in range(n):
        for e in ((v, r[v]), (v, s[v]), (v, mate[v])):
            E.add(frozenset(e))
    assert len(E) == 5 * n // 2
