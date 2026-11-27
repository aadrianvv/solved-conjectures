# Verification

## Tree reconstruction after long subdivisions

Run the three standard-library Python checks in the [reproduction instructions](research-results/stanley-tree-subdivisions/README.md#reproduction). They compare ordinary cut polynomials, rooted products, subdivision factors and competing branch configurations. [Independent mathematical review](research-results/stanley-tree-subdivisions/REVIEW.md)

## Circular windows in convex tilings

Run `python3 results/langi-wang-convex-tiling/check_sectors.py` with standard Python. The script checks one stage with 512 polygon sides, including sector convexity, inball clearance, diameter bounds, annular areas and which tiles lie inside the test disk. The all-scale estimates and the logarithmic-density bound have written proofs. [Construction](../results/langi-wang-convex-tiling/PROOF.md) · [Logarithmic density](../results/langi-wang-convex-tiling/LOG-DENSITY.md) · [Review](../results/langi-wang-convex-tiling/REVIEW.md)

## Universal Gaussian cold spots of dual type A

Run `python3 docs/research-results/dual-a-universal-cold-spots/verify.py` with standard Python. The verifier compares thirty degrees of the exact theta and product series in ranks one through ten. Direct lattice sums separately check the value, the directional Hessian and a displaced point for nine choices of rank and parameter. [Mathematical proof](research-results/dual-a-universal-cold-spots/PROOF.md) · [Review and reproduction details](research-results/dual-a-universal-cold-spots/REVIEW.md)

## Gaussian cold spots of high-rank type-A root lattices

Run `python3 docs/research-results/root-a-high-rank-cold-spots/check_central.py` and `python3 docs/research-results/root-a-high-rank-cold-spots/check_displaced.py`. The first script certifies 700 strict central-class comparisons across ranks 4 through 23 and ten more in ranks 4 and 5 at large scales that test both parities. The second compares four noncentral translates and two origin translates with the deep classes in ranks 5 and 9 at four times the natural logarithm of two. Both use explicit bounds on omitted Gaussian tails. The uniform all-translation theorem has a written proof. [Combined theorem](research-results/root-a-high-rank-cold-spots/README.md) · [Small-scale review](research-results/root-a-high-rank-cold-spots/SMALL-SCALE-REVIEW.md) · [Half-line review](research-results/root-a-high-rank-cold-spots/HALF-LINE-REVIEW.md)

## Leech lattice cold-spot coefficients

Run `python3 docs/research-results/leech-cold-spots-asymptotics/verify.py` with standard Python. Integer bisection bounds the optimized leading coefficient for each of the 23 deep-hole types. The verifier checks that $`E_8^3`$ has the smallest coefficient and $`D_{24}`$ the second smallest. The localization of the Gaussian minimizers is proved analytically. [Proof](research-results/leech-cold-spots-asymptotics/PROOF.md) · [Review](research-results/leech-cold-spots-asymptotics/REVIEW.md)

From `docs/research-results/leech-cold-spots-asymptotics`, run `python3 check_leech.py` for rational enumeration in Shimada’s lattice basis and `python3 check_resonance.py` for the finite numerical models. The first checks the two coefficients at $`A_{24}`$. The second tests the signs below, at, and above the equality threshold for later unbalanced shells. [Mixed-hole proof](research-results/leech-cold-spots-asymptotics/MIXED-HOLES.md) · [Reproduction and numerical scope](research-results/leech-cold-spots-asymptotics/MIXED-HOLES-REVIEW.md)

## Permutation digraph general position conjecture

Run `python3 results/permutation-digraph-general-position/verify.py` to check the marker constructions and reversal geodesics by BFS. Add `--extended` for all six test pairs including word length five. [Written proof](../results/permutation-digraph-general-position/PROOF.md) holds throughout the conjectured range.

## General position number of oriented trees

Run `python3 results/general-position-oriented-trees/verify.py` to compare the five-state recurrence and its witnesses against exact directed-distance oracles. Add `--atlas` with NetworkX available for all orientations of the nonisomorphic trees through order nine. [Written proof](../results/general-position-oriented-trees/PROOF.md).

## Mobile general position complexity

Run `python3 results/mobile-general-position-complexity/verify.py` to compare source recolouring reachability with actual host moves checked by ordinary graph distances. Add `--extended` for more source graphs and endpoint pairs. The [written proof](../results/mobile-general-position-complexity/PROOF.md) applies to every input.

## Barrett–Evans–Hall–Kempton’s spectrally extreme graph conjecture

Run `python3 results/barrett-evans-hall-kempton-se/check_small_parameters.py` for exact integer comparator checks. The [audit](../results/barrett-evans-hall-kempton-se/AUDIT.md) explains how to generate the small simple endpoints using nauty and certify their strict inequalities using an integer C++ checker. The proof for orders at least 36 and weighted interpolation are analytic.

## Liang’s slice-period conjecture

Run `python3 results/liang-slice-period/check.py` for the exact recurrence on 684 transfer representatives. The [audit](../results/liang-slice-period/AUDIT.md) gives instructions for the independent labeled C++ evaluator. The [all-three-heap supplement](../results/liang-slice-period/THREE-HEAPS.md) has its own [exact checker](../results/liang-slice-period/all_three.py).

## Liang’s 0.3123 slice problem

Run `python3 results/liang-03123-slice/verify.py` for the exact recurrence closure and 169 bulk cases. The [audit](../results/liang-03123-slice/AUDIT.md) gives instructions for the independent C++ verifier.

## Plambeck–Siegel infinite quotient conjecture for 0.3312

Run `python3 results/plambeck-siegel-03312/verify.py` to check the 9,570-state transfer certificate and witness bits. [The proof](../results/plambeck-siegel-03312/PROOF.md) extends this finite closure calculation to heaps of arbitrary sizes. [The audit](../results/plambeck-siegel-03312/AUDIT.md) includes instructions for the independent C++ checker. The [four-heap supplement](../results/plambeck-siegel-03312/FOUR-HEAPS.md) has its own [exact checker](../results/plambeck-siegel-03312/check_four.cpp).

## Misère Domination Game

Run `python3 results/misere-domination-game/verify.py` for exact minimax on octal partitions, direct graph outcomes, and parameter-family witnesses. The [written proof](../results/misere-domination-game/PROOF.md) applies to every path, every cycle, and every sum of octal 0.337 heaps.

## Builder–Blocker general position complexity conjecture

Run `python3 results/builder-blocker-general-position-complexity/verify.py` to compare both host games with the source optimization Node Kayles games by exact minimax. Add `--atlas` with NetworkX available to include the independent graph atlas. [Written proof and scope](../results/builder-blocker-general-position-complexity/PROOF.md).

## Fractional general position conjecture for square grids

Run `python3 results/fractional-general-position-square-grids/verify.py --limit 110 --also 199 200` to check the rank marginals, legal mass couplings and primal longest paths in exact rational arithmetic. The [written proof](../results/fractional-general-position-square-grids/PROOF.md) treats every even and odd order.

## Erdős’s one-third pinned-distance conjecture

Run `python3 results/erdos-general-position-pinned-distances/verify.py` to check the radius-class identities, the six pair-multiplicity bounds and the diameter argument on 4,675 grid sets and two additional configurations. The [proof](../results/erdos-general-position-pinned-distances/PROOF.md) and [independent review](../results/erdos-general-position-pinned-distances/REVIEW.md) give the separate compactness and covariance argument for arbitrarily large sets. The [arbitrary-collinearity review](../results/erdos-general-position-pinned-distances/UNRESTRICTED-REVIEW.md) documents the added incidence, sampling and limiting arguments. Run `python3 results/erdos-general-position-pinned-distances/verify_farthest_conflicts.py` for the exact finite geometric checks.

## Cioba–Savvas shutout number conjecture

Run `python3 results/cioba-savvas-shutout-number/verify.py` to check 127,850 endpoint updates for exact independence polynomials and 432 played games under the stated degree condition. The [written proof](../results/cioba-savvas-shutout-number/PROOF.md) is independent of the finite checks.

The pinned strict source build, all-owned transitive axiom audit (288 declarations, 241 theorems, 54 private declarations, nine required endpoints), and stock-kernel replay passed for the exact four-module Lean closure proving Conjectures 3.2 and 3.3 over arbitrary finite simple graphs. The aggregate repository gate is separate. [Lean scope and receipt](../results/cioba-savvas-shutout-number/FORMALIZATION.md).

## Elizalde–Rivera–Zhuang’s big-descent Schur-positivity conjecture

Run `python3 results/erz-big-descent-schur/verify.py` for the direct permutation and Frobenius-coordinate checks. Run `python3 results/erz-big-descent-schur/check_review.py` for the two-variable RSK expansion through degree nine and the higher-Durfee transforms. The [review](../results/erz-big-descent-schur/AUDIT.md) explains how the proof covers every degree.

## Sidon products, pattern packings and the four-cycle threshold

Run `python3 results/byrne-tait-odd-sidon/verify.py` for the two finite group actions, `python3 results/blitvic-kammoun-steingrimsson-packing-cutoff/check.py` for direct enumeration from packing windows, and `python3 results/erdos-85-four-cycle-threshold/check_affine_paths.py` for the affine path and charging tests. Each proof has a separate review identifying the arguments that cover its unrestricted parameters.

## Book domination roots and monophonic circulants

With SymPy 1.14.0 installed, run `python3 docs/research-results/rather-book-domination-roots/check.py` to enumerate dominating sets, isolate real roots over the rationals and verify the sign constants. Run `python3 docs/research-results/tuite-thomas-chandran-circulants/check.py` with standard Python to check finite border graphs, the uniform jump families and the order-15 exception. [Book review](research-results/rather-book-domination-roots/REVIEW.md) · [Circulant review](research-results/tuite-thomas-chandran-circulants/REVIEW.md)

## Oriented general position spectrum nonconstancy conjecture

Run `python3 results/oriented-general-position-spectrum-nonconstancy/verify.py` to check the two orientation certificates on all 33,868 labeled simple graphs of orders zero through six. The [proof](../results/oriented-general-position-spectrum-nonconstancy/PROOF.md) does not depend on finite computation.

## The lower oriented general position NP-hardness conjecture

Run `python3 results/lower-oriented-general-position-np-hardness/verify.py` to compare exact Hamilton-path counts to all 511,102 orientations of the 8,555 labelled graphs on up to six vertices with at least two leaves. The [proof](../results/lower-oriented-general-position-np-hardness/PROOF.md) is uniform and does not use this regression.

## Welton–Khudairi–Tuite lower general position product conjecture

Run `python3 results/welton-khudairi-tuite-lower-gp-product/verify.py`. It builds the actual factors and Cartesian products and checks all twin profiles, all six-vertex-base supports, and an endpoint witness for every outside product vertex at parameters 7, 8, 11 and 15. The [written disproof](../results/welton-khudairi-tuite-lower-gp-product/PROOF.md) holds uniformly, independently of the finite checks.

## Bollobás–Erdős–Tuza conjecture

Run `python3 results/erdos-611-clique-transversals/check.py`, `python3 results/erdos-611-clique-transversals/check_recursive.py` and `python3 results/erdos-611-clique-transversals/check_structure.py`. These check the base graphs, the substitution formula, 150 exact recurrence steps and the independent-block counting identity. The [review](../results/erdos-611-clique-transversals/AUDIT.md) identifies the arguments giving the asymptotic bounds.

## Alexandersson’s graphical dist conjecture

Run `python3 results/alexandersson-graphical-dist/check.py` and `python3 results/alexandersson-graphical-dist/check_unions.py`. Subset inversion and direct vertex insertion yield identical coefficients. Both verifiers also compare with literal enumeration on small ordered graphs. [Exact counting proof](../results/alexandersson-graphical-dist/proof.md) · [Independent review](../results/alexandersson-graphical-dist/review.md). Lean verifies the 71-vertex graph and its 310 edges, the triangle insertion law, exactly two nonreal roots of the computed coefficient polynomial, and every limiting root for each positive even order. The full orientation-count identity and convergence to the graph family remain in the written proof. [Formal scope and receipt](../results/alexandersson-graphical-dist/FORMALIZATION.md).

## Chandran–Di Stefano–Haritha–Thomas–Tuite general-position conjecture

Run `python3 results/general-position-nordhaus-gaddum/verify.py` to check all labelled graphs through order six and 2,000 seeded larger graphs. The [written proof](../results/general-position-nordhaus-gaddum/PROOF.md) is uniform; the [audit](../results/general-position-nordhaus-gaddum/AUDIT.md) separates the geodesic and induced-path targets.

## Brown–Cameron’s independence-root sector and stability problems

Run `python3 results/brown-cameron-stability/verify.py` for exact moment and avoidance checks on all 1,024 labelled graphs on five vertices at three edge densities, plus six finite rational probability certificates. This is the standard-library check run in CI. For an optional local Z3 check of four algebraic claims, install `z3-solver==4.16.0.0` and run `python3 results/brown-cameron-stability/verify_z3.py`. The [written proof](../results/brown-cameron-stability/PROOF.md) establishes the asymptotic bounds without either script. [Review and local replay output](../results/brown-cameron-stability/REVIEW.md) · [Source audit](../results/brown-cameron-stability/AUDIT.md).

## Gawron–Ulas’s partition-sign nonperiodicity conjecture

The [Lean verification receipt](../results/gawron-ulas-partition-signs/verification/receipt.json) covers the four-module closure for Conjecture 4.3. The [formalization page](../results/gawron-ulas-partition-signs/FORMALIZATION.md) gives the statement, scope, and commands for strict compilation, all-owned axiom auditing, and stock-kernel replay.

## Chandran–Di Stefano–Haritha–Thomas–Tuite monophonic product conjecture

Run `python3 results/monophonic-product-nordhaus-gaddum/verify.py` to verify all triples in the 45-vertex witness, enumerate 262,144 possible star-center sets, and check exact optimal independent monophonic colorings with 20 and 27 colors. The [written proof](../results/monophonic-product-nordhaus-gaddum/PROOF.md) covers the infinite family without the enumeration. [Source and review](../results/monophonic-product-nordhaus-gaddum/AUDIT.md). Lean verifies the 45-vertex counterexample, the exact color counts 20 and 27, and the complement count for every prism length. The original graph’s all-order color formula remains in the written proof. [Formal proof and verification receipt](../results/monophonic-product-nordhaus-gaddum/FORMALIZATION.md).

## Written results on eleven open problems

The [partial-results catalogue](../CONTENTS.md#partial-results-on-open-problems) links the statements, proofs, primary sources and open cases. The following checkers reproduce finite parts of five arguments. Their conclusions and scope are described on the individual result pages.

| Problem | Run from the repository root | Exact checks |
| --- | --- | --- |
| [Erdős–Purdy conjecture](../results/erdos-block-size-multiplicity/) | `python3 results/erdos-block-size-multiplicity/check_field.py` | All 65,536 subsets of the field of order 16, with four subplane calculations. |
| [Erdős–Hajnal set-mapping conjecture](../results/erdos-hajnal-set-mapping/) | `python3 results/erdos-hajnal-set-mapping/check.py` | 5,484 matching requests across 1,272 eligible colorings and 3,690 circuits across 930 matrices. |
| [Erdős–Hammer convex-subset problem](../results/erdos-hammer-838/) | `python3 results/erdos-hammer-838/check_binary.py` | 65,808 nonempty planar subsets and 43 exact probability coefficients. |
| [Erdős’s bounded blocking-set problem](../results/erdos-bounded-blocking-set/) | `python3 results/erdos-bounded-blocking-set/check_spread.py` | All 4,161 lines of the example, plus a Pappus witness in the non-Desarguesian plane. |
| [Gyárfás’s nearly bipartite graph conjecture](../results/gyarfas-nearly-bipartite/) | `python3 results/gyarfas-nearly-bipartite/check_grid.py` | 68 subdivisions, 408 paths and 136 forbidden parity patterns covering all switchings. |

## Asgarli–Ghioca–Yip blocking-pencil problem

Run `python3 results/asgarli-ghioca-yip-blocking-pencil/verify.py` for 266,184 shift sets over eight fields, 367 regular seed instances, 8,577 graph–line intersections and both squarefree quartic twists without rational roots over the field of order three. A second researcher checked the general proofs and the order-32 hyperplane computation. [Proof](../results/asgarli-ghioca-yip-blocking-pencil/PROOF.md) · [Independent review and source audit](../results/asgarli-ghioca-yip-blocking-pencil/AUDIT.md).

The [complete scoped Lean proof](../results/asgarli-ghioca-yip-blocking-pencil/FORMALIZATION.md) eliminates `RegularOrderingEstimate` as a hypothesis. The [31-module receipt](../results/asgarli-ghioca-yip-blocking-pencil/verification/receipt.json) records strict source compilation, the all-owned axiom audit and stock kernel replay. The finite Python checks are supplementary.

## Mallik–Diwan–Kothari degree-count conjecture

Run `python3 results/mallik-diwan-kothari-degree-count/verify.py`. The checker verifies all 3,420 three-edge matchings and all 36 edge deletions on the 16-vertex counterexample directly. Separate Hall checks sample 15 members of the infinite family. The [proof](../results/mallik-diwan-kothari-degree-count/PROOF.md) does not depend on the checker. [Source and audit](../results/mallik-diwan-kothari-degree-count/AUDIT.md). Lean constructs a minimal extendable bipartite counterexample for every stated even order and verifies its exact edge and degree counts. Explicit permutations identify the original 16-vertex search witness with the smallest family member. [Lean theorems and verification receipt](../results/mallik-diwan-kothari-degree-count/FORMALIZATION.md).

## The Steiner triple system sail problem

Run `python3 results/steiner-triple-system-sail/verify.py` to enumerate all 4,224 colorings of the systems of orders seven and nine and check each of the 24,576 disjoint opposite-colored block pairs. Fourteen additional colorings of systems on 87 and 127 points exercise the bound above its sufficient threshold. A second researcher rederived the general argument, checked the packing corollary and reran the verifier. [Proof](../results/steiner-triple-system-sail/PROOF.md) · [Review and source audit](../results/steiner-triple-system-sail/AUDIT.md). Lean proves the uniform count, existence from order 84, the limiting lower density of 1/49, the one-color disjoint packing with limiting lower rate 1/4802, and the fixed disjoint-union Ramsey consequence. [Lean theorems and verification receipt](../results/steiner-triple-system-sail/FORMALIZATION.md).

## En Gad–Yaakobi–Jiang–Bruck constant-weight strong WOM coding problem

Run `python3 results/constant-weight-strong-wom/verify.py` to construct the local labels by exact conditional expectations and test the encoder and decoder. The checker covers 7,252 state–message pairs exhaustively across three examples, all 51 endpoint states in its check, and 12 further round trips with 78-bit messages. A second researcher checked the all-length proof and separately tested the label covering property on 92,159 layer/state pairs. [Proof](../results/constant-weight-strong-wom/PROOF.md) · [Independent review and audit](../results/constant-weight-strong-wom/AUDIT.md).

## Nathanson’s linear-form Sidon systems conjecture

Run `python3 results/nathanson-sidon-systems/verify.py` to enumerate outputs in 119 signed, bilinear and higher-arity fixtures. The [proof](../results/nathanson-sidon-systems/PROOF.md) is for every nonzero integer coefficient vector, independently of the finite checks. [Source and audit](../results/nathanson-sidon-systems/AUDIT.md).

Lean proves all three original questions, the lower bound from the two largest absolute coefficients, the finite upper bound with the common coefficient divisor, and the exact bilinear limit for every choice of nonzero signed coefficients. [Lean scope and receipt](../results/nathanson-sidon-systems/FORMALIZATION.md).

## Fiscus–Hurlbert–Myzelev–Pence grid conjecture

Run `python3 results/fiscus-grid-game/verify_strategy.py` and `python3 results/fiscus-grid-game/check_minimax.py`. The first check replays the published response table; the other independently computes all 16,384 position values. [Proof](../results/fiscus-grid-game/PROOF.md) · [Scope and audit](../results/fiscus-grid-game/AUDIT.md). No Lean proof is claimed.

Lean proves that Player 1 wins on the 14-vertex ladder, verifies all 16,384 positions and identifies all four winning openings. [Theorems and receipt](../results/fiscus-grid-game/FORMALIZATION.md).

## Erdős–Gyárfás point-degree spectrum conjecture

Run `python3 results/erdos-gyarfas-point-degree-spectrum/verify.py` to generate all 8,778 labelled nontrivial linear spaces on three through seven points and reconstruct their degrees from the lines. The checker also tests the central two-set inequality on 10,315 selections. A separate researcher checked every step of the all-order proof and independently tested 50,926 selections. [Proof](../results/erdos-gyarfas-point-degree-spectrum/PROOF.md) · [Review and search record](../results/erdos-gyarfas-point-degree-spectrum/AUDIT.md).

Lean bounds the degree spectrum in every finite linear space, rules out the proposed square-root deficit and proves the same linear bound for real planar point sets. [Theorems and receipt](../results/erdos-gyarfas-point-degree-spectrum/FORMALIZATION.md).

## Zeng’s unscaled interlacing question

Run `python3 results/zeng-unscaled-interlacing/check.py`. The checker runs 224 exact signed remainder chains and 1,120 identities on rational parameters. The independent review also certified 176 indexed comparisons by root isolation. [Proof](../results/zeng-unscaled-interlacing/proof.md) · [Independent review](https://github.com/1337isnot1337/solved-conjectures/issues/792#issuecomment-7192093300)

## Alexandersson’s transportation polytope conjecture

Run `python3 results/alexandersson-transportation/check.py`. The checker reconstructs 25 Ehrhart counts directly from the transportation constraints and verifies the Laguerre violation and the exact real-root count by rational arithmetic. [Proof](../results/alexandersson-transportation/proof.md) · [Independent review](https://github.com/1337isnot1337/solved-conjectures/issues/814#issuecomment-7192093350) Lean proves the full-support counterexample and the square-root-logarithmic growth of nonreal roots, counted with multiplicity, for the Ehrhart numerators of the actual lattice polytopes. [Lean theorems and verification receipt](../results/alexandersson-transportation/FORMALIZATION.md). Run `python3 results/alexandersson-transportation/check_growth.py` for the Rodrigues, energy and Sturm checks.

## Wang–Yang's Fuss–Narayana conjecture

Run `python3 results/wang-yang-fuss-narayana/check.py`. The verifier checks all 82,344 minors of the six leading order-seven matrices at four parameters and 3,168 identities against the published entries. The [proof](../results/wang-yang-fuss-narayana/proof.md) covers arbitrary minors and integer parameters at least two.

The pinned strict source build, all-owned transitive axiom audit (322 declarations, 270 theorems), and stock-kernel replay passed for the exact five-module Lean closure proving all six matrices of Conjecture 4.1 for every integer parameter `m ≥ 2`. The aggregate repository gate is separate. [Lean scope and receipt](../results/wang-yang-fuss-narayana/FORMALIZATION.md).

## Gyárfás’s planar degree-repetition problem

The proof counts secants by their intercepts for every order at least 16. Run `python3 results/gyarfas-planar-degree-repetition/verify.py` to count actual incident lines at 116 sample orders using normalized integer line equations. A separate researcher checked the proof and independently enumerated the orders 16 through 160. [Proof](../results/gyarfas-planar-degree-repetition/PROOF.md) · [Review and search record](../results/gyarfas-planar-degree-repetition/AUDIT.md).

For every order from 16, Lean constructs noncollinear rational points in the real plane, proves optimal maximum degree multiplicity two and determines the entire interval of distinct degrees. [Theorems and receipts](../results/gyarfas-planar-degree-repetition/FORMALIZATION.md).

## The two truncated-square covering examples

Lean proves the exact Lebesgue areas and maximal four-shape covering scales of the parallelogram and rational pentagon, and the strict comparisons with the source’s trapezoid formula. The first comparison also holds near the boundary for every first truncation leg. Identifying this scale with symplectic capacity and proving the full strict bound for every convex body remain open in Lean. [Proof and receipt](../results/meylender-thalmaier-truncated-square/FORMALIZATION.md).

## Upper-half circular chromatic index examples in every degree from eight

For every integer maximum degree from eight, Lean constructs a finite simple graph whose real circular chromatic index is strictly between that degree plus one half and that degree plus one. The proof combines the two insertion families, regular circulants and tomdif’s seven exceptional examples. The three-block theorem gives the degree of every labelled vertex for every permitted packing. [Full theorem and verification](../results/circular-index-upper-half-remaining-deltas/FORMALIZATION.md).

## Ferroni–Pagaria–Vecchi’s type B real-rootedness conjecture

Run `python3 results/ferroni-pagaria-vecchi-type-b/verify.py` to check 132 rational source-series comparisons and 352 exact cancellation and coefficient-sign identities. The [all-rank proof](../results/ferroni-pagaria-vecchi-type-b/PROOF.md) uses Descartes' rule and a weighted Rolle argument; it does not use the finite checks. [Source and audit](../results/ferroni-pagaria-vecchi-type-b/AUDIT.md). No Lean verification is claimed.

## The seventeen nonregular graphs of the circulant construction

Lean verifies the maximum degree and the exact real circular chromatic index for every nonregular graph in Section 7.3. An independent table comparison matches all 19,649 edge colours to the original certificates. The two standard replays each checked 27 project modules, 455 declarations, 327 theorem declarations, 70 private declarations and all 17 required endpoints. [Proof and original data](../results/circular-index-upper-half-circulants/FORMALIZATION.md).

## The plane-partition polynomial inequalities

Lean proves the strict Turán inequality for every index at least 12 and every real parameter at least 1. The consecutive roots strictly decrease from index 1 when the parameter exceeds 5 and from index 6 when it is at least 1. [Scope and reproduction](../results/heim-neuhauser-troeger-plane-partition-turan/FORMALIZATION.md).

## Upper-half circular chromatic index in every even degree from eight

For every integer parameter of at least six, Lean constructs both simple graphs with the prescribed order, maximum degree and exact circular chromatic index. It proves the four finite cases of Proposition 2 and the three degree ranges of Corollary 3. Lean also proves that the stated two-matching base has no solution at parameters three, four and five. [Theorems, source data and verification](../results/circular-index-upper-half-delta-2-mod-4/FORMALIZATION.md).

## Finite circular chromatic index certificates

Lean checks 43 finite simple graphs from the published colouring records. All 32 complete graphs with deletions have rigorous density and colouring bounds. Eleven insertion graphs have exact circular index equal to the maximum degree plus two thirds. [Colourings, checks and receipt](../results/circular-index-complete-minus-edges/FORMALIZATION.md).


## Cyrusian–Kaplan’s ordinarization quasipolynomial question

Complete for both written conclusions. The literal count has exact degree `2r` in every residue on all positive genera, and it is eventually strictly increasing for each fixed positive ordinarization number. The exact scoped check includes strict compilation, the complete owned axiom audit, and pinned stock-kernel replay. The stronger all-genus monotonicity conjecture is not asserted. [Scope and receipt](../results/cyrusian-kaplan-ordinarization/FORMALIZATION.md).

## Burstein’s A218225 enumeration conjecture

The pinned strict source build, all-owned transitive axiom audit (815 declarations, 719 theorems), and stock kernel replay passed for the exact six-module closure. The aggregate repository gate is separate. [Lean scope and receipt](../results/burstein-a218225-enumeration/FORMALIZATION.md).


## Pomerance–Sárközy’s fluctuation conjecture

With the pinned Lean toolchain and Mathlib installed, run the target
check from the repository root. It builds the exact import closure with
warnings as errors, audits all its owned declarations, and replays it
with the stock kernel checker. The aggregate workflow includes the
same endpoint module and requires both declarations.
[Exact replay receipt](../results/pomerance-sarkozy-fluctuations/verification/source-fluctuations/receipt.json) · [Lean scope](../results/pomerance-sarkozy-fluctuations/FORMALIZATION.md#headline-arithmetic-limits) · [Aggregate workflow](../.github/workflows/lean.yml).

```bash
python3 scripts/verify_lean_target.py \
  --root Conjectures.PomeranceSarkozySourceFluctuations \
  --require PomeranceSarkozy.source_arithmetic_quarter_gaussian \
  --require PomeranceSarkozy.source_sqrt_converges_in_probability \
  --out /tmp/pomerance-sarkozy-source-fluctuations
```


## Novelli–Thibon's conjecture

Partial. Lean checks the finite commutative monomial product and
actual Jacobi–Trudi/bialternant bridge. The hook coefficients follow
from an explicit stable ordinary Schur expansion; the existence
and stability of that expansion remain outside the check.
[Lean scope and receipt](../results/novelli-thibon/FORMALIZATION.md).

## Gamma moments, log-concavity and real zeros for weighted complete graphs

Complete for the stated equal-variable result. Lean verifies the
literal Laguerre and actual Gamma expectation formulas, the boundary
color formulas, strict ordinary coefficient log-concavity, and the
real-zero count. Schur-log-concavity is outside the stated result.
[Lean scope and receipt](../docs/weighted-complete-graph-moments/FORMALIZATION.md).

## Defant–Engen–Miller’s Lassalle refinement conjecture

Partial. Lean checks the exact 205-box coverage, the 53 base rows,
the Bessel root bracket, and the approximation estimate. The exact
conjecture remains conditional on the original permutation-count bridge
and classical Bessel product data.
[Lean scope and receipt](../results/defant-engen-miller-lassalle/FORMALIZATION.md).

## Sobolewski–Ulas’s binary-partition exception regularity conjecture

Partial. Lean proves exact binary-partition congruences for all inputs, inclusion of the explicit layers in the original exception set, and the layer nonregularity in power-of-two bases. For actual nonregularity, Legendre’s sufficiency direction remains external, together with the Cobham–Durand implication for other bases. [Lean scope and receipt](../results/sobolewski-ulas-exception-regularity/FORMALIZATION.md).

## McNamara–Steingrímsson’s interval rank-unimodality conjecture

Complete for Conjecture 9.4. Lean proves that the actual repeated-sum interval has three consecutive rank sizes 8,598,793,292,661, 8,598,464,986,146 and 8,599,053,474,845. The strict dip refutes rank-unimodality of all classical permutation pattern intervals. [Lean proof and receipt](../results/mcnamara-steingrimsson-rank-unimodality/FORMALIZATION.md).

## Athanasiadis–Chapoton’s polar preorder duality conjecture

The [scoped Lean receipt](../results/athanasiadis-chapoton-polar-duality/verification/receipt.json) records strict compilation, the all-owned axiom audit, and stock-kernel replay of the four-module closure. The original exact Python checker also passed. [Lean scope](../results/athanasiadis-chapoton-polar-duality/FORMALIZATION.md)

## Heim–Neuhauser’s ordinary D’Arcais root conjecture

The [finite and central-integral receipt](../results/heim-neuhauser-ordinary-darcais-root/verification/receipt.json) and [ordinary Fourier receipt](../results/heim-neuhauser-ordinary-darcais-root/verification/fourier-receipt.json) record strict compilation, the axiom audit and stock-kernel replay of their respective proof modules. The exact small-index, GMP, and rational Fourier checkers also replayed successfully. [Lean scope](../results/heim-neuhauser-ordinary-darcais-root/FORMALIZATION.md)

## Rossi’s permutohedron characteristic-polynomial conjecture

The complete stock-kernel checked closure proves the exact finite and analytic sign grids and positivity, simplicity and interval counts for Rossi’s signed characteristic face sum. The literal ordered-face rank enumerator proves the paper’s equivalent conjecture without a Möbius assumption. [Scope and full receipt](../results/rossi-permutohedron-roots/FORMALIZATION.md).


## Shumyatsky’s conjugate prime-spectrum conjecture

The [Lean scope and receipts](../results/shumyatsky-conjugate-prime-spectrum/FORMALIZATION.md) record strict compilation, all-owned axiom audits, and stock-kernel replay for the prime-spectrum reduction, automorphisms of the actual simple-factor product, cyclic gluing, the indexed cycle partition, independent closed-word labels, the conditional multifactor lift, the simultaneous factor adjustments, the abelian reduction, the cyclic quotient normalization, the direct-product structure of the nonabelian socle, the transitive simple factors of each constituent, the Hall and coprime-complement steps, the conditional single-factor lift on the socle quotient, Gaschütz’s finite lifting lemma, the actual factor action of the socle quotient, and the exact conjecture under four explicit finite-simple-group inputs. The [audit](../results/shumyatsky-conjugate-prime-spectrum/AUDIT.md) retains the written review and source credits.


## McNamara–Steingrímsson’s interval rank-unimodality conjecture

Run `python3 results/mcnamara-steingrimsson-rank-unimodality/verify.py` from the repository root. The standard-library checker counts the relevant layered patterns using binomial sums and reproduces the strict dip at relative ranks 44–46. The [proof](../results/mcnamara-steingrimsson-rank-unimodality/PROOF.md) establishes that these coefficients count distinct patterns in the interval.

## Xu–Zhou’s diameter–Laplacian conjecture

The [original bound receipt](../results/xu-zhou-laplacian-diameter/verification/receipt.json) and [combined sharpness receipt](../results/xu-zhou-laplacian-diameter/verification/sharpness/receipt.json) record strict compilation, the all-owned axiom audit, and stock-kernel replay for the full literal Laplacian and diameter argument and the family attaining the bound for every `c ≥ 0`. [Statement scope](../results/xu-zhou-laplacian-diameter/FORMALIZATION.md).

## Higashitani–Kummer–Michałek conjecture

The [local receipt](../results/hkm-ehrhart/verification/receipt.json) covers strict compilation, the all-owned axiom audit and stock replay for the `Conjectures.HKMEhrhartDegreeBridge` closure. It includes exact lattice membership, polynomial counting at every dilation, the degree bound, uniqueness, and the off-line root of the literal Ehrhart polynomial. [Lean scope](../results/hkm-ehrhart/FORMALIZATION.md).

## Ferreira–Simon’s diagonal Mittag–Leffler conjecture

The [local receipt](../results/ferreira-simon-diagonal/verification/receipt.json) records the strict build, all-owned axiom audit, and stock-kernel replay of the one-module closure of `Conjectures.FerreiraSimonDiagonal`. The checked scope is partial. [Lean scope](../results/ferreira-simon-diagonal/FORMALIZATION.md).

## Revised Tan–Zhou conjecture

The [local receipt](../results/revised-tan-zhou-luroth/verification/receipt.json) covers the strict build, transitive owned-declaration audit, and stock-kernel replay of the eleven-module closure of `Conjectures.RevisedTanZhou`. The [Lean formalization](../results/revised-tan-zhou-luroth/FORMALIZATION.md) gives the scoped command. The new modules and endpoints are registered in the [aggregate workflow](../.github/workflows/lean.yml).


## Nuttall's conjecture

The complete [scoped receipt](../results/nuttall-cumulants/verification/full/receipt.json) records strict compilation, transitive all-owned axiom verification, and stock-kernel replay of the twenty-module closure. It checks the exact least-order conjecture and the eventual sign-reverse regularity of the literal kernel. The aggregate repository gate is separate. [Lean scope](../results/nuttall-cumulants/FORMALIZATION.md).

## Németh–Seberry–Shu conjecture

Separate target receipts cover the strict builds, full owned-axiom audits, and stock replays for the spectral and counting closures. This does not certify the aggregate repository gate. [Lean scope](../results/nemeth-seberry-shu/FORMALIZATION.md).

## Burstein’s descent-top shape-Wilf conjecture

The pinned strict source build, all-owned transitive axiom audit, and stock kernel replay passed for the exact one-module closure. The aggregate repository gate is separate. [Lean scope](../results/burstein-descent-top-shape-wilf/FORMALIZATION.md).

## Benfield–Lippard’s stable Waring-gap parity conjecture

The pinned strict source build, all-owned transitive axiom audit, and stock kernel replay passed for the exact one-module closure. The aggregate repository gate is separate. [Lean scope](../results/benfield-lippard-waring-gap-parity/FORMALIZATION.md).

## Cardon–Forgács–Piotrowski–Sorensen–White conjecture

The unchanged original proof and two extension modules passed pinned strict Lean, all-owned transitive axiom audit (68 declarations, nine endpoints) and stock kernel replay. [Exact scope](../results/cardon-zero-sector/LEAN.md). Aggregate CI is separate.

## Ćurgus–Mascioni’s Fréchet root-matching extremizer question

[Scoped checks](../results/curgus-mascioni-frechet/FORMALIZATION.md) for the nonuniqueness counterexample passed: pinned strict compilation, all-owned transitive axiom audit and stock kernel replay. Aggregate CI is separate.

## Ferroni–Morales–Panova’s cylindric Ehrhart-positivity conjecture

[Scoped checks](../results/fmp-cylindric/FORMALIZATION.md) for the exact unpinned counterexamples passed: pinned strict compilation, an all-owned transitive axiom audit, and stock kernel replay. This does not assert an aggregate CI pass.

## Csordas–Vishnyakova conjecture

The exact source of `Conjectures.CsordasVishnyakova` passed pinned strict compilation, all-owned transitive axiom audit and stock replay. [Lean scope](../results/csordas-vishnyakova/FORMALIZATION.md) includes the focused reproduction command and [Exact receipt](../results/csordas-vishnyakova/verification/lean-receipt.json) gives the source digest. The repository-wide aggregate gate is separate.

## Ma–Tang’s random subset-sum threshold conjecture

The exact 32-module closure was strict-built and stock-replayed with pinned Lean 4.35.0; the complete transitive axiom gate checked 1,514 declarations and 31 explicit endpoints. The aggregate repository run is separate. [Lean scope](../results/ma-tang-random-subset-sums/FORMALIZATION.md) includes the scoped reproducible command; see the [Exact receipt](../results/ma-tang-random-subset-sums/verification/limsup-receipt.json).

## Gravgaard–Lee’s Lüroth diameter question

The [local receipt](../results/gravgaard-lee-diameter-condition/verification/receipt.json) covers strict compilation, all-owned transitive axiom audit, and pinned stock-kernel replay for the closure of `Conjectures.GravgaardLeeDiameter`. See the [Lean formalization](../results/gravgaard-lee-diameter-condition/FORMALIZATION.md) for the scoped command. The imports and required endpoints are registered in the [aggregate workflow](../.github/workflows/lean.yml).

## Ulas’s disjoint-block square-product conjecture

The [local receipt](../results/ulas-disjoint-square-blocks/verification/receipt.json) records the strict Lean build, transitive axiom audit, and stock-kernel replay for the nine-module closure of `Conjectures.UlasDisjointSquareBlocks`. The [Lean formalization](../results/ulas-disjoint-square-blocks/FORMALIZATION.md) gives the scoped command. The [aggregate workflow](../.github/workflows/lean.yml) uses the registered imports, audit endpoints, and replay list.


## Feldheim–Feldheim’s weighted tail conjecture

From `lean/`, run `lake env python3 ../scripts/verify_feldheim_weighted_tail.py`. The [dedicated workflow](../.github/workflows/lean-feldheim-weighted-tail.yml) runs the same fresh strict source builds, complete all-owned/private transitive axiom audit and exact stock-kernel replay for the registered twenty-module closure. The [proof-lane receipt](../results/feldheim-weighted-tail/verification/lane/receipt.json) and [independent final validation](../results/feldheim-weighted-tail/verification/FINAL_INDEPENDENT_VALIDATION.json) cover 179 declarations, 161 theorems and all thirty required endpoints. The [publication receipt](../results/feldheim-weighted-tail/verification/receipt.json) checks the portable runner and current registrations separately. [Scope and reviews](../results/feldheim-weighted-tail/LEAN_REVIEW.md) retain all laws and all positive weights; higher-dimensional norm and finite-threshold supplements are unformalized. Aggregate verification and current-mode public deployment remain separate obligations in [#563](https://github.com/1337isnot1337/solved-conjectures/issues/563).

## Hajdu–Sárközy’s shifted-product total primitivity conjecture

From `lean/`, run `lake env python3 ../scripts/verify_hajdu_sarkozy_products.py`. The [dedicated workflow](../.github/workflows/lean-hajdu-sarkozy-shifted-products.yml) runs the same full strict source builds, all-owned/private transitive axiom audit, and exact stock-kernel replay. The [frozen proof receipt](../results/hajdu-sarkozy-shifted-products/verification/receipt.json) covers all twenty-four modules and fifty-three required endpoints. The [publication binding](../results/hajdu-sarkozy-shifted-products/verification/publication-binding.json) separately validates unchanged proof sources, the exact local closure, registrations, and the pinned checker; it does not claim an additional rebuild. [Scope and independent review](../results/hajdu-sarkozy-shifted-products/FORMALIZATION.md) distinguish the complete original/summable-family/two-variable results from the optional more-than-two-variable supplement. Aggregate verification and current-mode public deployment are separate obligations in [#563](https://github.com/1337isnot1337/solved-conjectures/issues/563).

## Gawron–Miska–Ulas’s Thue–Morse sign-density conjecture

The three-module source closure of `Conjectures.ThueMorseSignDensity` passed strict compilation, all-owned axiom audit (250 declarations, 212 theorems, 119 private declarations, 27 required endpoints), and independent stock-kernel replay at `471a5984bb7bd0936cf1b78bc1827ca1d8ff68e2`. The [result-level receipt](../results/gawron-miska-ulas-thue-morse-sign-density/LEAN.md) records exact hashes and the original conjecture scope. Reproduce using `python3 scripts/verify_lean_target.py --root Conjectures.ThueMorseSignDensity --require ThueMorseSignDensity.conjecture_false --require ThueMorseSignDensity.both_counterexamples --out .candidate-artifacts/thue-morse-sign-density`. Package-wide verification is separate.

## Ferroni–Higashitani’s first-three interior Ehrhart question

The [scoped receipt](verification/lean-ferroni-higashitani-complete-20261124/receipt.json) covers the full `Conjectures.FerroniHigashitaniEhrhart` closure, including the closed and interior counts, the polynomial reflection identity, and the original inequality. Run `python3 scripts/verify_lean_target.py --root Conjectures.FerroniHigashitaniEhrhart --require FerroniHigashitani.question_5_12a --out /tmp/ferroni-lean` from the repository root with pinned Lean and Mathlib installed. The [aggregate workflow](../.github/workflows/lean.yml) uses the updated imports, audit endpoints, and replay registry. The exact Python checker remains a supplementary independent computation.

## Gravgaard–Lee’s mixed upper/lower Lüroth conjecture

Complete for original Conjecture 2.6 and the stronger exact interval equality, for every k≥2. Lean constructs actual infinite expansions, proves the finite zero-tail repair, and includes the threshold-two boundary. The [scope report](../results/gravgaard-lee-upper-lower-luroth/FORMALIZATION.md) and [independent review](../results/gravgaard-lee-upper-lower-luroth/LEAN_REVIEW.md) record the correspondence. The [complete receipt](verification/lean-gravgaard-lee-upper-lower-complete-20261124-162051/receipt.json) covers 12 strict source builds, 664 declarations, 475 theorems, 173 private declarations, 29 required endpoints, and exact stock replay. Only the three allowed standard axioms occur. Aggregate verification and public deployment remain separate in [#563](https://github.com/1337isnot1337/solved-conjectures/issues/563). The two reused previously completed Lüroth modules are not recounted. The mixed bounded-digit dependency retains its original proof already published through [PR #547](https://github.com/1337isnot1337/solved-conjectures/pull/547).

Reproduce the isolated closure with `cd lean && lake env python3 ../scripts/verify_gravgaard_lee_upper_lower.py`. The protected aggregate attempt is preserved with its failed dependency-cache result; it does not assert an aggregate pass.

## Steinerberger’s greedy-energy Fourier conjecture

The [publication receipt](../results/steinerberger-greedy-fourier/verification/receipt.json) records the exact four-module closure: fresh strict source builds, the all-owned/private audit of 113 declarations and all 15 required endpoints, and unchanged stock-kernel replay. The only allowed transitive axioms are `propext`, `Classical.choice`, and `Quot.sound`. The [independent review](../results/steinerberger-greedy-fourier/LEAN_REVIEW.md) separately audits the original conjecture and full counterexample.

With the pinned Lean and Mathlib dependencies installed, reproduce the scoped check from `lean/`:

```sh
lake env python3 ../scripts/verify_steinerberger_greedy.py
```

The [dedicated workflow](../.github/workflows/lean-steinerberger-greedy.yml) uses that same runner on proof, registration, toolchain and verifier changes. The [original lane receipt](../results/steinerberger-greedy-fourier/verification/lane/receipt.json) preserves its three unsuccessful replay attempts and the subsequent passing single-thread replay. The publication receipt is a fresh check of the registered candidate. It does not claim the aggregate repository gate or a public-site deployment has passed; those obligations are tracked in [issue #563](https://github.com/1337isnot1337/solved-conjectures/issues/563).



## Coulangeon–Lazzarini’s two-shell counterexample

The [scoped receipt](verification/lean-coulangeon-lazzarini-20261124/receipt.json)
records strict compilation, the all-owned axiom audit and pinned replay
for the integer shell theorem and its full-rank real lattice realization.
The registered endpoints include first-shell order, moment equivalence and
the dimension-ten refutation.

## Gravgaard–Lee’s mixed Lüroth sumset

The [scoped receipt](verification/lean-gravgaard-lee-mixed-luroth-20261124/receipt.json)
records strict compilation, an all-owned axiom audit and pinned kernel replay
for both modules in the local closure. The source intervals and every real
residue are covered by the registered endpoints.

## Gravgaard–Lee’s large-digit Lüroth sumset

The [scoped receipt](verification/lean-gravgaard-lee-large-luroth-20261124/receipt.json)
records strict compilation, the all-owned axiom audit and stock-kernel replay
for `Conjectures.GravgaardLeeLargeLuroth`. The registered endpoints cover the
source series, the witness expansions and Conjecture 2.12.

## Gessel–Zhuang’s pinnacle-set gamma-positivity conjecture

The [complete closure receipt](verification/gessel-zhuang-20261124/receipt.json), finished 24 November 2026 at 17:30:16 UTC, records fresh strict compilation of 25 project modules, the unchanged audit of 641 declarations (479 theorems and 185 private declarations), all 17 required endpoints, and full stock-kernel replay. Only `propext`, `Classical.choice`, and `Quot.sound` occur transitively. The dedicated workflow repeats the target gate. The exact finite path checker passed through size nine and is supplementary. The repository-wide gate remains separately blocked by the documented dependency-cache problem; neither hosted success nor deployment is inferred from this target receipt.

## Hajdu–Sárközy’s shifted-power perturbation conjecture

From `lean/`, run `lake env python3 ../scripts/verify_hajdu_sarkozy.py`. The [dedicated workflow](../.github/workflows/lean-hajdu-sarkozy-shifted-power.yml) performs the same strict source builds, complete all-owned/private axiom audit, and exact stock-kernel replay. The [publication receipt](../results/hajdu-sarkozy-shifted-power-perturbations/verification/receipt.json) binds all eleven sources and their controls, objects, logs, and declaration inventory. The complete original and general-shift scope, optional unformalized supplement, [independent review](../results/hajdu-sarkozy-shifted-power-perturbations/LEAN_REVIEW.md), original lane receipt, and interrupted-run evidence are retained in the existing entry. The aggregate package gate and hosted deployment remain separate checks.

## An exact power-rank formula for a rank-six recurrence

The [complete closure receipt](verification/rowland-20261124/receipt.json), finished 24 November 2026 at 17:09:57 UTC, records 17 fresh strict module builds, the unchanged audit of 286 owned declarations (261 theorems and five private declarations), 11 required endpoints, and complete stock-kernel replay. The only transitive axioms are `propext`, `Classical.choice`, and `Quot.sound`. The `lean-rowland-sistos-barron.yml` workflow reproduces the target gate. The whole-repository gate and hosted deployment remain separate. The [exact supplemental checker](verification/rowland-20261124/supplementary-check.json) was rerun through exponent 180 and supplies no assumption to the unbounded proof.

## Johnson's conjecture

The [complete closure receipt](verification/johnson-20261124/receipt.json), finished 24 November 2026 at 17:06:28 UTC, records thirty fresh strict module compilations, the unchanged audit of all 1,195 owned declarations (1,006 theorems and 28 private declarations), eight required endpoints, and unchanged stock-kernel replay. It checks the full finite-tuple source statement and the general circular-product theorem. Only `propext`, `Classical.choice`, and `Quot.sound` are permitted.

The `lean-johnson.yml` workflow reproduces this target check. The target receipt does not assert the repository-wide gate for unrelated entries; hosted and aggregate results remain separate. The existing Python checker is a supplementary diagnostic, not a proof premise.

## Caiolo–Ferroni–Hoster counterexample family

Run the following from `lean/` with its pinned toolchain. The replay checks the
complete local import closure for the all-prime-powers theorem. The standard
`scripts/verify_lean.sh` package gate also includes these modules.

```sh
lake build Conjectures.CaioloFerroniHoster
lake env python3 ../scripts/replay_lean.py --root Conjectures.CaioloFerroniHoster
lake build Conjectures.CaioloFerroniHosterRanks
lake env python3 ../scripts/replay_lean.py --root Conjectures.CaioloFerroniHosterRanks
```

[Source correspondence and axiom audit](../results/caiolo-ferroni-hoster/LEAN_REVIEW.md)

## Juhnke’s arbitrary-step lattice-path log-concavity conjecture

The [complete target receipt](verification/juhnke-20261124/receipt.json) records fresh strict compilation of all 18 project modules, the unchanged audit of all 577 owned declarations (502 theorems and 11 required endpoints), and unchanged stock-kernel replay. The pinned Lean version is 4.35.0; the only allowed transitive axioms are `propext`, `Classical.choice`, and `Quot.sound`. The complete source statement and literal-path bridge were independently reviewed against the original report.

The dedicated `lean-juhnke.yml` workflow reproduces the target check with `scripts/verify_lean_target.py`. Its target receipt does not claim repository-wide verification of unrelated entries. The existing exact diagnostic checker also passed dimensions 3 through 62; the Lean theorem has unbounded dimension and step-count parameters.

## Steinerberger’s quantitative Feldheim-tail conjecture

The [complete Lean disproof](../results/steinerberger-feldheim-tail/LEAN-AUDIT.md)
constructs the probability law with survival function exp(−x−x²/200), identifies
its actual mean and median, and bounds the ratio of the original product-space
events for every positive threshold. Both original existence claims fail.
The four-module closure passed strict compilation, the audit of all 103 owned
declarations (92 theorems and six required endpoints), and stock-kernel replay.
The integrator checked the statement against both original primary sources.
The smoothing, all-epsilon family, strict log-concavity, and rate supplements
remain unformalized. This is one completed existing conjecture entry.

## Complex BSS separation research

[Research receipts and replay instructions](https://github.com/1337isnot1337/solved-conjectures/blob/research/docs/verification.md#complex-bss-separation-research). Check out `research` before running the research scripts.

## Boolean Hamiltonicity research lemmas

[Research receipts and replay instructions](https://github.com/1337isnot1337/solved-conjectures/blob/research/docs/verification.md#boolean-hamiltonicity-research-lemmas). These checks do not resolve Boolean P versus NP.

## Weighted counting for bounded-occurrence 3-CNF (conditional research note)

[Proof scope, research receipts, and verification instructions](https://github.com/1337isnot1337/solved-conjectures/blob/research/docs/verification.md#weighted-counting-for-bounded-occurrence-3-cnf-conditional-research-note). The source theorem dependency and exclusion from solved-conjecture counts are unchanged.

## Steinke–Zakynthinou’s agnostic VC learning conjecture

The same workflow checks the [measurable local reconstruction theorem](../lean/Conjectures/AgnosticVC/LocalReconstructionMeasurable.lean), including the [iid rates for the circle-orbit class](../lean/Conjectures/AgnosticVC/OrbitIidRates.lean).

The [dedicated GitHub Actions workflow](https://github.com/1337isnot1337/solved-conjectures/actions/workflows/lean-agnostic-vc.yml) runs on proof and verifier changes pushed to or proposed against `main`. To reproduce it locally, run `python3 scripts/verify_agnostic_vc.py --fetch-cache` from the repository root with the pinned toolchain on PATH. The command builds the [combined theorem](../lean/Conjectures/AgnosticVC/Theorem.lean) and the [fixed-pairing theorem](../lean/Conjectures/AgnosticVC/FixedPairing.lean), elaborates the full project import closure with warnings as errors, checks the transitive axioms of its declarations and replays the compiled objects with the pinned Lean checker. The [receipt](../results/steinke-zakynthinou-agnostic-vc/verification.json) records the checks. The [proof supplement](../results/steinke-zakynthinou-agnostic-vc/PROOF.md#4-information-in-the-returned-hypothesis) gives the fixed-pairing argument. The [manuscript](../results/steinke-zakynthinou-agnostic-vc/paper.pdf) gives the original proof and its Lean correspondence. Section 6 proves two obstructions to Borel measurability. Their Lean counterparts are included in the same verification workflow.

## Steinke–Zakynthinou threshold proof

Lean verifies the proper real-threshold case with a Borel output kernel, an information bound of 300 nats using Mathlib KL, and an empirical bound against the full source class, including the threshold at infinity. The [review](../results/steinke-zakynthinou-thresholds/LEAN_REVIEW.md) identifies the exact mathematical and formal statements. The [receipt](../results/steinke-zakynthinou-thresholds/verification.json) distinguishes the kernel replay from the supplementary finite checks. The private-tag constants and the efficient and deterministic variants have separate written proofs.

Gröchenig’s upper-density result is excluded after a [checked earlier resolution](https://github.com/1337isnot1337/solved-conjectures/tree/research/research/bounty-continuation-2026-11-21/grochenig-prior-resolution/). Its independent proof and verification receipts remain in [immutable Git history](https://github.com/1337isnot1337/solved-conjectures/blob/628270dc5e07d7924de265d2ac1beee4b5634b80/docs/verification/lean-grochenig-20261121/receipt.json). The reused KVZ results remain active.

[Home](../README.md) · [Catalogue](../CONTENTS.md) · [Lean status](lean-status.md)

## Chen–Khare–Sahi stable Hall local verification

The twelve new modules and seven reused semiring modules form an exact
nineteen-module closure. All nineteen sources passed strict compilation.
The unchanged modern owned/private audit covers eleven modules; the
unchanged complete audit covers 1,489 declarations, 1,294 theorem declarations, 950 private declarations and all 42 required endpoints. Only `propext`,
`Classical.choice` and `Quot.sound` occur. Stock-kernel replay passed for
this exact frozen nineteen-module closure, including all 41 object parts.
The combined repository gate and hosted validation remain separate pending
checks.

The receipt preserves all source commands, raw strict logs and process metrics,
both current raw audit logs and their revalidated inventories, and the complete
stock-replay log. The frozen inventory includes nineteen sources, 33 modern
object parts and eight legacy public objects, the unchanged verification
helpers, pins, generated audits, gate runner and checker binaries. Legacy
private/server facets are required to be absent.

The ten earlier modern helper records contain source and all output-object
hashes plus imported-object hashes. They do not contain historical compiler,
control or dependency-source hashes; those are not invented. The fresh seven
legacy records and the two final single-module receipts include their recorded
pre/post source, dependency and control checks. The full gate independently
freezes and rechecks the complete current source/object closure.

The earlier sixteen-module compatibility receipt remains a separate
checkpoint. Its strict sources and owned/private audit passed, but its
fresh stock replay remains pending. This nineteen-module replay shares
only seven modules with that closure and does not certify its other nine
modules.

See the [stable-Hall receipt](verification/lean-cks-hall-20261121/receipt.json).

## KVZ complete local verification

The full gamma-quotient theorem has an exact 15-module closure. The [receipt](verification/lean-kvz-20261121/receipt.json)
records all strict source commands, frozen source and object hashes, the
complete owned/private audit, and stock-kernel replay. All 62 required
endpoints passed. The mathematical scope includes arbitrary real translated
node grids, every determinant order, the positive-integer cutoff, and the
parameter-dependent signature.

Historical Wronskian strict receipts are accompanied by a separately dated
post-build frozen inventory; unavailable pre-build hashes are not claimed.
Other historical records retain their actual source/public-object hash
coverage. The convolution records identify their source, direct dependencies,
and every object part. The complete gate freezes and replays all 45 object
parts. No source-only refresh is relabeled as an object rebuild.

The combined repository gate and hosted verification of this checkpoint
remain separate pending checks.

## Chen–Khare–Sahi compatibility checkpoint

All 16 existing modules passed fresh strict Lean 4.35 compilation with warnings treated as errors. The complete owned/private audit checked 1,454 declarations, including 1,254 theorem declarations, 816 private declarations and all 49 required endpoints. Only `propext`, `Classical.choice` and `Quot.sound` are allowed. Independent stock-kernel replay of the revised closure and the combined repository gate remain pending. The README badge remains partial.

[Receipt](verification/lean-cks-compatibility-20261121/receipt.json) and [complete owned audit](verification/lean-cks-compatibility-20261121/audit.log). The current endpoints use the standard monic triangular Macdonald eigenfunctions. Stable Hall orthogonality followed by specialization is being formalized separately. The manuscript's literal truncated finite-variable Hall pairing conflicts with that convention; the [degree-three diagnostic](https://github.com/1337isnot1337/solved-conjectures/issues/201#issuecomment-7065320695) must be reconciled before claiming a full literal-source formalization.

## Chow complete local verification

The unweighted strict strengthening and its weak initial case have a checked 11-module closure. The positive-parameter extension remains written only.
The [receipt](verification/lean-chow-20261121/receipt.json) records every strict
source command, all source and object hashes, the complete owned/private
axiom audit, and exact stock-kernel replay. All 48 required endpoints passed.
The source bridge uses actual signed permutations and their descent statistic.
The combined repository gate and hosted verification remain separate.

## Oravcová–Soták local verification checkpoint

All nine new modules passed strict compilation with warnings treated as errors. The exact 28-module project closure passed an all-owned audit of 1239 declarations (1084 theorem declarations and 40 required endpoints) and independent stock-kernel replay. Only `propext`, `Classical.choice`, and `Quot.sound` are permitted. The [receipt](verification/lean-named-20261121/oravcova-receipt.json) binds the exact project sources and objects, the full declaration audit and the kernel replay. [Source records](verification/lean-named-20261121/oravcova-source-evidence.json) cover every new file. The [literal data comparison](verification/lean-named-20261121/oravcova-literal-data-comparison.json) independently matches the source certificate tables. `R5`–`R8` remain explicit inputs. The combined package gate and hosted validation are separate.

## Vishnyakova complete local verification

The original sampled-sequence and weighted root-radius theorems have a
checked 17-module closure. The
[receipt](verification/lean-vishnyakova-20261121/complete-receipt.json)
records source and object hashes, strict source commands, the complete axiom
audit, and stock-kernel replay. The audit covers all 439 declarations,
including 172 private declarations and all 66 required endpoints.
The independent checker replayed the frozen objects without changes.

This checkpoint proves the complete result-level assertions. The combined
repository gate and hosted verification of this checkpoint remain separate.

## Bernardi–Morales local verification checkpoint

The 13-module closure passed strict compilation with warnings treated as errors, an all-owned audit of 269 declarations (205 theorem declarations and 23 required endpoints), and independent replay by the pinned stock kernel. Only `propext`, `Classical.choice`, and `Quot.sound` are permitted. The [receipt](verification/lean-named-20261121/bernardi-receipt.json) records exact source/object hashes and toolchain pins; [source records](verification/lean-named-20261121/bernardi-source-evidence.json) preserve all 13 strict successes; the [kernel log](verification/lean-named-20261121/bernardi-kernel.log) covers the exact local module union. The scope is the full fixed-map tree and fixed-surjection event identities, including their source semantics. The combined repository gate is not claimed by this checkpoint.

## Ekhad–Zeilberger’s most unfair bet conjecture

The partial [Lean scope](../results/ekhad-zeilberger-unfair-bet/FORMALIZATION.md) and [receipt](../results/ekhad-zeilberger-unfair-bet/verification/receipt.json) cover the exact finite overlap covariance identity and the unrestricted normalized overlap-score optimization, including equality. The asymptotic probability formula is not part of this Lean closure.

Run `python results/ekhad-zeilberger-unfair-bet/verify.py`. It compares squared asymptotic advantages by integer cross-multiplication for all unordered pairs in the listed alphabet and word-length ranges. The all-length variance bound is in the [proof](../results/ekhad-zeilberger-unfair-bet/PROOF.md).

Run `python results/ekhad-zeilberger-unfair-bet/check_full_alphabet.py` to check the full-alphabet formula independently. It enumerates 120,259 ordered-pair classes up to relabeling, checks the upper bound by integer cross-multiplication and verifies that each maximum is attained for every feasible alphabet size at lengths two through five. The [review](../results/ekhad-zeilberger-unfair-bet/REVIEW.md) covers the argument for all lengths.

## Kauers–Koutschan recurrence conjecture

The [Lean scope and receipts](../results/kauers-koutschan-recurrence/FORMALIZATION.md)
include the complete theorem for the original A189281 permutation count
and both published operators. The current import closure verifies the
signed block formula, Schur moment, final extraction and transfer of the
factorized order-thirteen recurrence to the actual count.

With SymPy 1.14 installed, run `python results/kauers-koutschan-recurrence/verify.py`. The checker substitutes the exact Schur sum into both published operators over a rational polynomial ring, verifies the initial indices separately, and compares the count with all permutations through length eight. [Proof](../results/kauers-koutschan-recurrence/PROOF.md) · [Checker](../results/kauers-koutschan-recurrence/verify.py)

## Circular-index local verification checkpoint

The main circulant theorems and C31/C33 regular examples have a checked 19-module closure. The [receipt](verification/lean-named-20261121/circular-receipt.json), [all-owned inventory](verification/lean-named-20261121/circular-all-owned-inventory.json), and [raw kernel log](verification/lean-named-20261121/circular-kernel.log) record the exact source/object hashes, compiler/checker pins, 171 required theorem endpoints, and replay of only that closure. The receipt distinguishes the individual strict source checks from the subsequent combined audit and replay. It does not attest to the complete shared-package gate or to the nonregular Section 7 certificates.

## Requirements

- Python 3.12, matching CI. The Hadamard audit uses NumPy. The Frankl window enumeration uses NumPy and SciPy. The Chow checks use SymPy 1.14.0.
- A C++20 compiler available as `c++` for distance-graph checks and the lonely-runner spectrum/equality verifiers. Some Python entry points compile and launch C++ programs themselves.
- For formal proofs: Lean and Mathlib pinned in [the shared Lean package](../lean/). Use its `lean-toolchain` and `lake-manifest.json`; do not substitute a different toolchain.

Run commands from the repository root with Python assertions enabled (do not use `python -O`). Keep the whole checkout: some verifiers reuse code in sibling result directories.

The [Hadamard order-2396 replay](../results/hadamard-2396/) compares the C++ output with the archived pairs and runs a separate Python audit.

The partial-result entries contain their replay commands for the [Frankl generator theorems](../results/frankl-generator-families/), [two-speed insertion](../results/lonely-runner-two-insertions/) and [abelian cover certificate and sharpness example](../results/erdos-gyarfas-abelian-covers/). Their current formalized scope and remaining dependencies are recorded in the [Lean status](lean-status.md).

## Analytic proofs without computation

- [Tom–Vailaya’s weighted trace conjecture](../results/tom-vailaya-weighted-trace/PROOF.md): the proof of journal Conjecture 74 is algebraic and does not use the supplementary checker. Run `python3 results/tom-vailaya-weighted-trace/verify.py` to compare independent integer evaluations from forest triples and proper multigraph colorings; see the [source audit](../results/tom-vailaya-weighted-trace/AUDIT.md) and [Lean scope and receipt](../results/tom-vailaya-weighted-trace/FORMALIZATION.md) for the finite-color closure trace, multiplication under endpoint gluing, independence of the weighted path rows, the exact weighted path column identities, symbolic color-basis invertibility, endpoint reflection, and the conditional trace comparison.

- [Nuttall's conjecture](../results/nuttall-cumulants/PROOF.md): Complete proposed proof of Conjecture 1 in §4.5: for each finite order r, every sufficiently high repeated-tail cumulant of the Riemann theta kernel is strictly reverse regular through order r on the entire nonnegative node domain. The separate RH-equivalent Toeplitz positivity problem remains unresolved. [Audit](../results/nuttall-cumulants/AUDIT.md).
- [Coffey–Smith conjecture](../results/coffey-smith/PROOF.md): Complete proposed unconditional disproof of Smith’s named conjunction: if RH holds the dyadic coefficient square mass is O(N^(-1/2) log³ N), so both proposed positive-fraction sets have density zero for 0<ε<1/4; without RH the polynomial upper bound fails. The weaker Coffey upper-bound assertion alone is not refuted. [Audit](../results/coffey-smith/AUDIT.md).
- [Merlini–Sala–Sala conjecture](../results/merlini-sala-sala/PROOF.md): Complete proposed unconditional refutation of the logarithmic and all-ε subpower growth conjecture for the tiny Li term: limsup |λtiny(n)|/n^(1/4)=∞. The authors’ weaker linear stability conjecture is not resolved. [Audit](../results/merlini-sala-sala/AUDIT.md).
- [Wang–Yang's conjecture](../results/wang-yang/PROOF.md): Complete proposed disproof of the author-manuscript Conjecture 1.10: for every fixed coefficient index, the signed forward differences of the Xi coefficients have infinitely many values of each strict sign. Final journal wording has not been checked; the adjacent logarithmic conjecture is separate. [Audit](../results/wang-yang/AUDIT.md).

The [Csordas–Vishnyakova](../results/csordas-vishnyakova/PROOF.md) counterexample uses exact entire-function identities and local-uniform-limit arguments. No computation or Lean proof is required for their written mathematics; the source and review limits are recorded in the respective publication audits.

The [Dospolova–Germanskov–Zaporozhets disproof](../results/dospolova-germanskov-zaporozhets/PROOF.md) is analytic throughout. The strict Gaussian-range argument applies to every nontrivial Gaussian-bounded compact, including bounded discontinuous processes; Vitale's published normalized intrinsic-volume limit excludes every sequence c^k/k! with positive c. Three [independent reviews](../results/dospolova-germanskov-zaporozhets/ROOT_REVIEW.md) check the separability argument, strictness and normalization. The source audit credits Vitale and Long, and actual image inspection resolved an OCR ambiguity in an earlier inequality. There is no numerical verifier or new workflow step for this proof.


The [Ferreira–Simon stochastic-order proof](../results/ferreira-simon-stochastic/PROOF.md) and [diagonal Mittag–Leffler proof](../results/ferreira-simon-diagonal/PROOF.md) establish their full real-parameter statements by integral identities and pointwise comparisons. Neither depends on numerical tests, finite enumeration or computer algebra. Their separate [stochastic audit](../results/ferreira-simon-stochastic/AUDIT.md) and [diagonal audit](../results/ferreira-simon-diagonal/AUDIT.md) reconstruct the argument and check normalization, domains, strictness and convergence. The diagonal result now has a separate partial Lean verification; the stochastic-order argument is still presented as a written proof. Source and priority review are documented separately in each package.

The [Simon stable-infimum proof](../results/simon-stable-infimum/PROOF.md) is also analytic. Its [independent audit](../results/simon-stable-infimum/AUDIT.md) verifies the source normalization, prior Mellin transform, Brownian endpoint, positivity and parameter monotonicity of the logarithmic Lévy kernels, exponential integrability and independent mean-one multiplier. Conditional Jensen gives the full convex order. There is no numerical verifier or workflow test for this argument; the [source audit](../results/simon-stable-infimum/SOURCES.md) documents priority separately.

## Johnson's analytic proof and supplementary checks

The [Johnson proof](../results/johnson-pfaffian/PROOF.md) is a finite algebraic argument valid in every even order. Its use of Johnson's published additive-interval endpoint theorem is explicit. Three [independent mathematical reviews](../results/johnson-pfaffian/ROOT_REVIEW.md) check the complement scaling, cyclic Pfaffian signs, closure under deleting adjacent pairs, uncrossing, and nonnegative mixed-difference reconstruction. The separate [priority audit](../results/johnson-pfaffian/PRIOR_AUDIT.md) compares the exact source statement and seven public archives.

```sh
python3 results/johnson-pfaffian/verify.py
```

The standard-library checker uses exact rational arithmetic for supplementary identity and indexing checks. It explicitly records that finite checks do not prove the universal assertion. No Lean formalization is claimed.

## Matching excess and plane-partition inequalities

Run `python3 results/hartke-stolee-west-yancey-matching-excess/verify.py` for an independent exact finite replay of the graph and digit calculations; the proof does not use that replay.

The [plane-partition polynomial Turán proof](../results/heim-neuhauser-troeger-plane-partition-turan/PROOF.md) and [polynomization proof](../results/heim-neuhauser-plane-partition-polynomization/PROOF.md) do use exact arithmetic certificates. Run the `heim-neuhauser-fourier-certificate.py` and `heim-neuhauser-plane-partition-check.py` programs in the Turán result directory without Python optimization. Their assertions certify the rational parameter boxes and the remaining polynomial coefficient signs, respectively.

The [ordinary D’Arcais root proof](../results/heim-neuhauser-ordinary-darcais-root/PROOF.md) uses its own rational Fourier certificate, small-index integer polynomial check, and C++ GMP check. Run all three commands in the proof, with Python assertions enabled.

The [quantitative Feldheim-tail counterexample](../results/steinerberger-feldheim-tail/PROOF.md) is analytic. It uses two elementary integral bounds and no executable certificate.

Run `python3 results/benfield-lippard-waring-gap-symmetry/check.py` for the two exact Waring-gap symmetry defects. The [parity argument](../results/benfield-lippard-waring-gap-parity/PROOF.md) and the [smaller existential Feldheim-tail inequality](../results/steinerberger-feldheim-tail/LINEAR-EXISTENCE.md) are analytic and use no executable certificate.

The [Feldheim–Feldheim weighted-tail proof](../results/feldheim-weighted-tail/PROOF.md) is analytic. Run `python3 results/burstein-descent-top-shape-wilf/check.py` for literal short Ferrers-board fiber counts; the uniform refutation is analytic and does not depend on enumeration.

Run `python3 results/rossi-permutohedron-roots/check.py` for the 8,000 exact finite signs in Rossi’s characteristic-root proof. The uniform large-index argument and [weighted finite-threshold theorem](../results/feldheim-weighted-tail/FINITE-THRESHOLD.md) are analytic.

Run the exact checkers listed in the [leaf-type](../results/chappelon-ramirez-stamate-leaf-type/), [Ehrhart](../results/ferroni-higashitani-early-interior-ehrhart/) and [pinnacle](../results/gessel-zhuang-pinnacle-gamma/) result packages. Their proofs, and the convex-log-tail rate test, are analytic.

Run `python3 results/fan-tringali-power-monoid-lengths/check.py` and `python3 results/burstein-a218225-enumeration/check.py` for the graph-gadget and generating-tree replays. The [Apéry moment threshold](../results/sokal-apery-moment-threshold/) is proved analytically. The [scoped Lean receipt](../results/sokal-apery-moment-threshold/verification/receipt.json) records strict compilation, the all-owned axiom audit, and stock-kernel replay for the six-module partial formalization. [Lean scope](../results/sokal-apery-moment-threshold/FORMALIZATION.md)

The two [shifted-power perturbation](../results/hajdu-sarkozy-shifted-power-perturbations/) and [shifted-product](../results/hajdu-sarkozy-shifted-products/) proofs, and the [distinct D’Arcais-zero theorem](../results/darcais-distinct-right-half-plane-zeros/), are analytic and have no executable dependency.

## Pantone–Bóna asymptotic equivalence

Run `python3 results/pantone-bona-asymptotic/verify.py` for literal small permutation counts and exact tableau branching comparisons. The [proof](../results/pantone-bona-asymptotic/PROOF.md) derives the leading constant analytically; finite enumeration is not part of its argument.

The separate [differential-equation certificate](../results/pantone-bona-asymptotic/ode-proof.md) checks identities of rational functions, not truncated coefficients. Run `python3 results/pantone-bona-asymptotic/certify_ode.py` with SymPy 1.14.0.

## Pantone–Bóna second-largest-terminal asymptotic

Run `python3 results/pantone-bona-second-largest-terminal/verify.py` to compare the exact canonical gap formula with literal pattern filtering. The [proof](../results/pantone-bona-second-largest-terminal/PROOF.md) derives the asymptotic equivalence without the finite enumeration.

The [scoped Lean receipt](../results/pantone-bona-second-largest-terminal/verification/receipt.json) records strict compilation, the all-owned axiom audit, and stock-kernel replay. The exact Python checker also passed. [Lean scope](../results/pantone-bona-second-largest-terminal/FORMALIZATION.md)

## Pantone–Bóna third-largest-terminal asymptotic

Run `python3 results/pantone-bona-third-largest-terminal/verify.py` for exact finite checks against literal pattern filtering. The [written proof](../results/pantone-bona-third-largest-terminal/PROOF.md) derives the exact constant from fixed-shape RSK interval symmetry and a shared value band; it does not rely on those checks.

## Pantone–Bóna second-smallest-terminal asymptotic

Run `python3 results/pantone-bona-second-smallest-terminal/verify.py` for exact finite checks against literal pattern filtering. The [written proof](../results/pantone-bona-second-smallest-terminal/PROOF.md) derives the exact constant from the decreasing-band constraint and a uniform tableau-walk estimate; it does not rely on those checks.

## Bétermin FCC/BCC cold spots

The [all-scale proof](../results/betermin-fcc-bcc-cold-spots/PROOF.md) uses parity projection, Jacobi products and a strict concavity argument. The proof does not depend on numerical testing. Run `python3 results/betermin-fcc-bcc-cold-spots/verify.py` for finite Gaussian comparisons and exact rational distance checks, including the corrected BCC representative.

## Coulangeon–Lazzarini two-shell refutation

The [analytic proof](../results/coulangeon-lazzarini-two-shells/PROOF.md) uses parity cosets and does not rely on computation. Run `python3 results/coulangeon-lazzarini-two-shells/verify.py` to enumerate all three shells of the dimension-ten witness and check their second moments.

## Analytic disproofs with supplementary exact checks

The [Brown–Mol disproof](../results/brown-mol/PROOF.md) establishes an infinite tree counterfamily by an analytic local zero argument. Its checker verifies exact polynomial identities, independently enumerates the connected vertex sets of three small trees, and proves a separate Rouché certificate for a 1001-vertex example. The finite checks are not the basis for the infinite-family conclusion.

The [Kovalev disproof](../results/kovalev-hardy-duality/PROOF.md) uses a supporting functional and analytic expectation bounds for every matrix order in its counterfamily. Its two independently written checkers verify the fixed rational comparisons in the proof, including the positive gap above the conjectured constant. They do not approximate Gaussian integrals or perform a finite-dimensional matrix search.

Lean proves the pointwise transfer inequality, the dimension threshold, the fourth-moment calculation and the exact rational separation. The Gaussian expectations and spherical Hardy-norm identities remain to be formalized. [Lean scope and receipt](../results/kovalev-hardy-duality/FORMALIZATION.md).

```bash
python3 results/brown-mol/check.py
python3 results/kovalev-hardy-duality/verify.py
python3 results/kovalev-hardy-duality/review_constants.py
```

All three scripts use only the Python standard library and exact integer or rational arithmetic. The packages contain independent mathematical reviews, root reviews, exact source statements, and current prior-resolution audits. No Lean formalization is claimed for either package.

## Computer-assisted proof of Roos–Seiringer's conjecture

The [Roos–Seiringer package](../results/roos-seiringer-kernel/) proves positivity of the radial Dirichlet kernel on the whole positive real axis, together with its continuous value at zero. Analytic arguments cover arguments at most one and at least forty. On the intervening interval, an analytic derivative bound transfers each exact midpoint enclosure to a whole closed interval.

```bash
python3 results/roos-seiringer-kernel/verify.py
```

The standard-library verifier uses only integers and rational numbers. It retains 160 series terms, encloses pi by signed Machin-series remainders, rounds every operation outward at 384 binary fractional bits, and adds the proved full series-tail allowance. The 184 successful closed intervals cover exactly [1,40], including shared endpoints. Independent full replays reproduce 367 evaluations, maximum subdivision depth eleven, the strictly positive margin in the [proof](../results/roos-seiringer-kernel/PROOF.md), and the [recorded output](../results/roos-seiringer-kernel/check-output.json). The computation is essential, not a finite sample of kernel values. Both [mathematical](../results/roos-seiringer-kernel/ALGEBRA_REVIEW.md) and [root](../results/roos-seiringer-kernel/ROOT_REVIEW.md) reviews passed; no Lean verification is claimed.

## Computer-assisted proof of Lyon's conjecture

The [Lyon package](../results/lyon-gamma-median/) proves the monotonicity assertion on the entire positive half-line. Its exact certificate is an essential part of the proof. Analytic bounds cover the two tails; the [written interval criterion](../results/lyon-gamma-median/PROOF.md) uses known convexity of the gamma median to extend each certified inequality throughout a real cell.

```bash
python3 results/lyon-gamma-median/verify.py
```

The standard-library verifier independently checks 4258 rational median brackets and 4256 cells covering exactly the interval from one tenth to seven. Every sign assertion uses 128-bit-scaled integer intervals with outward rounding, convergent series and explicit signed remainder bounds. The JSON data are proposed brackets, not trusted quantile values. Both independent full replays passed with minimum margin 38316221661991044002598352939471477 divided by 2^128. Typical replay time is one to two minutes. The package has no Lean formalization; the unformalized marker does not erase the essential role of the exact certificate.

## Exact parking-function excedance counterexample

Run `python3 results/alexandersson-parking-excedance/verify.py`. The script checks two exact enumerations through length 17, direct word enumeration through length 6, and the negative Laguerre expression at −1/5. The [proof](../results/alexandersson-parking-excedance/PROOF.md) explains why this refutes the named conjecture. All computations in the Python check are exact. The [Lean receipt](../results/alexandersson-parking-excedance/verification/receipt.json) records strict compilation, the all-owned axiom audit, and stock-kernel replay for the five-module closure. [Lean scope](../results/alexandersson-parking-excedance/FORMALIZATION.md)

## Computational checks

The [Claesson–Dukes–Steingrímsson stack-sorting proof](../results/claesson-dukes-steingrimsson-stack-sorting/PROOF.md) uses an exhaustive count of eleven marked values. Run `pwsh -NoProfile -File results/claesson-dukes-steingrimsson-stack-sorting/verify.ps1` from the repository root with PowerShell 7, Python 3 and Node.js. The replay regenerates the integer coefficient table, checks the rational polynomial identity and boundary orders, and directly enumerates the three smallest orders.

The partial Lean checkpoint is `Conjectures.ClaessonMain`. From `lean`, run `lake build Conjectures.ClaessonMain` and `lake env lean Conjectures\ClaessonSanity.lean`. The build checks the definitions, the complement identity, the ten-row polynomial identity, the exact-depth equivalence under Corollary 2.3, and the stars-and-bars completion factor. The marked-order enumeration and the filtered-prefix principle remain explicit hypotheses; see the [Lean checkpoint](claesson-formalization.md). The full `scripts/verify_lean.sh` replay was not run for this partial milestone.

[Chaudhary–Khmiri–Mazhouda counterexample](../results/chaudhary-khmiri-mazhouda/PROOF.md): the exact interval certificate uses only Python's standard library. Run:

```sh
python3 results/chaudhary-khmiri-mazhouda/verify.py
```

The certificate proves the real-part difference is less than −3/2. [Review and replay](../results/chaudhary-khmiri-mazhouda/AUDIT.md).

The [Cardon et al. disproof](../results/cardon-zero-sector/PROOF.md) uses a symbolic discriminant and an exact rational witness, replayed with Python Fraction. The [Rowland–Sistos Barrón disproof under the quasipolynomial interpretation](../docs/rank-six-power-ranks/PROOF.md) has an all-exponent symbolic proof; its supplementary verifier checks exact coefficient degrees and independent modular recurrence ranks. These are not Lean checks.

```bash
python3 results/cardon-zero-sector/verify.py
python3 docs/rank-six-power-ranks/verify.py --max-exponent 100
```

The [dual Chow counterexample](../results/caiolo-ferroni-hoster/PROOF.md) uses two exact recursions and a symbolic discriminant sign certificate for all prime powers q ≥ 17. The [Ehrhart counterexample](../results/hkm-ehrhart/PROOF.md) uses integer lattice-point counts, exact polynomial interpolation, a rational Descartes certificate, and a negative Wronskian. Both were replayed on 2026-11-24; these are not Lean checks.

```bash
python3 -m pip install sympy==1.14.0
python3 results/caiolo-ferroni-hoster/verify_counterexample.py
python3 results/caiolo-ferroni-hoster/verify_ranks.py
python3 results/hkm-ehrhart/verify.py
```

The [Chen–Khare–Sahi proof](../results/chen-khare-sahi-macdonald/PROOF.md) reduces every degree-six Muirhead-semiring representation to 38 displayed products and seven pure monomials. An exact rational functional is nonnegative on all of them and negative on the specified normalized Macdonald difference. This exhaustive reduction proves nonmembership in the full semiring. The [independent reviews](../results/chen-khare-sahi-macdonald/ROOT_REVIEW.md) also verify the rectangular-translate and continuous-parameter families.

```bash
python3 results/chen-khare-sahi-macdonald/verify.py
python3 results/chen-khare-sahi-macdonald/independent_cone_check.py
python3 results/chen-khare-sahi-macdonald/independent_orthogonality_check.py
```

All three scripts use only exact integers and fractions from the Python standard library. The main verifier checks the full cone, cleared-denominator Macdonald difference equations, and exact normalized separator value. The other scripts independently regenerate the cone values and derive both polynomials from the Hall inner product on all eleven partitions of six before specialization to three variables. Numerical linear programming was used only during discovery and is not a proof premise.


The [Jack semiring proof](../results/chen-khare-sahi-jack/PROOF.md) uses the column-Schur coefficient. One exact checker constructs both Jack polynomials by their differential equation. The other constructs them from the Jack inner product and checks a second separator on all 77 degree-five products. Both use the Python standard library. [Review and expected values](../results/chen-khare-sahi-jack/REVIEW.md)

```bash
python3 results/chen-khare-sahi-jack/verify.py
python3 results/chen-khare-sahi-jack/independent_gram_check.py
```

The [Ferreira–Simon beta-prime proof](../results/ferreira-simon-beta-prime/PROOF.md) is a complete analytic Mellin-transform argument for the full parameter range. Its [two](../results/ferreira-simon-beta-prime/ALGEBRA_REVIEW.md) [independent reviews](../results/ferreira-simon-beta-prime/ROOT_REVIEW.md) check the normalization, domains, positive-series interchanges, and uniqueness step. The standard-library script checks 18 exact identities in formal parameters; these are supplementary algebra checks, not a finite-parameter proof.

```bash
python3 results/ferreira-simon-beta-prime/verify.py
```


The [Han–Sabag–Kostina–Hassibi checker](../results/han-sabag-kostina-hassibi/verify.py) performs 16 exact rational and symbolic checks of the feasible Lyapunov solution, all four sparse power thresholds, the strict objective gap, the determinant factorization and the open family. SymPy supplies only symbolic identity checks. The [written proof](../results/han-sabag-kostina-hassibi/PROOF.md) supplies the exhaustive classification and full disproof.

```bash
python3 results/han-sabag-kostina-hassibi/verify.py
```





The [López Pouso–Segura node disproof](../results/lopez-pouso-segura-quadrature/PROOF.md) has an exact rational comparison at the two-point Gauss–Legendre rule and an all-large-even-degree argument from the Legendre differential equation. The [independent audit](../results/lopez-pouso-segura-quadrature/AUDIT.md) reconstructs the perturbation coefficients, the central normalization, the Gaussian weight conversion and the strictly positive fourth-order term, with analytic remainder justification. Symbolic consistency checks supplement the written proof; no finite root screen or Lean formalization is used.

The [Vishnyakova checker](../results/vishnyakova-root-radius/verify.py) uses SymPy for 73 exact algebraic checks of the generating recurrence, reflection, finite Vandermonde identity, tridiagonal characteristic polynomials, matrix quadratic estimate, reciprocal-segment crossing, and sharpness witness. The [written proof](../results/vishnyakova-root-radius/PROOF.md) covers every degree, every positive weight, and arbitrary independent parameters. The finite checks diagnose algebra and transcription errors; they are not the unrestricted proof.

```sh
python3 results/vishnyakova-root-radius/verify.py
```

The [Novelli–Thibon checker](../results/novelli-thibon/verify.py) independently converts permutation fundamental expansions to Schur coefficients using Kostka numbers. It checks all first-moment identities for 209 partition pairs and all 135 hook coefficients through size six, and exactly matches the source's printed polynomial. These finite checks verify conventions; the [written proof](../results/novelli-thibon/PROOF.md) establishes both identities for every size. The script uses only the Python standard library.

```bash
python3 results/novelli-thibon/verify.py
```

The [López Pouso–Segura checker](../results/lopez-pouso-segura-bessel/verify.py) checks exact polynomial and rational identities used by the analytic proof, with the square of pi treated as a formal variable. The full all-index signs, strict monotonicity, and limits follow from the [written argument](../results/lopez-pouso-segura-bessel/PROOF.md), which has two independent internal reviews. The checker uses only the Python standard library and performs no floating-point root screen.

```bash
python3 results/lopez-pouso-segura-bessel/verify.py
```

The [McCrea checker](../results/mccrea-single-crossover/verify.py) independently enumerates profile words and checks both generating-function rewrites and mean values. It uses only the Python standard library; the full parameter claim is proved in the accompanying note.

```bash
python3 results/mccrea-single-crossover/verify.py
```

The [Chen–Kitaev–Zhang verifier](../results/chen-kitaev-zhang-records/verify.py) checks exact polynomial identities, regenerates the sixteen certificates in the credited tail argument, and checks the class conventions by enumerating separable permutations through length eight. The new result is the full written all-length proof. The [Zhu verifier](../results/zhu-jacobi-stirling/verify.py) independently constructs sparse integer polynomials from the original recurrence and expands the complete determinant by permutations. It verifies the disproof identity, including its negative coefficient. Both scripts use only the standard library.

```bash
python3 results/chen-kitaev-zhang-records/verify.py
python3 results/zhu-jacobi-stirling/verify.py
```

The Fang–Zhang–Zhao infinite-log-convexity and Sun–Zhao iterated-ratio disproofs were already public before this campaign. Their duplicate result packages and computational workflow entries have been removed. The [priority correction](https://github.com/1337isnot1337/solved-conjectures/blob/research/research/campaign-20261121/PRIOR_RESOLUTION_CORRECTION.md) links the immutable prior proofs. Existing unique Lean modules are preserved, with their exact previously checked scope in [Lean status](lean-status.md#formalizations-of-previously-resolved-results). The separate prior Sturm reproof remains only as [credited research](https://github.com/1337isnot1337/solved-conjectures/tree/research/research/fang-zhang-zhao-sturm/).

These are the commands in [the verification workflow](../.github/workflows/verify.yml). They include finite tests, exact certificates, and exhaustive searches; their mathematical roles are explained in the corresponding proof notes. A passing computation is not a claim that a full theorem has been formalized.

The older Karp–Vishnyakova–Zhang Bessel-ratio unimodality package was withdrawn after [a complete earlier analytic proof](https://github.com/the-omega-institute/trureturing/issues/25199) was found. Its duplicate verifier and workflow step are removed. The [priority correction](https://github.com/1337isnot1337/solved-conjectures/blob/research/research/kvz-bessel-unimodality/PRIOR_RESOLUTION_CORRECTION.md) preserves the exact domain comparison and historical proof links.

The [Wright verifier](../results/ferreira-simon-wright/verify.py) checks
the general curvature identity as an exact polynomial in three variables,
its two parameter-polynomial specializations, and the displayed derivative
values. The [analytic proof](../results/ferreira-simon-wright/PROOF.md) supplies
the uniform convergence and whole intervals of counterexamples.

The [Wright Lean module](../lean/Conjectures/FerreiraSimonWright.lean) now proves
the original universal conjecture false through its continuous beta-zero
family, directly from the infinite series. Strict compilation, the full
owned-declaration axiom audit, and stock-kernel replay passed; the
[receipt](verification/lean-wright-20261121/wright-receipt.json) records the
exact source, objects, compiler, audit, and replay. The written positive-beta
refinements are not formalized, and the combined repository gate is pending.

The [gamma-quotient verifier](../results/kvz-gamma-quotient/verify.py)
uses exact rational arithmetic for 115 checks of half-integer determinant
signs, integer rank cutoffs, and gamma-moment normalization. The complete
all-order result follows from the [integral proof](../results/kvz-gamma-quotient/PROOF.md),
not from these finite diagnostics.

The [Fuss–Catalan verifier](../results/alexandersson-fuss-catalan/verify.py)
enumerates small paths directly to check the north/east convention and
both marked factors against the classical formula. Its all-parameter
real-rootedness proof is written separately and uses no numerical roots.

The workflow also regenerates the two compact CUT certificate sources with
`results/cut-arithmetic-periodicity/generate_weight_certificates.py` into a
temporary directory and compares them byte for byte with the checked-in files.
Generation alone does not check a proof. The accepted Lean workflow checks the
finite tables, their collision and lower-option interpretation, and both actual
recursive-game identities through `CutPeriodWeightTheorem`.

```bash
python3 -m pip install sympy==1.14.0
python3 results/ferreira-simon-wright/verify.py
python3 results/kvz-gamma-quotient/verify.py
python3 results/alexandersson-fuss-catalan/verify.py
python3 results/sagan-swanson-normality/verify_model.py
python3 results/bernardi-morales-delta/verify.py
python3 results/bernardi-morales-delta/verify_events.py
python3 results/gilmore-crossing-nesting/verify.py
python3 results/chow-conjecture/verify.py
python3 results/erdos-granville-pomerance-spiro/verify.py
python3 results/hornak-wozniak/verify.py
python3 results/sonntag-teichert/verify.py
python3 docs/nss/sanity_check.py --output /tmp/nss-sanity-results.json
python3 results/l-solitaire-limit-shapes/verify.py
python3 results/pham-denominator-degree/verify.py
python3 results/pham-denominator-degree/verify.py --dual --brute-depth 13
(cd results/pham-denominator-degree && python3 -m unittest discover -s tests -v)
python3 results/graffiti-pc-318/verify.py
python3 results/li-coefficient-sign/verify.py
python3 results/li-coefficient-sign/independent_check.py
python3 results/batista-egyptian-fractions/verify.py
python3 results/erdos-607-line-sizes/verify.py
python3 results/rectangle-partition-asymptotics/verify.py
python3 results/spivey-multiplayer-war/verify.py
python3 results/cut-family-b/verify.py
python3 results/cut-arithmetic-periodicity/verify.py
c++ -std=c++20 -O3 results/distance-graph-densities/verify.cpp -o /tmp/verify-distance-graphs
/tmp/verify-distance-graphs
python3 results/distance-graph-densities/counterexample.py
python3 results/oravcova-sotak/verify.py
python3 results/babai-spectrum-paths/verify.py
python3 results/two-difference-motzkin/verify.py
python3 results/symmetric-four-point-density/verify.py
python3 results/nonmixed-gap-packing/verify.py
python3 results/haralambis-three-differences/verify.py
python3 results/circular-index-upper-half-circulants/verify.py
python3 results/circular-index-upper-half-circulants/verify_part2.py
python3 results/circular-index-upper-half-delta-2-mod-4/verify.py
python3 results/circular-index-upper-half-delta-3-mod-4/verify.py
python3 results/five-speed-spectrum/verify.py
python3 results/tight-six-speeds/verify.py
python3 results/six-speed-spectrum/verify.py
python3 results/tight-seven-speeds/verify.py
python3 results/tight-eight-speeds/verify.py
python3 results/eight-speed-spectrum/verify.py
python3 results/seven-speed-spectrum/verify.py
python3 results/tight-eleven-to-fourteen/verify.py
python3 results/currie-conjecture-19/verify.py
python3 results/tight-nine-speeds/verify.py
python3 results/zhang-deletion-values/verify.py
python3 results/shifted-lonely-runner-counterexamples/verify.py --quick
python3 results/circular-index-complete-minus-edge/verify.py
python3 results/circular-index-complete-minus-edges/verify.py
python3 results/circular-index-complete-minus-edges/verify_seq.py
python3 results/wild-number-complete-graphs/verify.py
```

The latest workflow is the executable reference when new checks are added.

## Circulants in the upper half of the circular chromatic index

Run `python3 results/circular-index-upper-half-circulants/verify.py` and `python3 results/circular-index-upper-half-circulants/verify_part2.py` with assertions enabled. The first standard-library script checks the `(2n,3)`-edge-colourings of Theorem 1 for `g = 2..30` (partition into classes, matchings, the window condition per vertex and per window, `α' = (n-1)/2` and `|E|/α' = 2n/3`), the vertex connectivity `4g` for `g <= 8` with its own max-flow routine, and the `(75,4)`-edge-colouring and connectivity of Theorem 2. The second rebuilds every certificate of Section 7 from `data/part2_certificates.json` and checks that it is a perfect colouring of a simple graph with the stated `Δ` and `χ'_c`, and the connectivity of the regular circulants. The scripts in `review/` (which need `networkx`) and in `search/` (most need `python-sat`) are not run by CI. The [Lean proof](../results/circular-index-upper-half-circulants/FORMALIZATION.md) covers the main theorems and all 17 stored nonregular examples.

## Graphs with circular chromatic index in the upper half for Δ ≡ 2 mod 4

Run `python3 results/circular-index-upper-half-delta-2-mod-4/verify.py` with assertions enabled. The standard-library script builds the base matchings of Section 3 for `6 <= g <= 60` (the `g = 6` base from `certificates.json`), checks their lengths, the partition of the circulant into `2n` classes, the windows of the base colouring and the two insertion blocks, and then checks for both final graphs simplicity, `Δ`, the `(p,3)`-colouring per vertex from the definition and `|E|/((n-1)/2) = p/3 = Δ+2/3`. Part 2 rechecks the `(3n-1,3)`-colourings of `K_n-tK_2` for `n = 11, 15, 19, 23, 27`, and five negative controls must be rejected. The referee scripts in `review/` are not run by CI; `indep_check.py` and `mut_test.py` need `numpy` and `networkx`. The [Lean proof](../results/circular-index-upper-half-delta-2-mod-4/FORMALIZATION.md) covers the infinite one- and two-block families and the explicit degree-21 example.

## Graphs with circular chromatic index in the upper half for Δ ≡ 3 mod 4

Run `python3 results/circular-index-upper-half-delta-3-mod-4/verify.py` with assertions enabled. The standard-library script builds the base matchings and the three insertion blocks of Sections 4 and 5 for `15 <= g <= 60` and checks the claimed lengths. For each graph it checks that the base matchings are perfect on `W_0`, `W_1` with `2g` distinct lengths, that every block class is a matching on the vertex set it copies, simplicity, that the graph contains `C_n(S)`, `Δ = 4g+3`, `|E| = 2gn+9g`, the `(2n+9,3)`-colouring per vertex from the definition and `|E|/((n-1)/2) = p/3 = Δ+2/3`. It runs the same checks on the nine certificates of Proposition B (`6 <= g <= 14`) from `certificates.json`, and six negative controls must be rejected. The independent re-check `indep_check.py` and the referee scripts in `review/` use only the standard library but are not run by CI. The [Lean proof](../results/circular-index-upper-half-delta-3-mod-4/FORMALIZATION.md) covers the uniform construction, all nine finite witnesses and the small forward-insertion exclusions.

## Perron root of permanental compounds

Run `python3 results/perron-root-permanental-compounds/verify.py` with assertions enabled. It uses only the Python standard library and checks 126 exact cyclic-permanent identities, 81 Newton inequalities and 2,048 support/zero-root comparisons. These finite checks validate the reduction formulas. They do not implement the permanent approximation sampler or prove the FPRAS's unbounded scope; those claims depend on the [written proof](../results/perron-root-permanental-compounds/proof.md), Gurvits's theorem and the Jerrum–Sinclair–Vigoda theorem. The result has no Lean verification or computer-assisted proof badge.

## Malek's conjecture

Run `python3 results/malek-subpermanent/verify.py` with assertions enabled. The standard-library checker verifies the exact scalar upper constants, the two expansions used to compute them, the positive cubic certificate, the all-order shifted polynomial, and the remaining small-degree coefficient. These are algebraic checks of the [written proof](../results/malek-subpermanent/proof.md), not a finite matrix search. The unbounded statement rests on the analytic argument and its cited inputs. Two internal review receipts and a bounded source audit accompany it. No Lean verification is included.

## Currie's complexity 2n+1 conjecture

Run `python3 results/currie-conjecture-19/verify.py` with assertions enabled. The standard-library script checks the morphism identities of the reduction, exact factor sets of the fixed point, the hypotheses of the insertion lemmas and the short bispecial factors, and the critical-exponent inequality for the 72 families by exact arithmetic in `Q(λ)`. As cross-checks it compares the bispecial factors with an exhaustive enumeration up to length 300, checks the complexity `2n+1` up to length 300 for all twenty words, and searches long prefixes for repetitions. It takes about 15 to 50 seconds. The standard-library scripts in `review/` are the independent referee pass's checks and are not run by CI. The [written proof](../results/currie-conjecture-19/PROOF.md) covers all lengths; no Lean verification is included.

## Pula–Song–Wanless conjecture

Run `python3 results/pula-song-wanless/verify.py` with assertions enabled and SymPy 1.14.0 installed. The script audits generic derivative/crossing identities, 72 coefficient ODE/variance cases, 48 direct permanent counts and 42 exact barycenter inequalities. The full proof, including the real-rooted-minor reduction repair and independent uniqueness argument, is [written separately](../results/pula-song-wanless/proof.md). These finite checks do not establish the unbounded statement on their own. No Lean verification is included.

## Mazák–Zrubák complete graphs minus an edge

Run `python3 results/circular-index-complete-minus-edge/verify.py` with assertions enabled. The standard-library script enumerates the 2160 proper 5-edge-colourings of `K_5-e`, checks Lemmas 2, 3, 4 and 5(1) on the 180 with acyclic digraph, and shows that no edge ordering with the properties of Lemma 3 exists for `d=6`. The optional `verify_sat.py` and `review/sat_levels.py` check `d=6` directly from the definition, need `python-sat`, and are not run by CI; the other `review/` scripts are the referee pass's independent checks. The [written proof](../results/circular-index-complete-minus-edge/PROOF.md) covers every even `d >= 6`; no script completed `d=8`. The [scoped Lean receipt](../results/circular-index-complete-minus-edge/verification/steps-1-3/receipt.json) covers Steps 1–3. The [Step 4 receipt](../results/circular-index-complete-minus-edge/verification/step-four/receipt.json) covers actual run rigidity. The [paired-column receipt](../results/circular-index-complete-minus-edge/verification/paired-columns/receipt.json) checks the first two Step 5 assertions. The [occurrence-interval receipt](../results/circular-index-complete-minus-edge/verification/actual-table/receipt.json) checks the third. The final equality remains outside the Lean scope.

## Circular chromatic index of complete graphs minus a few edges

Run `python3 results/circular-index-complete-minus-edges/verify.py` and `python3 results/circular-index-complete-minus-edges/verify_seq.py` with assertions enabled. The first standard-library script checks the 32 explicit `(p,q)`-edge-colourings of `K_n-F` in `colourings.json` from the definition and prints the matching lower bound `N/m`. The second searches exhaustively for perfect sequencings of `K_5-e`, `K_7-e`, `K_9-e`, `K_7-P_3` and `K_7-2K_2` and checks Lemmas A2 to A4 and the class counts of A5 on those of `K_5-e`; it takes about 25 seconds. The optional `verify_sat.py` and `drat/mkproof.py` need `python-sat` and are not run by CI, nor are the referee scripts in `review/`. The [written proof](../results/circular-index-complete-minus-edges/PROOF.md) of Theorem A covers every odd `n >= 7`; the exact values for small `n` also rest on exhaustive searches and SAT runs. No Lean verification is included.

## Wild number of complete graphs for n ≥ 155

Run `python3 results/wild-number-complete-graphs/verify.py` with assertions enabled. The standard-library script checks in exact rationals the counting inequality for the fixed block, condition (*) of Theorem B for every odd `n` from 155 to 189 with the author's coefficients and with the second referee's independent coefficients, the lopsided local-lemma condition of Theorem A for every odd `n` from 189 to 1201, and the first referee's monotone tail bound at `n = 1201`. It takes a few seconds. The counts themselves are proved in the [written notes](../results/wild-number-complete-graphs/); the scripts in `improvement/`, `review/` and `review2/` are optional cross-checks, and `theorem-a/verify.py` needs NumPy and SciPy. None of these checks decides any `n` in the open range `13 <= n <= 154`. No Lean verification is included.

## Zhang's Question 8.4

Run `python3 results/zhang-deletion-values/verify.py` with assertions enabled. The standard-library script checks the closed deletion-value formula in all 779 cases with `3 <= n <= 40`, the strict inequality in all 740 cases with `n >= 4` and `r <= n-2`, and the witness time used in the second case. The [elementary proof](../results/zhang-deletion-values/PROOF.md) is unconditional; the finite check confirms the formula in the stated range. No Lean verification is included.

## Upper-half circular chromatic index: the seven remaining degrees

Run `python3 results/circular-index-upper-half-remaining-deltas/verify.py`.
The [certificate note](../results/circular-index-upper-half-remaining-deltas/README.md)
gives tomdif’s seven graphs and exact bounds. Together with the earlier
construction notes they cover every maximum degree at least eight.
The optional SAT search is not needed for verification. The [scoped Lean replay](../results/circular-index-upper-half-remaining-deltas/verification/real-index/receipt.json) checks the real circular-index result for the seven new literal graphs.

## Zhang's Question 8.5: shifted lonely runner counterexamples

Run `python3 results/shifted-lonely-runner-counterexamples/generate_lean.py --check` to compare the Lean witnesses with all 40 records in the published JSON. The [target replay command](../results/shifted-lonely-runner-counterexamples/FORMALIZATION.md) rebuilds the proof of the real-time maxima, audits every declaration and replays the stock kernel. For an independent rational calculation run `python3 results/shifted-lonely-runner-counterexamples/verify.py --full`. Its `--quick` option checks arc coverage for every record and recomputes the exact maximum for $18\le n\le24$ and $n=41$.

Run `python3 results/shifted-lonely-runner-counterexamples/verify_frozen_extension.py` to check the exact optimum, the full interval of optimal phases and the stability margin for adding one runner to the fixed 57-runner seed. [Statement and proof](../results/shifted-lonely-runner-counterexamples/FROZEN_EXTENSION.md).

## Baricz–Pogány coefficient positivity

The existing result package's standard-library diagnostic is `python3 results/baricz-pogany-coefficients/verify.py`. It checks the formal-series identities and finite source fixtures described in its [landing page](../results/baricz-pogany-coefficients/). The full coefficient theorem and source-recurrence endpoint are Lean-verified; the [local receipt](verification/lean-named-20261121/baricz-receipt.json) records strict source compilation, the all-owned axiom audit, and stock-kernel replay.

## Oravcová–Soták distance-graph classification

Run `python3 results/oravcova-sotak/verify.py` with assertions enabled. The standard-library script checks the 65 spectrum-table sets and their exact `L(D)`, the 62 periodic colourings, the three exceptional sets, the 37 loop certificates for the four one-parameter families, the two-parameter family, and the small cases of the clique lemma. The classification is [proved relative to](../results/oravcova-sotak/PROOF.md) the repository's five- to eight-speed spectrum classifications. The optional SAT scan in `search/` is independent of those classifications and is not run by CI. The [Lean checkpoint](verification/lean-named-20261121/oravcova-receipt.json) verifies all explicit coloring certificates and the full relative deduction; `R5`–`R8` remain unproved inputs.

## Johnson–Kaya–Matzke path spectra

Run `python3 results/babai-spectrum-paths/verify.py` with assertions enabled. The standard-library script computes the chromatic number of every distance graph of `P_n` with `2 <= n <= 14`, 16,369 distance sets in all, and checks that each `Spec(P_n,k)` is the interval from `ceil(n/(n-k))` to `k+1`. It also checks the independence bound by exhaustive search for `n <= 10` and the integer `m` of Johnson–Kaya–Matzke's Theorem 2.3. The [Lean formalization](../lean/Conjectures/BabaiPathSpectrum.lean) proves both bounds and every realization for all admissible `n,k`; [local validation](verification/lean-named-20261121/babai-receipt.json) passed strict sources, all-owned axioms, and stock-kernel replay. The finite Python check is supplementary.

## Lean proofs

```bash
bash scripts/verify_lean.sh
```

The script builds each accepted module sequentially, builds the shared root imports, runs `ProofAudit.lean` with warnings treated as errors, and independently rechecks the listed compiled modules with `leanchecker`. The audit covers private declarations as well as public theorems, and rejects project axioms even when unused. Sequential builds keep large finite reductions from competing for memory. [The Lean workflow](../.github/workflows/lean.yml) runs the same audit in CI.

`scripts/replay_lean.py` checks that the replay list exactly matches the project
source-import closure. It stages those compiled objects, including their server
and private data, and replaces only the project entry in Lean's import path.
The unchanged pinned `leanchecker` then replays the two project namespaces.
This avoids repeated dependency-directory scans and excludes unfinished cached
modules. It does not change the kernel or omit any accepted proof module.

After building and auditing a separate candidate, replay its exact local import
closure from `lean/` with:

```bash
lake env python3 ../scripts/replay_lean.py --root Conjectures.DenominatorTheorem
```

The helper derives the closure from the selected source, requires every project
source and compiled object, stages only that closure, and propagates checker
failure. Cross-namespace candidates use the complete accepted-module mode.
`python3 scripts/test_replay_lean.py` checks the closure, staging, missing-object,
and failure-propagation rules with isolated fixtures. The kernel executable is
unchanged in both modes.

The [status report](lean-status.md) records the exact statements checked and dependencies that remain. Partial certificates do not establish the full conjecture. Accepted proofs permit only `propext`, `Classical.choice`, and `Quot.sound` as transitive axioms, as required by [the repository instructions](../AGENTS.md).

## What the checks establish

The two `results/bernardi-morales-delta/` verifiers use only the Python standard library. `verify.py` directly constructs the delta process and checks all membership coefficients for 71 fixed maps and 111,721 process pairs, including nonsurjective maps. It also checks 25 arbitrary-matrix determinant identities in sizes two through six. `verify_events.py` builds the source's cyclic I/J event matrices literally and compares every membership coefficient for 342 marked-surjection profiles and 438,952 exact determinants. These are independent finite checks of the [tree proof](../results/bernardi-morales-delta/PROOF.md) and [event proof](../results/bernardi-morales-delta/EVENT_PROOF.md), which cover every admissible parameter.

`results/gilmore-crossing-nesting/verify.py` compares the literal matrix product and the independently implemented recurrence through row seven, and compares the first column with all perfect matchings on at most twelve vertices. All four variables remain formal. The [written proof](../results/gilmore-crossing-nesting/PROOF.md) proves the identity in every row. The complete Lean proof and its [local validation receipt](verification/lean-named-20261121/gilmore-receipt.json) cover every row; the finite Python checks are supplementary.

`results/chow-conjecture/verify.py` compares signed-permutation enumeration with the refined recurrence through rank six, checks the separate Stembridge identity through rank 32, and checks exact degree, squarefreeness, consecutive gcd, and cutoff identities. These are finite consistency checks. The [written proof](../results/chow-conjecture/PROOF.md) uses Savage–Visontai's published theorem and a separate strictness argument for every rank.

`results/sonntag-teichert/verify.py` enumerates the minimal dominating sets of every labelled tournament through order six and every labelled oriented graph through order five. It also checks the two-star construction. The [proof](../results/sonntag-teichert/PROOF.md) covers every order.

`results/hornak-wozniak/verify.py` compares the five arithmetic tests against direct allocation of prescribed parts on small trees and checks the local transfer lemma by enumerating allocations. The [written proof](../results/hornak-wozniak/PROOF.md) covers both conjectures. The optional [symbolic check](../results/hornak-wozniak/verify_symbolic.py) uses `z3-solver` for the local endpoint implications.

`results/erdos-granville-pomerance-spiro/verify.py` checks finite instances of the quadratic-root bounds, the bilinear congruence lift and local sieve counts, and the cofactor identities in the [written partial result](../results/erdos-granville-pomerance-spiro/). The asymptotic statements use the analytic proofs.

`results/graffiti-pc-318/verify.py` uses only the Python standard library. It checks all 419,235 labeled graphs on 2–7 vertices with at most `n+1` missing edges; 7,337 satisfy the original hypothesis and each passes the total-domination test. A sharp five-vertex counterexample to a one-unit relaxation is separately verified. See [the all-order proof](../results/graffiti-pc-318/PROOF.md), **credited to [@JesterInABarrel](https://x.com/JesterInABarrel/status/2123233964827812334)**. This is not a Lean proof.

`results/l-solitaire-limit-shapes/verify.py` is the original embedded PDF attachment, extracted byte-for-byte. The finite search checks all pick-layer sets and integer partitions for deck sizes 1 through 14 and separately verifies the specific counterexample for sizes 1 through 1000. Exhaustive tests do not replace the general argument in the PDF.

`results/pham-denominator-degree/verify.py` checks a finite certificate of 26 coefficients and applies Pham's *proved* degree bounds to deduce the entire rational-function identity. Optional `--dual` checks a second exact identity.

The Li verifier also checks all 6,842 partition types of 31 and the coefficient `+29` using exact edge-cut and coloring calculations. Its independent parity-based check is included. The original PDF has the verifier embedded as an attachment.

## Reporting a check

Record the commit, command, toolchain, and result. Distinguish computational tests, source builds, axiom audits, kernel replay, and hosted CI. Do not infer that an unrun check passed.

## Loneliness on a fixed hyperplane

The complete original note is formally verified in the exact 72-module
`LonelinessHyperplaneMain` closure. The fresh gate checks strict sources,
every owned declaration including raw private declarations, all 106 named
theorem endpoints, and every exact stock-kernel target. The original
[statements and evidence](../results/loneliness-on-a-hyperplane/LEAN.md)
include the uniform-over-shifts estimate, exact positive-N counts and degree
bound, Haar-shift law, endpoint formula and sharpness.

Run `python3 results/loneliness-on-a-hyperplane/verify.py` for the additional
finite circle maxima, endpoint congruences and shifted examples.

## Complete rectangle proof and finite plane certificates

The accepted Lean root includes the full growing-rectangle theorem, including
its real-position tiling interpretation and uniform quantifiers over `w ≥ h`.
Its 46 proof modules passed source checks and independent kernel replay; the
final rectangle audit checked 587 theorem declarations. See the
[exact statement and receipt](../results/rectangle-partition-asymptotics/LEAN.md).

The accepted plane development includes all 64 finite certificate blocks and
their normalization and geometric soundness proofs. The matrix checks all
122,880 indexed cases by kernel reduction. The two complete hosted matrix
runs passed; [the source receipts](../results/five-speed-spectrum/plane-certificate-receipts.json)
bind their sources and generator. Run `python3 scripts/verify_plane_certificates.py --row N` for one row, with `0 ≤ N < 8`. The full accepted package is checked
by `scripts/verify_lean.sh`.

The accepted four-speed coordinate cutoff 5,832 is unconditional. The plane
classification and five-speed cutoff 279,841 retain `FourSpeedGap` as an
explicit premise. Neither the finite matrix nor that conditional cutoff is
a proof of the exhaustive five-speed classification.

## Selecting accepted-package checks

The full Lean workflow derives the transitive source closure of both
accepted roots and `ProofAudit`. Any change to that closure, the pinned
configuration, or the verification scripts runs the complete build, axiom
audit, and unchanged independent kernel checker. Missing roots, missing
imports, unknown change information, and manual runs also select the full
gate. Only candidate-only or documentation-only changes can skip it.

A skipped job is not a new proof receipt. Each unregistered candidate has
its own complete closure checks. Negative controls check transitive public
imports, missing-source handling, newly registered candidates, and stale
dependent-object rejection after a candidate source error.

## Frankl high-girth theorem

Run `python3 scripts/verify_frankl_high_girth_theorem.py --jobs 4` from the
repository root after preparing the pinned Lean package. This focused gate
rebuilds the exact 64-module theorem closure with warnings treated as errors,
audits every owned declaration against the standard three-axiom whitelist,
requires 35 named endpoints, and replays every project module with the
unchanged stock checker. It rejects changed source, object, compiler,
checker, or gate hashes.

[Successful hosted run](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44516856625) ·
[Original receipt](verification/frankl-components-44516856625/high-girth-theorem.json).
This verifies the complete high-girth frequency theorem. The cyclic
span-four theorem has separate finite graph, transport, coverage, and final
assembly gates. The registered full package is checked by
`scripts/verify_lean.sh`.

## Complete two-speed insertion gate

From the repository root with the pinned toolchain and Mathlib cache:

```sh
python3 scripts/verify_two_insertions_exact.py --plan
python3 scripts/verify_two_insertions_exact.py
```

The exact source model fixes all 27 project modules, 49 required theorem
endpoints, the toolchain configuration, and all transitive gate helpers.
The gate rebuilds every project source with warnings treated as errors and
no linter override, audits all owned declarations and raw private names,
then replays each of the 27 modules as an exact singleton target with the
unchanged stock checker in a fresh one-worker process. It rehashes the
sources, helpers, compiler, checker, every compiled facet, and proof
evidence before writing a passing receipt.

[Run 44524198858/job 135562276051](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44524198858/job/135562276051)
passed for source snapshot `9f51470529423e8135c08de881cd56f5b1fd9a95`.
It checked 563 owned declarations, including 424 theorems and 11 private
declarations. The [original receipt](verification/two-insertions-exact-44524198858/receipt.json)
and [authenticated original evidence](verification/two-insertions-exact-44524198858/)
are public. Receipt preservation performs byte and policy validation;
it is not an additional Lean proof run. This component pass is separate
from the full merged-package gate.

## Six-speed spectrum realization

```sh
python3 scripts/verify_six_spectrum_realization.py --plan
python3 scripts/verify_six_spectrum_realization.py
```

This dedicated gate rebuilds the exact 11-module closure, treats all source
warnings as errors without disabling linters, audits every owned declaration
and raw private name, requires theorem kind for all 15 endpoints, and replays
all 11 modules as exact singleton stock-kernel targets. Source, configuration,
transitive helper, compiler, checker, object and process-evidence hashes are
fixed and rechecked.

The [passed original receipt](verification/six-spectrum-realization-44527134869/receipt.json)
and [authenticated evidence](verification/six-spectrum-realization-44527134869/)
cover 392 owned declarations, 306 theorems and 30 private declarations.
The gate establishes realization of the proposed six-speed values; universal
classification and the full accepted-package verification are separate.

## Complete fixed-hyperplane theorem

All original statements of the fixed-hyperplane note are registered. They
use the original ordered positive, pairwise-distinct integer sample and
the actual time maximum. The general normal is primitive and real-admissible;
the endpoint formula alone additionally requires every normal coordinate
to be nonzero.

The theorem closure proves the deterministic bound and exact containing-torus
maximum, the uniform `O(1/N)` probability error over all shifts, fixed-shift
and independent Haar-shift laws, the exact finite proper-subspace description,
the denominator quasipolynomial, the actual subthreshold numerator at every
`N≥1` with degree at most `k−2`, the endpoint frequency including `k=2`,
and the sharp `(1,2,3)` example. No density, finite-fan, Ehrhart, counting
or classification statement is an unproved premise.

[Run 44531509741/job 135585736594](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44531509741/job/135585736594)
freshly checked the exact 72-module closure at `ee1f018fef258cdd54f73af31cdaf6485fd151cb`.
Sources used warnings as errors with no linter override. The all-owned audit
checked 1,403 declarations, including 1,149 theorems and 44
private declarations, and confirmed theorem kind for all 106 required
endpoints. Only `propext`, `Classical.choice` and `Quot.sound`
were allowed. All 72 modules passed exact singleton stock-kernel replay in
fresh one-worker processes.

The [unchanged raw receipt](verification/hyperplane-main-exact-44531509741/receipt.json)
has SHA-256 `1c0d6a6fbe2ea16bbcfa88808ec8d83f0e412217e76c03803780ff0737fa1c15`.
The [preservation record](verification/hyperplane-main-exact-44531509741/preservation.json)
authenticates the actual original source, object, audit, log and progress
bytes. Artifact `14535236819` has ZIP SHA-256 `27d65f3b5d667260dfad8d639f6d1182a3b5e54c032a2e2954d7764e060fe638`.

Registration adds 63 previously unregistered proof modules and 102 new
required endpoints, with all 72 checked source blobs guarded. The accepted
list has 969 proof modules plus two roots. This completes the fixed-hyperplane
result; verification of the merged accepted package remains a separate gate.
The [result-level scope](../results/loneliness-on-a-hyperplane/LEAN.md)
records the precise sample, formulas and distributional formulation.

## Conditional nine-through-thirteen speed norm reduction

The 81-module closure of `LonelinessTightNormBounds` is checked and
registered. For a positive primitive `k`-tuple with `9≤k≤13` and actual
loneliness value at most `1/(k+1)`, it proves the literal squared-norm
cutoff and a listed prime dividing no speed, under the explicit hypothesis
`∀ m, 1≤m → m<k → LonelyRunnerBound m`. The basis geometry,
nearest-plane bounds, all 7,936 KZ subset rows and prime-product margins
are proved internally.

[Run 44530735399/job 135583044214](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44530735399/job/135583044214)
passed at `8162a5dfbe89e441600e7a3bbcc03b573df0880e`: all 81 strict source checks, the all-owned
audit of 1,696 declarations (1,445 theorems and 538 private declarations),
all 25 required theorem endpoints, and all 81 exact singleton stock-kernel
replays. Sources and audit used warnings as errors without a linter override;
the only allowed axioms were `propext`, `Classical.choice` and `Quot.sound`.

The [unchanged receipt](verification/loneliness-large-norm-exact-44530735399/receipt.json)
has SHA-256 `fba4b952a87271f9691e983dd69dafc0be5c07617e412884eb82f2894ec2fef5`.
The [preservation record](verification/loneliness-large-norm-exact-44530735399/preservation.json)
authenticates the actual original sources, objects, audit and process records.
Artifact `14535137698` has ZIP SHA-256
`b6678fb2e27c872d01a2bbd6bea9982abc42411e79999b6c4113961195ab3366`.

Registration adds 64 proof modules and 25 required endpoints. The accepted
list then contains 1,033 proof modules plus two roots. The merged-package
gate remains separate. Lower-runner assumptions, exhaustive modular
classification and final uniqueness remain open, so no result directory
becomes complete from this reduction.
[Exact hypotheses, cutoffs and scope](loneliness-large-norm-lean.md).






## Chern–Fu–Lin’s three-statistic equidistribution conjecture

The [formalization page](../results/chern-fu-lin-three-statistic/FORMALIZATION.md) gives the target build, all-owned axiom audit, stock-kernel replay, and a separate literal statement check for Conjecture 6.1. The [original audit](../results/chern-fu-lin-three-statistic/AUDIT.md) records the finite checks and symbolic certificate for the written proof.

## Chern–Fu–Lin joint Eulerian exact certificate

With Python 3, SymPy 1.14, a C++ compiler, and GMP development libraries installed, run

```sh
python3 results/chern-fu-lin-joint-eulerian/joint-certificate.py
```

The two polynomial pseudo-remainders must both report exact zero. The program bounds the degrees and coefficient sizes before encoding, so neither a sampled variable substitution nor a finite series truncation is used. This is an exact algebraic certificate, not a Lean proof.

## Dukes revstack interlacing exact bridge

Run `python3 results/dukes-revstack/check.py` from the repository root. Exact rational sign isolation establishes all transitions 3→4 through 127→128. The [analytic proof](../results/dukes-revstack/PROOF.md) proves all later transitions.

Lean proves the literal Eulerian enumeration for every order at least three and the first strict root interlacing transition. The uniform root estimates remain in the written proof. [Lean verification](../results/dukes-revstack/FORMALIZATION.md).

## Chow type-D Eulerian exact bridge

Run `python3 results/chow-conjecture/check_dyadic.py` from the repository root. It certifies every strict transition into degree 128 using exact dyadic signs. The [analytic proof](../results/chow-conjecture/ALTERNATIVE-PROOF.md) handles all subsequent transitions.

## Gravgaard–Lee mixed Lüroth interval certificate

Run `python3 results/gravgaard-lee-mixed-luroth/check.py` from the repository root. The checker verifies the fifteen containments with exact rational arithmetic. The [proof](../results/gravgaard-lee-mixed-luroth/PROOF.md) establishes the graph-directed infinite expansions.

## Cylindric skew and truncated-square exact witnesses

Run `python3 results/fmp-cylindric/check.py` to reproduce the exact negative coefficient and boundary diagnostics, and `python3 results/meylender-thalmaier-truncated-square/check_pentagon.py` to replay the rational pentagon comparison. The corresponding proofs describe their full scope and the distinct conclusions left open.

## Juhnke arbitrary-step path checker

Run `python3 results/juhnke-lattice-paths/check.py` to replay the independent exact finite checks supporting the all-dimensional written proof.

## Lassalle first-value log-concavity enclosure

Run `python3 results/defant-engen-miller-lassalle/interval_check.py` to verify the finite integer rows and the 205 outward-rounded interval boxes in the all-order proof. The mathematical bridge from those boxes to every later row appears in the proof.

## Higashitani–Kummer–Michałek exact witnesses

Run `python3 results/hkm-ehrhart/check_sturm.py` and `python3 results/hkm-ehrhart/check_interlace.py` to reproduce the two exact complete-multipartite counterexamples. The [proof](../results/hkm-ehrhart/STURM-CERTIFICATE.md) and [interlacing supplement](../results/hkm-ehrhart/INTERLACING-CL.md) give the mathematical derivation.

## Sagan–Wilson coefficient mode certificate

Run `python3 results/sagan-wilson-plactic-mode/check.py` to verify the exact length-ten witness. The [proof](../results/sagan-wilson-plactic-mode/PROOF.md) also gives the general asymptotic position independently of the finite check. The [Lean receipt](../results/sagan-wilson-plactic-mode/verification/receipt.json) records strict compilation, the complete axiom audit and stock-kernel replay. Run `python3 results/sagan-wilson-plactic-mode/check_tableaux.py` for the direct insertion comparison.

## Bicyclic facets and complete-graph specialization

The [joint Lean verification](../results/braun-bruegge-bicyclic-facets/FORMALIZATION.md) checks the sharp bicyclic maximum and exact theta optimizer on the geometric facet counts. It includes the finite comparisons and the uniform bounds for all larger path lengths.

Run `python3 results/braun-bruegge-bicyclic-facets/check.py` and `python3 results/braun-bruegge-bicyclic-facets/check_maximizer.py` for the exact finite parts of the two graph theorems. Run `python3 docs/weighted-complete-graph-moments/check_complete.py` for the independent exact recurrence comparisons of complete graphs.

## Sharp matching-number facet bound

The two global minimum clauses have a complete scoped Lean gate for the actual geometric facets. The [formalization page](../results/braun-bruegge-minimum-facets/FORMALIZATION.md) gives the command and links the source, all-owned axiom audit and kernel replay evidence.

Run `python3 results/braun-bruegge-minimum-facets/check.py` for exact independent polar-vertex and maximum-matching counts on small graphs. Compile and run the optional exhaustive C++ checker for all graphs through order six. The two written proofs give the general results without enumeration.

## Xu–Zhou diameter–Laplacian conjecture

Run `python3 results/xu-zhou-laplacian-diameter/check.py` for exact rational inertia through all small ordered layer compositions and the sharp example family. The [analytic proof](../results/xu-zhou-laplacian-diameter/PROOF.md) establishes all parameters.

## Random subset sums and simultaneous spherical harmonics

The [mixed-group threshold proof](../results/ma-tang-random-subset-sums/PROOF.md), its [remainder supplement](../results/ma-tang-random-subset-sums/BOUNDED-REMAINDER.md) and [Han’s simultaneous saturation proof](../results/han-spherical-harmonic-saturation/PROOF.md) are analytic arguments independently checked against their primary sources. No finite-range search or Lean proof is used.

## Permutation word mixing and small eigenfunction norms

[Féray’s word-measure proof](../results/feray-conjugate-power-word/PROOF.md) and its [sharp-rate supplement](../results/feray-conjugate-power-word/SHARP-RATE.md), as well as the [spherical basis construction](../results/steinerberger-small-average-eigenfunction-norms/PROOF.md) and its [per-mode extension](../results/steinerberger-small-average-eigenfunction-norms/POINTWISE.md), are analytic arguments with independent source and proof audits.

## Fractional powers of geometric sums and sharp coefficient-segment bounds

Run `cd lean && lake env python3 ../scripts/verify_kovalev_zero_free.py` for the full registered 21-module closure. It freshly builds the sources with warnings as errors, audits all owned declarations including private ones, and replays the exact project closure with the pinned stock kernel. The [receipt](verification/lean-kovalev-zero-free-complete-20261124-162051/receipt.json) and [scope review](../docs/kovalev-fractional-taylor-sections/LEAN_REVIEW.md) cover the full original square-root conjecture. The general-exponent and segment supplements are not claimed. The scoped gate does not replace the aggregate repository command or certify public deployment.
## Thue–Morse valuation conjecture

The [Lean proof](../lean/Conjectures/ThueMorseValuation.lean) checks the original general clause’s disproof, the exponent-17 witness and the uniform family for k ≥ 11. The integer packing certificate is checked by ordinary kernel reduction. The [local receipt](../docs/verification/lean-thue-morse-valuation-publication-20261124/receipt.json) records source hashes, the complete owned/private axiom audit and stock-kernel replay.

From the repository root, build and replay the exact local closure with the pinned toolchain.

```sh
cd lean
lake build Conjectures.ThueMorseValuation
lake env python3 ../scripts/replay_lean.py --root Conjectures.ThueMorseValuation
```

## Hartke–Stolee–West–Yancey matching-excess conjecture

The complete 22-module closure passed fresh strict source builds, the all-owned/private audit (505 declarations, 435 theorems, 32 private declarations, 42 required endpoints), and exact stock-kernel replay. The [receipt](verification/lean-hartke-matching-excess-complete-20261124-162051/receipt.json), [statement correspondence](../results/hartke-stolee-west-yancey-matching-excess/FORMALIZATION.md), and [independent review](../results/hartke-stolee-west-yancey-matching-excess/LEAN_REVIEW.md) bind the checks to the original all-count tail-minimum conjecture. Only the three allowed standard axioms occur. The portable command is `cd lean && lake env python3 ../scripts/verify_hartke_matching_excess.py`; the dedicated workflow preserves its result separately. The aggregate dependency-artifact and public-site obligations remain tracked in [#563](https://github.com/1337isnot1337/solved-conjectures/issues/563).

## First short-proof Lean batch

- Lean proves Question 4.8, all six parts of Question 4.13 under the stated normalization, and the sharp two-generator thresholds. [Wilf-module proof and replay](../results/almiron-moyano-wilf-module-questions/LEAN.md).
- [Cardon et al.](../results/cardon-zero-sector/LEAN.md): exact negative answer to Question 6.1.
- [Chappelon–Ramírez Alfonsín–Stamate](../results/chappelon-ramirez-stamate-leaf-type/LEAN.md): exact disproof of Conjecture 4.4.

The [scoped verification receipt](verification/first-short-proof-lean-batch.md) records the pinned compiler, all-owned axiom audit, and stock kernel replay. The original conjecture disproofs do not certify the stronger written supplements.

## Benfield–Lippard’s stable Waring-gap symmetry conjecture

The seven-module source closure of `Conjectures.WaringGapSymmetry` passed strict compilation, all-owned axiom audit (335 declarations, 248 theorems, 108 private declarations, 14 required endpoints), and stock-kernel replay at `1229c35ae49d53008b91239b105c2dd15fdde6af`. The [result-level receipt](../results/benfield-lippard-waring-gap-symmetry/LEAN.md) records the source hashes and exact conjecture scope. Reproduce using `python3 scripts/verify_lean_target.py --root Conjectures.WaringGapSymmetry --require WaringGapSymmetryCore.not_conjecture10_1 --require WaringGapSymmetryCore.not_reflection_conjecture --out .candidate-artifacts/waring-gap-symmetry`. Package-wide verification is separate.

## The separable derangement limit

Partial. Lean verifies the displacement shift under arbitrary finite
direct and skew sums, an exact decomposition of their diagonal
fibers, and the strict separation of distinct child displacement
intervals at skew nodes. It also checks the same-diagonal ancestor
property, the finite spine-record counts, the critical offspring and
spine weights, the exact Schröder enumeration, and the conditional transfer from hit records to the
finite-instance probabilities.
[Lean scope and receipt](../results/separable-derangements-limit/FORMALIZATION.md).
