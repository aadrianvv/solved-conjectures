# Lean verification status

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
formalization, and ⬜ when a result has neither a computer-assisted proof nor
Lean verification.

| Note | Status | Checked scope and remaining gap |
| --- | --- | --- |
| Malek's conjecture | Not formalized | Complete written all-degree negative-transform proof with all equality cases, two independent internal reviews and exact scalar identity checks. The permanent endpoint is prior work; the named subsidiary is documented in the Minc site's linked survey. No proof-assistant work is claimed. |
| Baricz–Pogány's asymptotic-coefficient positivity conjecture | Not formalized | Existing complete written formal-series proof, with exact rational identity checks and two internal reviews. No proof-assistant formalization is claimed. The result's novelty audit retains its source-access limit. |
| Pula–Song–Wanless conjecture | Not formalized | Complete written proof of the all-parameter threshold, including its equality case and unique boundary minimizer. Real-rooted minor equalization and van der Waerden completion replace disputed dependencies. Exact identity checks supplement the proof. The full Minc Problems 14 and 15 remain outside its scope. |
| Perron root of permanental compounds | Not formalized | Written FPRAS proof for every nonnegative rational matrix and every compound degree, with deterministic zero detection. Exact finite checks supplement the argument. This is the randomized approximation formulation of Minc Problem 18; exact polynomial-time eigenvalue computation and the characteristic-polynomial problem are outside its scope. |
| Oravcová–Soták conjecture for five to eight distances | Not formalized | Written proof with machine-checkable certificates, conditional on the repository's five- to eight-speed spectrum classifications. The verifier checks the 65 table sets, 62 periodic colourings, three exceptional sets, 37 loops across four one-parameter families, and the two-parameter family; a separate SAT scan checks bounded ranges without those classifications. No proof-assistant formalization is claimed. |
| Johnson–Kaya–Matzke conjecture on Babai spectra of paths | Not formalized | Elementary written proof of the full spectrum for every `n >= 2` and `1 <= k <= n-1`. The standard-library verifier checks all 16,369 distance sets with `n <= 14`. No proof-assistant formalization is claimed. |
| Karp–Vishnyakova–Zhang's Bessel-ratio unimodality conjecture | Not formalized | Written proof of the full surviving unimodality assertion and all monotone/unique-maximum cases; exact series diagnostics are supplementary. |
| Ferreira–Simon's Wright log-concavity conjecture | Not formalized | Written analytic disproof on continuous boundary and interior parameter families; exact curvature checks are supplementary. |
| Karp–Vishnyakova–Zhang's gamma-quotient conjecture | Not formalized | Written all-order sign-regularity proof with exact signature and integer rank cutoff; finite determinant checks are supplementary. |
| Alexandersson's Fuss–Catalan conjecture | Not formalized | Written deduction from classical enumeration and ordinary-case real-rootedness, with attribution caveats and finite path checks. |
| Sagan–Swanson conjecture | Not formalized | Written proof of all four stated asymptotic normality assertions using actual means and variances; finite model checks are supplementary. |
| Bernardi–Morales's delta-process conjecture | Not formalized | Written proofs of the full tree and event identities, with exact finite checks. |
| Gilmore's crossing–nesting conjecture | Not formalized | Written weighted-path proof of the full matching-enumerator identity; finite recurrence checks are supplementary. |
| Chow's conjecture | Not formalized | Written deduction of weak interlacing from Savage–Visontai, with a separate strictness argument and explicit attribution caveat. |
| Németh–Seberry–Shu conjecture | Not formalized | Written asymptotic disproof and a quadratic lower bound; finite checks are not part of the proof. |
| Sonntag–Teichert conjecture | Not formalized | Written proof of tournament domination hypergraph connectivity and classification of disconnected oriented cases, with finite cross-checks. |
| Horňák–Woźniak conjecture | Not formalized | Written proof of both connected-partition conjectures, with separate finite and symbolic cross-checks. |
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
| Zhang's Question 8.4: deletion values of the lonely runner | Not formalized | Complete elementary written proof of the deletion-value formula and the strict inequality. The standard-library verifier checks 779 cases for `3 <= n <= 40`. No proof-assistant formalization is claimed. |
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

## War

[`Conjectures/War.lean`](../lean/Conjectures/War.lean)
defines three ordered queues of natural-number ranks. `step` removes the exposed
cards, compares them, and appends the trick to the winner's queue in decreasing
rank, seat, or clockwise order. An empty queue is absorbing; the checked safety
certificates prove that this case never occurs along any of the three trajectories.

`standard` checks that every rank from 1 through the deck size occurs once and
that the queue lengths are the sizes of a round-robin deal starting at A.
`standard_deal_witnesses` supplies three explicit distinct-rank decks and proves
that actually dealing their cards in A/B/C rotation gives the initial queues.
No particular shuffle or random-deal probability is claimed.

Main theorems:

- `War.standard_deal_witnesses`: explicit standard decks and their round-robin deals.
- `War.three_standard_cycles`: standard deals, returns, and activity for every time.
- `War.rank_first_return`: first return at 90.
- `War.seat_first_return`: first return at 180.
- `War.clockwise_first_return`: first return at 19,320.

The certificates use `decide`, with reduction checked by Lean's kernel.
They use neither `native_decide` nor an external Python replay as a premise.

## Exact denominator certificates

[`Conjectures/Denominator.lean`](../lean/Conjectures/Denominator.lean)
proves `finite_coefficient_identity` using divisibility by a power of `X`, a
polynomial degree bound, and cancellation of the unit denominator series.
`primary_certificate` and `dual_certificate` prove exact polynomial equations
`Q*T - R = X^N * W` for the displayed truncations, with `N = 26` and `31`.
The two `*_coprime` theorems provide explicit Bézout identities over `ℚ[X]`.

`primary_identity_of_representation` and `dual_identity_of_representation`
conclude `Q*H = R` for a formal series `H` **only given** its stated truncation
and a representation `B*H=A` with nonzero constant denominator coefficient and
the published degree bounds. These hypotheses are the outstanding mathematical
work, not facts inferred from running the Python verifier.

## Complete Egyptian-fraction theorem

[`Conjectures/EgyptianTheorem.lean`](../lean/Conjectures/EgyptianTheorem.lean)
proves `Egyptian.batista_admissible_congruence`, the exact statement of the note:
for every positive admissible `k` with `k % 5 != 1`, there exists a strictly
ordered solution that is lexicographically first and uniquely maximizes the
last denominator. `batista_congruence` also proves existence for every `k >= 3`
in those classes, and admissibility is proved to force `k >= 3`.

The original [`Egyptian.lean`](../lean/Conjectures/Egyptian.lean)
proves integrality of the strict-greedy construction. The new
[`EgyptianBounds.lean`](../lean/Conjectures/EgyptianBounds.lean)
proves the all-size competitor bounds, including the modular improvement in
the immediate-neighbor case. A concave quadratic proves positivity throughout
the unbounded interval; explicit endpoint polynomials have positive
coefficients after shifting the first denominator by 20.

[`EgyptianFinite.lean`](../lean/Conjectures/EgyptianFinite.lean)
checks every small `k < 100` by kernel reduction. Its soundness theorem derives
complete bounds on both enumerated denominators from the fraction equation,
then derives the third denominator exactly by integer division. The certificate
checks ordered existence and unique maximality; it is not used as evidence for
an unbounded claim. The infinite regime and the finite regime are combined in
`EgyptianTheorem.lean`, which also proves the lexicographic conclusion.

Chu's best-two-term theorem is not a hypothesis of either completed theorem.

## CUT Family B

[`Conjectures/CutFamily.lean`](../lean/Conjectures/CutFamily.lean)
contains the six-block formula and proves `large_cut_decreases` for every finite
list of positive pile sizes with at least `3x+2` parts, without any upper bound
on the sizes or number of parts. The quotient and residue XOR estimates are
proved, not checked on a finite range.

`OptionValue` implements legal splits, including their positive sizes, total,
arity, allowed cut, and XOR. `grundy_unique` proves uniqueness from the mex
conditions by induction on pile size. `sharp_collision` constructs the
smaller-odd-cut witness, and `small_odd_cut_forces_difference` proves the
size-`4x` distinction for any game containing that cut.

The five new modules `CutFamilyBlocks`, `CutFamilyBase`, `CutFamilyCover`,
`CutFamilyGame`, and `CutFamilyTheorem` remove the former base-formula
hypothesis. `gameValue` is defined by well-founded recursion using the mex of
actual positive-pile split options. Its mex existence and recursion equations
are proved for arbitrary, possibly infinite cut sets.

`even_base_mex` proves the six-block formula for `{1}` together with any set
of even cuts whose minimum is the given even `x >= 4`. The proof uses a finite
XOR-subadditive block cost table and explicit witnesses for every smaller
value; it is an all-size argument. `family_b` then states the exact comparison
with `{1,x}` for arbitrary sets of even and odd cuts, with minima `x` and `y`.
It proves equality at every positive size iff `3*x < y`.
`family_b_difference_by_four_x` proves the stated finite discrepancy bound.
No published base formula or mex equation is an unproved hypothesis of these
two complete theorems.

## Reverse-solitaire dynamics

`DenominatorDynamics.lean` works with actual multisets of positive pile sizes.
It proves that choosing a legal distinct size gives precisely one reverse
image, that every positive preimage arises this way, and that different chosen
sizes give different preimages. Forward and reverse moves preserve mass.
These results establish the enumeration model, but do not yet prove the
stabilized orbit coefficients or the representation bounds required by the
Pham denominator certificate.

## Exact loneliness certificates

`LonelinessMax.lean` defines distance to the nearest integer and the minimum
of the distances for a finite speed set. It proves continuity, attainment of
a global maximum, and a pair-sum maximizer: for distinct positive speeds there
are `a != b` in the set and an integer `0 <= k <= a+b` at which `k/(a+b)` is a
global maximizer. The proof covers every real time. It uses the intersection
of phase intervals and a strict improvement argument, not a sampled-time
assumption.

`LonelinessCertificate.lean` proves sound upper and lower Boolean checks using
exact natural-number remainder arithmetic. `LonelinessExamples.lean` checks
31 explicit values by ordinary kernel reduction. The Python generator is an
untrusted producer. The resulting theorems state an attained value and its
upper bound at every real time; they do not assert that the examples exhaust
any classification.

## Reproduce

Install the pinned toolchain with elan, then from the repository root:

```sh
export PATH="$HOME/.elan/bin:$PATH"
cd lean
lake exe cache get
cd ..
scripts/verify_lean.sh
```

The script rebuilds all sources, runs `ProofAudit.lean`, and rechecks the proof modules using `leanchecker`. The CI workflow runs the same script.
`ProofAudit.lean` checks every theorem in the imported accepted project modules, including
helper theorems, and rejects any transitive axiom other than `propext`,
`Classical.choice`, and `Quot.sound`. It also requires the listed main
declarations to exist. Missing proofs, `sorryAx`, native-computation axioms,
and custom axioms fail the check.

The original Python verifiers remain independent evidence, with their original
scope; their success does not upgrade a partial entry to a complete Lean proof.

## Validation receipt, 18 November 2026

`scripts/verify_lean.sh` completed with exit status 0 locally on Lean 4.35.0.
At the first checkpoint, all six `leanchecker` module rechecks completed successfully. The audit reported
466 project theorem declarations, including generated helper declarations;
this is not a count of independent mathematical results.

The audit was also challenged with three temporary negative controls. It
rejected a custom axiom transitively used by a War theorem, a proof containing
`sorry`, and a theorem proved with `native_decide`. These temporary controls
are not part of the repository's proof sources.

The GitHub Actions workflow has been updated to run the same checks; a hosted
CI run is separate from this local verification receipt.

The unchanged Python source checks also passed for all three War deals, the
primary and dual necklace certificates with direct enumeration through depth
12, Egyptian fractions through `k = 150` (including unpruned enumeration),
and all 46 CUT Family B test cut sets in the original verifier. These checks
corroborate transcription and retain their finite scope.

## Completed Batista checkpoint, 18 November 2026

The full `scripts/verify_lean.sh` passed with all nine proof-module kernel
rechecks, including `EgyptianBounds`, `EgyptianFinite`, and `EgyptianTheorem`.
The whitelist audit accepted 578 project theorem declarations. Both complete
Batista theorem declarations depend only on `propext`, `Classical.choice`, and
`Quot.sound`. The finite certificates use kernel reduction rather than native
computation. The source-level statement retains the exact admissibility,
congruence, lexicographic, maximality, and uniqueness requirements.

## CUT automata foundations

`BinaryAutomata.lean` proves subset-construction semantics and a refinement
certificate theorem that works for every input word. Its active-list variant
avoids scanning every NFA state during a finite certificate check.
`BinaryArithmetic.lean` proves that the carry constraints used by the original
high-bit-first automata are exactly integer addition, including both end
carries, and that columnwise XOR is exactly numerical XOR.

`CutPeriodGraph.lean` proves the arithmetic counter graph recognizes the
proposed pile-value function, including all six prefix exceptions and its
unbounded tail. `CutPeriodGraphCertificate.lean` checks every transition and
acceptance label of the 179-state representation and its 27-state quotient,
then proves the concrete DFA recognizes that graph for every finite word.

The Python producer `results/cut-arithmetic-periodicity/generate_lean_certificates.py`
is untrusted: it produces data that Lean checks. Its intermediate JSON archive
is reproducible and ignored; the checked Lean certificate is versioned. Other
produced automata do not count as proofs until their refinement and arithmetic
semantics are checked. The complete game-period claims remain open.

`BinaryComposition.lean` proves the exact language semantics of addition/XOR
composition in both directions, including safe pruning of rejecting sinks.
Every accepted composed word is decoded to accepted component words with the
actual numerical addition and XOR equations, and every such compatible column
sequence produces a composed path.

## Binary-semantics checkpoint, 18 November 2026

The full package including the four graph/arithmetic foundation modules passed
all kernel rechecks. The added generic composition module then passed its
source build, kernel replay, and a refreshed whitelist audit over 724 project
theorem declarations. The detailed continuation plan and measured certificate
performance limits are in `results/cut-arithmetic-periodicity/LEAN_PLAN.md`.

At this 18 November checkpoint, the distance-graph classifications, compact
Motzkin theorem, symmetric-four-point densities, and nonmixed-gap formulas
were still pending. Their later verified scopes appear in the current status
table and the subsequent component sections below.

## Complete padding and lower-value semantics

`BinaryEncoding.lean` supplies fixed-width encodings, uniqueness, shared
arithmetic columns and an encoding for every pair of naturals.
`CutPeriodPiles.lean` defines groups by actual lists of positive pile sizes;
it proves the candidate-value XOR fits within the total pile size. Using that
bound, `sum_recognizes_successor` proves both directions of the group-composition
semantics at every visible word width. No hidden witness is assumed to fit.

`BinaryOrder.lean` verifies the numerical comparison-state update, and
`BinaryProjection.lean` proves exact hidden-track projection semantics.
`CutPeriodLower.lean` specializes this to the proposed sequence.
`CutPeriodLowerCertificate.lean` checks every transition and final label for
the 111-state representation and its 23-state quotient. Its `correct` theorem
recognizes exactly positive sizes paired with a strictly smaller value,
universally over input words. `BinaryBoolean.lean` supplies Boolean product
semantics for the remaining error-language certificates.

The generated two-pile module has passed its source build, axiom audit and
kernel recheck. None of these components alone establishes either game's mex
equation.

`CutPeriodParameters.lean` proves that the proposed function has least positive
eventual additive period 12, unique saltus 8 at that period, and earliest start
at pile seven (preperiod length six). It rules out every smaller positive
period with every possible saltus, by descending any eventual identity to the
12 tail residues. Identification of the function with the games still awaits
the finite option/error certificates.

The 100 small Egyptian cases are now separate theorem declarations aggregated
by `FiniteCertificate.checked_list_rows`. This preserves the exhaustive check
and its soundness theorem while keeping source replay under the project's
4.5 GB Lean memory cap. The earlier single declaration exceeded that cap.

The full source build, refreshed whitelist audit and all 23 listed module
kernel rechecks passed locally for this checkpoint. Adding `CutPeriodMex`
then passed its source build, kernel replay and a refreshed audit over 1,094
project theorem declarations. Its error-language assumptions remain explicit;
the two-pile certificate was validated separately before registration.

## Complete two-pile certificate

`CutPeriodParts2Certificate.lean` checks a cache of all 1,458 finite product-NFA
states against the semantic composition rule, all 402 subset representations
and all quotient labels in the 126-state minimized DFA. `recognizes_piles`
proves its language is exactly the actual two-positive-pile relation, for every
input word. The current source build, whitelist audit and kernel replay passed.
The source build stayed below 3 GB RSS with the 4.5 GB Lean cap.

`BinaryFastComposition.lean` checks an eight-row digit-choice table against the
full numerical enumeration and proves a generic transition equality. Larger
groups use that equality to avoid repeating the numerical enumeration in every
cache row; no external computation or additional axiom is a premise.

The refreshed package audit accepted 3,391 theorem declarations, including
generated finite-row helpers. All newly registered modules passed kernel
replay; this is a two-pile checkpoint, not a proof of the full games.

The [Haralambis three-difference theorem](../results/haralambis-three-differences/PROOF.md) has a written proof and an executable check of the signed-edge and rotation certificates. The general theorem has no Lean formalization.

## Numerical error languages

`CutPeriodOptionData.lean` defines the two numerical 28-state option DFAs.
Their correspondence with actual legal splits is still unproved. Four checked
refinements in the `CollisionA/B` and `MissingA/B` certificate modules establish
that their collision and missing-smaller-value languages are empty for every
word. The collision representations have 32 states; the missing-value
representations have 34. Each quotient is a one-state rejecting DFA.

`CutPeriodCertifiedMex.lean` combines these certificates with the arithmetic
and actual-rule bridge. Its two mex theorems have one explicit remaining
hypothesis each: the numerical option DFA recognizes the actual legal splits.
Groups three through nine and the union refinements must discharge it before
either game theorem is complete. No finite error check supplies that hypothesis.

The added modules passed source builds and kernel replay. The refreshed
whitelist audit accepted 3,710 project theorem declarations, including helpers.

Both hosted workflows passed for the two-pile checkpoint `26b5c11` and the
error-language checkpoint `a6f4d06` on `main`. The three-pile group remains
experimental. Its current modular build checks short row blocks with explicit
interval coverage, rather than retaining the entire finite proof in one file.

`BinarySetCertificate.lean` proves a structural list-based set equality check
implies the original mask equality. `FiniteIntervalCertificate.lean` proves
that a checked proof list covers exactly its recorded numerical interval.
These are general certificate helpers, not completed game theorems.
Both helpers passed source builds and kernel replay; the refreshed package
audit accepted 3,725 theorem declarations using only the permitted axioms.

## Finite decision tests and paused continuation

`BinaryDecision.lean` connects the project automata to Mathlib's DFA interface,
uses the checked cycle-removal theorem to prove a complete short-word bound,
and proves `emptyCheck_correct` for every finite DFA. Its word enumeration is
a total finite computation; it need not be efficient for this termination
claim. `CutMexDecision.lean` proves the two finite error tests are necessary
and sufficient for the actual CUT mex equations, given exact finite graph,
lower-value and actual-option recognizers. Construction of those recognizers
uniformly from an arbitrary proposed arithmetic tail remains open.

At the earlier paused checkpoint, the generated three-pile source build passed
its data, all 27 transition blocks and their aggregation. It was stopped in
the shared subset-data module. The 39 experimental sources and their ordered
manifest are preserved, but are not registered in the accepted root imports
or included in the package's axiom/kernel verification claims. See
`docs/formalization.md` for exact resume commands and remaining checks.

At the paused checkpoint, the accepted source build and refreshed audit passed
over 3,738 theorem declarations. Both newly registered decision modules passed
independent kernel replay. This count excludes all unregistered experimental
three-pile modules and is not a count of independent mathematical results.

The [five-speed loneliness spectrum](../results/five-speed-spectrum/PROOF.md) has a written computer-assisted proof and an exhaustive arithmetic verifier. Its Lean formalization is open.

The [six-speed equality and seven-coordinate plane classifications](../results/tight-six-speeds/PROOF.md) have written proofs and executable finite checks. The seven-coordinate plane and large-norm family bridge is now registered under the two explicit lower-dimensional hypotheses described below. The primitive tight-six classification and unconditional seven-speed exhaustiveness remain open.

The [six-speed loneliness spectrum](../results/six-speed-spectrum/PROOF.md) has a written computer-assisted proof and an exhaustive arithmetic verifier. Its Lean formalization is open.

The [eight-runner equality classification](../results/tight-seven-speeds/PROOF.md) has a written computer-assisted proof and an exhaustive mixed-modulus verifier. Its Lean formalization is open.

The [nine-runner equality classification](../results/tight-eight-speeds/PROOF.md) has a written computer-assisted proof and an exhaustive mixed-modulus verifier. Its Lean formalization is open.

## Resumed campaign, 18 November 2026

The new Family B modules passed their source builds, a namespace audit of 575
project theorem declarations, and all five independent `leanchecker` replays.
The three loneliness modules, the reverse-solitaire dynamics module, the
uniform affine/tail graph modules, and the first three packing-density modules
also passed source builds and independent kernel replay locally. The shared
package verification is being rerun with the accepted root imports and audit
requirements. This paragraph does not claim a hosted CI result.

Li remains last in the active queue. The repository-wide campaign is incomplete.

## Complete general CUT decision test

`BinaryFiniteNFA`, `BinaryGenericComposition`, and `BinaryGenericProjection`
construct executable finite recognizers for arbitrary finite state types.
Hidden-number completeness uses an explicit common padded width, without an
assumption that values are bounded by pile size. `BinaryRecognizers` packages
finite union, difference, composition, projection, and complete emptiness.

`CutArithmeticTest.finiteSetTest_iff_gameValue` states that for every finite
cut set and every proposed finite prefix plus arithmetic tail, the constructed
Boolean test accepts iff the candidate equals the actual recursively defined
game value at every positive size. The test terminates for every input; no
practical complexity claim is made. No graph, option, projection, or mex
recognizer is an unproved input. This completes the general test in the note.
It does not replace the remaining finite certificate work for its two examples.

## Checked analytic solitaire transfer

