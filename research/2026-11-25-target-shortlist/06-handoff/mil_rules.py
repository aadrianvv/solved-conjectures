"""Test secondary selection rules on maximum MIL partitions (third session).

For each graph, all maximum MIL partitions are enumerated and tested for designations.
A rule is a lexicographic key on component statistics; the rule 'fails' on a graph if
some partition minimising the key is infeasible.
Usage: python mil_rules.py exhaustive N DIR | random N SAMPLES SEED
"""
import sys
from collections import Counter

from mil_sat import all_max_mil, designate, random_cubic


def stats(adj, Y):
    n = len(adj)
    Ys = set(Y)
    X = [v for v in range(n) if v not in Ys]
    seen = set()
    sizes = []
    for v in X:
        if v in seen:
            continue
        st = [v]
        seen.add(v)
        c = 0
        while st:
            a = st.pop()
            c += 1
            for b in adj[a]:
                if b not in Ys and b not in seen:
                    seen.add(b)
                    st.append(b)
        sizes.append(c)
    C = Counter(sizes)
    return {
        'k2': C.get(2, 0),
        'iso': C.get(1, 0),
        'even': sum(v for k, v in C.items() if k % 2 == 0 and k >= 4),
        'evenall': sum(v for k, v in C.items() if k % 2 == 0),
        'long': sum(k * k for k in sizes),
        'maxlen': max(sizes),
    }


RULES = {
    'none': lambda s: 0,
    'k2': lambda s: s['k2'],
    'k2,even': lambda s: (s['k2'], s['even']),
    'evenall': lambda s: s['evenall'],
    'evenall,k2': lambda s: (s['evenall'], s['k2']),
    'k2,-iso': lambda s: (s['k2'], -s['iso']),
    'k2,iso': lambda s: (s['k2'], s['iso']),
    'k2,long': lambda s: (s['k2'], s['long']),
    'k2,-long': lambda s: (s['k2'], -s['long']),
    'k2,maxlen': lambda s: (s['k2'], s['maxlen']),
}


def main():
    mode = sys.argv[1]
    if mode == 'exhaustive':
        from cubic_gen import load
        n = int(sys.argv[2])
        graphs = load(n, sys.argv[3])
    else:
        n, S, seed = map(int, sys.argv[2:5])
        graphs = [random_cubic(n, seed + i) for i in range(S)]
    fails = Counter()
    nofeas = 0
    for gi, adj in enumerate(graphs):
        L = all_max_mil(adj, limit=20000)
        rows = [(stats(adj, Y), designate(adj, Y) is not None) for Y in L]
        if not any(f for _, f in rows):
            nofeas += 1
            print('graph', gi, 'has no feasible maximum partition', flush=True)
            continue
        for name, key in RULES.items():
            best = min(key(s) for s, _ in rows)
            if any(not f for s, f in rows if key(s) == best):
                fails[name] += 1
                if name in ('k2', 'evenall,k2'):
                    print('rule', name, 'fails on graph', gi, [sorted(a) for a in adj], flush=True)
    print('order', n, 'graphs', len(graphs), 'no feasible max', nofeas, 'rule failures', dict(fails), flush=True)


if __name__ == '__main__':
    main()
