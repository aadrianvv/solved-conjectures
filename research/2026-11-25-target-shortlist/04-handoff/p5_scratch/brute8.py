from itertools import product, combinations
adj = [[1, 2, 3, 4, 7], [0, 3, 4, 5, 6], [0, 3, 5, 6, 7], [0, 1, 2, 4, 5], [0, 1, 3, 6, 7], [1, 2, 3, 6, 7], [1, 2, 4, 5, 7], [0, 2, 4, 5, 6]]
mate = {5: 7, 7: 5, 2: 6, 6: 2, 1: 3, 3: 1, 0: 4, 4: 0}
n = 8
H = [[w for w in adj[v] if w != mate[v]] for v in range(n)]
E = sorted({(min(u, v), max(u, v)) for u in range(n) for v in H[u]})
found = 0; orients = 0
for bits in product((0, 1), repeat=len(E)):
    arcs = [(u, v) if b else (v, u) for (u, v), b in zip(E, bits)]
    outd = [0]*n
    for u, v in arcs: outd[u] += 1
    if any(d != 2 for d in outd): continue
    orients += 1
    outs = {v: [b for a, b in arcs if a == v] for v in range(n)}
    ins = {v: [a for a, b in arcs if b == v] for v in range(n)}
    # P3: no pair both in
    if any(mate[x] == y for c in range(n) for x, y in combinations(ins[c], 2)):
        continue
    # choose r: for each vertex one out-arc; R must have each vertex exactly one R-in
    for ch in product((0, 1), repeat=n):
        r = {v: outs[v][ch[v]] for v in range(n)}
        if sorted(r.values()) != list(range(n)): continue
        rinv = {w: v for v, w in r.items()}
        if any(mate[rinv[c]] == r[c] for c in range(n)): continue
        # s: S-arcs are the remaining arcs; s(w) = tail of S arc into w
        s = {}
        for v in range(n):
            for w in outs[v]:
                if r[v] != w: s[w] = v
        if any(s[r[u]] == mate[u] for u in range(n)): continue
        found += 1
print("orientations", orients, "solutions", found)