`Solitaire/ProfileTransfer.lean` proves the explicit error bound
`4/(a*ε^2) + sqrt(2)/(ε*sqrt(n))`, its convergence to zero for diverging scales,
uniform convergence on `x >= ε`, and transfer of every pointwise stable limit.
`Solitaire/GeneralTheorem.lean` discharges every field of the finite input
`SolitaireGeneral.ProfileComparison` from the actual arbitrary-layer dynamics.
The completed chain proves return-time rank periodicity, the attained birth
range, sorted-column interlacing, stable mass and length estimates, and
classification of every positive fixed configuration. The reference is an
actual fixed configuration of largest mass at most n.

`corrected_solitaire_uniform` proves uniform convergence away from zero for
every rule sequence and every recurrent configuration sequence of mass n,
at every positive horizontal scale tending to infinity.
`corrected_solitaire_pointwise` transfers every stable pointwise limit.
`arbitrary_layers_uniform` accepts arbitrary (including infinite) layer sets
containing the bottom layer. The only recurrence premise is actual periodicity
under the defined move; no interlacing or return-period lemma is assumed.

All twelve finite-dynamics modules passed warning-as-error source checks and
independent kernel replay; the finite namespace audit checked 348 theorem
declarations. ProfileTransfer, StableCore, StableBounds and GeneralTheorem
also passed source checks and independent kernel replay. The combined package
gate is being rerun after the concurrent repository merge.

The floor step in the written note was corrected: `floor(a*x) >= a*ε/2` and
`floor(a*x)+1 > a*ε` follow when `a*ε >= 2`. These valid inequalities give the
same stated error bound. No stronger floor inequality is assumed in Lean.

## Complete symmetric four-point densities

`PackingFourPoint.symmetric_four_point_densities` proves the exact supremum of
upper packing densities and infimum of lower covering densities for every
coprime pair `0<a<b`. Opposite parity gives `1/4` for both. For odd steps,
`P=ab+b-a` and `Q=ab+a+b` give `(P-1)/(4P)` and `(Q+1)/(4Q)` respectively.
The density definitions use actual symmetric integer windows and real limsup
and liminf, not a periodic-only optimization.

The proof combines the all-size local obstruction with uniform count bounds,
passage to asymptotic density, and fully checked modular constructions.
`PackingLocalSharpness` additionally proves existence of global packings and
coverings with exactly-once intervals of lengths `P-1` and `Q-1`; together with
the obstruction the lengths are optimal. All ten packing modules passed local
source checks and independent kernel replay. Their main and helper theorems
are included in the shared whitelist audit.

The [ten-runner equality classification](../results/tight-nine-speeds/PROOF.md) has a written computer-assisted proof and an exhaustive verifier. Lean checks the explicit equality example and the [conditional norm cutoff and prime selection](loneliness-large-norm-lean.md). The lower-runner assumptions, exhaustive modular classification and uniqueness remain open.

The [eleven- through fourteen-runner equality classification](../results/tight-eleven-to-fourteen/PROOF.md) has a written computer-assisted proof using published sieves. Lean checks the displayed equality directions and the [conditional norm cutoffs and prime selection](loneliness-large-norm-lean.md). The lower-runner assumptions, modular exhaustiveness and uniqueness remain open.

The [eight-speed spectrum classification](../results/eight-speed-spectrum/PROOF.md) has a written computer-assisted proof and an exhaustive verifier. Its Lean formalization is open.

The [seven-speed spectrum classification](../results/seven-speed-spectrum/PROOF.md) has a written computer-assisted proof and an exhaustive verifier. Its Lean formalization is open.

## General finite CUT decision theorem

[`CutGeneralDecision.lean`](../lean/Conjectures/CutGeneralDecision.lean),
[`CutGeneralGraph.lean`](../lean/Conjectures/CutGeneralGraph.lean), and
[`CutGeneralSearch.lean`](../lean/Conjectures/CutGeneralSearch.lean) prove the
uniform construction that the earlier conditional finite-test theorem required.

`CutGeneral.Candidate.test_correct` states that the computable test returns true
if and only if the proposed sequence satisfies the actual CUT mex equations.
The candidate has an arbitrary finite prefix, a positive period, finite natural
number tail entries, and a nonnegative saltus. The cut set is any finite list.
Exact recognizers, complete hidden-witness padding, subset construction, and
finite emptiness checks are all constructed and proved from these inputs.

`verifiedCandidates_sound` and `verifiedCandidates_complete` prove that bounded
finite enumeration finds any valid representation once its explicit search
bound is reached. This does not assert that every CUT game is arithmetic
periodic, or that the decision procedure is practical on large inputs.
The two concrete games still use separate numerical option certificates.
See [the detailed proof and scope](../results/cut-arithmetic-periodicity/GENERAL_LEAN.md).

## Checked five-speed components

[`Loneliness.lean`](../lean/Conjectures/Loneliness.lean) defines actual real
nearest-integer distance, finite-list clearance, and its supremum on the unit
interval. `certified_value` proves exact real maxima from finite rational
interval covers and rational attaining witnesses. The generator proposes the
data; Lean checks their coverage for every real time.

[`LonelinessContinuity.lean`](../lean/Conjectures/LonelinessContinuity.lean)
proves continuity, rational approximation, and attainment of that supremum.
[`LonelinessRational.lean`](../lean/Conjectures/LonelinessRational.lean)
proves the exact remainder formula at rational times.

`Loneliness.five_family_value` proves, for every natural `s >= 1`,
`value [1,2,3,4,5*s] = s/(5*s+1)`. `five_family_realizes` supplies positivity,
distinctness, primitivity, and the strict threshold as well. The twelve
`Loneliness.FiveSpeedExamples.*_value` theorems prove the exact maxima of the
listed sporadic examples. These do not establish that the list is exhaustive.

`Loneliness.CriticalFamilies.critical_family_below_threshold` classifies every
positive primitive list of length five containing a positive dilation of
`[1,2,3,4]` or `[1,3,4,7]`. The second family's exact value is proved for all
`s >= 2`; its `s = 1` value is `2/11`. These are unconditional mathematical
proofs, with no published family theorem as a premise.
See [the critical-family proof](../results/five-speed-spectrum/CRITICAL_FAMILIES_LEAN.md).

The remaining five-speed classification requires the external geometric norm
bound and the complete modular lifting/enumeration argument. Neither the finite
Python verifier nor the twelve checked values discharge those dependencies.

## Local extension validation, 18 November 2026

The 36 new CUT, loneliness, and density source modules compiled with the pinned
toolchain. Each passed an independent `leanchecker` replay. The combined axiom
audit checked 1,025 theorem declarations across the four new namespaces and
allowed only `propext`, `Classical.choice`, and `Quot.sound`. The root
imports, required declarations, and kernel replay list include the new modules.
The full-package rebuild and hosted CI are recorded separately; the module
receipts alone are not a claim that every repository result is formalized.


## Exact density theorems

`SymmetricFourPoint.symmetric_four_point_densities` proves both parity cases
for every positive coprime pair `a < b`. The proof includes the literal tile
interpretation, exact supremum/infimum definitions, periodic attainment, and
both sharp local interval lengths. See
[the checked scope](../results/symmetric-four-point-density/LEAN.md).

`NonmixedGap.nonmixed_gap_density` proves both the actual packing density and
the real circle maximum for every positive coprime gap pair and arbitrary
positive gap counts. Euclidean division handles either sign of `a-b`.
`nonmixed_gap_periodic_optimum` proves attainment by a periodic packing of the
literal tile. See [the checked scope](../results/nonmixed-gap-packing/LEAN.md).

The shared density definitions use centered intervals `[-N,N+1)`. Their finite
window bounds hold uniformly over translations; the exact endpoints do not
assume periodicity of competing center sets. Common-divisor normalization is proved by exact residue counts and periodic
block expansion. `translated_symmetric_four_point_densities` covers arbitrary
integer translations and arbitrary common divisors.
`nonmixed_gap_density_general` and `nonmixed_gap_general_periodic_optimum`
remove the coprimality premise from both nonmixed-gap endpoints.

`Loneliness.Normalization.primitive_representative` proves that division by the
gcd preserves the actual value, list length, positivity, and distinctness and
produces a primitive list. Its `critical_family_below_threshold` removes the
primitivity premise from the checked critical-family reduction.


The norm-reduction development additionally proves coefficient-rounding density
transfer for arbitrary real subspaces modulo integer vectors. Its space value
is identified with the real-time loneliness value for speed lines.
`Loneliness.NormArithmetic.five_speed_threshold` proves the numerical threshold
from explicit lattice-product and larger-subspace hypotheses. The geometric
hypotheses and external exhaustive classifications remain open; the theorem
is not presented as an unconditional norm bound.
See [the exact reduction and dependency stack](../results/five-speed-spectrum/NORM_REDUCTION_LEAN.md).

## Common loneliness interface

`LonelinessPairBridge.lean` proves equality of the fractional-part and
nearest-integer distances, and of finite-set score and list clearance.
`Loneliness.exists_pair_sum_maximum` gives the pair-sum maximizer for the shared
`Loneliness.value`; `certified_pair_value` turns the finite Boolean checks into
that same real supremum. The earlier certificates now live in
`Loneliness.PairSum`, avoiding declaration collisions.

## Rectangle combinatorial inputs

`RectangleFinite.shelf_packing` assigns every positive width list to at most Q
strips of width B when every width is at most M≤B and the total is at most
Q(B−M). It preserves the input list exactly and applies at every size.
`RectangleFinite.deletion_count_bound` proves that deleting parts
below a from any finite family of partitions of T loses at most a factor
(T+1)^(a−1). Its proof recovers each original partition from the retained
multiset and the bounded small-part multiplicities. Both modules passed
warning-as-error source checks and independent kernel replay.

## Gap-five and gap-seven character classification

The nine `DistanceGraph` modules prove `gap_five_value` and `gap_seven_value`
for every positive integer parameter, with the seven/nine residue tables and
21 small value certificates. `corrected_prediction_strict` proves the infinite
strict-discrepancy branch; `counterexample_character_difference` is the exact
1/2958 difference at k=50, where the true character value is 25/58.
All nine modules passed strict source checks and independent kernel replay;
all 263 namespace theorem declarations passed the standard-axiom audit.
The separately checked `ThreeDistanceGraph` endpoint below completes the
actual-density classification. Haralambis permits repeated entries and
therefore also applies directly at k=1.


## Complete Haralambis theorem, 18 November 2026

`Haralambis.three_difference_theorem` proves the full result for every function
`d : Fin 3 → ℕ` with positive entries. The extremal density is the supremum
of the actual upper densities of all subsets of the integers avoiding the
three differences. The circle value is the existing real-time supremum of
the minimum distance to the nearest integer. The same theorem supplies an
avoiding set of period `d i + d j`, with `i ≠ j`, whose density is that supremum.
Repeated entries are allowed; distinct triples are included.

The finite proof constructs balanced signs on the defect multigraph, obtains
three square identities, and derives an odd integer period vector by finite
weighted sums and Bézout. Pair inequalities give intersecting real intervals.
Uniform finite-window counting proves the density upper bound for arbitrary
sets. Exact residue counts remove the gcd. A compactness argument places a
circle maximizer at a pair-sum denominator, and the rational-character
packing theorem preserves that denominator even for a nonprimitive character.
No infinite cocycle extension or external Haralambis theorem is a premise.

`Haralambis.example_two_five_nine_centers` checks the literal period-seven
center set with residues `0,1,4`; both its density and the optimum are `3/7`.
See [the complete checked scope](../results/haralambis-three-differences/LEAN.md).

`Loneliness.Packing.one_div_length_add_one_le_density` additionally proves the
general greedy packing lower bound. Combined with Haralambis,
`Loneliness.SmallRunner.lonelyRunnerBound` proves the lonely-runner bound for
at most three speeds. No small-runner theorem is left as a hypothesis.

The new coalescence files prove that a coordinate-free rational subspace of
dimension `d` in `n` coordinates contains an integer direction with at most
`n-d+1` distinct absolute speeds. The real span has the same dimension, and
subspace extensions by independent projected integer vectors have the claimed
dimension and coefficient-rounding value bound. The dimension-three, -four,
and -five lower bounds in five coordinates now follow unconditionally.
The lattice covolume, successive minima, cube-section estimate, and four-speed
classification remain explicit outstanding dependencies of the full norm bound.

All twenty new modules passed source compilation and separate independent
kernel replay. The Haralambis/packing audit checked 233 declarations, and
the coalescence and small-runner headline checks used only `propext`,
`Classical.choice`, and `Quot.sound`. The combined accepted-package axiom audit checked 5,077 theorem declarations
and accepted only those three axioms. Hosted source and kernel validation for
this checkpoint are tracked separately.

The earlier density/CUT/loneliness checkpoint `6c095083d6c17eff3797f798cbfe35d0ea98c1f6`
passed the complete [hosted Lean workflow](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44433833213),
including the source build, project axiom audit, and every registered kernel replay.

`DistanceGraphOddCycle.lean` separately proves the exact l/(2l+1) density
for every pair {1,2l}, l>0, with periodic attainment and an upper bound for
arbitrary avoiding sets. Its source, kernel and 30-theorem axiom checks passed.

## Combined verified checkpoint, 18 November 2026

The immutable verification gate for commit `c0cf593d22cfb8bb927274a3032b664a32ad45cd`
completed locally with exit status 0.
The full source build passed. Both the compiled audit and the direct
warning-as-error audit checked 6,954 project theorem declarations and accepted
only `propext`, `Classical.choice`, and `Quot.sound`.

All 152 proof modules registered in that snapshot and both project roots completed the pinned
`leanchecker` replay. The script checked that the registered list equals the
local project source-import closure, staged the exact accepted compiled objects
including private/server data, and used the unchanged checker on the two
project namespaces. The replay finished with 154 reported targets and its
success footer. Accepted mathematical sources remained unchanged during the
gate. The theorem count includes helper declarations and is not a count of
independent mathematical results.

Two additional negative controls passed: the ownership-based audit rejected
an unused private project axiom, and the replay helper rejected an incomplete
module list before launching the checker. Temporary controls are outside the
repository's proof sources.

The Pham orbit/recurrence extensions, further concrete CUT certificates,
compact-group Motzkin work, and Erdős 607 work remain separate ongoing source
trees. Their unfinished scope is not covered by this receipt. Hosted CI for
the publication is a separate validation run.

## Additive integration, 19 November 2026

The merged accepted package contains 177 proof modules and two roots. Its
registered replay list equals the source-import closure. The combined
`lake build` passed, followed by a direct warning-as-error `ProofAudit.lean`
check. Both the compiled and direct audits checked 7,581 project theorem
declarations and accepted only the three standard logical axioms. The local
repair-and-integration runner completed with exit status 0.

The kernel receipts have the following exact scope:

- The `c0cf593d22cfb8bb927274a3032b664a32ad45cd` gate above replayed its
  152 proof modules and both roots. Of those proof sources, 150 remain
  byte-for-byte unchanged in this integration.
- The 25 additional proof sources match
  `a7b1ca1a96abc67e1dbc6c547629409c25ad2964` byte-for-byte. They rebuilt locally,
  and that commit's [hosted Lean run](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44439617882)
  passed source compilation, axiom audit, and independent kernel replay.
- The two changed proof sources, `RectanglePacking.lean` and
  `RectanglePartitionCounts.lean`, now use `RectangleFinite` instead of
  `RectanglePartitions`. Their statements and proof bodies are unchanged.
  Both passed fresh warning-as-error source checks and independent kernel
  replay of their exact local import closures. The rename resolves the
  duplicate `RectanglePartitions.shelf_packing` declaration detected by the
  first combined root build.

These component receipts cover every accepted proof module. The full hosted
replay of the merged publication is a separate run and was not yet available
when this integration receipt was written. Unregistered Pham, finite/compact
Motzkin, concrete CUT, Erdős 607, and other teams' candidate work is excluded
from this accepted-module count.

## Complete distance-graph classifications, 18 November 2026

`ThreeDistanceGraph.gap_five_classification` and `gap_seven_classification`
prove the complete tables for every positive `k`, for the actual upper-density
supremum and the actual real-time circle maximum. The proof applies the
checked Haralambis theorem, reduces a maximizer to one of three pair-sum
denominators, and proves each residue-class bound by integer arithmetic.
Exact rational interval certificates discharge the small cases.

`gap_five_periodic_classification` and `gap_seven_periodic_classification`
supply actual periodic avoiding sets. The Conjecture 39 residue-five branch
has density `(4k+25)/(9(k+8))` for `k>=41`, `k mod 9=5`; its claimed value
exceeds this by `(k-41)/(9(k+1)(k+8))`. The proof gives strict counterexamples
for every `k=50+9n` and proves that their set is infinite. At `k=50`, the
checked discrepancy is `1/2958`.

All ten modules passed source compilation and independent kernel replay.
The namespace axiom audit checked 399 declarations with only the three
permitted logical axioms. See [the complete checked scope](../results/distance-graph-densities/LEAN.md).
The `ThreeDistanceGraph` prefix avoids collisions with a concurrent team's
independent `DistanceGraph` development.

## Rectangle components, 18 November 2026

Seven finite modules prove the actual grid-placement and multiset semantics,
shelf packing, recovery after unit-square filling, finite bounded-partition
counts, deletion multiplicity, and the logarithmic packing lower bound.
Their 125 theorem declarations passed the whitelist audit and all seven
modules passed independent kernel replay.

Four analytic modules prove the finite Euler-product bound, the sharp limit
`t*logEuler(B,t) -> pi^2/6` when `t -> 0+` and `B*t -> infinity`, and the
uniform ordered-rectangle and diagonal upper bounds. Mathlib's checked
Basel-sum theorem supplies the exact constant. The 38 analytic theorem
declarations passed the same axiom audit; all four modules were independently
replayed. These were partial components at that checkpoint; the complete theorem is
recorded in the later rectangle receipt below.
See [the checked components](../results/rectangle-partition-asymptotics/LEAN.md).

## Two-direction plane reduction

`Loneliness.CoordinateSubspace.two_integer_directions` proves that every
coordinate-free rational plane in `n` coordinates is spanned by two integer
vectors, both having nonzero coordinates and at most `n-1` distinct absolute
speeds. The coalescence step can avoid a prescribed nonzero-coordinate point;
its coefficients remain exactly `+1` or `-1`.

`two_critical_integer_directions` applies this in five coordinates below
value `2/9`, with the exact `FourSpeedGap` statement retained as an explicit
hypothesis. The gap states that four distinct positive speeds below `2/9`
are a dilation and permutation of `[1,2,3,4]` or `[1,3,4,7]`. This hypothesis
is not an axiom or a proved classification. The at-most-three-speed cases
are discharged by the previously checked small-runner bound. The four new
modules passed source, axiom, and independent kernel checks.


The combined accepted-package audit for this checkpoint checked 5,655 theorem
declarations and accepted only the three permitted logical axioms. All
twenty-five new modules passed individual source compilation and independent
kernel replay. The generated distance-graph examples reproduce byte-for-byte.
The source build and full hosted replay for this commit are tracked separately.

## Complete Pham denominator result, 19 November 2026

`DenominatorForest.pham_denominator_counterexample` proves the complete
primary result for the word `0001001011`.
`DenominatorForest.pham_dual_denominator` proves the stated reverse-complement
result for `0010110111`. Both words have length ten and distinct rotations.
Their reduced denominators have degrees five and ten, respectively.

The proof uses actual positive multiset partitions. It proves the complete
inverse-move correspondence, the repeated-word forward cycles, and the
cardinality of each first-entry orbit level. For every depth `n`,
`primary_level_stabilizes` and `dual_level_stabilizes` identify the exact finite
level with the limiting coefficient for every repetition count `k ≥ n + 2`.
`IsOrbitLevelLimit` explicitly quantifies over all coefficients and all
sufficiently large repetitions.

Finite head/tail recursions derive the two formal-power-series identities.
The rationality and degree bounds used in the original written certificate
are not hypotheses of these endpoints. Coprimality is proved, and
`Denominator.reduced_denominator_dvd` shows divisibility into every alternative
nonzero denominator, giving the exact minimal degrees. The common degree-ten
denominator identity is proved as a separate statement.

The strict source sweep completed successfully. The ownership-based audit
checked all 1,080 Denominator theorem declarations, including private
declarations, and accepted only `propext`, `Classical.choice`, and `Quot.sound`.
The unchanged pinned `leanchecker` independently replayed all 36 project
modules in the exact local import closure of `Conjectures.DenominatorTheorem`.
Both source/audit and kernel runners returned exit status 0; the replay
printed its completion footer.

The 418 polynomial-recursion identities and their aggregate certificates were
checked in Lean. All 15 generated Lean files reproduced byte-for-byte from
the deterministic producer. The [direct proof guide](../results/pham-denominator-degree/FORMAL_PROOF.md)
explains the mathematical construction and its correspondence with the code.

## Checked finite Motzkin theorem, 19 November 2026

For every finite abelian group algebraically generated by the two marked
elements, `Motzkin.finite_two_difference_theorem` supplies an independent set
and a circle-valued additive character attaining the same normalized value.
It proves maximality against every independent set and every such character.
Zero marked elements are allowed; no cyclic-group assumption is used.

`Motzkin.finite_density_eq_characterValue` states the equality for the actual
measurable-set and continuous-character suprema with invariant probability
measure on the finite discrete group. `Motzkin.characterValue_le_density`
proves the general character lower bound for Borel probability measure.
The signed-grid, cocycle and defect arguments are internal proof steps.

Eight new modules passed source checks. The Motzkin audit checked all 115
namespace theorem declarations and accepted only the three allowed logical
axioms. Independent kernel replay completed all 12 project modules in the
exact local closure of `Conjectures.MotzkinDensity`, with exit status 0 and the
completion footer. The eight source files remained unchanged during replay
and registration preparation.

The arbitrary compact-group upper bound, the annihilator evaluations and
cyclic sharpness criteria, and the full exact algorithm with its complexity
bound remain separate unfinished work. The imported character-separation and
biduality developments are not part of this finite checkpoint.

## Pham and finite Motzkin integration receipt

Registration adds 42 previously checked modules to `c862951`: 34 Denominator
modules and eight Motzkin modules. The accepted package now contains 219 proof
modules and two roots. The replay helper verified that its 221 targets equal
the exact local source-import closure.

The combined `Conjectures.lean` root passed a fresh strict pinned-Lean source
check against the checked objects. `ProofAudit.lean` then passed its strict
source check and audited 8,653 project theorem declarations, including private
declarations. Only `propext`, `Classical.choice`, and `Quot.sound` were accepted.
All accepted source hashes were checked before and after this integration
gate; the runner returned exit status 0.

The 36-module Pham and 12-module finite Motzkin kernel receipts above cover
every new proof module. The full package rebuild and whole-package replay in
the hosted workflow are tracked separately from these local component checks.

