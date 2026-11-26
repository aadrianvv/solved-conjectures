from collections import Counter, defaultdict
from functools import cache


def identifications(labels, vertices):
    if not labels:
        yield ()
        return
    for v in range(vertices + 1):
        for suffix in identifications(labels[1:], max(vertices, v + 1)):
            yield (v,) + suffix


def undirected(p):
    return tuple(tuple(sorted(pair)) for pair in zip(p, p[1:]))


def valid_canonical(t, q):
    if len(set(q)) < 6 and (len(set(q)) != 5 or (q[0] != q[4] and q[1] != q[5])):
        return False
    if len(set(undirected(t) + undirected(q))) != 10:
        return False
    match = tuple(path[2:4] for path in (t, q))
    if len({v for edge in match for v in edge}) != 4:
        return False
    for pos in (2, 1):
        arcs = tuple((path[pos], path[pos-1]) for path in (t,q)) + tuple((path[5-pos], path[6-pos]) for path in (t,q))
        for side in (0, 1):
            if len({arc[side] for arc in arcs}) != 4:
                return False
    return all(a != b for a,b in undirected(q))


def cover(edges):
    target = (1 << len(edges)) - 1
    adj = defaultdict(list)
    for idx,(v,w) in enumerate(edges):
        adj[v].append((w,idx))
        adj[w].append((v,idx))
    poss = [[] for e in edges]
    def walk(path, emask):
        if len(path) == 6:
            if path[0] < path[-1]:
                for i in range(len(edges)):
                    if emask >> i & 1:
                        poss[i].append((emask, path))
            return
        for w,i in adj[path[-1]]:
            if w not in path:
                walk(path + (w,), emask | (1 << i))
    for v in adj:
        walk((v,), 0)
    @cache
    def solve(mask):
        if mask == target:
            return ()
        options = min(([p for p in poss[i] if not p[0] & mask]
                     for i in range(len(edges)) if not (mask >> i & 1)), key=len)
        for emask,p in options:
            tail = solve(mask | emask)
            if tail is not None:
                return (p,) + tail
        return None
    result = solve(0)
    if result is not None:
        assert all(len(path) == len(set(path)) == 6 for path in result)
        assert Counter(edge for path in result for edge in undirected(path)) == Counter(edges)
    return result

if __name__ == "__main__":
    t = (0,1,2,3,4,1)
    counts = Counter()
    for x,f,g,h,y in identifications("xfghy", 5):
        q = (x,2,f,g,h,y)
        if not valid_canonical(t,q):
            continue
        good = len(set(q)) == 6
        dec = cover(undirected(t) + undirected(q))
        alpha = (0,1,4,3,2,x), (1,2,f,g,h,y)
        alpha_good = all(len(set(p)) == 6 for p in alpha)
        counts[good,dec is not None,alpha_good,len(set(t+q))] += 1
        if dec is None:
            print("blocked",good,q)
    print(counts)
