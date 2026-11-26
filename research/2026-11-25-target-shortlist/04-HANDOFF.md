# Regular path decomposition handoff

**Conjecture 1 remains open.** Favaron, Genest and Kouider ask whether every finite simple odd \(d\)-regular graph with a perfect matching admits an edge partition into simple paths of exactly \(d\) edges. Here \(d\) counts edges, and the perfect matching need not be the middle-edge set. The unrestricted degree-five case remains open in the sources checked. The exact adjacent Problems 3, 5 and 6 have the constructions below. [Original paper, Section 6](https://doi.org/10.1002/jgt.20413) · [Full text](https://www.academia.edu/25437460/Regular_path_decompositions_of_odd_regular_graphs)

## Session 6 (2026-11-26): one-triangle class: still open; reformulations proved, exhaustive small-order evidence

Details are in [04j](04j-regular-path-one-triangle-class.md). **No new theorem. Conjecture J is neither proved nor refuted.**

- **Exact target (Conjecture J).** If every \(M\)-edge lies in at most one triangle, then some \(r,s\) satisfy (P1)–(P3) and (P5).
  - Theorem C consumes exactly this, with no bridge, cap or connectivity hypothesis.
  - The hypothesis is equivalent to (K1): every vertex is a target of at most one cherry.
  - The class strictly contains B′; it adds \(M\)-side diamonds and mutual cherry edges.
- **At-most-two counterexamples** (`p5_scratch/c12.log`, 5 instances). Every minimal unsatisfiable core contains a fibre with two apexes, which (K1) forbids. This explains the class but does not prove it, since the cores are global.
- **Proved:**
  - J1 (2-factor form): (P5) ⇔ no cherry lies in \(F_R\); (P3) ⇔ no cherry is both-in.
  - J2: the strategy *cross* is a \(\mathbb Z_2\) system once the 2-factorization is fixed; *trans* is a \(\mathbb Z_2\) system once \(\Omega\) is fixed.
  - J3: for an Euler circuit \(W\), a turn vector \(t\) gives a valid colouring ⇔ \((A_I+\mathrm{Id})t=\mathbf 1\). This was checked on 4,800 colourings with 0 mismatches.
  - J3′: the exact parity obstruction to prescribing the turns at the apexes.
- **Evidence.** The abstract version replaces \((G,M)\) by any 4-regular \(H\) with a (K1) cherry system.
  - Exhaustive at orders 5–10 over all maximal systems: all 216,412 feasible.
  - Planted real instances, \(n\le24\): 984/984 feasible.
  - Strategy *cross* (every cherry one-in one-out): 1,499/1,499; *trans*: 2 failures.
  - Fixed orientations fail about 30% of the time, so the orientation must be chosen.
  - Gadgets on 2- and 4-edge cuts: no incompatible interfaces.
- **Why the proof stopped.**
  - All uniform strategies fail.
  - Each linear layer depends on the other.
  - Naive vertex-splitting induction fails: 2 of 6,378 edge pairs are forced to have equal colours, and splitting may violate (K1).
- **Literature.** A bounded arXiv API check found no result on this class (04j §6).
- **Next steps.**
  1. Try to prove "J3′ obstruction removable by ≤2 equal-colour D-apexes for a suitable admissible \(W\)". In the data, 1 apex sufficed in 105 of 111 transcross failures and 2 in the rest. Use local complementation at non-apex vertices.
  2. Or find a 2-SAT proof of J1(ii) that uses (K1) at the parity step.
  3. Weak (P5), the bridge-end windows of 04i (b), was not started.

Restart (from `04-handoff/p6_scratch/`, `python -B`):

```powershell
python -B exhaust.py 5,6,7,8,9 nonadj      # ~50 s, all feasible
python -B exhaust.py 10 nonadj             # ~9 min: 10 {True: 189673, 'graphs': 60}
python -B interlace_check.py 1 40          # tested 4800 mismatches 0
python -B stratabs.py 1 1500 ABC,ABD,BCD,ACD
python -B oneD.py 1 400
```

## Session 5 (2026-11-26): review fixes applied; P5* refuted; (P5) reformulations

- **Reviews.** Theorem B′ and Theorem C were independently reviewed: accept with fixes ([04-REVIEW-theorem-Bprime.md](04-REVIEW-theorem-Bprime.md), [04-REVIEW-theorem-C.md](04-REVIEW-theorem-C.md)). All fixes are applied in 04g §2–3 (changelog at the end of 04g). Lemma C8 now has a proof. The Lemma 4 run under (P5) is now part of [check_regular_path_p5sweep.py](check_regular_path_p5sweep.py). Reruns: p5sweep 0 failures, mdiamond 0 failures, referee's Theorem C checker `--quick` passed. Theorem C is a *conditional reduction* (needs P5\*); B′ belongs inside the Theorem B entry.
- **P5\* is FALSE** ([04i](04i-regular-path-p5star-counterexample.md)), and P5\*\* with it. The counterexample is a 9-vertex block \(B\) whose three degree-4 vertices are joined by bridges to 7-vertex caps, 30 vertices in all. Every perfect matching contains the bridges, so it meets \(B\) in one of two matchings, and both make (P5) impossible on \(B\).
  - The hand proof is in 04i.
  - [check_regular_path_p5star_counterexample.py](check_regular_path_p5star_counterexample.py) (4 s) brute-forces all 2,000 matchings and all 142 Euler orientations from the definitions. A control without (P5) finds 208 solutions.
  - \(G\) decomposes into 15 five-edge paths, so it is **not** an FGK counterexample. The coordinator checked this independently.
  - The route "Theorem C + P5\* ⇒ degree five" is dead as stated. Theorem C stays a correct conditional theorem.
- **Rescue evidence** (04i; searches over blocks attached by bridges or cuts):
  - (a) Bridgeless P5\*: no bridgeless counterexample was found. No 2-attachment block of order ≤10 qualifies, and no forced 3-cut block was found at small orders.
  - (b) Weak (P5), which ignores cherries at bridge-end apexes: no counterexample block exists among all blocks up to (10,4) attachments. In 04i's example, dropping one bridge-end apex already restores feasibility.
  - Any switching proof must use alternating cycles of unbounded length: there is an \(n=14\) infeasible \(M\) whose shortest improving cycle has length 10.
- **Reformulations** ([04h](04h-regular-path-p5-reformulations.md)). (P3)+(P5) ⟺ "at each cherry, if one edge is R-in the other is S-out". In the Ω-form, D2 apexes need only an orientation condition, and singly paired apexes need "not (r(x)∈Y and t(x)∉Y)". In the trail form, cross cherries give unit demands. Evidence: every \(M\)-edge in ≤1 triangle ⇒ (P5) held in all 13,382 tests (unproved).
- **Next steps:**
  1. Decide between (a), proving P5\* for bridgeless graphs plus a separate reduction for bridge caps, and (b), extending Theorem C's windows to (P5)-violations at bridge-end apexes and then proving "weak P5\*".
  2. Test weak P5\* on larger blocks, including 2-edge-cut gadgets.
  3. The ≤1-triangle class theorem remains a provable-looking side target.

## Session 4 (2026-11-25): (P5) negative result, Theorem B′, Theorem C program

Details in [04g](04g-regular-path-p5-and-m-diamond.md). Conjecture 1 remains open in degree five.

- **(P5) cannot always be imposed for a given \(M\).** An 8-vertex \((G,M)\) has no \((r,s)\) with (P1)–(P3)+(P5); an independent brute force over all 94 Euler orientations confirms it. Infeasibility is common on dense small graphs (192/932 at \(n=8\)) and occurs even with at most one M-pair per apex.
- **Conjecture P5\*** (some \(M\) admits (P5)): true for every graph of orders 8 and 10 (exhaustive); every matching minimising the number of M-pair incidences was feasible in all tests.
- **Theorem B′ (candidate):** no diamond contains an \(M\)-edge ⇒ decomposition. Proof = 04e with diamond appeals replaced by M-diamond appeals (table in 04g §2); [check_regular_path_mdiamond.py](check_regular_path_mdiamond.py) re-ran Lemma 4, Lemma 4′ and W1–W8 with 0 failures. Depends on 04e (under review).
- **Theorem C (candidate, unreviewed):** (P1)–(P3)+(P5) ⇒ decomposition. (P5) ⇒ first sweep leaves only X2 (Lemma 4 re-run under (P5)). X2 second sweep: D-rule (α), D-pendant (β), absorption / Γ_D / rule F (γ); D-chains by alternation on paths and a new D-rotation on cycles; X2 sources never have type-2 links (Lemma C2). All windows in [check_regular_path_p5sweep.py](check_regular_path_p5sweep.py) pass (0 failures, ~2 min). [check_regular_path_p5_endtoend.py](check_regular_path_p5_endtoend.py): 400/400 annealed generic instances (121 D-cycles, 100 Γ_D, 17 F) and 539 graph instances verified.
- **What remains for the full degree-five case: Conjecture P5\*** (some perfect matching admits (P5)). Theorem C + P5\* ⇒ Conjecture 1 for \(d=5\). P5\* is open; see 04g §4. Sharper form P5\*\*: every triangle-minimal matching admits (P5). There are no counterexamples in 63 exhaustive graphs plus 1,167 sampled instances, including 355 dense ones.
- **Next steps (session 4 → 5):** (1) independent review of Theorem B′ (04g §2) and Theorem C (04g §3), especially Lemma C8 completeness and the endpoint-uniqueness fact in the D-rotation; (2) attack P5\*\* via matching switches, starting from the 8-vertex fixed-M obstruction in 04g §1, to see which matchings fail and why; (3) add odd type-2 cycle rotations to the end-to-end checker and anneal for odd type-2 cycles.

## Session 3 (2026-11-25): diamond-free degree five, candidate theorem

**[04e](04e-regular-path-diamond-free.md) Theorem B: every diamond-free 5-regular graph with a perfect matching decomposes into five-edge paths.** The proof is computer-assisted and **has not been reviewed**. It strictly contains Chu–Fan–Hong–Zhou 2024, and also the FGK \(C_4\)-free and BMW triangle-free degree-five theorems. Conjecture 1 remains open for graphs that contain diamonds.

- **Method.** Proposition B of 04d leaves only G-configurations. A second sweep repairs them, after a case split on the trail \(W_0\) in which \(f\) is a red head:
  - α: the **G-rule**;
  - β: a **G-pendant**;
  - γ: **absorption** of \(W_0\), or the **Γ/Γ′ rule** when \(W_0\)'s trade is type-2 or creates a G-configuration.

  The "Gtarget" dependencies form a functional graph, resolved by alternation. An odd cycle uses Γ/Γ′ at a valid node, or a **rotation** when every node fails.
- **Verification.**
  - [check_regular_path_gsweep.py](check_regular_path_gsweep.py) runs all windows W1–W8 in 14 min with 0 failures, plus Lemma 4′ with G-pendants. It is built on the exhaustive label engine [check_regular_path_label_engine.py](check_regular_path_label_engine.py), which enumerates every identification compatible with (P1)–(P3), injectivity, disjoint edge classes and diamond-freeness of the known edges.
  - W7 (Γ at a Gtarget node) was re-run with the tightened criterion, allowing failure only under (F1) \(s(q)=c\) with pendant \(
e h\). It gave 0 failures, as logged in 04e.
e h\).
  - End-to-end: [check_regular_path_diamond_free.py](check_regular_path_diamond_free.py) produced 3,200 verified decompositions of random diamond-free graphs (orders 12–60). These included 6 Gtarget cancellations and 25 γ-configurations. A further 2,400 verified decompositions came from seed 7. The generic planted \((M,r,s)\) run gave 193 verified decompositions, with 28 γ-configurations, 8 type-2 Γ uses and 8 Gtarget absorptions. No odd Gtarget cycle was observed. These runs are evidence only.
