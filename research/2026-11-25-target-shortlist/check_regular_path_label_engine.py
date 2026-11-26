"""Exhaustive label-identification engine for local configurations of the canonical construction.

A *scenario* is a finite list of symbols together with facts r(x)=y, s(x)=y, m(x)=y,
forced equalities and extra inequalities.  The engine enumerates every partition of the
symbols (every way in which the named vertices can coincide) such that the quotient
satisfies the axioms that hold in every canonical construction of 04d:

* r, s are injective partial functions and m is an involution, all without fixed points;
* the edges {x,r(x)}, {x,s(x)}, {x,m(x)} are pairwise distinct, so M, R and S are
  disjoint edge sets of a simple graph; this includes (P2);
* (P3): s(r(x)) != m(x) whenever both sides are known;
* (optional) the known edges contain no diamond: every edge has at most one common
  neighbour among the known edges;
* the scenario's extra equalities and inequalities.

Facts are only necessary conditions, so the enumeration is a superset of the realizable
configurations.  It is complete: every partition is generated exactly once (restricted
growth strings), and a branch is cut only when one of the listed axioms already fails on
the assigned symbols.  The checks are incremental and undone on backtracking.
"""

from itertools import combinations


class Scenario:
    def __init__(self, name):
        self.name = name
        self.syms = []
        self.facts = []      # (fn, x, y)
        self.neq = []        # (x, y)
        self.eq = []         # (x, y) forced equalities
        self.diamond_free = True

    def sym(self, *names):
        for n in names:
            if n not in self.syms:
                self.syms.append(n)

    def r(self, x, y):
        self.sym(x, y); self.facts.append(("r", x, y))

    def s(self, x, y):
        self.sym(x, y); self.facts.append(("s", x, y))

    def m(self, x, y):
        self.sym(x, y); self.facts.append(("m", x, y)); self.facts.append(("m", y, x))

    def ne(self, x, y):
        self.sym(x, y); self.neq.append((x, y))

    def same(self, x, y):
        self.sym(x, y); self.eq.append((x, y))

    def distinct(self, *xs):
        for x, y in combinations(xs, 2):
            self.ne(x, y)


class _State:
    def __init__(self, diamond_free):
        self.F = {"r": {}, "s": {}, "m": {}}
        self.Fi = {"r": {}, "s": {}, "m": {}}
        self.edges = {}
        self.adj = {}
        self.undo = []
        self.diamond_free = diamond_free

    def _set(self, d, k, v):
        self.undo.append((d, k))
        d[k] = v

    def add(self, fn, X, Y):
        """Add fact fn(X)=Y on classes. Return False on contradiction."""
        if X == Y:
            return False
        F, Fi = self.F[fn], self.Fi[fn]
        if X in F:
            return F[X] == Y
        if Y in Fi:
            return False
        if fn == "r":
            lab = ("R", X, Y)
        elif fn == "s":
            lab = ("S", Y, X)
        else:
            lab = ("M",)
        key = frozenset((X, Y))
        old = self.edges.get(key)
        if old is not None and old != lab:
            return False
        self._set(F, X, Y)
        self._set(Fi, Y, X)
        # (P3): s(r(x)) != m(x)
        R, S, M, Ri = self.F["r"], self.F["s"], self.F["m"], self.Fi["r"]
        if fn == "r" and Y in S and X in M and S[Y] == M[X]:
            return False
        if fn == "s" and X in Ri and Ri[X] in M and M[Ri[X]] == Y:
            return False
        if fn == "m" and X in R and R[X] in S and S[R[X]] == Y:
            return False
        if old is None:
            self._set(self.edges, key, lab)
            for A, B in ((X, Y), (Y, X)):
                if A not in self.adj:
                    self._set(self.adj, A, set())
                self.adj[A].add(B)
                self.undo.append(("adjadd", A, B))
            if self.diamond_free:
                common = self.adj[X] & self.adj[Y]
                if len(common) >= 2:
                    return False
                for Z in common:
                    if len(self.adj[X] & self.adj[Z]) >= 2 or len(self.adj[Y] & self.adj[Z]) >= 2:
                        return False
        return True

    def mark(self):
        return len(self.undo)

    def rollback(self, k):
        while len(self.undo) > k:
            item = self.undo.pop()
            if item[0] == "adjadd":
                self.adj[item[1]].discard(item[2])
            else:
                d, key = item
                del d[key]


def enumerate_partitions(sc, check_p3=True, limit=None):
    """Yield dicts symbol -> class id for every admissible identification."""
    syms = sc.syms
    pos = {x: i for i, x in enumerate(syms)}
    facts_at = [[] for _ in syms]
    for f in sc.facts:
        facts_at[max(pos[f[1]], pos[f[2]])].append(f)
    neq_at = [[] for _ in syms]
    for x, y in sc.neq:
        neq_at[max(pos[x], pos[y])].append((x, y))
    eq_at = [[] for _ in syms]
    for x, y in sc.eq:
        eq_at[max(pos[x], pos[y])].append((x, y))
    st = _State(sc.diamond_free)
    cls = {}

    def rec(i, ncls):
        if i == len(syms):
            yield dict(cls)
            return
        x = syms[i]
        for k in range(ncls + 1):
            cls[x] = k
            if all(cls[a] != cls[b] for a, b in neq_at[i]) and all(cls[a] == cls[b] for a, b in eq_at[i]):
                mk = st.mark()
                if all(st.add(fn, cls[a], cls[b]) for fn, a, b in facts_at[i]):
                    yield from rec(i + 1, max(ncls, k + 1))
                st.rollback(mk)
            del cls[x]

    yield from rec(0, 0)


def simple(piece, cls):
    return len({cls[v] for v in piece}) == len(piece)


def groups(cls):
    g = {}
    for x, v in cls.items():
        g.setdefault(v, []).append(x)
    return [sorted(v) for v in g.values() if len(v) > 1]
