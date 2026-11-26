"""Independent referee checker for Theorem C (04g-regular-path-p5-and-m-diamond.md, section 3).

Theorem C (candidate): (M, r, s) with (P1)-(P3) and (P5) m(r^{-1}(x)) != r(x) for all x
=> E(G) partitions into five-edge paths.

Written from the text of 04g section 3 (and 04d sections 1-3).  It does not import or copy
check_regular_path_p5sweep.py, check_regular_path_p5_endtoend.py or the p5 scratch scripts.
Reused audited pieces: Lemma 1, (P1)-(P3) check, exact path cover and the first sweep of the
Theorem A referee (check_regular_path_theoremA_independent.py); the Plant helper of the
Theorem B referee; the graph generators of check_regular_path_theoremBprime_independent.py.

Parts:
  lemma4   own enumeration of Lemma 4 with (P5) (changed pendant != own d) as the only local
           restriction (D-pendants are changed pendants by Lemma C6).
  firstsweep / procedure  on planted generic (M,r,s) data with (P1)-(P3)+(P5): X2 sources in
           cases alpha / beta / gamma (links 0, 1, 2 and (F1)), D-paths, D-cycles of lengths
           3..7, odd type-2 cycles of lengths 3, 5, 7 with D-pendants and type-1 pendants,
           random glue; and on random graphs with Lemma 1 constructions satisfying (P5).
           Checks Proposition C1 (after the first sweep only X2 sources are non-simple) with the
           Theorem A referee's sweep, then runs an own implementation of section 3 and verifies
           every output exactly.  Intermediate claims (Lemma C2, C3(iv),(v), C4 degrees, C6) are
           asserted.
Random runs are evidence, not proof.

Usage: python -B check_regular_path_theoremC_independent.py [--quick] [--seed N]
"""

import sys
import time
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import combinations, product
from random import Random

from check_regular_path_theoremA_independent import lemma1, check_P, path_cover
from check_regular_path_theoremA_independent import sweep as first_sweep, SweepFailure
from check_regular_path_theoremB_independent import Plant


def E(u, v):
    return (u, v) if u < v else (v, u)


def edges_of(seq):
    return [E(seq[i], seq[i + 1]) for i in range(len(seq) - 1)]


class Failure(Exception):
    pass


def p5_ok(m, r):
    rinv = {y: x for x, y in r.items()}
    return all(m[rinv[x]] != r[x] for x in r)


# ----------------------------------------------------------------------------------------
# Lemma 4 under (P5), own enumeration (pendant kinds u = s(b_i), c = r(b_i))