- **Open points for review.**
  - The completeness of the case catalogue (04e §4), which is the highest-risk point.
  - The justification of each engine fact.
  - The rotation case, which has no observed real instance.
- **Review of Theorem A.** [04-REVIEW-theorem-A.md](04-REVIEW-theorem-A.md) gave ACCEPT WITH FIXES. Fixes m1–m8 are applied to 04d.
- **FGK comparison.** The coordinator read the FGK full text ([04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md)). Theorem A is not in FGK, and the two results are incomparable.
  - Our "bad pair" was renamed *triangle–square conflict* in 04d and in the pipeline checker.
  - FGK Theorems 6–7 are cited in 04d, with the comparison.
  - Lemma 1 is credited to FGK's construction.
  - Corollary 1 is restated.
- **The P5 reduction, a side result.** Proposition B and Lemma 3 use only (P1)–(P3). If \(r,s\) also satisfy (P5), \(m(r^{-1}(c))
e r(c)\), no G-configuration exists.
  - Exact backtracking found (P5) feasible on 102 diamond-free graphs with \(n\le60\).
  - It is unproved, and a fixed-orientation 2-SAT fails for large \(n\).
  - (P5) would also remove the Lemma 3 cases \(A=r(b)=d\) and \(r(e)=c\) in general graphs.
