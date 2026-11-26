**Released for anyone to use.** This issue records partial progress on the subcubic case of the revised Local Irregularity Conjecture. Nobody holds a claim on this target. Anyone may use, extend or cite these results toward a full proof or disproof.

## Target

[Conjecture 6.1 of Lužar, Maceková, Rindošová, Soták, Sroková and Štorgel](https://arxiv.org/abs/2210.04649): every connected decomposable graph with maximum degree 3 has a locally irregular 3-edge-colouring, that is, $\chi'_{\rm irr}(G)\le3$.

The general revised conjecture of Sedlar and Škrekovski excludes only the bow-tie cactus, which is not subcubic. It appears as [Conjecture 27 of arXiv 2207.03941](https://arxiv.org/abs/2207.03941), which also proves the cactus case, and as [Conjecture 3 of arXiv 2603.13178](https://arxiv.org/abs/2603.13178). Both the subcubic and the cubic cases are open.

## What has been achieved

- **Theorem A (one block of low cycle rank).** Let $G$ be a finite connected simple graph with exactly one noncactus block, and let that block have cycle rank at most 3. Arbitrary rooted cacti may be attached, and the maximum degree is unrestricted. Then $\chi'_{\rm irr}(G)\le3$.
- **Theorem B (subcubic, $K_4$-minor-free).** Every connected decomposable subcubic graph with no $K_4$ minor has $\chi'_{\rm irr}\le3$. The cycle rank is unbounded.
- **Corollary C.** The same conclusion holds for connected decomposable subcubic graphs in which every noncactus block is $K_4$-minor-free or a subdivision of $K_4$.
- **Earlier computer-assisted results for the general revised conjecture**, at any maximum degree:
  - noncactus graphs with a two-edge cut into two cacti;
  - graphs with a single noncactus block made of $k\ge3$ parallel paths, with cactus attachments;
  - noncacti of minimum degree at least 2 and cycle rank at most 4.
- **Written proofs (not computer-assisted):**
  - noncacti whose vertices of degree at least 3 form an independent set;
  - for cubic graphs, a maximality inequality for maximum "MIL" partitions, where $Y$ is independent and $G-Y$ is an induced linear forest.

## What has been done

- **Theorem A**
  - **Written reduction.** Bridge-attached cacti become forbidden-degree constraints through the cactus theorem. Private cycles are normalised to triangles or squares. Unbounded attachments at a vertex are removed and restored afterwards by a degree-avoidance lemma. This leaves finitely many junction domains (8, 44 and 83) and 7 connector modes.
  - **Kernels.** Suppressing degree-2 vertices of the block gives one of five kernels:
    - a theta with 3 or 4 paths;
    - $K_4$;
    - a triangle with two doubled sides;
    - a square with two opposite doubled sides.
  - **Certificates.** The theta cases are checked exhaustively. The other three kernels have witness-box covering certificates:
    - $K_4$: $4.68\cdot10^{10}$ cases, 692 witnesses;
    - doubled triangle: $1.57\cdot10^{9}$ cases, 484 witnesses;
    - doubled square: $2.94\cdot10^{11}$ cases, 1,366 witnesses.
  - **Coverage check.** A second program checked the coverage in a different coordinate order, but it shares the domain and mode generator with the producer.
- **Theorem B**
  - A $K_4$-minor-free subcubic noncactus block has a cubic kernel with a doubled edge (Dirac).
  - The doubled-edge piece is a two-terminal cactus. A checked equality shows that it can be replaced by one of the 7 connector modes.
  - Iterating the replacement reduces the block to the 3-path theta.
  - Blocks are joined by bridges and handled by peeling, using port probes that force degree 1, 2 or 3.
- **Independent review.** A separate reviewer agent checked the written reductions line by line and reran every checker, with matching output. Its own brute-force solver found no counterexample on random graphs from the classes of Theorems A–C.
- **Evidence (not proofs).**
  - Every connected subcubic graph through order 13 is either a nondecomposable cactus or 3-colourable by a "frame" (one locally irregular colour plus a 2-colourable rest). The counts match OEIS A243393. The one exception is $K_4$, which is 3-colourable directly.
  - Random cubic graphs up to order 70 also have frames.

## What a full proof would still need

- **Remaining subcubic blocks:** noncactus blocks with a $K_4$ minor that are not subdivisions of $K_4$, such as the prism and $K_{3,3}$.
  - Their kernels are cubic graphs of unbounded size, so the finite-kernel certification of Theorem A cannot be extended directly. Some structural induction would be needed.
  - One route is the frame conjecture: every connected decomposable subcubic graph other than $K_4$ has a frame. Through Lužar–Przybyło–Soták Theorem 8, that would give 3 colours.
- **The cubic case.**
- **Housekeeping:** an independent reimplementation of the junction-domain and connector-mode generator used in Theorem A.

## Prior work checked

- [Lužar–Przybyło–Soták](https://arxiv.org/abs/1611.02341): $\chi'_{\rm irr}\le4$ for decomposable subcubic graphs, plus computer checks of small cubic and subcubic graphs.
- Lužar et al.: Conjecture 6.1 holds for claw-free subcubic graphs, cycle permutation graphs and generalized Petersen graphs.
- Papers on cacti, unicyclic graphs, split graphs and large minimum degree.
- The general bound of 18 in [arXiv 2609.09355](https://arxiv.org/abs/2609.09355), and arXiv 2609.31205.
- Bensmail–Dross–Nisse's bound for degenerate graphs.
- Papers citing 2210.04649 through November 2026.
- Searches of arXiv, the web and GitHub (including public AI-solution repositories), and this repository's issues, PRs and branches.

None of these proves the subcubic or cubic case or covers the classes above.

The doubled-graph problem ([arXiv 2412.04200](https://arxiv.org/abs/2412.04200)) and locally irregular total colourings are related but distinct problems.

## Credit and provenance

The conjecture is due to Sedlar and Škrekovski. The subcubic formulation and the claw-free, cycle-permutation and generalized Petersen cases are due to Lužar et al. The cactus theorem is due to Sedlar–Škrekovski. Theorem 8, which also underlies our frame lemma, is due to Lužar–Przybyło–Soták.

Claude Opus 5.5 (Anthropic) research agents produced the new results, and a separate Claude Opus 5.5 agent reviewed them. No human has refereed them, and there is no Lean formalization. No priority claim is made.

The full write-ups, checkers and review are not public yet. They will be linked in a comment on this issue.
