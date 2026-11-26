from collections import Counter
from itertools import product
from check_regular_path_sweep_pipeline import solve_cluster, path_edges
b, c = (0, 1, 2), (3, 4, 5)
counts = Counter(); fails = []
for closed in (True, False):
    e = (c[2] if closed else 6, c[0], c[1])
    corners = set(c + e)
    for first, last in product((7,) if closed else (7, b[2]), (9,) if closed else (9, b[0])):
        d = (first, 8, last)
        terminals = (corners | set(d)) - set(b)
        options = [sorted((terminals - {c[i], e[i]}) | {10 + i}) for i in range(3)]
        for a in product(*options):
            if len(set(a)) != 3: continue
            trails = [(a[i], b[i], c[i], d[i], e[i], b[i]) for i in range(3)]
            if len({x for t in trails for x in path_edges(t)}) != 15: continue
            for changed in product((False, True), repeat=3):
                if any(a[i] in corners if changed[i] else a[i] == d[i] for i in range(3)): continue
                if any(changed[i] and a[i] == d[i] for i in range(3)):
                    counts["excluded by P5 (changed A_i = d_i)"] += 1; continue
                sol = solve_cluster(trails, require_simple=True)
                if sol is not None:
                    counts[("closed" if closed else "open", "cover")] += 1
                elif not closed and d[1] in (a[0], a[2]):
                    counts[("open", "d1 in {A0,A2}")] += 1
                else:
                    counts[("closed" if closed else "open", "OTHER FAIL")] += 1
                    fails.append((closed, trails, changed))
print(dict(counts))
for f in fails[:12]: print(f)