## Complete rectangle asymptotic, 19 November 2026

`RectangleAsymptotics.uniform_log_asymptotic` proves that one height threshold
works for every larger height and every width `w ≥ h`:

```math
\left|\frac{\log p(h,w)}{\sqrt{hw\log\min(h,(hw)^{1/4})}}
      -\pi\sqrt{2/3}\right|<\varepsilon.
```

The count uses finite, integer-sided, axis-parallel blocks at arbitrary real
positions. Rotation and arrangement do not distinguish block multisets.
`realTiles_iff_gridTiles` and `realRectangleCount_eq` prove the exact bridge
to the grid count; `RealTiling.cover_closed` checks the outer boundary.
The joint-filter and arbitrary-filtered-family endpoints are also proved.

The proof derives the cumulative bounded-partition asymptotic from finite
Euler products and tail estimates. It verifies both strip/column reservation
budgets, all floor errors, the harmonic active range, and the negligible
small-part deletion loss. The exact Basel constant closes the uniform squeeze.
There is no unproved Hardy–Ramanujan or real-tiling premise.

All 46 modules passed source and stock kernel checks; the final audit checked
587 theorem declarations and permitted only the three standard logical
axioms. Eleven inherited source files match the successful `a7b1ca1` hosted
checkpoint. The 35 new modules have local source, axiom, and kernel receipts.
See [the complete scope](../results/rectangle-partition-asymptotics/LEAN.md)
and [source hashes](../results/rectangle-partition-asymptotics/lean-verification-receipt.json).

## Finite planes and coordinate cutoffs, 19 November 2026

`Loneliness.Pigeonhole.four_speed_cutoff` proves that every coordinate of a
positive primitive four-speed tuple below value `2/9` is at most 5,832.
It assumes neither distinctness nor the four-speed gap. The proof combines
an exact finite pigeonhole approximation with the proved three-speed bound.

The 64 plane certificate blocks cover all `8 × 8 × 120 × 16 = 122,880`
indexed direction pairs. Both [run 44446557652](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44446557652)
and [run 44447687031](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44447687031)
passed every row's source check, independent stock kernel replay, and axiom
audit. Every generated-source hash, support-source hash, and generator hash
was checked against the retrieved receipts. The second run also retained
compiled artifacts; their ZIP digests and source hashes matched.

The semantic normalization, admissibility, product-plane identification,
finite-coverage aggregate, and spectrum conversion passed separate source,
axiom, and kernel checks. `critical_product_of_low_value` now discharges
finite coverage internally; `FourSpeedGap` remains an explicit mathematical
input of this accepted theorem.

With that input, `five_speed_finite_or_critical_quadruple` bounds every
positive primitive nonfamily five-speed tuple below `1/5` by `23^4 = 279841`.
The weaker `five_speed_finite_or_spectrum` also follows. The two structural
modules passed their six-declaration audit and separate stock kernel replays.
This does not establish the enumeration of the bounded tuples.
See [the plane proof](../results/five-speed-spectrum/PLANE_REDUCTION_LEAN.md),
[the cutoff proof](../results/five-speed-spectrum/PIGEONHOLE_REDUCTION_LEAN.md),
and [the finite receipts](../results/five-speed-spectrum/plane-certificate-receipts.json).

## Combined rectangle and plane integration, 19 November 2026

The accepted source-import closure now contains 338 proof modules and two
roots. The registration script checked exact equality between that closure
and the replay list. Both combined root compilations passed with the pinned
Lean toolchain and the configured 4,500 MB allocation limit. The final
warning-as-error `ProofAudit.lean` compilation passed at 6,000 MB and checked
9,424 project theorem declarations, including private declarations. It
accepted only `propext`, `Classical.choice`, and `Quot.sound`.

The 119 newly registered modules consist of 35 rectangle modules and 84
plane/pigeonhole modules. Every new proof source has a successful component
source check, transitive axiom audit, and independent stock kernel replay.
The inherited 219 accepted modules retain the source-matched receipts from
the preceding checkpoints. The finite plane blocks also have both complete
hosted matrix receipts recorded above.

The full combined audit took about nine and a half minutes and exited
successfully; no interruption or partial audit is counted as a pass.
This integration uses the exact frozen proof sources. The hosted package
build and complete combined kernel replay are a separate validation run;
no hosted result for this publication was available when this receipt was
written.

The [integration receipt](rectangle-plane-integration-receipt.json) records
the exact accepted source hashes, root hashes, and gate results.


## Complete concrete CUT games, 19 November 2026

`CutPeriod.Weight.both_games_exact` proves equality of the actual recursively
defined `CutFamily.gameValue` with the stated candidate for cuts `{1,2,8}` and
`{1,2,7,8}`, including pile zero. Its `ExactArithmeticParameters` conclusion
states all four requirements: period 12 with saltus 8 holds from pile 7; every
positive eventual arithmetic period is at least 12; every period-12 saltus is
8; and the period-12/saltus-8 law holds from a start exactly when that start is
at least 7. This gives preperiod 6 on positive piles.

The seven `CutPeriodWeight*` modules prove finite shape classification,
collision exclusion, lower-option construction, both actual mex equations,
and game identification. A quotient/residue representation reduces collisions
to finitely checked weight masks. Explicit lower-option templates lift to all
quotients. The extra eight-pile options in the second game remain collision
free. Both generated table files reproduce byte for byte from
`generate_weight_certificates.py`. The large higher-pile automata drafts are
preserved, but are not dependencies of this complete proof.

All seven sources passed their checks. The ownership-based closure audit
checked 1,127 theorem declarations and allowed only `propext`,
`Classical.choice`, and `Quot.sound`. The pinned unchanged independent checker
replayed all 23 project modules in the exact import closure successfully.
Frozen source, generator, manifest, and toolchain hashes matched after replay.

## Erdős 607 checked foundations, 19 November 2026

Seven modules are accepted as components of the full line-size result:

- `LineSizeCost` and `LineSizeGeometry` prove the incidence cost bound for actual
  distinct affine lines in the real plane, with their actual point counts.
- `LineSizeCore` proves existence and uniqueness of the positive core, the
  staircase and tail bounds, and the exact core cost formula.
- `LineSizeImported.SylvesterGallai` and `LineSizeOrdinary` prove ordinary-line
  existence for every noncollinear finite real-plane point set, and bridge the
  coordinate determinant statement to Mathlib affine lines and collinearity.
  The upstream source is pinned, ported locally, and retains its CC0 license
  and provenance. No Sylvester–Gallai theorem is assumed as an axiom.
- `LineSizeGraphCounts` proves the selected-graph incidence degree identities,
  exact tail degrees, core capacity bounds, and the total point-cost identity.
- `LineSizeCoreGaps` gives an explicit core/gap equivalence and both inverse
  identities, its exact weighted sum, the last-gap shift, and the exceptional
  minimum weights 3 and 6 for core lengths one and two.

The ordinary-line, selected-graph, and core-gap closures passed strict source
checks and independent kernel replay of respectively four, three, and three
project modules. Their ownership audits checked 54, 97, and 122 theorem
declarations respectively, allowing only the three standard axioms. These
closures overlap; these numbers are not separate mathematical-result counts.
Their seven distinct source files matched the frozen replay hashes.

The actual geometric construction and padding, the bijection to full records,
the exact generating function, and the sharp asymptotic prefactor remain
ongoing work. This result is partial.

## Hosted verification of the Pham/finite-Motzkin checkpoint

Commit `18bf908ae3b19c293aba07944d339e5193ec483f` passed the complete hosted Lean
workflow: [run 44450524136](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44450524136),
job `135313034960`. Source build, the project axiom audit, and independent
kernel replay all succeeded for its 219 proof modules and both project roots.
This confirms the complete published Pham result and the stated finite Motzkin
scope; it does not establish the still unregistered compact-group theorem.

## CUT and line-size foundation integration, 19 November 2026

Fourteen checked proof modules are added to the 338-module rectangle and
plane checkpoint: seven complete CUT modules and seven line-size foundation
modules. The accepted import closure and replay list agree exactly on
352 proof modules and two roots. Every inherited proof source matches its
previous receipt, and every new proof source matches the component source,
axiom, and independent kernel checks recorded above.

Before this merge, the 233-module CUT/line-size snapshot passed a fresh
strict root compilation and the complete 9,035-theorem ownership audit.
The root compilation took 311.6 seconds; the audit took 677.8 seconds.
These checks and the separate 338-module rectangle/plane receipt establish
component coverage. The full 352-module hosted rebuild, combined audit,
and whole-package kernel replay remain a separate pending check.

The [integration receipt](cut-line-integration-receipt.json) records the
frozen accepted sources and both validation scopes. Unregistered line-size
and Motzkin candidates are excluded from the accepted roots and replay list.

## Graph theorem, runner families, and deterministic hyperplane registration

This checkpoint registers 27 additional proof modules and preserves the complete
rectangle/plane registration. The separately checked snapshot has 365 proof modules
and two roots. Its replay list matches that source-import closure exactly.

The all-order Graffiti.pc318 theorem and its sharpness example are complete.
The consecutive families for counts 2 through 14, both exceptional eight-speed
families, all three stated eight-speed product-family classifications, and the
listed higher-speed examples are registered components. The exact shifted
hyperplane maximum, attainment, and orthogonal-velocity upper bound are also
registered. The remaining runner classifications and hyperplane statistics
are not marked complete.

All 27 added modules passed their individual local Lake source gates. The
strict combined roots passed at a 4,500 MB allocation limit. The complete
warning-as-error ownership/axiom audit passed at 6,000 MB, checking **10,144**
project theorem declarations, including private declarations, and allowing
only `propext`, `Classical.choice`, and `Quot.sound`. The audit completed in
about 563 seconds and exited successfully.

The source-identical `base`, `product`, and `hyperplane` jobs in
[run 44451283261](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44451283261)
passed source builds, transitive axiom audits, and independent stock kernel
replay of their complete project closures. Their union covers every added
module. All 338 inherited proof-source hashes match the prior integration
receipt. The earlier 219-module accepted snapshot also passed its complete
hosted gate in run 44451283317. No interrupted broad local Lake build is
counted as a full build; the full merged hosted package gate remains a
separate check after this publication.

See the [source hashes and gate receipts](graph-family-hyperplane-integration-receipt.json).


## Concurrent registration union

The graph, runner-family, and deterministic-hyperplane registration is merged
additively with the 14 CUT and line-size modules from `5981218`. The accepted
import closure and replay list agree on **379 proof modules and two roots**.
All accepted proof sources match the union of the two component receipts.
The 365-module, 10,144-theorem local audit described above does not include
those 14 concurrent additions. Their checked scope is recorded separately
in the CUT/line-size receipt. A full 379-module combined source, axiom, and
kernel run remains pending; neither earlier receipt is relabeled as that run.
The five-speed candidates from `06747c7` remain outside the accepted roots.

## Erdős 607 geometry and analytic profile, 19 November 2026

`LineSize.exists_large_record_iff` proves both directions of the literal
real-plane realizability criterion. The construction provides actual
carrier lines, canonical distinct intersections, exact filling, and generic
padding, with no unintended three-point line. Ordinary-line existence and
the collinear case give `LineSize.lineSizeCount_eq_tupleCount` for every
natural n, including zero, one, and two.

The geometry job in [run 44456107859](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44456107859)
passed every source, the 342-theorem ownership audit, and unchanged pinned
kernel replay of all 20 project modules. The smooth Euler-kernel job in
the same run passed its 11-theorem audit and one-module kernel replay.

`LineSize.Profile.saddle_profile_exact` establishes the exact integral
constant, saddle at log 2, curvature 3, and the mean/variance identities
for the literal functions in the proof. The global Gaussian phase bound
is proved too. Its five-module closure passed local source checks, the
137-theorem ownership audit, and full independent kernel replay. The
integral constant is derived from the exponential series and the Basel
sum; no dilogarithm evaluation is assumed.

This registration adds 18 proof modules to the concurrent 379-module
checkpoint. The exact accepted closure is 397 proof modules and two roots.
Every added component has source-matched axiom and kernel coverage. The
full merged hosted build/audit/replay remains pending. The shared
`HaralambisFaces` lint repair also passed source, its complete 62-theorem
audit, and independent replay without changing any theorem statement.

See the [source-bound integration receipt](line-size-integration-receipt.json).
The formal generating function and corrected Euler-product sources remain
unregistered candidates. The Fourier local limit and the final asymptotic
prefactor are still being formalized; Erdős 607 is not yet complete.


## Complete four-speed gap and runner bound

The accepted package now contains `Loneliness.CoordinateSubspace.four_speed_gap`,
`four_speed_below_gap_value`, and `four_speed_lonelyRunnerBound`. For every
positive distinct four-speed list with value below `2/9`, the first theorem
identifies a positive scaling and permutation of `[1,2,3,4]` or `[1,3,4,7]`.
Both directions have value exactly `1/5`. The runner lower bound covers every
nonempty distinct positive list of length at most four.

The proof joins the unconditional coordinate cutoff 5,832 to the ten exact
prime residue covers and their exhaustive lifting certificates. It assumes no
unformalized four-speed theorem. The finite plane and five-speed reductions
can now use this proved gap input; their bounded five-speed classification is
still separate work.

The exact four-speed closure contains 84 project modules. Its ownership and
transitive axiom audit passed for 1,880 theorems, including private declarations.
The four aggregate modules passed fresh strict source checks and stock
independent kernel replay. A dependency-coverage check identified the separate
`LonelinessFourSpeedClassification` module; that module then passed its own
fresh strict source check and independent replay. Every other dependency has
an exact source-matched accepted or hosted leaf receipt.

This registration preserves the concurrent 18-module line-size addition and
adds 36 proof modules to its 397-module package, giving 433 accepted proof
modules and two roots. The import closure and replay list agree exactly.
Inherited sources match the line-size integration receipt or the subsequent
five-module profile gate, which passed at `65435fc` with a 120-theorem audit.
The proof-only `HaralambisFaces` lint repair is a shared four-speed dependency and
has separate fresh source, 62-theorem audit, and kernel checks; the earlier
84-module audit keeps its original source snapshot. These are component
receipts; a whole 433-module combined hosted pass is not asserted here.
See the [four-speed integration receipt](four-speed-integration-receipt.json)
and the [statement and proof map](../results/five-speed-spectrum/FOUR_SPEED_GAP_LEAN.md).

## General compact Motzkin equality, 19 November 2026

`Motzkin.compact_two_difference_theorem` proves equality of the actual
measurable-set density and continuous-character supremum for every compact
Hausdorff abelian group with Borel measurable space and a given invariant
probability measure. The two differences may be zero. The finitely generated
subgroup they generate need not be closed; no rank, cyclicity, or second
countability hypothesis is added.

[Hosted job 135345252509](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44460317093/job/135345252509)
checked all 34 project sources with warnings as errors, audited all 664 project
theorem declarations against the standard axiom whitelist, and replayed all
34 project modules through the pinned independent kernel checker. The source
and gate hashes remained unchanged. The exact artifact receipt is preserved
in [motzkin-compact-hosted-receipt.json](motzkin-compact-hosted-receipt.json).

This adds 22 proof modules to the concurrent 433-module accepted package.
The combined closure is 455 proof modules and two roots; its full merged
hosted gate remains pending. The
[integration receipt](motzkin-compact-integration-receipt.json) binds every
accepted source to this registration snapshot. The note's further rank,
cyclic, evaluation, and exact complexity claims remain separate candidates.

## Relation formulas, Euler correction, and finite tuple reconstruction

Three previously separate passing components are now registered. Their
statements retain the hypotheses in their exact source receipts.

| Component | Strict source closure | Theorem axiom audit | Independent kernel replay |
| --- | --- | --- | --- |
| Motzkin relation formulas and attainment | 39 modules | 729 theorems | 39 modules |
| Corrected finite Euler product | 8 modules | 122 theorems | 8 modules |
| Finite tuple/core/tail reconstruction | 9 modules | 307 theorems | 9 modules |

`Motzkin.rank_zero_density`, `rank_one_density`, and `rank_two_density`
evaluate the compact density for the relation data stated in each theorem.
`finite_relation_density_attained` constructs an actual Borel avoiding set
when two independent finite relations hold. The formulas take relation
generators as input. A theorem producing the appropriate generators for
every subgroup of the integer plane is still being formalized.

`LineSize.EulerKernel.finiteProduct_correction_exact` proves the literal
finite-product correction with its square-root factor. The accompanying
uniform bound controls the logarithmic error by a constant times the positive
scale on each fixed compact range of positive `r*t`. The proof includes the
Stirling remainder and a trapezoidal estimate for the smooth regular part.

The tuple component proves canonical reconstruction, exact cost weights, and
the identity relating cumulative and exact-cost formal series. It does not
yet establish the complete explicit generating function.

The new registration adds 13 proof modules to the 455-module package, giving
468 proof modules and two roots. All inherited proof source hashes match the
preceding registration. The full merged hosted gate remains pending.
See the [integration receipt](motzkin-relations-euler-tuples-integration-receipt.json),
[Motzkin receipt](motzkin-relations-hosted-receipt.json),
[Euler receipt](line-size-euler-correction-hosted-receipt.json), and
[tuple receipt](line-size-tuples-hosted-receipt.json).


## Exact generating function and cyclic Motzkin formulas, 19 November 2026

Both components passed strict source checking with warnings treated as errors,
the complete project-theorem axiom audit, and independent replay with the
unchanged pinned checker at `8da1d13a6d09a740bda9300205a22c2da2a5f03b`.
Their recorded source hashes match the registered sources.

| Component | Strict source closure | Audited theorems | Kernel replay |
| --- | --- | --- | --- |
| Exact coefficientwise line-size generating function | 14 modules | 496 | 14 modules |
| Cyclic Motzkin formulas and sharpness | 48 modules | 812 | 48 modules |

`LineSize.Generating.exactCount_formula` and
`one_sub_X_mul_tupleCountSeries_eq` identify the literal formal series from
canonical core encodings, including the exceptional small cores. The finite
product denominators are proved coefficientwise. Convergence at complex
arguments and the coefficient asymptotic remain separate candidate work.
See the [generating-function receipt](line-size-generating-function-hosted-receipt.json)
and [hosted job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44462991011/job/135354045624).

`Motzkin.Cyclic.finite_cyclic_theorem_all` covers every positive modulus;
`independenceNumber_gcd` proves the component scaling. The generated-case
Hermite basis and odd-closed-walk sharpness criterion are proved. For the
stated modulus 24 with jumps 3 and 4, the independence number is 9, the odd
girth is 7, the odd-cycle upper bound is 10, and no pair is sharp. Rational
circle density and abstract Borel attainment are also proved. The explicit
finite union of half-open intervals remains a candidate construction.
See the [cyclic receipt](motzkin-cyclic-hosted-receipt.json) and
[hosted job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44462990839/job/135354043741).

Registration adds six generating-function modules and eight cyclic modules,
giving 482 proof modules and two roots. The empty cyclic candidate wrapper
is omitted; four real imports cover all 47 real modules in its checked
closure. All 468 inherited proof source hashes remain unchanged. The
combined hosted gate is pending. The
[integration receipt](generating-cyclic-integration-receipt.json) records
all accepted source hashes and the component evidence.

## Full hosted verification of the 397-module checkpoint

The complete accepted-package workflow at
`42fff1a2f87955f29c25beb0d16f23d46e91b489` has now passed its source build,
10,843-theorem axiom audit, and independent pinned kernel replay of all
397 proof modules and both roots. The completion log is dated 19 November
2026 at 05:02:59 UTC. See
[run 44458108002](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44458108002)
and the [exact-commit receipt](full-397-hosted-receipt.json).
This historical receipt does not verify later source revisions or additions.

## Hosted replay of the four-speed integration snapshot

On 18 November 2026, [run 44459759725](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44459759725)
completed the full accepted-package gate at
`3349777d40eacc26df93df09dad3d95c0333e59b`. The source build passed, the
axiom audit checked 11,867 project theorem declarations, and stock Lean
4.35.0 replayed all 433 proof modules and both root modules. Only
`propext`, `Classical.choice`, and `Quot.sound` occurred in the audit.

The [machine-readable receipt](accepted-3349777-hosted-receipt.json) lists
every replayed module. Later registrations require their own merged hosted
receipts; this snapshot covers only the 433-module integration commit.


## Five-speed finite certificate checkpoint, 19 November 2026

All 260 scalar tables and 574 required canonical-plane candidates are now
published in 24 separately gated groups. Their complete hosted gates are
still running. The 29-module cached-root checkpoint at `108168d` passed its
full hosted source, axiom, and stock-kernel gate. The new packed selector
and oracle let the previously failing p1789 ordinary row compile locally.
The repaired map 26 and bounded block helper passed their local source,
axiom, and independent kernel gates. Eight new groups cover all 164 maps;
the final aggregate and complete root-prime coverage remain open. See
[the scoped checkpoint](five-speed-packed-bounded-candidates.md). Accepted
roots are unchanged, and Li remains last.


## Five-speed root candidate and component gates, 19 November 2026

The 227-module finite-assembly closure passed hosted source compilation,
the owned transitive axiom audit, and stock-kernel replay. Its coverage
hypotheses are still explicit. Five of the 24 scalar/plane groups also
passed their complete hosted gates. A complete p179 root candidate is now
published in 14 modules; only its cache, packed oracle, helper, and first
part have local source evidence so far. Its full hosted gate remains
pending. See [the exact scope](five-speed-root179-candidate.md) and
[component receipts](five-speed-receipts/hosted-component-index.json).


## Frankl counting components — 19 November 2026

Six proof modules were checked at `57d699c770471fc898850079bde384a269da5d4f` in
[run 44475531664](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44475531664).
All four component jobs rebuilt their exact source closures, audited all
113 project theorem declarations using only `propext`, `Classical.choice`, and
`Quot.sound`, and replayed all six kernel objects with the unchanged pinned
checker. The accepted root, required endpoints, and replay list now include
those exact modules. The full merged-package run is a separate gate.

This verifies the general local-certificate implication, actual graph
bijection, finite lopsided-conditioning theorem, and numerical inequalities.
It does not yet verify either complete Frankl result. See
[the scope and remaining obligations](frankl-formalization.md) and
[the exact hosted receipt](frankl-foundations-hosted-receipt.json).


## Frankl large-generator theorem — 19 November 2026

The full `k ≥ 15` theorem is checked: in every finite `k`-uniform generating family with exactly three generators through each point and pairwise intersections of size at most one, every point belongs to at least `657/1000` of the distinct unions, including the empty union. The cyclic span-four theorem and the `3 ≤ k ≤ 14` high-girth cases remain incomplete.

