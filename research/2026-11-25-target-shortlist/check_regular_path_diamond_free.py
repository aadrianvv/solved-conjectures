"""End-to-end implementation of the diamond-free degree-five procedure of 04e.

Pipeline: canonical construction (04d Lemma 1) -> first sweep (04d Section 2, with
Section 3 implemented as written: block search, pair replacement, rotations) -> second
sweep of 04e (G-rule, G-pendants, absorption, Gamma / Gamma' rules, Gtarget resolution
with the rotation).  The rule choice is the deterministic one of 04e Section 3; there is
no search.  Every run verifies that the output is an exact partition of E(G) into simple
paths with five edges.

Random runs are evidence for the correctness of the implementation and of the case
catalogue; the proof is the written argument of 04e together with the exhaustive window
checks in check_regular_path_gsweep.py.
"""

import sys
from argparse import ArgumentParser
from collections import Counter, defaultdict
from random import Random

from check_regular_path_sweep_pipeline import (canonical, kind, solve_cluster, edge,
                                               path_edges, diamond_free_graph)


class Fail(Exception):
    pass


def first_and_second_sweep(adj, mate, r, s, trails, stats):
    n = len(adj)
    rinv = {v: u for u, v in r.items()}
    m = mate
    key_of = {}
    for key in trails:
        key_of[key[0]] = key
        key_of[key[1]] = key
    defect = {}
    for key, t in trails.items():
        k = kind(t)
        if k == "square":
            defect[key] = t if t[1] == t[5] else t[::-1]
        elif k != "path":
            raise Fail("canonical trail of unexpected shape")
    target, link = {}, {}
    for key, (a, b, c, d, e, _) in defect.items():
        tk = key_of[rinv[c]]
        target[key] = tk
        if tk in defect:
            link[key] = 1 if c == defect[tk][1] else 2
            assert c in (defect[tk][1], defect[tk][4])
        else:
            link[key] = 0
    succ = {k: target[k] for k in defect if link[k] == 2}
    pred = {t: k for k, t in succ.items()}
    sources, oddcycles = set(), []
    seen = set()
    for k in defect:
        if k in seen:
            continue
        start, here = k, {k}
        while start in pred and pred[start] not in here:
            start = pred[start]
            here.add(start)
        if start in pred:
            cyc = [start]
            x = succ[start]
            while x != start:
                cyc.append(x)
                x = succ[x]
            seen.update(cyc)
            if len(cyc) % 2 == 0:
                sources.update(cyc[0::2])
            else:
                oddcycles.append(cyc)
        else:
            chain = [start]
            while chain[-1] in succ:
                chain.append(succ[chain[-1]])
            seen.update(chain)
            sources.update(chain[0::2])
    in_odd = {k for cyc in oddcycles for k in cyc}

    # ---- G-configurations (determined by the first sweep alone)
    G = {}
    for k in sources:
        if link[k] != 0:
            continue
        a, b, c, d, e, _ = defect[k]
        f = rinv[c]
        if m[f] != b:
            continue
        h = r[b]
        W0 = key_of[rinv[f]]
        if W0 not in defect:
            case = "alpha"
        elif f == defect[W0][1]:
            case = "beta"
        else:
            assert f == defect[W0][4]
            case = "gamma"
        G[c] = dict(T=k, f=f, b=b, h=h, W0=W0, case=case)
    # gamma: W0 kept as a source if its own trade is type-2.  If W0 = T_{c*} is the source
    # of another G-configuration c* ("Gtarget" edge c -> c*), resolve the functional graph of
    # these edges: an existing configuration absorbs W0 and cancels c*; odd cycles use the
    # Gamma rule at the first valid node or, if no node is valid, the rotation rule.
    gt = {}
    for c, g in G.items():
        if g["case"] == "gamma":
            W0 = g["W0"]
            assert W0 in sources, "gamma partner must be a source"
            if link[W0] == 0 and defect[W0][2] in G:
                gt[c] = defect[W0][2]
    prev = {v: k for k, v in gt.items()}
    assert len(prev) == len(gt)
    cancelled, absorb_edge, gamma_src, rotations, visited = set(), set(), set(), [], set()
    for c0 in gt:
        if c0 in prev:
            continue
        cur, exists = c0, True
        while cur in gt:
            visited.add(cur)
            if exists:
                absorb_edge.add(cur); cancelled.add(gt[cur])
            exists = not exists
            cur = gt[cur]
        visited.add(cur)
    for c0 in gt:
        if c0 in visited:
            continue
        cyc = [c0]
        while gt[cyc[-1]] != c0:
            cyc.append(gt[cyc[-1]])
        visited.update(cyc)
        k = len(cyc)
        stats["Gtarget cycle length %d" % k] += 1
        if k % 2 == 0:
            for i in range(0, k, 2):
                absorb_edge.add(cyc[i]); cancelled.add(cyc[i + 1])
        else:
            # 04e: the Gamma rules are valid at node j unless F1 (s(q_j) = c_j) holds
            # and the pendant s(g_j) differs from h_j; if every node fails, rotate
            ch = "rot"
            for j, cj in enumerate(cyc):
                W0 = G[cj]["W0"]
                qj, gj = defect[W0][2], defect[W0][1]
                if not (s[qj] == cj and s[gj] != G[cj]["h"]):
                    ch = j
                    break
            stats["odd Gtarget cycle: " + ("rotation" if ch == "rot" else "Gamma at one node")] += 1
            if ch == "rot":
                rotations.append(cyc)
            else:
                gamma_src.add(cyc[ch])
                for t in range(1, k, 2):
                    absorb_edge.add(cyc[(ch + t) % k]); cancelled.add(cyc[(ch + t + 1) % k])
    stats["cancelled configurations"] += len(cancelled)
    for c in cancelled:
        del G[c]
    rot_nodes = {c for cyc in rotations for c in cyc}
    absorbed = {}
    gamma_rule = {}
    for c, g in G.items():
        if g["case"] != "gamma" or c in rot_nodes:
            continue
        W0 = g["W0"]
        if link[W0] == 2:
            gamma_rule[c] = W0
            stats["gamma kept as source (type-2)"] += 1
        elif c in gamma_src:
            gamma_rule[c] = W0
            stats["gamma kept as source (Gtarget odd cycle)"] += 1
        else:
            assert c not in gt or c in absorb_edge
            absorbed[W0] = c
            stats["gamma absorbed (type-%d link%s)" % (link[W0], ", Gtarget" if c in gt else "")] += 1
    for c, g in G.items():
        stats["G-config " + g["case"]] += 1

    trading = sources - set(absorbed)
    # ---- pendants: type-1 changes and G-pendants
    newA = {}
    for k in trading:
        if link[k] == 1:
            tk = target[k]
            newA[tk] = defect[k][1]
            assert r[defect[tk][1]] == defect[k][1]
    for c, g in G.items():
        if g["case"] == "beta":
            W0 = g["W0"]
            assert W0 not in newA
            newA[W0] = g["b"]           # G-pendant; Q_c takes the old pendant edge {s(f), f}
    recv = defaultdict(dict)
    for k in trading:
        if link[k] == 0:
            a, b, c, d, e, _ = defect[k]
            recv[target[k]][c] = b
    pieces = []
    for key in trails:
        if key in defect:
            a, b, c, d, e, _ = defect[key]
            A = newA.get(key, a)
            if key in absorbed:
                gc = G[absorbed[key]]
                pieces.append((A, b, c, d, e, gc["b"]))     # (A*, g, q, p, f, b)
            elif key in trading:
                pieces.append((A, b, e, d, c, s[c]))
            elif key in in_odd:
                continue
            else:
                assert pred[key] in trading
                pieces.append((A, b, c, d, e, r[e]))
        else:
            p = list(trails[key])
            for cc, bb in recv.get(key, {}).items():
                if p[1] == cc:
                    p[0] = bb
                else:
                    assert p[4] == cc
                    p[5] = bb
            pieces.append(tuple(p))
    # ---- odd type-2 cycles (04d Section 3 as written)
    for cyc in oddcycles:
        L = len(cyc)
        T = []
        for k in cyc:
            a, b, c, d, e, _ = defect[k]
            T.append((newA.get(k, a), b, c, d, e))
        for i in range(L):
            assert T[i][2] == T[(i + 1) % L][4]
        done = False
        for j in range(L if L > 3 else 1):
            block = [T[(j + t) % L] for t in range(3)]
            sol = solve_cluster([(x[0], x[1], x[2], x[3], x[4], x[1]) for x in block], require_simple=True)
            if sol is None:
                continue
            pieces.extend(sol)
            for t in range(3, L, 2):
                Ai, bi, ci, di, ei = T[(j + t) % L]
                Aj, bj, cj, dj, ej = T[(j + t + 1) % L]
                pieces.append((Ai, bi, ei, di, ci, bj))
                pieces.append((Aj, bj, cj, dj, ci, bi))
            done = True
            stats["odd cycle: block cover"] += 1
            break
        if not done:
            if L == 3:
                raise Fail("odd 3-cycle without a simple cover")
            A = [x[0] for x in T]; B = [x[1] for x in T]; C = [x[2] for x in T]; D = [x[3] for x in T]
            if all(A[i] == D[(i + 1) % L] for i in range(L)):
                pieces.extend((A[i], B[i], C[(i - 1) % L], D[(i - 1) % L], C[(i - 2) % L], B[(i - 2) % L]) for i in range(L))
            elif all(A[i] == D[(i - 1) % L] for i in range(L)):
                pieces.extend((A[i], B[i], C[i], D[(i + 1) % L], C[(i + 1) % L], B[(i + 2) % L]) for i in range(L))
            else:
                raise Fail("odd cycle: no block and no uniform rotation")
            stats["odd cycle: rotation"] += 1

    # ---- second sweep
    def find_piece(e, pos_check=None):
        out = [i for i, p in enumerate(pieces) if e in set(path_edges(p))]
        assert len(out) == 1
        return out[0]

    def replace_terminal(f, old, new):
        """In the piece where {f, old} is a terminal edge with old at the end, put new."""
        i = find_piece(edge(f, old))
        p = list(pieces[i])
        if p[0] == old and p[1] == f:
            p[0] = new
        elif p[5] == old and p[4] == f:
            p[5] = new
        else:
            raise Fail("partner edge is not terminal")
        pieces[i] = tuple(p)

    def q_index(c, g):
        i = find_piece(edge(c, g["f"]))
        q = pieces[i]
        q = q if q[0] == q[3] else q[::-1]
        assert q[:5] == (g["b"], c, g["f"], g["b"], g["h"]), (q, g)
        return i, q

    # rotation rule for odd Gtarget cycles in which the Gamma rules fail at every node
    for cyc in rotations:
        k = len(cyc)
        idx = []
        for i, c in enumerate(cyc):
            g = G[c]
            iq, q = q_index(c, g)
            iw = find_piece(edge(s[g["f"]], g["f"]))
            w = pieces[iw] if pieces[iw][2] == g["f"] else pieces[iw][::-1]
            idx.append((iq, q, iw, w))
        new = {}
        for i, c in enumerate(cyc):
            g = G[c]
            iq, q, iw, w = idx[i]
            A, gg, f, p, qq, last = w
            nxt, nxt2 = cyc[(i + 1) % k], cyc[(i + 2) % k]
            if not (qq == nxt and last == c and gg == G[nxt]["b"]):
                raise Fail("rotation rule not applicable")
            new[iq] = (q[5], g["h"], g["b"], f, gg, A)
            new[iw] = (g["b"], c, f, p, nxt, nxt2)
        for i, v in new.items():
            pieces[i] = v
        stats["Gtarget rotation used"] += 1

    # Gamma / Gamma' rules first (they rebuild two whole pieces)
    for c, W0 in gamma_rule.items():
        g = G[c]
        f, b, h = g["f"], g["b"], g["h"]
        i, q = q_index(c, g)
        Y = q[5]
        gg = s[f]
        j = find_piece(edge(gg, f))
        w = pieces[j]
        w = w if w[2] == f else w[::-1]
        A, g2, f2, p, qq, sq = w
        assert g2 == gg and f2 == f and r[p] == f and m[p] == qq
        if A == h:
            new = [(Y, h, gg, f, c, b), (h, b, f, p, qq, sq)]
            stats["Gamma' used"] += 1
        else:
            new = [(sq, qq, p, f, c, b), (Y, h, b, f, gg, A)]
        pieces[i], pieces[j] = new
    # beta, absorbed gamma, alpha: Q' -> (s(f), f, c, b, h, Y*); alpha also moves b into P.
    # Locate every Q' first, then apply the alpha terminal replacements (which may change
    # the h-end of another Q'), then rebuild the Q's.
    qidx = {c: q_index(c, g)[0] for c, g in G.items() if c not in gamma_rule and c not in rot_nodes}
    for c, g in G.items():
        if g["case"] == "alpha":
            replace_terminal(g["f"], s[g["f"]], g["b"])
    for c, i in qidx.items():
        g = G[c]
        q = pieces[i] if pieces[i][0] == pieces[i][3] else pieces[i][::-1]
        assert q[:5] == (g["b"], c, g["f"], g["b"], g["h"])
        pieces[i] = (s[g["f"]], g["f"], c, g["b"], g["h"], q[5])
    return pieces


