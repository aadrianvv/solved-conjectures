"""Independent referee checker for Theorem B of 04e-regular-path-diamond-free.md.

Written from the text of 04d (Lemma 1, sweep, Section 3) and 04e (Lemma 5, the rules of
Section 3 of 04e, the Gtarget resolution, the rotation, Lemma 7) only.  It does not import
or copy check_regular_path_diamond_free.py, check_regular_path_gsweep.py,
check_regular_path_label_engine.py or check_regular_path_sweep_pipeline.py.  It reuses the
Lemma 1 construction, (P1)-(P3) check and exact path cover of the previous referee's
check_regular_path_theoremA_independent.py (audited for that purpose).

Parts
  lemma4p   own enumeration of Lemma 4' (odd type-2 triples, diamond-free, with
            G-pendants allowed as Lemma 7 permits).
  graphs    random diamond-free 5-regular graphs (several triangle-rich families), Lemma 1
            constructions, full procedure, exact verification.
  planted   generic (M, r, s) data satisfying only (P1)-(P3) and diamond-freeness, with
            planted G-configurations of every case: alpha (with alpha-links and two partner
            ends), beta (also on odd type-2 cycles), gamma with type-0/1/2 links, beta and
            gamma at one W0, Gtarget paths and cycles of length 2..7, with and without (F1).
Every output is checked to be an exact partition of E(G) into simple five-edge paths.
Random runs are evidence, not proof.

Usage: python check_regular_path_theoremB_independent.py [--quick] [--seed N]
"""

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from itertools import product
from random import Random

from check_regular_path_theoremA_independent import lemma1, check_P, path_cover


def E(u, v):
    return (u, v) if u < v else (v, u)


def edges_of(seq):
    return [E(seq[i], seq[i + 1]) for i in range(len(seq) - 1)]


class Failure(Exception):
    pass


def diamond_free(adj):
    return all(len(adj[u] & adj[v]) <= 1 for u in adj for v in adj[u])


# ----------------------------------------------------------------------------------------
# the procedure (04d sweep + 04e second sweep), from the text

