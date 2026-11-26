# Referee report: thread 06, revised local irregularity / subcubic Conjecture 6.1

Referee pass of 2026-11-26. Inputs read: `06-HANDOFF.md`, `06-revised-local-irregularity.md` (all sections), `06-ISSUE-DRAFT.md`, `06-local-irregularity-cut-check.py`, `06-local-irregularity-rank-check.py`, `06-handoff/verify-kernel-cover.py`, `06-handoff/full_cactus.py` (diffed), `06-handoff/subcubic-frames.py` (run), receipts. Scratch: `REVIEW-2026-11-26/06-scratch/`.

## 0. Bottom line

- No resolution of Conjecture 6.1 (subcubic) or of the cubic case. The thread's honest claims are partial.
- The partial results that matter are **Theorem A** (one noncactus block of cycle rank at most 3, arbitrary rooted cacti attached, any maximum degree) and its subcubic consequences: the **K4-minor-free subcubic theorem** and **Corollary B**. They are computer-assisted. Their hand-written reductions check out, and all checkers rerun with matching output. One caveat: the cactus-normalisation layer that every one of them uses (junction domains, the seven arc modes, the cactus-side closure) exists in only **one implementation**. The "independent" kernel verifier imports that same module.
- The frame lemma (Lemma 2) and Lemma 1′ are correct but **not substantively new**. Lemma 1′ is the subcubic case of Theorem 8 of Lužar–Przybyło–Soták, arXiv 1611.02341, which has a published proof. Lemma 2 is then an immediate combination of that theorem with the exact "one locally irregular class plus a 2-colourable remainder" reformulation already used by Lužar et al. Lemma M is correct. It is a tool toward the unproved designation and absorption lemmas and has no standalone value.
- Novelty: no prior proof was found for the subcubic K4-minor-free case or for Theorem A. Both appear new, but the search was bounded.
- Significance is low to moderate: the results cover special graph classes in a niche conjecture. **Recommendation: issue-only for now.** If the maintainers list it later, it belongs near the bottom of "Partial results on open problems" (see §4).

## 1. Line-by-line review of the written lemmas

### Lemma 2 (frame lemma): Correct
- $Y$ is independent and each $y$ has exactly two $T$-edges, so $T$ is the full subdivision of $H$ plus isolated vertices. $H$ is loopless because $G$ is simple. Colour 1 on $S$ is locally irregular by (F1).
- In colours 2 and 3, each $y$ has degree 2. An $X$-vertex has degree equal to its number of $H$-edges of that colour. Under (F2) that number is 1 for $H$-degree 1 or 2 and $\deg_H\ge3$ otherwise, so it is never 2. The proof is complete.
- **Not new in substance.** Under (F2w), the frame lemma says only this: if $S$ is a locally irregular spanning subgraph whose complement is the full subdivision of a multigraph with no odd-cycle component, then $\chi'_{\rm irr}\le3$. That follows from LPS Theorem 8 ("$G$ not an odd cycle $\Rightarrow \chi'_{\rm irr}(\mathcal S(G))\le2$"). The ring-permutation proof of Lužar et al. uses the same reformulation. The frame terminology is a useful search framework, not a theorem to advertise.

### Lemma 1 (propagation): Correct
- The tree-propagation rules are consistent at degree-2 and degree-at-least-3 vertices. A non-tree edge is consistent exactly when its fundamental cycle has an even number of degree-2 vertices.
- The hypothesis covers all cycles, so in particular all fundamental cycles. Lemma 1′ supersedes it in the subcubic setting.

### Lemma 1′ (weak parity): Correct, but a known result
- Modes M and D check out:
  - In mode M a subdivision vertex has degree 2, against degree 1 at an internal vertex, 3 at a degree-3 hub and 1 at a leaf.
  - In mode D a subdivision vertex has degree 1, against degree 2 at an internal vertex and 3 at a hub. A leaf end is forbidden in mode D, and the proof handles it.
- The far-end parities are $L-1$ for mode M and $L$ for mode D, so exactly one mode fits two hub ends. A cycle component needs even length.
- It is the subcubic case of LPS Theorem 8. The note's statement that "the published proof is only sketched" overstates the gap. LPS give a minimal-counterexample proof with some brief steps. **Fix:** cite it as known, and present the thread's version as a short self-contained proof of the subcubic case.