- **General case: exploration only.**
  - On 300 random general graphs (with diamonds), greedy 2- and 3-piece local re-decomposition after the first sweep always succeeded.
  - The remaining shapes are mainly sources with \(s(c)=e\), which needs a diamond with chord \(ce\). The others are changed-pendant lollipops \(A=d\), recipients \(r(e)=c\), double G-configurations and odd-cycle chords.
  - Without diamond-freeness, the G-rule windows fail only through \(s(f)=h\).
  - A "lollipop rule" for \((x,y,z,x,w,v)\) exchanges \(xz\) for \(\{z,s(z)\}\) from the trail where \(z\) is a red head. It covers \(s(c)=e\) and \(r(e)=c\). The case \(A=d\) needs another partner.

## New partial theorem (session 2, 2026-11-25)

[04d](04d-regular-path-matching-relative-theorem.md) proves **Theorem A**: if a 5-regular graph has a perfect matching \(M\) with no *bad pair*, then it decomposes into five-edge paths. A bad pair is an \(M\)-triangle and an \(M\)-square that share an edge. Here an \(M\)-triangle is a triangle through an edge of \(M\), and an \(M\)-square is a 4-cycle with exactly one edge of \(M\).

- **What it generalizes.** It contains the FGK \(C_4\)-free theorem, the Botler–Mota–Wakabayashi triangle-free theorem and the Chu–Fan–Hong–Zhou 2024 theorem. It also covers every graph with a perfect matching none of whose edges lies in a triangle.
- **How it is proved.** The proof assembles the earlier construction and sweep and re-proves every collision claim (Lemma 3). The only computer-assisted step is the odd-cycle triple lemma (Lemma 4), restricted to this hypothesis.
- **The earlier rotation gap is closed.** The odd-cycle rotation needed \(A_i\ne b_{i-2}\), and this is now proved by (o4).
- **Diamond-free case.** Proposition B reduces it to one configuration, called the G-configuration. It is a type-0 target \((b,c,f,b,h,Y)\) with \(fb\in M\), \(r(f)=c\) and \(r(c)=b\).
- **The G-rule.** One subcase of a rule for the G-configuration is proved. The rule exchanges \(fb\) for \(f\,s(f)\) with the piece holding \(f\) as a red head. It fixed every G-configuration in all 187 diamond-free random graphs tried, which is evidence, not proof.
- **Checker.** The new [pipeline checker](check_regular_path_sweep_pipeline.py) reimplements the construction and sweep and runs the exact lemma. It took about 45 s; add `--diamond-free 40` for the diamond-free run.
- **Not yet done.** Theorem A is unreviewed by an independent reader, and the FGK full text was not readable (403), so its novelty is not yet confirmed.