The exact 16-module closure at `663f72751f7cfb13e533050985072e59204cbd26`
passed strict source checking, a 231-theorem transitive axiom audit, and
independent kernel replay in [job 135402205987](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44477677129/job/135402205987).
The only allowed axioms are `propext`, `Classical.choice`, and `Quot.sound`.
The probability estimates, lopsided dependence, query independence, and
bijection with actual distinct unions are all proved internally. Thirteen
additional modules are registered here. The full merged-package gate is
separate from this exact component receipt.
See [the source-hash receipt](frankl-large-hosted-receipt.json).

## Hadamard automorphism arithmetic

The arithmetic and integral-basis coefficient component passed its exact hosted
checks at `56cb125ec61bbac0d95d2dba9a2099b42a242d78`: strict compilation of
five local modules, a transitive axiom audit of 38 project theorems, and an
independent replay of all five modules with the unchanged pinned kernel.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44478301527/job/135404210981) ·
[Exact receipt](verification/hadamard-automorphism-arithmetic-56cb125e.json).

The accepted source files are `HadamardAutomorphismArithmeticBasic`,
`HadamardAutomorphismArithmetic`, `HadamardAutomorphismArithmeticRational`,
and `HadamardAutomorphismCoefficients`. They prove order 239 for the residue
of 599 modulo 479; the absence of the required integer and rational norm
representations; the exact fifth-power norm witness; and coefficient
congruences in the full ring of integers of the 479th cyclotomic field.
The arithmetic certificate uses ordinary kernel reduction, with no native
computation axiom. The permitted transitive axioms are only `propext`,
`Classical.choice`, and `Quot.sound`.

The full signed-automorphism obstruction and the independent ideal-class proof
are checked below under [issue 21](https://github.com/1337isnot1337/solved-conjectures/issues/21).
Hadamard existence at 2396 remains open.

## Hadamard automorphism Fourier component

At `ee1be6e0e00c49beadf5f3a563473f86346bf618`, the six-module Fourier
candidate closure passed strict compilation, a 32-theorem transitive axiom
audit, and independent pinned-kernel replay with unchanged sources.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44479208216/job/135407227160) ·
[Exact receipt](verification/hadamard-automorphism-fourier-ee1be6e0.json).

The five proof files `HadamardAutomorphismBinary`,
`HadamardAutomorphismDeterminant`, `HadamardAutomorphismFourier`,
`HadamardAutomorphismIndicator`, and `HadamardAutomorphismDeterminantNorm`
are registered. They construct the literal character embedding and Fourier
matrix, prove the inherited Gram equation, replace sign entries by their
negative-position indicators, and prove determinant divisibility and the
norm 599³ quotient from the stated residue obstructions. The binary overlap
lemma is also checked. These general components are connected to the actual signed Hadamard
automorphism theorem by the completed assembly below.


## Hadamard automorphism permutation component

At `e9a9bb45e2935112239380212b5977dd5fca2a2b`, the seven-module
permutation closure passed strict source checks, a transitive axiom audit of
100 project theorems, and independent replay with the unchanged pinned kernel.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44480689737/job/135412036944) ·
[Exact receipt](verification/hadamard-automorphism-permutation-e9a9bb45.json).

The six registered proof files are `HadamardAutomorphismPermutation`,
`HadamardAutomorphismPermutationMatrix`, `HadamardAutomorphismFixedPoints`,
`HadamardAutomorphismPermutationCycles`, `HadamardAutomorphismPermutationIntegral`,
and `HadamardAutomorphismGroupBasic`. They normalize an odd-order signed
permutation by explicit diagonal signs, derive one fixed index and five
479-cycles in each permutation at order 2396, construct compatible cyclic
labels, and transport the real sign matrix into a number field's ring of
integers. They also construct the full signed row/column automorphism subgroup.
The completed assembly below proves that its order is coprime to 479. This
permutation component alone does not prove that obstruction.


## Hadamard quadratic field and class-order component

At `ae7871fc31c478e00b0c1f2778e707081c1af9a2`, the class-order
closure passed strict source checks, a transitive axiom audit of 111 project
theorems, and independent pinned-kernel replay of all nine local modules.
The source files and verification inputs remained unchanged during the checks.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44483833039/job/135422470403) ·
[Exact receipt](verification/hadamard-automorphism-class-order-ae7871fc.json).

Six additional files are registered: `HadamardAutomorphismClassGroup`,
`HadamardAutomorphismCyclotomic`, `HadamardAutomorphismCyclotomicGauss`,
`HadamardAutomorphismCyclotomicQuadratic`, `HadamardAutomorphismQuadraticNorm`,
and `HadamardAutomorphismClassOrder`. They construct the actual Frobenius and
quadratic fixed field, a generator whose square is −479, and a quadratic model
whose algebraic norm is the required quadratic form. They exclude absolute
norm 599 for quadratic integers. The explicit fifth-power norm witness then
constructs a prime ideal above 599 with norm 599 and proves that its ideal class
has exact order five. The proof establishes principality of the fifth power
and nonprincipality of the prime itself.

This earlier component constructs such a prime. The stronger universal
prime-pair and independent relative-ideal-norm results have since passed the
separate checks recorded below, as has the full signed-automorphism theorem.


## Hadamard cyclotomic norm obstruction

At `7098a0e8dccd5273be61bdb4108529dbcd169544`, the twelve-module
cyclotomic closure passed strict source checks, a transitive axiom audit of
128 project theorems, and independent replay with the unchanged pinned kernel.
The source files and verification inputs were unchanged throughout the checks.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44485841643/job/135429136270) ·
[Exact receipt](verification/hadamard-automorphism-cyclotomic-7098a0e8.json).

Five more proof files are registered: `HadamardAutomorphismCyclotomicCharacter`,
`HadamardAutomorphismCyclotomicPrimes`, `HadamardAutomorphismDescentIdeals`,
`HadamardAutomorphismDescentUnits`, and `HadamardAutomorphismDescent`.
They construct the integer-valued primitive character and prove that the two
primes above 599 are distinct, conjugate, and unramified, with intersection
equal to the principal ideal generated by 599. Frobenius fixes those primes.
For a hypothetical integer of conjugate norm 599³, the proof constructs the
Frobenius unit ratio, proves it is a root of unity, removes its sign, and twists
the integer into the actual quadratic fixed field. The checked quadratic norm
exclusion then proves `cyclotomic_norm_cube_impossible`. No descent or norm
obstruction is assumed as a hypothesis.

The completed signed-matrix assembly and independent class-group proof are
recorded below. The additional uniqueness and exact integer-coordinate
endpoints are checked in the final component below. Hadamard existence at 2396 is not asserted.


## Complete Hadamard order-479 automorphism obstruction

At `fb6b6e068efa37c5b5834b8f969211c951cac2d5`, the assembly closure
passed strict source checks, a transitive axiom audit of 297 project theorems,
and independent pinned-kernel replay of all 28 local modules. Source and gate
hashes matched the published snapshot and remained unchanged during checking.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44486671857/job/135431911100) ·
[Exact receipt](verification/hadamard-automorphism-assembly-fb6b6e06.json).

`HadamardAutomorphismAutocorrelation`, `HadamardAutomorphismMatrixObstruction`,
`HadamardAutomorphismMain`, and `HadamardAutomorphismGroup` complete the chain.
Starting from any real matrix with Mathlib's `Matrix.IsHadamard` predicate and
index-set cardinality 2396, the proof normalizes the signed symmetry, derives
one fixed point and five 479-cycles, reindexes the actual matrix, constructs
the indicator Fourier matrix, proves nonzero reductions at both primes, and
constructs an integer of the forbidden conjugate norm 599³. No symmetry
normal form, Fourier identity, prime nonvanishing, or norm obstruction is an
extra input to the final theorem.

The registered endpoints include `hadamard_signed_pair_order_ne_479`,
`isHadamard_automorphism_card_not_dvd_479`, and
`isHadamard_automorphism_quotient_card_not_dvd_479`. The group carrier contains
all signed row/column permutation pairs preserving the given matrix. The
quotient statement holds for the coset cardinality of every subgroup, and
therefore covers the common-sign quotient.

This completes the automorphism theorem. The sequence restrictions and
fixed-border construction remain separate obligations. The later fixed-border
symmetry result is completed in the section below.

## Complete independent ideal-class norm obstruction

At the same snapshot, the independent class-group closure passed strict
sources, a 164-theorem transitive axiom audit, and independent pinned-kernel
replay of all 15 local modules, with unchanged sources and gate inputs.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44486671857/job/135431911435) ·
[Exact receipt](verification/hadamard-automorphism-class-alternative-fb6b6e06.json).

Five additional files are registered: `HadamardAutomorphismClassArithmetic`,
`HadamardAutomorphismClassPair`, `HadamardAutomorphismNormFactorization`,
`HadamardAutomorphismQuadraticIntegers`, and `HadamardAutomorphismRelativeNorm`.
Every prime above 599 in the actual quadratic fixed field has norm 599 and
ideal-class order five. The proof constructs the distinct conjugate pair and
its inverse classes. A hypothetical integer of conjugate norm 599³ gives a
principal ideal factorization with exponents a+b=3. The relative ideal norm
has residue degree 239 and forces the class exponent 239(a−b) to vanish,
contradicting the order-five calculation. The endpoint
`cyclotomic_norm_cube_impossible_by_class_group` does not import or call the
unit-descent norm obstruction.

The final quadratic-model component below brings the union of registered
Hadamard automorphism proof source modules to 37.


## Complete quadratic integer model

At `0a1deef73d38965fc62e0d42070450079fec850a`, the expanded
cyclotomic closure passed strict sources, a 157-theorem standard-axiom audit,
and independent pinned-kernel replay of all 16 local modules. The checked
sources and verification inputs remained unchanged.
[Hosted check](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44487424755/job/135434449472) ·
[Exact receipt](verification/hadamard-automorphism-quadratic-model-0a1deef7.json).

`HadamardAutomorphismQuadraticUnique` proves that every degree-two intermediate
field of the actual cyclotomic extension is the constructed fixed field, and
identifies it with the field generated by the explicit square root of −479.
`HadamardAutomorphismQuadraticConverse` proves that an element of that field
is integral over the integers if and only if it has the form
(a+b√(−479))/2 with integers a,b of equal parity. The converse uses the monic
polynomial T²−T+120 for the half generator. Both files are registered.

Together with the preceding components, this checks the full automorphism
note, including both norm-obstruction routes and its stated quadratic-field
model. The separate sequence and border notes remain incomplete.

## Frankl local certificate checkers — 19 November 2026

The accepted package now includes `FranklLocalCertificate` and
`FranklLocalMaximalCover`. The first checker tests every boundary pair
`M ⊆ E ⊆ B`. A successful nonzero nonnegative integer weight vector gives
an abundant point in the actual family of distinct unions.

The maximal-cover checker is proved equal to the first checker. For each
inside pattern, it uses the union of all local generators contained in the
allowed inside and exterior set. It therefore avoids enumerating every local
union without changing the compatible-pattern count.

The exact five-module closure at `ad07e385` passed strict source checks, an
explicit import-all audit of 66 project theorems, all eight required endpoint
checks, and the unchanged pinned kernel replay.
[Hosted receipt](verification/frankl-maximal-cover-ad07e385.json) ·
[Scope and reproduction](frankl-fc-formalization.md#local-maximal-cover-checker).

This registration asserts no finite window weight certificate. The cyclic
window data, graph reduction, and complete span-four assembly remain separate.
The full merged-package gate is also separate from this exact component check.

## Frankl FC and small cyclic components — 19 November 2026

The accepted package now contains the full Vaughan shortcut. Every finite
union-closed family containing three distinct triples through a common point
has an abundant point in the union of those triples. The proof has no ambient
ground-size restriction and does not assume that the family contains the
empty set. Classification, integer certificates, and finite-support transport
are all proved in Lean.

Every nontrivial cyclic span-four generator family on at most six sites also
has an abundant point. The proof permits arbitrary generator sizes and cyclic
overlaps. It uses exact search trees, the Vaughan shortcut, a Pasch certificate,
and the two-point shortcut.

Further checked results concern the specified 35-edge residual graph. Its
period-seven, period-eight, and period-ten words are zero. Every nonzero
period-nine word generates a family with an abundant point. These statements
retain explicit residual-graph membership. The reduction of arbitrary larger
cyclic families to that graph still needs its finite window and rank data.

At source snapshot `6544adcc`, the exact 53-module closure passed strict source
checks, an import-all audit of 2,057 project theorems, 56 required endpoint
checks, visibility checks for all 534 private certificate nodes, and stock
kernel replay of every module. The 50 newly registered sources match that
snapshot byte for byte.
[Hosted receipt](verification/frankl-fc-packet-6544adcc.json) ·
[Detailed scope and reproduction](frankl-fc-formalization.md).

The complete span-four theorem and the small-degree high-girth theorem remain
incomplete. The full merged-package gate is separate from these component
checks. Li remains deferred.

## Frankl mask checker and exact domains — 19 November 2026

The accepted package includes `FranklLocalMaskCertificate` and
`FranklLocalMaskDomains`. The mask checker decodes the actual finite generator
family and counts each compatible inside set once. Its domain constructor
proves the exact inside and boundary powersets, including code bounds and
absence of duplicate inside codes. Literal quotient masks can therefore be
checked without assuming an injective unwrapping map.

At `a632fc82`, all ten sources passed strict checking, an import-all audit of
163 project theorems, all 38 required endpoints, and stock kernel replay of
every module. The two newly registered sources match that snapshot exactly.
[Hosted receipt](verification/frankl-mask-domains-a632fc82.json) ·
[Scope and reproduction](frankl-fc-formalization.md#local-mask-checker-and-domains).

This registers reusable checker semantics. The full finite weight collection
and graph/rank tables remain separate obligations. The complete span-four
theorem remains incomplete, and the full merged-package gate is separate.

## Complete fixed-border multiplier and orbit bounds

The exact source snapshot `682d0917b1cf7cfbe3bee2e003e1df0735b23d0f`
passed strict source compilation for all 12 modules, a transitive standard-axiom
audit of 216 project theorems, and independent replay by the unchanged pinned
kernel checker. The receipt records every source, toolchain, manifest, and
gate hash. All registered proof sources match that snapshot.
[Exact receipt](verification/hadamard-border-transfer-682d0917.json) ·
[Hosted gate](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44492941039/job/135452942122).
The product-domain assembly also has its own ten-module, 154-theorem receipt
at `2006a76a`.
[Product-domain receipt](verification/hadamard-border-main-2006a76a.json).

The hypotheses are the actual four sign rows on an arbitrary finite abelian
group `G`, a subgroup `S` of cardinality 149 and index four, and combined
periodic autocorrelation −12 on nonzero elements of `S` and 4 outside `S`.
The full group of additive automorphisms preserving those rows is cyclic
and has order dividing four. For every subgroup `U` preserving the rows,
its order also divides four and its actual action on `G` has at least 151
orbits. The group definition imposes no coordinate-form or subgroup-preservation
hypothesis on its automorphisms.

The strongest original-domain endpoints are
`symmetry_subgroup_card_dvd_four_on_subgroup149`,
`symmetry_subgroup_isCyclic_on_subgroup149`, and
`symmetry_subgroup_orbit_count_ge_151_on_subgroup149`. The corresponding
`common_multiplier_*_on_subgroup149` endpoints apply to the full actual group.
They are registered in the root import, required-theorem audit, and replay list.

The proof constructs `G ≃+ (G ⧸ S) × ZMod 149`, maps `S` exactly to the
second factor, and transports the actual rows, correlations, symmetry group,
and orbit quotient. The multiplier injection follows from raw compressed
correlations: energy 608 bounds every fiber sum by 24, while a nontrivial
quotient symmetry forces a weighted correlation 298 whose absolute value is
at most 48. An order-37 multiplier would force all 16 fiber sums to be signs,
contradicting that energy. The cyclic unit group has order 148, so Cauchy's
theorem leaves only group orders dividing four. The origin orbit and a small
nonzero four-torsion orbit then give the 151-orbit bound.

This completes the final symmetry section of `BORDER.md`. The length-1197
and length-598 sequence restrictions, quotient/no-lift certificates, pattern
enumeration, and fixed-border matrix construction remain under issue 17.
The full merged-package gate is separate from this exact component check.
Hadamard existence at order 2396 remains open, and Li remains deferred.

## Frankl cyclic assembly and weight helpers — 19 November 2026

The accepted package includes the all-period span-four assembly with its
original eleven finite-check premises: eight graph, rank and literal-weight
checks, plus three actual short-period weight checks. The family transfer
retains arbitrary finite union-closed families and requires no empty member.
The theorem is still conditional; the concrete finite packet is unfinished.

The unchanged components passed five hosted proof jobs:

| Closure | Modules | Audited theorems | Private finite nodes |
| --- | ---: | ---: | ---: |
| Assembly and weight batches | 76 | 2,440 | 597 |
| Literal period-7/8/9 pilot | 25 | 378 | 24 |
| Word coverage | 1 | 22 | 0 |
| Exact injective transport | 23 | 371 | 0 |
| Cached mask evaluator | 10 | 155 | 0 |

Each job rebuilt its complete closure, audited every owned theorem with
explicit private imports, and replayed the exact closure with the unchanged
pinned stock checker. Only the three standard logical axioms are allowed.
The closures overlap; their union has 86 modules. This registration adds
32 unchanged proof modules, bringing the accepted set to 636 proof modules
plus two roots. The merged full-package gate remains separate.

The pilot checks only 16 original rows at each of periods seven, eight and
nine. The transport and caching theorems are generic. The 9,448-class orbit
dataset remains candidate data; it does not prove the full arithmetic,
transport or coverage tables.

[Assembly receipt](verification/frankl-span-four-77fa9a75.json) ·
[Pilot receipt](verification/frankl-cyclic-pilot-77fa9a75.json) ·
[Word-coverage receipt](verification/frankl-word-coverage-77fa9a75.json) ·
[Transport receipt](verification/frankl-mask-transport-5d86c291.json) ·
[Cache receipt](verification/frankl-mask-cached-5d86c291.json) ·
[Remaining finite work](frankl-cyclic-weight-orbits.md).

## Complete sharp 95-vertex example and arbitrary-voltage normalization

The seven `ErdosGyarfasSharp*.lean` modules prove the exact finite example in
`results/erdos-gyarfas-abelian-covers/sharpness.py`. The literal graph is a
connected cyclic nineteen-sheeted cover of the displayed subdivided tetrahedron.
It has 95 vertices, an explicit simple 32-cycle, and no simple cycles of lengths
4, 8, or 16. The endpoint `sharp95_cyclic_cover_and_least_power_cycle` states
that 32 is the attained least power-of-two cycle length.

The covering statement concerns the actual projection: every neighbor map is
bijective, and actual sheet translations act freely and transitively on each
fiber. Search soundness excludes actual graph cycles. Translation reduces
their starting points to five roots. Each complete root search is assembled
from its checked four-extension frontier and fourteen smaller kernel
computations, for seventy subtrees in total. The finite data, frontier
completeness, search semantics, and cycle witness are checked in Lean.
No native-evaluation axiom or external search result is a premise.

The two `ErdosGyarfasVoltage*.lean` modules normalize every assignment of
seven voltages in every abelian group. An explicit graph isomorphism
subtracts the tree potential from each sheet coordinate, making the four
tree voltages zero and giving three explicit chord voltages. It preserves
the existence of actual simple cycles of every specified length in both
directions. Normalized adjacency is expressed through a homomorphism from
`Fin 3 → ℤ`. The assignment `[0,0,0,0,1,8,0]` over `ZMod 19` is proved to
give exactly the sharp graph.

| Exact checked snapshot | Project closure | Audited project theorems | Receipt |
| --- | --- | --- | --- |
| `c6735b93` | Seven sharp-example modules | 288 | [Sharp example](verification/erdos-gyarfas-sharp-main-c6735b93.json) |
| `0cf8667d` | Four modules, including the actual base graph | 131 | [Voltage normalization](verification/erdos-gyarfas-voltage-normalization-0cf8667d.json) |

Both exact component closures passed strict source checking, the standard
transitive axiom whitelist, and independent replay with the unchanged pinned
kernel checker. The receipts bind the exact sources, toolchain, manifest,
and gate inputs. The later universal-cover registration below discharges the remaining
4-, 8-, 16-, or 32-cycle theorem for every abelian voltage cover. The general minimum-degree-three
conjecture is outside this result. Li remains deferred.

## Fixed-border certificate transport

`HadamardFixedBorderTransport.lean` and `HadamardFixedBorderFin16.lean` prove
the reindexing and reflection step of `BORDER.md`. Their input is an explicit
finite certificate: sign matrices `K`, `E`, and `F`, their three Gram
identities, the balanced-column identity, and the cross identity. All five
identities and all three sign conditions remain input premises.

The formalization connects the canonical index `position + 4 * block` with
`Fin 4 × Fin 4`. For every finite additive quotient `Q` of cardinality four,
it constructs actual transported matrices on `Fin 4 × Q`, preserving
sign-valuedness and all five identities with the original corner `K`.
The left border uses the actual permutation `q ↦ -q`; the reflected cross
term is proved for those same matrices. Cardinality four supplies the
labeling equivalence. No splitting of the ambient group, classification
of order-four groups, or oddness assumption is needed.

The endpoint is `HadamardFixedBorder.exists_transported_matrices_of_card_four`.
Its exact two-module closure at `23b2b187` passed strict source checks,
a 66-theorem standard-axiom audit, and independent pinned-kernel replay.
[Receipt](verification/hadamard-fixed-border-fin16-23b2b187.json).
The literal finite certificate is discharged by the later registration below.
Derivation of the compression shapes and the final bordered Hadamard
construction remain separate obligations under issue 17.

## Actual row normalization from compression shapes

`HadamardBorderNormalizationTransportOps.lean` and
`HadamardBorderNormalizationTransport.lean` construct operations on the
original sign rows. Their inputs are a surjective additive map, one constant
compressed row, and three compressed rows with one exceptional coset of
jump `2` or `-2`. Deriving these shapes from the original autocorrelations
remains a separate obligation under issue 17.

The theorem constructs a row permutation, signs, and translations in the
original group. The actual transformed rows are
`f'_i(x) = ε_i * f_(σ(i))(x + t_i)`. Their compressions are exactly `d`,
`a + 2δ₀`, `b + 2δ₀`, and `c + 2δ₀`. Every transformed entry remains in
`{-1,1}`, and the combined periodic autocorrelation is unchanged at every
group element. The constant compressed row retains its baseline. No
positivity condition on `d`, split extension, or quotient-cardinality
premise is added. Surjectivity supplies the lifts that move the exceptional
cosets to zero.

The final endpoint is
`HadamardBorderNormalizationTransport.exists_normalized_sign_rows`.
Its exact two-module closure at `14ab84e7` passed strict source checks,
a 14-theorem standard-axiom audit, and unchanged pinned-kernel replay.
[Receipt](verification/hadamard-border-normalization-main-14ab84e7.json).

## Exact fixed character-window witness

The literal witness from the Motzkin note is now checked and registered.
For an actual measurable additive circle character $`\chi`$, write
$`h=\min(\|\chi(a)\|,\|\chi(b)\|)`$. The set
$`\chi^{-1}([0,h))`$ is measurable, avoids both differences, and has measure
exactly $`h`$ under the given invariant probability measure. The proof also
covers finite character images and $`h=0`$; it does not replace the fixed
window by a separately shifted or abstract maximizing set.

The proof integrates an exact representative identity. For a general endpoint
$`0\le h\le1`$, the measure lemma explicitly requires that $`h`$ lie in the
character image. For the stated minimum-distance endpoint, an actual preimage
is constructed from one of $`a,-a,b,-b`$, so the final witness theorem has no
extra endpoint-image hypothesis.

Required endpoints are `Motzkin.characterWindow_measure`,
`Motzkin.character_window_exact`, and
`Motzkin.continuous_character_window_exact`, together with the two underlying
representative identities recorded in the receipt. Three newly registered
modules extend the two already accepted foundations.

The exact five-module closure at
`fea6cba2091c38a7cca5561b039eac262f4a3f61` passed strict source checks,
a transitive audit of **53 project theorems**, and unchanged pinned-kernel
replay. [Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44504300869/job/135494637842)
· [Exact receipt](verification/motzkin-character-window-fea6cba2.json).
All sixteen source and gate-input paths were compared with their frozen Git
blobs before registration and were unchanged. The receipt export independently
verified original artifact `14520517281`, whose ZIP SHA-256 is
`47e0b7df5fca6bd5efeabe514071a241841f6754def5100221fe9b26807ef8a8`.
[Receipt export](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44509280655/job/135508967148).

This was the first witness component registration. The subsequent evaluator
and rational-interval registrations below discharge those two obligations.
The final relation-basis registration below discharges the exhaustive
classification. The full merged package has its own verification run.


## Exact Motzkin evaluator and explicit rational intervals

The exact evaluator closure at `df244bd98eb43f1efc32d92d8e002dc461be58bb`
passed strict source compilation, an audit of 1,212 project theorems, and
independent pinned-kernel replay of all 65 project modules.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44507598703/job/135505396596)
· [Exact receipt](verification/motzkin-evaluator-df244bd9.json).
The accepted root now imports `MotzkinEvaluatorCandidates`; 21 newly registered
modules supply the floor-sum computation, both searches, the attaining
character, Hermite-quotient independence number, and cyclic gcd conversion.

For positive normalized Hermite inputs `m,k` with `s<m`, the checked
`Motzkin.Evaluator.evaluator_complexity` bounds the explicitly metered
arithmetic operations by `256*((m*k).log2+1)^2` and every recorded integer's
bit size by `6*((m*k).log2+1)`. The operation count includes both binary
searches and their floor-sum loops. The integer trace includes initialization,
query expressions, recursive floor-sum intermediates, and residue recovery.
These are arithmetic-operation and integer-size bounds for the formal
algorithm; they are not a machine-runtime measurement of the Python program.

The rational-interval closure at
`ad125705ce715d289be1a89a74e42d6ac095402b` passed strict sources,
a 795-theorem audit, and independent replay of all 46 modules.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44509224343/job/135511574207)
· [Exact receipt](verification/motzkin-rational-intervals-ad125705.json).
Three newly registered modules construct the literal half-open union of
cells `[j/N,(j+1)/N)`, prove its measure and avoidance of the two rational
jumps, and attain the actual extremal density. The finite independent set
and every geometric bridge are part of the checked closure.