### Lemma M (maximality inequality): Correct
- $Y'=(Y\setminus R)\cup A$ is independent.
- Each $y\in R$ has at most one neighbour in $X\setminus A$, using cubicity and $\ge2$ neighbours in $A$. Adding $R$ therefore keeps $G-Y'$ a forest.
- A greedy extension to a maximal independent set gives an MIL partition, because maximality forces degree at most 2 in the cubic graph. Then $|Y''|\ge|Y|-|R|+|A|$.
- Corollaries 1–3 are correct. In Corollary 3, $v_1\ne v_2$ because each $I^+$ vertex has a unique $Y$-neighbour, and two $I^+$ vertices are never consecutive on a path.
- Corollary 4 was not fully re-derived. Treat it as plausible.
- None of this proves the designation or absorption lemma; the note states this correctly. The "barrier-counting sketch" is explicitly not a proof.

### Two-cactus-side theorem and junction bounds: Correct for the hand parts; computational part from a single implementation
- I re-derived the triangle-petal rule (reject exactly $(1,1),(2,2)$ with distinct spoke colours) and the square rule (reject exactly $\{1,2\}$). Both match `blossom_use`.
- I re-derived the length-4 rows of the degree-two path table.
- The Hall reduction for branch slots is correct: it is a perfect matching with equal sides, and two distinct branch types cover every slot.
- I checked both "delete and restore" thresholds case by case, including the concavity step and the $t=2$, $p\in\{4,5\}$ type-3 patch. All are correct.
- The branch-signature argument is correct. A singleton signature lies in $\{1,2,3\}$ via the Sedlar–Škrekovski cactus theorem, and a flexible signature can be replaced by a leaf.
- I independently confirmed the probe signatures by brute force (`06-scratch/probe_signatures.py`): leaf $\{1\}$, two-vertex path $\{2\}$, rooted half bow-tie $\{3\}$.

### Parallel-path theorem ($k\ge3$): Correct as a computer-assisted result
- The $k\ge5$ hand argument is sound given the checked arc property (`distinct_high_spokes`).
- The $k=3,4$ cases were rerun: 216,832 and 2,025,366 cases.

### Kernel classification for Theorem A: Correct
- From $m=h+r-1$ and $2m\ge3h$ we get $h\le2r-2$.
- Rank 2 gives the theta.
- Rank 3 gives:
  - $h=2$: four parallel paths;
  - $h=3$: degrees $(4,3,3)$, which forces the triangle with two doubled sides;
  - $h=4$: cubic, so either $K_4$ or the square with two opposite doubled sides. A common exterior neighbour of a doubled pair would create a degree-1 vertex or a bridge.
- The list is complete.

### Theorem A (one noncactus block of rank at most 3, arbitrary rooted cacti): Correct with fixable gaps
The reduction from the infinite family to a finite enumeration is sound:
1. **Cactus parts.** Every rooted cactus at a block vertex is a bridge-branch (summarised by its signature) or a private cycle (normalised to a triangle or square by the arc-containment check, inductively from the leaves). This uses the proven signature lemma, the cactus theorem and the junction bounds.
2. **Junctions.** Unbounded numbers of attachments at a junction are removed by the delete-and-restore lemma. What remains is a finite list of inclusion-minimal junction domains: 8, 44 and 83 at arities 2, 3 and 4.
3. **Kernel edges.** A subdivided kernel edge with ornaments is a series composition of arity-2 domains. Monotonicity plus the closure give that it contains one of 7 minimal modes, plus the direct edge. Simplicity allows at most one direct edge per parallel class, and `verify-kernel-cover.py` enforces this via `parallel`.
4. **Finite check.** All (domain, mode) assignments on each kernel are covered by witness boxes. Kernel automorphisms are applied to witness boxes, and caps are sorted only for $K_4$, whose vertex-automorphism group is $S_4$. This is valid because the junction domains are closed under port permutation (built from permutations in `cap_domains_with_petals`) and every arc relation is symmetric (asserted in `kernel_cubes`).

