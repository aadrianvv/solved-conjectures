# The one-triangle class for (P5): exact statement, proved reformulations, evidence (session 6)

**Status (2026-11-26, session 6).** Research note. **The class theorem is neither proved nor refuted.** This note pins down the exact statement, proves three reformulations that any proof can use, records an exhaustive small-order check of a strictly stronger abstract statement, and says why each uniform construction fails. No new decomposition theorem is claimed. Conjecture 1 (FGK) remains open in degree five.

Notation follows [04g](04g-regular-path-p5-and-m-diamond.md) and [04h](04h-regular-path-p5-reformulations.md): \(G\) is simple and 5-regular, \(M\) a perfect matching, \(H=G-M\) (4-regular), \(m\) the mate map. A *cherry* at an apex \(x\) is a pair of \(H\)-edges \(xy,xy'\) with \(yy'\in M\). Its *K-arcs* are \(x\to y\) and \(x\to y'\), pointing away from the apex. The *targets* of the cherry are \(y\) and \(y'\).

## 1. Exact statement

**Conjecture J (one-triangle class).** Let \(M\) be a perfect matching of a simple 5-regular graph \(G\) such that every edge of \(M\) lies in at most one triangle of \(G\). Then there are fixed-point-free permutations \(r,s\) satisfying (P1)–(P3) of 04d and (P5) of 04g: \(m(r^{-1}(x))\ne r(x)\) for all \(x\).

- **What Theorem C consumes.** Theorem C (04g §3.1, reviewed) assumes exactly (P1)–(P3) and (P5) for the given \((M,r,s)\). It has no hypothesis on bridges, caps, D-chains or connectivity. So Conjecture J would give the **conditional corollary**: *every simple 5-regular graph with a perfect matching \(M\) in which every \(M\)-edge lies in at most one triangle decomposes into paths with five edges.* The weak (P5) of 04i (cherries at bridge-end apexes ignored) is **not** what Theorem C consumes, and it is not used here.
- **Hypothesis in cherry language.** A triangle through \(yy'\in M\) is the same as a cherry with targets \(\{y,y'\}\). So the hypothesis says that each fibre has at most one apex. Since the fibres partition \(V\), this is equivalent to **(K1): every vertex is a target of at most one cherry**, i.e. the K-arcs have pairwise distinct heads. Consequences:
  - at most \(n/2\) cherries;
  - an apex has one cherry (single) or two (D2), and these are disjoint;
  - an edge may carry K-arcs in both directions (a *mutual* edge: \(x\) is an apex of \(\{z,m(z)\}\) and \(z\) of \(\{x,m(x)\}\)).
- **Relation to B′.** Theorem B′ (no diamond through an \(M\)-edge) lies strictly inside the class. An \(M\)-chord diamond puts an \(M\)-edge in two triangles, so it is excluded by both hypotheses. An \(M\)-side diamond, such as a mutual edge, is allowed here but not in B′. Example (\(n=10\)): \(N(0)=\{1,2,3,4,8\}\), \(N(1)=\{0,2,6,7,8\}\), \(N(2)=\{0,1,3,4,5\}\), \(N(3)=\{0,2,6,7,9\}\), \(N(4)=\{0,2,5,7,9\}\), \(N(5)=\{2,4,6,7,8\}\), \(N(6)=\{1,3,5,8,9\}\), \(N(7)=\{1,3,4,5,9\}\), \(N(8)=\{0,1,5,6,9\}\), \(N(9)=\{3,4,6,7,8\}\), \(M=\{04,89,17,23,56\}\). Here \(02\) and \(68\) are mutual edges, every \(M\)-edge lies in at most one triangle, and (P5) is feasible.

### 1.1 The recorded "at most two triangles" counterexamples, and why one triangle blocks them

The five instances are in `04-handoff/p5_scratch/c12.log`: four at \(n=12\) and one at \(n=14\), from `an3.py`. In each, every \(M\)-edge lies in at most two triangles, and no \((r,s)\) exists.

`04-handoff/p6_scratch/core12.py` computes a minimal unsatisfiable set of cherry constraints for each instance, using `core.py`.

