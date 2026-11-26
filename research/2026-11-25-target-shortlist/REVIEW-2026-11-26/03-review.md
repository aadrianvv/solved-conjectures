# Referee report: thread 03, Caro–Petruševski–Škrekovski Conjecture 6.4 at Δ = 4

Reviewer: independent referee agent, 2026-11-26. Scope: `03-HANDOFF.md`, `03-conflict-free-colouring.md`, `03-ISSUE-DRAFT.md`, `check_03_*.js`, `03-handoff/` (in particular `pcf-tw3-language.js` and `pcf-census-rs`). Nothing in the research files was edited. Scratch scripts and logs are in `REVIEW-2026-11-26/03-scratch/`.

Target: every graph of maximum degree at most four has a proper conflict-free (PCF) colouring with five colours (the Δ = 4 case of CPS Conjecture 6.4, Discrete Math. 346 (2023) 113221, arXiv:2203.01088). It remains open. Nothing below resolves it.

## Verdicts

| Claim | Verdict |
| --- | --- |
| (a) Δ ≤ 4 and treewidth ≤ 3 ⇒ PCF 5-colourable (computer-assisted) | **Correct with fixable gaps.** The argument and checker are sound as far as I can audit them. The claim that it was checked by "two implementations" is overstated. The pathwidth ≤ 3 statement is a corollary and adds nothing. |
| (b) No counterexample on at most 14 vertices | **Correct, with a fixable gap in the trust base.** The reductions and generator are sound. Orders 13 (three strata) and 14 rest on one run of a line-by-line port, with no second implementation. |
| (c) Minimum-counterexample reductions | **Correct.** I checked each written proof. The three-edge-cut lemma depends on a finite palette checker, which I reran. One stale proposition needs fixing. |

## (a) Treewidth at most three

### The argument

1. Take a minimum-order counterexample G within the class {Δ ≤ 4, tw ≤ 3}. Every auxiliary graph used by the reductions is a minor of G with fewer vertices and maximum degree at most four, so it stays in the class. I checked each one. Leaf deletion and the induced pieces are subgraphs. Degree-2 suppression contracts an edge. The K4 case uses H+xy, which is a contraction along x–s_x–s_y–y. In the matching three-edge cut, the added terminal edge comes from a path through the other side, which is connected because G is 2-edge-connected. The star-plus-edge hub contracts the opposite side. In the 1,3 and 2,2 two-vertex cuts, xy is added along a path through the other component. The degree-three reduction contracts va and is only needed for (b). Hence G is connected, K4-free, 3-connected, has degrees in {3,4}, and every edge cut with at least two vertices on each side has size at least 4. The fact that Δ ≤ 3 graphs are PCF 5-colourable (CPS / Liu–Yu) is the only external input.
2. With n ≥ 4, G is a spanning subgraph of a 3-tree. Root the 3-tree at its initial triangle. Each later vertex p (the pivot) is added onto a triangle T and creates the bag T∪{p} and three facets. Each non-root triangle is created by a unique bag, so the pieces below T are well defined, and different pieces below T have no edges between them. Every K4 of a 3-tree is a bag, so K4-freeness is exactly the mask < 63 condition. All three facts hold.
3. The pruning conditions are necessary for a minimum counterexample. Every boundary vertex has an interior neighbour: by 3-connectivity when the exterior is nonempty, and by minimum degree at the root. An interior of two or more vertices has at least 4 crossing edges. A boundary vertex with a nonempty exterior has used degree at most 3. A pivot has degree at least 3. This also holds for partial unions of the pieces under one triangle. In the code, single versus multiple interior is recovered correctly from the shape: a single pivot gives exactly 3 crossing edges, otherwise there are at least 4.
4. Transitions (`check_03_treewidth_three.js`). Signatures record each boundary row's colour and neighbour-colour counts up to palette permutation. The canonical form (`encode`) is a true canonical form: tied free colours have identical count vectors. `merge` enumerates every palette permutation consistent with the boundary colours. Shared boundary edges are subtracted once (`interiorCounts` together with the `countedDegrees` subtraction). A degree-4 row is checked for a singleton when it reaches degree 4 and is then zeroed. An attached row can never be zeroed, because attached boundary states with degree 4 are never saved. A pivot is checked at projection, when all its neighbours are present (bags containing p form the subtree below p's bag). The root's boundary vertices are checked by the terminal test, which runs before any domination pruning.
5. Domination. Bag states are pruned when their signature set is a subset of another with the same key (mask, degrees, lastFacet). Boundary states are pruned by inclusion of accepted exterior patterns (equality type plus exterior multisets of size between max(0,3−d) and 4−d, avoiding the vertex colour). The pattern set is a superset of the realisable ones, so inclusion is a sound "at least as restrictive" test. Every search state is the exact state of a concrete piece graph. Substituting that piece preserves boundary degrees, mask and size class, so every later pruning test and terminal test behaves as before. The substitution argument therefore goes through.
6. Ordered boundaries. A child's boundary order is forced by the parent facet (`facets[i]`). All 63 masks of every bag are enumerated, so the child's own bag can be labelled in that order, and induction over the parse needs no S3 symmetry of the closure. This is correct, but the note never says it.