Gaps and fixes:
- (a) State "simple" and "connected" explicitly. Decomposability is automatic, since every noncactus graph is decomposable.
- (b) **Independence label.** `verify-kernel-cover.py` recomputes the witness boxes and covers them in a different order. However, it imports `full_cactus.py`, whose first 260 lines are byte-identical to `06-local-irregularity-cut-check.py` apart from the docstring. The domain and mode derivation, on which everything rests, is therefore single-implementation. Say "independent coverage check of the exported certificates; shared domain/mode generator."
- (c) The Python code for domain and mode generation should get an independent reimplementation, or at least an independent brute-force cross-check of the 8/44/83 domains and 7 modes on small explicit ornaments, before any main-branch publication.
- (d) It is not a subcubic result as such, since non-subcubic attachments are allowed. Keep that scope sentence.

### Subcubic K4-minor-free theorem: Correct with fixable gaps
- The handling of unbounded rank is sound. The kernel $H$ of a subcubic noncactus block is a loopless, bridgeless (2-edge-connected) cubic multigraph.
- If $H$ is simple with more than 2 vertices, Dirac's theorem gives a $K_4$ minor. So $H$ has a doubled edge $uv$ with distinct exterior neighbours $a\ne b$; a common neighbour would force a bridge.
- The piece made of $u$, $v$, the two parallel routes and the tails to $a$ and $b$, together with their ornaments, is a connected two-terminal cactus side with distinct terminals and traversed cycle flag = true. $G$ minus the piece is connected by 2-edge-connectivity.
- The checker asserts that the acceptance-minimal relations over all cactus sides equal the seven nondirect arc modes. Hence the piece can be replaced by one arc-mode representative between $a$ and $b$, with exterior degrees at $a$ and $b$ unchanged.
- The new kernel is cubic, loopless and bridgeless, and its simple graph is a minor of the old one. Cycle rank drops by 1, so after finitely many steps the kernel is the 3-path theta, which is the checked $k=3$ case. Lifting back is valid.
- This handles **unbounded cycle rank**, not just rank at most 3, and needs no kernel certificate.
- Gap: the argument relies on the cactus-closure computation for unbounded cactus sides (single implementation). Explain in one line why the side's cut is "genuine".

### Corollary B: Correct with fixable gaps
- Correct:
  - Nontrivial blocks of a subcubic graph are vertex-disjoint.
  - The outside edge at a block vertex is a bridge.
  - A bridge $e=bq$ cutting off a component $C$ with exactly one noncactus block exists, taking the farthest noncactus block from a root.
  - The three test graphs ($C+e+$ probe) have one noncactus block with cactus attachments; the half bow-tie makes the test graph non-subcubic, but both single-block theorems allow arbitrary cacti.
  - The values $\delta_1\ne1$, $\delta_2\ne2$, $\delta_3\ne3$ cannot all coincide, so $C$ realises at least two port degrees.
  - Replacing $C$ by a leaf keeps the graph subcubic and noncactus, hence decomposable. The induction and lift are valid.
- Fix 1, wording: "attach the root of the leaf, of the two-edge path and of the rooted half bow-tie". The probe forcing degree 2 is the **two-vertex path** (root plus one pendant edge). A root with a pendant path of two edges forces 1, not 2; I checked this by brute force. The "size bound" section uses the correct name.
- Fix 2, honest restatement: in a subcubic graph, a noncactus block of rank at most 3 is a theta, a subdivided $K_4$ or a doubled square. Thetas and doubled squares are already $K_4$-minor-free. The doubled triangle and the 4-path theta have degree-4 kernel vertices. So Corollary B says exactly: **every decomposable connected subcubic graph each of whose noncactus blocks is $K_4$-minor-free or a subdivision of $K_4$ has $\chi'_{\rm irr}\le3$.** Only the $K_4$ certificate is needed beyond the $K_4$-minor-free theorem.

### Rank ≤ 4, minimum degree ≥ 2 theorem: Correct (computer-assisted)
- Rerun passed: 87 kernels, 1,781,720 assignments and 220,942 witnesses.
- The rank-5 run has a single implementation and was not rerun.

## 2. Reruns (2026-11-26, Python 3.12, this worktree)

