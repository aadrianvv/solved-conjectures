# Conjecture P5\* is false: a 30-vertex counterexample

**Status (2026-11-26, session 5).** A counterexample to Conjecture P5\* of [04g](04g-regular-path-p5-and-m-diamond.md) §4, with a hand proof and an exhaustive independent check. **It is not a counterexample to Conjecture 1 (FGK).** The graph decomposes into 15 simple five-edge paths. So it refutes only the reduction route "Theorem C + P5\* ⇒ degree five". P5\*\* is refuted along with it, because every matching of the graph fails, minimal ones included. Conjecture 1 remains open in degree five.

## Statement

**Proposition I1.** There is a simple 5-regular graph \(G\) on 30 vertices, with a perfect matching, such that for **every** perfect matching \(M\) of \(G\) no fixed-point-free permutations \(r,s\) satisfy (P1)–(P3) and (P5).

## Construction

The block \(B\) has vertex set \(\{0,\dots,8\}\) and the following neighbourhoods:

| vertex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| neighbours | 3 4 5 6 | 3 4 7 8 | 3 4 7 8 | 0 1 2 5 6 | 0 1 2 5 6 | 0 3 4 7 8 | 0 3 4 7 8 | 1 2 5 6 8 | 1 2 5 6 7 |

Vertices \(0,1,2\) have degree 4 in \(B\); the others have degree 5. Each \(a\in\{0,1,2\}\) is joined by a bridge to the root of its own 7-vertex cap \(K_7-\{\rho u_1,\rho u_2,u_3u_4,u_5u_6\}\). Here \(\rho\) is the root, of degree 4 in the cap, and every other cap vertex has degree 5. Then \(G\) is simple and 5-regular on \(9+3\cdot7=30\) vertices.

## Proof

1. **The bridges are forced.** Deleting a bridge leaves its cap, which has 7 vertices, an odd number. So every perfect matching \(M\) contains all three bridges. Hence \(M\cap E(B)\) is a perfect matching of \(B-\{0,1,2\}\).
   - In \(B-\{0,1,2\}\), vertices 3 and 4 are adjacent only to 5 and 6, so 7 must be matched to 8.
   - Therefore \(M\cap E(B)\) is \(\{35,46,78\}\) or \(\{36,45,78\}\).
   - These two are exchanged by the automorphism \(5\leftrightarrow6\) of \(B\), so it suffices to treat \(\{35,46,78\}\).
2. **The B-part is a separate instance.** Every bridge lies in \(M\), so \(H=G-M\) has no edge leaving \(B\).
   - Hence \(r\) and \(s\) restrict to permutations of \(V(B)\), and the conditions at vertices of \(B\) involve only \(B\) and the mates.
   - No triangle contains a bridge, so the M-pairs ("cherries") inside \(B\) come only from \(35,46,78\). They are as follows:
     - \(0\) is an apex of both \(\{3,5\}\) and \(\{4,6\}\), since \(N_H(0)=\{3,4,5,6\}\); so \(0\) is doubly paired (D2);
     - \(1,2,5,6\) are apexes of \(\{7,8\}\);
     - \(N_H(7)=N_H(8)=\{1,2,5,6\}\).
3. **Ω-form.** By [04h](04h-regular-path-p5-reformulations.md) Proposition H2, reverse the \(R\)-arcs. This gives an Euler orientation \(\Omega\) of \(H_B\) with directed 2-factors \(R,T\), subject to two conditions:
   - at a singly paired apex \(x\) with fibre \(Y\), it is not the case that \(r(x)\in Y\) and \(t(x)\notin Y\);
   - at the D2 apex \(0\), the out-pair \(O(0)\) is \(\{3,5\}\) or \(\{4,6\}\).
4. **Senders into \(\{7,8\}\).** All edges at 7 and 8 go to \(\{1,2,5,6\}\). So exactly four arcs enter \(\{7,8\}\), two \(R\) and two \(T\) (one of each into each vertex).
   - An \(R\)-arc \(x\to y\in\{7,8\}\) forces \(t(x)\in\{7,8\}\), so \(O(x)=\{7,8\}\).
   - The two \(R\)-arcs come from distinct vertices, and each of these also sends its \(T\)-arc into \(\{7,8\}\). This uses all four arcs.
   - So exactly two *senders* \(x\in\{1,2,5,6\}\) have \(O(x)=\{7,8\}\). The other two receive both of their \(\{7,8\}\)-edges.