def solve_one(adj, mate, r, s, trails, stats):
    """Run the procedure of 04e with its deterministic rule choice (no search) and verify
    the output exactly.  Any failure is raised: the written rule must succeed."""
    probe = Counter()
    pieces = first_and_second_sweep(adj, mate, r, s, trails, probe)
    verify(adj, mate, pieces)
    stats.update(probe)
    stats["verified decompositions"] += 1
    return pieces


def generic_instance(n, rng, steps=6000, bonus=1.0):
    """Generic data (M, r, s) satisfying (P1)-(P3) on a diamond-free simple graph.

    The procedure of 04e uses only these properties (not Lemma 1's construction), so such
    data are a broader test.  Simulated annealing rewards P5-violating apices and square
    defects, which create many G-configurations.  Returns (adj, mate, r, s) or None."""
    import math
    perm = list(range(n)); rng.shuffle(perm)
    m = {}
    for i in range(0, n, 2):
        m[perm[i]], m[perm[i + 1]] = perm[i + 1], perm[i]
    r = list(range(n)); rng.shuffle(r)
    sv = list(range(n)); rng.shuffle(sv)

    def score(r, sv):
        bad = 0
        E = Counter()
        for v in range(n):
            if r[v] == v or sv[v] == v:
                bad += 1
            E[frozenset((v, r[v]))] += 1
            E[frozenset((v, sv[v]))] += 1
            if v < m[v]:
                E[frozenset((v, m[v]))] += 1
        bad += sum(c - 1 for c in E.values() if c > 1)
        rinv = {r[v]: v for v in range(n)}
        for u in range(n):
            if sv[r[u]] == m[u]:
                bad += 1
        adj = defaultdict(set)
        for e in E:
            if len(e) == 2:
                a, b = tuple(e)
                adj[a].add(b); adj[b].add(a)
        for e in E:
            if len(e) == 2:
                a, b = tuple(e)
                if len(adj[a] & adj[b]) >= 2:
                    bad += 1
        good = 0
        for c in range(n):
            if m[rinv[c]] == r[c]:
                good += 1
        for u in range(n):
            v = m[u]
            if u < v and (sv[r[u]] == r[v] or sv[r[v]] == r[u]):
                good += 1
        return bad, good

    bad, good = score(r, sv)
    T = 2.0
    for it in range(steps):
        arr = r if rng.random() < 0.5 else sv
        x, y = rng.randrange(n), rng.randrange(n)
        arr[x], arr[y] = arr[y], arr[x]
        nb, ng = score(r, sv)
        delta = (nb - bad) * 10 - bonus * (ng - good)
        if delta <= 0 or rng.random() < math.exp(-delta / T):
            bad, good = nb, ng
        else:
            arr[x], arr[y] = arr[y], arr[x]
        T = max(0.05, T * 0.999)
    if bad:
        return None
    adj = [set() for _ in range(n)]
    for v in range(n):
        for w in (r[v], sv[v], m[v]):
            adj[v].add(w); adj[w].add(v)
    assert all(len(a) == 5 for a in adj)
    return adj, m, {v: r[v] for v in range(n)}, {v: sv[v] for v in range(n)}


