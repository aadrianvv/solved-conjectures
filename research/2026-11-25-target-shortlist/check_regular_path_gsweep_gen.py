"""Diamond-free 5-regular graphs where (almost) every M-edge lies in a triangle."""
import random
from itertools import combinations


def creates_diamond(adj, u, v):
    common = adj[u] & adj[v]
    if len(common) >= 2:
        return True
    # new triangles u v w (w common) must not share an edge with an existing triangle
    for w in common:
        if (adj[u] & adj[w]) or (adj[v] & adj[w]):
            return True
    # edge uv must not become a chord in an existing triangle pair: covered above
    # also: adding uv creates triangle uvw; edges uw, vw must not be in other triangles (checked);
    # and existing triangles through u w etc. -- that's the check above.
    return False


def is_diamond_free(adj):
    n = len(adj)
    for u in range(n):
        for v in adj[u]:
            if u < v and len(adj[u] & adj[v]) >= 2:
                return False
    return True


def tri_graph(n, rng, two_apex_frac=0.5, tries=2000):
    assert n % 2 == 0
    for _ in range(tries):
        adj = [set() for _ in range(n)]
        perm = list(range(n))
        rng.shuffle(perm)
        mate = {}
        for i in range(0, n, 2):
            a, b = perm[i], perm[i + 1]
            mate[a], mate[b] = b, a
            adj[a].add(b); adj[b].add(a)
        Medges = [(perm[i], perm[i + 1]) for i in range(0, n, 2)]
        rng.shuffle(Medges)
        apexcount = [0] * n
        # choose some vertices as double apexes
        for x, y in Medges:
            cands = [c for c in range(n) if c not in (x, y) and len(adj[c]) <= 3 and len(adj[x]) < 5 and len(adj[y]) < 5
                     and c not in adj[x] and c not in adj[y]]
            rng.shuffle(cands)
            cands.sort(key=lambda c: -(apexcount[c] == 1) if rng.random() < two_apex_frac else 0)
            for c in cands[:30]:
                if creates_diamond(adj, c, x):
                    continue
                adj[c].add(x); adj[x].add(c)
                if creates_diamond(adj, c, y):
                    adj[c].discard(x); adj[x].discard(c)
                    continue
                adj[c].add(y); adj[y].add(c)
                apexcount[c] += 1
                break
        # fill remaining degrees
        stuck = 0
        while stuck < 200:
            low = [v for v in range(n) if len(adj[v]) < 5]
            if not low:
                break
            u = rng.choice(low)
            cand = [v for v in low if v != u and v not in adj[u]]
            rng.shuffle(cand)
            for v in cand:
                if not creates_diamond(adj, u, v):
                    adj[u].add(v); adj[v].add(u)
                    break
            else:
                stuck += 1
                # random switch to unstick: remove a random non-M edge at u
                if any(len(adj[v]) < 5 for v in range(n)):
                    nb = [w for w in adj[u] if w != mate[u]]
                    if nb:
                        w = rng.choice(nb)
                        adj[u].discard(w); adj[w].discard(u)
        if all(len(a) == 5 for a in adj) and is_diamond_free(adj):
            return adj, mate
    return None


def stats(adj, mate):
    n = len(adj)
    ap = [sum(1 for x, y in combinations([w for w in adj[v] if w != mate[v]], 2) if mate[x] == y) for v in range(n)]
    return sum(ap), sum(1 for a in ap if a == 2)
