"""Structure of maximum MIL partitions in the Gamma formulation (third session).

Phase convention: every path v1..vk (k >= 3) has v2, v4, ... designated (I+).  For odd k
both ends are usable (U); for even k the end vk is a W-end ({0,2}).
Gamma_U: graph on Y whose edges are the U-ends (joining the two Y-neighbours of the end).
A y is bound if its interior neighbour is I+, free otherwise.
A deficient component is a component of Gamma_U that is a tree and has only free vertices.
"""
from collections import Counter


def classify(adj, Y, flips=frozenset()):
    n = len(adj)
    Ys = set(Y)
    X = [v for v in range(n) if v not in Ys]
    seen = set()
    paths = []
    for v in X:
        if v in seen:
            continue
        if sum(w not in Ys for w in adj[v]) <= 1:
            p = [v]
            seen.add(v)
            prev, cur = None, v
            while True:
                nxt = [w for w in adj[cur] if w not in Ys and w != prev]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                p.append(cur)
                seen.add(cur)
            paths.append(p)
    kind = {}   # x -> 'I+','I-','U','W','K2','Z'
    for pi, p in enumerate(paths):
        k = len(p)
        if k == 1:
            kind[p[0]] = 'Z'
        elif k == 2:
            kind[p[0]] = kind[p[1]] = 'K2'
        else:
            par = 0 if (k % 2 == 1 or pi not in flips) else 1
            for i in range(1, k - 1):
                kind[p[i]] = 'I+' if i % 2 == 1 - par else 'I-'
            kind[p[0]] = 'U' if kind[p[1]] == 'I+' else 'W'
            kind[p[-1]] = 'U' if kind[p[-2]] == 'I+' else 'W'
    return paths, kind


def gamma(adj, Y, kind):
    Ys = set(Y)
    bound = {y: any(kind[x] == 'I+' for x in adj[y]) for y in Y}
    edges = []
    for x, kd in kind.items():
        if kd == 'U':
            a, b = [w for w in adj[x] if w in Ys]
            edges.append((a, b, x))
    return bound, edges


def deficient(adj, Y, flips=frozenset()):
    paths, kind = classify(adj, Y, flips)
    bound, edges = gamma(adj, Y, kind)
    par = {y: y for y in Y}

    def f(a):
        while par[a] != a:
            par[a] = par[par[a]]
            a = par[a]
        return a
    ecount = Counter()
    for a, b, _ in edges:
        ra, rb = f(a), f(b)
        if ra != rb:
            par[ra] = rb
    comp = {}
    for y in Y:
        comp.setdefault(f(y), []).append(y)
    for a, b, _ in edges:
        ecount[f(a)] += 1
    out = []
    for r, vs in comp.items():
        if ecount[r] == len(vs) - 1 and not any(bound[y] for y in vs):
            out.append(vs)
    return kind, bound, out


def absorption_feasible(adj, Y, flips=frozenset(), allow_w=True, k2_odd=False):
    """Reduced absorption problem (see note, fifth pass):
    choose absorbed sets so that every K2 gets exactly one absorbed neighbour (mode 'one'),
    each z absorbs 0, 2 or 3 free neighbours, each W-end absorbs 0 or both neighbours
    (if allow_w), absorbed vertices are distinct, and every deficient component has an
    absorbed vertex.  Returns True/False (SAT)."""
    from pysat.formula import IDPool
    from pysat.solvers import Cadical153
    from pysat.card import CardEnc, EncType
    import itertools
    kind, bound, D = deficient(adj, Y, flips)
    Ys = set(Y)
    free = [y for y in Y if not bound[y]]
    pool = IDPool()
    a = {}   # (y, gadget) absorption variables
    gad = {}
    for y in free:
        for x in adj[y]:
            kd = kind[x]
            if kd == 'Z' or (kd == 'W' and allow_w):
                a[(y, x)] = pool.id((y, x))
                gad.setdefault(x, []).append(y)
            elif kd == 'K2':
                a[(y, x)] = pool.id((y, x))
                gad.setdefault(x, []).append(y)
    cls = []
    for y in free:
        vs = [a[(y, x)] for x in adj[y] if (y, x) in a]
        for p, q in itertools.combinations(vs, 2):
            cls.append([-p, -q])
    # gadget constraints
    done_k2 = set()
    for x, ys in gad.items():
        kd = kind[x]
        lits = [a[(y, x)] for y in ys]
        if kd == 'Z':
            # not exactly one
            for i, l in enumerate(lits):
                cls.append([-l] + [m for j, m in enumerate(lits) if j != i])
        elif kd == 'W':
            # 0 or both Y-neighbours (both must be free)
            ynb = [w for w in adj[x] if w in Ys]
            if len(ys) < 2:
                cls.append([-lits[0]])
            else:
                cls.append([-lits[0], lits[1]])
                cls.append([-lits[1], lits[0]])
    for x in kind:
        if kind[x] == 'K2' and x not in done_k2:
            x2 = [w for w in adj[x] if w in kind and kind[w] == 'K2'][0]
            done_k2.add(x)
            done_k2.add(x2)
            lits = [a[(y, e)] for e in (x, x2) for y in gad.get(e, [])]
            if not lits:
                return False
            if k2_odd:
                # odd number absorbed in total; an even total is never used (sufficient, see note)
                for pat in itertools.product([0, 1], repeat=len(lits)):
                    if sum(pat) % 2 == 0:
                        cls.append([(-lits[i] if pat[i] else lits[i]) for i in range(len(lits))])
            else:
                enc = CardEnc.equals(lits, bound=1, vpool=pool, encoding=EncType.pairwise)
                cls += enc.clauses
    for comp in D:
        lits = [a[(y, x)] for y in comp for x in adj[y] if (y, x) in a]
        cls.append(lits)
    with Cadical153(bootstrap_with=cls) as s:
        return s.solve()


def absorption_any_phase(adj, Y, allow_w=True, k2_odd=False):
    """Try every phase choice of the even paths (odd paths keep phase A)."""
    import itertools
    paths, _ = classify(adj, Y)
    ev = [i for i, p in enumerate(paths) if len(p) >= 4 and len(p) % 2 == 0]
    for r in range(len(ev) + 1):
        for fl in itertools.combinations(ev, r):
            if absorption_feasible(adj, Y, frozenset(fl), allow_w, k2_odd):
                return True
    return False