## Separate completed results

| Question | Result | Proof and checks |
|---|---|---|
| Problem 3 asks for a simple odd \(d\)-regular graph with a \(d\)-edge path decomposition and no perfect matching for every odd \(d\ge7\). | Such a graph exists for each odd \(d\ge5\). | [Proof](04c-regular-path-problems-3-and-6.md). Exchange an interior occurrence of one vertex with a distant root occurrence in an explicit balanced decomposition of a cycle power. Attach a smallest odd bridge cap at each root occurrence. One vertex has two bridges and cannot be matched. Independent JS verified distinct paths, exact edges, degrees and forced bridge cuts at \(d=5,7,9,11,13,15,17\). |
| Problem 5 asks whether every simple 2-edge-connected odd \(d\)-regular graph with a perfect matching admits a \(d\)-edge path decomposition whose middle edges form some perfect matching. | The answer is negative for each odd \(d\ge5\). | [Proof](04b-regular-path-center-counterexample.md) and [verifier](check_regular_path_center_counterexample.py). A substituted even cap forces both connectors into every matching. Those forced connectors reproduce the clique-cut obstruction in the original Figure 3 for every matching. Independent constructions checked parity, cuts, connectivity and matchings at \(d=5,7,9,11\). The degree-five graph has 288 vertices and 720 edges. Its explicit 144 simple paths prove that this graph satisfies Conjecture 1. |
| Problem 6 asks if the converse in Theorem 2 holds above degree five. | For each odd \(d\ge7\), a simple path decomposition can have a perfect middle matching and fail to be rainbow-making. | [Proof](04c-regular-path-problems-3-and-6.md). Four explicit Hamilton paths of \(K_8\) have perfect middle matching and a type-1 vertex of degree three. Equal-label factors between cyclic copies extend both ends to arbitrary odd degree without changing middle or type-1 edges. Independent JS checked the graph and exact edge partition for \(d=7,9,11,13,15,17\). |

