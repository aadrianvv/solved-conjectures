# Independent SAT check (different encoding from verify_sat.py): does K_n - uv (n = d+1) have a proper n-edge-colouring
# whose tight digraph is acyclic?  Acyclicity is encoded by a potential L: E -> {0..N-1} (order encoding,
# y[e][k] <=> L(e) >= k), with L(f) >= L(e)+1 for every arc e -> f.  A finite digraph is acyclic iff such an L exists.
import sys, time, itertools
from pysat.solvers import Solver
from pysat.card import CardEnc
def run(d, extra_sym=True):
    n = d+1; E = [(a, b) for a in range(n) for b in range(a+1, n) if (a, b) != (0, 1)]; N = len(E)
    top = [0]
    def new():
        top[0] += 1; return top[0]
    X = [[new() for c in range(n)] for e in E]
    Y = [[None] + [new() for k in range(1, N)] for e in E]   # Y[e][k], k=1..N-1 : L(e) >= k
    cl = []
    for e in range(N):
        cl.append(X[e][:])
        for c1, c2 in itertools.combinations(range(n), 2): cl.append([-X[e][c1], -X[e][c2]])
        for k in range(2, N): cl.append([-Y[e][k], Y[e][k-1]])
    for e, f in itertools.permutations(range(N), 2):
        if not set(E[e]) & set(E[f]): continue
        for c in range(n):
            if e < f: cl.append([-X[e][c], -X[f][c]])
            a, b = X[e][c], X[f][(c+1) % n]
            cl.append([-a, -b, Y[f][1]])
            for k in range(1, N-1): cl.append([-a, -b, -Y[e][k], Y[f][k+1]])
            cl.append([-a, -b, -Y[e][N-1]])
    if extra_sym: cl.append([X[E.index((0, 2))][0]])
    t = time.time()
    with Solver(name='cadical153', bootstrap_with=cl) as s:
        r = s.solve()
        model = s.get_model() if r else None
    res = "SAT" if r else "UNSAT"
    if r:
        m = set(x for x in model if x > 0)
        col = {E[e]: next(c for c in range(n) if X[e][c] in m) for e in range(N)}
        res += " example " + str(col)
    print("d=%d: %s  (%d vars, %d clauses, %.1fs)" % (d, res, top[0], len(cl), time.time()-t), flush=True)
for d in map(int, sys.argv[1:]): run(d)
