# (P5) feasibility: exact reformulations, sufficient conditions and data (session 5)

**Status (2026-11-26, session 5).** Research note on Conjecture P5\* / P5\*\* of [04g](04g-regular-path-p5-and-m-diamond.md) §4. **Superseded in part: P5\* (hence P5\*\*) is false; see [04i](04i-regular-path-p5star-counterexample.md).** The reformulations below remain valid; 04i's hand proof uses Proposition H2. This note proves three exact reformulations of (P1)–(P3)+(P5) (Propositions H1–H3), isolates the purely orientational part of the problem, records which natural sufficient conditions hold and which fail, and gives new evidence. Random and family runs are evidence only. Conjecture 1 remains open in degree five.

Notation: \(G\) 5-regular with perfect matching \(M\), \(H=G-M\) (4-regular), \(m\) the mate map. A *fibre* is an \(M\)-edge \(Y=\{y,y'\}\). A vertex \(x\) is an *apex* of \(Y\) if \(xy,xy'\in E(H)\) (the M-pair, or *cherry*, \(\{xy,xy'\}\) at \(x\)); \(B(x)\) is the union of the fibres of which \(x\) is an apex. A vertex is *singly* or *doubly* (D2) paired if it is an apex of one or two fibres. The number of M-pair incidences equals the number of triangles through an \(M\)-edge.

## 1. Exact reformulations

**Proposition H1 (local form).** Choosing \((r,s)\) with (P1)–(P2) is the same as choosing an Euler orientation of \(H\) and a decomposition of it into two directed 2-factors \(R\) (arcs \(u\to r(u)\)) and \(S\) (arcs \(s(w)\to w\)). Write the four roles at a vertex as \(R_i,R_o,S_i,S_o\). Then (P3)+(P5) hold iff **at every cherry \(\{xy,xy'\}\) at \(x\), if one edge is the \(R\)-in edge at \(x\), the other is the \(S\)-out edge at \(x\).** Equivalently: for every \(x\), if \(m(r^{-1}(x))\in N_H(x)\) then \(s^{-1}(x)=m(r^{-1}(x))\).

*Proof.* The first sentence is 04g §1. (P3) at the cherry forbids the role sets \(\{R_i,S_i\}\) (both arcs into \(x\); \(\{R_i,R_i\}\) etc. are impossible); (P5) forbids \(\{R_i,R_o\}\). Of the six role pairs these are exactly the two containing \(R_i\) other than \(\{R_i,S_o\}\). \(\square\)

So at a D2 vertex the roles are forced up to the choice of which cherry carries \(R_i\): the cherries are \(\{R_i,S_o\}\) and \(\{R_o,S_i\}\).

**Proposition H2 (Ω-form).** Reversing every \(R\)-arc is a bijection between such data and pairs \((\Omega;R,T)\): \(\Omega\) an Euler orientation of \(H\), \(R,T\) directed 2-factors of \(\Omega\) with successor maps \(r,t\) (\(T\) is \(S\), unchanged; \(R\) is reversed). In this form the condition reads:

- at a singly paired apex \(x\) with fibre \(Y\): **not (\(r(x)\in Y\) and \(t(x)\notin Y\))**;
- at a D2 apex with fibres \(Y,Z\): **\(\{r(x),t(x)\}\in\{Y,Z\}\)**, i.e. both edges of one cherry leave \(x\) and both edges of the other enter it.

*Proof.* Under the reversal the roles \(R_i,R_o\) are exchanged, so H1 becomes "the pair partner of the \(R\)-out edge is the \(T\)-out edge". At a singly paired apex this says: if \(r(x)\in Y\) then \(t(x)=m(r(x))\); since \(t(x)\ne r(x)\), this is "\(r(x)\notin Y\) or \(t(x)\in Y\)". At a D2 apex \(r(x)\in Y\cup Z\) always, so \(t(x)=m(r(x))\). \(\square\)

The D2 condition involves **only the orientation \(\Omega\)**, not the colouring.

**Proposition H3 (trail form).** Fix \(\Omega\). Its *antidirected trails* (at each vertex pair the two out-arcs and the two in-arcs) are the cycles of the bipartite graph \(B_\Omega\) (out-copies against in-copies). Colourings \((R,T)\) correspond exactly to choosing, on each antidirected trail, which of its two alternate edge classes is \(T\). Then (P1)–(P3)+(P5) hold iff

1. every D2 apex has both cherries aligned (one both-out, one both-in); and
2. for every singly paired apex \(x\) whose cherry is **cross** in \(\Omega\) (one edge \(x\to p\) out, one in), the antidirected trail through the out-pair of \(x\) puts \(x\to p\) in \(T\); these unit demands are consistent on every trail (demanded edges at even distance along the trail).

Aligned cherries at singly paired apexes impose nothing. *Proof.* Immediate from H2: if the cherry is both-out, \(\{r(x),t(x)\}=Y\); if both-in, \(r(x)\notin Y\); if cross with out-edge \(x\to p\), the only violation is \(r(x)=p\). \(\square\)

**Consequences.**

- **(S) aligned orientation.** If \(H\) has an Euler orientation in which every cherry is aligned at its apex, \(M\) admits (P5) with *every* colouring. (S) is equivalent to a \(\mathbb Z_2\) system on apexes plus an Euler completion: with \(s(x)\) = "cherry out", an \(H\)-edge between apexes \(u,v\) forces \(s(u)+s(v)=1+c_u+c_v\) (\(c\) = "edge is a cherry edge at that end"), so (S) needs every cycle \(Z\) of the apex subgraph to satisfy \(|Z|+\#\{\text{vertices where }Z\text{ switches between cherry and non-cherry edges}\}\equiv0\), plus a Hakimi completion at non-apexes.
- **Given an oriented \(T\)** (any directed 2-factor of \(H\)), all remaining conditions are *unit* constraints on the orientations of the cycles of \(R=H-T\) (or contradictions). Symmetrically for oriented \(R\). So for a fixed 2-factorization the problem is 2-SAT whose clauses join an \(R\)-cycle and an \(S\)-cycle at each mixed cherry, and D2 apexes give equivalences.
- Two uniform strategies make every singly paired apex free: **TC** (\(t(x)\in Y\) at each singly paired apex) and **R0** (\(r(x)\notin Y\)). H2 says the full condition at a singly paired apex is exactly "TC or R0 holds locally".
- **(P5) holds for every \((r,s)\) when no \(M\)-edge lies in a triangle** (no cherries), recovering 04d Corollary 4.

## 2. Data (evidence; exact CSP per instance)

Scripts in `04-handoff/p5_scratch/` (`an*.py`, `aligned.py`, `r0.py`, `tc.py`, `modes.py`, `core.py`, `circ.py`).

| test | result |
|---|---|
| all graphs of orders 8, 10, all matchings: infeasible \((G,M)\) vs. max triangles per \(M\)-edge | every infeasible \(M\) has an \(M\)-edge in \(\ge3\) triangles (orders 8, 10 only) |
| random/dense, \(n=12,14\), matchings with every \(M\)-edge in \(\le2\) triangles | **false in general**: 5 infeasible of 23,079 (all non-minimal; some with no D2 vertex) |
| **every \(M\)-edge in \(\le1\) triangle** (maxt ≤ 1), \(n=10\)–\(16\), random, square, dense, K5-block | **feasible in all 13,382 instances** (two seeds) |
| (S) aligned orientation, all graphs \(n\le10\) | fails: 2 of 3 order-8 graphs have **no** matching with (S); also fails often under maxt ≤ 1 |
| TC (all graphs \(n=8,10\)) | 1 order-8 and 1 order-10 graph have no TC matching |
| **R0** (all graphs \(n=8,10\)) | **every graph has a matching with R0**; R0 fails for some minimum matchings (6 order-10 graphs) |
| TC / R0 restricted to maxt ≤ 1 (random \(n=10\)–\(16\)) | each fails occasionally (TC: 8 of 663 instances without D2 vertices; R0: 4 of 735), while full (P5) never failed |
| minimal unsatisfiable cores (all infeasible \(M\), \(n=8,10\)) | smallest cores have 4 cherries: a fibre \(Y\) with two apexes \(a,b\), each of \(y,y'\) itself an apex of another fibre; cores are global (they need the whole Euler/2-factor structure) |
| P5\*\* on all 210 5-regular circulants \(C_n(a,b,n/2)\), \(12\le n\le24\), up to 12 minimum matchings each | 1,889/1,889 minimum matchings feasible |

All infeasible instances found so far are non-minimal (consistent with P5\*\*).

## 3. Where a proof could go

1. **Class theorem (target):** *if every \(M\)-edge lies in at most one triangle, \(M\) admits (P5).* With Theorem C this would give decompositions for all such graphs, strictly containing Theorem B′ (which also forbids \(M\)-side diamonds). Under this hypothesis distinct apexes have disjoint cherry fibres. Neither uniform strategy (S), TC, R0 suffices, so a proof must mix them (per-apex choice "TC or R0", i.e. H3 demands). Not yet proved.
2. **P5\*\* by switching:** an infeasibility certificate is a global 2-SAT/parity object (cores above), so the alternating-cycle exchange must be extracted from a global obstruction; no candidate exchange found yet.
3. **Weighted-orientation view of (S):** splitting each apex into its two cherry groups joined by a doubled virtual edge, (S) is an orientation in which every virtual edge carries flow \(\pm2\) (never 0): a nowhere-zero-type condition; cross cherries (flow 0) are allowed only at singly paired apexes and cost a unit demand (H3).