def verify(adj, mate, pieces):
    n = len(adj)
    allE = Counter(edge(u, v) for u in range(n) for v in adj[u] if u < v)
    used = Counter(e for p in pieces for e in path_edges(p))
    if used != allE:
        raise Fail("not an edge partition")
    for p in pieces:
        if len(p) != 6 or len(set(p)) != 6:
            raise Fail("piece is not a simple 5-edge path: %r" % (p,))


def main():
    ap = ArgumentParser()
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--graphs", type=int, default=40)
    ap.add_argument("--constructions", type=int, default=10)
    ap.add_argument("--orders", type=int, nargs="*", default=[12, 14, 16, 20, 24, 30, 40, 60])
    ap.add_argument("--generic", type=int, default=0, help="number of generic (M,r,s) instances")
    args = ap.parse_args()
    rng = Random(args.seed)
    sys.path.insert(0, ".")
    from check_regular_path_gsweep_gen import tri_graph
    stats = Counter()
    for n in args.orders:
        for t in range(args.graphs):
            gen = tri_graph(n, rng, 0.5) if t % 2 == 0 else diamond_free_graph(n, rng)
            if gen is None:
                stats["generation failures"] += 1
                continue
            adj, mate = gen
            for _ in range(args.constructions):
                r, s, trails = canonical(adj, mate, rng)
                solve_one(adj, mate, r, s, trails, stats)
    for t in range(args.generic):
        n = rng.choice([10, 12, 14, 16, 18, 20, 24])
        inst = generic_instance(n, rng)
        if inst is None:
            stats["generic: annealing failed"] += 1
            continue
        adj, mate, r, s = inst
        trails = {}
        for u in range(n):
            v = mate[u]
            if u < v:
                trails[(u, v)] = (s[r[u]], r[u], u, v, r[v], s[r[v]])
        solve_one(adj, mate, r, s, trails, stats)
        stats["generic instances"] += 1
    for k in sorted(stats):
        print(k, stats[k])


if __name__ == "__main__":
    main()