def lemma4_p5():
    res = Counter()
    bad = []
    for closed in (True, False):
        for d0b2, d2b0 in ([(False, False)] if closed else list(product((False, True), repeat=2))):
            b = ["b0", "b1", "b2"]
            c = ["c0", "c1", "c2"]
            e = ["c2" if closed else "cm1", "c0", "c1"]
            d = ["b2" if d0b2 else "d0", "d1", "b0" if d2b0 else "d2"]
            ce = set(c) | set(e)
            present = (ce | set(d)) - set(b)
            for kinds in product("uc", repeat=3):
                opts = []
                for i in range(3):
                    if kinds[i] == "u":
                        opts.append(sorted(present - {c[i], e[i], d[i]}) + ["F%d" % i])
                    else:
                        opts.append(sorted(present - ce) + ["F%d" % i])
                for A in product(*opts):
                    if len(set(A)) != 3:
                        continue
                    if any(kinds[i] == "c" and A[i] == d[i] for i in range(3)):
                        res["excluded by (P5): changed A_i = d_i"] += 1
                        continue
                    trails = [(A[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                    el = [x for t in trails for x in edges_of(t)]
                    if len(set(el)) != 15:
                        continue
                    kind = "closed" if closed else "open"
                    cov = path_cover(el, 3)
                    if cov is not None:
                        assert sorted(x for p in cov for x in edges_of(p)) == sorted(el)
                        res[(kind, "cover")] += 1
                    elif not closed and d[1] in (A[0], A[2]):
                        res[(kind, "no cover, d1 in {A0,A2}")] += 1
                    else:
                        res[(kind, "NO COVER OTHER")] += 1
                        bad.append((trails, kinds))
    return res, bad


# ----------------------------------------------------------------------------------------
# own implementation of 04d first sweep + 04g section 3

def procedure_C(adj, m, r, s, rng, st):
    V = list(adj)
    rinv = {r[v]: v for v in V}
    key = lambda x: E(x, m[x])
    trails, lab = {}, {}
    for u in V:
        if u < m[u]:
            trails[key(u)] = (s[r[u]], r[u], u, m[u], r[m[u]], s[r[m[u]]])
    for k, t in trails.items():
        x1, x2 = t[1] == t[5], t[0] == t[4]
        if x1 and x2:
            raise Failure("both defects")
        if x1:
            lab[k] = t[0:5]
        elif x2:
            lab[k] = (t[5], t[4], t[3], t[2], t[1])
        elif len(set(t)) != 6:
            raise Failure("Lemma 2")
    target, link = {}, {}
    for k, (a, b, c, d, e) in lab.items():
        tk = key(rinv[c])
        target[k] = tk
        link[k] = 0 if tk not in lab else (1 if lab[tk][1] == c else (2 if lab[tk][4] == c else None))
        if link[k] is None:
            raise Failure("link type")
    succ = {k: target[k] for k in lab if link[k] == 2}
    pred = {}
    for k, t in succ.items():
        if t in pred:
            raise Failure("two incoming type-2 links")
        pred[t] = k
    sources, oddcyc, seen = set(), [], set()
    for k in lab:
        if k in seen:
            continue
        x, walk = k, {k}
        while x in pred and pred[x] not in walk:
            x = pred[x]; walk.add(x)
        if x in pred:
            cyc = [x]; y = succ[x]
            while y != x:
                cyc.append(y); y = succ[y]
            seen.update(cyc)
            if len(cyc) % 2 == 0:
                sources.update(cyc[rng.randrange(2)::2])
            else:
                oddcyc.append(cyc)
        else:
            ch = [x]
            while ch[-1] in succ:
                ch.append(succ[ch[-1]])
            seen.update(ch)
            sources.update(ch[0::2])
    inodd = {k for cy in oddcyc for k in cy}
    st["odd type-2 cycles"] += len(oddcyc)

    # ---- X2 sources and their D-partners
    X2 = {}
    for k in sources:
        a, b, c, d, e = lab[k]
        if s[c] != e:
            continue
        if link[k] not in (0, 1):
            raise Failure("Lemma C2: X2 source with type-2 link")
        dl = rinv[d]; mu = m[dl]; u = r[mu]; W = key(dl)
        if W == k:
            raise Failure("Lemma C3(ii)")
        if W not in lab:
            case = "alpha"
        elif lab[W][1] == d:
            case = "beta"
        elif lab[W][4] == d:
            case = "gamma"
            if W not in sources or W in pred:
                raise Failure("Lemma C3(v): gamma partner not a source / has incoming type-2")
            if s[d] != u:
                raise Failure("gamma: s(d) != u")
        else:
            raise Failure("D-partner defective but d not a red head label")
        X2[k] = dict(a=a, b=b, c=c, d=d, e=e, dl=dl, mu=mu, u=u, W=W, case=case)
        st["X2 " + case] += 1
    # D-chains
    nxt = {k: x["W"] for k, x in X2.items() if x["case"] == "gamma" and x["W"] in X2}
    prv = {}
    for k, w in nxt.items():
        if w in prv:
            raise Failure("D-chain in-degree 2")
        prv[w] = k
        y, z = X2[k], X2[w]
        if not (z["b"] == s[y["d"]] and z["c"] == y["mu"] and z["d"] == y["dl"] and z["e"] == y["d"]):
            raise Failure("Lemma C4 relations")
    cancelled, dcycles, visited = set(), [], set()
    for k0 in set(nxt) | set(nxt.values()):
        if k0 in prv:
            continue
        cur, exists, ln = k0, True, 0
        while True:
            visited.add(cur)
            if not exists:
                cancelled.add(cur)
            if cur not in nxt:
                break
            cur = nxt[cur]; exists = not exists; ln += 1
        st["D-path length %d" % ln] += 1
    for k0 in nxt:
        if k0 in visited:
            continue
        cyc = [k0]
        while nxt[cyc[-1]] != k0:
            cyc.append(nxt[cyc[-1]])
        visited.update(cyc)
        if len(cyc) < 3:
            raise Failure("D-cycle of length < 3")
        dcycles.append(cyc)
        st["D-cycle length %d" % len(cyc)] += 1
    rot = {k for cy in dcycles for k in cy}
    exist = {k for k in X2 if k not in cancelled}
    rule = {}
    for k in exist:
        x = X2[k]
        if k in rot:
            rule[k] = "rotation"
        elif x["case"] in ("alpha", "beta"):
            rule[k] = x["case"]
        elif x["W"] in X2:
            if x["W"] not in cancelled:
                raise Failure("existing X2 with existing X2 gamma-partner outside a D-cycle")
            rule[k] = "absorb"
        elif link[x["W"]] in (0, 1):
            rule[k] = "absorb"
        elif s[x["mu"]] == x["c"]:
            rule[k] = "F"
        else:
            rule[k] = "GammaD"
        st["rule " + rule[k]] += 1
    absorbedW = {X2[k]["W"] for k in exist if rule[k] == "absorb"}
    trading = sources - cancelled - absorbedW
    for k in lab:
        if k in pred and k not in inodd and k not in sources and pred[k] not in trading:
            raise Failure("a recipient lost its source (removed type-2 trade)")
    # pendants
    newA = {}
    for k in trading:
        if link[k] == 1:
            newA[target[k]] = lab[k][1]
    for k in exist:
        if rule[k] == "beta":
            W = X2[k]["W"]
            if W in newA:
                raise Failure("Lemma C3(iv): pendant changed twice")
            newA[W] = X2[k]["e"]
            st["D-pendant"] += 1
            if W in inodd:
                st["D-pendant on odd type-2 cycle"] += 1
    # ends of non-defective trails
    alpha_d = {X2[k]["d"]: k for k in exist if rule[k] == "alpha"}

    def end_value(x):
        kx = key(x)
        rec = kx in lab and lab[kx][2] == x and kx in trading
        lk = x in alpha_d
        if rec and lk:
            raise Failure("end both received and D-linked")
        if rec:
            return r[x]
        if lk:
            return X2[alpha_d[x]]["e"]
        return s[x]

    pieces = {}
    for k, t in trails.items():
        if k in lab:
            continue
        pieces[k] = (end_value(t[1]),) + t[1:5] + (end_value(t[4]),)
    for k, (a, b, c, d, e) in lab.items():
        A = newA.get(k, a)
        if k in trading:
            pieces[k] = (A, b, e, d, c, s[c])
        elif k in inodd:
            continue
        elif k in pred and pred[k] in trading:
            pieces[k] = (A, b, c, d, e, r[e])
        elif k in absorbedW:
            pieces[k] = None          # rebuilt by the absorbing rule
        else:
            raise Failure("defective trail with no role")
    # odd type-2 cycles (04d section 3); D-pendants already applied
    for cy in oddcyc:
        L = len(cy)
        T = [(newA.get(k, lab[k][0]),) + tuple(lab[k][1:]) for k in cy]
        A_ = [x[0] for x in T]; B_ = [x[1] for x in T]; C_ = [x[2] for x in T]; D_ = [x[3] for x in T]
        Eo = [x[4] for x in T]
        loc = set(B_) | set(C_) | set(D_) | set(Eo)
        for i, k in enumerate(cy):
            if k in newA and any(rule.get(t) == "beta" and X2[t]["W"] == k for t in exist):
                if A_[i] in loc:                       # Lemma C6
                    which=[(nm,j) for nm,arr in (("b",B_),("c",C_),("d",D_),("e",Eo)) for j,v in enumerate(arr) if v==A_[i]]
                    print("DIAG L=",L,"i=",i,"pendant",A_[i],"equals",which, "own d_i",D_[i]); print("DIAG trails",T)
                    raise Failure("Lemma C6: D-pendant is a local label")
        if len(set(A_)) != L:
            raise Failure("(o5) on odd cycle")
        tri = lambda i: (lambda x: (x[0], x[1], x[2], x[3], x[4], x[1]))(T[i % L])
        order = list(range(L)) if L > 3 else [0]
        rng.shuffle(order)
        done = False
        for j in order:
            el = [x for t in range(3) for x in edges_of(tri(j + t))]
            cov = path_cover(el, 3)
            if cov is None:
                if L == 3 or D_[(j + 1) % L] not in (A_[j % L], A_[(j + 2) % L]):
                    raise Failure("Lemma 4 (P5) violated on a realized block")
                continue
            for i, p in enumerate(cov):
                pieces[("odd", cy[0], i)] = p
            for t in range(3, L, 2):
                i1, i2 = (j + t) % L, (j + t + 1) % L
                pieces[("odd", cy[0], "p", t, 0)] = (A_[i1], B_[i1], Eo[i1], D_[i1], C_[i1], B_[i2])
                pieces[("odd", cy[0], "p", t, 1)] = (A_[i2], B_[i2], C_[i2], D_[i2], C_[i1], B_[i1])
            done = True
            st["odd type-2 cycle: block"] += 1
            break
        if not done:
            if all(A_[i] == D_[(i + 1) % L] for i in range(L)):
                for i in range(L):
                    pieces[("odd", cy[0], "r", i)] = (A_[i], B_[i], C_[i - 1], D_[i - 1], C_[i - 2], B_[i - 2])
            elif all(A_[i] == D_[(i - 1) % L] for i in range(L)):
                for i in range(L):
                    pieces[("odd", cy[0], "r", i)] = (A_[i], B_[i], C_[i], D_[(i + 1) % L],
                                                       C_[(i + 1) % L], B_[(i + 2) % L])
            else:
                raise Failure("odd type-2 cycle: no block, no uniform rotation")
            st["odd type-2 cycle: rotation"] += 1
    # ---- Proposition C1 on the pieces before the second sweep (excluding absorbed W)
    for k, p in pieces.items():
        if p is None or len(set(p)) == 6:
            continue
        if not (k in X2 and k in trading and p == (p[0], X2[k]["b"], X2[k]["e"], X2[k]["d"], X2[k]["c"], X2[k]["e"])):
            raise Failure("Prop C1: non-simple first-sweep piece that is not an X2 source: %r" % (p,))
    # ---- second sweep
    new = {}

    def expect(k, p):
        if pieces[k] != p:
            raise Failure("piece not of the stated form: %r vs %r" % (pieces[k], p))

    for k in exist:
        x = X2[k]
        a, b, c, d, e, dl, mu, u, W = (x[t] for t in ("a", "b", "c", "d", "e", "dl", "mu", "u", "W"))
        A = newA.get(k, a)
        if rule[k] == "rotation":
            continue
        expect(k, (A, b, e, d, c, e))
        if rule[k] in ("alpha", "beta"):
            new[k] = (s[d], d, c, e, b, A)
        elif rule[k] == "absorb":
            AW = newA.get(W, lab[W][0])
            new[k] = (u, d, c, e, b, A)
            new[W] = (AW, u, mu, dl, d, e)
        elif rule[k] == "GammaD":
            AW = newA.get(W, lab[W][0])
            expect(W, (AW, u, d, dl, mu, s[mu]))
            new[W] = (s[mu], mu, dl, d, c, e)
            new[k] = (A, b, e, d, u, AW)
        else:  # rule F
            AW = newA.get(W, lab[W][0])
            Xk = target[W]
            f = rinv[c]; dX = m[f]
            if Xk != target[k] or link[k] != 1 or Xk != key(f):
                raise Failure("rule F: X is not Q_T with a type-1 link from T")
            expect(W, (AW, u, d, dl, mu, c))
            expect(Xk, (b, c, f, dX, mu, u))
            new[k] = (A, b, c, d, u, AW)
            new[W] = (b, e, d, dl, mu, c)
            new[Xk] = (e, c, f, dX, mu, u)
    for cyc in dcycles:
        L = len(cyc)
        for j, k in enumerate(cyc):
            x, xp, xn = X2[k], X2[cyc[j - 1]], X2[cyc[(j + 1) % L]]
            A = newA.get(k, x["a"])
            expect(k, (A, x["b"], xp["d"], x["d"], x["c"], xp["d"]))
            new[k] = (A, x["b"], xp["d"], x["c"], x["d"], xn["d"])
    for k, p in new.items():
        if k not in pieces:
            raise Failure("rule rebuilt an unknown piece")
        pieces[k] = p
    if any(p is None for p in pieces.values()):
        raise Failure("absorbed trail not rebuilt")
    return list(pieces.values())


def verify_partition(adj, pieces):
    allE = Counter(E(u, v) for u in adj for v in adj[u] if u < v)
    used = Counter()
    for p in pieces:
        if len(p) != 6 or len(set(p)) != 6:
            raise Failure("piece not a simple 5-edge path: %r" % (p,))
        for u, v in zip(p, p[1:]):
            if v not in adj[u]:
                raise Failure("non-edge in %r" % (p,))
        used.update(edges_of(p))
    if used != allE:
        raise Failure("not an exact edge partition")


# ----------------------------------------------------------------------------------------
# planting (P5)-compatible structures

def x2node(P, c=None, d=None, b=None, e=None):
    c = P.new() if c is None else c
    d = P.m.get(c, P.new()) if d is None else d
    b = P.r.get(c, P.new()) if b is None else b
    e = P.r.get(d, P.new()) if e is None else e
    P.setm(c, d); P.setr(c, b); P.setr(d, e); P.sets(e, b); P.sets(c, e)
    return dict(c=c, d=d, b=b, e=e)


def plant(rng, budget):
    P = Plant()
    nodes = []
    ops = ["alpha", "beta", "gamma0", "gamma1", "gamma2", "gammaF", "dpath", "dcycle", "dcycle",
           "oddcyc", "oddcyc", "oddrot", "x2", "attach", "glue_s", "glue_r", "glue_m"]
    for _ in range(budget):
        op = rng.choice(ops)
        try:
            if op == "x2":
                nodes.append(x2node(P))
            elif op == "attach" and P.nv:
                nodes.append(x2node(P, **{rng.choice("cdbe"): rng.randrange(P.nv)}))
            elif op.startswith("glue") and P.nv > 1:
                for _ in range(rng.randint(1, 3)):
                    x, y = rng.sample(range(P.nv), 2)
                    try:
                        {"glue_s": P.sets, "glue_r": P.setr, "glue_m": P.setm}[op](x, y)
                    except ValueError:
                        pass
            elif op in ("alpha", "beta") or op.startswith("gamma"):
                T = x2node(P); nodes.append(T)
                dl, mu = P.new(), P.new()
                P.setr(dl, T["d"]); P.setm(dl, mu)
                if op == "alpha":
                    continue
                u = P.new(); P.setr(mu, u)
                if op == "beta":
                    P.sets(u, T["d"])
                    continue
                P.sets(T["d"], u)
                if op == "gamma1":           # W's target Y defective with b_Y = mu
                    cY, dY, eY = P.new(), P.new(), P.new()
                    P.setr(cY, mu); P.setm(cY, dY); P.setr(dY, eY); P.sets(eY, mu)
                elif op == "gamma2":         # W's target X defective with e_X = mu
                    dX, cX, bX = P.new(), P.new(), P.new()
                    P.setr(dX, mu); P.setm(dX, cX); P.setr(cX, bX); P.sets(mu, bX)
                elif op == "gammaF":         # (F1) s(mu) = c, X = Q_T
                    f, dX = P.new(), P.new()
                    P.setr(f, T["c"]); P.setm(f, dX); P.setr(dX, mu); P.sets(mu, T["c"])
            elif op in ("dpath", "dcycle"):
                L = rng.randint(3, 7) if op == "dcycle" else rng.randint(2, 6)
                ds = [P.new() for _ in range(L)]
                for j in range(L):
                    if op == "dpath" and j == 0:
                        nodes.append(x2node(P, d=ds[0]))
                    else:
                        nodes.append(x2node(P, d=ds[j], e=ds[j - 1]))
            elif op == "oddrot":        # odd type-2 cycle with A_i = d_{i+1} for all i
                L = rng.choice((5, 7))
                c = [P.new() for _ in range(L)]; d = [P.new() for _ in range(L)]; b = [P.new() for _ in range(L)]
                for i in range(L):
                    P.setm(c[i], d[i]); P.setr(c[i], b[i])
                for i in range(L):
                    P.setr(d[i], c[(i - 1) % L]); P.sets(c[(i - 1) % L], b[i])
                for i in range(L):
                    if rng.random() < 0.5:
                        P.sets(b[i], d[(i + 1) % L])
                    else:                         # changed pendant r(b_i) = d_{i+1} via a type-1 source
                        P.setr(b[i], d[(i + 1) % L])
                        ds, es = P.new(), P.new()
                        P.setm(b[i], ds); P.setr(ds, es); P.sets(es, d[(i + 1) % L])
            elif op == "oddcyc":
                L = rng.choice((3, 3, 5, 7))
                c = [P.new() for _ in range(L)]; d = [P.new() for _ in range(L)]; b = [P.new() for _ in range(L)]
                for i in range(L):
                    P.setm(c[i], d[i]); P.setr(c[i], b[i])
                for i in range(L):
                    P.setr(d[i], c[(i - 1) % L]); P.sets(c[(i - 1) % L], b[i])
                for i in range(L):
                    x = rng.random()
                    if x < 0.35:                  # D-pendant: X2 with d-label b_i (case beta)
                        nodes.append(x2node(P, d=b[i]))
                    elif x < 0.55:                # type-1 source with c-label b_i
                        bs, ds, es = P.new(), P.new(), P.new()
                        P.setr(b[i], bs); P.setm(b[i], ds); P.setr(ds, es); P.sets(es, bs)
        except (ValueError, KeyError):
            continue
    return P


CONTROL = False


def complete_and_repair_p5(P, rng, extra, iters):
    n = P.nv + extra
    n += n % 2
    V = list(range(n))
    m, r, s = dict(P.m), dict(P.r), dict(P.s)
    free = [v for v in V if v not in m]
    rng.shuffle(free)
    for i in range(0, len(free), 2):
        m[free[i]], m[free[i + 1]] = free[i + 1], free[i]
    mfree = [E(free[i], free[i + 1]) for i in range(0, len(free), 2)]
    rdom = [v for v in V if v not in r]
    rcod = [v for v in V if v not in set(r.values())]
    rng.shuffle(rcod); r.update(zip(rdom, rcod))
    sdom = [v for v in V if v not in s]
    scod = [v for v in V if v not in set(s.values())]
    rng.shuffle(scod); s.update(zip(sdom, scod))

    def bad():
        b = 0
        cnt = Counter()
        rinv = {y: x for x, y in r.items()}
        for v in V:
            if r[v] == v or s[v] == v:
                b += 3
            cnt[E(v, r[v])] += 1; cnt[E(v, s[v])] += 1
            if v < m[v]:
                cnt[E(v, m[v])] += 1
            b += (r[r[v]] == v) + (s[s[v]] == v) + (s[r[v]] == m[v]) + ((m[rinv[v]] == r[v]) and not CONTROL)
        return b + 2 * sum(x - 1 for x in cnt.values())

    cur = bad()
    for _ in range(iters):
        if cur == 0:
            break
        x = rng.random()
        if x < 0.45 and len(rdom) > 1:
            a, b_ = rng.sample(rdom, 2)
            r[a], r[b_] = r[b_], r[a]
            nb = bad()
            if nb <= cur or rng.random() < 0.01:
                cur = nb
            else:
                r[a], r[b_] = r[b_], r[a]
        elif x < 0.9 and len(sdom) > 1:
            a, b_ = rng.sample(sdom, 2)
            s[a], s[b_] = s[b_], s[a]
            nb = bad()
            if nb <= cur or rng.random() < 0.01:
                cur = nb
            else:
                s[a], s[b_] = s[b_], s[a]
        elif len(mfree) > 1:
            i, j = rng.sample(range(len(mfree)), 2)
            (a, b_), (c, d) = mfree[i], mfree[j]
            m[a], m[c], m[b_], m[d] = c, a, d, b_
            nb = bad()
            if nb <= cur or rng.random() < 0.01:
                cur = nb; mfree[i], mfree[j] = E(a, c), E(b_, d)
            else:
                m[a], m[b_], m[c], m[d] = b_, a, d, c
    if cur:
        return None
    adj = {v: set() for v in V}
    for v in V:
        for w in (m[v], r[v], s[v]):
            adj[v].add(w); adj[w].add(v)
    if any(len(adj[v]) != 5 for v in V) or (not CONTROL and not p5_ok(m, r)):
        return None
    check_P(adj, m, r, s)
    return adj, m, r, s


# ----------------------------------------------------------------------------------------

def check_instance(adj, m, r, s, rng, stats, tag):
    check_P(adj, m, r, s)
    if not CONTROL:
        assert p5_ok(m, r)
    elif p5_ok(m, r):
        stats[(tag, "control instance happens to satisfy (P5)")] += 1
    # Proposition C1 with the Theorem A referee's own first sweep
    st1 = Counter()
    try:
        pcs = first_sweep(adj, m, r, s, rng, st1, False)
    except (SweepFailure, AssertionError) as ex:
        raise Failure("A-referee first sweep: %s" % (ex,))
    if st1["Lemma4 realized: closed block without cover"] or st1["Lemma4 realized: open block failing OTHER"]:
        raise Failure("Lemma 4 under (P5) fails on a realized block")
    for tg, p in pcs:
        if len(set(p)) != 6:
            A, b, e, d, c, e2 = p
            if not (tg == "source" and e == e2 and s[c] == e and r[c] == b and r[d] == e and m[c] == d):
                raise Failure("Prop C1 (A-referee sweep): non-X2 defect %s %r" % (tg, p))
            stats[(tag, "first-sweep X2 sources")] += 1
    st = Counter()
    out = procedure_C(adj, m, r, s, rng, st)
    verify_partition(adj, out)
    stats[(tag, "verified decompositions")] += 1
    for k, v in st.items():
        stats[(tag, k)] += v
        stats[("ALL", k)] += v


def main():
    ap = ArgumentParser()
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--planted", type=int, default=None)
    ap.add_argument("--graphs", type=int, default=None)
    ap.add_argument("--skip-lemma", action="store_true")
    ap.add_argument("--control", action="store_true", help="drop (P5) from the generic data (sensitivity test; failures expected)")
    args = ap.parse_args()
    global CONTROL
    CONTROL = args.control
    rng = Random(args.seed)
    t0 = time.time()
    nfail = 0
    if not args.skip_lemma:
        print("== Lemma 4 under (P5), own enumeration ==", flush=True)
        res, bad = lemma4_p5()
        for k in sorted(res, key=str):
            print("  ", k, res[k])
        nfail += len(bad)
    stats, fails = Counter(), []
    npl = args.planted if args.planted is not None else (200 if args.quick else 1200)
    print("== planted generic (M,r,s) with (P1)-(P3)+(P5) ==", flush=True)
    for _ in range(npl):
        P = plant(rng, rng.randint(1, 6))
        inst = complete_and_repair_p5(P, rng, rng.choice((4, 8, 14)), 4000 if args.quick else 8000)
        if inst is None:
            stats[("planted", "repair failed (skipped)")] += 1
            continue
        adj, m, r, s = inst
        try:
            check_instance(adj, m, r, s, rng, stats, "planted")
        except (Failure, AssertionError, KeyError) as ex:
            stats[("planted", "FAILURE " + str(ex)[:90])] += 1
            fails.append((adj, m, r, s, str(ex)))
    print("== graphs: Lemma 1 constructions satisfying (P5) ==", flush=True)
    from check_regular_path_theoremBprime_independent import graph_instance
    ng = args.graphs if args.graphs is not None else (3 if args.quick else 10)
    for fam, orders in (("circulant", (12, 16, 20, 24)), ("K5blocks", (10, 20, 30))):
        for n in orders:
            for _ in range(ng):
                inst = graph_instance(n, rng, fam, hyp=False, quick=True)
                if inst is None:
                    continue
                adj, m = inst
                stats[(fam, "graphs")] += 1
                found = 0
                for _ in range(150):
                    r, s = lemma1(adj, m, rng)
                    if not p5_ok(m, r):
                        continue
                    found += 1
                    try:
                        check_instance(adj, m, r, s, rng, stats, fam)
                    except (Failure, AssertionError, KeyError) as ex:
                        stats[(fam, "FAILURE " + str(ex)[:90])] += 1
                        fails.append((adj, m, r, s, str(ex)))
                    if found >= 4:
                        break
    for k in sorted(stats, key=str):
        print("  ", k, stats[k])
    nfail += len(fails)
    if fails:
        import pickle
        with open("04-handoff/review-theoremC/failures.pkl", "wb") as fh:
            pickle.dump(fails[:50], fh)
    print("elapsed %.0fs" % (time.time() - t0))
    print("ALL CHECKS PASSED" if nfail == 0 else "FAILURES: %d" % nfail)
    return 1 if nfail else 0


if False:
    sys.setrecursionlimit(10000)
    sys.exit(main())
