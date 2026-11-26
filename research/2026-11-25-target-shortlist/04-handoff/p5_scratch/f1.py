from collections import Counter
import check_regular_path_p5sweep as P
tally = Counter()
for aopt in P.PEND:
    for a2opt in P.PEND:
        sc = P.Sc("F1")
        c, d, b, e, a, dl, mu, u = P.gamma_base(sc)
        sc.s(mu, c); sc.r("f", c); sc.m("f", "dX"); sc.r("dX", mu)
        P.pendant(sc, b, aopt, "1", plain_name=a)
        A = a if aopt == "plain" else ("bsP1" if aopt == "type1" else "eQ1")
        P.pendant(sc, u, a2opt, "2", plain_name="su")
        A2 = "su" if a2opt == "plain" else ("bsP2" if a2opt == "type1" else "eQ2")
        before = [(A, b, e, d, c, e), (A2, u, d, dl, mu, c), (b, c, "f", "dX", mu, u)]
        P.find_rules(sc, before, [(A, b), (A2, u)], tally, f"F1 A={aopt} A'={a2opt}")
