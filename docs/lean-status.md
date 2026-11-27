# Lean verification status

## Tree reconstruction after long subdivisions

The subdivision and repeated-branch theorems have written proofs and executable finite checks. They have no registered Lean formalization. [Mathematical scope and evidence](research-results/stanley-tree-subdivisions/README.md)

## Cioba–Savvas shutout number conjecture

Complete for the exponential shutout-number bounds in Conjectures 3.2 and 3.3 of Cioba–Savvas (2015). Lean proves for arbitrary finite simple graphs that Breaker prevents an immediate $s$-shutout whenever $s \ge 2$, $D = \Delta(G) \ge 1$, and $2^{1-s} \le D^D / (D+1)^{D+1}$, and via Bernoulli's inequality deduces $\sigma(s) \ge \tau(s) > 2^{s-3}$ for every $s \ge 3$ and $\sigma(s) \ge 2^s / 8$ for every $s \ge 1$. The four-module closure passed strict compilation, the complete 288-declaration all-owned axiom audit (241 theorems, 54 private declarations), and stock-kernel replay. [Lean scope and receipt](../results/cioba-savvas-shutout-number/FORMALIZATION.md).

## Universal Gaussian cold spots of dual type A

The all-rank theorem, its equality cases and its positive Hessian have a reviewed written proof. No Lean formalization is registered. [Statement and verification scope](research-results/dual-a-universal-cold-spots/README.md)

## Gaussian cold spots of high-rank type-A root lattices

The all-positive-scale theorem in sufficiently high ranks and the two dimension-independent endpoint intervals have an internally reviewed written proof, finite exact comparisons, and no Lean formalization. [Scope and checks](research-results/root-a-high-rank-cold-spots/README.md)

## Leech lattice cold-spot limit

**Lean status:** none. The written proof establishes the limiting deep-hole type. A Python verifier checks the coefficient comparison over all 23 types. [Proof and verification scope](research-results/leech-cold-spots-asymptotics/README.md)

The mixed-hole stability criterion and the local $`A_{24}`$ expansion have written proofs and no Lean formalization. Rational enumeration verifies the two Leech coefficients. [Supplement and checks](research-results/leech-cold-spots-asymptotics/MIXED-HOLES-REVIEW.md)

## Pattern packing and four-cycle partial results

The [packing cutoff construction](../results/blitvic-kammoun-steingrimsson-packing-cutoff/) and [four-cycle regularity obstructions](../results/erdos-85-four-cycle-threshold/) have written proofs and exact checks. No formalization is registered for either package.

## Book domination roots and monophonic circulants