| Check | Result |
| --- | --- |
| `python 06-local-irregularity-cut-check.py` | Exit 0 in 1 min 46 s. Domains (8,44,83); 8 arc modes including the direct edge; parallel-path cases 216,832 / 2,025,366; closure 80,919 transitions, 124 states; 24 traversed components; 8,198 bridge joins; probe sizes (2,3,9,9) / (1,2,3,5,5,8,13); "all two-ended cactus connectors use the same seven arc modes". Identical to the saved receipt. Log: `06-scratch/cut-check.log`. |
| `python 06-local-irregularity-rank-check.py` | Exit 0 in 3 min 18 s. "Verified all normalized noncactus cases through cycle rank four" (87 / 1,781,720 / 220,942). Log: `06-scratch/rank-check.log`. |
| `06-handoff/verify-kernel-cover.py` | Exit 0. $K_4$ passed at cube 15,242 (2,816 s), the doubled triangle at cube 2,209 (1 s) and the doubled square at cube 13,062 (79 s). The cube indices match the saved receipt. Log: `06-scratch/kernel-cover.log`. The first launch with `python -I` failed on import only, because `-I` drops the script directory from the path; the rerun used plain `python`. |
| `06-handoff/subcubic-frames.py control` and `exhaustive 12` | Exit 0 in 2 min 12 s. Counts match A243393 through order 12. Only $K_4$ is 3-colourable without a frame. Non-3-colourable counts are 0,1,1,1,2,2,3,3,5,6,8,12 for orders 1–12. Log: `06-scratch/frames.log`. `exhaustive 13` (all orders 1–13) exited 0 in 6 min 57 s: 69,322 graphs at order 13, of which 69,306 are framed and verified, 16 have no 3-colouring, and none is 3-colourable without a frame. Log: `06-scratch/frames13.log`. |
| `06-handoff/lemma1prime-check.py` | Passed on 13,390 random multigraphs. |
| **Independent referee test** `06-scratch/lir_random_check.py` (my own backtracking solver; shares no code with the thread) | Controls: bow-tie rejected, $K_4$ accepted, series-parallel tester correct on $K_4$. (A) Random graphs in Theorem A's class: kernels theta3, theta4, $K_4$, doubled triangle and doubled square, edges subdivided to length 1–4, random rooted cacti (pendant paths, 3/4/5-cycles, nested), up to 45 edges. (B) Random connected subcubic noncactus $K_4$-minor-free graphs of order 8–30. Seed 20261126, exit 0 in 15 min: **no counterexample**. (A) covered 19,999 graphs: $K_4$ 4,059, doubled square 3,953, doubled triangle 3,948, theta3 3,946, theta4 4,093. (B) covered 43,324 graphs (orders 8–30). Log: `06-scratch/random-check.log`. |
| **Independent referee test** `06-scratch/lir_random_blocks.py` | Random subcubic block trees of subdivided $K_4$, theta3 and doubled-square blocks joined by bridge paths, with pendant paths and bridged triangles (Corollary B's class). Seed 20261126, exit 0 in 19 min: **no counterexample among 2,847 graphs** with up to 60 edges. Log: `06-scratch/random-blocks.log`. These random tests are evidence only, but they are independent of the thread's normalisation code. |

## 3. Prior-resolution and novelty gate (2026-11-26)

**arXiv API.**
- `abs:"locally irregular"`, sorted by date, returned 57 hits; all relevant ones were inspected.
- New since the thread's screen:
  - 2609.09355, Lintzmayer–Mota–Sambinelli–dos Santos (Sep 2026): $\chi'_{\rm irr}\le18$ for all decomposable graphs, improving 220. **The draft's "bound 220" is stale and must be updated.**
  - 2609.31205, Madarasi–Simon: locally irregular 2-edge-colouring is NP-complete on cubic planar graphs.
  - 2603.13178: total colourings, proves tlir ≤ 2 for subcubic graphs and cacti; a different problem.
- Older, all different problems or classes: 2111.08111 (unicyclic graphs and cacti with vertex-disjoint cycles), 2207.03941 (cacti), 2211.08270, 2412.04200 / AMC 2026 (2-multigraphs), 2402.18739 (regular graphs of large degree, 4 colours), 2405.13893, 2502.07933, 2511.14514.

**Citations of 2210.04649 (Semantic Scholar).**
- The citing papers are 2609.31205, 2609.09355, "Locally irregular edge-coloring of claw-free graphs with maximum degree 4" (2026: $\chi'_{\rm irr}\le5$), the 2-multigraph paper (2026), the Malatya algorithm paper (2025), "Highly irregular graph decompositions" (2024), 2405.13893 and 2211.08270.
- None proves Conjecture 6.1, the cubic case, or a $K_4$-minor-free, series–parallel or outerplanar case.

**Web searches.**
- Queries: subcubic or cubic three colours 2025–2026; series-parallel, $K_4$-minor-free, outerplanar or treewidth with locally irregular; Sedlar–Škrekovski bicyclic or cyclomatic number.
- Only known class results turned up: trees, cacti, unicyclic graphs, claw-free subcubic graphs, ring-permutation graphs, generalized Petersen graphs, split graphs, large minimum degree and regular graphs of large degree.
- Bensmail–Dross–Nisse (Graphs Combin. 2020) give $3k+1$ for $k$-degenerate graphs, hence at most 7 for $K_4$-minor-free graphs. That is not 3.
- LPS 1611.02341 Theorem 8 covers Lemma 1′; see §1.

**GitHub.**
- `gh search repos "locally irregular"` found:
  - DomenFlakusBosilj/locally_irregular_edge_colorings: a 2020 student computational project testing cubic graphs, no proof;
  - KevinMaSAI/doubled-graphs-local-irregularity: a 2026 AI-assisted preprint on doubled graphs $^2G$, claiming a subcubic proof of the **2-multigraph** conjecture. This is a different problem from Conjecture 6.1 and should be cited as related work;
  - DannyExperiments/imbalance-conjecture and sen-ltd/sukoro: unrelated.
- `gh search code` for "irregular" in s66lem/conjectures, chy4pro/automath, the-omega-institute/trureturing, ai-math-edu-lab/math-agents, google-deepmind/formal-conjectures, openai/math and 1337isnot1337/solved-conjectures found nothing on local irregularity.
- bespokelabsai/conjecture-bench(-old) lists the revised conjecture as an open benchmark target (track A, #28) with no claimed solution.
- Several code searches were rate-limited (HTTP 403/503) and are not exhaustive.

**Upstream.**
- `gh search issues --include-prs` in 1337isnot1337/solved-conjectures for "local irregularity", "locally irregular", "Sedlar" and "2210.04649": no hits.
- `git grep -il irregular origin/main` and `origin/research`: no local-irregularity entry.

**Conclusion.** No prior resolution of Conjecture 6.1, the cubic case, the subcubic $K_4$-minor-free case, or Theorem A was found. The partial theorems appear new, subject to the usual bounded-search caveat. Lemma 1′ and, in substance, the frame lemma are not new.

## 4. Significance and placement

- Conjecture 6.1 is a genuine open conjecture, but local irregularity is a niche topic. The proved cases are special graph classes:
  - subcubic graphs whose noncactus blocks have treewidth at most 2 or are $K_4$-subdivisions;
  - graphs with a single noncactus block of rank at most 3.
- These are the "special case" partial results that the AGENTS.md significance policy discourages as standalone targets. The results are also computer-assisted, through a single-implementation normalisation layer.
- **Recommendation: issue-only, not listed**, until (i) the domain/mode generator has an independent reimplementation and (ii) there is a significance argument stronger than "a new subclass".
- If the maintainers nevertheless list it, the right place in "Partial results on open problems" (origin/main) is **immediately below "Erdős–Oler conjecture"** and **immediately above "Hadamard existence, order 2396"** (currently the last entry):
  - Its scope, an infinite but special graph class of a lesser-known conjecture, is narrower in impact than the Erdős–Oler lattice-packing case and the Erdős–Gyárfás abelian-cover theorem.
  - It is a genuine infinite-family theorem, whereas the Hadamard 2396 entry establishes only obstructions and no existence.

## 5. Readiness

**Not ready for main-branch publication. Ready to post as an issue after the fixes below**, which are reflected in `06-ISSUE-FINAL.md`:
1. Update the general bound to 18 (arXiv 2609.09355).
2. Relabel Lemma 1′ as the subcubic case of LPS Theorem 8, and the frame lemma as a reformulation.
3. Restate Corollary B as "$K_4$-minor-free or $K_4$-subdivision blocks".
4. Fix the probe name to "two-vertex path".
5. Label the kernel verification as an independent coverage check that shares the domain/mode generator.
6. Drop the claimed theorem labels for unproved items: the absorption lemma, the designation lemma and the frame conjecture.
