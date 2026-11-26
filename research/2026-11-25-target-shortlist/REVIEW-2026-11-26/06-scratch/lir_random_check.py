"""Independent random check (referee scratch, 2026-11-26).

Independent of the thread's normalisation code: a plain backtracking search for
locally irregular 3-edge-colourings, applied to random graphs from
 (A) Theorem A's class: one noncactus block whose degree-2 suppression is one of
     theta3, theta4, K4, doubled triangle, doubled square, with random rooted
     cactus attachments (not necessarily subcubic);
 (B) Corollary B's K4-minor-free part: random connected subcubic noncactus
     K4-minor-free graphs (several blocks, bridges, pendant paths).
Usage: python lir_random_check.py SEED COUNT_A COUNT_B
"""
import random, sys
from collections import defaultdict

def lir3(n, edges):
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj[u].append(i); adj[v].append(i)
    # vertex order by BFS, edge order by vertex completion
    start = max(range(n), key=lambda v: len(adj[v]))
    seen = [False]*n; order = []; q = [start]; seen[start] = True
    while q:
        u = q.pop(0); order.append(u)
        for i in adj[u]:
            w = edges[i][0] ^ edges[i][1] ^ u
            if not seen[w]:
                seen[w] = True; q.append(w)
    eorder = []; placed = set()
    for u in order:
        for i in adj[u]:
            if i not in placed:
                placed.add(i); eorder.append(i)
    m = len(edges)
    col = [-1]*m
    remaining = [len(adj[v]) for v in range(n)]
    cnt = [[0]*3 for _ in range(n)]
    def ok_vertex(u):
        for i in adj[u]:
            w = edges[i][0] ^ edges[i][1] ^ u
            if remaining[w] == 0:
                c = col[i]
                if cnt[u][c] == cnt[w][c]:
                    return False
        return True
    sys.setrecursionlimit(10000)
    def rec(k, maxc):
        if k == m:
            return True
        i = eorder[k]; u, v = edges[i]
        for c in range(min(3, maxc+2)):
            col[i] = c; cnt[u][c] += 1; cnt[v][c] += 1
            remaining[u] -= 1; remaining[v] -= 1
            good = True
            if remaining[u] == 0 and not ok_vertex(u): good = False
            if good and remaining[v] == 0 and not ok_vertex(v): good = False
            if good and rec(k+1, max(maxc, c)):
                return True
            col[i] = -1; cnt[u][c] -= 1; cnt[v][c] -= 1
            remaining[u] += 1; remaining[v] += 1
        return False
    return rec(0, -1)

def is_simple(edges):
    s = set()
    for u, v in edges:
        if u == v: return False
        k = (min(u, v), max(u, v))
        if k in s: return False
        s.add(k)
    return True

KERNELS = {
    'theta3': (2, [(0,1)]*3),
    'theta4': (2, [(0,1)]*4),
    'K4': (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]),
    'dtri': (3, [(0,1),(0,1),(0,2),(0,2),(1,2)]),
    'dsq': (4, [(0,1),(0,1),(0,2),(1,3),(2,3),(2,3)]),
}

def subdivide(rng, kn, kedges, maxlen):
    while True:
        n = kn; edges = []; verts_on = []
        for a, b in kedges:
            L = rng.randint(1, maxlen)
            prev = a
            for _ in range(L-1):
                edges.append((prev, n)); prev = n; n += 1
            edges.append((prev, b))
        if is_simple(edges):
            return n, edges

def attach_cactus(rng, n, edges, budget):
    """Attach random rooted cacti: pendant paths, triangles, longer cycles, recursively."""
    verts = list(range(n))
    for _ in range(budget):
        r = rng.choice(verts)
        kind = rng.random()
        if kind < 0.4:  # pendant path
            L = rng.randint(1, 3); prev = r
            for _ in range(L):
                edges.append((prev, n)); verts.append(n); prev = n; n += 1
        else:  # cycle of length 3..5 through r
            L = rng.choice([3, 3, 3, 4, 5]); prev = r
            for _ in range(L-1):
                edges.append((prev, n)); verts.append(n); prev = n; n += 1
            edges.append((prev, r))
    return n, edges