All source and gate-input paths in both receipts were compared with the
frozen Git blobs and were unchanged before registration. The final
relation-basis registration below discharges the remaining classification.
These component passes do not claim a pass for the full merged package.

## Prime-257 minimum-pair-20 support certificate

The exact closure at `10ebb0e4cc69c25871fd339f8207ced070a018d7` passed
deterministic data reproduction, strict source compilation, the standard-axiom
audit of 1,202 project theorems, and independent replay of all 33 project
modules. [Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44507989478/job/135507165330)
· [Exact receipt](verification/loneliness-support257-10ebb0e4.json).
Twenty-three newly registered modules comprise thirteen literal-certificate
modules and ten generic search/encoding dependencies.

The 307-frame table uses fragments of size at most three. Its soundness theorem
reconstructs the original tape check with the original initial masks and fuel.
`Loneliness.Modular.SixSpeed.Support257Cuts.normalized_cover_impossible`
excludes a complete bad-time cover for a folded support modulo 257 of size at
most six, containing 1 and 20, with minimum nonunit entry 20 and every distinct
pair's folded quotient at least 20. No numerical search result or covering
obstruction is assumed. All fourteen required endpoints are registered in
the accepted axiom audit.

All source and gate-input paths match the exact passing snapshot. This closes
the narrow fragment task in issue 27. It supplies only the minimum-pair-20
probe; complete prime-257 coverage, the remaining primes, and the full
six-speed classification remain under issue 12.

## Checked order-11 fiber component

The two-module `Hadamard598Fibers` closure at
`e911b12c6ee8eb2ae02a0226e855f9314b24237e` passed strict sources,
a 28-theorem audit, and independent pinned-kernel replay.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44508575882/job/135508656032)
· [Exact receipt](verification/hadamard598-fibers-e911b12c.json).
It proves the actual order-11 invariant fiber-sum decomposition from sign
values. Its source and pinned package files are unchanged. The candidate gate
and workflow have since been extended; the archived receipt records their
historical hashes. This earlier component has now been subsumed by the full length-598
registration below, which includes the fiber source and the actual
multiplier contradiction.

The four exact archive digests and receipt-export checks are recorded in
[the component receipt record](verification/20261119-component-receipts.md).


## Complete universal abelian-cover cycle theorem

`ErdosGyarfasUniversal.universal_cover_cycle` quantifies over every abelian
group and every assignment of the seven oriented-edge labels of the specified
base graph. It constructs an actual graph walk that is a simple cycle, with
length in `{4,8,16,32}`. No finiteness, lattice classification, or certificate
premise remains in the endpoint. The equivalent power-of-two endpoint records
an exponent between two and five.

The literal 64-node table checks 546 collision branches using 1,264 explicit
integer combinations. The semantic proof transfers every checked combination
through the actual chord-label homomorphism, follows a smaller-index child
when a lifted walk collides, and otherwise constructs the simple cycle.
The producer and original public input are hashed and reproduced by the gate.
The already registered gauge isomorphism restores all seven arbitrary labels.
The already registered connected 95-vertex cyclic example proves sharpness.
This completes the stated cover theorem; it makes no claim about arbitrary
minimum-degree-three graphs.

At `daa7d2c5eb297ee0ebe5519cc256e418208db658`, the 17-module closure passed
exact data reproduction, strict source checks, an audit of 304 project
theorems, and independent replay with the unchanged pinned kernel checker.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44512718926/job/135523858461)
· [Exact receipt](verification/erdos-gyarfas-universal-daa7d2c5.json).
All 27 recorded source/gate/input paths match their passing hashes.
Thirteen new modules and all 69 required endpoints are registered.

## Complete literal finite-border certificate

`HadamardFixedBorder.Literal.literal_certificate_correct` checks the exact
displayed matrices `K`, `E`, and `F`: all three sign conditions, all three
Gram identities, the balanced-column identity, and the cross identity.
`HadamardFixedBorder.Literal.exists_border_of_card_four` supplies actual
transported matrices for every finite additive quotient of cardinality four.
The finite identities are proved by kernel-reduced cases and are no longer
premises of this existence statement. The larger bordered-core assembly is
still separate work.

At `ee6a8b03c9ad5166e6cccea2652112f10ee79e36`, the three-module closure passed
exact literal-source reproduction, strict source checks, an audit of 1,246
project theorems, and independent pinned-kernel replay.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44511099486/job/135518971308)
· [Exact receipt](verification/hadamard-fixed-border-literal-ee6a8b03.json).
All thirteen source/gate/data paths match their passing hashes. The new
literal module and all ten required endpoints are registered.

## Complete length-598 order-eleven obstruction

For four actual sign rows on `ZMod 26 × ZMod 23` whose combined periodic
autocorrelation is `−4` at every nonzero shift,
`Hadamard598.order11_multiplier_invariance_impossible` excludes any unit of
order eleven fixing all rows. The translated and individual-origins endpoints
allow separate origins for the four rows. Row-sum bounds, compression energy,
fiber values, and the exceptional-position structure are derived from the
original sign and correlation assumptions.

The proof forces exactly five compressed entries of magnitude 21 and none
of magnitude 23. Writing each entry as its zero-position sign plus `22e`,
the nonzero-shift correlations of `e` must vanish. Their row-sum squares then
sum to five, contradicting the bounds inherited from the original rows.
The final unit-group argument derives the actual order-eleven action on the
23-coordinate and trivial action on the 26-coordinate.

At `daa7d2c5eb297ee0ebe5519cc256e418208db658`, the eight-module closure passed
strict source checks, an audit of 141 project theorems, and independent
pinned-kernel replay.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44512718948/job/135523696857)
· [Exact receipt](verification/hadamard598-multiplier-daa7d2c5.json).
All sixteen source/gate paths match their passing hashes. Five length-598
modules and the general compression dependency are newly registered, with
all six required multiplier endpoints.

These three registrations add twenty modules to the previously registered
734 proof modules. All 754 proof modules are in the sequential prebuild and
kernel-replay list; the three endpoints are imported by `Conjectures`, and
all 85 required declarations are added to `ProofAudit`. These are exact
component passes. The merged accepted package has its own full gate.


## Complete two-difference Motzkin theorem

The final relation-basis closure constructs the missing bases for every
subgroup of the actual integer relation lattice. For arbitrary elements
`a,b` of an abelian group, `Motzkin.relation_lattice_trichotomy` proves
that one of the needed forms is available: the trivial lattice, one
nonzero integer generator, or a normalized rank-two Hermite basis
`(m,0),(s,k)` with positive `m,k` and `0 ≤ s < m`.
The endpoint takes no rank classification or basis-existence premise.

`Motzkin.compact_density_trichotomy` applies this construction to every pair
in a compact Hausdorff abelian group with its Borel structure and an invariant
probability measure. It gives density `1/2` in rank zero, the proved
one-relation formula in rank one, and the exact finite-grid maximum in rank
two. Together with the previously registered compact equality, cyclic
formulas, fixed character window, explicit rational interval unions, and
exact evaluator with its operation and integer-size bounds, this completes
the stated Motzkin note. Zero differences remain included in the original
definitions and theorem.

At `244cbd23366506b2c5ea268414a6b11dddb3d5fe`, all 41 modules passed strict
source checks, the 743-project-theorem standard-axiom audit, and independent
replay with the unchanged pinned kernel checker.
[Passing job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44511430092/job/135519975225)
· [Exact receipt](verification/motzkin-relations-244cbd23.json).

Artifact `14524686541` has ZIP SHA-256
`e4747a7a28da369e25cb28c0d0d26f8d50793c8fa9faf28e2548660324a14ac9`.
The archived receipt is byte-for-byte unchanged, with SHA-256
`f04006021604da3cd93e6ec885452cc2f9d8765b0592770c103f325926ae1529`.
All 52 distinct recorded source, gate, and pinned-input paths match the
passing hashes. The two missing modules and seven additional required
declarations are registered. At this checkpoint the prebuild list contained
756 proof modules plus its two roots; the full merged-package gate is separate.


## Complete conditional fixed-border construction and fourteen patterns

For every finite abelian group `G`, actual subgroup `H` of index four, and
four sign-valued integer rows, the endpoint assumes precisely the raw
nonzero-shift combined correlations: `-12` on `H` and `4` outside `H`.
`HadamardBorderConstruction.exists_hadamard_fin_of_subgroup_correlation`
constructs an actual sign matrix of order `4*card G+12` and proves its
full Gram identity. When `card H=149`, the specialized endpoint returns
a matrix indexed by `Fin 2396` with Gram matrix `2396 • 1`.

The proof constructs the quotient map from `H`, derives compression,
parity, and the four-coset variance classification, performs actual row
permutations, sign changes, and lifted translations, and proves that all
combined correlations are preserved. It then verifies the actual
Goethals–Seidel core, its border action, and all literal finite-border
identities. No split extension, chosen quotient, baseline, energy, core-Gram,
or finite-certificate premise remains in the endpoint.

For fibers of size 149, the same original rows yield the exact squared-row-sum
equation and one of the fourteen listed patterns. The result retains the
actual row-operation witnesses, identifies the constant entry by `p.d=|d|`,
and gives a permutation witness for the other three entries. The proof does
not assume the input baseline was positive or the input rows were sorted.
The finite classification proves both coverage and admissibility of the
fourteen distinct entries. This completes the stated conditional border
construction; finding binary rows satisfying its hypotheses remains open.

## Checked length-1197 reduction to order 27

`HadamardLegendre.common_multiplier_card_dvd_twenty_seven` starts with the
actual two sign rows, their Legendre-pair correlation equation, and
`card G=1197` on an arbitrary finite abelian group. It proves that the
actual common-multiplier group has order dividing 27, allowing the separate
row translations built into that group. Row sums, centering, product
coordinates, the odd-order obstruction, and injectivity away from the
order-nine component are derived. Every subgroup inherits the divisibility.

The companion `exists_invariant_quotient_three` constructs a surjective
invariant quotient with kernel of order three for an action of a group whose
order divides 27 on an abelian group of order nine. It uses fixed points on
the actual character group and does not assume either classification of the
order-nine group. These components do not yet establish the manuscript's
bound of nine: exclusion of order 27 still requires the finite quotient and
no-lift packet and its connection to the original rows.

### Exact receipts and registration

All four closures passed at `e25e0dcdc69ea1076df8c628b3a459eb12b0fe97`:
strict source checks, the transitive standard-axiom whitelist, and independent
replay with the unchanged pinned kernel checker. Their overlapping theorem
and module counts are not additive.

| Component | Modules | Audited project theorems | Passing job | Exact receipt |
| --- | ---: | ---: | --- | --- |
| subgroup | 17 | 1441 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44516496778/job/135534046058) | [JSON](verification/hadamard-border-construction-subgroup-e25e0dcd.json) |
| pattern-reduction | 9 | 164 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44516496778/job/135534046078) | [JSON](verification/hadamard-border-pattern-reduction-e25e0dcd.json) |
| reduction | 22 | 282 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44516496780/job/135534059970) | [JSON](verification/hadamard-legendre-reduction-e25e0dcd.json) |
| invariant-quotient | 2 | 11 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44516496780/job/135534060014) | [JSON](verification/hadamard-legendre-invariant-quotient-e25e0dcd.json) |

The four artifact ZIP SHA-256 values were independently checked:
- `14524674769`: `b54c4b65e4de48a631b9ce1975585b746d2c24dea5ef3adda1e7731cccee2fef`.
- `14526356497`: `1b8e368416dd6ec1a5fbe506fbec72bc2de19ebe8e227171ab2f3fb92ccaddb3`.
- `14524904432`: `e3510f82c06ff27774c75dab90048852945b6398093910aaec4a9e04f5277838`.
- `14526286474`: `2cbe184e7b4207e4056cac7c07208553d14582772fd8a37fdddd0684bd757981`.

All fifty distinct recorded source, gate, and pinned-input paths match their
passing hashes. The unchanged JSON receipts are archived above. This adds
31 proof modules and 17 required declarations to the accepted roots,
sequential prebuild list, and audit, for 787 proof modules plus the two roots.
The full merged-package verification remains a separate gate.

## Complete Frankl high-girth frequency theorem

`FranklHighGirth.high_girth_generator_frequency` proves the full
`518208/1000000` bound for every point of a finite `k`-uniform generating
family, for every `k ≥ 3`, with exactly three indexed generators through each
point and no incidence cycle shorter than sixteen. The counted family
contains each distinct union once, including the empty union. Finite ground
is derived from the stated regularity assumptions. The small-degree cases
use all twelve checked K03–K14 cone certificates and actual graph-ball
configuration counts; the large-degree case derives linearity from the
girth assumption and applies the accepted `657/1000` bound.

The graph proof identifies the radius-seven incidence ball with its recursive
tree, transports actual boundary-conditioned independent-set configurations,
and averages the finite fiber bounds. There is no unproved recurrence,
counting identity, finite-certificate assertion, or numerical bound in the
final theorem's hypotheses. The `girth` and extended-`egirth` formulations
and the frequency bound after removing the empty union are also checked.

At source commit `f421f4434ffc8117a57a14b99c19818e76dcfd8e`, all 64 project
modules passed fresh strict compilation. The explicit import-all audit
covered 1,363 owned declarations, including 909 theorems, and all 35 required
endpoints. Exact replay with the pinned, unchanged stock checker passed in
72.750 seconds, with peak RSS 12,834,268 KiB. Every recorded source, object
facet, compiler, checker, and gate hash was unchanged after checking.

[Original receipt](verification/frankl-components-44516856625/high-girth-theorem.json) ·
[Hosted run](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44516856625).
The original receipt SHA-256 is
`e872e48c8199c0c713d6a9cbc50e3d9ef42d8e32ed62e418ddcd282e104f65cf`.
The 47 newly registered modules and 34 new required endpoints join the shared
package. Its full merged-package build and replay are a separate gate.
The cyclic span-four theorem remains incomplete, so the Frankl result entry
remains partial. Li remains last.


## Complete Erdős 607 line-size asymptotic

The final endpoints concern `lineSizeCount n`, the actual number of records
of determined-line sizes for finite sets of `n` distinct real-plane points.
The previously registered geometric theorem identifies this count with the
canonical tuple count for every natural `n`, including the small cases.
The final analytic proof retains that definition throughout.

Writing

```math
A=\frac{\pi^2}{12}+\frac{(\log 2)^2}{2},
```

`LineSize.CoefficientAsymptotic.lineSizeCount_sharp_ratio` proves that the
ratio of this actual count to

```math
\frac{3}{16\sqrt{6\pi}\,A^{1/4}}\,
n^{-1/4}\exp(2\sqrt{An})
```

tends to one. The companion `lineSizeCount_sharp_asymptotic` states the
asymptotic equivalence directly. All local-limit, domination, tail, and
coefficient-extraction inputs are discharged in the import closure.

The proof uses the literal finite geometric characteristic product, its
summed cubic logarithmic error, the corrected Euler factor, and the actual
first and second moment limits. A floor-defined lattice step turns the
core-length sum into an integral. Its measurable integrand, pointwise limit,
integrable majorant, and coupled Gaussian constant are all proved. The exact
saddle choice and negligible constant contribution complete the normalization.

The analytic generating-function closure also proves absolute convergence,
the actual count's series value, the explicit generating function, and the
Fourier coefficient identity. It complements the earlier coefficientwise
formal power-series proof.

| Final component | Snapshot | Modules | Audited project theorems | Passing job | Exact receipt |
| --- | --- | ---: | ---: | --- | --- |
| generating-evaluation | `daa7d2c5eb297ee0ebe5519cc256e418208db658` | 39 | 867 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44512719031/job/135523776951) | [JSON](verification/line-size-generating-evaluation-daa7d2c5.json) |
| sharp-asymptotic | `36b137220a62a4c9170fcd6a96978dc5ac175bf9` | 78 | 1582 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44517650047/job/135537784932) | [JSON](verification/line-size-sharp-asymptotic-36b13722.json) |

Both closures passed strict source checks, the transitive standard-axiom
whitelist, and independent replay with the unchanged pinned kernel checker.
The module and theorem counts overlap and are not additive. Both artifact
ZIPs were verified before their unchanged JSON receipts were recovered:

- Artifact `14525466121`: ZIP SHA-256 `c138d6e941eefd2568856ca02e56307779d32d0ed3aba7c328a84be33ad2b0d8`; receipt SHA-256 `93d7bf4cb5ef276f1f25e06fddfa831338dd245ff6168f986e9e53d18af6732a`.
- Artifact `14527596723`: ZIP SHA-256 `26f545e4418122d186c7bfdc32b0a8133f70f1161fb1d46880a7df6f2265b152`; receipt SHA-256 `16e86762b72ede1922f907ad76af0164ebb0ba18ee646620dbc09c9853ef1c34`.

All 93 distinct recorded source, gate, and pinned-input paths match their
passing hashes. The registration adds 44 proof modules and 20 required
declarations, for 878 accepted proof modules plus the two roots.
This completes the stated Erdős 607 note. The full merged-package gate
remains separate, and the repository-wide campaign is incomplete.


## Actual Legendre-pair matrix and quotient transport

The actual two-row construction is checked for every finite abelian group: a Legendre pair yields a sign matrix of order twice the group cardinality plus two, with the required Hadamard Gram identity. In particular, a length-1197 pair yields an actual order-2396 Hadamard matrix. The proof derives the row-sum normalization internally.

The quotient transport is also checked. From the actual centered rows and an order-27 subgroup of common multipliers, Lean derives the order-133 quotient rows, their bounds, weighted sums and correlations, and the order-21 layer constraints used by the finite no-lift argument. No abstract quotient-data certificate is assumed. The final exclusion of order 27 and the sharper multiplier bound of nine remain pending the complete finite certificate and final assembly.

| Task | Modules | Audited project theorems | Passing job | Exact receipt |
| --- | ---: | ---: | --- | --- |
| construction | 5 | 87 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44519345569/job/135546487503) | [JSON](verification/hadamard-legendre-construction-20e04e58.json) |
| quotient-data | 18 | 353 | [Job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44519345569/job/135546487631) | [JSON](verification/hadamard-legendre-quotient-data-20e04e58.json) |

Both exact closures at `20e04e589d227086cc926579fc70806594d8f817` passed strict source checks with warnings treated as errors, the standard-axiom whitelist audit, and independent pinned-kernel replay. The 29 distinct source, verification-script, workflow and toolchain-pin paths in the two receipts were checked against current main before registration. 8 previously unregistered proof modules and 13 named endpoints are added; the accepted prebuild list grows from 878 to 886 proof modules, plus the two roots. Verification of the merged accepted package remains a separate gate.