- **Every core contains a fibre with two apexes.** The typical core has four cherries. A fibre \(\{y,y'\}\) has two apexes \(a,b\), and \(y\) and \(y'\) are themselves apexes of other fibres that have two apexes. Example: the core \((2;8,10),(3;8,10),(8;1,11),(10;6,9)\).
- **In the class, this local pattern is impossible by (K1).** That is the mechanism the class removes.
- **This is not a proof.** 04h shows that the cores are global: they need the whole Euler/2-factor structure. The absence of these particular cores does not by itself imply feasibility.
- **The 04i counterexample to P5\* is also outside the class.** Its fibre \(\{7,8\}\) has the four apexes \(1,2,5,6\).

## 2. Proved reformulations

**Lemma J1 (2-factor form).** For a given \(M\), the following are equivalent:

- (i) there exist \(r,s\) with (P1)–(P3) and (P5);
- (ii) there is a 2-factorization \(E(H)=F_R\sqcup F_S\) and an orientation of every cycle of \(F_R\) and \(F_S\) such that
  - (a) no cherry has both edges in \(F_R\), and
  - (b) no cherry has both edges directed into its apex.

*Proof.* By 04h H1, (P1)–(P2) is the same as a directed 2-factorization \((R,S)\) of an Euler orientation of \(H\). Simplicity of \(H\) excludes 2-cycles, which is (P2). This is the same as a 2-factorization together with cycle orientations.

At an apex \(x\), let the roles of a cherry's two edges be taken from \(\{R_i,R_o,S_i,S_o\}\).

- (P5) forbids \(\{R_i,R_o\}\), which happens exactly when the cherry lies in \(F_R\). This gives (a).
- (P3) forbids \(\{R_i,S_i\}\). Vertex \(x\) has exactly two in-arcs, one in \(R\) and one in \(S\), so this happens exactly when the cherry is both-in. This gives (b).

All other role pairs are allowed (04h H1). \(\square\)

So (P5) depends only on the undirected factor \(F_R\), and (P3) only on the orientation. In (b), "both-in" means that both K-arcs of the cherry are reversed.

**Lemma J2 (two linear sub-problems).** Label the allowed cherry role sets
A \(=\{R_i,S_o\}\), B \(=\{R_o,S_i\}\), C \(=\{R_o,S_o\}\) (both-out) and D \(=\{S_i,S_o\}\) (cherry \(\subseteq F_S\)). At a D2 apex only A/B and B/A are possible.

- (*cross*, options ABD, i.e. every cherry is one-in one-out). **For a fixed 2-factorization with no cherry in \(F_R\), the remaining condition is a system of \(\mathbb Z_2\) equations on the cycle orientations.** Each cherry with one edge in each factor gives one equation, between its \(R\)-cycle and its \(S\)-cycle, saying that exactly one of the two edges enters \(x\). A cherry inside \(F_S\) gives nothing. The two equations at a D2 apex coincide.
- (*trans*, options ABC, i.e. \(F_R\) contains exactly one edge of every cherry). **For a fixed Euler orientation \(\Omega\) with no cherry both-in, the remaining condition is a \(\mathbb Z_2\) system on the phases of the antidirected trails** (the cycles of \(B_\Omega\), 04h H3). For each cross cherry with in-arc \(a\) and out-arc \(b\), it requires \([a\in R]+[b\in R]=1\). Both-out cherries impose nothing.

*Proof.*

- **Cross.** With the factors fixed, a cherry with one edge in each factor is cross iff the orientations of its two cycles satisfy one linear relation. That relation is fixed by the reference orientations.
- **Trans.** Each antidirected trail alternates \(R/S\) and has two phases. \([a\in R]\) is an affine function of the phase of the trail through \(a\).
- **D2.** In the cross case, at a D2 apex the cycle through \(x\) enters through one cherry iff it leaves through the other, so the second equation equals the first. \(\square\)

**Lemma J3 (interlace criterion).** Let \(W\) be an Euler circuit of \(H\), oriented along \(W\), with interlace graph \(I\) (vertices \(u,v\) adjacent iff they alternate along \(W\)). Colour the arcs so that the colour changes at the pass through \(v\) iff \(t_v=1\). This colouring is a directed 2-factorization \((R,S)\) iff
```math
(A_I+\mathrm{Id})\,t=\mathbf 1\quad\text{over }\mathbb F_2 .
```
*Proof.*

- **Closure.** The total number of colour changes around \(W\) is \(\sum_v 2t_v\), which is even, so the colouring closes up.
- **Validity at a vertex.** Let \(x\) have in-arcs at positions \(k<l\). Validity at \(x\) means the two in-arcs have different colours. The out-colours then differ automatically, because both passes turn iff \(t_x=1\).
- **The in-colour difference.** The colour difference between positions \(k\) and \(l\) is the sum of \(t\) over the passes between them, counting \(x\)'s first pass. Vertices visited twice in that segment contribute \(0\). So the difference is \(t_x+\sum_{v\sim_I x}t_v\), which must equal 1. \(\square\)

`04-handoff/p6_scratch/interlace_check.py` checked the criterion against direct validation for all \(t\) on random circuits: 4,800 colourings, 0 mismatches.

**Corollary J3′ (solvability with prescribed turns).** Let \(P\subseteq V\). Write \(N=A_I+\mathrm{Id}\), a symmetric matrix with unit diagonal. A solution of \(Nt=\mathbf 1\) with \(t_P=\mathbf 1\) exists iff, for every \(z\) with \(\operatorname{supp}(Nz)\subseteq P\),
```math
\sum_{j\in z}\deg_I(j)\equiv 0 \pmod 2 .
```
*Proof.* By duality, a solution exists iff \(\mathbf 1\cdot z=(Nz)_P\cdot\mathbf 1_P\) whenever \((Nz)_{V\setminus P}=0\).

- The left side is \(|z|\).
- The right side is \(|Nz|=|z+A_Iz|\equiv|z|+|A_Iz|\pmod 2\).
- \(|A_Iz|\equiv\sum_{j\in z}\deg_I(j)\pmod 2\).

Comparing the two sides gives the criterion. For \(P=\emptyset\) this is Sutner's theorem that \(Nt=\mathbf 1\) is always solvable. \(\square\)

Take \(W\) through the cherry transitions at every apex; this is Lemma 1 of 04d, so every cherry is a pass and therefore cross. Then the strategy *transcross* (options AB) is exactly \(t_P=\mathbf 1\) for the set \(P\) of apexes. J3′ is its exact obstruction, and the data below show that the obstruction does occur. The D option, which turns \(t_x\) to 0 at a single apex whose cherry pass is coloured \(S\), adds one affine condition per such apex.

## 3. Evidence (computational; not proof)

Scripts are in `04-handoff/p6_scratch/`. "Abstract" instances replace \((G,M)\) by an arbitrary 4-regular \(H\) and any cherry system satisfying (K1). This is strictly more general than Conjecture J, because a cherry system need not come from a perfect matching and its triangles.

| test | result |
|---|---|
| **abstract, exhaustive** (`exhaust.py`): every 4-regular simple graph of order \(5\)–\(10\) from the census generator, every *maximal* (K1) cherry system with non-adjacent targets | **all feasible**: 1, 64, 405, 4,472, 21,797 and 189,673 systems at orders 5–10 (60 graph labels at order 10; the generator may repeat classes) |
| abstract, exhaustive, targets allowed adjacent, orders 5–8 | all feasible (135, 224, 1,763, 7,972 systems) |
| abstract random (`abstract_rand.py`), orders 7–12, maximal (K1) systems | 2,987/2,987 feasible; control with shared targets (orders 7–10): 51 of 992 infeasible |
| real planted class instances (`plant.py`, `exp2.py`), \(n=10\)–24, average about 8 cherries | 984/984 feasible, for *full*, *cross* and *trans* alike |
| real class instances from triangle-rich generators (`exp1.py`) | 175/175 feasible; *outorS* (CD) failed 2, *transcross* (AB) failed 10 |
| strategy sweep, abstract (`stratabs.py`, 1,499 instances) | *cross* ABD 1,499/1,499; *trans* ABC **2 failures**; ACD (TC) and BCD (R0) 442 failures each |
| fixed random Euler orientation with all cherries cross (`anyomega.py`, `anyomega2.py`) | a valid \(R\) fails for about 30% of orientations, and for about 22% without D2 apexes. **The orientation must be chosen.** |
| transcross failures (`oneD.py`, 400 abstract instances) | 289 transcross-feasible; of the other 111, 105 are fixed by allowing D at one single apex and 6 need two |
| 2-port gadgets (2-edge-cut sides, `gadget.py`, 300) | every gadget realises all 4 interface states |
| 4-port gadgets (`gadget4.py`, `pairs4.py`, 200) | interface sets of size 27–36 out of 36; no incompatible pair under any of the 24 gluings |
| pair flexibility (`flex.py`) | 2 of 6,378 edge pairs are forced to have equal colours, so "any two edges can be coloured differently" is **false**. This blocks the naive vertex-splitting induction. |
| solution counts (`count.py`) | the fraction of directed 2-factorizations that are valid is close to \((2/3)^{\#\text{single}}(1/3)^{\#D2}\); no parity pattern |

The exhaustive abstract check through order 10 subsumes the 5-regular census of 04g §4 for the class at orders 8 and 10.

## 4. Why the proof attempts stopped

1. **Uniform strategies are refuted by data.**
   - Strategies with fewer options than the two minimal successful sets fail: TC, R0, (S), transcross, and CD. Among the minimal sets, only *cross* (ABD) never failed; *trans* (ABC) has 2 abstract failures.
   - So any proof must make **non-uniform, globally coordinated** choices at single apexes.
2. **Each layer alone is linear, but the layers are coupled.**
   - By J2, cross is linear once the 2-factorization is fixed, and trans is linear once \(\Omega\) is fixed.
   - Neither the orientation layer nor the factor layer can be fixed first in a uniform way (row "fixed random Euler orientation").
   - The parity conditions (J3′, and the cycle-label conditions of J2) must be met by a choice the proof has not identified. The two natural candidates are:
     - local complementation at non-apex vertices, which changes \(W\) while keeping the cherry transitions;
     - non-circuit transition systems.
3. **Induction is blocked.**
   - Splitting off a non-apex vertex needs the two new edges to get different colours. This is not always attainable (row "pair flexibility").
   - It also needs the split to preserve (K1). The partner of the apex-side edge must be a non-target, and one may not exist.
4. **Counterexample search found nothing** in the targeted failure modes:
   - 2- and 4-edge-cut gadgets;
   - mutual edges together with D2 apexes;
   - dense maximal systems.

   The bridge/cap mechanism of 04i cannot operate inside the class. Its forcing step used a fibre with four apexes (04i, step 4).

**What a proof needs.** One promising formulation is a lemma saying that, for some admissible Euler circuit \(W\), the J3′ obstruction for \(P\) can be removed by D-options at single apexes whose cherry passes have equal colour. Data: 1 or 2 such apexes always sufficed (row `oneD.py`). Another is a 2-SAT argument for Lemma J1(ii) that uses the distinct heads of K-arcs (K1). In both cases (K1) must enter at the parity step. The minimal infeasible cores of §1.1 show that this is exactly where shared targets fail.

## 5. Secondary lead (weak (P5)): not started

Weak (P5) (04i (b)) would require extending the Theorem C windows to (P5)-violations at bridge-end apexes. That is a new computer-assisted window campaign. It was not attempted this session.

## 6. Bounded literature check (2026-11-26)

The arXiv API was queried with these searches:

- `all:"path decompositions" AND all:regular AND all:matching` (50 results);
- `all:"decomposition" AND all:"5-regular" AND all:paths`;
- `all:"path decomposition" AND all:"regular graphs"`, newest first (60 results).

Two searches over `abs:` fields with spaced phrases returned 0 results because of the query syntax.

Relevant hits were the following:

- arXiv:2012.05145 (Botler–Hoffmann; cycle powers and Cayley spanning subgraphs; already cited in the main note);
- arXiv:1510.02526 (Botler–Jiménez; even degree);
- arXiv:2406.02514 (approximate decompositions).

None states a result on matching edges in at most one triangle, or on (P5)-type conditions. The comparison with FGK 2010 Theorems 6–7, BMW 2015 and CFHZ 2024 is in [04d](04d-regular-path-matching-relative-theorem.md) and [04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md). If proved, the class corollary would contain B′ and hence everything B′ contains: FGK's \(C_4\)-free degree-five theorem (two triangles on a common edge span a 4-cycle, so \(C_4\)-free graphs are diamond-free), BMW (no triangles) and CFHZ 2024. Its relation to Theorem A of 04d (no triangle–square conflict) was not analysed. No novelty is claimed, since nothing is proved.

## 7. Files and commands

Run from `research/2026-11-25-target-shortlist/04-handoff/p6_scratch/` with `python -B`:

- `python -B exhaust.py 5,6,7,8,9 nonadj` (about 50 s) and `python -B exhaust.py 10 nonadj` (about 9 min): exhaustive abstract check; `python -B exhaust.py 5,6,7,8 any` (about 30 s).
- `python -B interlace_check.py 1 40`: Lemma J3 check, `tested 4800 mismatches 0`.
- `python -B core12.py ../p5_scratch/c12.log`: cores of the at-most-two counterexamples (`core12.py` imports `core.py` from `p5_scratch` by absolute path).
- `python -B stratabs.py 1 1500 ABC,ABD,BCD,ACD`, `python -B exp2.py 2 150 full,cross,trans`, `python -B oneD.py 1 400`, `python -B gadget.py 1 300 9`, `python -B gadget4.py 1 200 9 g4a.pkl && python -B pairs4.py g4a.pkl`, `python -B flex.py 1 40`.
