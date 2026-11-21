# Solved conjectures in combinatorics and number theory

Mathematical proofs, counterexamples, and partial results in combinatorics, number theory, graph theory, and discrete geometry. Includes Lean 4 formalizations and reproducible verification code.

These notes are unrefereed. Computational checks and Lean verification are distinct from peer review and priority claims.

Curated by [Cinna Davis](https://1337isnot1337.github.io/) and GPT-6.2 Astra. External contributions have separate result-level credit.

[Search the collection](https://1337isnot1337.github.io/solved-conjectures/) · [Full catalogue](CONTENTS.md) · [Verification](docs/verification.md) · [Lean status](docs/lean-status.md) · [History](HISTORY.md)

## Results

| Problem | Verification |
| :--- | :---: |
| [Haralambis’s three-difference conjecture](results/haralambis-three-differences/) | ✅ |
| [Németh–Seberry–Shu conjecture ★](results/nemeth-seberry-shu/) | ⬜ |
| [Natalchenko–Sagdeev nonmixed-gap packing](results/nonmixed-gap-packing/) | ✅ |
| [Liu–Zhu packing and Natalchenko–Sagdeev covering](results/symmetric-four-point-density/) | ✅ |
| [Sonntag–Teichert conjecture](results/sonntag-teichert/) | ⬜ |
| [Horňák–Woźniak conjecture](results/hornak-wozniak/) | ⬜ |
| [Eight-speed Loneliness Spectrum Conjecture](results/eight-speed-spectrum/) | 🟢 |
| [Seven-speed Amended Loneliness Spectrum Conjecture](results/seven-speed-spectrum/) | 🟢 |
| [Karp–Vishnyakova–Zhang's Bessel-ratio unimodality conjecture](results/kvz-bessel-unimodality/) | ⬜ |
| [Ferreira–Simon's Wright log-concavity conjecture](results/ferreira-simon-wright/) | ⬜ |
| [Karp–Vishnyakova–Zhang's gamma-quotient conjecture](results/kvz-gamma-quotient/) | ⬜ |
| [Alexandersson's Fuss–Catalan conjecture](results/alexandersson-fuss-catalan/) | ⬜ |
| [Sagan–Swanson conjecture](results/sagan-swanson-normality/) | ⬜ |
| [Bernardi–Morales's delta-process conjecture](results/bernardi-morales-delta/) | ⬜ |
| [Gilmore's crossing–nesting conjecture](results/gilmore-crossing-nesting/) | ⬜ |
| [Two-difference Motzkin density](results/two-difference-motzkin/) | ✅ |
| [Six-speed Loneliness Spectrum Conjecture](results/six-speed-spectrum/) | 🟢 |
| [Five-speed Loneliness Spectrum Conjecture](results/five-speed-spectrum/) | 🟢 |
| [Erdős Problem 607: line-size sets](results/erdos-607-line-sizes/) | ✅ |
| [Random lonely runners on a fixed hyperplane](results/loneliness-on-a-hyperplane/) | ✅ |
| [Distance graphs with three missing differences](results/distance-graph-densities/) | ✅ |
| [Oravcová–Soták conjecture for five to eight distances](results/oravcova-sotak/) | ⬜ |
| [Chow's conjecture](results/chow-conjecture/) | ⬜ |
| [Rectangle partition asymptotics](results/rectangle-partition-asymptotics/) | ✅ |
| [Generalized Bulgarian solitaire limit shapes](results/l-solitaire-limit-shapes/) | ✅ |
| [Graffiti.pc Conjecture 318](results/graffiti-pc-318/) | ✅ |
| [Li's chromatic symmetric function signs](results/li-coefficient-sign/) | ✅ |
| [CUT Family B: nim-sequence threshold](results/cut-family-b/) | ✅ |
| [Eleven through fourteen lonely runners, all equality cases](results/tight-eleven-to-fourteen/) | 🟢 |
| [Zhang's Question 8.4: deletion values of the lonely runner](results/zhang-deletion-values/) | ⬜ |
| [Ten lonely runners, unique equality case](results/tight-nine-speeds/) | 🟢 |
| [Nine lonely runners, unique equality case](results/tight-eight-speeds/) | 🟢 |
| [Eight lonely runners, all equality cases](results/tight-seven-speeds/) | 🟢 |
| [Tight six-speed sets and seven-coordinate critical subtori](results/tight-six-speeds/) | 🟢 |
| [CUT arithmetic periodicity with a preperiod](results/cut-arithmetic-periodicity/) | ✅ |
| [Batista's Egyptian fractions](results/batista-egyptian-fractions/) | ✅ |
| [Pham's Bulgarian solitaire denominator degree](results/pham-denominator-degree/) | ✅ |
| [Spivey's three-player War](results/spivey-multiplayer-war/) | ✅ |
| [Baricz–Pogány's asymptotic-coefficient positivity conjecture](results/baricz-pogany-coefficients/) | ⬜ |
| [Perron root of permanental compounds](results/perron-root-permanental-compounds/) | ⬜ |
| [Pula–Song–Wanless conjecture](results/pula-song-wanless/) | ⬜ |
| [Currie's conjecture on complexity 2n+1 and critical exponent](results/currie-conjecture-19/) | ⬜ |
| [Malek's conjecture](results/malek-subpermanent/) | ⬜ |

Entries are ranked approximately by relative mathematical significance, weighing generality, connection to established problems, and the scope of the result. This editorial order does not imply independent verification or priority.

**Verification key**

- ✅ Fully Lean-verified.
- 🟢 Partially Lean-verified, with a computer-assisted proof.
- 🟡 Partially Lean-verified.
- ⬜ No computer-assisted proof or Lean verification yet.
- ★ Outside confirmation: an independent external review is documented at the result level. This is separate from Lean verification and is not journal peer review.

For the 🟢 Lonely Runner results, the written proofs reduce the classification to finitely many cases. Exact computations exhaust those cases, with some results drawing on archived searches from cited papers. Completing the Lean proofs requires formalizing the remaining reductions and cited bounds and checking the remaining search certificates in Lean. The [verification guide](docs/verification.md#computational-checks) gives the replay commands, and the [Lean status report](docs/lean-status.md) gives the remaining steps for each result.

## Partial results on open problems

This section is ordered by the significance of the partial contributions, not the prominence of the unsolved parent conjectures.

- [Frankl’s union-closed sets conjecture](results/frankl-generator-families/). A four-position generator theorem and a frequency bound for regular, high-girth incidence graphs. Both all-point frequency bounds are fully Lean-verified, including the high-girth theorem for every uniform generator size at least three. The cyclic span-four formalization remains incomplete. [Checked scope](docs/lean-status.md#complete-frankl-high-girth-frequency-theorem).
- [Lonely Runner Conjecture](results/lonely-runner-two-insertions/). Two arbitrary speeds can be adjoined to every Goddyn–Wong simultaneous acceleration. The full prescribed-interval theorem, acceleration bridge, unbounded and finite cases, common-dilation value bound, and three-insertion obstruction are Lean-verified. [Checked scope](docs/lean-status.md#complete-unrestricted-two-speed-insertion-theorem).
- [Erdős–Sauer conjecture](docs/erdos-sauer-research.md). The hypergraph decomposition bound holds asymptotically for each fixed uniformity.
- [Bollobás–Erdős–Tuza conjecture](docs/bollobas-erdos-tuza-research.md). A lower bound of order $\sqrt{n\log n}$ for maximal independent set transversals, and a constant upper bound at bounded modular width.
- [Erdős–Granville–Pomerance–Spiro conjecture](results/erdos-granville-pomerance-spiro/). For every natural density-zero target set, the preimage conclusion holds on a fixed family of inputs of natural density approximately 53.46%. The full conjecture remains open.
- [Erdős–Gyárfás power-of-two cycles](results/erdos-gyarfas-abelian-covers/). A sharp cycle-length bound for abelian covers of a singly subdivided tetrahedron. The universal voltage-cover theorem, arbitrary-voltage normalization, and sharp connected 95-vertex cyclic example are Lean-verified. [Checked scope](docs/lean-status.md#complete-sharp-95-vertex-example-and-arbitrary-voltage-normalization).
- [Erdős essential-component conjecture](docs/erdos-essential-component-research.md). An equivalent expansion problem modulo powers of two, with quantitative density gains on all sufficiently long prefixes.
- [Hadamard existence, order 2396](results/hadamard-2396/). The automorphism obstruction, fixed-border symmetry bounds, complete conditional fixed-border construction with all fourteen patterns, and length-598 order-eleven obstruction are Lean-verified. The actual two-row Hadamard construction from a Legendre pair and its invariant quotient transport are also checked. The order-nine subgroup and orbit statements are also checked. The length-1197 multiplier order is proved to divide 27; the sharper bound of nine and finite quotient/no-lift certificates remain pending. Existence stays open. [Checked scope](docs/lean-status.md#complete-conditional-fixed-border-construction-and-fourteen-patterns).
- [Erdős–Oler conjecture](docs/erdos-oler-research.md). The conjectured lower bound holds for packings on any unit-separated lattice, and triangular lattice packings with one site removed are locally rigid.

## Layout

- `results/`: individual results, proofs, and computational checks.
- `lean/`: shared formalizations and pinned dependencies.
- `docs/`: verification instructions and formalization status.
- `scripts/`: repository-wide validation tools.

## How to cite

GitHub's **Cite this repository** control reads [`CITATION.cff`](CITATION.cff).
The repository-level authors are Cinna Davis and GPT-6.2 Astra (an AI model), in that order.
Credit the [Graffiti.pc 318 result](results/graffiti-pc-318/) and its proof to [@JesterInABarrel](https://x.com/JesterInABarrel/status/2123233964827812334), who contributed them.
Credit the [Zhang deletion-values result](results/zhang-deletion-values/) and the [Oravcová–Soták five-to-eight-distance result](results/oravcova-sotak/) to [@aadrianvv](https://github.com/aadrianvv), who contributed their proofs and verification packages in [PR #143](https://github.com/1337isnot1337/solved-conjectures/pull/143) and [PR #144](https://github.com/1337isnot1337/solved-conjectures/pull/144). The latter result is conditional on the repository's spectrum classifications and does not settle the unrestricted conjecture.

Suggested BibTeX for the repository:

```bibtex
@misc{davis2026solvedconjectures,
  author       = {Cinna Davis and {GPT-6.2 Astra}},
  title        = {Solved conjectures in combinatorics and number theory},
  year         = {2026},
  howpublished = {GitHub repository},
  url          = {https://github.com/1337isnot1337/solved-conjectures},
  note         = {Unrefereed mathematical notes and reproducible verification code}
}
```

For an individual result, cite its credited author, result title, directory, and commit or release.
Cite the original conjecture's publication separately (see [the catalogue](CONTENTS.md#primary-sources)).
These notes have no DOI or peer-reviewed publication.

## Verification

The badges show the current workflow status on `main`. The Lean workflow checks the registered package, transitive axioms, and kernel replay. The computational workflow runs the result verifiers.

The [verification guide](docs/verification.md) gives commands, compiler requirements, and the scope of each check.

## Precise scope

See [the scope notes](CONTENTS.md#precise-scope) and each result's proof for hypotheses and limitations.

## Primary sources

Sources are linked in the [catalogue](CONTENTS.md#primary-sources) and individual proofs.

