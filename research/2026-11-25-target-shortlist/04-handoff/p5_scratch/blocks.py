"""P5* counterexample search via bridge-forced blocks.

A block B has attachment set A (degree 4 in B, each later joined by a bridge to a smallest odd cap) and all
other vertices of degree 5.  Every perfect matching of the final graph contains every bridge, so it restricts
to a perfect matching of B - A, and the bridges are M-edges in no triangle.  H = G - M then has the B-part as
a union of components, so (P5) for G fails whenever it fails on the B-part.  P5* fails for G iff (for the caps
feasible) every perfect matching of B - A gives an infeasible B-part.  Exhaustive over the listed (n_B, |A|)."""
import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
from check_regular_path_decomposition import label_graph, isomorphic, list_bits
from p5solve import solve
from collections import Counter

def degseq_graphs(degs):
    order = len(degs)
    adjacency = [0] * order
    remaining = list(degs)
    def visit(v):
        if v == order:
            yield tuple(adjacency); return
        groups = {}
        for w in range(v + 1, order):
            if remaining[w]:
                groups.setdefault((adjacency[w], degs[w]), []).append(w)
        groups = list(groups.values())
        room = sum(map(len, groups))
        if remaining[v] > room or any(d > order - v - 1 for d in remaining[v + 1:]):
            return
        def choices(k, needed, room):
            if not needed:
                yield (); return
            if k >= len(groups): return
            group = groups[k]
            for take in range(max(0, needed - room + len(group)), min(needed, len(group)) + 1):
                for rest in choices(k + 1, needed - take, room - len(group)):
                    yield tuple(group[:take]) + rest
        for nb in choices(0, remaining[v], room):
            for w in nb:
                adjacency[v] ^= 1 << w; adjacency[w] ^= 1 << v; remaining[w] -= 1
            remaining[v] = 0
            yield from visit(v + 1)
            remaining[v] = len(nb)
            for w in nb:
                adjacency[v] ^= 1 << w; adjacency[w] ^= 1 << v; remaining[w] += 1
    yield from visit(0)

def matchings(adj, verts):
    def go(free):
        if not free: yield {}; return
        u = min(free)
        for v in adj[u]:
            if v in free:
                for m in go(free - {u, v}):
                    m = dict(m); m[u] = v; m[v] = u; yield m
    yield from go(frozenset(verts))

def run(nB, k):
    degs = [4] * k + [5] * (nB - k)
    classes = []; tal = Counter()
    for g in degseq_graphs(degs):
        if any(bin(g[v]).count('1') != degs[v] for v in range(nB)): continue
        lab = label_graph(g); key = tuple(sorted(lab))
        if any(kk == key and isomorphic(g, h, lab, hl) for kk, h, hl in classes): continue
        classes.append((key, g, lab))
    for _, g, _ in classes:
        adj = [set(list_bits(a)) for a in g]
        A = [v for v in range(nB) if len(adj[v]) == 4]
        nm = feas = 0
        for mm in matchings(adj, [v for v in range(nB) if v not in A]):
            nm += 1
            mate = dict(mm)
            for a in A: mate[a] = a          # bridge partner outside B; no triangles
            if solve(adj, mate, node_limit=10**6) is not None:
                feas += 1; break
        tal['blocks'] += 1
        if nm == 0: tal['no matching of B-A'] += 1
        elif feas == 0:
            tal['ALL MATCHINGS INFEASIBLE'] += 1
            print("CANDIDATE P5* COUNTEREXAMPLE BLOCK", nB, k, [sorted(a) for a in adj], flush=True)
    print(nB, k, dict(tal), flush=True)

if __name__ == "__main__":
    for spec in sys.argv[1:]:
        nB, k = map(int, spec.split(','))
        run(nB, k)