5. **Out-degree count.** Write \(s_x=1\) if \(x\) is a sender, so \(s_1+s_2+s_5+s_6=2\). A sender's two other edges point into it; a non-sender's two other edges point out of it. Let \(e_{30}=1\) if \(3\to0\) and \(e_{40}=1\) if \(4\to0\).
   - Out-degree 2 at vertex 3 (neighbours \(0,1,2,6\)) gives \(s_1+s_2+s_6+e_{30}=2\).
   - Out-degree 2 at vertex 4 (neighbours \(0,1,2,5\)) gives \(s_1+s_2+s_5+e_{40}=2\).
   - At 0, the arc \(0\to5\) occurs iff \(s_5=1\), \(0\to6\) iff \(s_6=1\), \(0\to3\) iff \(e_{30}=0\), and \(0\to4\) iff \(e_{40}=0\).
6. **Contradiction.**
   - If \(O(0)=\{3,5\}\), then \(s_5=1\), \(s_6=0\), \(e_{30}=0\) and \(e_{40}=1\). The equation at 3 gives \(s_1=s_2=1\), so \(\sum s=3\ne2\).
   - The case \(O(0)=\{4,6\}\) is symmetric: the equation at 4 gives \(s_1=s_2=1\).

Both cases are impossible. \(\square\)

## Verification

[check_regular_path_p5star_counterexample.py](check_regular_path_p5star_counterexample.py) runs in about 4 s.

- It builds \(G\) and enumerates all 2,000 perfect matchings of \(G\). Each contains the three bridges, and only the two restrictions to \(B\) above occur.
- For each restriction it brute-forces **all** 142 Euler orientations of the B-part of \(H\) and every choice of \(R\). It checks (P2), (P3) and (P5) from their definitions, without the reformulation and without `p5solve.py`. It finds 0 valid \((r,s)\).
- **Control.** With (P5) removed, the same brute force finds 208 valid \((r,s)\).
- **Conjecture 1 holds for \(G\).** The exact-cover solver of `check_regular_path_decomposition.py` finds 15 simple five-edge paths, and the checker verifies them. The coordinator found a decomposition independently.
- `--full` re-checks all 2,000 matchings with `p5solve.py`.

## Consequences

- **The P5\* route is dead as stated.** Theorem C remains a correct conditional theorem about data \((M,r,s)\), but it cannot reach graphs like \(G\).
- **Bridges do not save the route.** The handoff's cut arithmetic allows a minimal counterexample to Conjecture 1 to have bridges whose small side is a smallest \((d+2)\)-vertex cap. The caps used here are exactly of that kind.
- **More blocks exist.** The search `04-handoff/p5_scratch/blocks.py` enumerates blocks with degree-4 attachment vertices, each attached by a bridge. It found more P5\*-counterexample blocks:
  - a second block of order 9 with 3 attachments;
  - two blocks of order 10 with 4 attachments.

  It found none for the cases \((n_B,|A|)\) = (7,1), (8,2), (8,4), (9,1), (9,5) and (10,2). Completeness of these searches rests on the orderly generator, which is a copy of the census generator with a degree list; it was not independently checked.

## Rescue routes (evidence only)

- **(a) Bridgeless graphs.** No bridgeless counterexample is known. Targeted searches found nothing:
  - no 2-attachment block of order 8 or 10 has all its matchings infeasible;
  - no "forced" block exists for (9,3), (8,2), (8,4) or (10,2), meaning a block in which every perfect matching of a host graph must use all cut edges;
  - gluing two copies of the counterexample block along a 3-edge cut gives three 18-vertex graphs, one per gluing. All matchings using the three cut edges are infeasible, but each graph has feasible matchings using one cut edge: 1,024, 1,024 and 1,056 of them. So P5\* holds for all three graphs (`glue2.py`).

  A rescue would need P5\* for bridgeless graphs together with a separate reduction for bridges to smallest caps. That reduction is equivalent in difficulty to Kouider–Lonc-type balanced decompositions (see the handoff).
- **(b) Weak (P5).** Drop the cherry conditions at apexes that are bridge ends.
  - In the counterexample, dropping the condition at a single bridge-end apex (0 or 1) already restores feasibility.
  - With the cherry conditions dropped at bridge-end apexes, `blocks_weak.py` found **no** counterexample block among all blocks for (7,1), (8,2), (8,4), (9,1), (9,3), (9,5), (10,2) and (10,4). This includes the cases where P5\*-counterexample blocks exist.

  Using (b) would require extending Theorem C's windows by (P5)-violations at bridge-end apexes. These are R-paths \(u\to a\to m(u)\) with \(a\) a bridge end, whose own \(M\)-edge is the bridge. Then one would need "weak P5\*" for all graphs, which is unproved.
- **Locality (relevant to any switching proof).** At \(n=14\) there is an infeasible \(M\) whose shortest incidence-reducing alternating cycle has 5 \(M\)-edges, and none of length \(\le8\) reduces the count. A second program confirms the infeasibility by enumerating 2-factorizations. The instance and the script are in `04-handoff/p5_scratch/loc6.py` and `chkmin.py`. So any exchange argument must use alternating cycles of unbounded length.