def sp_reducible(n, edges):
    """K4-minor-free test: series-parallel reduction of the multigraph."""
    adj = defaultdict(lambda: defaultdict(int))
    for u, v in edges:
        adj[u][v] += 1; adj[v][u] += 1
    alive = set(range(n)); changed = True
    while changed:
        changed = False
        for u in list(alive):
            for w in list(adj[u]):
                if adj[u][w] > 1:
                    adj[u][w] = 1; adj[w][u] = 1; changed = True
            deg = len(adj[u])
            if deg <= 1:
                for w in list(adj[u]):
                    del adj[w][u]
                adj[u].clear(); alive.discard(u); changed = True
            elif deg == 2:
                a, b = list(adj[u])
                del adj[a][u]; del adj[b][u]; adj[u].clear(); alive.discard(u)
                adj[a][b] += 1; adj[b][a] += 1; changed = True
    return not alive

def is_cactus(n, edges):
    # cactus iff every block is an edge or a cycle: m - n + 1 == number of cycles... use DFS bridges/blocks
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i)); adj[v].append((u, i))
    disc = [-1]*n; low = [0]*n; t = [0]; stack = []; blocks = []
    sys.setrecursionlimit(10000)
    def dfs(u, pe):
        disc[u] = low[u] = t[0]; t[0] += 1
        for w, i in adj[u]:
            if i == pe: continue
            if disc[w] == -1:
                stack.append(i); dfs(w, i)
                low[u] = min(low[u], low[w])
                if low[w] >= disc[u]:
                    b = []
                    while True:
                        j = stack.pop(); b.append(j)
                        if j == i: break
                    blocks.append(b)
            elif disc[w] < disc[u]:
                stack.append(i); low[u] = min(low[u], disc[w])
    dfs(0, -1)
    for b in blocks:
        vs = set()
        for j in b: vs.update(edges[j])
        if len(b) > 1 and len(b) != len(vs):
            return False
    return True

def random_subcubic(rng, n, extra):
    """Random connected subcubic graph: random tree with max deg 3 plus extra edges."""
    deg = [0]*n; edges = []; es = set()
    for v in range(1, n):
        cands = [u for u in range(v) if deg[u] < 3]
        u = rng.choice(cands)
        edges.append((u, v)); es.add((u, v)); deg[u] += 1; deg[v] += 1
    tries = 0
    while extra > 0 and tries < 500:
        tries += 1
        u, v = rng.sample(range(n), 2)
        k = (min(u, v), max(u, v))
        if deg[u] < 3 and deg[v] < 3 and k not in es:
            edges.append(k); es.add(k); deg[u] += 1; deg[v] += 1; extra -= 1
    return edges

def main():
    seed, ca, cb = map(int, sys.argv[1:4])
    rng = random.Random(seed)
    stats = defaultdict(int)
    for t in range(ca):
        name = rng.choice(list(KERNELS))
        kn, ke = KERNELS[name]
        n, edges = subdivide(rng, kn, ke, 4)
        n, edges = attach_cactus(rng, n, edges, rng.randint(0, 6))
        if len(edges) > 45:
            continue
        stats['A:'+name] += 1
        if not lir3(n, edges):
            print('COUNTEREXAMPLE A', name, n, edges, flush=True); return 1
    for t in range(cb):
        n = rng.randint(8, 30)
        edges = random_subcubic(rng, n, rng.randint(1, n//3))
        if is_cactus(n, edges) or not sp_reducible(n, edges):
            continue
        stats['B:n%d' % (n//10*10)] += 1
        if not lir3(n, edges):
            print('COUNTEREXAMPLE B', n, edges, flush=True); return 1
    print('no counterexample', dict(sorted(stats.items())), flush=True)
    return 0

if __name__ == '__main__':
    # controls: bow-tie must fail; K4 must pass
    bow = [(0,1),(0,2),(0,3),(2,3),(0,4),(0,5),(4,5),(1,6),(1,7),(6,7),(1,8),(1,9),(8,9)]
    assert not lir3(10, bow), 'bow-tie control'
    assert lir3(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]), 'K4 control'
    assert not sp_reducible(4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)])
    assert sp_reducible(5, [(0,1),(1,2),(2,3),(3,0),(0,2),(2,4)])
    print('controls ok', flush=True)
    sys.exit(main())
