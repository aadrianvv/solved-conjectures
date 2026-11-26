"""Planted generator: perfect matching M = {2i,2i+1}; H 4-regular simple avoiding M; many planted cherries;
accept iff every M-edge lies in <= maxt triangles."""
from random import Random
def planted(n, rng, p=0.8, maxt=1, tries=2000):
    for _ in range(tries):
        m = {}
        perm = list(range(n)); rng.shuffle(perm)
        for i in range(0, n, 2): m[perm[i]] = perm[i+1]; m[perm[i+1]] = perm[i]
        adj = [set() for _ in range(n)]
        deg = [0]*n
        def add(u, v):
            if u == v or v in adj[u] or m[u] == v or deg[u] >= 4 or deg[v] >= 4: return False
            adj[u].add(v); adj[v].add(u); deg[u] += 1; deg[v] += 1; return True
        fibres = [(u, m[u]) for u in range(n) if u < m[u]]
        rng.shuffle(fibres)
        for y, z in fibres:
            if rng.random() < p:
                cand = [x for x in range(n) if x not in (y, z) and deg[x] <= 2 and deg[y] < 4 and deg[z] < 4
                        and y not in adj[x] and z not in adj[x]]
                if cand:
                    x = rng.choice(cand); add(x, y); add(x, z)
        # complete randomly
        stubs = [v for v in range(n) for _ in range(4 - deg[v])]
        ok = False
        for _ in range(200):
            rng.shuffle(stubs)
            pairs = [(stubs[i], stubs[i+1]) for i in range(0, len(stubs), 2)]
            if all(a != b and b not in adj[a] and m[a] != b for a, b in pairs) and len({frozenset(p) for p in pairs}) == len(pairs):
                for a, b in pairs: adj[a].add(b); adj[b].add(a)
                ok = True; break
        if not ok: continue
        G = [set(adj[v]) | {m[v]} for v in range(n)]
        if all(len(G[u] & G[m[u]]) <= maxt for u in range(n)):
            return G, m
    return None