### Reruns (2026-11-26, Node v24.22.1 via the VS Code runtime)

- `check_03_treewidth_three.js` gave `{"states":1540,"representatives":1539,"boundaryStates":78,"bagStates":1469,"facetJoins":10669,"boundaryJoins":215,"projections":9442,"terminalTests":4129}` in 1 min 42 s. This matches the handoff.
- `03-handoff/pcf-tw3-language.js` gave processed 1540, live 1539, j4 10669, j3 215, term 4129, projs 9442, `complete:true`. This matches.
- `check_03_pathwidth_three.js` gave 5,145 states, 17,812 transitions and 2,392 terminal states, largest set 793. This matches.
- **Non-vacuity test (mine).** I made a copy of the treewidth checker with a 4-colour palette (`03-scratch/tw3_mutant_4colours.js`, three-line diff). It fails with `AssertionError: bag without a partial colouring`. The closure does detect failures. It is not vacuously green.
- **Sampling corroboration (mine, not a proof).** 3,000 random maximal subquartic subgraphs of random 3-trees on 8 to 40 vertices were all PCF 5-coloured by an independent solver with an independent verifier (`03-scratch/random_tw3.js`).

### Gaps to fix before publication

- **Independence is overstated.** `pcf-tw3-language.js` is not an independent implementation. It is the terse precursor of the same algorithm, with the same state model, key, domination rule, facet order and processing loop. Agreement of the counts checks transcription only, not the design. Write "one algorithm, two transcriptions", or supply a genuinely different check, such as a nice-tree-decomposition DP without 3-tree completion or a Lean development.
- **The written proof leaves steps implicit.** Add the orientation and induction remark from item 6. State explicitly that each state is realised by a concrete piece, that the substituted graph keeps maximum degree ≤ 4, and that every parse step passes the same local tests. Also state that the Δ ≤ 3 input is used only as "Δ ≤ 3 ⇒ PCF 5-colourable".
- **Pathwidth.** pw ≤ 3 implies tw ≤ 3. Drop the pathwidth result as a separate claim, or keep it only as an independent sanity check of the subclass, which uses different code.
- **Scope wording.** Write "maximum degree at most four", not "subquartic". The theorem includes disconnected graphs and isolated vertices, which is fine because a disjoint union of PCF colourings is a PCF colouring.

## (b) The order bound

- **What was enumerated.** The program enumerates a labelled cover of connected K4-free graphs with all degrees in {3,4} and at least one 4. At orders 13 and 14 it also requires that cubic vertices induce maximum degree ≤ 1. Every enumerated graph received a colouring that a simple independent verifier accepted. Search completeness is irrelevant because no graph failed, so the trust base is the generator's coverage plus the verifier.
- **Why ≥ 15 follows.** A minimum counterexample on n ≤ 14 vertices would be connected, K4-free, have degrees in {3,4} with some 4, and have cubic vertices inducing a graph of maximum degree ≤ 1, which gives n3 ≤ 2n4. Parity and n3 ≤ 2n4 leave exactly n4 ∈ {5,7,9,11,13} at order 13 and {6,…,14} at order 14, as the note says. I verified the prefix-normalisation cover argument: vertices in the same degree class with equal adjacency to earlier rows are interchangeable without changing processed rows. The K4 pruning (the last edge of any K4 triggers it) and the cubic-edge filter are also correct.
- **Reruns.** Rust `pcf-census 5 12` reproduced 1; 8; 75; 666; 6,975; 77,937; 943,509; 12,148,600 (2 min 15 s), including the built-in brute-force generator cross-check at orders 5 and 6. Rust order 13 with n4 = 5, 7, 13 reproduced 79,484; 10,760,307; 1,934,746. JavaScript `5 11` reproduced every count through order 11. Not rerun: order 12 in JavaScript, order 13 with n4 = 9 and 11, and all of order 14 (about 1.48 × 10⁹ graphs, several hours).
- **Independent checks (mine, separate code).**
  - Vertex augmentation with canonical forms enumerated all isomorphism classes of graphs with Δ ≤ 4 on n ≤ 9 vertices (2, 4, 11, 34, 122, 510, 2,590, 15,471 for n = 2 to 9). It PCF 5-coloured every one, using no reductions, with 0 failures (`03-scratch/indep_upto9.js`).
  - Within that enumeration, the census class has 1, 5, 22, 100 and 581 isomorphism classes at orders 5 to 9. Canonicalising the census generator's output gives 5, 22, 100 and 581 classes at orders 6, 7, 8 and 9, an exact match (`03-scratch/gen_classes*.js`). This extends the authors' generator cross-check from orders 5–6 to 7–9 at the level of isomorphism classes.