## Complete unrestricted two-speed insertion theorem

The literal two-speed interval statement is checked for every natural
$`p\ge3`$ and every two positive integer speeds $`b,c`$, with no upper bound:
there is a real $`t\in[1/(p+2),1/p]`$ such that both distances to the nearest
integer are at least $`1/(p+2)`$.

The closure proves the measure estimate, endpoint divisibility, explicit
perturbed reciprocal times, all eight small-parameter certificates, and the
bound that reduces the remaining second-speed search to finitely many cases.
No numerical table or large-speed cutoff is assumed.

The insertion theorem applies to every base that stays separated on the
whole prescribed interval. The proof verifies that interval property directly
from the stated Goddyn–Wong gcd criterion for simultaneous accelerations,
and proves the lower bound after common dilation. The arithmetic criterion
is the stated hypothesis of the result, not an unproved external theorem.

The same closure checks the three-insertion obstruction: throughout
$`[1/6,1/3]`$, the clearance of `[4,6,10]` is at most $`1/7`$. It also checks
the actual five-speed witness for `[1,2,4,6,10]` at $`3/8`$.

At source commit `9f51470529423e8135c08de881cd56f5b1fd9a95`,
[run 44524198858/job 135562276051](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44524198858/job/135562276051)
freshly checked all 27 modules with warnings treated as errors and no linter
override. The audit covered all 563 owned declarations, including 424
theorems and 11 private declarations, and required all 49 named endpoints
to be theorems. Every module was then replayed as an exact singleton target
in a fresh process by the unchanged pinned stock checker, with one worker.
Only `propext`, `Classical.choice` and `Quot.sound` were allowed.

The [unchanged raw receipt](verification/two-insertions-exact-44524198858/receipt.json)
has SHA-256
`215df211e3e47abf148fd306cf43eef6cd1827a4b1b4cb61140743b2de36f55a`.
[Preserved audit, inventory, logs and controls](verification/two-insertions-exact-44524198858/)
and the [archive verification record](verification/two-insertions-exact-44524198858/preservation.json)
authenticate the original artifact `14529194546`, whose ZIP SHA-256 is
`bed76da06d98fda0721def565d9d451a3a79ce2071fe7ebe708bc723e8d7c248`.
All 27 checked source hashes were guarded at registration. The accepted
registry gains 18 proof modules and 49 named endpoints, bringing its
prebuild list to 904 proof modules plus the two roots.

This completes the original insertion note. The general lonely-runner
conjecture and the separate spectrum/classification notes remain outside
this result. Verification of the merged accepted package is separate.

## Six-speed spectrum: complete realization

For every natural `P ≥ 7` with `P % 6 = 1` or `P % 6 = 5`,
`Loneliness.SixSpectrumRealization.realizes` constructs a list of exactly
six distinct positive integer speeds with gcd one and actual loneliness
value $`(P-1)/(6P)`$, strictly below $`1/6`$. It assumes no runner bound,
critical-plane classification or finite-exhaustion statement.

The residue-one branch uses the proved consecutive family. The residue-five
branch proves the exact value of
`[6, 6n+5, 6n+11, 6n+17, 6n+23, 12n+28]` for every natural `n`,
including zero, with an actual attaining time and an upper bound at every
real time. A separate checked tuple supplies `P = 11`.
Both branches retain the positive, distinct and primitive conclusions.

[Run 44527134869/job 135570566146](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44527134869/job/135570566146)
checked the exact 11-module closure at
`a3d77bc65f3cd979f92590037eb8895c5c2eb25d`. All project sources were
freshly compiled with warnings treated as errors and no linter override.
The audit checked all 392 owned declarations, including 306 theorems and
30 private declarations; all 15 required endpoints have theorem kind.
All 11 modules passed exact singleton stock-kernel replay in fresh
one-worker processes. Only `propext`, `Classical.choice` and
`Quot.sound` were permitted.

The [unchanged raw receipt](verification/six-spectrum-realization-44527134869/receipt.json)
has SHA-256
`6d0d9bb9f7215e2f5138e277d72debf13f99edf9e3519c26eca0bdf6595d8bb9`.
The [preservation record](verification/six-spectrum-realization-44527134869/preservation.json)
authenticates all 71 original archive files, including sources, proof
objects, audit inventory and process evidence. Original artifact
`14532651083` has ZIP SHA-256
`b58416de9802b4a54b1d9dd2590144c8933de7368b32e7257ef20de18306b2ce`.
The raw receipt's `explicit_import_all` label records validated full
serialized visibility for this legacy-module closure; it does not assert
that the source used modern `import all` syntax.

Registration adds the two new modules and 13 previously unregistered
endpoints, with all 11 checked source blobs guarded. The accepted prebuild
list now has 906 proof modules plus two roots. This completes the existence
direction of the spectrum statement. The universal family and off-family
classification remains incomplete; the result entry remains partial.
Verification of the merged accepted package is a separate gate.

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

## Six-speed spectrum reduced fraction arithmetic

`Conjectures.LonelinessSixSpectrumArithmetic` is registered. It proves the exact
reduced forms of the proposed values: `a/(6a+1)` for `a≥1`, or
`(3s+5)/(18s+33)` for `s≥0`. Every member has six distinct positive primitive
integer speeds realizing that value. The odd-denominator condition and gaps
one or three are proved necessary. They are not sufficient by themselves:
`4/27` satisfies both conditions but is outside the proposed parameter set.
No statement that all six-speed tuples have these values is assumed or proved
by this component; the universal classification remains open.

[Run 44537865221/job 135607998981](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44537865221/job/135607998981)
passed at `26ad213ec179acb14affbe5274f8ed4af45ef7d5`: all 12 fresh strict sources,
all 421 owned declarations (335 theorems, 31 private declarations), all eight
required theorem endpoints, and all 12 exact singleton stock-kernel replays.
Only `propext`, `Classical.choice` and `Quot.sound` were allowed. The sibling
seven/eight-speed job in this run failed; its candidate scope is not accepted
by this receipt.

The [unchanged raw receipt](verification/six-spectrum-arithmetic-exact-44537865221/receipt.json)
has SHA-256 `7eeecaabb0f4c334857f415fd9b2e84025600e503c80098e340aa3ba6dd20c45`.
Artifact `14535809302` has ZIP SHA-256
`78561160c02bf670763318a1fe7ce8d02451995ae08ddef6d0f4b22912b820fa`.
The [preservation record](verification/six-spectrum-arithmetic-exact-44537865221/preservation.json)
records authentication of the original archived source and object bytes,
reconstructed all-owned audit, and process records. Registration adds one
proof module and eight required endpoints. The merged-package gate remains
separate, and the six-speed result remains partial.


### Six-speed sporadic values and denominator bounds

The module `Conjectures.LonelinessSixSporadicBounds` is registered after its exact gate passed at commit `85550e14596e630cd09c470ae29222331f1aa3fb`, [run 44539038584, job 135612147649](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44539038584/job/135612147649). This is the passing six-arithmetic matrix job; the sibling seven/eight job failed and is not accepted by this record.

The six public theorem endpoints prove the exact values of all nine listed sporadic sextuples, their arithmetic, their spectrum parameter form, the speed bound `d < 3*q` for every positive-denominator representation of their actual value, and the reduced denominator identity `q = 6*a + 1`. List permutations are included. This does not classify sextuples outside the nine-row list.

The gate rebuilt all 13 project source modules with warnings treated as errors, audited all 465 owned/raw declarations (359 theorems, 33 private declarations, 14 required endpoints), and independently replayed all 13 exact module targets with the pinned stock kernel. Only `propext`, `Classical.choice`, and `Quot.sound` are allowed. Compiler and checker hashes, exact source bytes, all object facets, original audit source and inventory, process records, and log hashes were checked against artifact `14538960017` (ZIP SHA256 `87afb597432653a835959a50358b2f5145a8605b606d2831c1389f2046c1cf92`). The raw receipt SHA256 is `93d5a70e16e3b2d7b1586dc06f88dd9f80ac60689cc0451ec058520d37152a26`.

Original receipt, audit, logs, progress records, archive member inventory, and preservation record are under [verification/six-sporadic-exact-44539038584](verification/six-sporadic-exact-44539038584/). Registration adds this one module and six endpoints; the full combined accepted-root gate remains a separate obligation. The six-speed spectrum directory remains partial because universal exhaustiveness has not been proved.


### Seven- and eight-speed spectrum realizations and exact candidate bounds

Three modules are registered: `LonelinessSevenSpectrumRealization`, `LonelinessEightSpectrumRealization`, and `LonelinessHigherSpectrumBounds`. Their exact passing snapshot is `4ccedd53fd68e40ef36e6d133f5e793f4c611a9f`, [run 44541874811, job 135622052992](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44541874811/job/135622052992). Only the passing seven-eight job supports this registration; failed triangle and six-plane siblings are excluded.

Every proposed seven-speed value `s/(7*s+1)` for `s >= 1`, or `3/23`, `5/37`, `9/65`, is realized by seven distinct positive primitive speeds. Every proposed eight-speed value `s/(8*s+1)` for `s >= 1` is likewise realized by eight distinct positive primitive speeds. Positivity and the strict thresholds `1/7` and `1/8` are proved.

The 27 original seven-speed sporadic rows and 17 eight-speed rows have their stated exact values and arithmetic. `KnownSeven` contains the consecutive seven-speed family and its finite table, with permutations; `KnownEight` contains all three stated eight-speed families and its table, with permutations. For every member and every positive-denominator representation of its actual value, the sharp bounds are `5*d <= 13*q` and `17*d <= 21*q`. Explicit equality witnesses prove that the constants `13/5` and `21/17` cannot be lowered on these candidate classes. The exceptional eight-speed families retain their special parameter-one value.

The modules also prove that every listed candidate has a proposed spectrum value and identify every reduced numerator/denominator pair. Seven-speed reduced pairs have `q = 7*p+1` or are exactly `(3,23)`, `(5,37)`, `(9,65)`; eight-speed reduced pairs have `q = 8*p+1`. The corresponding denominator-defect conclusions follow for `KnownSeven` and `KnownEight`. These statements do not assert that every arbitrary low-value tuple belongs to the candidate classes. Universal seven/eight classification remains open in this campaign, so neither directory is marked complete.

The gate freshly checked all 16 project sources with warnings treated as errors, audited all 647 owned/raw declarations (481 theorems, 16 private declarations, 26 required endpoints), and independently replayed all 16 exact module targets with the pinned stock kernel. The only allowed transitive axioms are `propext`, `Classical.choice`, and `Quot.sound`. Artifact `14538953168` has ZIP SHA256 `408e523f52846a868217f97aae153d74369ef3f89fa3868d92d45a2a6722e346`; its raw receipt SHA256 is `5ccd2ff37f0928feb38e10e153abcd1f36eb759b0cdd5c264e11ca910ddc9981`. Source and control hashes, every object facet, the original audit and inventory, process records and logs were authenticated before preserving the unchanged evidence in [verification/seven-eight-spectrum-exact-44541874811](verification/seven-eight-spectrum-exact-44541874811/). Registration adds three modules and 26 required endpoints; the combined accepted-root build/audit/replay remains separate.


## Five-runner lower-bound candidate

The new `LonelinessFiveRunner*` sources target the unconditional lower bound
`1/6` for at most five positive speeds and the two primitive equality
directions `[1,2,3,4,5]` and `[1,3,4,5,9]`. The direct route combines a
16-row KZ product certificate, a squared-norm cutoff of `347142`, and five
complete modular packets with 7070 support frames. The finite soundness,
consequences, and product-certificate modules passed local strict source
checking. The full final theorem gate is pending; no result is registered or
marked complete by this candidate. The structural population counter also
passed an eight-case source and stock-kernel diagnostic with the original
checker propositions. [Statements, census, and verification scope](five-runner-exact-candidate.md).

### Higher-speed triangle consequences under primitive classification

`Conjectures.LonelinessHigherTriangleConsequences` is registered after its exact gate passed at commit `788e2572b877750158bd471191ef9701c50b93bd`, [run 44545339492, job 135634276616](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44545339492/job/135634276616). Only the passing triangle job supports this checkpoint; the failed six-plane semantic and data-pilot jobs are excluded.

The module constructs triangles in the actual integer distance graph for both six-speed product families, the signed six-speed third family, all nine six-speed sporadics, the stated seven/eight families, and all 27/17 higher sporadics. The vertices are `0, x, x+y`; the signed third-family identity supplies these vertices without a positivity assumption on its real parameters. The speed list itself remains positive. Permutations and gcd rescaling are handled explicitly.

The final Zhu implications retain the precise primitive classification hypothesis: every positive, distinct, primitive list of length `k` with actual loneliness below `1/k` belongs to the stated candidate class. Under that hypothesis, for `k = 6, 7, 8`, a triangle-free integer distance graph is `k`-colorable, and a graph of chromatic number `k+1` contains a triangle. The classification hypothesis is not discharged here, so this checkpoint does not prove unconditional Zhu or exhaustive speed classification.

The gate rebuilt all 34 project source modules with warnings treated as errors, audited all 1,024 owned/raw declarations (805 theorems, 36 private declarations, all 23 required endpoints), and independently replayed all 34 exact targets with the pinned stock kernel. Only `propext`, `Classical.choice`, and `Quot.sound` are allowed. Artifact `14541661556` has ZIP SHA256 `7dfc4798aed3e9a21b50010b5d9d00108d134253494fab8b41051d5bd0b60291`; the raw receipt SHA256 is `42b1e5aa90a5eef82cd785d70445d6d3273ed1fe13b62b26a62e119abf41dcba`. All 47 original source/control/configuration/helper files match the exact Git tree at the passing commit. Every archived source and object hash, original audit and declaration inventory, process record, and log hash was authenticated.

Unchanged receipt, audit, logs, progress records, archive-member inventory, and preservation record are under [verification/higher-triangle-exact-44545339492](verification/higher-triangle-exact-44545339492/). Registration adds one module and 23 required endpoints. The combined accepted-root gate remains separate, and no result directory is marked complete.



## Renault foundations and six-speed prime pilot, 19 November 2026

Two separate hosted gates passed. Neither checkpoint completes a spectrum classification.

| Checkpoint | Source commit | Project modules | Owned declarations | Private declarations | Required endpoints |
| --- | --- | ---: | ---: | ---: | ---: |
| Renault foundations | `f6b37c31b67d4905a03ebafca4e427aaf36d8ad8` | 18 | 605 | 131 | 64 |
| Prime-307 pilot | `7bfbeef3715b82f33bae00493f05c72d7a6978e4` | 85 | 3,910 | 91 | 8 |

Each gate rebuilt its complete project dependency closure with warnings treated as errors. It audited every owned declaration, including serialized private declarations, and replayed every module with the unchanged stock Lean checker. The transitive axiom whitelist was exactly `propext`, `Classical.choice`, and `Quot.sound`. Source, object, control, runtime, log, and audit hashes remained fixed.

The Renault checkpoint proves all eight universal real phase lemmas from Renault's six-runner argument, together with constrained maximization, affine time changes, exact gcd orbits, third-shift obstructions, two-multiple fiber arithmetic, and reindexing. The phase-certificate producers also reproduced their frozen source payloads. These are proved components; the full five-speed lower bound was not part of this passing gate.

[Renault run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44549206241/job/135648012899) ·
[Unchanged receipt](verification/renault-foundations-44549206241/receipt.json) ·
[Source, audit, and log evidence](verification/renault-foundations-44549206241/evidence.tar.gz) ·
[Preservation record](verification/renault-foundations-44549206241/preservation.json).

The prime-307 pilot proves the original support-checker propositions for minimum pairs 2 and 153. The larger root uses blocks of 32 frames and transports computation through the proved counted-bit checker. The pilot checks two selected roots; the remaining minimum pairs and the complete prime classification are still open.

[Prime-307 run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44540677853/job/135617953079) ·
[Unchanged receipt](verification/p307-pilot-44540677853/receipt.json) ·
[Source, audit, and log evidence](verification/p307-pilot-44540677853/evidence.tar.gz) ·
[Preservation record](verification/p307-pilot-44540677853/preservation.json).

The original artifact ZIPs and raw receipt hashes were authenticated against GitHub's artifact metadata and completed job logs. Every preserved source, object digest, audit inventory, and process log was revalidated after download. The evidence archives contain the original proof sources, controls, certificate data where present, audit inventories, logs, and process profiles. This preservation step did not perform a new local Lean replay.