def procedure(adj, m, r, s, rng, st, odd_pick="random"):
    V = list(adj)
    rinv = {r[v]: v for v in V}

    def key(x):
        return E(x, m[x])

    trails = {}
    for u in V:
        if u < m[u]:
            trails[key(u)] = (s[r[u]], r[u], u, m[u], r[m[u]], s[r[m[u]]])
    lab = {}                       # defective: (a, b, c, d, e) with repetition at b
    for k, t in trails.items():
        x1, x2 = t[1] == t[5], t[0] == t[4]
        if x1 and x2:
            raise Failure("both defects")
        if x1:
            lab[k] = t[0:5]
        elif x2:
            lab[k] = (t[5], t[4], t[3], t[2], t[1])
        elif len(set(t)) != 6:
            raise Failure("Lemma 2 violated")
    for k, (a, b, c, d, e) in lab.items():
        assert b == r[c] and e == r[d] and a == s[b] and s[e] == b and m[c] == d
    # links
    target, link = {}, {}
    for k, (a, b, c, d, e) in lab.items():
        tk = key(rinv[c])
        target[k] = tk
        if tk not in lab:
            link[k] = 0
        elif lab[tk][1] == c:
            link[k] = 1
        elif lab[tk][4] == c:
            link[k] = 2
        else:
            raise Failure("link of unknown type")
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
            x = pred[x]
            walk.add(x)
        if x in pred:
            cyc = [x]
            y = succ[x]
            while y != x:
                cyc.append(y)
                y = succ[y]
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

    # ---- G-configurations (Proposition B): source, type-0 link, m(f) = b
    G = {}
    for k in sources:
        if link[k] != 0:
            continue
        a, b, c, d, e = lab[k]
        f = rinv[c]
        if m[f] != b:
            continue
        p = rinv[f]
        q = m[p]
        W0 = key(p)
        if W0 == k:
            raise Failure("Lemma 5(iii): W0 = T")
        if W0 not in lab:
            case = "alpha"
        elif lab[W0][1] == f:
            case = "beta"
        elif lab[W0][4] == f:
            case = "gamma"
        else:
            raise Failure("Lemma 5(ii): W0 defective but f not a red head label")
        G[c] = dict(T=k, a=a, b=b, d=d, e=e, f=f, h=r[b], g=s[f], p=p, q=q, u=r[q], W0=W0, case=case)
        st["G-config " + case] += 1
    for c, g in G.items():
        if g["case"] == "gamma":
            if g["W0"] not in sources:
                raise Failure("Lemma 5 gamma: W0 not a source")
            if g["g"] != g["u"]:
                raise Failure("gamma: s(f) != r(q)")
            if lab[g["W0"]][2] != g["q"]:
                raise Failure("gamma: c-label of W0 is not q")
        if g["case"] == "beta" and s[g["u"]] != g["f"]:
            raise Failure("beta: s(u) != f")
    # Gtarget edges c -> c*
    gt = {}
    for c, g in G.items():
        if g["case"] == "gamma" and link[g["W0"]] == 0 and g["q"] in G:
            gt[c] = g["q"]
            assert G[g["q"]]["T"] == g["W0"]
    gpred = {}
    for c, cs in gt.items():
        if cs in gpred:
            raise Failure("Gtarget in-degree 2")
        gpred[cs] = c
    st["Gtarget edges"] += len(gt)
    cancelled, absorb_cfg, gamma_cfg = set(), set(), set()
    visited = set()
    nodes = set(gt) | set(gt.values())
    for c0 in nodes:
        if c0 in gpred:
            continue
        cur, exists, ln = c0, True, 0
        while cur in gt:
            visited.add(cur)
            if exists:
                absorb_cfg.add(cur)
                cancelled.add(gt[cur])
            exists = not exists
            cur = gt[cur]
            ln += 1
        visited.add(cur)
        st["Gtarget path length %d" % ln] += 1
    odd_gt = []
    for c0 in nodes:
        if c0 in visited:
            continue
        cyc = [c0]
        while gt[cyc[-1]] != c0:
            cyc.append(gt[cyc[-1]])
        visited.update(cyc)
        st["Gtarget cycle length %d" % len(cyc)] += 1
        if len(cyc) % 2 == 0:
            off = rng.randrange(2)
            for i in range(off, len(cyc) + off, 2):
                absorb_cfg.add(cyc[i % len(cyc)])
                cancelled.add(cyc[(i + 1) % len(cyc)])
        else:
            odd_gt.append(cyc)
    # gamma configurations outside odd Gtarget cycles
    odd_nodes = {c for cy in odd_gt for c in cy}
    for c, g in G.items():
        if g["case"] != "gamma" or c in cancelled or c in odd_nodes:
            continue
        if c in gt:
            assert c in absorb_cfg
            continue
        if link[g["W0"]] == 2:
            gamma_cfg.add(c)
        else:
            absorb_cfg.add(c)
            st["absorption, type-%d link" % link[g["W0"]]] += 1
    exist = lambda c: c in G and c not in cancelled
    absorbedW0 = {G[c]["W0"]: c for c in absorb_cfg}
    # pendants (type-1 changes from trading sources; G-pendants of existing beta configs)
    trading0 = sources - set(absorbedW0)

    def pendants(trading):
        A = {}
        for k in trading:
            if link[k] == 1:
                tk = target[k]
                A[tk] = lab[k][1]
                assert r[lab[tk][1]] == lab[k][1]
        for c, g in G.items():
            if exist(c) and g["case"] == "beta":
                if g["W0"] in A:
                    raise Failure("Lemma 5 beta: W0 pendant also type-1 changed")
                A[g["W0"]] = g["b"]
                st["G-pendant"] += 1
        return A

    newA = pendants(trading0)
    # odd Gtarget cycles
    rotations = []
    for cyc in odd_gt:
        L = len(cyc)
        valid = []
        for j, cj in enumerate(cyc):
            g = G[cj]
            Ap = newA.get(g["W0"], lab[g["W0"]][0])
            if Ap != lab[g["W0"]][0]:
                raise Failure("odd Gtarget node with a changed pendant (04e claims impossible)")
            if not (s[g["q"]] == cj and Ap != g["h"]):
                valid.append(j)
        if valid:
            j = rng.choice(valid) if odd_pick == "random" else valid[0]
            gamma_cfg.add(cyc[j])
            for t in range(1, L, 2):
                absorb_cfg.add(cyc[(j + t) % L])
                cancelled.add(cyc[(j + t + 1) % L])
            st["odd Gtarget cycle: Gamma at a node"] += 1
        else:
            rotations.append(cyc)
            st["odd Gtarget cycle: ROTATION"] += 1
    absorbedW0 = {G[c]["W0"]: c for c in absorb_cfg}
    for c in absorb_cfg:
        assert exist(c) and G[c]["case"] == "gamma"
    trading = sources - set(absorbedW0)
    newA2 = pendants(trading)
    if newA2 != newA:
        raise Failure("pendants depend on odd-cycle choice")
    newA = newA2
    for c, g in G.items():
        if exist(c):
            st["existing config " + g["case"]] += 1
    st["cancelled configurations"] += len(cancelled)
    rot_nodes = {c for cy in rotations for c in cy}

    # end values of non-defective canonical trails
    alpha_f = {G[c]["f"]: c for c in G if exist(c) and G[c]["case"] == "alpha"}

    def recv_source(x):
        k = key(x)
        return k in lab and lab[k][2] == x and k in trading and link[k] == 0

    def end_value(x):
        rec = recv_source(x)
        lk = x in alpha_f
        if rec and lk:
            raise Failure("end both received and alpha-partner")
        if rec:
            st["received ends"] += 1
            return r[x]
        if lk:
            return G[alpha_f[x]]["b"]
        return s[x]

    pieces = {}      # name -> piece
    q_of = {key(G[c]["f"]): c for c in G if exist(c)}
    partner_ends = Counter()
    for c in alpha_f.values():
        partner_ends[G[c]["W0"]] += 1
    for k, cnt in partner_ends.items():
        st["alpha partner with %d partner ends" % cnt] += 1
    for k, t in trails.items():
        if k in lab:
            continue
        x0, x1, x2, x3, x4, x5 = t
        left, right = end_value(x1), end_value(x4)
        if k in q_of:
            c = q_of[k]
            g = G[c]
            if x1 == c:
                Y = right
            else:
                assert x4 == c
                Y = left
            g["Y"] = Y
            if Y != s[g["h"]]:
                st["Q_c with changed h-end (%s)" % ("received" if Y == r[g["h"]] else "alpha-link")] += 1
            continue
        pieces[("trail", k)] = (left, x1, x2, x3, x4, right)
    # defective trails
    for k, (a, b, c, d, e) in lab.items():
        A = newA.get(k, a)
        if k in absorbedW0:
            cc = absorbedW0[k]
            pieces[("trail", k)] = (A, b, c, d, e, G[cc]["b"])
        elif k in trading:
            pieces[("trail", k)] = (A, b, e, d, c, s[c])
        elif k in inodd:
            continue
        else:
            if not (k in pred and pred[k] in trading):
                raise Failure("recipient without trading source")
            pieces[("trail", k)] = (A, b, c, d, e, r[e])
    # odd type-2 cycles: 04d Section 3
    for cy in oddcyc:
        L = len(cy)
        T = [(newA.get(k, lab[k][0]),) + tuple(lab[k][1:]) for k in cy]
        for i in range(L):
            assert T[i][2] == T[(i + 1) % L][4]
        Gp = [newA.get(k) is not None and any(exist(c) and G[c]["W0"] == k and G[c]["case"] == "beta" for c in G)
              for k in cy]
        if any(Gp):
            st["odd type-2 cycle with G-pendant"] += 1
            locals_ = {x for t in T for x in t[1:]}
            for i in range(L):
                if Gp[i] and T[i][0] in locals_:
                    raise Failure("Lemma 7 violated")

        def tri(i):
            x = T[i % L]
            return (x[0], x[1], x[2], x[3], x[4], x[1])

        order = list(range(L)) if L > 3 else [0]
        rng.shuffle(order)
        done = False
        for j in order:
            el = [x for t in range(3) for x in edges_of(tri(j + t))]
            if len(set(el)) != 15:
                raise Failure("odd cycle block edges")
            cov = path_cover(el, 3)
            if cov is None:
                continue
            for i, p in enumerate(cov):
                pieces[("odd", cy[0], "blk", i)] = p
            for t in range(3, L, 2):
                i1, i2 = (j + t) % L, (j + t + 1) % L
                Ai, bi, ci, di, ei = T[i1]
                Aj, bj, cj, dj, ej = T[i2]
                pieces[("odd", cy[0], "pair", t, 0)] = (Ai, bi, ei, di, ci, bj)
                pieces[("odd", cy[0], "pair", t, 1)] = (Aj, bj, cj, dj, ci, bi)
            done = True
            st["odd type-2 cycle: block"] += 1
            break
        if not done:
            if L == 3:
                raise Failure("closed odd triple without cover")
            A_ = [x[0] for x in T]; B_ = [x[1] for x in T]; C_ = [x[2] for x in T]; D_ = [x[3] for x in T]
            if all(A_[i] == D_[(i + 1) % L] for i in range(L)):
                for i in range(L):
                    pieces[("odd", cy[0], "rot", i)] = (A_[i], B_[i], C_[(i - 1) % L], D_[(i - 1) % L],
                                                       C_[(i - 2) % L], B_[(i - 2) % L])
            elif all(A_[i] == D_[(i - 1) % L] for i in range(L)):
                for i in range(L):
                    pieces[("odd", cy[0], "rot", i)] = (A_[i], B_[i], C_[i], D_[(i + 1) % L],
                                                       C_[(i + 1) % L], B_[(i + 2) % L])
            else:
                raise Failure("odd type-2 cycle: no block, no uniform rotation")
            st["odd type-2 cycle: rotation"] += 1

    # ---- second sweep
    for c, g in G.items():
        if not exist(c) or c in rot_nodes:
            continue
        f, b, h, gg, Y = g["f"], g["b"], g["h"], g["g"], g["Y"]
        if c in gamma_cfg:
            wkey = ("trail", g["W0"])
            W = pieces[wkey]
            # source piece (A', g, f, p, q, s(q))
            if not (W[1] == gg and W[2] == f and W[3] == g["p"] and W[4] == g["q"] and W[5] == s[g["q"]]):
                raise Failure("Gamma: W is not (A',g,f,p,q,s(q))")
            Ap = W[0]
            if Ap == h:
                pieces[wkey] = (h, b, f, g["p"], g["q"], s[g["q"]])
                pieces[("Q", c)] = (Y, h, gg, f, c, b)
                st["Gamma' used"] += 1
            else:
                pieces[wkey] = (s[g["q"]], g["q"], g["p"], f, c, b)
                pieces[("Q", c)] = (Y, h, b, f, gg, Ap)
                st["Gamma used (%s)" % ("Gtarget" if c in gt else "type-2")] += 1
        else:
            pieces[("Q", c)] = (gg, f, c, b, h, Y)
    for cyc in rotations:
        L = len(cyc)
        newp = {}
        for k, c in enumerate(cyc):
            g = G[c]
            n1, n2 = cyc[(k + 1) % L], cyc[(k + 2) % L]
            wkey = ("trail", g["W0"])
            W = pieces[wkey]
            if not (W[1] == G[n1]["b"] and W[2] == g["f"] and W[3] == g["p"] and W[4] == n1 and W[5] == c):
                raise Failure("rotation: W_k not of the stated form")
            newp[wkey] = (g["b"], c, g["f"], g["p"], n1, n2)
            newp[("Q", c)] = (g["Y"], g["h"], g["b"], g["f"], G[n1]["b"], W[0])
        pieces.update(newp)
    return list(pieces.items())