Both [all-orders classifications](research-results/README.md#all-orders-graph-classifications) have written proofs and executable checks. Neither manuscript has a registered formalization.

## Bollobás–Erdős–Tuza conjecture

The [transversal bounds](../results/erdos-611-clique-transversals/) have written proofs and exact finite checks. The unrestricted conjecture remains open. No formalization is registered for these bounds.

## Written partial results on eleven open problems

The eleven notes on finite designs, set mappings, independence ratios, convex subsets, blocking sets, odd cycles, hypergraph colorings, Steiner sails, projective rigidity and normed spaces have written proofs. Their landing pages report `none` for formalization. The [partial-results catalogue](../CONTENTS.md#partial-results-on-open-problems) gives each statement, and the [verification record](verification.md#written-results-on-eleven-open-problems) identifies the five executable checks.

## Wang–Yang's Fuss–Narayana conjecture

Complete for all six matrices of Conjecture 4.1 at every integer parameter `m ≥ 2` and every finite minor on arbitrary strictly increasing row and column selections. Lean proves total nonnegativity for `[B(n, k)]`, `[A(n, k)]`, `[B(n, n - k)]`, and `[A(n, n - k)]`, and strict total positivity for `[B(n + k, k)]` and `[A(n + k, k)]`, proving Krattenthaler's product determinant (Lemma 3), Cauchy–Binet, the column STP criterion, the triangular flag-minor test, and Galvin–Pacurar Theorem 1.2 from scratch. The five-module closure passed strict compilation, the complete 322-declaration all-owned axiom audit (270 theorems, 79 private declarations), and stock-kernel replay. [Lean scope and receipt](../results/wang-yang-fuss-narayana/FORMALIZATION.md).

## Circular-index certificates within the package memory limit

The finite circular-index certificates for degrees 49, 50, 51, 53, 55 and 59 now verify their vertex tables in groups of sixteen. All six modules passed the normal Lake build under the configured 4.5 GB limit. The joint finite, stored-graph and all-degree proof suites also passed strict compilation, full axiom audit and stock-kernel replay twice. [Finite certificates](../results/circular-index-complete-minus-edges/FORMALIZATION.md) · [Stored insertions](../results/circular-index-upper-half-circulants/FORMALIZATION.md) · [All degrees](../results/circular-index-upper-half-remaining-deltas/FORMALIZATION.md).


## Burstein’s A218225 enumeration conjecture

Complete for the two outstanding avoidance classes `X = Av(2134, 42153, 24153)` and `Y = Av(2143, 42135, 24135)`. Lean proves literal equinumerosity `countX n = countY n` for every `n : ℕ` (including `n = 0`) and proves that their common nonempty generating series `P ∈ PowerSeries ℤ` is the unique zero-constant-term solution to `P = (1 + P)(x + (1 - x)P^2)`. The six-module closure passed strict compilation, the complete 815-declaration owned axiom audit, and stock-kernel replay. [Lean scope and receipt](../results/burstein-a218225-enumeration/FORMALIZATION.md).


## Pomerance–Sárközy’s fluctuation conjecture

The two headline arithmetic declarations give the quarter-root Gaussian
law for the literal counting function and its square-root convergence in
probability. The written proof uses the probability limit to obtain a
single density-one set and also gives the second-moment asymptotic.
[Lean scope](../results/pomerance-sarkozy-fluctuations/FORMALIZATION.md#headline-arithmetic-limits).


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

## Seven upper-half circular chromatic index certificates

Lean verifies the seven graphs and the combined existence result for every maximum degree from eight. Six of the seven exact indices are known from the certificates. The degree-15 graph has a strict upper-half interval. [Graph bounds and all-degree theorem](../results/circular-index-upper-half-remaining-deltas/FORMALIZATION.md).

## Revised Tan–Zhou conjecture

The [Lean formalization](../results/revised-tan-zhou-luroth/FORMALIZATION.md) proves the exact Hausdorff dimension for every positive nonincreasing approximation function bounded by one. The proof checks the literal unreduced denominators, the cylinder upper bound, and the lower bound by a Hölder decoding of nested target intervals. The eleven-module closure passed strict compilation, the complete owned-declaration axiom audit, and stock-kernel replay. See the [local receipt](../results/revised-tan-zhou-luroth/verification/receipt.json).


## Nuttall's conjecture

Complete for Conjecture 1, §4.5. Lean proves strict sign-reverse regularity on every ordered nonnegative grid through any prescribed finite order for all sufficiently high literal cumulants, and proves existence of the least cumulant order. [Lean scope](../results/nuttall-cumulants/FORMALIZATION.md).

## Németh–Seberry–Shu conjecture

Partial. Lean verifies exact-cardinality biased Fourier supports, binary circulant spectra, prime-order permanent congruence, and the conditional dense-row counting reduction. The uniform permanent asymptotic, within-row separation, and quadratic refinement are written only. [Lean scope](../results/nemeth-seberry-shu/FORMALIZATION.md).

## Burstein’s descent-top shape-Wilf conjecture

Complete disproofs of the original Conjectures 16 and 17 with the same traversable Ferrers board and suffix 1. The stronger every-suffix construction is written only. [Lean scope](../results/burstein-descent-top-shape-wilf/FORMALIZATION.md).

## Benfield–Lippard’s stable Waring-gap parity conjecture

Complete for original Conjecture 10.4 for every exponent at least two. Both the largest positive stable exception and the total number of positive stable exceptions are odd; the stronger congruences are written only. [Lean scope](../results/benfield-lippard-waring-gap-parity/FORMALIZATION.md).

## Ćurgus–Mascioni’s Fréchet root-matching extremizer question

Pinned strict build, 50-owned-declaration audit, eight endpoints and stock replay passed for the nonuniqueness counterexample. [Lean scope](../results/curgus-mascioni-frechet/FORMALIZATION.md).

## Ferroni–Morales–Panova’s cylindric Ehrhart-positivity conjecture

Strict compilation, a 256-owned-declaration/14-endpoint axiom audit, and stock replay passed for the two relaxed-seam unpinned conventions. The group entry stays partial. [Lean scope](../results/fmp-cylindric/FORMALIZATION.md).

## Csordas–Vishnyakova conjecture

Lean 4.35.0 strict build, 49-owned-declaration/9-endpoint axiom audit, and stock replay passed. [Lean scope](../results/csordas-vishnyakova/FORMALIZATION.md) · [Exact receipt](../results/csordas-vishnyakova/verification/lean-receipt.json).

## Ma–Tang’s random subset-sum threshold conjecture

Lean 4.35.0 passed the 32-module strict build, 1,514-declaration owned-axiom audit, and 32 stock replays. The original target and equation (1) are checked, not the separate bounded-error supplement. [Lean scope](../results/ma-tang-random-subset-sums/FORMALIZATION.md) · [Exact receipt](../results/ma-tang-random-subset-sums/verification/limsup-receipt.json).

## Gravgaard–Lee’s Lüroth diameter question

The [Lean formalization](../results/gravgaard-lee-diameter-condition/FORMALIZATION.md) proves the exact positive sum hull for arbitrary finite lower digit bounds of total diameter at least one, including equality. It also proves necessity of this threshold for modulo-one coverage. The eight-module closure passed strict compilation, the complete owned-declaration axiom audit, and stock-kernel replay. See the [local receipt](../results/gravgaard-lee-diameter-condition/verification/receipt.json).

## Ulas’s disjoint-block square-product conjecture

The [Lean formalization](../results/ulas-disjoint-square-blocks/FORMALIZATION.md) proves the original Conjecture 4 for every common length at least five and the stronger common-length theorem for every positive length. The nine-module source closure passed strict compilation, the complete owned-declaration axiom audit, and stock-kernel replay. The bounded mixed-length supplement remains unformalized. See the [local receipt](../results/ulas-disjoint-square-blocks/verification/receipt.json).

## Braun–Bruegge’s minimum facet conjecture

Lean proves both global minimum clauses of Conjecture 2 for the actual facets of the symmetric edge polytope. It establishes the exact even and odd formulas and the equality criterion up to graph isomorphism. The scoped gate passed for 19 modules, all 433 owned declarations and 30 required endpoints, followed by pinned kernel replay. The matching-number refinement remains a written supplement. [Lean scope](../results/braun-bruegge-minimum-facets/FORMALIZATION.md) · [Verification receipt](verification/lean-braun-bruegge-complete-20261124/receipt.json)

## Feldheim–Feldheim’s weighted tail conjecture

Complete for original Conjecture 1, with every positive weight below one, arbitrary distinct laws and atoms. The terminal theorem uses literal noncompact almost-sure support and an actual infinite limsup. Twenty fresh strict modules, the complete audit of 179 declarations and all thirty required endpoints, and exact stock-kernel replay passed. The higher-dimensional norm and finite-threshold supplements remain unformalized. [Scope](../results/feldheim-weighted-tail/FORMALIZATION.md) · [Independent review](../results/feldheim-weighted-tail/LEAN_REVIEW.md) · [Receipt](../results/feldheim-weighted-tail/verification/receipt.json).

## Hajdu–Sárközy’s shifted-product total primitivity conjecture

The [complete Lean formalization](../results/hajdu-sarkozy-shifted-products/FORMALIZATION.md) proves the original conjecture for every exponent pair at least two and every finite modification. It also proves every nonzero-shift two-variable symmetric-difference perturbation at the inverse minimum-exponent scale, and the full summable-family theorem with actual real-threshold counts and a positive retained-count limsup. Coefficient representations may overlap, and the candidate factor sets may be infinite.

The twenty-four-module closure, comprising thirteen new modules and eleven unchanged dependencies, passed strict builds, the complete all-owned/private axiom audit, and exact stock-kernel replay. All fifty-three required endpoints are checked, and only the three standard axioms occur. The [independent review](../results/hajdu-sarkozy-shifted-products/LEAN_REVIEW.md), [proof receipt](../results/hajdu-sarkozy-shifted-products/verification/receipt.json), and [publication binding](../results/hajdu-sarkozy-shifted-products/verification/publication-binding.json) distinguish the proof gate from metadata-only registration checks. The optional extension to more than two variables is not separately formalized. Existing credits, priority uncertainty, and catalogue rank are retained; reused dependencies and corollaries are not additional results.

## Fractional powers of geometric sums and sharp coefficient-segment bounds

The original Conjecture 1.2 is complete, with every positive geometric-polynomial length and every section degree proved. The literal Taylor coefficients use iterated complex derivatives. Actual beta measures, their transport identity, the finite-section integral identity, and every closed-disk boundary point are included. Twenty-one fresh strict modules, the complete all-owned/private axiom audit, and exact stock-kernel replay passed; only the three standard logical axioms occur. [Scope](../docs/kovalev-fractional-taylor-sections/FORMALIZATION.md) · [Statement review](../docs/kovalev-fractional-taylor-sections/LEAN_REVIEW.md) · [Receipt](verification/lean-kovalev-zero-free-complete-20261124-162051/receipt.json).

The recorded fractional-exponent and sharp-segment supplements remain unformalized. One original conjecture is counted; individual lengths and degrees are not separate results. The repository-wide cache/hosted/deployment follow-up is [issue #563](https://github.com/1337isnot1337/solved-conjectures/issues/563).

## Gravgaard–Lee’s mixed upper/lower Lüroth conjecture

Complete for original Conjecture 2.6 and the stronger exact interval equality, for every k≥2. Lean constructs actual infinite expansions, proves the finite zero-tail repair, and includes the threshold-two boundary. The [scope report](../results/gravgaard-lee-upper-lower-luroth/FORMALIZATION.md) and [independent review](../results/gravgaard-lee-upper-lower-luroth/LEAN_REVIEW.md) record the correspondence. The [complete receipt](verification/lean-gravgaard-lee-upper-lower-complete-20261124-162051/receipt.json) covers 12 strict source builds, 664 declarations, 475 theorems, 173 private declarations, 29 required endpoints, and exact stock replay. Only the three allowed standard axioms occur. Aggregate verification and public deployment remain separate in [#563](https://github.com/1337isnot1337/solved-conjectures/issues/563). The two reused previously completed Lüroth modules are not recounted. The mixed bounded-digit dependency retains its original proof already published through [PR #547](https://github.com/1337isnot1337/solved-conjectures/pull/547).

## Coulangeon–Lazzarini’s two-shell conjecture

[Lean refutes Conjecture 21 in dimension ten](../lean/Conjectures/CoulangeonLazzariniRealLattice.lean).
It verifies the full-rank discrete lattice in real space, identifies its first two
positive squared norms as 4 and 8, and checks the two spherical moment
identities and the failure at squared norm 9. The [integer-coordinate proof](../lean/Conjectures/CoulangeonLazzariniShells.lean)
also verifies the arbitrary-delay parity-lattice family.
The orthogonally indecomposable family and height results remain open in Lean.

## Gravgaard–Lee’s mixed Lüroth sumset

[Lean proves Conjecture 2.2 and the interval from the written proof](../lean/Conjectures/GravgaardLeeMixedLuroth.lean).
The sum of the digit sets bounded above by three and four contains $[2879/3520,2]$
and represents every real residue modulo one. The proof checks the fifteen
branch containments and the geometric approximation argument for the closed
sumsets of infinite Lüroth expansions. The two-module local import closure
passed the pinned kernel replay.

## Gravgaard–Lee’s large-digit Lüroth sumset

[Lean proves Conjecture 2.12 and the stronger interval in the written proof](../lean/Conjectures/GravgaardLeeLargeLuroth.lean).
For every integer $k\ge2$, the sum of the large-digit Lüroth set with itself contains
$(0,1/(k-1)]$. The witnesses have strictly increasing interleaved digits.
The development verifies both the convergence of the source's series and the half-open
digit intervals. See `conjecture_2_12`, `interval_subset_sum` and `interleaved_decomposition`.

## Hajdu–Sárközy’s shifted-power perturbation conjecture

The [complete Lean formalization](../results/hajdu-sarkozy-shifted-power-perturbations/FORMALIZATION.md) proves the original conjecture for every exponent at least two and the stronger nonzero-shift symmetric-difference theorem. The actual real-threshold error is little-o of the root scale; arbitrary nontrivial positive-integer product decompositions are excluded after every finite modification. The original root-zero convention is included.

The eleven-module closure passed strict compilation, the all-owned/private transitive axiom audit, and exact stock-kernel replay. The audit covers 185 declarations, 157 theorems, and twenty required endpoints, allowing only `propext`, `Classical.choice`, and `Quot.sound`. The [independent review](../results/hajdu-sarkozy-shifted-power-perturbations/LEAN_REVIEW.md) checks the exact source statement, the full argument and the frozen verification evidence. The [portable receipt](../results/hajdu-sarkozy-shifted-power-perturbations/verification/receipt.json) is distinct from the retained lane and interrupted-run records. The optional weaker-hypothesis retained-limsup supplement remains unformalized. Existing proposer/proof-author credits and bounded priority uncertainty are retained; this is one existing conjecture entry.

## Parking-function excedance certificate

Lean proves the marked counting recurrence and its bijection with actual parking words, identifies the exact length-17 coefficient row, and proves the existence of a nonreal root. [Lean scope](../results/alexandersson-parking-excedance/FORMALIZATION.md)

## Steinke–Zakynthinou’s agnostic VC learning conjecture

The companion paper's Conjecture 4.18 uses distribution-free information on fixed paired supersamples. Its two guarantees hold for every positive sample size by [the Lean theorem](../lean/Conjectures/AgnosticVC/FixedPairing.lean). The COLT bounty version uses conditional mutual information for iid data. [Companion paper, Definition 1.1 and Conjecture 4.18](https://arxiv.org/pdf/2001.09122v3)

Lean proves the two guarantees for a single proper learner. The original CMI is at most $`19{,}712d`$ nats, and the expected empirical excess on every sample is at most $`583\sqrt{d/n}`$. The [fixed-pairing theorem](../lean/Conjectures/AgnosticVC/FixedPairing.lean) bounds every deterministic paired pool for arbitrary hypothesis sets. The population theorem specifies measurability of its chosen representatives and discharges this assumption for countable measurable classes, countable instance domains with measurable singletons, and classes ordered with a countable initial segment of measurable predictors realizing every finite trace. A separate theorem requires only almost-everywhere measurability of the pool information to obtain the iid bound. [Theorem](../lean/Conjectures/AgnosticVC/Theorem.lean) · [Verification receipt](../results/steinke-zakynthinou-agnostic-vc/verification.json)

The negative statements are also formalized. The [global Borel disproof](../lean/Conjectures/AgnosticVC/BorelChoiceObstruction.lean) has standard Borel spaces and Borel finite-trace tests. The [completed-iid disproof](../lean/Conjectures/AgnosticVC/CompletedFiniteGroups.lean) defeats every candidate constant with a VC-one class of finite supports. Measurability of the scalar expected empirical loss under one completed iid law suffices for the disproof. The [written analysis](https://github.com/1337isnot1337/solved-conjectures/blob/research/research/steinke-zakynthinou-agnostic-vc/completed-finite-groups.md) proves class-by-class distribution-uniform convergence in outer probability and quantifies its sample-size dependence. The general standard Borel completed-iid conjecture remains open in this repository.

The [local reconstruction theorem](../lean/Conjectures/AgnosticVC/LocalReconstructionMeasurable.lean) proves the actual iid CMI bound $`197{,}120d+32k`$ nats for classes with measurable proper reconstructions from at most $`k`$ rows. It retains the empirical rate and covers the [circle-orbit example](../lean/Conjectures/AgnosticVC/OrbitIidRates.lean) with $`k=1`$.

For a single VC-one class of disjoint two-point supports, Lean verifies that the empirical rate is impossible when the scalar expected loss must be universally measurable. The [verified uniform-deviation envelope](../lean/Conjectures/AgnosticVC/FiniteSupportUniform.lean) has expectation at most $`2/\sqrt n+2/n`$ for that class under every iid law. A [written learner](https://github.com/1337isnot1337/solved-conjectures/blob/research/research/steinke-zakynthinou-agnostic-vc/completed-disjoint-support-learner.md) proves both rates for the same class with measurability on each completed iid law.

The [integer-noise learner](../lean/Conjectures/AgnosticVC/NoisySupportIid.lean) gives actual iid CMI at most $`20s`$ nats and all-sample expected empirical excess at most $`m/n+8/\sqrt n`$ for bounded support size $`m`$ and overlap $`s`$. The [sharp-deviation extension](../lean/Conjectures/AgnosticVC/NoisySupportSharpIid.lean) removes the support-size restriction given a sharp outer uniform-convergence bound. A positive-outer-mass event of too many hits on a null support would violate that bound under a reweighted iid law.

The [conditional joint-law disproof](../lean/Conjectures/AgnosticVC/ConditionalJointObstruction.lean) derives the literal finite-support obstruction from measurability of the actual conditional selector/output kernel used for iid CMI. Lean also verifies the version with conditional laws on an ambient standard Borel code space, where the proper subclass has the trace Borel sigma-algebra. The [repeated-feature lemmas](../lean/Conjectures/AgnosticVC/RepeatedFeatureReadout.lean) verify a measurable version for any repeated-feature readout and an almost-sure hit bound for every null finite support.

The [seeded-pool disproof](../lean/Conjectures/AgnosticVC/ConditionalJointObstruction.lean) assumes completed measurability only of the actual ambient output on the iid pool, fair selector and independent seed, along with ordinary seed expectations on every fixed sample. It derives the empirical-loss contradiction directly from those random variables.

The [fair-label disproof](../lean/Conjectures/AgnosticVC/FairLabelObstruction.lean) forces iid CMI at least $`n/32`$ for tolerance at most $`1/8`$, allowing improper outputs. Lean verifies the benchmark, population and empirical loss estimates, and the contradiction for every candidate constant, with the published generalization inequality as an explicit premise.

## Steinke–Zakynthinou threshold theorem

[Lean proves the proper real-threshold case of Conjecture 6](../lean/Conjectures/SteinkeZakynthinou.lean). For every positive sample size the same measurable learner works for every iid labeled distribution and every fixed sample. Its outputs are finite closed thresholds. Lean bounds original paired-pool CMI by 300 nats or 600 bits and expected empirical excess by $`512/\sqrt n`$, including arbitrary ties and label noise. The source statement in bits with the infimum over all thresholds is `SteinkeZakynthinou.properThresholdTheorem_bits`. The written proof supplies sharper information constants and separate efficiency and determinism extensions. All 28 modules in the Lean theorem’s project import closure passed the pinned kernel replay. The standalone audit checked 806 declarations against the standard axiom whitelist.

Gröchenig’s upper-density result is excluded after a [checked earlier resolution](https://github.com/1337isnot1337/solved-conjectures/tree/research/research/bounty-continuation-2026-11-21/grochenig-prior-resolution/). Its independent proof and verification receipts remain in [immutable Git history](https://github.com/1337isnot1337/solved-conjectures/blob/628270dc5e07d7924de265d2ac1beee4b5634b80/docs/verification/lean-grochenig-20261121/receipt.json). The reused KVZ results remain active.

The shared package is in [`lean`](../lean/).
It uses Lean **4.35.0** and Mathlib commit
`56a005855ea17e0b0958f73ec801ae140b0a1679`, as pinned in the existing manifest.
The campaign has incorporated the source collection and layout through commit
`daad0edf918f12cd57f6b30d3f16b28e7a12d2c5`. Earlier receipts below retain their
original checked scope.

Unregistered proofs and their separate hosted checks are tracked in
[`lean-candidates.md`](lean-candidates.md). Their presence in the repository
does not expand the accepted scope in the table below.

At candidate snapshot `75df6294`, the six-speed classification-to-bound
adapter passed its 21-module closure and 284-theorem axiom audit. The
hyperplane residue and endpoint-component closures also passed, covering
26 modules/463 theorems and 29 modules/490 theorems respectively. Each job
rebuilt sources, checked the standard axiom whitelist, independently replayed
every project kernel object, and confirmed unchanged sources. These older receipts retain their original scope; the table below records
subsequent registrations. In particular, the adapter retains its five-speed
bound and primitive six-speed classification hypotheses. Exact job links and
scopes are in [`loneliness-75df-component-receipts.json`](loneliness-75df-component-receipts.json).

A complete formalization here means that Lean checks the mathematical conclusion
from the definitions in the indicated files. The correspondence between those
definitions and an external publication remains subject to mathematical review.
Published mathematical theorems that have not been formalized are hypotheses,
never additional Lean axioms.

The README uses ✅ for complete formalization of the stated result, 🟢 for
partial formalization with a computer-assisted proof, 🟡 for partial
formalization, and ⬜ when a result has no Lean verification. Essential computer-assisted
proofs are documented separately in the catalogue and result package.

| Note | Status | Checked scope and remaining gap |
| --- | --- | --- |
| Nuttall's conjecture | Complete | Literal cumulants are strictly sign-reverse regular on all ordered nonnegative grids through any prescribed finite order for all sufficiently large cumulant indices; the least index exists. |
| Coffey–Smith conjecture | Not formalized | Complete proposed unconditional disproof of Smith’s named conjunction: if RH holds the dyadic coefficient square mass is O(N^(-1/2) log³ N), so both proposed positive-fraction sets have density zero for 0<ε<1/4; without RH the polynomial upper bound fails. The weaker Coffey upper-bound assertion alone is not refuted. Internally reviewed; no Lean verification. |
| Chaudhary–Khmiri–Mazhouda conjecture | Not formalized | Complete proposed computer-assisted disproof of the universal automorphic Li-coefficient monotonicity claim. The admissible GL1 imaginary norm twist L(s+8i,χ₋₃) has Re(λ(2)−λ(1))<−3/2, certified by rational interval bounds. No GRH assumption. Internally reviewed; no Lean verification. |
| Merlini–Sala–Sala conjecture | Not formalized | Complete proposed unconditional refutation of the logarithmic and all-ε subpower growth conjecture for the tiny Li term: limsup $`\lvert\lambda_{\mathrm{tiny}}(n)\rvert/n^{1/4}=\infty`$. The authors’ weaker linear stability conjecture is not resolved. Internally reviewed; no Lean verification. |
| Zeng’s unscaled interlacing question | Not formalized | Consecutive unscaled two-parameter Narayana rows have strictly interlacing negative roots throughout the source domain, with the stronger multiplicative gap $q^2$. [Written proof](../results/zeng-unscaled-interlacing/proof.md) · [Exact check](../results/zeng-unscaled-interlacing/check.py) |
| Alexandersson’s graphical dist conjecture | Partial | Lean verifies the 71-vertex graph and its 310 edges, the triangle insertion law, exactly two nonreal roots of the computed coefficient polynomial, and every limiting root for each positive even order. The full orientation-count identity and convergence to the graph family remain in the written proof. [Formal scope and receipt](../results/alexandersson-graphical-dist/FORMALIZATION.md). |
| Alexandersson’s transportation polytope conjecture | Complete | Lean proves the full-support counterexample and the square-root-logarithmic growth of nonreal roots, counted with multiplicity, for the Ehrhart numerators of the actual lattice polytopes. [Lean theorems and verification receipt](../results/alexandersson-transportation/FORMALIZATION.md). |
| Wang–Yang's Fuss–Narayana conjecture | Complete | All six matrices of Conjecture 4.1 for every integer parameter `m ≥ 2` and every finite minor: TN for `[B(n, k)]`, `[A(n, k)]`, `[B(n, n - k)]`, `[A(n, n - k)]`, and STP for `[B(n + k, k)]`, `[A(n + k, k)]`, including self-contained Lean proofs of Krattenthaler Lemma 3, Cauchy–Binet, and Galvin–Pacurar Theorem 1.2. Five-module strict build, 322-declaration all-owned axiom audit (270 theorems), and stock-kernel replay passed. [Lean scope and receipt](../results/wang-yang-fuss-narayana/FORMALIZATION.md). |
| Wang–Yang's conjecture | Not formalized | Complete proposed disproof of the author-manuscript Conjecture 1.10: for every fixed coefficient index, the signed forward differences of the Xi coefficients have infinitely many values of each strict sign. Final journal wording has not been checked; the adjacent logarithmic conjecture is separate. Internally reviewed; no Lean verification. |
| Pantone–Bóna’s asymptotic conjecture | Not formalized | Full written asymptotic argument with explicit leading constant, checked canonical decomposition and exact independent small counts. |
| Pantone–Bóna’s second-largest-terminal asymptotic conjecture | Partial | Lean verifies the literal four-pattern class, its canonical split by a unique marker gap, the binomial interleaving count, and the block-deletion lemma for tableau walks. The exact leading amplitude follows in Lean from explicit counting and gap estimates. [Lean scope](../results/pantone-bona-second-largest-terminal/FORMALIZATION.md) |
| Pantone–Bóna’s third-largest-terminal asymptotic conjecture | Not formalized | All-order proof with explicit leading constant. Supplementary exact counts do not enter the proof. |
| Pantone–Bóna’s second-smallest-terminal asymptotic conjecture | Not formalized | All-order proof with explicit leading constant. Supplementary exact counts do not enter the proof. |
| Hartke–Stolee–West–Yancey matching-excess conjecture | Complete | Original Conjecture 9.15 for actual finite simple graphs, with exact extremal stabilization and quantitative bounds for both constants and tail minima. All 22 strict sources, the all-owned/private audit and exact stock replay passed. [Scope](../results/hartke-stolee-west-yancey-matching-excess/FORMALIZATION.md) · [Receipt](verification/lean-hartke-matching-excess-complete-20261124-162051/receipt.json). |
| Chappelon–Ramírez Alfonsín–Stamate’s leaf-type conjecture | Complete: original Conjecture 4.4 refuted | Lean verifies the genus-66 leaf of type 33 using actual numerical-semigroup leaf and pseudo-Frobenius definitions. The separate family and sharp asymptotic remain written only. [Scope and source](../results/chappelon-ramirez-stamate-leaf-type/LEAN.md). |
| Feldheim–Feldheim’s weighted tail conjecture | Complete original Conjecture 1 | Every positive weight below one and arbitrary independent nonnegative noncompact laws, including atoms; literal infinite limsup. Norm and finite-threshold supplements remain unformalized. [Scope](../results/feldheim-weighted-tail/FORMALIZATION.md) · [Receipt](../results/feldheim-weighted-tail/verification/receipt.json). |
| Hajdu–Sárközy’s shifted-power perturbation conjecture | Complete original conjecture and general-shift symmetric-difference theorem | All exponents at least two, actual little-o counts, arbitrary nontrivial positive factor sets, and every finite modification. Eleven modules passed strict compilation, complete declaration/axiom audit, and stock replay. The weaker retained-limsup supplement remains unformalized. [Scope](../results/hajdu-sarkozy-shifted-power-perturbations/FORMALIZATION.md). |
| Hajdu–Sárközy’s shifted-product total primitivity conjecture | Complete original conjecture, summable-family theorem and two-variable perturbations | Every exponent pair, every nonzero shift, actual real-threshold counts and every finite modification. Twenty-four modules passed strict compilation, complete axiom audit and stock replay; thirteen modules are new. The optional extension to more than two variables is not separately formalized. [Scope](../results/hajdu-sarkozy-shifted-products/FORMALIZATION.md). |
| Hegyvári’s conjecture | Not formalized | Proves strong completeness of the two-ray set across the remaining rational ratios that are not powers of two, with exact strong-completeness obstructions. |
| Ma–Tang’s random subset-sum threshold conjecture | Complete for the original conjecture | Exact real-log limsup, the written third-log correction and convergence on the mixed orders. The separate bounded-remainder refinements remain unformalized. [Lean scope](../results/ma-tang-random-subset-sums/FORMALIZATION.md) · [Exact receipt](../results/ma-tang-random-subset-sums/verification/limsup-receipt.json). |
| Féray’s conjugate-power word-measure conjectures | Not formalized | Proves both cycle limits and total-variation mixing for the stated permutation word, with sharp distance asymptotic e⁻¹/(n−1). |
| Barrett–Evans–Hall–Kempton’s spectrally extreme graph conjecture | Not formalized | [Full proof](../results/barrett-evans-hall-kempton-se/PROOF.md) uses exact finite certificates for small simple endpoint graphs and analytic reduction to arbitrary real weights. |
| Xu–Zhou’s diameter–Laplacian conjecture | Complete for Conjecture 1.1 | Lean proves the original all-parameter bound for the actual connected simple graph and the closed interval, with eigenvalue multiplicity. It also proves attainment for unbounded `c` using `4*t+1` layers and `t` doubled layers. [Lean scope](../results/xu-zhou-laplacian-diameter/FORMALIZATION.md). |
| Han’s simultaneous spherical-harmonic saturation question | Not formalized | Constructs one real orthonormal basis per degree attaining both sharp Lᵖ growth regimes for every basis vector simultaneously. |
| Steinerberger’s small-average eigenfunction norm question | Not formalized | Refutes the proposed near-linear lower bound and constructs real spherical bases with optimal aggregate and per-mode L¹ sizes. |
| Pomerance–Sárközy’s fluctuation conjecture | Partial | The quarter-root Gaussian law and the square-root convergence in probability hold for the original count on the full uniform sample. The written proof supplies the single density-one set and the second-moment asymptotic. [Lean scope](../results/pomerance-sarkozy-fluctuations/FORMALIZATION.md#headline-arithmetic-limits). |
| Ulas’s disjoint-block square-product conjecture | Complete | Original Conjecture 4 and the stronger common-length theorem at every positive length. The nine-module strict build, owned-declaration axiom audit, and kernel replay passed. [Scope](../results/ulas-disjoint-square-blocks/FORMALIZATION.md) · [Receipt](../results/ulas-disjoint-square-blocks/verification/receipt.json). |
| Kovalev’s linear Lipschitz clustering questions | Not formalized | Constructs convex-hull-preserving finite-subset retractions with a dimension-free linear Lipschitz bound, uniformly for every target size. |
| Revised Tan–Zhou conjecture | Complete | Exact Hausdorff dimension with unreduced Lüroth denominators and every lower order, including zero and infinity. Strict compilation, all-owned axiom audit, and stock-kernel replay passed. [Lean formalization](../results/revised-tan-zhou-luroth/FORMALIZATION.md) · [local receipt](../results/revised-tan-zhou-luroth/verification/receipt.json). |
| Simmons–Weiss’s Hausdorff-measure question | Not formalized | Proves natural-Hausdorff-almost-sure non-bad approximation after every irrational translate of a bounded continued-fraction Cantor set. |
| Gravgaard–Lee’s mixed Lüroth sumset conjecture | Complete | Proves that the mixed bounded-digit Lüroth sum represents every residue modulo one, with an explicit ordinary interval in the sum. |
| Gravgaard–Lee’s large-digit Lüroth sumset conjecture | Complete | Gives a positive-length ordinary sum interval for every lower digit threshold, using two expansions whose combined digits strictly increase. |
| Gravgaard–Lee’s Lüroth diameter question | Complete | Exact positive sum hull for actual infinite expansions and the exact threshold for coverage modulo one. The strict build, owned-declaration axiom audit, and stock-kernel replay passed. [Lean formalization](../results/gravgaard-lee-diameter-condition/FORMALIZATION.md) · [local receipt](../results/gravgaard-lee-diameter-condition/verification/receipt.json). |
| Gravgaard–Lee’s mixed upper/lower Lüroth conjecture | Complete | Exact interval equality and original modulo-one conclusion for every k≥2, with actual infinite upper/lower expansions. All 12 strict sources, the complete axiom audit and exact stock replay passed. [Scope](../results/gravgaard-lee-upper-lower-luroth/FORMALIZATION.md) · [Receipt](verification/lean-gravgaard-lee-upper-lower-complete-20261124-162051/receipt.json). |
| Dougherty-Bliss–Galván–Polley–Shuster’s separable derangement conjecture | Partial | Lean checks the actual direct and skew displacement shifts, diagonal fiber counts, and the separation of distinct children at skew nodes. Lean constructs the alternating tree permutations and verifies the finite spine-record counts. Lean checks the exact tree enumeration, critical weights, and conditional transfer from finite record probabilities. The asymptotic and almost-sure hit arguments remain. [Scope and receipt](../results/separable-derangements-limit/FORMALIZATION.md). |
| Dougherty-Bliss–Galván–Polley–Shuster’s separable derangement asymptotic conjecture | Not formalized | Refutes every proposed fixed power exponent by exact finite two-branch counting and saturation of the occupation loss. |
| Fan’s interval Riesz capacity-ratio conjecture | Not formalized | Proves the full negative-exponent conjecture and the nontrivial one-dimensional Clark–Laugesen range, with equality conditions. |
| McNamara–Steingrímsson’s interval rank-unimodality conjecture | Complete | Original Conjecture 9.4, with the exact three literal rank counts and strict dip. [Lean proof and receipt](../results/mcnamara-steingrimsson-rank-unimodality/FORMALIZATION.md). |
| Shumyatsky’s conjugate prime-spectrum conjecture | Partial | Lean proves the exact finite-group statement under four explicit finite-simple-group automorphism and generation inputs. It checks the abelian and nonabelian reductions, actual factor actions, local lifts under those hypotheses, and Gaschütz’s lifting lemma. [Scope and receipts](../results/shumyatsky-conjugate-prime-spectrum/FORMALIZATION.md). |
| Elizalde–Rivera–Zhuang’s big-descent Schur-positivity conjecture | Not formalized | The [all-degree written proof](../results/erz-big-descent-schur/PROOF.md) includes the exact longest-increasing-subsequence refinement. Two [exact checkers](../results/erz-big-descent-schur/AUDIT.md) accompany the proof. |
| Chern–Fu–Lin’s joint Eulerian equidistribution conjecture | Not formalized | Proves the joint descent and inverse-descent equidistribution of Conjecture 6.2 at every length by exact formal generating functions. |
| Dukes’s revstack interlacing conjecture | Partial | Lean proves the literal Eulerian enumeration for every order at least three and the first strict root interlacing transition. The uniform root estimates remain in the written proof. [Lean scope](../results/dukes-revstack/FORMALIZATION.md). |
| Claesson–Dukes–Steingrímsson’s stack-sorting conjecture | Partial formalization | The [computer-assisted proof](../results/claesson-dukes-steingrimsson-stack-sorting/PROOF.md) covers every order at least eight. The [replay](../results/claesson-dukes-steingrimsson-stack-sorting/verify.ps1) regenerates the finite coefficient table and checks the exact polynomial identity and the small orders. The [Lean checkpoint](claesson-formalization.md) verifies the definitions, the ten-row polynomial identity and the exact-depth equivalence; the marked-order enumeration and the filtered-prefix principle remain explicit hypotheses. |
| Almirón–Moyano-Fernández’s Wilf-module questions | Complete | Lean proves the threshold-two counterexample family, all six normalized module clauses, the gap-antichain classification and the exact thresholds over every two-generated semigroup. [Scope and receipt](../results/almiron-moyano-wilf-module-questions/LEAN.md). |
| Defant–Engen–Miller’s Lassalle refinement conjecture | Partial | Lean checks all 53 base rows, the eventual interval and error bounds, and the Bessel root bracket. The exact permutation conjecture follows conditionally on the count bridge and classical Bessel product data. [Lean scope](../results/defant-engen-miller-lassalle/FORMALIZATION.md). |
| Sagan–Wilson’s plactic centralizer conjecture | Not formalized | Proves eventual stability of all plactic centralizers of powers, with an alphabet-only cutoff independent of word length. |
| Sagan–Wilson’s plactic coefficient-mode conjecture | Partial | Lean disproves Conjecture 7.3(d) from the insertion tableaux of actual centralizing words. For length ten the fifth and sixth binomial coefficients are 75,095 and 88,704. The asymptotic mode theorem remains in the written proof. [Lean scope](../results/sagan-wilson-plactic-mode/FORMALIZATION.md) |
| Juhnke’s arbitrary-step lattice-path log-concavity conjecture | Complete | Log-concavity and unimodality of the literal original path counts for every dimension `d ≥ 2` and every step count. All 18 modules passed strict compilation, the all-owned audit (577 declarations, 502 theorems), and stock-kernel replay. [Scope and receipt](../results/juhnke-lattice-paths/LEAN-AUDIT.md). |
| Athanasiadis–Chapoton’s polar preorder duality conjecture | Complete | Lean proves Conjecture 6.2 for every finite preorder. The actual polar dilates have equivalent lattice-point sets, hence equal Ehrhart series and numerators. The real transfer is a positively homogeneous homeomorphism. [Lean scope](../results/athanasiadis-chapoton-polar-duality/FORMALIZATION.md) |
| Gawron–Miska–Ulas’s Thue–Morse valuation conjecture | Complete | Lean proves the literal disproof of Conjecture 5.2 using exponent 17 and verifies the aligned family for every k ≥ 11. All three modules passed strict compilation, the all-owned axiom audit and stock-kernel replay. [Lean](../lean/Conjectures/ThueMorseValuation.lean) · [Local receipt](../docs/verification/lean-thue-morse-valuation-20261124/receipt.json). |
| Sobolewski–Ulas’s binary-partition exception regularity conjecture | Partial | Lean proves the exact source-layer power-of-two obstruction, all actual partition congruences, and inclusion in the exception set. The converse of Legendre’s criterion and the Cobham–Durand implication remain external. [Lean scope](../results/sobolewski-ulas-exception-regularity/FORMALIZATION.md). |
| Gawron–Ulas’s partition-sign nonperiodicity conjecture | Complete for the original conjecture | Lean proves non-eventual periodicity of the signs for parts congruent to 1 modulo 3. The stronger sign assertions on every index progression and for other part moduli remain in the written proof. [Lean scope and receipt](../results/gawron-ulas-partition-signs/FORMALIZATION.md). |
| Steinerberger’s greedy-energy Fourier conjecture | Complete | An actual infinite van der Corput sequence satisfies the greedy rule and violates every eventual logarithmic bound for the stated weighted absolute Fourier sum. Four modules, complete owned/private axiom audit and stock-kernel replay; sharp-constant and all-tie-breaking supplements remain unformalized. |
| Ćurgus–Mascioni’s Fréchet root-matching extremizer question | Partial: nonuniqueness counterexample | Every quadratic has a matching of cost at most one and a continuum of pairwise inequivalent quadratics attain it. General attainment and the cubic comparison are not formalized. [Lean scope](../results/curgus-mascioni-frechet/FORMALIZATION.md). |
| Chern–Fu–Lin’s three-statistic equidistribution conjecture | Complete | For every length and prescribed set of left-to-right minimum positions, Lean equates the fibres of the right-to-left maximum count and inverse descent count on the two literal classes. [Theorem and verification](../results/chern-fu-lin-three-statistic/FORMALIZATION.md). |
| Gawron–Miska–Ulas’s Thue–Morse sign-density conjecture | Complete disproof of original Conjecture 5.8 | Stabilized coefficients of the actual infinite formal product, nonvanishing, signed-block identities, both cardinality bounds for every finite prefix, infinitude and nonzero lower density. Strict compilation, all-owned audit (250 declarations, 212 theorems, 119 private declarations), and independent replay of all three modules passed. The stronger exact-density theorem is separate. [Scope and receipt](../results/gawron-miska-ulas-thue-morse-sign-density/LEAN.md). |
| Fan–Tringali’s power-monoid length-set conjecture | Complete original 2018 conjecture | Both power monoids of every Dedekind-finite monoid with infinitely many distinct positive powers, and the exact reduced natural-number system. All 18 modules passed strict source builds, the complete declaration/axiom audit and stock kernel replay. Survey irreducibles, multiplicities and relative cancellativity remain unformalized. [Scope](../results/fan-tringali-power-monoid-lengths/LEAN.md). |
| Sokal’s Apéry moment threshold | Partial | Lean excludes every parameter with 0 < x ≤ 1/40 and an open neighborhood of one quarter. It checks the moment continuation and the lower-endpoint obstruction under the torus transform identity. The identity and the saddle cusp remain unformalized. [Lean scope](../results/sokal-apery-moment-threshold/FORMALIZATION.md) |
| Gessel–Zhuang’s pinnacle-set gamma-positivity conjecture | Complete | Conjectures 7.3 and 7.2 for all positive sizes, pinnacle sets, and peak counts, using literal permutations and inverse descents. The full history bijection, root preservation, symmetry, and nonnegative gamma expansion are proved. The 25-module closure passed strict compilation, the all-owned audit (641 declarations, 479 theorems), and stock-kernel replay. Conjecture 7.1 remains separate. [Statement audit and receipt](../results/gessel-zhuang-pinnacle-gamma/LEAN-AUDIT.md). |
| Burstein’s descent-top shape-Wilf conjecture | Complete | Both original conjectures fail on one valid Ferrers board with suffix 1. The stronger every-suffix construction is written only. |
| Burstein’s A218225 enumeration conjecture | Complete | Both previously unresolved avoidance classes `X = Av(2134, 42153, 24153)` and `Y = Av(2143, 42135, 24135)` are proved literally equinumerous for every `n : ℕ`, with common nonempty generating series uniquely satisfying `P = (1 + P)(x + (1 - x)P^2)`. Six-module strict build, 815-declaration all-owned axiom audit, and stock-kernel replay passed. [Lean scope and receipt](../results/burstein-a218225-enumeration/FORMALIZATION.md). |
| Steinerberger’s quantitative Feldheim-tail conjecture | Complete for both original conjectures | The actual absolutely continuous unbounded nonnegative law violates both proposed ratio bounds for every positive threshold, with its actual expectation and median. All four modules passed strict compilation, the audit of 103 owned declarations (92 theorems), and stock-kernel replay. The smoothing, all-parameter, strict log-concavity, and rate supplements remain unformalized. [Scope and receipt](../results/steinerberger-feldheim-tail/LEAN-AUDIT.md). |
| Benfield–Lippard’s stable Waring-gap symmetry conjecture | Complete for original Conjecture 10.1 and intended reflection formulation 10.2 | At both exponents 64 and 128, the proof identifies the entire stable exception set, its largest element and a duplicate-free finite list of all members, and proves strict symmetry defect. Seven-module strict build, all-owned audit (335 declarations, 248 theorems, 108 private declarations) and independent kernel replay passed. Exact numerical genus supplement remains separate. [Scope and receipt](../results/benfield-lippard-waring-gap-symmetry/LEAN.md). |
| Benfield–Lippard’s stable Waring-gap parity conjecture | Complete | Both parities in Conjecture 10.4 for every exponent at least two. Stronger two-adic congruences are written only. |
| Heim–Neuhauser–Tröger’s plane-partition polynomial Turán conjecture | Complete | Lean proves strict Turán for every real parameter at least 1 and every index at least 12. The finite coefficient check ends at 250 and the uniform Fourier proof starts at 251. [Lean scope](../results/heim-neuhauser-troeger-plane-partition-turan/FORMALIZATION.md). |
| Heim–Neuhauser’s plane-partition polynomization conjecture | Complete | Lean proves strict consecutive-root decrease for every positive index when the parameter exceeds 5 and from index 6 for every real parameter at least 1. At index 1 the threshold 5 is sharp. [Lean scope](../results/heim-neuhauser-plane-partition-polynomization/FORMALIZATION.md). |
| Heim–Neuhauser’s ordinary D’Arcais root conjecture | Partial | Lean proves the root comparison for indices 6–50 at every real parameter at least one. It constructs the unique positive saddle, proves Fourier inversion for the ordinary coefficients, and reduces strict log-concavity at every index from 501 onward to two explicit inequalities. [Lean scope](../results/heim-neuhauser-ordinary-darcais-root/FORMALIZATION.md) |
| Charlton et al.’s distinct D’Arcais zeros question | Not formalized | Infinitely many distinct right-half-plane zero values via scaled entire limits, with the inverse-index scale on a positive-density family. Prior non-Hurwitz theorem credited. |
| Lángi–Wang’s disk-average question for convex tilings | Not formalized | Written proofs of the disk-average bounds and logarithmic-density theorem. A floating-point check covers one stage of the construction. [Scope](../results/langi-wang-convex-tiling/) |
| Bétermin’s FCC/BCC cold-spot conjecture | Not formalized | All-scale analytic proof with full equality cases and correction of the printed BCC coordinate. Numerical diagnostic not used in the proof. |
| Meylender–Thalmaier’s truncated-square conjecture | Partial | Lean proves the exact Lebesgue areas and maximal four-shape covering scales of the parallelogram and rational pentagon, and the strict comparisons with the source’s trapezoid formula. The first comparison also holds near the boundary for every first truncation leg. Identifying this scale with symplectic capacity and proving the full strict bound for every convex body remain open in Lean. [Scope and receipt](../results/meylender-thalmaier-truncated-square/FORMALIZATION.md). |
| Rossi’s permutohedron characteristic-polynomial conjecture | Complete for Conjecture 6.16 | Lean proves the all-length original equivalent rank enumerator, counting every ordered face, and the exact positive characteristic root split for Rossi’s signed face sum. The q-deformation and a separate re-proof of the evaluated Möbius formula are outside scope. [Proof and receipt](../results/rossi-permutohedron-roots/FORMALIZATION.md). |
| Ferroni–Higashitani’s first-three interior Ehrhart question | Complete for Question 5.12(a) | The actual dimension-170 IDP lattice polytope has strict failure at the three negative evaluations of its unique Ehrhart polynomial. [Lean scope](../results/ferroni-higashitani-early-interior-ehrhart/FORMALIZATION.md). |
| Ferroni–Morales–Panova’s cylindric Ehrhart-positivity conjecture | Partial: relaxed-seam counterexamples | Both unpinned vertical-edge conventions contradict positivity. Standard-boundary positivity remains written only. [Lean scope](../results/fmp-cylindric/FORMALIZATION.md). |
| Braun–Bruegge’s bicyclic facet conjectures | Complete | Lean proves the geometric facet maximum for every bicyclic order at least four, and the exact theta optimizer for every order at least ten, including uniqueness up to permuting paths. [Formalization and receipt](../results/braun-bruegge-bicyclic-facets/FORMALIZATION.md). |
| Braun–Bruegge’s minimum facet conjecture | Complete for Conjecture 2(3)–(4) | Actual geometric facets, exact even and odd minimum counts, attainment and uniqueness up to graph isomorphism. The 19-module scoped build, all-owned axiom audit and pinned replay passed. The fixed-matching-number refinement remains a written supplement. [Lean scope](../results/braun-bruegge-minimum-facets/FORMALIZATION.md) |
| Cyrusian–Kaplan’s ordinarization quasipolynomial question | Complete | Lean proves exact degree `2r` in every residue on all positive genera and eventual strict increase for each fixed positive ordinarization number. [Scope and receipts](../results/cyrusian-kaplan-ordinarization/FORMALIZATION.md). |
| Coulangeon–Lazzarini’s two-shell conjecture | Complete | The real dimension-ten counterexample and the elementary arbitrary-delay family. Orthogonal indecomposability and height extensions remain open in Lean. |
| Alexandersson’s parking-function excedance conjecture | Complete | Lean proves the marked counting recurrence and its bijection with actual parking words, identifies the exact length-17 coefficient row, and proves the existence of a nonreal root. [Lean scope](../results/alexandersson-parking-excedance/FORMALIZATION.md) |
| Tom–Vailaya’s weighted trace conjecture | Partial | Lean verifies the finite-color trace under literal endpoint closure with directed arc multiplicity, loop vanishing, the matrix product for endpoint gluing, the edge transfer, independence of the weighted path test rows, the path action, symbolic color-basis invertibility, the conditional trace comparison, and endpoint reflection. The general forest-triple matrix identification remains written. [Lean scope](../results/tom-vailaya-weighted-trace/FORMALIZATION.md). |
| Csordas–Vishnyakova conjecture | Complete | Original Conjecture 3.6, including all real arguments and all Taylor orders, with the actual approximation definition. [Lean scope](../results/csordas-vishnyakova/FORMALIZATION.md) · [Exact receipt](../results/csordas-vishnyakova/verification/lean-receipt.json). |
| Cardon–Forgács–Piotrowski–Sorensen–White conjecture | Complete: Question 6.1 and uniform small-damping obstruction | Lean checks the exact cubic at p = 3 and proves failure throughout a small positive-damping interval for each real p > 2. [Scope and source](../results/cardon-zero-sector/LEAN.md). |
| Brown–Cameron’s independence-root sector and stability problems | Not formalized | The [written proof](../results/brown-cameron-stability/PROOF.md) gives limsup lower bounds for right-half-plane roots and failure of log-concavity. The [exact checks](../results/brown-cameron-stability/REVIEW.md#reproducible-checks) are corroboration, not part of the proof. |
| Byrne–Tait’s odd-length Sidon-set question | Not formalized | The [written proof](../results/byrne-tait-odd-sidon/PROOF.md) establishes the uniform density gap for every odd length. The [finite examples](../results/byrne-tait-odd-sidon/verify.py) test normal and nonnormal subgroups. |
| Nathanson’s linear-form Sidon systems conjecture | Complete | Lean proves all three original questions, the lower bound from the two largest absolute coefficients, the finite upper bound with the common coefficient divisor, and the exact bilinear limit for every choice of nonzero signed coefficients. [Lean scope](../results/nathanson-sidon-systems/FORMALIZATION.md). |
| Fiscus–Hurlbert–Myzelev–Pence grid conjecture | Complete | Lean proves that Player 1 wins on the 14-vertex ladder, verifies all 16,384 positions and identifies all four winning openings. [Lean scope](../results/fiscus-grid-game/FORMALIZATION.md). |
| En Gad–Yaakobi–Jiang–Bruck constant-weight strong WOM coding problem | Not formalized | The [written proof](../results/constant-weight-strong-wom/PROOF.md) proves the capacity and polynomial complexity guarantees. A [reference implementation](../results/constant-weight-strong-wom/verify.py) checks exact-weight encoding and recovery. |
| The Steiner triple system sail problem | Complete | Lean proves the uniform count, existence from order 84, the limiting lower density of 1/49, the one-color disjoint packing with limiting lower rate 1/4802, and the fixed disjoint-union Ramsey consequence. [Lean theorems and verification receipt](../results/steiner-triple-system-sail/FORMALIZATION.md). |
| Fractional general position conjecture for square grids | Not formalized | The [written proof](../results/fractional-general-position-square-grids/PROOF.md) constructs the exact minimum fractional geodesic cover for every square grid. [Exact checker](../results/fractional-general-position-square-grids/verify.py). |
| Erdős’s one-third pinned-distance conjecture | Not formalized | Written proofs give the mean one-third gap under either no three collinear or no four cocircular. [First proof](../results/erdos-general-position-pinned-distances/PROOF.md) · [Arbitrary-collinearity proof](../results/erdos-general-position-pinned-distances/ARBITRARY-COLLINEARITIES.md) · [Review and finite checks](../results/erdos-general-position-pinned-distances/UNRESTRICTED-REVIEW.md). |
| Cioba–Savvas shutout number conjecture | Complete for Conjectures 3.2 and 3.3 | Lean proves the exponential degree lower bounds for the immediate shutout and free-star games over arbitrary finite simple graphs. [Scope and replay](../results/cioba-savvas-shutout-number/FORMALIZATION.md). |
| Mobile general position complexity | Not formalized | The [written proof](../results/mobile-general-position-complexity/PROOF.md) gives PSPACE-completeness for ordinary, fixed-start, and completely mobile thresholds at diameter two. [Exact move checker](../results/mobile-general-position-complexity/verify.py). |
| Misère Domination Game | Not formalized | The [written proof](../results/misere-domination-game/PROOF.md) gives exact congruences for paths and cycles and solves impartial misère octal 0.337. [Independent game checker](../results/misere-domination-game/verify.py). |
| Plambeck–Siegel infinite quotient conjecture for 0.3312 | Not formalized | [Written transfer proof](../results/plambeck-siegel-03312/PROOF.md) and [exact recurrence certificate](../results/plambeck-siegel-03312/verify.py) prove infinitude. |
| Liang’s 0.3123 slice problem | Not formalized | [Written transfer proof](../results/liang-03123-slice/PROOF.md) and [exact certificate](../results/liang-03123-slice/verify.py) solve Open Problem 6.2. |
| Liang’s slice-period conjecture | Not formalized | [Exact transfer proof](../results/liang-slice-period/PROOF.md) and [certificate](../results/liang-slice-period/check.py) refute Conjecture 4.3 with an unbounded family. |
| Builder–Blocker general position complexity conjecture | Not formalized | The [written proof](../results/builder-blocker-general-position-complexity/PROOF.md) establishes PSPACE-completeness for both starters at diameter two. [Exact minimax checker](../results/builder-blocker-general-position-complexity/verify.py). |
| Permutation digraph general position conjecture | Not formalized | The [written proof](../results/permutation-digraph-general-position/PROOF.md) refutes equality on the entire stated parameter range. [Directed-distance checker](../results/permutation-digraph-general-position/verify.py). |
| General position number of oriented trees | Not formalized | The [written proof](../results/general-position-oriented-trees/PROOF.md) gives a chain-partition formula and a linear-time recurrence. [Independent checker](../results/general-position-oriented-trees/verify.py). |
| Chandran–Di Stefano–Haritha–Thomas–Tuite general-position conjecture | Not formalized | The [written proof](../results/general-position-nordhaus-gaddum/PROOF.md) establishes both general-position clauses in every order. An [exact regression checker](../results/general-position-nordhaus-gaddum/verify.py) tests the constructed partition in the original metric. |
| The lower oriented general position NP-hardness conjecture | Not formalized | The [written proof](../results/lower-oriented-general-position-np-hardness/PROOF.md) establishes NP-completeness, including for planar bipartite two-leaf graphs cubic elsewhere. [Exact checker](../results/lower-oriented-general-position-np-hardness/verify.py). |
| Oriented general position spectrum nonconstancy conjecture | Not formalized | The [written proof](../results/oriented-general-position-spectrum-nonconstancy/PROOF.md) gives two separating orientations for every graph with a vertex of degree at least two. [Executable regression](../results/oriented-general-position-spectrum-nonconstancy/verify.py) tests the witnesses. |
| Welton–Khudairi–Tuite lower general position product conjecture | Not formalized | The [written proof](../results/welton-khudairi-tuite-lower-gp-product/PROOF.md) gives an infinite family with unbounded factor lower general position numbers and a six-vertex maximal set in the product. The [exact regression](../results/welton-khudairi-tuite-lower-gp-product/verify.py) checks the construction by shortest paths. |
| Chandran–Di Stefano–Haritha–Thomas–Tuite monophonic product conjecture | Partial | Lean verifies the 45-vertex counterexample, the exact color counts 20 and 27, and the complement count for every prism length. The original graph’s all-order color formula remains in the written proof. [Formal proof and verification receipt](../results/monophonic-product-nordhaus-gaddum/FORMALIZATION.md). |
| Mallik–Diwan–Kothari degree-count conjecture | Complete | Lean constructs a minimal extendable bipartite counterexample for every stated even order and verifies its exact edge and degree counts. Explicit permutations identify the original 16-vertex search witness with the smallest family member. [Lean theorems and verification receipt](../results/mallik-diwan-kothari-degree-count/FORMALIZATION.md). |
| Asgarli–Ghioca–Yip blocking-pencil problem | Complete for the stated pencil and all-graph bounds | Lean proves `regularOrderingEstimate`, `missing_lines` and `pencil_bounds` with no geometric hypothesis. [Scope and replay](../results/asgarli-ghioca-yip-blocking-pencil/FORMALIZATION.md). |
| Erdős–Gyárfás point-degree spectrum conjecture | Complete | Lean bounds the degree spectrum in every finite linear space, rules out the proposed square-root deficit and proves the same linear bound for real planar point sets. [Lean scope](../results/erdos-gyarfas-point-degree-spectrum/FORMALIZATION.md). |
| Gyárfás’s planar degree-repetition problem | Complete | For every order from 16, Lean constructs noncollinear rational points in the real plane, proves optimal maximum degree multiplicity two and determines the entire interval of distinct degrees. [Lean scope](../results/gyarfas-planar-degree-repetition/FORMALIZATION.md). |
| Ferroni–Pagaria–Vecchi’s type B real-rootedness conjecture | Not formalized | The [written proof](../results/ferroni-pagaria-vecchi-type-b/PROOF.md) proves Conjecture 4.13 at every rank and strict consecutive-rank interlacing. The exact rational checks validate the algebra and normalized source slice; no Lean code is claimed. |
| Caiolo–Ferroni–Hoster conjecture | Complete | For every prime power q ≥ 17, Lean constructs the simple rank-five matroid, counts its flat flags, and proves both dual polynomials fail to split over the reals. The quartic is positive on the real line; the quintic has the single simple real root −1. [Theorem](../lean/Conjectures/CaioloFerroniHoster.lean) · [Review and replay](../results/caiolo-ferroni-hoster/LEAN_REVIEW.md) · Supplement: dual Chow real-rootedness holds exactly in ranks at most four ([theorem](../lean/Conjectures/CaioloFerroniHosterRanks.lean), [scope](../results/caiolo-ferroni-hoster/RANKS.md)) |
| Higashitani–Kummer–Michałek conjecture | Complete for Conjecture 4.10 | Lean constructs the unique literal Ehrhart polynomial for the six-pair witness, establishes every natural-dilation count and the degree bound, and proves an off-line root. The independent Wronskian certificate and the stronger interlacing witness remain written. [Lean scope](../results/hkm-ehrhart/FORMALIZATION.md). |
| Steinke–Zakynthinou’s agnostic VC learning conjecture | Partial | Lean verifies the fixed-pool rate and empirical accuracy. The iid information and measurable learner results retain the hypotheses in the [scope audit](../results/steinke-zakynthinou-agnostic-vc/SCOPE.md). |
| Steinke–Zakynthinou agnostic threshold problem | Complete | Lean proves the proper real-threshold prize statement, including measurability, original CMI for arbitrary iid labeled distributions, and empirical accuracy on every fixed sample. The exact source bounds follow with the common constant 1024. The [scope review](../results/steinke-zakynthinou-thresholds/LEAN_REVIEW.md) checks the constant-zero comparator, the Borel Markov kernel, and the KL of the selector and the actual cutoff. |
| Johnson's conjecture | Complete | The original finite-tuple statement holds for every even order, every positive nonincreasing log-convex kernel, and every perfect matching. The general circular interval-product theorem is also unconditional. All thirty project modules passed strict compilation, the all-owned audit (1,195 declarations, 1,006 theorems), and stock-kernel replay. [Statement audit and receipt](../results/johnson-pfaffian/LEAN-AUDIT.md). |
| Brown–Mol's conjecture | Complete | Lean proves the explicit 1001-vertex counterexample and that all sufficiently large members of the literal tree family have diameter four and a nonzero subtree root in the forbidden disk. It counts actual connected induced vertex sets and establishes the infinite family through local analytic inverses and logarithmic derivatives. Strict standalone compilation, all-owned axiom audit and stock-kernel replay passed; the combined repository gate is pending. |
| Ekhad–Zeilberger’s most unfair bet conjecture | Partial | Lean verifies the exact finite covariance identity and the unrestricted normalized overlap-score maximum with all equality cases. The winning-probability asymptotics and the full-alphabet restriction have a reviewed written proof. [Lean scope](../results/ekhad-zeilberger-unfair-bet/FORMALIZATION.md) · [Written review](../results/ekhad-zeilberger-unfair-bet/REVIEW.md). |
| Kauers–Koutschan recurrence conjecture | Complete | Lean proves Conjecture 10 for the actual A189281 permutation count and the published order-eight operator at every natural index. Lean also proves the order-thirteen supplement for that same count at every index. [Scope and receipts](../results/kauers-koutschan-recurrence/FORMALIZATION.md). |
| Kovalev's conjecture | Partial | Lean proves the pointwise transfer inequality, the dimension threshold, the fourth-moment calculation and the exact rational separation. The Gaussian expectations and spherical Hardy-norm identities remain to be formalized. [Lean scope and receipt](../results/kovalev-hardy-duality/FORMALIZATION.md). |
| Roos–Seiringer's conjecture | Not formalized | Complete proposed computer-assisted proof of the full radial Dirichlet kernel assertion. Analytic tails and an essential exact certificate over 184 closed intervals cover the entire positive real axis; source scaling covers all positive chemical potentials. Two independent mathematical/code reviews, a separate priority audit and full replays passed. The unaveraged kernel is outside the claim. No Lean formalization is claimed. |
| Dospolova–Germanskov–Zaporozhets's conjecture | Partial | Lean checks the positive factorial family, exact ultra-log-concavity and scaled ratios, countable-limit step, and strict expected sample range for an actual Gaussian process under almost-sure boundedness and deterministic local-range-limit assumptions. Intrinsic volumes, determinism of those local limits, and Vitale's limiting theorem remain unformalized. Strict source compilation, isolated kernel replay and endpoint axiom checks passed; full repository gate pending. |
| Chen–Khare–Sahi's conjecture | Partial: literal source convention unresolved | At q=1/10, t=9/10, Lean proves the complete stable Hall family over all eleven degree-six partitions, literal power-sum coordinates and polynomial injectivity, unique monic dominance-triangular orthogonality, three-variable specialization, positive normalization, and full Muirhead-semiring nonmembership. The degree-three finite-Hall source conflict is formal. All 19 modules passed strict sources, complete owned/private audits and exact stock replay. Broader families remain eigenfunction-characterized; the separate earlier 16-module compatibility replay and the combined repository gate remain pending. |
| Chen–Khare–Sahi’s Jack semiring conjecture | Not formalized | Written counterexample to Conjecture 4 with two exact rational checks. The Jack witness and its parameter family have no Lean formalization. [Proof and review](../results/chen-khare-sahi-jack/REVIEW.md). |
| Ferreira–Simon's conjecture | Not formalized | Complete proposed analytic proof of the beta-prime self-convolution identity for its full real-parameter range. Two independent mathematical reviews and 18 supplementary exact formal-parameter checks passed. No Lean formalization is claimed. |
| Lyon's conjecture | Not formalized | Complete proposed computer-assisted proof for every positive real shape. Analytic tails and an essential exact integer certificate covering 4256 real intervals establish the derivative sign. Two independent mathematical/code reviews and full certificate replays passed. No Lean theorem or partial Lean credit is claimed. |
| Han–Sabag–Kostina–Hassibi's conjecture | Complete source formalization; merged-package gate pending | Lean proves the original matrix feasibility, rational witness, exact sparse infimum and all four individual assignment infima, plus the uniform gap throughout the stated open gain interval. Standalone strict source compilation, all-owned axiom audit and stock-kernel replay passed; the merged-package gate is pending. |
| López Pouso–Segura's node conjecture | Partial | Lean checks the two Legendre roots, standard weight formula, exact cubic quadrature, and the two failed inequalities; the degree-two polynomial and its derivative are connected to mathlib’s shifted Legendre polynomial. Strict source compilation, one-module kernel replay and endpoint axiom checks passed. Lean also verifies the explicit perturbation functions, derivatives, differential equations final coefficient algebra, and the deduction of the scaled limit and eventual violation from three separate factor approximations with vanishing second-order remainders. Controlled ODE and root asymptotics, the gamma-ratio expansion, those factor approximations and the full repository gate remain pending. |
| Vishnyakova's conjecture | Complete | Lean proves the original sampled-sequence and weighted transform-class theorems for every positive degree and weight. The proof uses all finite ordered Toeplitz minors and proves both centered disks and attained exact radii. All 17 modules passed strict sources, the complete axiom audit, and stock-kernel replay. |
| Novelli–Thibon's conjecture | Partial | Lean verifies the finite commutative monomial product, the actual Jacobi–Trudi/bialternant bridge, and the hook coefficients from an explicit stable ordinary Schur expansion. Existence and stability of that expansion are not independently formalized. [Scope and receipts](../results/novelli-thibon/FORMALIZATION.md). |
| López Pouso–Segura's conjectures | Partial | Lean proves all three signs, strict monotonicity and exact limits conditionally on the stated finite mixture, phase ODE, endpoint, zero/weight asymptotics and two resolvent expansions. It also proves the reference kernel integral and the dominated-convergence and comparison steps linking those inputs to the limits. The Bessel identification, special-function inputs, reference Euler–Maclaurin remainder and full repository gate remain open. |
| Simon's stable-infimum conjecture | Not formalized | Complete proposed proof of the full parameterwise convex order, including the Brownian endpoint. The independent review checks the prior Mellin transform, increasing logarithmic Lévy measures, exponential integrability and conditional Jensen argument. No numerical or finite-case inference is used. |
| Ferreira–Simon's stochastic-order conjecture | Not formalized | Complete proposed proof for every pair of real parameters in the source interval. The Poisson-series scale and strict sequence-norm comparison give a simultaneous coupling, both endpoint limits and the associated Mittag–Leffler inequalities. Independent internal review passed. |
| Ferreira–Simon's diagonal Mittag–Leffler conjecture | Partial | Lean proves strict monotonicity of the explicit Pollard density integral and checks termwise differentiation of the Mittag–Leffler series. The diagonal inequality follows under the local Pollard representation hypothesis. [Lean scope](../results/ferreira-simon-diagonal/FORMALIZATION.md) |
| McCrea's conjecture | Not formalized | Complete proposed proof of the unique linear-density crossover for every modulus at least three. Positive coefficient asymptotics handle the floor, and the exponent difference has exactly one zero in the stated interval. Independent internal review and exact profile-word diagnostics passed. |
| Chen–Kitaev–Zhang's record conjectures | Complete | Lean proves the original Conjectures 1 and 3 for actual separable-permutation classes and all four record statistics, with every stated length and singleton case. The credited source-pinned trureturing proof supplies the previously resolved Conjecture 2 tail and permutation decomposition; direct Pell certificates prove the remaining low-record comparisons. Strict standalone compilation, a 1,132-theorem axiom audit and isolated stock-kernel replay passed; the combined repository gate is pending. |
| Zhu's generalized Jacobi–Stirling conjecture | Complete source formalization; merged-package gate pending | Lean proves the original recurrence, the 3×3 determinant identity, the exact coefficient −4, the negation of coefficientwise positivity of all finite Hankel minors, and the stated counterexample region over every linearly ordered field. The standalone source passed strict compilation, an all-owned axiom audit, and stock-kernel replay. The combined repository gate has not yet passed for this registration. |
| Circulants with circular chromatic index in the upper half | Partial overall; main theorems and all stored positive examples complete | Lean proves the actual `4g`-regular and `4g`-connected graph with real circular index `4g+2/3` for every `g ≥ 2`, and the complete degree/connectivity/index statements for C25, C31 and C33. The real-colouring lower bound and atom/subgroup connectivity arguments are proved internally. Strict sources, an all-owned audit of 601 declarations/500 theorem declarations and 171 required endpoints, and exact stock-kernel replay passed. [Local receipt](verification/lean-named-20261121/circular-receipt.json). Lean also verifies all 17 nonregular positive examples in Section 7.3. The additional general structural and insertion lemmas and the complete set of Section 7.4 search exclusions remain outside these receipts. [Nonregular verification](../results/circular-index-upper-half-circulants/FORMALIZATION.md). |
| Graphs with circular chromatic index in the upper half for Δ ≡ 2 mod 4 | Complete | Lean proves Theorems 1 and 1′, Proposition 2 and Corollary 3, including every even maximum degree from 8 and every degree congruent to 1 modulo 4 from 21. It also verifies the base exclusions at parameters 3, 4 and 5. [Lean scope](../results/circular-index-upper-half-delta-2-mod-4/FORMALIZATION.md). |
| Graphs with circular chromatic index in the upper half for Δ ≡ 3 mod 4 | Complete | Lean proves Theorem A for every permitted packing, all nine graphs in Proposition B, Corollary C and the additional claims in Sections 3, 6 and 8. [Lean scope](../results/circular-index-upper-half-delta-3-mod-4/FORMALIZATION.md). |
| Malek's conjecture | Not formalized | Complete written all-degree negative-transform proof with all equality cases, two independent internal reviews and exact scalar identity checks. The permanent endpoint is prior work; the named subsidiary is documented in the Minc site's linked survey. No proof-assistant work is claimed. |
| Mazák–Zrubák conjecture on complete graphs minus an edge | Partial | The actual order, run rigidity, special columns, first-position labels and all assertions of Lemma 5 are verified. The boundary comparisons and final lower bound remain unverified in Lean. [Scope and receipt](../results/circular-index-complete-minus-edge/FORMALIZATION.md). |
| Circular chromatic index of complete graphs minus a few edges | Partial | Lean checks all 32 labelled colourings, including 14 exact indices, six strict upper-half examples and the counterexample on 11 vertices. The other exclusions and the general single-edge theorem are separate. [Lean scope](../results/circular-index-complete-minus-edges/FORMALIZATION.md). |
| Baricz–Pogány's asymptotic-coefficient positivity conjecture | Complete | Original factorial products, formal division, all-degree strict positivity and the explicit lower bound are proved. The source coefficient recurrence uniquely determines the same sequence; its inequality is now an explicit endpoint. Strict compilation, an all-owned audit of 65 declarations/55 theorem declarations and all seven required endpoints, and stock-kernel replay passed. [Local receipt](verification/lean-named-20261121/baricz-receipt.json); combined repository gate pending. Source-access and priority limits are unchanged. |
| Pula–Song–Wanless conjecture | Not formalized | Complete written proof of the all-parameter threshold, including its equality case and unique boundary minimizer. Real-rooted minor equalization and van der Waerden completion replace disputed dependencies. Exact identity checks supplement the proof. The full Minc Problems 14 and 15 remain outside its scope. |
| Perron root of permanental compounds | Not formalized | Written FPRAS proof for every nonnegative rational matrix and every compound degree, with deterministic zero detection. Exact finite checks supplement the argument. This is the randomized approximation formulation of Minc Problem 18; exact polynomial-time eigenvalue computation and the characteristic-polynomial problem are outside its scope. |
| Oravcová–Soták conjecture for five to eight distances | Partial | The formalization uses the actual distance graph on the integers. Its unconditional results include the greedy upper bound, periodic-word transport, loop concatenation, integer base change, the four unbounded one-parameter coloring families, the full two-parameter family, and the exceptional chromatic numbers. Theorem A, the Oravcová–Soták clique conclusion, and the primitive triangle-free corollary retain the explicitly named propositions `R5`, `R6`, `R7`, and `R8` as hypotheses. Those four real-loneliness classifications are not proved by this closure. All nine new modules passed strict compilation with warnings treated as errors. The exact 28-module project closure passed an all-owned audit of 1239 declarations (1084 theorem declarations and 40 required endpoints) and independent stock-kernel replay. Only `propext`, `Classical.choice`, and `Quot.sound` are permitted. [Receipt](verification/lean-named-20261121/oravcova-receipt.json). Combined package gate remains pending. |
| Johnson–Kaya–Matzke conjecture on Babai spectra of paths | Complete | Lean proves the exact spectrum interval for every `n ≥ 2` and `1 ≤ k < n`, using the actual `SimpleGraph.chromaticNumber` of the distance graph on `Fin n`. It proves the independence and coloring bounds, greedy coloring, and modular-coloring/clique realization of every allowed value. Strict compilation, an all-owned audit of 43 declarations/39 theorem declarations and all 12 required endpoints, and stock-kernel replay passed. No published input remains a hypothesis. [Local receipt](verification/lean-named-20261121/babai-receipt.json); the combined repository gate and hosted validation remain separate. |
| Ferreira–Simon's Wright log-concavity conjecture | Complete original-conjecture disproof | The actual infinite Wright series has a continuous beta-zero counterexample family, with admissible alpha approaching one. Strict compilation, the complete 25-declaration owned audit including eight private declarations, and independent stock-kernel replay passed. The positive-beta refinements in the written proof and the combined repository gate remain separate and pending. |
| Karp–Vishnyakova–Zhang's gamma-quotient conjecture | Complete | Lean proves the literal gamma quotient on every strictly ordered real grid with c>d and positive denominator arguments. Noninteger differences are strict at every order; integer m gives nonzero minors through order m+1 and zero larger minors. The exact signature and third-order correction are checked. All 15 modules passed strict sources, the complete owned/private audit, and stock-kernel replay. The combined repository gate remains pending. |
| Alexandersson's Fuss–Catalan conjecture | Complete | Lean proves the literal Fuss–Dyck enumeration and closed formula, real-rootedness, the exact simple-negative-root count, and scalar reduction to the ordinary case. It proves that any ordinary-case relation between root multisets transfers; the cited ordinary-case interlacing theorems themselves are not re-proved. Strict standalone compilation, all-owned axiom audit and isolated stock-kernel replay passed; the combined repository gate is pending. |
| Sagan–Swanson conjecture | Not formalized | Written proof of all four stated asymptotic normality assertions using actual means and variances; finite model checks are supplementary. |
| Bernardi–Morales's delta-process conjecture | Complete | Lean proves published Conjectures 27–28 for all admissible parameters: the literal delta-map tree count for every fixed color map, and the complete marked interval-event count and source probability determinant for every fixed surjection. Full subsets, singleton complements and the singular averaging case are included. The 13-module closure passed strict compilation with warnings treated as errors, an all-owned audit of 269 declarations (205 theorem declarations and 23 required endpoints), and independent replay by the pinned stock kernel. Only `propext`, `Classical.choice`, and `Quot.sound` are permitted. [Receipt](verification/lean-named-20261121/bernardi-receipt.json). Combined package gate and hosted validation remain separate. |
| Gilmore's crossing–nesting conjecture | Complete | Lean proves the full crossing–nesting identity for the stabilized product-defined matrix, with alignment and size refinements, over every commutative ring. Canonical matching lists enumerate exactly the literal perfect matchings; their weights count the actual crossing, nesting and alignment inequalities. Fresh strict compilation, the all-owned audit of 449 declarations (346 theorem declarations, including private declarations) and all 20 required endpoints, and stock-kernel replay passed. [Local receipt](verification/lean-named-20261121/gilmore-receipt.json). The combined repository gate and hosted validation are separate. |
| Currie's conjecture on complexity 2n+1 and critical exponent | Not formalized | Written proof for all twenty words of the journal and arXiv versions, computer-assisted in finitely many described places, after one independent model referee pass. The standard-library verifier checks the morphism identities, exact factor sets, the hypotheses of the insertion lemmas, the short bispecial factors and the exact inequalities in `Q(λ)` for the 72 families; brute-force cross-checks cover bounded lengths and prefixes. No proof-assistant formalization is claimed. |
| Dawkins–Nappo–Tong–Zimbizi wild-number conjecture for n ≥ 155 | Not formalized | Written proof for every `n >= 155` after one independent model referee pass per theorem; the conjecture remains open for `13 <= n <= 154`. The standard-library verifier rechecks the local-lemma and cluster-expansion conditions in exact rationals. |
| Strict consecutive interlacing of type-D Eulerian polynomials | Complete | For the ordinary, unweighted even-signed permutation enumerators, Lean proves weak interlacing from rank two and strict interlacing from rank three. The 11-module proof derives the refinement recurrence and root inequalities internally and passed strict compilation, the declaration audit and stock-kernel replay. The weighted extension has only a written proof. |
| Németh–Seberry–Shu conjecture | Partial | Exact Fourier support and spectra, congruence and counting reduction. The uniform permanent asymptotic and within-row separation remain written only. |
| Sonntag–Teichert conjecture | Complete source formalization; merged-package gate pending | Lean proves the tournament theorem, the forward classification of separated oriented-graph cases as two stars, and an explicit realization for every pair of stars with arbitrary additional isolated vertices. The standalone strict source check, all-owned axiom audit and stock-kernel replay passed; the combined repository gate is pending. |
| Horňák–Woźniak conjecture | Partial | Lean proves arbitrary vertex decomposability for tripods with a positive short arm of length at most two, conditional on source tests 1 and 5. For all positive short-arm lengths it proves partitions containing a larger part under those tests, realizes partitions with a sublist summing to the short arm unconditionally, and reduces the remainder to partitions with no mergeable noncentral pair. The general all-small case, four-arm reduction, existence constructions and combined gate remain. Strict compilation, a 958-theorem full-chain axiom audit and isolated kernel replay passed. |
| L-solitaire | Complete for both the counterexample and corrected theorem | Actual moves for arbitrary layer sets containing 1; all recurrent states; classification and maximality of stable references; one-column interlacing; the explicit uniform profile bound and convergence for every diverging scale. The separate fixed-scale counterexample remains checked. |
| Three-player War | Complete for all three explicit cycling deals | Distinct ranks and round-robin deal sizes; exact transition rules; returns after 90, 180, and 19,320 turns; no earlier positive return; all three players active at every nonnegative time. |
| Pham denominator degree | Complete | Both exact rational identities follow from actual Bulgarian-solitaire cycles and coefficientwise stabilization of their first-entry levels. The primitive period-10 words have reduced denominator degrees 5 and 10, with coprimality and minimality against every nonzero alternative denominator. No published rationality or degree-bound theorem is assumed. |
| Batista Egyptian fractions | Complete | An ordered lexicographically first solution uniquely maximizes the last denominator for every admissible positive `k` outside residue class 1. The proof uses the elementary global comparison and a kernel-reduced exhaustive certificate below 100, with proved denominator bounds; no published comparison theorem is a hypothesis. |
| CUT Family B | Complete | The actual well-founded mex games have identical values at every positive pile size iff `3x < y`, including infinite cut sets. The six-block base formula, preservation under all even cuts, and discrepancy by `4x` are proved internally. |
| CUT arithmetic periodicity | Complete | The uniform terminating decision test and exhaustive candidate enumeration are proved for every finite cut set and proposed arithmetic tail. Compact quotient/residue certificates identify both actual example games at every pile size and prove least eventual period 12, saltus 8, and earliest start 7, hence positive-pile preperiod 6. |
| Loneliness on a fixed hyperplane | Complete | Original ordered positive distinct sample; deterministic maximum and velocity bound; uniform O(1/N) error over all shifts; fixed and independent Haar-shift laws; exact finite-subspace and positive-N quasipolynomial counts with degree bound; full-support endpoint formula including k=2; sharp (1,2,3) example. The complete 72-module closure passed strict sources, all-owned/private audit and exact stock replay. |
| Graffiti.pc Conjecture 318 ([@JesterInABarrel](https://x.com/JesterInABarrel/status/2123233964827812334)) | Complete | The all-order theorem uses actual graph distances and undirected complement-edge counts. Every total dominating set contains an adjacent total dominating pair; every minimal set has size two. The stated five-vertex graph proves sharpness of a one-unit relaxation. |
| Hadamard order-2396 partial results | Partial overall; automorphism, fixed-border construction and symmetry, and length-598 obstruction complete | The full signed-automorphism group excludes order 479, with both norm proofs checked. The fixed-border common multiplier group is cyclic of order dividing four and every preserving subgroup leaves at least 151 sign orbits. On any finite abelian group with a subgroup of index four, the original four sign rows and raw correlation equations yield an actual bordered Hadamard matrix; normalization, the literal finite border, and all fourteen size-149 baseline patterns are proved. The length-598 order-eleven obstruction is complete. The actual two-row Hadamard construction and quotient transport are checked. For length 1197, the actual common multiplier order is proved to divide 27; exclusion of order 27 and the finite quotient/no-lift certificates remain candidates. |
| Lonely-runner two insertions | Complete | Every `p ≥ 3` and arbitrary positive integer speeds have a common witness in `[1/(p+2),1/p]` with clearance at least `1/(p+2)`. The unbounded branch, all small cases, interval-good base insertion, Goddyn–Wong acceleration criterion, common-dilation value bound, and literal three-insertion obstruction are proved. |
| Zhang's Question 8.4: deletion values of the lonely runner | Complete theorem; full gate pending | Lean proves the exact values in both ranges for every n≥3, 1≤r≤n−1, and the strict inequality for n≥4, using actual real distances and speeds. The small-deletion upper bound is proved internally via rational maximizers and the modular certificate; Liu's theorem is not assumed. The seven-module closure passed local kernel replay, and the theorem endpoints use only allowed axioms. Full repository gate pending. · [Current scoped replay](../results/zhang-deletion-values/FORMALIZATION.md). |
| Seven upper-half circular chromatic index certificates | Complete | Lean checks the seven literal examples and proves the combined upper-half existence theorem for every maximum degree from eight. At degree 15 it establishes the stated bracket. [Complete scope](../results/circular-index-upper-half-remaining-deltas/FORMALIZATION.md). |
| Zhang's Question 8.5 for 18 ≤ n ≤ 57: shifted lonely runner counterexamples | Complete for the published range | All 40 rational certificates attain their recorded maxima over all real times and give $\Gamma(n)<1/(n+1)$ for $18\le n\le57$. The remaining sizes 58–94 are open. [Lean proof and receipt](../results/shifted-lonely-runner-counterexamples/FORMALIZATION.md). |
| Erdős–Gyárfás abelian covers | Complete for the stated voltage-cover theorem and sharpness | Every seven-label voltage cover of the singly subdivided tetrahedron over every abelian group contains an actual simple cycle of length 4, 8, 16, or 32. The 64-node literal certificate, its collision-branch soundness, and voltage normalization are checked. The connected 95-vertex cyclic cover attains least power-of-two cycle length 32. The general minimum-degree-three conjecture is outside this result. |
| Li coefficient sign | Complete for the explicit counterexample | Full coefficients +29 and −6304, all 6,842 partition types, exact count eight, and `2^30` genuine connected partitions. All 44 source checks, 25 literal contracts, owned and raw-occurrence audits, and 44 exact stock replays passed. Alternative Python proof implementations remain outside this Lean scope. |
| Frankl generating families | Partial: both frequency bounds complete; cyclic span-four pending | The all-point high-girth bound is checked for every `k ≥ 3`: incidence girth at least 16 and exactly three generators through each point imply frequency at least `518208/1000000` among distinct unions. The `k ≥ 15` linear-family bound is also checked with frequency `657/1000`. Both include the empty union. The complete Vaughan shortcut, small-cycle cases, local checker semantics, and conditional all-period assembly are checked. The remaining cyclic span-four graph/transport certificates and unconditional assembly are still being verified. |
| Erdős 607 line sizes | Complete | Lean proves the exact realizability and geometric counting identity for every natural point count, the coefficientwise and analytic generating functions, Fourier extraction, the actual finite-product limit and domination, and the sharp asymptotic for the actual record count with prefactor 3/(16√(6π)A^(1/4)), where A=π²/12+(log 2)²/2. No unproved local-limit, tail, or coefficient-transfer premise remains. |
| Growing rectangles | Complete | The logarithmic asymptotic is proved uniformly for every `w ≥ h` as `h → ∞`, for literal integer-sided real-position tilings counted by block multiset. The real-to-grid bridge, cumulative partition asymptotic, both packing reservations, and exact leading constant are checked. |
| Distance graphs with three missing differences | Complete | The actual extremal densities and circle maxima for `{1,k,k+5}` and `{1,k,k+7}` are classified for every positive `k`, including every small exception. Explicit periodic optima, the exact Conjecture 39 discrepancy, and infinitely many strict counterexamples are proved. |
| Two-difference Motzkin theorem | Complete | The exact compact-group character formula, exhaustive relation-basis trichotomy, all-modulus cyclic formulas, gcd scaling, odd-cycle criterion, and stated example are checked. The literal fixed character window and rational interval unions attain the stated bounds. The exact floor-sum evaluator, Hermite independence number, attaining character, and explicit arithmetic-operation and integer-size bounds are checked and registered. |
| Tight six speeds and critical planes | Partial | The consecutive six-speed set has global value `1/7`. The complete split certificate for the prime-257 minimum-pair-20 probe is checked and registered, including its original normalized-support exclusion without a certificate premise. Full prime coverage, uniqueness, unconditional plane classification, and the large-norm consequence remain open. |
| Six-speed spectrum | Partial; complete realization direction | Every proposed value `(P−1)/(6P)` for `P ≥ 7`, `P % 6 = 1 or 5`, is attained by six distinct positive primitive speeds. The consecutive and progression families, the `P=11` boundary and displayed finite examples have checked exact global values. The universal family and off-family classification remains incomplete. |
| Eight-runner equality cases | Partial | All three displayed sets have global value `1/8`. Exhaustiveness remains open. |
| Nine-runner equality case | Partial | The consecutive set has global value `1/9`. Uniqueness remains open. |
| Symmetric four-point density | Complete | Exact real packing and covering densities for every literal translated symmetric four-point integer set, including common-divisor normalization. Both periodic constructions and the two sharp local interval lengths are proved. |
| Packing with two nonmixed gaps | Complete | The exact three-case packing and real circle formula for every positive gap pair and arbitrary positive gap counts, including gcd normalization, literal tile semantics, periodic attainment, and the stated example. |
| Haralambis three-difference theorem | Complete | Exact equality of actual extremal density and real circle value for every positive triple, with no coprimality premise. An optimal periodic set has a pair-sum period. The proof includes finite balanced orientations, signed defects, odd periods, interval counting, and the explicit `{2,5,9}` example. |
| Five-speed spectrum | Partial | All twelve example values and both critical-family reductions are checked. The unconditional four-speed gap theorem is proved: below `2/9`, precisely the two scaled critical directions occur, both with value `1/5`. This also proves the four-speed runner bound. The unconditional five-speed lower bound `L(v) ≥ 1/6` is also proved by Renault’s argument. All 122,880 indexed plane cases and the five-speed coordinate cutoff are checked, and their gap input is now available. The bounded five-speed classification remains open. |
| Tight nine-speed sets | Partial | The consecutive direction has exact global value `1/10`. The norm cutoff and prime selection are checked under explicit smaller-dimensional runner bounds. Those bounds, exhaustive modular classification and uniqueness remain open. |
| Seven-speed spectrum | Partial | Realization, the 27 displayed exceptional values, and sharp candidate bounds are checked. The critical-plane classification and large-norm family bridge are registered under explicit `LonelyRunnerBound 5` and primitive tight-six classification hypotheses. Unconditional tuple exhaustiveness remains open. |
| Eight-speed spectrum | Partial | All three displayed product families are classified and evaluated within those families, including both exceptional `s=1` values. All 17 displayed sporadic values are checked. The norm bound and exhaustive classification outside the families remain open. |
| Eleven-through-fourteen-runner equality | Partial | The displayed equality directions have their exact global values. Norm cutoffs and prime selection are checked under explicit smaller-dimensional runner bounds. Those bounds, modular exhaustiveness and uniqueness remain open. |

The full verification receipts are collected in [Lean verification checkpoints, part 1](lean-checkpoints-1.md), [Lean verification checkpoints, part 2](lean-checkpoints-2.md).

## Complete gamma-quotient theorem

[Read checkpoint](lean-checkpoints-1.md#complete-gamma-quotient-theorem).

## Complete Chow interlacing theorem

[Read checkpoint](lean-checkpoints-1.md#complete-chow-interlacing-theorem).

## Complete root-radius theorems

[Read checkpoint](lean-checkpoints-1.md#complete-root-radius-theorems).

## Formalizations of previously resolved results

[Read checkpoint](lean-checkpoints-1.md#formalizations-of-previously-resolved-results).

## War

[Read checkpoint](lean-checkpoints-1.md#war).

## Exact denominator certificates

[Read checkpoint](lean-checkpoints-1.md#exact-denominator-certificates).

## Complete Egyptian-fraction theorem

[Read checkpoint](lean-checkpoints-1.md#complete-egyptian-fraction-theorem).

## CUT Family B

[Read checkpoint](lean-checkpoints-1.md#cut-family-b).

## Reverse-solitaire dynamics

[Read checkpoint](lean-checkpoints-1.md#reverse-solitaire-dynamics).

## Exact loneliness certificates

[Read checkpoint](lean-checkpoints-1.md#exact-loneliness-certificates).

## Reproduce

[Read checkpoint](lean-checkpoints-1.md#reproduce).

## Validation receipt, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#validation-receipt-18-november-2026).

## Completed Batista checkpoint, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#completed-batista-checkpoint-18-november-2026).

## CUT automata foundations

[Read checkpoint](lean-checkpoints-1.md#cut-automata-foundations).

## Binary-semantics checkpoint, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#binary-semantics-checkpoint-18-november-2026).

## Complete padding and lower-value semantics

[Read checkpoint](lean-checkpoints-1.md#complete-padding-and-lower-value-semantics).

## Complete two-pile certificate

[Read checkpoint](lean-checkpoints-1.md#complete-two-pile-certificate).

## Numerical error languages

[Read checkpoint](lean-checkpoints-1.md#numerical-error-languages).

## Finite decision tests and paused continuation

[Read checkpoint](lean-checkpoints-1.md#finite-decision-tests-and-paused-continuation).

## Resumed campaign, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#resumed-campaign-18-november-2026).

## Complete general CUT decision test

[Read checkpoint](lean-checkpoints-1.md#complete-general-cut-decision-test).

## Checked analytic solitaire transfer

[Read checkpoint](lean-checkpoints-1.md#checked-analytic-solitaire-transfer).

## Complete symmetric four-point densities

[Read checkpoint](lean-checkpoints-1.md#complete-symmetric-four-point-densities).

## General finite CUT decision theorem

[Read checkpoint](lean-checkpoints-1.md#general-finite-cut-decision-theorem).

## Checked five-speed components

[Read checkpoint](lean-checkpoints-1.md#checked-five-speed-components).

## Local extension validation, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#local-extension-validation-18-november-2026).

## Exact density theorems

[Read checkpoint](lean-checkpoints-1.md#exact-density-theorems).

## Common loneliness interface

[Read checkpoint](lean-checkpoints-1.md#common-loneliness-interface).

## Rectangle combinatorial inputs

[Read checkpoint](lean-checkpoints-1.md#rectangle-combinatorial-inputs).

## Gap-five and gap-seven character classification

[Read checkpoint](lean-checkpoints-1.md#gap-five-and-gap-seven-character-classification).

## Complete Haralambis theorem, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#complete-haralambis-theorem-18-november-2026).

## Combined verified checkpoint, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#combined-verified-checkpoint-18-november-2026).

## Additive integration, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#additive-integration-19-november-2026).

## Complete distance-graph classifications, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#complete-distance-graph-classifications-18-november-2026).

## Rectangle components, 18 November 2026

[Read checkpoint](lean-checkpoints-1.md#rectangle-components-18-november-2026).

## Two-direction plane reduction

[Read checkpoint](lean-checkpoints-1.md#two-direction-plane-reduction).

## Complete Pham denominator result, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#complete-pham-denominator-result-19-november-2026).

## Checked finite Motzkin theorem, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#checked-finite-motzkin-theorem-19-november-2026).

## Pham and finite Motzkin integration receipt

[Read checkpoint](lean-checkpoints-1.md#pham-and-finite-motzkin-integration-receipt).

## Complete rectangle asymptotic, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#complete-rectangle-asymptotic-19-november-2026).

## Finite planes and coordinate cutoffs, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#finite-planes-and-coordinate-cutoffs-19-november-2026).

## Combined rectangle and plane integration, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#combined-rectangle-and-plane-integration-19-november-2026).

## Complete concrete CUT games, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#complete-concrete-cut-games-19-november-2026).

## Erdős 607 checked foundations, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#erdős-607-checked-foundations-19-november-2026).

## Hosted verification of the Pham/finite-Motzkin checkpoint

[Read checkpoint](lean-checkpoints-1.md#hosted-verification-of-the-phamfinite-motzkin-checkpoint).

## CUT and line-size foundation integration, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#cut-and-line-size-foundation-integration-19-november-2026).

## Graph theorem, runner families, and deterministic hyperplane registration

[Read checkpoint](lean-checkpoints-1.md#graph-theorem-runner-families-and-deterministic-hyperplane-registration).

## Concurrent registration union

[Read checkpoint](lean-checkpoints-1.md#concurrent-registration-union).

## Erdős 607 geometry and analytic profile, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#erdős-607-geometry-and-analytic-profile-19-november-2026).

## Complete four-speed gap and runner bound

[Read checkpoint](lean-checkpoints-1.md#complete-four-speed-gap-and-runner-bound).

## General compact Motzkin equality, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#general-compact-motzkin-equality-19-november-2026).

## Relation formulas, Euler correction, and finite tuple reconstruction

[Read checkpoint](lean-checkpoints-1.md#relation-formulas-euler-correction-and-finite-tuple-reconstruction).

## Exact generating function and cyclic Motzkin formulas, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#exact-generating-function-and-cyclic-motzkin-formulas-19-november-2026).

## Full hosted verification of the 397-module checkpoint

[Read checkpoint](lean-checkpoints-1.md#full-hosted-verification-of-the-397-module-checkpoint).

## Hosted replay of the four-speed integration snapshot

[Read checkpoint](lean-checkpoints-1.md#hosted-replay-of-the-four-speed-integration-snapshot).

## Five-speed finite certificate checkpoint, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#five-speed-finite-certificate-checkpoint-19-november-2026).

## Five-speed root candidate and component gates, 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#five-speed-root-candidate-and-component-gates-19-november-2026).

## Frankl counting components — 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#frankl-counting-components--19-november-2026).

## Frankl large-generator theorem — 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#frankl-large-generator-theorem--19-november-2026).

## Hadamard automorphism arithmetic

[Read checkpoint](lean-checkpoints-1.md#hadamard-automorphism-arithmetic).

## Hadamard automorphism Fourier component

[Read checkpoint](lean-checkpoints-1.md#hadamard-automorphism-fourier-component).

## Hadamard automorphism permutation component

[Read checkpoint](lean-checkpoints-1.md#hadamard-automorphism-permutation-component).

## Hadamard quadratic field and class-order component

[Read checkpoint](lean-checkpoints-1.md#hadamard-quadratic-field-and-class-order-component).

## Hadamard cyclotomic norm obstruction

[Read checkpoint](lean-checkpoints-1.md#hadamard-cyclotomic-norm-obstruction).

## Complete Hadamard order-479 automorphism obstruction

[Read checkpoint](lean-checkpoints-1.md#complete-hadamard-order-479-automorphism-obstruction).

## Complete independent ideal-class norm obstruction

[Read checkpoint](lean-checkpoints-1.md#complete-independent-ideal-class-norm-obstruction).

## Complete quadratic integer model

[Read checkpoint](lean-checkpoints-1.md#complete-quadratic-integer-model).

## Frankl local certificate checkers — 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#frankl-local-certificate-checkers--19-november-2026).

## Frankl FC and small cyclic components — 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#frankl-fc-and-small-cyclic-components--19-november-2026).

## Frankl mask checker and exact domains — 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#frankl-mask-checker-and-exact-domains--19-november-2026).

## Complete fixed-border multiplier and orbit bounds

[Read checkpoint](lean-checkpoints-1.md#complete-fixed-border-multiplier-and-orbit-bounds).

## Frankl cyclic assembly and weight helpers — 19 November 2026

[Read checkpoint](lean-checkpoints-1.md#frankl-cyclic-assembly-and-weight-helpers--19-november-2026).

## Complete sharp 95-vertex example and arbitrary-voltage normalization

[Read checkpoint](lean-checkpoints-1.md#complete-sharp-95-vertex-example-and-arbitrary-voltage-normalization).

## Fixed-border certificate transport

[Read checkpoint](lean-checkpoints-1.md#fixed-border-certificate-transport).

## Actual row normalization from compression shapes

[Read checkpoint](lean-checkpoints-1.md#actual-row-normalization-from-compression-shapes).

## Exact fixed character-window witness

[Read checkpoint](lean-checkpoints-1.md#exact-fixed-character-window-witness).

## Exact Motzkin evaluator and explicit rational intervals

[Read checkpoint](lean-checkpoints-1.md#exact-motzkin-evaluator-and-explicit-rational-intervals).

## Prime-257 minimum-pair-20 support certificate

[Read checkpoint](lean-checkpoints-1.md#prime-257-minimum-pair-20-support-certificate).

## Checked order-11 fiber component

[Read checkpoint](lean-checkpoints-1.md#checked-order-11-fiber-component).

## Complete universal abelian-cover cycle theorem

[Read checkpoint](lean-checkpoints-1.md#complete-universal-abelian-cover-cycle-theorem).

## Complete literal finite-border certificate

[Read checkpoint](lean-checkpoints-1.md#complete-literal-finite-border-certificate).

## Complete length-598 order-eleven obstruction

[Read checkpoint](lean-checkpoints-1.md#complete-length-598-order-eleven-obstruction).

## Complete two-difference Motzkin theorem

[Read checkpoint](lean-checkpoints-1.md#complete-two-difference-motzkin-theorem).

## Complete conditional fixed-border construction and fourteen patterns

[Read checkpoint](lean-checkpoints-1.md#complete-conditional-fixed-border-construction-and-fourteen-patterns).

## Checked length-1197 reduction to order 27

[Read checkpoint](lean-checkpoints-1.md#checked-length-1197-reduction-to-order-27).

### Exact receipts and registration

[Read checkpoint](lean-checkpoints-1.md#exact-receipts-and-registration).

## Complete Frankl high-girth frequency theorem

[Read checkpoint](lean-checkpoints-2.md#complete-frankl-high-girth-frequency-theorem).

## Complete Erdős 607 line-size asymptotic

[Read checkpoint](lean-checkpoints-2.md#complete-erdős-607-line-size-asymptotic).

## Actual Legendre-pair matrix and quotient transport

[Read checkpoint](lean-checkpoints-2.md#actual-legendre-pair-matrix-and-quotient-transport).

## Complete unrestricted two-speed insertion theorem

[Read checkpoint](lean-checkpoints-2.md#complete-unrestricted-two-speed-insertion-theorem).

## Six-speed spectrum: complete realization

[Read checkpoint](lean-checkpoints-2.md#six-speed-spectrum-complete-realization).

## Complete fixed-hyperplane theorem

[Read checkpoint](lean-checkpoints-2.md#complete-fixed-hyperplane-theorem).

## Conditional nine-through-thirteen speed norm reduction

[Read checkpoint](lean-checkpoints-2.md#conditional-nine-through-thirteen-speed-norm-reduction).

## Six-speed spectrum reduced fraction arithmetic

[Read checkpoint](lean-checkpoints-2.md#six-speed-spectrum-reduced-fraction-arithmetic).

### Six-speed sporadic values and denominator bounds

[Read checkpoint](lean-checkpoints-2.md#six-speed-sporadic-values-and-denominator-bounds).

### Seven- and eight-speed spectrum realizations and exact candidate bounds

[Read checkpoint](lean-checkpoints-2.md#seven--and-eight-speed-spectrum-realizations-and-exact-candidate-bounds).

## Five-runner lower-bound candidate

[Read checkpoint](lean-checkpoints-2.md#five-runner-lower-bound-candidate).

### Higher-speed triangle consequences under primitive classification

[Read checkpoint](lean-checkpoints-2.md#higher-speed-triangle-consequences-under-primitive-classification).

## Renault foundations and six-speed prime pilot, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#renault-foundations-and-six-speed-prime-pilot-19-november-2026).

## Critical seven-coordinate planes and large-norm family

[Read checkpoint](lean-checkpoints-2.md#critical-seven-coordinate-planes-and-large-norm-family).

### Accepted seven-speed low-gap input for the eight-coordinate argument

[Read checkpoint](lean-checkpoints-2.md#accepted-seven-speed-low-gap-input-for-the-eight-coordinate-argument).

### Accepted six-plane direction coverage and certificate chunk joins

[Read checkpoint](lean-checkpoints-2.md#accepted-six-plane-direction-coverage-and-certificate-chunk-joins).

### Six-speed norm geometry from an explicit plane gap

[Read checkpoint](lean-checkpoints-2.md#six-speed-norm-geometry-from-an-explicit-plane-gap).

## Product-plane integer speed bridge (2026-11-19)

[Read checkpoint](lean-checkpoints-2.md#product-plane-integer-speed-bridge-2026-11-19).

## Five-speed norm and prime avoidance, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#five-speed-norm-and-prime-avoidance-19-november-2026).

## Six-coordinate plane semantics (19 November 2026)

[Read checkpoint](lean-checkpoints-2.md#six-coordinate-plane-semantics-19-november-2026).

## Unconditional five-speed bound and primitive transport, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#unconditional-five-speed-bound-and-primitive-transport-19-november-2026).

## Six-speed finite-field prime-product reduction (2026-11-19)

[Read checkpoint](lean-checkpoints-2.md#six-speed-finite-field-prime-product-reduction-2026-11-19).

## Conditional gcd shift test (19 November 2026)

[Read checkpoint](lean-checkpoints-2.md#conditional-gcd-shift-test-19-november-2026).

### Six-speed first-cover support reduction: accepted component

[Read checkpoint](lean-checkpoints-2.md#six-speed-first-cover-support-reduction-accepted-component).

### Accepted six-plane membership-to-family bridge

[Read checkpoint](lean-checkpoints-2.md#accepted-six-plane-membership-to-family-bridge).

## Complete tight-five classification and independent finite lower bound (19 November 2026)

[Read checkpoint](lean-checkpoints-2.md#complete-tight-five-classification-and-independent-finite-lower-bound-19-november-2026).

## Modular support, unit orbits and literal binary lifts, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#modular-support-unit-orbits-and-literal-binary-lifts-19-november-2026).

## Seven-speed norm and reduced prime sets, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#seven-speed-norm-and-reduced-prime-sets-19-november-2026).

## Order-nine automorphism subgroups and orbits

[Read checkpoint](lean-checkpoints-2.md#order-nine-automorphism-subgroups-and-orbits).

## Initial cut pilot and prime-251 binary lifts, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#initial-cut-pilot-and-prime-251-binary-lifts-19-november-2026).

## Rational integer-point lattices and six-speed norm components

[Read checkpoint](lean-checkpoints-2.md#rational-integer-point-lattices-and-six-speed-norm-components).

## Prime filtering and proved runner classes, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#prime-filtering-and-proved-runner-classes-19-november-2026).

## Conditional two-parameter radius estimate

[Read checkpoint](lean-checkpoints-2.md#conditional-two-parameter-radius-estimate).

## Six-speed norm bounds with the four-speed input discharged

[Read checkpoint](lean-checkpoints-2.md#six-speed-norm-bounds-with-the-four-speed-input-discharged).

## Seven-coordinate implications with the five-speed input discharged

[Read checkpoint](lean-checkpoints-2.md#seven-coordinate-implications-with-the-five-speed-input-discharged).

## Four-input prime filtering, 19 November 2026

[Read checkpoint](lean-checkpoints-2.md#four-input-prime-filtering-19-november-2026).

## Li coefficient-sign counterexample

[Read checkpoint](lean-checkpoints-2.md#li-coefficient-sign-counterexample).

## Actual rational-lattice quotient index

[Read checkpoint](lean-checkpoints-2.md#actual-rational-lattice-quotient-index).

## Complete Wright log-concavity disproof

[Read checkpoint](lean-checkpoints-2.md#complete-wright-log-concavity-disproof).

## Fan–Tringali’s power-monoid length-set conjecture

[Read checkpoint](lean-checkpoints-2.md#fantringalis-power-monoid-length-set-conjecture).

## Hartke–Stolee–West–Yancey matching-excess conjecture

[Read checkpoint](lean-checkpoints-2.md#hartkestoleewestyancey-matching-excess-conjecture).