The complete Renault proof is a separate candidate at `af144a83407065bc9b4ffae707c9b360a5f9c399`, tracked in [issue 38](https://github.com/1337isnot1337/solved-conjectures/issues/38). Its final endpoint has type `CoordinateSubspace.LonelyRunnerBound 5` and discharges the four-speed input. Its [106-module gate](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44550409224) is separate from the passing foundation gate. No complete five-speed bound or new accepted-module registration is claimed by this checkpoint.

## Critical seven-coordinate planes and large-norm family

The roots `LonelinessSevenCoordinateClassification` and
`LonelinessSevenCoordinateLargeNormFamily` are registered. Their classification
directions retain exactly these two mathematical inputs:

- `h5 : LonelyRunnerBound 5`: every nonempty list of at most five distinct
  positive speeds has loneliness at least `1/6`.
- `h6 : PrimitiveSixClassification`: every positive, distinct, primitive
  six-speed list with loneliness at most `1/7` is a permutation of
  `[1,2,3,4,5,6]`.

Under `h5` and `h6`, a rational two-plane in seven coordinates has actual
space loneliness `1/7` if and only if it is a signed coordinate permutation
of the standard product plane. The converse value calculation for every
standard product plane is unconditional. The finite enumeration, repeat-line
tests, signed-coordinate normalization, and geometric assembly are proved
internally.

Under the same two inputs, every positive primitive tuple `v : Fin 7 → ℕ`
with `value (List.ofFn v) < 1/7` and Euclidean norm at least `7*42^10` is an
actual permutation of `[1,2,3,4,5,6,7*s]` for some `s >= 1`. Its exact
real-time loneliness is `s/(7*s+1)`. Integer product parameters, gcd transfer,
and the family value are included in the checked proof.

Exact [run 44547965580, job 135643591005](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44547965580/job/135643591005)
at `d082b9a7adbed4144ccc9a961023bcae46f00e3d` passed all 105 fresh strict
source checks, all 23 required theorem endpoints, the complete audit of
2,105 owned/raw declarations (1,864 theorems and 630 private declarations),
and 105 independent exact stock-kernel targets. Only `propext`,
`Classical.choice`, and `Quot.sound` are allowed.

Artifact `14542847200` has ZIP SHA256
`194c41f3c61b853102ee11251881edf82b0bdbda0fbf0fb3c4776966050bf7f8`.
The unchanged receipt has SHA256
`7ed624c23f151717a7d2df018d77c994bbe26dbc9f6a20122eb353234a95adf7`.
All 635 archive files were authenticated. The 425 original receipt, audit,
log, and progress files are preserved in
[verification/critical-seven-exact-44547965580](verification/critical-seven-exact-44547965580/),
with archive-member hashes and an independent validation record.

Registration adds 47 modules to the accepted module list and 23 required
endpoints. This checkpoint completes the stated finite and geometric bridge
with its explicit inputs. It does not discharge `h5` or `h6`, and it does not
establish unconditional seven-speed spectrum exhaustiveness. No result
directory is marked complete by this registration. The merged-package gate
remains separate from this exact component evidence.


### Accepted seven-speed low-gap input for the eight-coordinate argument

`LonelinessSevenLowGapInput` is now an accepted component. Within the stated seven-speed families and sporadic rows, loneliness strictly below `3/23` leaves exactly the bases `[1,2,3,4,5,6,7]`, `[1,2,3,4,5,7,12]`, and `[1,4,5,6,7,11,13]`, each with value `1/8`. The proof filters every table row, forces the consecutive-family parameter to be one, and retains permutation and positive gcd scaling. Its extension to arbitrary positive distinct seven-speed lists explicitly assumes `PrimitiveClassification`; this registration does not establish that classification or the eight-speed spectrum theorem.

The original passing [run 44551449045](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44551449045), job `135655971010`, checked commit `aac4fff06ba8f6678d60a1665ab4790562cbbc5a`. It compiled all 17 project modules from fresh sources with warnings as errors, audited all 663 owned/raw declarations (494 theorems and 16 private declarations), required all eight endpoints, and replayed all 17 exact project-module targets separately with the unchanged stock checker. Only `propext`, `Classical.choice`, and `Quot.sound` were permitted. No linter override or cached project-proof acceptance was used.

Artifact `14542014520` has ZIP SHA256 `256cfdb7f4e00cee8253f0f8c2e59037d9e3bcb4db428d3484054a7c7ed33077`; its unchanged raw receipt has SHA256 `4d5996deff454e567510b3445317d11bea3ba1b65e8e6047d3637c8e41c30211`. All 30 source/control/helper/configuration files matched the exact passing tree. The archive validator authenticated all 107 members and preserved 75 unchanged evidence files under [`docs/verification/seven-low-gap-exact-44551449045/`](verification/seven-low-gap-exact-44551449045/), including the original receipt, complete owned-declaration inventory, generated audit source, process logs and progress records. Failed or still-running sibling tasks are outside this acceptance checkpoint.


### Accepted six-plane direction coverage and certificate chunk joins

The exact 20-module data-and-coverage component is accepted. It checks all `10 × 720 × 6 = 43,200` cells of the coordinate-permutation lookup through 120 bounded checks and a proved quotient/remainder join. The permutation-rank proof covers all 720 permutations; the lookup supplies the exact 360-row quotient used by the numerical certificate. The three certificate pilots are nested checks of 32, 256, and 1,280 cases for the first pattern pair, so their sizes must not be added as disjoint coverage. The generic chunk-join theorems recover every row when the chunk size is positive and `blocks * size = 360`, and transport checked row certificates to `CandidatePairsChecked` with numerical direction coverage explicit. They still require all numerical chunk checks as hypotheses.

This checkpoint does not establish all 1,152,000 candidate-pair cases or the six-plane classification. The complete pair table and its separate distributed gate remain separate work. The lookup tables are pure noncomputable definitions; the ordinary kernel evaluates the checked expressions, with no `native_decide`, custom axiom, linter override, or increased verification budget.

Original [run 44551449045](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44551449045), job `135655971048`, passed at `aac4fff06ba8f6678d60a1665ab4790562cbbc5a`: 20 fresh strict source modules, all 414 owned/raw declarations (317 theorems, zero private declarations), all nine required endpoints, and 20 exact independent stock-kernel targets. The axiom whitelist was exactly `propext`, `Classical.choice`, and `Quot.sound`.

Artifact `14543834207` has ZIP SHA256 `1a8fa5d2400e25a00ca381c16a98be42f765cf7b199a07e171dfbb648dce5067`; the unchanged receipt hash is `e648e84040f83963f18d44152638d02c3c800e1e3ee1624a2de96d50285c67ee`. All 33 source/control/helper/configuration files matched the original passing tree, and the proof sources still match the registered versions. All 125 archive members were authenticated. The 87 unchanged raw evidence files are preserved under [`docs/verification/six-plane-coverage-exact-44551449045/`](verification/six-plane-coverage-exact-44551449045/). Failed semantic sibling jobs and later whole-table jobs are outside this acceptance checkpoint.


### Six-speed norm geometry from an explicit plane gap

The 52-module norm component is accepted. For a positive primitive six-speed vector with loneliness value at most `1/6`, it proves Euclidean norm strictly below `21829`, assuming `LonelyRunnerBound 4` and that every rational two-dimensional plane containing the vector has space value at least `2/11`. It constructs a reduced integral basis, proves all five Gram-prefix bounds, and proves the determinant identity internally. The five required endpoints are `exists_gram_data`, `numerical_margin`, `squaredNorm_lt`, `norm_lt`, and `natural_squaredNorm_lt` in `Loneliness.SixSpectrumNormGeometry`.

The norm bound is stronger than the original ambient bound `163350`. This component retains its plane-gap and four-speed hypotheses. It does not prove arbitrary rational-subspace covolume bounds, the finite off-critical classification, or the complete six-speed spectrum. The result-level completion status is unchanged.

Original [run 44555513834](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44555513834), job `135670390120`, passed at `f66de17709f2dd9f46c96cd1fc9b0ed3b60fda2a`: 52 fresh strict source modules, all 1,269 owned/raw declarations (1,051 theorems, 60 private declarations), five required endpoints, and 52 exact independent stock-kernel targets. The axiom whitelist was exactly `propext`, `Classical.choice`, and `Quot.sound`. Verification budgets and warning settings were unchanged.

Artifact `14544624570` has ZIP SHA256 `541410f007a756a1a10fee1c5abebb53d6cd6c40ecf163c576d0df9a18f15a11`; the unchanged receipt hash is `1ac075b71fe894ee81f37c8bab28dc9679b4528371c9afaef61ee14f4fc81a5c`. All 65 original source/control/helper/configuration files matched the passing tree. All 317 archive members were authenticated. The 213 unchanged raw evidence files are preserved under [`verification/six-spectrum-norm-exact-44555513834/`](verification/six-spectrum-norm-exact-44555513834/), with a separate preservation record and archive inventory. `scripts/validate_six_spectrum_norm_archive.py` reproduces the offline provenance checks; it does not claim a new Lean execution. `LonelinessKZSmallData` and `LonelinessSixSpectrumNormGeometry` are now registered with the accepted root and verifier.


## Product-plane integer speed bridge (2026-11-19)

`Conjectures.LonelinessProductPlaneSpeeds` is registered from the original passing [run 44553736720](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44553736720), job `135664057075`, source commit `eeef183d9fbb54a0dc46148a56b26928216101b3`. The exact 40-module project closure passed fresh strict source compilation, the complete owned and private declaration audit, and 40 separate stock-kernel target replays. The audit checked 860 owned/raw declarations, 730 theorems, 10 private declarations, and all four required theorem endpoints. Only `propext`, `Classical.choice`, and `Quot.sound` occur in the allowed axiom set.

The theorem uses the actual rational plane spanned by `(W,0)` and the last coordinate axis, transported by signed coordinate permutations. A base coordinate equal to one recovers an integer scale. A positive integer direction then gives the complete speed list `(A W,b)`, including all multiplicities and its actual permutation. For a primitive list below `1/q`, with `q ≥ 4`, a primitive base and nonzero base residues modulo `q`, the proved product-family arithmetic yields exactly `W ++ [q*s]` for a positive integer `s`. The required endpoints are `Loneliness.ProductPlaneSpeeds.integer_coordinates`, `absolute_list`, `product_parameters_of_positive_direction`, and `primitive_family_of_below`.

This is a membership-to-family bridge. It does not prove that every low-value direction lies in one of these planes, discharge any finite classification premise, or complete the six-, seven-, or eight-speed spectrum result.

The original artifact is `14545500562` (6,623,688 bytes), ZIP SHA-256 `03bfed1335de52058aacd5d81887684eb38368baad81102fc6d0121b539fc002`; the raw receipt SHA-256 is `6b416de0a4c875bfbacf0164c65cc3d8648b1c23f4ef388c367b6504ac11f0c5`. All 53 historical source/control/configuration files match the original Git blobs, and all 245 archived members were authenticated. The unchanged receipt, generated audit source, declaration inventory, process logs, progress records, archive manifest, and preservation record are under [`docs/verification/product-plane-speeds-exact-44553736720`](verification/product-plane-speeds-exact-44553736720/). The recorded validation command is `python3 scripts/verify_higher_spectrum_realization_exact.py product-plane-speeds` at that original source commit; preservation does not claim a new execution of that gate.


## Five-speed norm and prime avoidance, 19 November 2026

`LonelinessFiveRunnerNormData` and `LonelinessFiveRunnerNorm` are now registered.
For every positive primitive vector `v : Fin 5 → ℕ` of actual loneliness at most
`1/6`, the squared norm is at most `347142`. One of the primes
`149, 151, 163, 167, 173` divides none of its coordinates. Neither endpoint
assumes distinct coordinates. The norm certificate and the complete prime
product argument are proved internally.

[Run 44555436644](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44555436644)
freshly compiled the exact 108-module project closure, audited 2,824 owned
declarations including 34 private declarations and all 15 required endpoints,
and stock-replayed exactly those 108 modules. Only `propext`, `Classical.choice`,
and `Quot.sound` are allowed. The downloaded artifact was authenticated against
the published commit, every recorded source/object/log hash, the complete
private declaration inventory, and the actual replay transcript.

The original receipt and detailed scope are preserved in the
[component checkpoint](verification/loneliness-five-runner-norm-44555436644/README.md).
The other 106 dependencies were already registered with identical source bytes.
This component does not close the five-speed lower bound, either tight-five
classification, or the full five-speed spectrum theorem. The merged-package
gate remains separate from this component receipt.

## Six-coordinate plane semantics (19 November 2026)

The six-coordinate plane semantic component is accepted from [run 44557816556](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44557816556), job `135681972978`, at source commit `fdd22c92c4e8c88a486881b5561e95be5c44cd62`. Its exact 63-module closure passed fresh strict source compilation, the complete owned and private declaration audit, and 63 independent stock-kernel target replays. The audit checked 1,313 owned/raw declarations, 1,055 theorems, 15 private declarations, and all 31 required theorem endpoints. The allowed axioms were exactly `propext`, `Classical.choice`, and `Quot.sound`.

For a coordinate-free rational two-dimensional plane in six coordinates with actual space value below `2/11`, the semantic theorem recognizes one of the three original planes, up to coordinate signs and permutations: `(s,2s,3s,4s,5s,t)`, `(s,3s,4s,5s,9s,t)`, or `(s,t,s+t,2s+t,3s+t,3s+2t)`. The proof retains explicit inputs for the four-speed runner bound, the exact five-speed low-gap classification, and complete candidate-pair certificate coverage. The five-speed input is separately derived from `Loneliness.FiveSpeedCertificate.SporadicExhaustion`. The enumeration interface checks all 720 permutation ranks and proves that complete direction lookups and row/block certificate checks imply `CandidatePairsChecked`.

This acceptance supplies the semantic bridge and exact coverage interface. It does not discharge `SporadicExhaustion`, supply the complete numerical pair certificate, or establish unconditional six-plane or six-speed spectrum classification. The later wrapper that discharges the four-speed hypothesis and the separate complete finite-data gate are outside this receipt. Result-level completion boxes are unchanged.

Artifact `14550615276` contains 10,650,461 bytes and has ZIP SHA-256 `236667c95848500328181d1b15b1414ec6544a68daa31b27884e6974f19a4eeb`. The unchanged original receipt has SHA-256 `431d8358951a12ba901f94a124724a07a26802dcc7f43a65110ab5ba530f625a`. All 76 historical proof-source, helper, configuration, and controller Git blobs were authenticated; all 383 archive members, object hashes, process records, and audit data were checked. The 257 unchanged raw evidence files, archive inventory, and separate preservation record are under [`verification/six-plane-semantics-exact-44557816556/`](verification/six-plane-semantics-exact-44557816556/).

The original command was `python3 scripts/verify_higher_spectrum_realization_exact.py six-plane-semantics` at the stated source commit. `scripts/validate_spectrum_archive.py` reproduces the offline archive checks; preservation is not a new Lean execution. The eight new semantic modules, their seven previously unlisted five-speed dependencies, and the 31 required endpoints are appended to the accepted root, prebuild, and audit registries. `LonelinessSixPlaneDefs` and `LonelinessSixPlaneEnumeration` were already registered from the earlier coverage component.

## Unconditional five-speed bound and primitive transport, 19 November 2026

`Loneliness.Renault.five_speed_lonelyRunnerBound` now proves the unconditional five-speed runner bound. Its common-time endpoint proves that every positive `v : Fin 5 → ℕ` has a time in `[0,1]` at which all five distances are at least `1/6`; repeated speeds are allowed. The primitive intermediate theorem is extended by gcd normalization and padding. The final wrapper supplies the proved four-speed bound, so no unformalized runner theorem remains as an assumption of the five-speed endpoint. The proof follows [Renault's six-runner argument](https://compmath.wordpress.com/wp-content/uploads/2008/08/view-obstruction_a_shorter_proof_for_6_lonely-runners.pdf), including all eight real phase lemmas.

Three fixed component gates passed fresh strict source compilation, complete ownership and raw-private axiom auditing, and unchanged stock-kernel replay of every project module:

| Component | Source snapshot | Project modules | Audited declarations | Private declarations | Required endpoints |
| --- | --- | ---: | ---: | ---: | ---: |
| Unconditional five-speed bound | `93022640cfd5f8c4fa2ce837dd8743d101374f2d` | 106 | 3,003 | 230 | 100 |
| Primitive classification transport | `58c9bcc77d97b970af006b00bb40f549fcf737b1` | 15 | 317 | 10 | 5 |
| Distinct positive padding | `d59ba2141fb6015f5eb8b7460d75056d16439a71` | 16 | 327 | 15 | 4 |

The axiom whitelist is exactly `propext`, `Classical.choice`, and `Quot.sound`. The original receipts, declaration inventories, proof sources, gate controls, logs, and process profiles are preserved under [renault-five-speed-44556621749](verification/renault-five-speed-44556621749/), [runner-bound-transport-44557243499](verification/runner-bound-transport-44557243499/), and [runner-bound-padding-44559299513](verification/runner-bound-padding-44559299513/). Each downloaded ZIP was checked against its GitHub artifact digest; every source, compiled object, control, log, profile, and declaration inventory was then revalidated. This preservation step did not rerun Lean locally.

The padding result removes a smaller-runner premise from the transport itself: a primitive bound at exact length `k` extends to every positive distinct list of length at most `k`. Its classification version requires a classification of the closed sublevel `value ds ≤ 1/(k+1)` and a matching lower bound for every classified case. It does not prove those classifications or discharge lower-dimensional assumptions used inside their proofs.

Registration adds 23 module roots and 109 required theorem endpoints to the accepted imports, axiom audit, and kernel-replay list. These unchanged component receipts remain distinct from the merged accepted-package gate. The five-speed spectrum, the higher-speed exhaustive classifications, and the overall campaign remain incomplete. Li remains last.

## Six-speed finite-field prime-product reduction (2026-11-19)

`Conjectures.LonelinessSixSpectrumFieldsDefs` and `Conjectures.LonelinessSixSpectrumFieldsProduct` are registered from the original passing [run 44559208975](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44559208975), job `135691218139`, source commit `1ccbc51789fed2aded3597c7dc1491aefabe716a`. The exact nine-module project closure passed fresh strict source compilation, complete owned/private axiom auditing, and nine separate stock-kernel target replays. The audit checked 266 owned/raw declarations, 202 theorems, 13 private declarations, and all 16 required theorem endpoints, with only `propext`, `Classical.choice`, and `Quot.sound` allowed.

The factor type contains exactly 20 increasing index triples and four sign choices, giving the stated 80 forms `v_i ± v_j ± v_k`. The finite `PrimeTriangleCover p` premise ranges over every nonzero raw residue sextuple, including repetitions. Its point checker accepts a genuine threshold-six modular witness or two distinct divisible factor indices. This sufficient condition is weaker than the original C++ condition involving distinct folded values. The definitions do not assert that any particular prime passes that cover.

For positive actual integer speeds, let `G = (∏ v_i)^2 * ∏ |v_i ± v_j ± v_k|`. Every counted prime contributes `p^2 ∣ G`: the squared speed product covers primes dividing any coordinate; otherwise the explicit cover and actual value below `1/6` give two distinct divisible factors. Distinct primes in a finite set yield `P^2 ∣ G`. From the actual squared norm `∑ v_i^2 ≤ N`, the proved Cauchy bounds give `G^2 ≤ N^12*(3*N)^80`. The strict inequality `P^4 > N^12*(3*N)^80` therefore forces a zero factor and an actual additive triangle on three pairwise distinct coordinate indices. Distinct speed values require the application's separate distinctness premise.

The required endpoints in `Loneliness.SixSpectrumFields` are `triple_card`, `form_card`, `twoRelationsCheck_sound`, `pointCheck_sound`, `primeCheck_sound`, `eval_mod_decomposition`, `relations_of_mod`, `relations_of_cover`, `eval_square_le`, `additive_of_zero`, `prime_square_product_dvd`, `twoRelations_square_dvd`, `prime_square_dvd_obstruction`, `obstruction_square_le`, `zero_form_of_prime_covers`, and `additive_triangle_of_prime_covers`.

Every prime cover, the prime-product comparison, the actual norm bound, positivity, and the strict real-value hypothesis remain explicit. This component does not discharge finite support/orbit coverage, prove sporadic exhaustion, or complete the six-speed spectrum classification. The larger support transport and coverage modules are separate candidates.

Original artifact `14549736325` has 1,265,230 bytes and ZIP SHA-256 `6ce08dfa9c1cc41e58ebf718befd70143eaf23e35861df05e936c85095272f5f`. The unchanged raw receipt SHA-256 is `15e8e925d8cd36fc5df28d1f03e4e37dae5910f47e1bc80e13aa07960791f7cc`. All 22 historical source/control/configuration files match the original Git blobs. The unchanged receipt, declaration inventory, generated audit source, process logs, progress records, and complete archive manifest are preserved under [`docs/verification/six-fields-product-exact-44559208975`](verification/six-fields-product-exact-44559208975/). The original command was `python3 scripts/verify_higher_spectrum_realization_exact.py six-fields-product`; preservation does not claim a new execution of that gate.

## Conditional gcd shift test (19 November 2026)

`LonelinessGcdShiftCounting` and `LonelinessGcdShift` are registered with
20 required theorem endpoints. For nine distinct positive integer speeds,
the final theorem assumes `LonelyRunnerBound 8`, a modulus `d ≥ 2`, a
nonempty set of coordinates not divisible by `d`, and a gcd-weighted ceiling
cost strictly below `d`. It concludes that actual loneliness is strictly
above `1/10`. The floor-cost and residue versions retain their explicit
positive-cost conditions.

[Run 44562942517](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44562942517)
at `4f97f1e9936e089a7f33b8d6093ea820661c1f31` passed all 17 fresh strict sources,
399 owned/raw declarations (319 theorems and 10 private declarations), all
20 named obligations, five literal statement checks, and exact stock replay
of the 17-module closure. The downloaded artifact and original receipt were
authenticated against the published Git blobs and complete source/object/log
inventories. The other 15 project dependencies were already registered with
identical source bytes. See the [conditional component checkpoint](verification/loneliness-gcd-shift-44562942517/README.md).

The eight-speed bound remains a hypothesis. This receipt does not establish
an unconditional nine-speed result, signed-unit transport, or a complete
finite lift census. Result-level classification status is unchanged; the
merged-package gate remains separate from this component verification.


### Six-speed first-cover support reduction: accepted component

The exact candidate at `3273ac1a24ea061b0cbd73244e2ac57c08d491ec` passed [run 44563135178, job 135701825289](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44563135178/job/135701825289). The original [receipt](verification/six-fields-support-exact-44563135178/receipt.json), [declaration inventory](verification/six-fields-support-exact-44563135178/declaration-inventory.json), process logs, and [preservation record](verification/six-fields-support-exact-44563135178/preservation.json) are preserved unchanged. The ZIP is artifact `14550958428`, SHA256 `2bc3b08c68ae7ae155015b1c1e8d212871781df5653350de749b1bb9f0ac8a20`; the receipt SHA256 is `eca423609c80888ebc5eb19a024b81b58e82343c3e758100e50ff408bd3676bf`.

All **22 project modules** passed fresh strict source checks and separate exact stock-kernel replay. The audit checked **837 owned and raw declarations**, including **545 theorems**, **72 private declarations**, and **22 required theorem endpoints**, using only `propext`, `Classical.choice`, and `Quot.sound`. The registration adds `LonelinessModularMultiplicity`, `LonelinessModularSupportLists`, and the three `LonelinessSixSpectrumFieldsSupportDefs`, `LonelinessSixSpectrumFieldsTransform`, and `LonelinessSixSpectrumFieldsSupport` modules. The generic support modules were existing public sources and were checked again in this exact closure.

`SixSpectrumFields.primeTriangleCover_of_checked_supports` proves the first-cover proposition for every nonzero raw residue sextuple, including repeated folded residues. Its proof retains distinct factor indices under independent signs, coordinate permutations, congruences, and multiplication by a modular unit. Pure modular normalization uses the absence of a modular witness, so it does not assume a real loneliness bound in the finite cover. A complete checked search covers all possible folded supports. The retained-row checks handle six distinct values and every possible repeated member of a five-value support.

The endpoint still requires a valid inverse table, every initial support-tree check, and `supportRelationsCheck` for every decoded retained row. It does not require the reverse claim that every retained row is a survivor. No numerical `PrimeTriangleCover p`, completed prime table, or universal six-speed spectrum classification is supplied by this component. The separate finite certificate and later dimension reductions remain pending.

### Accepted six-plane membership-to-family bridge

`LonelinessSixPlaneFamilies` is registered from the exact passing candidate `3273ac1a24ea061b0cbd73244e2ac57c08d491ec`, [run 44563135178, job 135701825634](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44563135178/job/135701825634). Its 66-module closure passed fresh strict source compilation, the complete owned/private axiom audit (1,795 owned and raw declarations, 1,449 theorems, 49 private declarations, all five required endpoints), and 66 separate exact stock-kernel target replays. Only `propext`, `Classical.choice`, and `Quot.sound` were allowed.

For any positive integer sextuple actually lying in a critical rational plane, the theorem gives a permutation of `(A,2A,3A,4A,5A,b)` or `(A,3A,4A,5A,9A,b)` with both integers positive, or the full signed third family. Primitivity and actual loneliness below `1/6` further force the product alternatives to `(1,2,3,4,5,6s)` or `(1,3,4,5,9,6s)` with `s ≥ 1`. The third alternative retains all real parameters and every coordinate sign. Exclusion of these literal families implies that the tuple lies in no critical plane, supplying the exact off-critical premise used by the norm route.

This component assumes actual critical-plane membership for its forward implications. It does not prove that every low-value plane is critical, discharge the remaining five-speed exhaustion, certify the complete six-plane finite table, or evaluate the full third family. Those obligations and result-level completion remain separate.

Artifact `14549664948` has ZIP SHA256 `b9ad7ea510611134327c246572be59b5b1ce67a9f75d3ba26ef63249cd385989`; the unchanged raw receipt has SHA256 `d06c6f0e813120dfe3bf118f5d9c96b516e1abfd02620114c372944caeb155fe`. All 79 historical source/control/configuration Git blobs, every archived object, process log and progress record, and the reconstructed ownership audit were authenticated. The original evidence and separate preservation record are under [`verification/six-plane-families-exact-44563135178/`](verification/six-plane-families-exact-44563135178/). Registration adds one module and five endpoints; it preserves the concurrent FieldsSupport registration.

## Complete tight-five classification and independent finite lower bound (19 November 2026)

The complete threshold classification at `1/6` is registered. A positive
primitive five-element natural-number tuple with actual loneliness at most
`1/6` is a permutation of `[1,2,3,4,5]` or `[1,3,4,5,9]`, and has value exactly
`1/6`. The normalized theorem applies to every positive list of length five;
its gcd-normalized list has one of those two forms. Distinctness is not an
extra premise of either classification statement.

`Loneliness.Modular.FiveRunner.five_runner_bound` and
`Loneliness.CoordinateSubspace.five_speed_lonelyRunnerBound` also prove the
lower bound `1/6` for every nonempty list of at most five distinct positive
speeds. This finite proof is independent of the already registered Renault
proof. The original Renault modules and endpoints remain registered.

[Run 44549751944](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44549751944)
at `1ffeb0932ac9a5674f2d416757d786a85e43ffde` passed all 250 fresh strict sources,
7,586 required theorems, four literal quantified contracts, and the complete
audit of 28,383 owned/raw declarations, including 118 private declarations.
The unchanged stock kernel replayed exactly the 250-module closure. The
118 generated modules reproduce all 394 minimum-pair roots and 7,070 frames
for primes `149,151,163,167,173`; all smaller-runner and prime-classification
hypotheses are discharged. Only `propext`, `Classical.choice`, and `Quot.sound`
are permitted transitive axioms.

The [authenticated original checkpoint](verification/loneliness-five-runner-exact-44549751944/README.md)
preserves every receipt, audit, generation, log, and process-record file.
Registration adds exactly 129 previously unaccepted modules and
7,577 previously unregistered required endpoints, including every
frame theorem. The other 121 dependencies were already accepted and
prebuilt with source bytes matching this run. GcdShift and Renault
registrations are preserved. The full five-speed spectrum below `1/5` remains
incomplete; no result-directory spectrum status is promoted. The merged
accepted-package gate remains separate from this complete component receipt.

## Modular support, unit orbits and literal binary lifts, 19 November 2026

Four authenticated component closures are now registered: support multiplicities
and the finite-tree consumer (98 modules, 63 required endpoints), unit-orbit
transport (26/8), literal seven-speed binary roots (34/58), and byte-count/check
equality (8/15). Their exact source, all-owned/private audit and stock-kernel
receipts are linked in the [component scope record](verification/modular-support-components-20261119.md).
The registration includes all 55 generated multiplicity source files from the
passing artifact and preserves every earlier accepted registry entry.

The seven-speed literal check retains the six-speed runner bound and does not
prove initial-support exhaustiveness. The multiplicity and orbit interfaces
retain their terminal and covering hypotheses. The byte evaluator has a
universal equality proof; its interrupted benchmark supplies no speedup result.
The separate prime-251 closed-lift gate and bounded initial-cut pilot have
passed their exact component gates; their limited scopes are recorded below. The merged accepted package
still requires its separate complete source, audit and stock-replay run.

## Seven-speed norm and reduced prime sets, 19 November 2026

`LonelinessSevenSpectrumNormGeometry` is verified and registered from source
`f782472e2ccd4d276ed6090b30727dbd2b92346e`,
[run 44576585527](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44576585527),
job `135745583518`. Its full 129-module project closure passed fresh strict
source compilation, all 27 required endpoints, seven literal quantified
contracts, the complete owned/private axiom audit, and 129 separate exact
stock-kernel replays. The audit covered 3,620 declarations, including 2,881
theorems and 280 private declarations. Only `propext`, `Classical.choice`, and
`Quot.sound` were permitted.

For an actual positive primitive seven-speed vector with loneliness at most
`1/7`, the component constructs the integral basis, derives all six Gram-prefix
bounds and the determinant identity, and proves
`8993 * squaredNorm v ≤ 1186638179795145`,
`∑ i, (v i)^2 ≤ 131951315444`, and Euclidean norm strictly below `363252`.
The remaining premise states that every rational plane containing the vector
has space value at least `5/33`. The accepted five-speed, four-speed, and
smaller-runner results discharge the smaller-runner hypotheses.

The original nineteen-prime avoiding theorem is preserved. The sharper norm
bound also gives an avoiding prime among the first sixteen original primes,
from `151` through `233`, under the closed threshold `≤ 1/7`. Under the strict
threshold `< 1/7`, the verified forced factor `420` reduces the set to the
first fifteen primes, through `229`. The strict assumption is retained in the
fifteen-prime theorem and its literal contract.

The [original evidence and full scope record](verification/seven-spectrum-norm-exact-44576585527/README.md)
bind the exact run, job, artifact `14556969731`, and source commit. All 782
archive members were authenticated. The original ZIP SHA-256 is
`e94a210f21bbd4f19e37bd1466c82948f25deb0bfb2e02b22562b5e5852bd948`; the unchanged
receipt SHA-256 is
`583fcd94f60c5606bb1ebdf9bf1030f59ac573e4b13e92cb1324d6a04216c0b1`.
Registration adds one module and 27 audit endpoints while preserving every
previous accepted entry. Li remains outside the accepted roots. The plane gap
and the final seven-speed finite residue classification remain open;
no result-directory completion status is promoted.

## Order-nine automorphism subgroups and orbits

For every abelian group of order nine, every odd subgroup of its actual
additive automorphism group has order dividing three. A nontrivial such
subgroup has order three and three fixed points. Its other two orbits are
the two nonzero cosets of the fixed subgroup, so there are exactly five
orbits in total.

`HadamardLegendreOrderNineGroup` and `HadamardLegendreOrderNineOrbits` are now
registered. Their four-module closure passed the original hosted strict
source, axiom, and stock-kernel gate at
`91b7afd6c31b5654e0d7aa0517a270c0b802eedc`, run 44523474204,
job 135557905916. All theorem-source and pinned-configuration hashes still
match. The original replay log contains exactly the four required modules.

Fresh local strict sources and the complete owned/private audit also passed:
68 declarations, 64 theorems, nine private declarations, and 13 required
endpoints, using only the three standard allowed axioms. The optional local
repeat of stock replay timed out and remains recorded as such. The
[preserved evidence](verification/hadamard-order-nine-orbits-44523474204/README.md)
separates the original hosted pass from the local outcomes.

The theorem sources are unchanged. Two prebuild targets and 13 required
endpoints are added. This verifies the order-nine action claims in the
Legendre-pair argument; exclusion of order 27 and the finite quotient/no-lift
packet remain outstanding. Hadamard existence at order 2396 stays open.

## Initial cut pilot and prime-251 binary lifts, 19 November 2026

Two further component gates passed from source
`8abe17f1b329ca1df0ae81f4e0b2c4425d1b03a6` and are registered with their exact
checked sources. The [scope and preserved evidence](verification/modular-cut-and-closed-lift-components-20261119.md)
record the source, all-owned/private declaration audit, and stock-kernel checks.

The cut pilot passed its complete 53-module closure and 54 required endpoints
in [run 44577155795](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44577155795).
It proves the complete small initial list for five speeds, denominator six and
prime eleven, plus the validity of all 19 prime-251 rows and only cuts 0 through
3 of the minimum-pair-four root. Exactly 30 generated sources were compiled,
audited, replayed and added. The other 105 generated sources remain outside
this accepted scope. Prime-251 initial-support coverage is still incomplete.

The closed binary-lift component passed 33 modules and 23 required endpoints
in [run 44577160577](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44577160577).
It checks all 19 ordered prime-251 roots, 2,451 states and 19 complete
128-child binary branches, to maximum depth two. Its classification theorem
retains the six-speed runner bound and the premise that the tuple is
represented by one of those roots. It does not establish initial-support
coverage or the full seven-speed classification.

Registration preserves all earlier entries and adds four imports, 68 audit
names and 33 explicit prebuild/replay modules. No result-directory completion
status changes. A complete merged-package source, audit and kernel replay
remains a separate verification obligation.

## Rational integer-point lattices and six-speed norm components

The registered components construct the full integer-point lattice of
every rational coordinate subspace, prove its span and rank, and identify its
squared covolume with the Gram determinant of an actual integer lattice basis.
They prove squared covolume at least one. In rank four in six coordinates,
the lower bound is six when the subspace contains an integer vector whose
coordinates are nonzero and pairwise unequal up to sign.

Suppose an integer matrix has r columns lying in a rational subspace of
dimension r, and its Gram determinant is positive. The proof gives an
exact factorization of the column Gram determinant as a nonzero integer
square times the full lattice's squared covolume. It therefore bounds the
full lattice's squared covolume by the column Gram determinant. The endpoints do not
identify that integer with the cardinality of a finite quotient.

The rectangular components also prove integer-parameter recovery under an
integer left inverse, primitive basis transfer, Cauchy--Binet and integer Gram
identities, and the literal map Gram determinants 3, 9 and 8. The six-by-four
Gram lower bound assumes positive Gram determinant, nonzero rows and rows
that are pairwise unequal up to sign; it derives the bound six internally.

The original norm constants 9075, 54450 and 163350 now use the covolume of the
actual full integer-point lattice. The 9075 theorem assumes rank four,
containment of the speed vector, and distinct positive primitive speeds.
The 54450 and 163350 theorems hold for every rational coordinate subspace,
without a rank or containment premise. All three norm theorems retain
`hfour : CoordinateSubspace.LonelyRunnerBound 4` and `hplane`, the containing-plane gap
hypothesis, as well as positivity, primitivity and loneliness at most `1/6`.
These are component theorems. The unconditional plane-gap deduction and the
remaining exhaustive classification are not supplied here; the six-speed
spectrum result remains partially formalized.

The complete 60-module hosted gate passed at `e815f14555472b873683f491bc878eb16d4eb0a4` ([run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44590263136/job/135794055426)). It checked all fresh strict sources, all owned and private declarations, all 50 required theorem endpoints, and one exact stock-kernel target per module. The permitted axioms were only `propext`, `Classical.choice`, and `Quot.sound`. The unchanged receipt has SHA-256 `4a3f6a5df8723dc21f2b5eb2899a10ea55b47b9eb0538cd48927016c0195e4ee`. The merged accepted-package check remains a separate obligation.

[Preserved receipt](verification/rectangular-lattice-exact-44590263136/receipt.json).

## Prime filtering and proved runner classes, 19 November 2026

Twelve prime-filtering modules are registered. They formalize Lemma 2 and
Corollary 3 of Barajas and Serra, *The lonely runner with seven runners*
(Electronic Journal of Combinatorics 15 (2008), R48, DOI 10.37236/772).
The proofs produce an actual prime-power unit, preserve higher residues
when starting from a coprime seed, and derive modular witnesses and bounds
for the real-valued loneliness function.

For positive speeds, the verified `1/7` consequence assumes that every
7-adic valuation level below the maximum contains at most three distinct
speeds. The highest level has no cardinality restriction. Repeated speeds
are allowed. A separate uniform-valuation theorem gives the `1/p` bound
for any base `p ≥ 2`, with no restriction on the number of speeds.
The four- and five-input exceptional lower levels, and the unrestricted
six-speed runner theorem, remain pending.

[Run 44591941338](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44591941338)
at `e6d53ced9fd3b6ad4a311c3eecbe1fcbd0cdd491` passed the complete
18-module closure: fresh strict sources, 68 required theorem endpoints,
33 literal quantified contracts, the full audit of 299 owned declarations
(243 theorems and 10 private declarations), and 18 exact singleton stock-kernel
replays. Only `propext`, `Classical.choice`, and `Quot.sound` are permitted.
All 116 original artifact members and every source, object, process record,
audit inventory and pinned control hash were authenticated. The receipt
SHA-256 is `009a768a638e275c6705f1bc08c316ca3686553bd591c2c25765fc29531ed394`.

[Original evidence and exact scope](verification/prime-filtering-exact-44591941338/README.md).
Every previous accepted entry is preserved. Li remains outside the accepted
roots. The complete merged-package gate remains a separate obligation;
no result-directory completion status changes.

## Conditional two-parameter radius estimate

For an integer matrix with two columns and a finite nonempty row set, the theorem uses the actual real column span and the actual line generated by a primitive signed integer parameter pair. The primitive premise is `Int.gcd x y = 1` on the parameters. For any real upper bound `C` on every squared row norm, `plane_value_le` bounds the plane value by the line value plus `1/2 * sqrt(C / (x^2+y^2))`.

If the actual plane value is at least `2/11` and the actual line value is strictly below `1/6`, the proof gives `x^2+y^2 < 1089*C`. Taking the exact finite maximum of the squared row norms gives the natural-number bound `x.natAbs^2 + y.natAbs^2 < 1089 * maxRowSq A`. An explicit coordinate-equality theorem carries this bound to a natural six-speed vector. It does not separately require the natural speed vector to be positive, distinct or primitive, and adds no rank, integer-left-inverse, four-speed or six-speed-classification premise.

The plane gap remains an assumption. This theorem does not classify the 78 maps or complete the six-speed spectrum.

The complete 13-module hosted gate passed at `6932e0ba9c532f86fbf9e5fb23aff9e55b8e99f9` ([run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44593469748/job/135805428239)). It checked all fresh strict sources, all 295 owned declarations including 13 private declarations, all 6 required theorem endpoints, and one exact stock-kernel target per module. The permitted axioms were only `propext`, `Classical.choice`, and `Quot.sound`. The unchanged raw receipt has SHA-256 `b4722be2222c18d959a57252b8bc797e71a489c41d6c3c0b92647fadaf663de7`. A merged accepted-package source, audit and kernel pass remains a separate obligation.

[Preserved receipt](verification/two-parameter-radius-exact-44593469748/receipt.json).

## Six-speed norm bounds with the four-speed input discharged

The three new six-speed lattice norm bounds supply the proved four-speed runner theorem internally. They retain the containing-plane gap, positivity and primitivity of the natural speed vector, and loneliness at most `1/6`. The bound with constant 9075 additionally assumes a rational subspace of rank four containing the speed vector and pairwise distinct speeds. The bounds with constants 54450 and 163350 apply to every rational coordinate subspace, without a rank, containment or distinctness premise. The lattice is the actual full integer-point lattice.

The new endpoints end in `_of_plane_gap`. They remove the explicit `hfour` input and retain `hplane : SixSpectrumNormGeometry.ContainingPlaneGap v`. The old endpoints keep their original signatures. These results do not prove the containing-plane gap or complete the six-speed classification.

The complete 113-module hosted gate passed at `14f3403c7afe204c85b376df0f02c68c86c7fea0` ([run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44591091795/job/135796982020)). It checked all fresh strict sources, all 3108 owned declarations including 90 private declarations, all 3 required theorem endpoints, and one exact stock-kernel target per module. The permitted axioms were only `propext`, `Classical.choice`, and `Quot.sound`. The unchanged raw receipt has SHA-256 `af61227a92a04443c42d8c928139f13a9bb201b3bfd5b359f464138f2d3ae5ac`. A merged accepted-package source, audit and kernel pass remains a separate obligation.

[Preserved receipt](verification/lattice-norm-four-speed-exact-44591091795/receipt.json).

## Seven-coordinate implications with the five-speed input discharged

The new seven-coordinate critical-plane and large-norm statements supply Renault's proved five-speed runner theorem internally. Every new endpoint retains `hsix : PrimitiveSixClassification`. The plane results concern rational subspaces of dimension two. One classifies coordinate-free planes with value at most `1/7`; another assumes equality to `1/7` without a separate coordinate-free premise; the third states that equality is equivalent to `StandardProductPlane`.

The quantitative results concern positive primitive natural speed vectors with Euclidean norm at least `7 * 42^10`. Below loneliness `1/7`, such a vector is a permutation of `[1,2,3,4,5,6,7*s]` for an integer `s >= 1`, and its loneliness is `s/(7*s+1)`. The family equivalence puts the strict loneliness inequality on the left side of its equivalence. No separate distinctness premise is added. The six-speed classification remains an assumption; these implications do not establish the full seven-speed classification.

The complete 171-module hosted gate passed at `9c5b1203a4405508254332b1d13dd19f9bdefe38` ([run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44592471446/job/135801829445)). It checked all fresh strict sources, all 4246 owned declarations including 850 private declarations, all 6 required theorem endpoints, and one exact stock-kernel target per module. The permitted axioms were only `propext`, `Classical.choice`, and `Quot.sound`. The unchanged raw receipt has SHA-256 `25d85fa1a9a5fa514e1a1505d370790f273656bafa3a9c4b991316ba9f043b5e`. A merged accepted-package source, audit and kernel pass remains a separate obligation.

[Preserved receipt](verification/critical-seven-five-speed-exact-44592471446/receipt.json).

## Four-input prime filtering, 19 November 2026

Twenty modules are registered for the four-input filtering step in the
seven-runner argument. For four natural inputs nonzero modulo seven and
any exponent `m`, the theorem gives `1 <= j <= 5` and `0 <= k <= 6` such
that `j + k*7^m` is coprime to `7^(m+1)` and each actual folded residue
is at least `7^m`. Every input divisible by seven keeps its full residue
relative to multiplication by `j`. Repeated inputs are allowed.

The finite quotient sampling, symmetry reduction, ten canonical decision
checks and natural arithmetic transport are all proved. No finite-check
hypothesis remains. The higher-family seed must still be safe under the
selected multiplier `j`; this component does not supply that seed or prove
the unrestricted six-speed runner theorem. The five-input lower-level
case also remains outside this component.

[Run 44601096014](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44601096014)
at `8d1933b7b568515fe5bf7e8b474fe22e284521e8` passed 20 fresh strict
source checks, four literal contracts, all seven required endpoints,
the complete owned and raw-occurrence audit, and 20 exact singleton
stock-kernel replays. The audit covers 133 declarations and 97 theorems.
Its closed raw dependency graph has 5,101 nodes and 70,060 edges, with
only `propext`, `Classical.choice`, and `Quot.sound`. All 128 original
artifact members and exact source, object, import, control, log and profile
bindings were independently authenticated.

[Original evidence and exact scope](verification/prime-filtering-four-exact-44601096014/README.md).
All prior accepted entries, verification code and the axiom whitelist are
preserved. No result-directory completion status changes. The full merged
accepted-package gate remains a separate obligation.


## Li coefficient-sign counterexample

The 44-module development is registered with 71 required theorem
endpoints. The original hosted gate passed at source snapshot
`20e0e95eb421cf8ea728d34aa29a6d0eb1137789`: all 44 fresh strict sources,
25 literal contracts, 1,247 owned declaration names (932 theorems and
95 private names), all 71 required endpoints, and 44 exact stock-kernel
targets. The separate hosted supplement passed against the same object
bytes and covers every reachable serialized proof occurrence. Both
original artifacts and the complete baseline backup were authenticated
and independently reviewed before this registration.
The original 38-module contribution is by [aadrianvv](https://github.com/aadrianvv)
in [PR #35](https://github.com/1337isnot1337/solved-conjectures/pull/35),
original head `fb700255fed86b6ac29b4980ff4704fa46adab63`.

The explicit tree has 31 vertices, maximum degree 4, one degree-4 vertex with
exactly one leaf neighbour, and is neither a spider nor a caterpillar. Every
one of the 6,842 integer partition types is realized by genuine nonempty,
disjoint, covering connected vertex blocks. Exactly eight connected
partitions have type `(3,2^14)`. An equivalence with deleted-edge subsets gives
exactly `2^30 = 1,073,741,824` connected vertex partitions in total.

For every finite colour type of cardinality at least 31, the actual
proper-colouring polynomial has full elementary coefficients
`[e₂¹⁴e₃]=29` and `[e₂⁸e₃⁵]=−6304`. The five degree-31 coefficients using only
`e₂,e₃` are `29, 83, −6304, −6800, −8384`. Full-coordinate restriction and
colour-renaming theorems prove stability. No separate infinite-variable
symmetric-function ring is constructed, and 31 is a sufficient degree-bound
threshold without a minimality claim for these coefficients.

The positive coefficient contradicts Li's strict-negative prediction in
Problem 4.9. The leaf count contradicts the first question of Problem 4.6.
The count eight contradicts the separate informal prediction
`b_(3,2^14)=1`; uniqueness of the degree-4 vertex remains true. The negative
coefficient proves that this tree is not elementary-positive.

The original Python dynamic program and the vertex-deletion contribution
argument remain alternative explanations. The formal development proves the
main conclusions independently; it does not certify those Python programs
or every numerical step of the alternative argument. The separate graph-
distance and branching source `LiStructure` is outside this 44-module
acceptance. Its dedicated verification closure also includes `LiBasic`.

[Theorem inventory, scope and attribution](../results/li-coefficient-sign/LEAN.md).
The complete merged accepted-package gate remains separate. Earlier dated
checkpoints retain their historical scope, including their former Li queue
status. The repository-wide campaign remains incomplete.

The original [run 44599210697, job 135825706963](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44599210697/job/135825706963)
produced artifact `14568527194`, ZIP SHA-256
`281b57fd87cf7d6123cdcabff4a5803f3d426116dbb4a9aa01370318b2a138ed`.
The unchanged receipt SHA-256 is
`da585dbd99530825af7bac8c4730c1a6666bfa151ce98ad4c6f52b9d537aa09d`.
All 272 original members, source/object/direct-import bindings, process
logs and profiles, original git controls, and compiler/checker pins have
been authenticated. The artifact authentication SHA-256 is
`cc956d198ed081f35fb7ea35ff22aaf9bbec7b3ce2138519c43db53d778fef29`;
the independent root review SHA-256 is
`9de0d30a11a09d0c54bfdd76358f6ef2e3abdcc07254c314af520bbfbd04361b`.

The [raw-occurrence supplement, run 44606051622 / job 135849912826](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44606051622/job/135849912826)
passed at `26ef845d1ec4adb15e0c87c9264905baeb69491f` against the exact original
44 compiled objects. It rechecked all 25 literal contracts and traversed
17,647 dependency nodes and 316,338 edges from all 1,247 owned declarations.
The scan indexed 22 differing theorem bodies across the imported environment;
none was reachable from those roots, so no extra variant alias checks were
needed. The trust-zero checked-kernel negative control was rejected. The
only transitive axioms were `propext`, `Classical.choice`, and `Quot.sound`.

The raw artifact is `14569498196`, ZIP SHA-256
`7ea288555021d503775aa3886fc59edc65ae9a096ca26bb9add7e9950b1e1489`,
with receipt SHA-256
`8cb7e81896bc67b3c68ed976f256e6894b6c52318063ab0894360fed1d0a8b46`.
The preserved baseline backup is artifact `14569584489`, ZIP SHA-256
`dfbb03a7571256df786f9c28f45b306cb924f89403ba403d81063072e6f1eb2f`;
its inner archive equals the original baseline ZIP byte for byte.
The raw-artifact authentication SHA-256 is
`6abda54c54c591fef864220fd7624374ad25af865a94989204969305eecb0610`;
the independent review SHA-256 is
`8f14f2f5844973ea3d432b741185e01a8385841fc0d8f8b90e7181e88f5d6aee`.
The supplement retains the original source-build and stock-replay evidence;
it does not claim to have repeated those stages.

## Actual rational-lattice quotient index

For a rational coordinate subspace E of dimension r, let L be its actual full integer-point lattice. An integer matrix A with r columns in E and positive Gram determinant generates the sublattice M = columnSubmodule E A. Relative to an actual integer basis of L, the columns have an integer square coordinate matrix C. Lean proves that the quotient cardinality Nat.card (L ⧸ M) equals the absolute determinant of C and is positive. It then proves the exact identity det(AᵀA) = [L:M]² * covolume(L)². The containment, dimension and positive-Gram hypotheses are explicit; no saturation or quotient-index identity is assumed.

This identifies the integer determinant factor in the earlier Gram/covolume comparison with the actual finite lattice quotient. It does not discharge the containing-plane gap or complete the six-speed classification. The six-speed result remains partial.

The complete 20-module hosted gate passed at `a8577e5da31b851ce64333aa921b39c6623e0389` ([run and job](https://github.com/1337isnot1337/solved-conjectures/actions/runs/44606981694/job/135853171450)). It checked all fresh strict sources, selected declaration values and types for 446 owned names including 12 private names, all 5 required theorem endpoints, and one exact stock-kernel target per module. The audit includes raw/private-name visibility; it is not a separate audit of every duplicate theorem body occurrence. The permitted axioms were only `propext`, `Classical.choice`, and `Quot.sound`. The unchanged raw receipt has SHA-256 `62b4ab2b3b0dcdaa55b210e5de3e8322e7e6b57201b05e085983d8ff0882afa2`. A merged accepted-package source, audit and kernel pass remains a separate obligation.

[Preserved receipt](verification/rational-lattice-quotient-exact-44606981694/receipt.json).