- **Gap.** Order 14 and the n4 = 9 and 11 strata at order 13 rely on a single run of the Rust port. That port is a line-by-line translation of the JavaScript program, so it is not independent. No logs, hashes or per-stratum timings were committed. Before claiming the bound in public, commit the run logs (or rerun order 14) and label it plainly as "a finite computation with one generator design, reproduced in two languages up to order 13 (strata 5, 7) and order 12". Also fix the stale "Proposition (order bound) … at least 14 vertices" paragraph in the note (§Finite census), which contradicts the later order-14 paragraph.
- **Significance.** A lower bound on the order of a counterexample is the kind of finite computation that `AGENTS.md` asks us not to count as a standalone advance. Report it as supporting evidence only.

## (c) Structural reductions

I checked these proofs line by line in `03-conflict-free-colouring.md` (§Structural reductions, §Three-edge cuts, §Two-vertex cuts, §Degree-three vertices).

- **Correct as written:**
  - the one-added-neighbour lemma;
  - leaf and degree-2 suppression;
  - cut vertices (the four colours other than v's can avoid the chosen singleton on at most three neighbours);
  - two-edge cuts (the Hall list sizes 1/3, 2/3 and 3/4 all check out, including the b_i = β_j case);
  - the K4 reduction (all three subcases, including the 2+2 old-neighbour case at x and the H+xy contradiction);
  - two-vertex cuts (degree bookkeeping and the union bounds 1/3 + 1/3 and 1/6 + 1/6);
  - degree-three vertices, giving the cubic-induced maximum-degree-1 bound and n3 ≤ 2n4 (both recolouring branches and the B = C contradiction).
- **Three-edge cuts.** The case analysis (matching, star plus edge, three-edge path, with the star excluded by 2-connectivity) is complete. The permutation facts are delegated to `check_03_cut_permutations.js`, which I reran: matching 390,625, required 170,565, star-and-edge 45,800, path 10,000, universal terminal 5,000, matching the note. This makes the lemma computer-assisted. Say so in the statement.
- **Minor fix.** The issue draft lists "2-connected, 3-edge-connected" while the handoff says 3-connected. Use "3-connected, 3-edge-connected and every edge cut separating two sets of at least two vertices has size at least 4".
- **Not in scope of (c), not reviewed in depth:** the matching four-edge-cut sufficient conditions, the few-defects lemma, the neutral-Kempe rank bound and the dominating-set condition. They are not needed for (a) or (b) and should not be advertised as results in the issue.

## Novelty gate (2026-11-26)

- **arXiv API** queries:
  - `all:"proper conflict-free"` returned 24 results, through 2611.26645 (9 Nov 2026).
  - `abs:"conflict-free" AND abs:"maximum degree"`, `abs:"conflict-free" AND abs:treewidth`, `abs:"odd coloring" AND abs:"maximum degree"`, and `all:Petrusevski AND all:conflict` found nothing beyond the list below.
  - I read the abstracts of 2611.26645, 2611.08534, 2611.03906, 2610.41668, 2609.11249, 2608.29375, 2608.10874, 2608.00555, 2512.22805, 2509.12560, 2509.06280, 2212.08936, 2402.09762, 2211.02818 and 2203.12248.
  - The nearest results are: Wang–Zhang 2512.22805, Thm 1.6 ((degree+2)-choosability for K4-minor-free graphs with Δ ≤ 4, so 6 colours), with outerplanar (degree+2) by Kashima–Škrekovski–Xu; Thm 1.4(1) of KSX ((degree+3), so 7 colours for Δ ≤ 4); Lu–Ying–Song (κ_G-choosability for mad < 12/5 or Δ ≤ 3); Xu 2610.41668 (mad < 8/3); Cho–Choi–Kwon–Park (chordal graphs); Liu 2203.12248 (layered treewidth w gives 8w−1).
  - New since the internal screen are three November 2026 papers by Das–Santra and Santra on structured classes (cocomparability, chordal subclasses, interval and biconvex graphs) and Pradhan–Sharma on block and proper interval graphs. None addresses Δ+1 for bounded treewidth or Δ = 4. I fetched Wang–Zhang's HTML and confirmed it gives no ordinary five-colour bound for any class at Δ = 4 and only layered-treewidth bounds.
- **Web search** (two queries, on CPS Δ = 4 and on treewidth, partial 3-trees, series-parallel or K4-minor-free with Δ+1) found no resolution of Δ = 4 and no five-colour bounded-treewidth result.
- **GitHub.**
  - Repository search for "proper conflict-free" coloring found only sandro-roch/proper-conflict-free-coloring, a general SAT solver.
  - Code search for "proper conflict-free", "conflict-free" coloring and "chi_pcf" returned 0 hits. Two further code queries hit the rate limit.
  - Code search for `conflict-free` in s66lem/conjectures and google-deepmind/formal-conjectures returned 0 hits. Hits in chy4pro/automath (an arXiv-abstract dump of 2608.10874 and a 2505.04543 triage line), the-omega-institute/trureturing (git "conflict-free" merge text) and ai-math-edu-lab/math-agents (a PSL(2,7) colouring log) are unrelated.
- **Upstream.** In 1337isnot1337/solved-conjectures, issue and PR searches for "conflict-free" found 9 unrelated items, "PCF" and "Petrusevski" found 0, and "Škrekovski" found only #156, which mentions a different Škrekovski conjecture. `git grep -i "conflict-free"` on origin/main (d87f8935) found nothing. On origin/research it found only two unrelated files (erdos617, gyarfas-sumner).
- **Conclusion.** No prior or concurrent resolution of Δ = 4 was found. The treewidth ≤ 3 five-colour theorem appears new. For ordinary colouring it strengthens the six-colour consequence of Wang–Zhang Thm 1.6 at Δ = 4 and extends it from treewidth 2 (K4-minor-free) to treewidth 3. Theirs is a list-colouring result and ours is not, so the two are incomparable as list statements. The absence of hits is not proof of novelty.

## Significance and placement

- **Would it be listed?** Under the `AGENTS.md` significance policy, the finite order bound (b) and the reductions (c) are supporting material, not listable results. The treewidth ≤ 3 theorem (a) is a genuine infinite-class partial theorem toward a well-known open conjecture with an active 2024–2026 literature. Its strength is comparable to recent journal results (Wang–Zhang, KSX outerplanar). It does not touch the core difficulty: the minimum counterexample is now known to have treewidth at least 4 and at least 15 vertices, but there is no general mechanism. It is borderline. I would list it only after the gaps in (a) are fixed and with a precise scope line. Issue-only is also defensible.
- **If listed**, it belongs near the bottom of "Partial results on open problems": immediately **below "Erdős–Oler conjecture"** and immediately **above "Hadamard existence, order 2396"**.
  - Below Erdős–Oler, and well below "Gyárfás's nearly bipartite graph conjecture" (its closest analogue): Gyárfás reduces the conjecture to a finite check (counterexample ≤ 330 vertices), which is strictly stronger in kind than a restricted-class theorem plus a lower order bound. The conjectures above it (Erdős–Sauer, Erdős–Purdy, Lonely Runner, Frankl and others) are also substantially more prominent.
  - Above Hadamard 2396: that entry proves obstructions for one order without settling existence, whereas this is a theorem for an infinite, minor-closed class.
- **Verification label:** ⬜ (no Lean). It is computer-assisted, with a finite-state closure plus written reductions.

## Readiness

**Ready after listed fixes** for posting as a tracking issue. That needs the corrected wording, which is supplied in `03-ISSUE-FINAL.md`. **Not ready** for a `main` publication package until:

1. the treewidth proof write-up adds the steps above;
2. the "two implementations" claim is corrected or a genuinely independent check is added;
3. order-14 logs are committed or the computation is rerun;
4. the stale order-bound proposition is fixed.
