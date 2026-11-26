"""Session 6 scratch: (P1)-(P3)+(P5) CSP with restricted role sets at apexes (original orientation).
Roles of an H-edge at a vertex: 'Ri','Ro','Si','So'.  A cherry at apex x = pair of H-edges xy,xy' with yy' in M.
allowed: function(kind, roles_of_cherry_as_frozenset) -> bool, kind in {'single','d2'}.
"""
import sys
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist")
sys.path.insert(0, r"C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/04-handoff/p5_scratch")
from itertools import combinations, permutations
BAD = {frozenset(('Ri', 'Si')), frozenset(('Ri', 'Ro'))}
ROLESETS = [p for p in permutations(('Ri', 'Ro', 'Si', 'So'))]

def cherries(adj, m):
    n = len(adj)
    H = [sorted(w for w in adj[v] if w != m[v]) for v in range(n)]
    ch = [[(y, z) for y, z in combinations(H[x], 2) if m[y] == z] for x in range(n)]
    return H, ch

def solve(adj, m, allowed=None, node_limit=10**6, rng=None):
    n = len(adj)
    H, ch = cherries(adj, m)
    doms = []
    for x in range(n):
        kind = 'd2' if len(ch[x]) == 2 else 'single'
        d = []
        for perm in ROLESETS:
            role = dict(zip(H[x], perm))
            good = True
            for y, z in ch[x]:
                rs = frozenset((role[y], role[z]))
                if rs in BAD or (allowed and not allowed(kind, rs)):
                    good = False; break
            if good:
                d.append(role)
        if rng: rng.shuffle(d)
        doms.append(d)
    comp = {('Ri', 'Ro'), ('Ro', 'Ri'), ('Si', 'So'), ('So', 'Si')}
    asg = [None] * n
    cur = [list(d) for d in doms]
    nodes = [0]
    def rec():
        nodes[0] += 1
        if nodes[0] > node_limit: raise TimeoutError
        best = None
        for v in range(n):
            if asg[v] is None and (best is None or len(cur[v]) < len(cur[best])):
                best = v
        if best is None: return True
        v = best
        for a in cur[v]:
            asg[v] = a; saved = []; ok = True
            for w in H[v]:
                if asg[w] is None:
                    saved.append((w, cur[w]))
                    cur[w] = [b for b in cur[w] if (a[w], b[v]) in comp]
                    if not cur[w]: ok = False; break
            if ok and rec(): return True
            for w, d in reversed(saved): cur[w] = d
            asg[v] = None
        return False
    if not rec(): return None
    return asg

def to_rs(adj, m, asg):
    n = len(adj); r = {}; s = {}
    for v in range(n):
        for w, ro in asg[v].items():
            if ro == 'Ro': r[v] = w
            if ro == 'Si': s[v] = w
    return r, s

def verify(adj, m, r, s):
    n = len(adj)
    rinv = {v: u for u, v in r.items()}
    E = set()
    for v in range(n):
        assert r[v] in adj[v] and s[v] in adj[v]
        assert r[r[v]] != v and s[s[v]] != v
        assert s[r[v]] != m[v]
        assert m[rinv[v]] != r[v]
        for e in ((v, r[v]), (v, s[v]), (v, m[v])): E.add(frozenset(e))
    assert len(E) == 5 * n // 2
    assert sorted(r.values()) == list(range(n)) and sorted(s.values()) == list(range(n))

STRATS = {
    'full': None,
    'cross': lambda k, rs: k == 'd2' or rs in {frozenset(('Ri','So')), frozenset(('Ro','Si')), frozenset(('Si','So'))},
    'trans': lambda k, rs: k == 'd2' or rs in {frozenset(('Ri','So')), frozenset(('Ro','Si')), frozenset(('Ro','So'))},
    'transcross': lambda k, rs: k == 'd2' or rs in {frozenset(('Ri','So')), frozenset(('Ro','Si'))},
    'outorS': lambda k, rs: k == 'd2' or rs in {frozenset(('Ro','So')), frozenset(('Si','So'))},
    'noRi': lambda k, rs: k == 'd2' or 'Ri' not in rs,
    'So': lambda k, rs: k == 'd2' or 'So' in rs,
}
