"""Survey of maximum MIL partitions (third session).  Usage:
  python mil_survey.py exhaustive N DIR     all cubic graphs in DIR/cubic-N.txt
  python mil_survey.py random N SAMPLES SEED
Reports, per graph, the number of maximum MIL partitions, how many are feasible, and
statistics on K2 components, isolated vertices, triangle-freeness.
"""
import sys
from collections import Counter

from mil_sat import all_max_mil, designate, random_cubic


def comps(adj, Y):
    n = len(adj)
    Ys = set(Y)
    X = [v for v in range(n) if v not in Ys]
    seen = set()
    out = []
    for v in X:
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        c = []
        while stack:
            a = stack.pop()
            c.append(a)
            for b in adj[a]:
                if b not in Ys and b not in seen:
                    seen.add(b)
                    stack.append(b)
        out.append(len(c))
    return Counter(out)


def triangle_free(adj):
    return not any(set(adj[u]) & set(adj[v]) for u in range(len(adj)) for v in adj[u])


def survey_graph(adj, limit=5000):
    L = all_max_mil(adj, limit=limit)
    rows = []
    for Y in L:
        c = comps(adj, Y)
        f = designate(adj, Y) is not None
        rows.append((c.get(2, 0), c.get(1, 0), f))
    return L, rows


def main():
    mode = sys.argv[1]
    if mode == 'exhaustive':
        n = int(sys.argv[2])
        sys.path.insert(0, '.')
        from cubic_gen import load
        graphs = load(n, sys.argv[3])
    else:
        n, S, seed = map(int, sys.argv[2:5])
        graphs = [random_cubic(n, seed + i) for i in range(S)]
    tot = Counter()
    for gi, adj in enumerate(graphs):
        L, rows = survey_graph(adj)
        nf = sum(1 for r in rows if r[2])
        tf = triangle_free(adj)
        tot['graphs'] += 1
        tot['partitions'] += len(rows)
        tot['feasible'] += nf
        if nf == 0:
            tot['no_feasible_max'] += 1
            print('NO FEASIBLE MAX', gi, 'trianglefree', tf, [sorted(a) for a in adj], flush=True)
        elif nf < len(rows):
            tot['some_infeasible'] += 1
            if tf:
                tot['some_infeasible_trianglefree'] += 1
            bad = [r for r in rows if not r[2]]
            # does every infeasible one have a K2?
            if all(r[0] > 0 for r in bad):
                tot['all_bad_have_K2'] += 1
            mink2 = min(r[0] for r in rows)
            if any(not r[2] and r[0] == mink2 for r in rows):
                tot['minK2_rule_fails'] += 1
            print('some infeasible', gi, 'tf', tf, 'bad', len(bad), 'of', len(rows),
                  'K2 of bad', sorted(Counter(r[0] for r in bad).items()),
                  'K2 of good', sorted(Counter(r[0] for r in rows if r[2]).items()), flush=True)
        if any(r[0] == 0 and r[1] == 0 for r in rows):
            tot['has_max_noK2_noiso'] += 1
        if any(r[0] == 0 for r in rows):
            tot['has_max_noK2'] += 1
    print(n, dict(tot), flush=True)


if __name__ == '__main__':
    main()
