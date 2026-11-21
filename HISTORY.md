# History

## 2026-11-20 — Malek's conjecture

Added a complete proposed proof of Malek's all-degree negative-transform subpermanent inequality, including equality. The reciprocal-mean capacity cost improves the optimized-slice estimate enough to separate the lower and upper constants in every proper degree. The permanent endpoint is credited to prior work. Two independent internal reviews and a standard-library rational checker found no gap; the proof is unrefereed. A bounded audit of primary literature, recent transform followups, and public repositories found no earlier complete endpoint theorem. The original 1989 full text remained inaccessible, while Cheon–Wanless's 2005 survey states the exact conjecture. This is a named subsidiary in the Minc site's linked literature, not an additional numbered entry. No Lean work was performed.

## 2026-11-20 — Independent outside confirmation of Németh–Seberry–Shu

[Yair Lavi's Minc Conjecture 27 record](https://yair-lavi.com/mincs-list/conjecture-27/index.html) now identifies the conjecture as disproved by Cinna Davis and GPT-6.2 Astra, including the quadratic lower bound, and reports an independent audit that found no gap. The main index marks this outside confirmation with ★, separate from Lean status. This is not journal peer review.

## 2026-11-21 — Mazák–Zrubák conjecture on complete graphs minus an edge

Proved Conjecture 2 of Mazák and Zrubák: for every even `d >= 6`, the circular chromatic index of `K_{d+1}` minus an edge is `d+1`. By Guichard's theorem a smaller value would give a proper `(d+1)`-edge-colouring whose digraph of consecutive colours is acyclic; the proof derives a contradiction from the longest-path levels of such a colouring. The package contains the written proof, a standard-library check of the lemmas for `d=4` and of the ordering obstruction for `d=6`, an optional SAT check from the definition, and the scripts of one independent model referee pass, which found no mathematical error. The scripts did not complete `d=8`. The note is otherwise unrefereed; no Lean verification was performed.

## 2026-11-20 — Sagan–Swanson formula rendering

Replaced an unsupported fixed-width TeX spacing command by standard spacing in the two Sagan–Swanson proof copies. The displayed formula is unchanged. The unsupported command blocked the native MathML site build after catalogue registration was repaired.

## 2026-11-20 — Oravcová–Soták distance-graph conjecture

Added the classification of primitive distance sets of size five through eight with maximum chromatic number, relative to the repository's five-, six-, seven- and eight-speed spectrum classifications. The package contains a written proof, 62 periodic colourings, loop certificates for four one-parameter families, base loops for the two-parameter six-distance family, an independent standard-library verifier, and a separate SAT scan. The note is unrefereed and conditional on the spectrum classifications; no Lean verification was performed. Contributed by [@aadrianvv](https://github.com/aadrianvv) in [PR #144](https://github.com/1337isnot1337/solved-conjectures/pull/144).

## 2026-11-20 — Repaired an omitted result registration

Registered the existing `baricz-pogany-coefficients` package in the shared catalogue, root index and status map after its orphan landing page blocked the site build. The mathematical files and their stated scope were preserved. This is integration of previously published work from issue #112, not a new result of the Minc campaign.

## 2026-11-20 — Pula–Song–Wanless conjecture

Added a complete proposed proof of the named threshold conjecture for all positive block sizes with `n>1`. At `n>=m+sqrt(m)` the stated boundary matrix uniquely minimizes the permanent. The equality threshold is included. A real-rooted-minor argument replaces a gap in the available 2011 equalization proof; a separate van der Waerden completion proves uniqueness. The known cohesive and non-barycentric directions are credited and independently checked. The result includes two written independent reviews, exact identity audits and a source audit through November 2026. The notes are unrefereed and priority remains provisional. This does not resolve the unrestricted Minc Problems 14 or 15, and no Lean verification was performed.

## 2026-11-20 — Perron root of permanental compounds

Added a general FPRAS theorem for Minc Problem 18's approximation formulation. The result covers every nonnegative rational input and every compound degree, with deterministic zero detection. A stable-symbol trace bound, cyclic permanent reduction and rational grid give the algorithm without constructing the compound. The directory includes the full proof, exact finite checks, two independent reviews and a source audit. This is not an exact polynomial-time eigenvalue-computation claim, and it does not solve the characteristic-polynomial problem. No Lean verification was performed.

The Minc research record also documents partial Gyires and integrality results without counting them as full resolutions.

## 2026-11-20 — Zhang's Question 8.4

Answered Zhang's Question 8.4: the deletion values `LR([n-1] \ {r})` are `1/r` when `2r > n-1` and `2/D_r` when `2r <= n-1`, so the strict inequality holds for all `n >= 4` and `1 <= r <= n-2`. The package contains an elementary proof and an exact standard-library verifier for `n <= 40`. The note is unrefereed; no Lean verification was performed. Contributed by [@aadrianvv](https://github.com/aadrianvv) in [PR #143](https://github.com/1337isnot1337/solved-conjectures/pull/143).

## 2026-11-20 — Removed previously resolved conjectures

Removed the result entries and duplicate research writeups for Karp's
coefficient-positivity conjecture, Karp–Vishnyakova–Zhang's reciprocal
q-gamma and Hankel-product conjectures, Simon's Le Roy conjecture, and
Gatzweiler–Krattenthaler's unrestricted shifted-product Conjecture 4.
Earlier exact resolutions were established by Principia Math In Progress
(MathDB 323156 and 349140), Knowledge Sense's October 2026 preprint,
Simon's Beta–Gamma theorem, and the CoPEER archive. The
[prior audits at the pre-removal revision](https://github.com/1337isnot1337/solved-conjectures/tree/a354c349b80c70bb575ffc0230d17c3ced5ec7f7/results)
record the source and scope for each correction.

Removed standalone research writeups for the previously resolved binomial
Eulerian, intrinsic-volume sequence, and inverse-gamma Newton-series
targets. The catalogue and verification instructions now describe the
remaining collection.

## 2026-11-20 — Chow proof rendering

Replaced an obsolete bold-math command in the two Chow proof copies
with standard mathematical markup after it blocked the research-site build.
The mathematical statement is unchanged.


## 2026-11-20 — Karp–Vishnyakova–Zhang's Bessel-ratio unimodality conjecture

Added a complete proof of the full surviving unimodality assertion for all
ordered real orders greater than minus one and all ordered positive scales.
The Bessel differential equation gives a Wronskian derivative with at most
one positive-to-negative sign change. Positive series terms determine the
endpoint signs and give the complete monotonicity/unique-maximum
classification, including negative orders and every equality case.

The separate stronger log-concavity clause was already refuted and is not
claimed here. Root and analysis completed independent written audits.
Exact rational series checks passed 130 coefficient identities and ten
endpoint/positivity checks. The prior-work audit distinguishes adjacent-order,
same-argument, and Kaiser–Bessel results from this full assertion. No outside
peer review or exclusive priority is claimed.

[Proof, classification, exact checks, and source audit](results/kvz-bessel-unimodality/).

## 2026-11-20 — Ferreira–Simon's Wright log-concavity conjecture

Added a complete disproof of the conjectured equivalence between the
gamma-defined parameter threshold and log concavity of the Wright density.
Gamma reflection and log convexity give a uniform summable coefficient
bound. The resulting differentiated-series limit has explicit curvature
of the wrong sign on entire intervals of admissible parameters, including
strictly interior positive beta.

The full written proof passed separate root and algebra reviews. Exact
rational-polynomial checks passed for the general curvature identity and
the displayed derivative values. The analytic convergence argument supplies
the counterexample intervals. The source audit records both search engines,
current author records, later primary-paper comparisons, and full-text
access limits. No outside peer review or exclusive priority is claimed.

[Proof, source audit, and exact algebra](results/ferreira-simon-wright/).

## 2026-11-20 — Karp–Vishnyakova–Zhang's gamma-quotient conjecture

Added a complete proof of all-order sign regularity for the additive gamma
quotient with every positive parameter difference. An explicit Wronskian gives
the signs for the power kernel; two gamma-density integral transforms transfer
those signs to the quotient through continuous Cauchy–Binet. The proof includes
absolute integrability, strictness, all integer rank cutoffs, and translated
domains with positive gamma arguments.

The source's proposed fixed third-order signature is corrected within the same
result. Two independent reviews of the full proof passed. A standard-library
verifier passed 115 exact rational checks of half-integer signs, integer rank,
and gamma-moment normalization. These finite diagnostics are supplementary to
the all-parameter proof. The source audit records both search engines, primary
theorem comparisons, public solution checks, and inaccessible-source limits.
No external peer review or absolute priority guarantee is claimed.

[Proof, source audit, and exact checks](results/kvz-gamma-quotient/).

## 2026-11-20 — Alexandersson's Fuss–Catalan conjecture

Recorded a short uniform deduction of the named real-rootedness conjecture.
Classical Kreweras/cycle-lemma enumeration shows that, after fixing the
number of north steps and north runs, the Fuss parameter changes only a
positive scalar. The real-zero polynomial is already known from the
ordinary-Dyck work of Bóna and coauthors and Wang–Zhang. A self-contained
Rolle argument is included for independent checking.

The complete argument passed independent review. Direct enumeration of
10,188 paths across 18 parameter pairs checked the exact source convention.
These finite comparisons are diagnostic. The attribution record expressly
credits both classical ingredients and records an inaccessible recent
paper; no unconditional novelty claim is made. This entry is distinguished
from a new enumeration or a new root-preserving theorem.
[Proof, classical attribution, and checks](results/alexandersson-fuss-catalan/).

## 2026-11-20 — Sagan–Swanson conjecture

Added a complete proof of asymptotic normality for all four q-Stirling
coefficient distributions in the proportional regime of Conjecture 7.8.
An exact conditioned probability model reduces the elementary and complete
homogeneous symmetric-function families to one theorem. A direct Fourier
bound controls the conditioning, and exponential tilting proves convergence
of the actual means and variances. The limiting variance is positive and
has order $n^3$.

Independent source/model and analytic audits passed, followed by a separate
review of the full written proof. The standard-library verifier passed 168
exact identities against the four original recurrences. These finite checks
do not replace the asymptotic proof. The literature record distinguishes
older row-distribution and fixed-parameter theorems, as well as the already
resolved bottom-heaviness conjecture, and states the access limits.
[Proof, source audit, and model checks](results/sagan-swanson-normality/).

## 2026-11-20 — Bernardi–Morales's delta-process conjecture

Added complete written proofs of the delta-process tree-probability identity
and the stronger event-determinant identity, published as Conjectures 27–28
and numbered 21–22 in the preprint. The tree count holds for each fixed
color map, and the event identity holds for each fixed surjection.

The two arguments use cycle Laplacians and cyclic adjugates, respectively.
The event proof explicitly handles full subsets, where the cycle matrix is
singular. Separate internal reviews checked the original event definitions,
the determinant identities, and membership-coefficient extraction.
The standard-library verifiers passed locally on Python 3.12.14: 71 fixed
maps and 111,721 tree-process pairs; 25 arbitrary-matrix determinant checks;
and 342 marked-surjection profiles with 438,952 literal event determinants.
The literature audit records checked sources and access limits. External
peer review and author confirmation have not been obtained.
[Result, both proofs, and checks](results/bernardi-morales-delta/).

## 2026-11-20 — Gilmore and Chow conjectures

Added an all-row proof of
Gilmore's crossing–nesting matrix identity with an alignment refinement,
and a proof of consecutive type-D Eulerian interlacing.

The weak Chow assertion is a direct consequence of Savage–Visontai's
published refinement theorem; that dependency and the separate strictness
argument are explicit. Each result includes its primary conjecture source,
a bounded literature audit, precise scope, and reproducible exact checks.
A second agent independently checked each mathematical argument. The
published verifiers passed locally on Python 3.12.14, with SymPy 1.14.0 for
Chow's checks. No Lean work was performed.
[Result entries and scope](CONTENTS.md#polynomial-identities-and-positivity).

## 2026-11-20 — Németh–Seberry–Shu conjecture

Added a written disproof of the all-row-sums conjecture for prime-order
binary circulant permanents and linked the quadratic strengthening.
[Result and scope](results/nemeth-seberry-shu/).

## 2026-11-20 — Horňák–Woźniak and Sonntag–Teichert conjectures

Added written proofs and literature checks for both connected-partition
conjectures of Horňák and Woźniak and for Sonntag and Teichert's
tournament domination hypergraph conjecture. The respective exact
cross-checks pass. The same campaign added partial results for the Erdős
essential-component, Erdős–Sauer, Bollobás–Erdős–Tuza and Erdős–Oler
conjectures. [Proofs and research notes](CONTENTS.md).

## 2026-11-19 — Four-input prime filtering

Registered 20 modules after the complete hosted source, literal-statement,
owned/raw-occurrence audit and stock-kernel gate passed. Ten canonical
finite checks now give an unconditional arithmetic filter for four inputs
nonzero modulo seven, with actual folded bounds and higher-residue
preservation relative to one of the multipliers 1 through 5.
The unrestricted six-speed runner theorem remains pending.
[Scope and original evidence](docs/verification/prime-filtering-four-exact-44601096014/README.md).

## 2026-11-19 — Prime filtering and proved runner classes

Registered twelve modules after the complete 18-module hosted gate passed
strict sources, 33 literal contracts, all 299 owned declarations, and exact
stock-kernel replay. The proofs formalize the published prime-filtering
lemma and seeded distance corollary. The `1/7` runner consequence retains
the three-distinct-speeds budget at each valuation level below the maximum.
The unrestricted six-speed bound remains pending.
[Scope and original evidence](docs/verification/prime-filtering-exact-44591941338/README.md).

## 2026-11-19 — Registered order-nine automorphism subgroup and orbit proofs

Registered the two existing modules for odd automorphism subgroups of abelian
groups of order nine. They prove subgroup order three, three fixed points,
and five orbits in the nontrivial case. The four unchanged source modules
retain their original hosted strict-source, axiom, and stock-kernel pass.
A fresh local strict-source check and complete 68-declaration audit also
passed; the separate local repeat stock replay timed out and is preserved
with its actual outcome. The length-1197 order-27 exclusion remains pending.
[Exact scope and evidence](docs/verification/hadamard-order-nine-orbits-44523474204/README.md).

## 2026-11-19 — Complete tight-five classification and independent finite lower bound

Registered the complete primitive and gcd-normalized five-speed equality
classification at `1/6`, with exactly `[1,2,3,4,5]` and `[1,3,4,5,9]` as primitive
directions. The proof also gives an independent finite derivation of the
five-speed lower bound; the earlier Renault proof remains registered.

The original run 44549751944 passed all 250 fresh strict source modules,
7,586 required theorem endpoints, 7,070 finite frames, the complete raw/private
axiom audit, and exact stock kernel replay. Every finite source was reproduced
and the original artifact authenticated. The full five-speed spectrum below
`1/5` remains incomplete.
[Exact statements and preserved evidence](docs/verification/loneliness-five-runner-exact-44549751944/README.md).

## 2026-11-19 — GitHub proof rendering and results index

- Simplified the README results table to directory links and Lean status emoji.
- Standardized Markdown math for GitHub and kept native MathML on the reading site.

## 2026-11-19 — Conditional norm reductions for nine through thirteen speeds

- Registered the actual primitive-speed norm cutoffs and prime-selection
  theorems, retaining every smaller-dimensional runner bound as an explicit
  hypothesis. The basis geometry and all 7,936 KZ subset rows are proved internally.
- Exact run 44530735399 checked 81 strict sources, 1,696 owned/raw declarations
  (1,445 theorems and 538 private declarations), 25 required theorem endpoints
  and 81 exact stock-kernel targets. Original evidence is authenticated under
  `docs/verification/loneliness-large-norm-exact-44530735399/`.
- Added 64 proof modules and 25 required endpoints. The equality classifications
  remain partial; lower-runner bounds, modular exhaustiveness and uniqueness
  are still required. The merged accepted-package gate remains separate.

## 2026-11-19 — Complete fixed-hyperplane formalization

- Registered the original fixed-hyperplane probability, counting, Haar-shift,
  endpoint and sharpness statements, preserving the ordered positive distinct
  sampling model and all original hypotheses.
- Exact run 44531509741 at `ee1f018fef258cdd54f73af31cdaf6485fd151cb` checked all 72 sources with warnings as
  errors, all 1,403 owned declarations (1,149 theorems and 44 private declarations),
  all 106 required theorem endpoints and all 72 exact stock-kernel targets.
- Preserved the unchanged raw receipt and authenticated original evidence under
  `docs/verification/hyperplane-main-exact-44531509741/`.
  Registration adds 63 proof modules and 102 previously unregistered endpoints.
  The merged accepted-package gate remains separate.


## 2026-11-19 — Both six-speed spectrum realization branches

Registered the unconditional existence theorem for every proposed six-speed
value `(P−1)/(6P)`, for `P ≥ 7` congruent to one or five modulo six.
The witnesses are positive, distinct and primitive; their exact global
values include actual attaining times. The 11-module closure passed fresh
strict sources, the audit of all 392 owned declarations including 30 private
declarations, and every exact stock-kernel target. All 15 required endpoints
are theorems. Universal classification remains incomplete.
[Scope](docs/lean-status.md#six-speed-spectrum-complete-realization) ·
[Receipt](docs/verification/six-spectrum-realization-44527134869/receipt.json).


## 2026-11-19 — Complete unrestricted two-speed insertion theorem

Registered the full two-speed insertion result, including the arbitrary
positive speeds, prescribed interval, Goddyn–Wong acceleration criterion,
common-dilation value bound, small and unbounded branches, and literal
three-insertion obstruction. The exact 27-module closure passed fresh
strict source checks, an audit of all 563 owned declarations including
11 private declarations, and exact stock-kernel replay of every module.
All 49 required endpoints are theorems. The registration adds 18 proof
modules and preserves the checked source hashes.
[Scope](docs/lean-status.md#complete-unrestricted-two-speed-insertion-theorem) ·
[Raw receipt](docs/verification/two-insertions-exact-44524198858/receipt.json).
The merged-package gate remains separate.


## 2026-11-19 — Actual Legendre-pair construction and quotient transport

Registered the matrix constructed from an actual Legendre pair, including the order-2396 specialization, and the actual invariant quotient/layer data used to exclude order 27. Their exact closures passed all three gates: construction, five modules and 87 project theorems; quotient transport, eighteen modules and 353 project theorems. Eight previously unregistered modules and thirteen named endpoints were added. The full finite no-lift certificate and final multiplier bound of nine remain pending.
[Statements and receipts](docs/lean-status.md#actual-legendre-pair-matrix-and-quotient-transport).

## 2026-11-19 — Complete Erdős 607 line-size asymptotic

Registered the sharp asymptotic for the actual real-plane record count, with
the exact leading constant. The proof discharges the characteristic-product
limit, Fourier domination, core-lattice integral, Gaussian constant, and
normalization. Its 78-module closure passed strict sources, a 1,582-theorem
standard-axiom audit, and independent pinned-kernel replay at `36b13722`.

The analytic generating function and actual Fourier coefficient identity also
passed their 39-module/867-theorem closure at `daa7d2c5`. Both exact receipts
are archived after comparison of all 93 recorded paths. The 44 new proof
modules and 20 required endpoints complete the stated note, alongside its
earlier geometry and formal-series proofs. The full merged-package gate is
separate; Li remains last.
[Exact statement and receipts](docs/lean-status.md#complete-erdős-607-line-size-asymptotic).

## 2026-11-19 — Complete Frankl high-girth frequency theorem

Registered the full all-point `518208/1000000` distinct-union bound for every
uniform generator size at least three, under three-regularity and incidence
girth at least sixteen. Actual boundary configurations, finite fiber
averaging, all twelve small-degree certificates, and the large-degree
linearity consequence discharge every proof input. Both girth formulations
and removal of the empty union are included.

The exact 64-module closure passed fresh strict sources, the all-owned
1,363-declaration axiom audit, and pinned stock-kernel replay. The 47 new
modules and 34 new required endpoints are registered; the full merged gate
remains separate. The cyclic span-four result and the overall campaign
remain incomplete. [Checked scope and receipt](docs/lean-status.md#complete-frankl-high-girth-frequency-theorem).

## 2026-11-19 — Complete conditional Hadamard border construction

Registered the full fixed-border construction from the original sign rows
and correlation equations on every finite abelian group with an index-four
subgroup. The proof derives normalization, checks the actual core and literal
border, and returns the final matrix. Its size-149 specialization has order
2396. The fourteen baseline patterns are exhaustive with actual row-operation
witnesses. Binary rows satisfying the hypotheses are still required.

The length-1197 multiplier group is also proved to have order dividing 27,
with its invariant quotient of order three constructed. The sharper bound of
nine and finite quotient/no-lift proof remain pending. Four exact passing
source/audit/kernel receipts register 31 modules and 17 required endpoints,
after comparison of all fifty recorded paths. The full merged gate remains
separate. [Scope and receipts](docs/lean-status.md#complete-conditional-fixed-border-construction-and-fourteen-patterns).

## 2026-11-19 — Complete two-difference Motzkin formalization

Registered the exhaustive integer relation-basis classification and its
compact-density trichotomy. Every pair now receives the appropriate zero-rank,
one-relation, or rank-two Hermite formula without an assumed basis. The exact
41-module closure passed strict sources, a 743-theorem standard-axiom audit,
and independent pinned-kernel replay. Two modules and seven required
endpoints join the accepted package after comparison of every recorded hash.

This closes the stated Motzkin note, including its earlier compact and cyclic
equalities, exact evaluator with complexity bounds, and explicit attaining
witnesses. The full merged-package gate remains separate. Li remains last.
[Exact scope and receipt](docs/lean-status.md#complete-two-difference-motzkin-theorem).

## 2026-11-19 — Checked sharp cover, voltage normalization, and border transport

Registered thirteen unchanged proof modules after four exact hosted closures
passed strict source checks, standard-axiom audits, and independent replay
with the unchanged pinned kernel checker. The connected 95-vertex cyclic
cover has attained least power-of-two cycle length 32; its seven-module
closure audited 288 project theorems. Arbitrary seven-voltage normalization
passed in four modules with 131 audited theorems. Finite-border transport
passed in two modules with 66 audited theorems, retaining its finite
certificate identities as inputs. Actual-row normalization passed in two
modules with 14 audited theorems, retaining its compression-shape inputs.

The universal cover theorem remains under issue 18. Deriving the compression
shapes, checking the literal finite certificate, and final Hadamard assembly
remain under issue 17. The actual row-operation scope in issue 26 is complete.
Li remains deferred. [Checked scope and receipts](docs/lean-status.md#complete-sharp-95-vertex-example-and-arbitrary-voltage-normalization).

## 2026-11-19 — Checked cyclic assembly and weight transport

Registered 32 unchanged proof modules after five hosted source, axiom and
stock-kernel gates passed. The accepted packet includes the conditional
all-period span-four assembly, its arbitrary-family transfer, the 48-case
literal weight pilot, exact overlap enumeration, and injective weight
transport with a proved cached evaluator. The concrete graph, rank and full
weight tables remain unfinished. No complete span-four theorem is claimed.
[Scope and receipts](docs/lean-status.md#frankl-cyclic-assembly-and-weight-helpers--19-november-2026).

## 2026-11-19 — Complete fixed-border multiplier and orbit bounds

Registered all 12 border-symmetry proof modules after their exact closure at
`682d0917` passed strict sources, a 216-theorem standard-axiom audit, and the
unchanged pinned kernel replay. The theorem applies to actual sign rows on
every finite abelian group with a subgroup of size 149 and index four.
The full common multiplier group is cyclic of order dividing four, and every
preserving subgroup leaves at least 151 actual sign orbits. Product coordinates
and all transports are proved; no split-domain or normalized-pattern premise
is added. The proof uses raw compressed correlations and does not require
the fourteen-pattern enumeration.
[Receipt](docs/verification/hadamard-border-transfer-682d0917.json) ·
[Checked statement](docs/lean-status.md#complete-fixed-border-multiplier-and-orbit-bounds).

Issue 22 is complete. The separate sequence restrictions and fixed-border
construction remain under issue 17. Issue 23 takes the sharp 95-vertex
Erdős–Gyárfás example in separate candidate sources. Li remains deferred.

## 2026-11-19 — Checked literal mask checker and exact domains

Registered two exact local-mask checker modules after their ten-module hosted
gate passed at `a632fc82`. The gate checked 163 project theorems, 38 required
endpoints, and every module with the stock kernel checker. The checker counts
actual compatible sets and proves its finite domains. Full window data and
the complete span-four theorem remain separate obligations.
[Receipt](docs/verification/frankl-mask-domains-a632fc82.json).

## 2026-11-19 — Checked Vaughan theorem and small cyclic components

Registered the full three-triples Vaughan theorem and every nontrivial cyclic
span-four family on at most six sites. Further period-seven-through-ten
results retain an explicit residual-graph hypothesis. The exact 53-module
closure passed strict sources, a 2,057-theorem axiom audit, checks of all 534
private certificate nodes, and stock kernel replay at `6544adcc`. Its 50 new
proof sources are unchanged. The full span-four theorem remains incomplete.
[Receipt](docs/verification/frankl-fc-packet-6544adcc.json).

## 2026-11-19 — Checked Frankl local certificate semantics

Registered the integer local checker and its equivalent maximal-cover checker.
Their exact five-module closure passed strict source checks, a 66-theorem axiom
audit, and independent kernel replay at `ad07e385`. Both checkers count actual
distinct inside patterns. No finite window weight table is asserted by this
registration. The full merged-package check remains separate.
[Receipt](docs/verification/frankl-maximal-cover-ad07e385.json).

## 2026-11-19 — Complete Hadamard automorphism obstruction

The full signed row/column automorphism theorem at order 2396 passed its
28-module strict-source, 297-theorem standard-axiom, and unchanged pinned-kernel
gate at `fb6b6e06`. The actual automorphism group and all subgroup quotients
have cardinalities not divisible by 479. The independent relative-ideal-norm
proof also passed its 15-module, 164-theorem gate. Sixteen additional proof
source files are registered, bringing this lane to 37; their closures include
the earlier 12-module, 128-theorem cyclotomic descent check at `7098a0e8`.
[Assembly receipt](docs/verification/hadamard-automorphism-assembly-fb6b6e06.json) ·
[Independent proof receipt](docs/verification/hadamard-automorphism-class-alternative-fb6b6e06.json) ·
[Descent receipt](docs/verification/hadamard-automorphism-cyclotomic-7098a0e8.json).
The expanded quadratic-model closure also passed all three gates at `0a1deef7`,
with 16 modules and 157 audited theorems, proving uniqueness of the quadratic
subfield and the exact equal-parity integer-coordinate equivalence.
[Quadratic-model receipt](docs/verification/hadamard-automorphism-quadratic-model-0a1deef7.json).

The separate sequence and border results remain pending. Issue 22 claims the
later fixed-border common multiplier and 151-orbit tail. The status inventory
now explicitly includes the two-insertion and Erdős–Gyárfás cover obligations;
Li remains deferred.

## 2026-11-19 — Checked quadratic field and ideal-class witness

Registered six Hadamard automorphism proof files that construct the actual
quadratic fixed field and a prime above 599 of norm 599 and exact ideal-class
order five. The nine-module closure passed strict sources, a 111-theorem axiom
audit, and independent pinned-kernel replay at `ae7871fc`. The universal
prime-pair alternative and full automorphism assembly remain candidates.
[Receipt](docs/verification/hadamard-automorphism-class-order-ae7871fc.json).

## 2026-11-19 — Checked Hadamard automorphism permutation component

Six proof files now cover explicit diagonal normalization, fixed-point and
cycle counts, cyclic reindexing, integer transport, and the signed automorphism
subgroup. Their seven-module closure passed strict source checks, a 100-theorem
axiom audit, and independent pinned-kernel replay at `e9a9bb45`. The full
obstruction still awaits cyclotomic descent and final assembly.
[Receipt](docs/verification/hadamard-automorphism-permutation-e9a9bb45.json).

## 2026-11-19 — Checked Hadamard automorphism Fourier component

Registered the explicit Fourier, binary overlap, indicator, and determinant
components after strict source checks, a 32-theorem transitive axiom audit,
and independent pinned-kernel replay of their six-module closure at `ee1be6e0`.
The full automorphism and ideal-class statements remain candidates.
[Receipt](docs/verification/hadamard-automorphism-fourier-ee1be6e0.json).

## 2026-11-19 — Checked Hadamard automorphism arithmetic

Registered the arithmetic and integral-basis coefficient component of the
order-479 automorphism obstruction. The five-module candidate closure passed
strict source checks, a 38-theorem transitive axiom audit, and independent
pinned-kernel replay at `56cb125e`, with unchanged sources. The full matrix
and cyclotomic assembly, and the separate ideal-class argument, remain
candidates. [Receipt](docs/verification/hadamard-automorphism-arithmetic-56cb125e.json).

## 2026-11-19 — Complete Frankl large-generator frequency bound

Registered the full all-`k ≥ 15` bound of `657/1000` for every point, with
actual distinct-union counting and the original size, regularity, and linear
intersection hypotheses. Its 16-module closure passed strict sources, a
231-theorem transitive axiom audit, and pinned-kernel replay at `663f7275`.
The high-girth cases `3 ≤ k ≤ 14` and cyclic span-four theorem remain in
progress. [Receipt](docs/frankl-large-hosted-receipt.json).

## 2026-11-19 — Checked Frankl counting foundations

Registered six proof modules after their exact hosted source, transitive axiom,
and pinned-kernel gates passed at `57d699c7`. The packet proves the general
weighted local-certificate implication, the incidence-graph bijection, finite
lopsided conditioning, and the all-parameter numerical criterion. Both full
Frankl results remain incomplete. [Receipt](docs/frankl-foundations-hosted-receipt.json).

## 2026-11-19 — Searchable collection website

Added a GitHub Pages site with search, subject filters, and individual result pages.
Updated result titles, citation metadata, and links to the maintainer's website.
The README now shows the Lean and computational verification workflows.
Reconciled five index flags with the existing partial results in the [Lean status report](docs/lean-status.md).
Mathematical claims and checked proof scopes are unchanged.

## 2026-11-19 — Partial results for three open problems

Published the two Frankl generator results, the two-speed Lonely Runner insertion theorem and a sharp bound for abelian covers in the Erdős–Gyárfás search. Each entry gives its hypotheses and reproducible checks. [Catalogue](CONTENTS.md#partial-results-on-open-problems)

## 2026-11-19 — Formal generating function and cyclic Motzkin formulas

- Registered the exact coefficientwise generating function after its
  14-module strict source check, 496-theorem axiom audit, and kernel replay.
- Registered the all-modulus cyclic formulas, gcd scaling, odd-cycle
  criterion, exact example, and abstract rational-circle attainment after
  the 48-module source check, 812-theorem audit, and kernel replay.
- Added 14 proof modules, giving 482 proof modules and two roots. The empty
  cyclic candidate wrapper is excluded. The full merged gate remains pending.
- Recorded the completed historical full check of `42fff1a2`: 397 proof
  modules, both roots, and 10,843 audited theorems.
- Added separate unregistered gates for Gaussian integration, branch
  coefficients, coefficient rescaling, the actual supported integral limit,
  exhaustive Motzkin relation bases, rational interval witnesses, the fixed
  character window, and the final sharp coefficient theorem.


## 2026-11-19 — Order-479 automorphisms excluded at Hadamard order 2396

Added a cyclotomic obstruction for every candidate matrix, with a second ideal-class proof. The index-four core search also has common multiplier group size at most four. [Scope and proofs](results/hadamard-2396/)

## 2026-11-19 — Partial results at Hadamard order 2396

Added two verified symmetry restrictions, the finite enumeration and a conditional border construction for the open order-2396 existence problem. [Scope and checks](results/hadamard-2396/)

## 2026-11-19 — Relation formulas, Euler correction, and tuple reconstruction

- Registered the Motzkin formulas for stated relation generators and
  finite-relation Borel attainment after a 39-module strict source check,
  729-theorem axiom audit, and independent kernel replay.
- Registered the uniform corrected finite Euler product after its eight-module
  closure passed strict sources, a 122-theorem audit, and independent replay.
- Registered finite tuple/core/tail reconstruction and cumulative cost counting
  from the earlier nine-module, 307-theorem hosted receipt.
- Added 13 checked proof modules, giving 468 proof modules and two roots.
  Full merged verification remains pending. Motzkin basis existence and the
  cyclic/evaluator claims, and the line-size sharp asymptotic, remain open.

## 2026-11-19 — General compact Motzkin equality

- Registered the exact density/continuous-character equality for arbitrary
  compact Hausdorff abelian groups, including zero differences.
- The exact 34-module hosted closure passed strict sources, a 664-theorem axiom
  audit, and independent kernel replay with unchanged source and gate hashes.
- Added 22 checked proof modules to the concurrent 433-module package. The
  combined 455-module hosted gate remains pending; ancillary rank, cyclic,
  evaluation, and complexity claims remain candidates.

## 2026-11-19 — Exact line-size geometry and saddle profile

- Proved the real-plane realizability criterion and exact geometric record
  count for every point count; the 20-module closure passed source, the
  342-theorem ownership audit, and independent kernel replay.
- Proved the exact saddle constant and moment identities from the literal
  integral, with a five-module, 137-theorem audit and kernel replay.
- Registered these checked components and the smooth Euler kernel. The
  exact generating function, corrected product estimate, Fourier bounds,
  and sharp asymptotic remain ongoing work.

## 2026-11-18 (America/Chicago) — Complete four-speed gap

- Proved the all-size four-speed gap and both critical directions below `2/9`,
  including their exact value `1/5` and the four-speed runner lower bound.
- Registered 36 additional modules after exact dependency coverage, an
  1,880-theorem ownership/axiom audit, and independent kernel checks.
- Supplied the previously explicit gap input to the existing five-speed
  plane and cutoff reductions. The bounded five-speed enumeration remains open.

## 2026-11-19 — Complete concrete CUT games and line-size foundations

- Identified both actual recursive CUT games with their proposed sequence at
  every natural pile size. Proved least eventual arithmetic period 12, saltus
  8, and earliest period-12 start 7. Seven compact certificate modules passed
  source checks and the 1,127-declaration ownership audit; all 23 project
  modules in their exact closure passed independent kernel replay.
- Checked seven Erdős 607 foundations, including ordinary-line existence for
  actual finite real-plane point sets, the selected-graph cost identity, and
  the core-to-gap weight equivalence. Geometric sufficiency and the asymptotic
  theorem remain in progress.
- Recorded successful hosted full source, axiom, and kernel verification of
  the 219-module Pham/finite-Motzkin checkpoint `18bf908`.

[Home](README.md) · [Catalogue](CONTENTS.md)

## 2026-11-18 (America/Chicago) — Graph theorem and runner components

- Registered the all-order Graffiti.pc318 theorem and its sharp five-vertex
  example after local and hosted source, axiom, and independent kernel checks.
  The contributed proof remains credited to @JesterInABarrel.
- Registered the consecutive runner family for counts 2 through 14, both
  exceptional eight-speed families, classification within all three stated
  eight-speed product families, and the displayed higher-speed examples.
  Exhaustive higher-speed classifications remain open.
- Registered the exact shifted hyperplane maximum, its attaining point, and
  the upper bound for every orthogonal integer velocity. The statistical and
  counting parts remain open.
- Kept the finite four-speed assembly, KZ arithmetic, reduced-basis geometry,
  Haar/Fourier, and closed-search developments under separate candidate gates.

## 2026-11-19 — Complete rectangle asymptotic and finite plane reduction

- Completed the growing-rectangle theorem for literal real-position tilings,
  uniformly over every `w ≥ h`. The 46-module proof includes the cumulative
  partition estimate and passed the 587-declaration axiom audit and kernel replay.
- Registered the unconditional four-speed cutoff 5,832 and all 64 finite plane
  certificate blocks, covering 122,880 indexed cases. Both hosted matrix runs
  passed source, axiom, and stock kernel checks.
- Registered the plane classification and five-speed cutoff 279,841 with the
  four-speed gap retained as an explicit mathematical input. The exhaustive
  five-speed classification remains in progress.
- Preserved the concurrent completed Pham proof, finite Motzkin theorem, and
  separate unregistered candidate developments.

## 2026-11-19 — Complete Pham proof and finite Motzkin theorem

- Derived both Pham limiting-series identities from actual Bulgarian-solitaire
  cycles and first-entry levels. Proved reduced denominator degrees 5 and 10
  and minimality against every nonzero alternative denominator. The complete
  36-module closure passed source checks, its 1,080-declaration axiom audit,
  and independent kernel replay.
- Completed the Motzkin equality and both attaining witnesses for every finite
  abelian group generated by the two differences. The 12-module closure passed
  independent kernel replay and the 115-declaration Motzkin audit passed.
  The arbitrary compact-group theorem and later algorithmic claims remain open.
- Added exact-closure replay for a selected candidate root. Six protocol tests
  check closure validation, object staging and checker failure propagation.

## 2026-11-19 — Additive Lean integration

- Combined 177 accepted proof modules with both project roots. The merged
  source build and compiled/direct standard-axiom audits passed; the audit
  checked 7,581 theorem declarations.
- Renamed the two independent finite rectangle inputs to `RectangleFinite`
  after detecting a collision with the concurrent shelf-packing proof. Both
  renamed modules passed fresh strict source checks and independent kernel replay.
- Preserved the separate candidate workflows and their unregistered sources.
  The component kernel receipts and the full merged hosted gate are recorded
  separately in the Lean status report.

## 2026-11-18 — Random lonely runners on a fixed hyperplane

- Added the conditional limiting law for Beck and Everett’s statistical question, the finite-subspace description of exceptional velocities, and the unshifted endpoint density for full-support normals.

## 2026-11-18 — Corrected solitaire and combined formalizations

- Completed the corrected L-solitaire theorem in Lean for arbitrary layer sets,
  actual recurrent configurations, and every diverging horizontal scale. The
  finite dynamics, stable-reference classification, analytic bound and limit
  transfer passed source, axiom and independent kernel checks.
- Merged the concurrent density and loneliness foundations, and identified the
  two real distance definitions through a checked pair-sum interface.
- Completed the all-parameter gap-five/gap-seven character formulas and the
  general odd-cycle density theorem. Added finite rectangle packing/counting
  inputs and the exact actual-pile CUT composition theorem.
- Passed the combined source build, the 6,954-theorem standard-axiom audit,
  and independent kernel replay of all 152 accepted proof modules and both
  roots. The replay list is checked against the source-import closure.

## 2026-11-18 — Graffiti.pc Conjecture 318 (credited to @JesterInABarrel)

- Added the all-order proof of Conjecture 318 **credited to [@JesterInABarrel](https://x.com/JesterInABarrel/status/2123233964827812334)**, its stronger total-dominating-pair theorem, and a sharp five-vertex counterexample to lowering the hypothesis by one.
- Checked 419,235 labeled graphs (7,337 satisfying the hypothesis); Lean formalization remains open.

## 2026-11-18 — Complete distance-graph classifications

- Proved the exact gap-five and gap-seven density tables for every positive parameter, including optimal periodic constructions.
- Proved the exact Conjecture 39 discrepancy and infinitely many strict counterexamples.
- Added checked finite rectangle-tiling and Euler-product components; the uniform rectangle asymptotic remains incomplete.
- Added the two-integer-direction plane reduction with the four-speed gap retained as an explicit hypothesis.

## 2026-11-19 — Equality for eleven through fourteen runners

- Classified the primitive equality cases using published binary sieves and an additional integer-direction calculation.

## 2026-11-18 — Complete Haralambis formalization

- Proved the three-difference density theorem and an optimal pair-sum-period construction for every positive triple.
- Proved the general greedy packing bound and the lonely-runner lower bound for at most three speeds.
- Added coordinate coalescence, integer directions, real-span dimension, and rational subspace extensions to the five-speed reduction.
- Recorded the successful hosted Lean build, axiom audit, and kernel replay for the previous density/CUT checkpoint.

## 2026-11-19 — Eight-speed loneliness spectrum

- Added the full classification below 1/8, the three families, and the table of 17 sporadic tuples.

## 2026-11-19 — Seven-speed loneliness spectrum

- Added the full classification below 1/7, the table of 27 sporadic tuples and the corollary on Zhu’s triangle conjecture for six and seven distances.

## 2026-11-18 — Checked density, CUT, and loneliness proofs

- Added complete symmetric four-point packing/covering and nonmixed-gap packing/circle proofs, including common-divisor normalization.
- Added the complete general finite CUT test and completeness of candidate enumeration.
- Added exact real-time loneliness certificates, both critical-family reductions, and the infinite five-speed family.
- Updated the formalization index to distinguish these checked components from the remaining spectrum classification.

## 2026-11-19 — Ten-runner equality classification

- Added the proof that only consecutive primitive speeds attain 1/10 and the verifier for its 28 modular certificates.

## 2026-11-19 — Collection navigation

- Split the landing page, full result catalogue, and verification instructions.
- Added landing pages for results that previously opened as file listings.
- Grouped result files under `results/` and moved the shared Lean package to `lean/`.
- Updated navigation, CI commands, and certificate-generation paths.
- Kept mathematical statements and formalization status unchanged.

## 2026-11-18 — Formalization campaign resumed

- Completed the CUT Family B theorem for the actual recursively defined games,
  including infinite cut sets and the sharp discrepancy bound.
- Added exact reverse-solitaire preimage semantics and uniform arithmetic-tail
  graph recognizers.
- Added a general loneliness maximum theorem and 31 kernel-checked exact values.
- Completed the symmetric four-point packing and covering densities, including
  attainments and sharp interval lengths.
- Continued the corrected solitaire and remaining density/automata proofs.
- Kept Li last and tracked active lanes in issue 1.

This file records collection-level changes, not a complete discovery or priority timeline. For individual additions and revisions, see [the commit history](https://github.com/1337isnot1337/solved-conjectures/commits/main/). Ongoing formalization work is recorded in [the status report](docs/lean-status.md) and [campaign notes](docs/formalization.md).


## 2026-11-19: universal abelian-cover theorem and further exact components

Registered the complete abelian voltage-cover cycle theorem and retained
the sharp 95-vertex example. Also registered the literal finite-border
certificate and the full length-598 order-eleven multiplier obstruction.
Exact source, axiom, and kernel receipts are recorded in `docs/verification`.
The Motzkin evaluator, explicit rational interval witnesses, and narrow
prime-257 minimum-pair-20 support certificate were registered separately.
The remaining collection results are still in progress; Li has not started.

## 2026-11-19: Rational-lattice and Gram components

Registered the eight rectangular/rational-lattice sources and their 50 theorem endpoints after the complete hosted source, owned/private axiom, and stock-kernel gate passed. The six-speed spectrum remains partial; the norm components retain `hfour` and `hplane`.

## 2026-11-19: Conditional two-parameter radius estimate

Registered `Conjectures.LonelinessTwoParameterRadius` and its 6 theorem endpoints after the complete 13-module hosted source, owned/private axiom, and stock-kernel gate passed. The result status remains partial; the retained hypotheses are stated in the status report.

## 2026-11-19: Six-speed norm bounds with the four-speed input discharged

Registered `Conjectures.LonelinessSixSpectrumLatticeNormFourSpeed` and its 3 theorem endpoints after the complete 113-module hosted source, owned/private axiom, and stock-kernel gate passed. The result status remains partial; the retained hypotheses are stated in the status report.

## 2026-11-19: Seven-coordinate implications with the five-speed input discharged

Registered `Conjectures.LonelinessSevenCoordinateFiveSpeed` and its 6 theorem endpoints after the complete 171-module hosted source, owned/private axiom, and stock-kernel gate passed. The result status remains partial; the retained hypotheses are stated in the status report.

## 2026-11-19: Actual rational-lattice quotient index

Registered `Conjectures.LonelinessRationalLatticeQuotient` and its 5 theorem endpoints after the complete 20-module hosted source, selected-declaration axiom audit with raw/private visibility, and stock-kernel gate passed. The result status remains partial; the retained hypotheses are stated in the status report.

## 2026-11-20 — Erdős–Granville–Pomerance–Spiro conjecture

Added a written partial result for arbitrary natural density-zero target sets.
The three input families in the [divisor-sum proof](results/erdos-granville-pomerance-spiro/)
have combined natural density about 53.46%. The computational workflow checks
finite algebra and congruence cases. The full conjecture remains open.

## 2026-11-20 — Horňák–Woźniak conjecture

Added a [proof of both vertex-decomposability conjectures](results/hornak-wozniak/) for tripods and four-arm trees with a one-edge arm. The endpoint argument removes the middle-arm bound and shows that three of the five admissibility tests suffice. The catalogue links the literature check and reproducible allocation checks.

## 2026-11-20 — Sonntag–Teichert conjecture

Added a [proof of connectivity for tournament domination hypergraphs](results/sonntag-teichert/) on their nonisolated vertices. The argument uses minimal closed in-neighbourhoods and also characterizes the disconnected cases for oriented graphs.