Targeted literature, local branch, remote tracker and formal library searches are described in [the main note](04-regular-path-decomposition.md). Priority for the separate results remains provisional. The definitive sources checked include the [2024 triangle/square overlap theorem](https://www.sciengine.com/cfs/files/pdfs/view/1674-7216/9A038B7537554B7284033EDD2D967FFB.pdf) and [the 2025 approximate theorem](https://doi.org/10.1112/jlms.70269). No remote branch, index, issue or PR was changed for this thread.

## Main conjecture reductions and receipts

- The [main note](04-regular-path-decomposition.md) proves that a matching-relative Euler orientation and two spanning factors always give a degree-five partition into simple paths and square-plus-pendant trails. It gives a simultaneous repair criterion involving only matched triangles and squares, with a 408-vertex example that falls outside the cited sufficient hypotheses. It also treats uniform dependency cycles and specifies which mixed repairs were sampled.
- The opposite reduction starts from that same canonical partition. Simultaneous exchanges along type-2 dependency chains and even cycles remove the pure square trails. An exact triple check handles the odd cycles with their incoming pendant changes. The resulting partition has only simple paths and open trails whose repetitions are between an endpoint and a vertex three edges away. It can contain a triangle with a two-edge tail or a diamond. The [repair checker](check_regular_path_repair_obstruction.py) passed all 344 closed and 945 open triple cases with that exact predicate, and verifies the covering edges and blue terminal arc directions. Eliminating the remaining triangles is open.
- The same checker passed 52 closed pure-cycle triple cases and 169 of 173 open cases for the stronger requirement of simple paths, with four exceptions addressed by the stated uniform cycle rotations. It builds a canonical matched 1,880-vertex graph and proves one specified defect has minimum repair size exactly four. There are five adjacent two-piece unions and 45 connected three-piece unions, none coverable by simple five-edge paths. It also verifies the earlier arbitrary-partition obstruction on 7,232 vertices. These examples concern a specified defect and do not exclude choosing a different defect or applying a global switch.
- The [regular-graph checker](check_regular_path_decomposition.py) completed all 1, 3 and 60 isomorphism classes of 5-regular graphs at orders 6, 8 and 10. It checked 52 and 51 labelled samples at orders 12 and 14. It verifies simplicity and exact coverage separately after finding a partition. No complete order-12 census is claimed.
- Cut arithmetic makes every actual bridge the middle edge of its path. Two-edge cuts separate even-order sides, each connector lies on a different path, and the two inside arm lengths sum to \(d-1\). At fixed odd degree, any minimum counterexample has only bridges with one smallest \((d+2)\)-vertex side. Attaching smallest bridge caps to every vertex of a \(2k\)-regular graph makes the resulting case equivalent to Kouider–Lonc's balanced decomposition into \(k\)-edge paths. The core arms in the two directions are rooted once and end once at each vertex. [Kouider–Lonc formulation](https://doi.org/10.1016/j.disc.2017.04.024)
- A cap with a perfect matching and one forbidden ordered noncentral pair \((i,d-1-i)\), \(i\ne(d-1)/2\), would refute the conjecture. Joining it with a reversed copy in series forbids both orders. Use \((d-1)/2\) copies of that composite at one hub, attach a true bridge cap, and count oriented arm appearances to force one pair of each noncentral level. An even cap with a matching only after deleting its distinct ports and without its balanced central pair would also refute the conjecture on attaching true bridge caps to both ports. Neither candidate cap has been found.
- The degree-five cap kernel must include joint outer/bridge arms. In the original 11-vertex Figure 4 half-core with one spoke removed, a purported missing \((3,1)\) comes back via an outer port and a true bridge in the same piece. Independent corrected checks find all four noncentral pairs. A cap missing only the central pair can have an internal matching, as shown by the explicit shared-root construction in the main note. Its example realizes all noncentral pairs and does not refute the conjecture.
- Completed positive cap searches include all eligible one-port degree-five shores through order 11, 1,802 eligible distinct-port shores of orders 6, 8 and 10, and 181 shared-port shores of orders 8 and 10. The tested noncentral pairs also succeeded at more than 6,000 adjacent port placements in quartic cores of orders 5–12 with true bridges at all other vertices, at 112 Figure 4 half-core bridge-terminal closures, and in the 3,000 eligible plain order-11 three-port compositions and tested decorated batches up to order 12. These searches use marked cut incidence columns and allow compound bridge pieces. The degree-seven search produced positive small cases including \(K_7\) and \(K_8\) minus a matching as sextic cores. Larger solver time limits were inconclusive. This supplemental search was stopped during order 10 after preserving its source.

## Fixed-factor approaches that fail

Changing only the arm assignments of the post-sweep positions is insufficient. At former middle vertices with zero middle incidences there are two pairings of incoming position-1 arcs with outgoing outer edges. At promoted vertices with two middle incidences there are two pairings with outgoing position-1 arcs. A Boolean search exhausts these choices for a given sweep. It fails on an 8-vertex example even with all its permitted sweep choices. Use canonical successor maps \(r=(1,5,0,4,6,2,7,3)\), \(s=(7,3,1,2,5,6,0,4)\), and matching map \(m=(5,7,4,6,2,0,3,1)\) with vertices indexed from zero. The sweep yields the four sequences \((3,1,0,5,2,0)\), \((6,5,1,7,3,4)\), \((7,0,6,4,2,1)\), and \((5,4,7,6,3,2)\). Relaxing the fixed positions gives many ordinary path decompositions of this same host.

Even if middle and outer edges and orientations can all change, holding the undirected position-1 2-factor can fail. A 5-edge path uses a position-1 edge as its second and fourth edges, counting distance one from the middle. The following proof supplies a matched 48-vertex graph and a disjoint prescribed 2-factor \(R\) for which no decomposition uses \(R\) as this type.

**First cap.** On labels \(0,\ldots,5\) take two nonred triangles \(012\) and \(345\) and the red cycle \(0,4,2,3,1,5,0\). Attach one smallest seven-vertex cap by a bridge at each of \(2,3,4,5\), and reserve the two exterior ports at \(0,1\). Match \(0\) with \(1\) and use the four bridges and the port-deleted matchings of their caps. The red cycle stays entirely inside the core and crosses between \(A=\{0,1,2\}\) and \(B=\{3,4,5\}\) at every step. An outer connector pair of lengths \((0,4)\) or \((4,0)\) is impossible with these fixed red edges. The zero arm gives a core terminal in \(A\). If the length-four arm stays in the core, each of the three bridge arms rooted in \(B\) must remain in the core and use one red edge then one nonred edge. They give three further terminal occurrences in \(A\), exceeding its three vertices. If the long arm instead uses a bridge, it uses exactly one native red edge into \(B\), that bridge, and the attached cap's two-edge arm. Two other bridges at \(B\) still give core terminals in \(A\). This saturates the three terminals in \(A\). The remaining ordinary five-edge path in the core must have both endpoints in \(B\). Its pattern nonred, red, nonred, red, nonred would require four distinct vertices of \(B\), which is impossible. The two types exhaust the possible long arm because actual bridges are centred.

**Completion.** Join both first-cap ports to a hub, attach a true bridge cap at the hub, and join the hub to both deficient vertices \(a,b\) of an independent \(K_6-ab\). Prescribe red on the two connectors to this second cap and its Hamilton path \((a,2,3,4,5,b)\). Use matching pairs \(a3,b4,25\) in it. In every seven-vertex bridge cap use cyclic distance one as its red factor. This specifies the full factor disjoint from the exhibited matching. The two cut pairs at the hub fill one level each, so the first cap must supply its forbidden noncentral outer-level pair. The graph is simple and 5-regular, with 120 edges.

**Unrestricted witness.** In the first cap assign the zero arm to \(0\), use the length-four arm from \(1\) through \(5\) and its bridge, use core arms \((4,0,5),(2,4,3),(3,1,2)\) at the other actual bridges, and use the internal path \((1,0,2,3,5,4)\). In the second cap label \(a=0,b=1\), take arms \((0,2),(1,3,4,5)\) and internal paths \((0,3,2,5,1,4),(1,2,4,0,5,3)\). Join the one-edge second-cap arm to the hub bridge arm, the three-edge second-cap arm to the first-cap zero arm, and the four-edge first-cap arm to the hub as its terminal. Use the alternating-step paths of the smallest seven-vertex bridge cap for all its internal decompositions. An independent JS check compared all 24 simple paths against the 120 expected edges and verified the specified red factor and 24-edge matching. Thus this is a fixed-factor obstruction, not a main counterexample.

## Restart

Run these commands from the worktree root.

```powershell
Set-Location research/2026-11-25-target-shortlist
python check_regular_path_decomposition.py
python check_regular_path_repair_obstruction.py
python check_regular_path_center_counterexample.py --degrees 5 7 9 11
python 04-handoff/verify_fixed_factor_examples.py
```

Representative commands for the preserved exploratory kernels are below. The degree-seven script requires NumPy and SciPy. Its time limits are not negative certificates. The other exploratory scripts report sample bounds, and several have longer default searches.

```powershell
Set-Location 04-handoff
python fgk_cut_scratch.py --ports 2 --orders 6 8 10 --cut
python fgk_cut_scratch.py --ports 3 --orders 7 9 11 --samples 3000 --composed-arm
python fgk_bridge_closure_caps_scratch.py --copies 1
python fgk_quartic_caps_scratch.py --orders 5 6 7 8 9 10 11 12 --maximum 3000
python fgk_weighted_core_scratch.py --caps --ordered --orders 8 10 12 --samples 1000
python fgk_forced_cap_search_scratch.py --hubs 4 --cases 100 --all-lengths --macro
python fgk_mixed_cycles_scratch.py --lengths 3 4 5 6 7 8 9 --attempts 100
python fgk_degree7_cap_scratch.py 10 7 8 9 10
```

**Next steps, in order (updated, session 3).**

1. **Done:** the 04d review was accepted with fixes, and the FGK full-text comparison was made, showing Theorem A is new.
2. **Done, under review:** the diamond-free case, Theorem B in 04e. An independent referee is auditing it; the output will be 04-REVIEW-theorem-B.md. Make only small, logged fixes to 04e during the review.
3. **General case.** [04f](04f-regular-path-general-degree-five-plan.md) lists the exceptions X1–X6 that appear with diamonds. In exploration, local repair solved 400/400 graphs. It also gives the first D-rule window for X2 (a source with \(s(c)=e\)). Continue as follows:
   - choose partner rules for X1–X5;
   - run the windows with `diamond_free=False`;
   - redo Lemma 4 for general local structure;
   - extend the end-to-end checker.
4. **Alternative route.** Prove (P5) can always be imposed. It is open even in the diamond-free case, and it would remove X1, X3, X4 and X5.

```powershell
python check_regular_path_sweep_pipeline.py --diamond-free 40
python check_regular_path_gsweep.py                       # 04e windows W1-W8 + Lemma 4', about 14 min
python check_regular_path_diamond_free.py --generic 300   # 04e end-to-end evidence
```

Earlier guidance follows. The most direct open proof direction is a global repair of the triangular trails after the square-to-triangle sweep, allowing the position-1 factor to change. The fixed-factor obstruction rules out treating that factor as part of the invariant. For a disproof, the strongest small target remains a matched cap lacking one ordered noncentral pair. A search based on the fixed-red obstruction should allow all red factors, actual bridge compounds and three/four-port transits when their edge counts permit them. No candidate against Conjecture 1 is pending verification.