def verify(adj, pieces):
    allE = Counter(E(u, v) for u in adj for v in adj[u] if u < v)
    used = Counter()
    for name, p in pieces:
        if len(p) != 6:
            raise Failure("wrong length %r" % (p,))
        for u, v in zip(p, p[1:]):
            if v not in adj[u]:
                raise Failure("non-edge in %r %r" % (name, p))
        used.update(edges_of(p))
        if len(set(p)) != 6:
            raise Failure("non-simple piece %r %r" % (name, p))
    if used != allE:
        raise Failure("not an exact edge partition")


# ----------------------------------------------------------------------------------------
# Part 1: Lemma 4' own enumeration

def lemma4_prime():
    """Triples of an odd type-2 cycle; pendant kinds u (unchanged), c (type-1 changed),
    G (G-pendant m(b_i)).  Lemma 7: a G-pendant avoids every local b,c,d,e label and every
    changed pendant; it may coincide with another trail's fresh unchanged pendant.  Local
    diamonds are excluded.  Claim: simple cover unless open and d1 in {A0, A2}."""
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
            for kinds in product("ucG", repeat=3):
                opts = []
                for i in range(3):
                    if kinds[i] == "u":
                        opts.append(sorted(present - {c[i], e[i], d[i]}) + ["F%d" % i])
                    elif kinds[i] == "c":
                        opts.append(sorted(present - ce) + ["F%d" % i])
                    else:
                        opts.append(["N%d" % i] + ["F%d" % j for j in range(3) if j != i])
                for A in product(*opts):
                    ok = True
                    for i in range(3):
                        for j in range(i):
                            if A[i] == A[j]:
                                # only a G-pendant equal to a fresh unchanged pendant
                                pair = {kinds[i], kinds[j]}
                                if not (pair == {"G", "u"} and A[i].startswith("F")
                                        and (kinds[int(A[i][1])] == "u")):
                                    ok = False
                    for i in range(3):
                        if A[i].startswith("F") and int(A[i][1]) != i and kinds[i] != "G":
                            ok = False
                        if kinds[i] == "G" and A[i].startswith("F") and kinds[int(A[i][1])] != "u":
                            ok = False
                        if kinds[i] == "G" and A[i].startswith("F") and A[int(A[i][1])] != A[i]:
                            ok = False
                    if not ok:
                        continue
                    trails = [(A[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
                    el = [x for t in trails for x in edges_of(t)]
                    if len(set(el)) != 15:
                        continue
                    nb = defaultdict(set)
                    for u, v in el:
                        nb[u].add(v); nb[v].add(u)
                    if any(len(nb[u] & nb[v]) >= 2 for u, v in el):
                        res["excluded (local diamond)"] += 1
                        continue
                    kind = "closed" if closed else "open"
                    hasG = "G" in kinds
                    cov = path_cover(el, 3)
                    if cov is not None:
                        assert sorted(x for p in cov for x in edges_of(p)) == sorted(el)
                        assert all(len(set(p)) == 6 for p in cov)
                        res[(kind, "G" if hasG else "noG", "cover")] += 1
                    else:
                        okx = (not closed) and d[1] in (A[0], A[2])
                        res[(kind, "G" if hasG else "noG", "no cover, d1 in {A0,A2}" if okx else "NO COVER OTHER")] += 1
                        if not okx:
                            bad.append((trails, kinds))
    return res, bad


# ----------------------------------------------------------------------------------------
# generic data: planting + completion + repair

class Plant:
    def __init__(self):
        self.m, self.r, self.s = {}, {}, {}
        self.ri, self.si = {}, {}
        self.nv = 0

    def new(self):
        self.nv += 1
        return self.nv - 1

    def setr(self, x, y):
        if x == y or self.r.get(x, y) != y or self.ri.get(y, x) != x:
            raise ValueError
        self.r[x] = y; self.ri[y] = x

    def sets(self, x, y):
        if x == y or self.s.get(x, y) != y or self.si.get(y, x) != x:
            raise ValueError
        self.s[x] = y; self.si[y] = x

    def setm(self, x, y):
        if x == y or self.m.get(x, y) != y or self.m.get(y, x) != x:
            raise ValueError
        self.m[x] = y; self.m[y] = x

    def get_or_new(self, fn, x):
        d = getattr(self, fn)
        if x in d:
            return d[x]
        y = self.new()
        {"r": self.setr, "s": self.sets, "m": self.setm}[fn](x, y)
        return y

    def config(self, c=None, d=None, b=None, e=None, f=None):
        """G-configuration skeleton: m(c)=d, r(c)=b, r(d)=e, s(e)=b, r(f)=c, m(f)=b."""
        c = self.new() if c is None else c
        d = self.m.get(c, self.new()) if d is None else d
        b = self.r.get(c, self.new()) if b is None else b
        e = self.r.get(d, self.new()) if e is None else e
        f = self.ri.get(c, self.new()) if f is None else f
        self.setm(c, d); self.setr(c, b); self.setr(d, e); self.sets(e, b)
        self.setr(f, c); self.setm(f, b)
        self.get_or_new("r", b)          # h
        return dict(c=c, d=d, b=b, e=e, f=f)


def plant_random(rng, budget):
    P = Plant()
    cfgs = []
    ops = ["alpha", "beta", "gamma0", "gamma1", "gamma2", "gtpath", "gtcycle", "gtcycleF1",
           "alink", "beta_gamma", "alpha2", "oddbeta", "free", "attach", "attach",
           "glue_s", "glue_s", "glue_r", "glue_m"]
    for _ in range(budget):
        op = rng.choice(ops)
        try:
            if op == "free" and cfgs:
                cfgs.append(P.config())
            elif op == "attach" and P.nv:
                x = rng.randrange(P.nv)
                role = rng.choice(("f", "e", "c", "b", "d"))
                cfgs.append(P.config(**{role: x}))
            elif op.startswith("glue") and P.nv > 1:
                for _ in range(rng.randint(1, 3)):
                    x, y = rng.sample(range(P.nv), 2)
                    try:
                        {"glue_s": P.sets, "glue_r": P.setr, "glue_m": P.setm}[op](x, y)
                    except ValueError:
                        pass
            elif op == "alpha":
                g = P.config(); p = P.new(); P.setr(p, g["f"]); P.setm(p, P.new()); cfgs.append(g)
            elif op == "beta":
                g = P.config(); p = P.new(); q = P.new(); P.setr(p, g["f"]); P.setm(p, q)
                u = P.new(); P.setr(q, u); P.sets(u, g["f"]); cfgs.append(g)
            elif op.startswith("gamma"):
                g = P.config(); p = P.new(); q = P.new(); P.setr(p, g["f"]); P.setm(p, q)
                gg = P.new(); P.sets(g["f"], gg); P.setr(q, gg)
                if op == "gamma2":       # W0's target X defective with e_X = q
                    dX, cX, bX = P.new(), P.new(), P.new()
                    P.setr(dX, q); P.setm(dX, cX); P.setr(cX, bX); P.sets(q, bX)
                elif op == "gamma1":     # X defective with b_X = q
                    cX = P.new(); P.setr(cX, q); dX = P.new(); P.setm(cX, dX)
                    eX = P.new(); P.setr(dX, eX); P.sets(eX, q)
                cfgs.append(g)
            elif op in ("gtpath", "gtcycle", "gtcycleF1"):
                L = rng.randint(2, 7)
                fs = [P.new() for _ in range(L)]
                ks = []
                for k in range(L):
                    e = fs[k - 1] if (op != "gtpath" or k > 0) else None
                    g = P.config(e=e, f=fs[k])
                    ks.append(g)
                if op == "gtpath":
                    # last node gets a random case partner
                    pass
                if op == "gtcycleF1":
                    for k in range(L):
                        P.sets(ks[(k + 1) % L]["c"], ks[k]["c"])
                cfgs.extend(ks)
            elif op == "alink" and cfgs:
                g = rng.choice(cfgs)
                h = P.r[g["b"]]
                cfgs.append(P.config(f=h))
            elif op == "beta_gamma":
                # W0 = (g, f, p, q, u, f): beta for c, gamma for c2 with f2 = u
                g = P.config(); p = P.new(); q = P.new(); P.setr(p, g["f"]); P.setm(p, q)
                u = P.new(); P.setr(q, u); P.sets(u, g["f"])
                cfgs.append(g)
                cfgs.append(P.config(f=u))
            elif op == "alpha2":
                g = P.config(); p = P.new(); q = P.new(); P.setr(p, g["f"]); P.setm(p, q)
                cfgs.append(g)
                u = P.get_or_new("r", q)
                cfgs.append(P.config(f=u))
            elif op == "oddbeta":
                L = rng.choice((3, 5, 7))
                c = [P.new() for _ in range(L)]
                d = [P.new() for _ in range(L)]
                b = [P.new() for _ in range(L)]
                for i in range(L):
                    P.setm(c[i], d[i]); P.setr(c[i], b[i])
                for i in range(L):
                    P.setr(d[i], c[(i - 1) % L]); P.sets(c[(i - 1) % L], b[i])
                for i in range(L):
                    if rng.random() < 0.6:
                        cfgs.append(P.config(f=b[i]))
        except (ValueError, KeyError):
            continue            # partial facts already set are still consistent facts
    return P


def complete_and_repair(P, rng, extra, iters=6000):
    n = P.nv + extra
    if n % 2:
        n += 1
    V = list(range(n))
    m, r, s = dict(P.m), dict(P.r), dict(P.s)
    free = [v for v in V if v not in m]
    rng.shuffle(free)
    for i in range(0, len(free), 2):
        m[free[i]], m[free[i + 1]] = free[i + 1], free[i]
    rdom = [v for v in V if v not in r]
    rcod = [v for v in V if v not in set(r.values())]
    rng.shuffle(rcod)
    r.update(zip(rdom, rcod))
    sdom = [v for v in V if v not in s]
    scod = [v for v in V if v not in set(s.values())]
    rng.shuffle(scod)
    s.update(zip(sdom, scod))

    def violations():
        bad = 0
        cnt = Counter()
        for v in V:
            if r[v] == v or s[v] == v:
                bad += 3
            cnt[E(v, r[v])] += 1
            cnt[E(v, s[v])] += 1
            if v < m[v]:
                cnt[E(v, m[v])] += 1
            if r[r[v]] == v or s[s[v]] == v:
                bad += 1
            if s[r[v]] == m[v]:
                bad += 1
        bad += sum(x - 1 for x in cnt.values()) * 2
        adj = defaultdict(set)
        for u, v in cnt:
            if u != v:
                adj[u].add(v); adj[v].add(u)
        for u, v in cnt:
            if u != v and len(adj[u] & adj[v]) >= 2:
                bad += 1
        return bad

    cur = violations()
    for _ in range(iters):
        if cur == 0:
            break
        if rng.random() < 0.5 and len(rdom) > 1:
            x, y = rng.sample(rdom, 2)
            r[x], r[y] = r[y], r[x]
            nb = violations()
            if nb <= cur or rng.random() < 0.01:
                cur = nb
            else:
                r[x], r[y] = r[y], r[x]
        elif len(sdom) > 1:
            x, y = rng.sample(sdom, 2)
            s[x], s[y] = s[y], s[x]
            nb = violations()
            if nb <= cur or rng.random() < 0.01:
                cur = nb
            else:
                s[x], s[y] = s[y], s[x]
    if cur:
        return None
    adj = {v: set() for v in V}
    for v in V:
        for w in (m[v], r[v], s[v]):
            adj[v].add(w); adj[w].add(v)
    if any(len(adj[v]) != 5 for v in V) or not diamond_free(adj):
        return None
    check_P(adj, m, r, s)
    return adj, m, r, s


# ----------------------------------------------------------------------------------------
# diamond-free graph families

def random_regular(n, d, rng, tries=200):
    for _ in range(tries):
        stubs = [v for v in range(n) for _ in range(d)]
        rng.shuffle(stubs)
        adj = {v: set() for v in range(n)}
        ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or b in adj[a]:
                ok = False
                break
            adj[a].add(b); adj[b].add(a)
        if ok:
            return adj
    return None


def triangle_count(adj):
    return sum(len(adj[u] & adj[v]) for u in adj for v in adj[u] if u < v) // 3


def anneal_triangles(adj, rng, steps):
    """Degree-preserving switches, keeping diamond-freeness, favouring many triangles."""
    es = [E(u, v) for u in adj for v in adj[u] if u < v]
    for _ in range(steps):
        i, j = rng.randrange(len(es)), rng.randrange(len(es))
        (a, b), (c, d) = es[i], es[j]
        if len({a, b, c, d}) < 4:
            continue
        if rng.random() < 0.5:
            c, d = d, c
        if c in adj[a] or d in adj[b]:
            continue
        before = len(adj[a] & adj[b]) + len(adj[c] & adj[d])
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        after = len(adj[a] & adj[c]) + len(adj[b] & adj[d])
        loc = {a, b, c, d} | adj[a] | adj[b] | adj[c] | adj[d]
        okd = all(len(adj[x] & adj[y]) <= 1 for x in loc for y in adj[x])
        if okd and (after >= before or rng.random() < 0.2):
            es[i], es[j] = E(a, c), E(b, d)
        else:
            adj[a].discard(c); adj[c].discard(a); adj[b].discard(d); adj[d].discard(b)
            adj[a].add(b); adj[b].add(a); adj[c].add(d); adj[d].add(c)
    return adj


def make_diamond_free(adj, rng, steps=20000):
    """Switch until diamond-free (or give up)."""
    es = [E(u, v) for u in adj for v in adj[u] if u < v]

    def bad_edges():
        return [(u, v) for (u, v) in es if len(adj[u] & adj[v]) >= 2]

    for _ in range(steps):
        bl = bad_edges()
        if not bl:
            return adj
        a, b = rng.choice(bl)
        i = es.index(E(a, b))
        j = rng.randrange(len(es))
        c, d = es[j]
        if len({a, b, c, d}) < 4 or c in adj[a] or d in adj[b]:
            continue
        adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
        adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
        es[i], es[j] = E(a, c), E(b, d)
    return adj if not bad_edges() else None


def line_cubic_plus_matching(n, rng):
    """L(cubic triangle-free graph) is 4-regular, every edge in one triangle; add a
    matching of non-adjacent pairs avoiding diamonds."""
    m3 = 2 * n // 3
    if m3 % 2 or 3 * m3 // 2 != n:
        return None
    for _ in range(100):
        cub = random_regular(m3, 3, rng)
        if cub is None:
            continue
        if any(cub[u] & cub[v] for u in cub for v in cub[u]):
            continue
        es = sorted({E(u, v) for u in cub for v in cub[u]})
        idx = {e: i for i, e in enumerate(es)}
        adj = {i: set() for i in range(len(es))}
        for v in cub:
            inc = [idx[E(v, w)] for w in cub[v]]
            for x in inc:
                for y in inc:
                    if x != y:
                        adj[x].add(y)
        verts = list(adj)
        for _ in range(50):
            rng.shuffle(verts)
            freev = set(verts)
            okm = True
            added = []
            for x in verts:
                if x not in freev:
                    continue
                freev.discard(x)
                cand = [y for y in freev if y not in adj[x]]
                rng.shuffle(cand)
                for y in cand:
                    common = adj[x] & adj[y]
                    if len(common) >= 2:
                        continue
                    if any(adj[x] & adj[w] or adj[y] & adj[w] for w in common):
                        continue
                    adj[x].add(y); adj[y].add(x); freev.discard(y); added.append((x, y))
                    break
                else:
                    okm = False
                    break
            if okm and diamond_free(adj):
                return adj
            for x, y in added:
                adj[x].discard(y); adj[y].discard(x)
    return None


def perfect_matching(adj, rng, prefer_tri=True):
    tri = {E(u, v) for u in adj for v in adj[u] if adj[u] & adj[v]}
    mate = {}

    def go(free):
        if not free:
            return True
        u = min(free, key=lambda x: (len(adj[x] & free), rng.random()))
        cand = sorted((v for v in adj[u] if v in free),
                      key=lambda v: ((E(u, v) not in tri) if prefer_tri else 0, rng.random()))
        for v in cand[:3]:
            mate[u], mate[v] = v, u
            if go(free - {u, v}):
                return True
            del mate[u], mate[v]
        return False

    sys.setrecursionlimit(10000)
    return dict(mate) if go(frozenset(adj)) else None


def graph_instance(n, rng, fam):
    if fam == "line-cubic":
        adj = line_cubic_plus_matching(n, rng)
        if adj is not None and rng.random() < 0.5:
            adj = anneal_triangles(adj, rng, n * 5)
    else:
        # circulant C_n(1, 2, n/2) randomised by simple switches
        adj = {v: {(v + 1) % n, (v - 1) % n, (v + 2) % n, (v - 2) % n, (v + n // 2) % n} for v in range(n)}
        es = [E(u, v) for u in adj for v in adj[u] if u < v]
        for _ in range(n * 30):
            i, j = rng.randrange(len(es)), rng.randrange(len(es))
            (a, b), (c, d) = es[i], es[j]
            if rng.random() < 0.5:
                c, d = d, c
            if len({a, b, c, d}) < 4 or c in adj[a] or d in adj[b]:
                continue
            adj[a].discard(b); adj[b].discard(a); adj[c].discard(d); adj[d].discard(c)
            adj[a].add(c); adj[c].add(a); adj[b].add(d); adj[d].add(b)
            es[i], es[j] = E(a, c), E(b, d)
        adj = make_diamond_free(adj, rng)
        if adj is None:
            return None
        adj = anneal_triangles(adj, rng, n * 60)
    if adj is None or not diamond_free(adj) or any(len(adj[v]) != 5 for v in adj):
        return None
    mate = perfect_matching(adj, rng, prefer_tri=rng.random() < 0.85)
    if mate is None:
        return None
    return adj, mate


# ----------------------------------------------------------------------------------------

def run_one(adj, m, r, s, rng, stats, tag):
    st = Counter()
    pieces = procedure(adj, m, r, s, rng, st)
    verify(adj, pieces)
    stats[(tag, "verified decompositions")] += 1
    for k, v in st.items():
        stats[(tag, k)] += v
        stats[("ALL", k)] += v


def main():
    ap = ArgumentParser()
    ap.add_argument("--seed", type=int, default=31)
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--skip-lemma", action="store_true")
    ap.add_argument("--planted", type=int, default=None)
    ap.add_argument("--graphs", type=int, default=None)
    args = ap.parse_args()
    rng = Random(args.seed)
    q = args.quick
    if not args.skip_lemma:
        print("== Lemma 4' (own enumeration) ==", flush=True)
        res, bad = lemma4_prime()
        for k in sorted(res, key=str):
            print("  ", k, res[k])
        if bad:
            print("  LEMMA 4' COUNTEREXAMPLES:", bad[:5])
    stats = Counter()
    fails = []
    print("== planted generic (M,r,s), diamond-free ==", flush=True)
    nplant = args.planted if args.planted is not None else (300 if q else 3000)
    for it in range(nplant):
        P = plant_random(rng, rng.randint(1, 5))
        if P is None:
            stats[("planted", "plant conflict")] += 1
            continue
        inst = complete_and_repair(P, rng, rng.choice((4, 8, 14, 24)))
        if inst is None:
            stats[("planted", "repair failed")] += 1
            continue
        adj, m, r, s = inst
        try:
            run_one(adj, m, r, s, rng, stats, "planted")
        except (Failure, AssertionError) as ex:
            stats[("planted", "FAILURE " + str(ex)[:80])] += 1
            fails.append((adj, m, r, s, str(ex)))
    print("== random diamond-free graphs, Lemma 1 constructions ==", flush=True)
    ngr = args.graphs if args.graphs is not None else (20 if q else 120)
    for fam, orders in (("switch", (12, 16, 20, 24, 30, 40)), ("line-cubic", (12, 18, 24, 30, 36, 48))):
        for n in orders:
            for _ in range(ngr // len(orders) + 1):
                inst = graph_instance(n, rng, fam)
                if inst is None:
                    stats[(fam, "generation failed")] += 1
                    continue
                adj, mate = inst
                stats[(fam, "graphs")] += 1
                stats[(fam, "triangles")] += triangle_count(adj)
                for _ in range(6 if q else 15):
                    r, s = lemma1(adj, mate, rng)
                    check_P(adj, mate, r, s)
                    try:
                        run_one(adj, mate, r, s, rng, stats, fam)
                    except (Failure, AssertionError) as ex:
                        stats[(fam, "FAILURE " + str(ex)[:80])] += 1
                        fails.append((adj, mate, r, s, str(ex)))
    for k in sorted(stats, key=str):
        print("  ", k, stats[k])
    if fails:
        import pickle
        with open("04-handoff/review-theoremB/theoremB_independent_failures.pkl", "wb") as fh:
            pickle.dump(fails[:50], fh)
        print("FAILURES:", len(fails))
        return 1
    print("ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    sys.exit(main())
