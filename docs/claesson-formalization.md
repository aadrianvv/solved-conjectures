# Claesson–Dukes–Steingrímsson: Lean formalization checkpoint

This page records the partial Lean 4 formalization of Conjecture 2.4 of
Anders Claesson, Mark Dukes and Einar Steingrímsson, *Permutations sortable by
n - 4 passes through a stack* ([arXiv:0812.0143v2](https://arxiv.org/abs/0812.0143v2)),
whose proof is published in
[`results/claesson-dukes-steingrimsson-stack-sorting`](../results/claesson-dukes-steingrimsson-stack-sorting/PROOF.md).

The formalization lives in the shared `lean` package under
`Conjectures.Claesson*`.  It is **partial**: the statement and the arithmetic
reduction are checked, but the marked-order inclusion–exclusion identity that
evaluates the finite `11!` enumeration is stated as an explicit hypothesis, not
proved.  The result therefore remains `⬜` in the ranked catalogue.

## Formalized statement

`Conjectures/ClaessonDefs.lean` defines West's iterated stack sort on
one-line permutations of `Fin n` and the set

```lean
def W (n t : ℕ) : Finset (Equiv.Perm (Fin n))
```

of permutations sorted by at most `t` passes.  The conjecture is the
cleared-denominator integer statement

```lean
def Claim : Prop :=
  ∀ n : ℕ, 8 ≤ n →
    ((W n (n - 5)).card : ℤ) * 60 =
      (Nat.factorial (n - 5) : ℤ) * nearTopPolynomial (n : ℤ)
```

with `nearTopPolynomial n = 60 n^5 - 600 n^4 + 506 n^3 + 11241 n^2 - 38369 n + 34236`.
The complement form `ClaimBad` uses
`badPolynomial n = 1594 n^3 - 14241 n^2 + 39809 n - 34236`.

The checked modules are:

| Module | Content |
| --- | --- |
| `Conjectures.ClaessonDefs` | `W`, `sortedAfter`, `Claim`, `ClaimBad`, monotonicity |
| `Conjectures.ClaessonStack` | pre-flush map, threshold commutation, sorting depth |
| `Conjectures.ClaessonArithmetic` | complement cubic, ten-row coefficient table, exact `n ≥ 11` identity |
| `Conjectures.ClaessonExactDepth` | exact-depth layer, Corollary 2.3 equivalence, stars and bars |
| `Conjectures.ClaessonMain` | assembly of the conditional theorem |
| `Conjectures.ClaessonSanity` | small kernel checks (`W 3 1 = 5`, `W 4 1 = 14`, …) |

## What is proved

- `Claesson.claim_iff_claimBad`: the near-top and complement forms are
  equivalent.  The proof uses the factorial identity
  `n! = (n - 5)! n (n - 1) (n - 2) (n - 3) (n - 4)` and the polynomial identity
  `nearTopPolynomial n + badPolynomial n = 60 n (n - 1) (n - 2) (n - 3) (n - 4)`.
- `Claesson.markedBad_identity`: for every `n ≥ 11`, the ten-row marked count
  from `coefficients.csv` equals
  `(n - 5)! (1594 n^3 - 14241 n^2 + 39809 n - 34236) / 60` over `ℚ`.
- `Claesson.claim_iff_claimExact_of_corollary23`: assuming the paper's
  Corollary 2.3,
  `|W n (n-4)| = (n-4)! (3 n^4 - 18 n^3 - 4 n^2 + 158 n - 192) / 3`,
  the near-top form `Claim` and the exact-depth form `ClaimExact`,
  `|E_{n,n-4}| = (n-5)! (854 C(n-8,3) + 5099 C(n-8,2) + 12545 (n-8) + 16130) / 10`,
  are equivalent.
- `Claesson.card_weakCompositions`: the number of weak compositions of `m`
  into `u ≥ 1` parts is `C(m + u - 1, u - 1)`; this is the completion factor
  used by the paper.
- `Claesson.W_zero`: the only permutation sorted by zero passes is the identity.
- `Claesson.westStackSort_filter`: deleting all values below a threshold
  commutes with one stack-sorting pass.
- `Claesson.westStackSort_eq_preflush_append_finalStack`: the pre-flush output
  and final stack decomposition.
- `Claesson.sortingDepth_eq_succ` and `Claesson.excess`: the pre-flush depth
  statistic decreases by exactly one per pass on nonempty words.

## The remaining hypothesis

`Conjectures/ClaessonMain.lean` defines

```lean
def MarkedCountIdentity : Prop :=
  (∀ n : ℕ, 11 ≤ n →
    (((Finset.univ \ W n (n - 5)).card : ℚ) = markedBad n)) ∧
  (Finset.univ \ W 8 3).card = 18894 ∧
  (Finset.univ \ W 9 4).card = 133020 ∧
  (Finset.univ \ W 10 5).card = 1067508
```

and proves

```lean
theorem claim_of_markedCountIdentity (h : MarkedCountIdentity) : Claim
```

The first conjunct is the marked-order argument of `counter.cs`: eleven marked
labels, at most six constrained generic entries, ten free gaps, and
inclusion–exclusion over the possible witness values.  The three small counts
are the direct stack-sorting values `n! - 21426`, `n! - 229860` and
`n! - 2561292`; they are not kernel-enumerated in Lean because reducing
`Finset.univ` over `Equiv.Perm (Fin 10)` is not feasible.

The following are also not formalized and are recorded as open dependencies:

1. The marked-order inclusion–exclusion identity itself.
2. The filtered-prefix principle of Zhang in the iterated form
   `s^k(w)` sorted ↔ `p^k(X_b(w)) = []` for every value `b`, and its
   witness-bound corollary.  The pre-flush map and the statistics are defined,
   but the equivalence is not proved.
3. Corollary 2.3 of the paper.  It is used as an explicit hypothesis for the
   exact-depth equivalence only.

## Verification

```powershell
cd lean
$env:PATH = "C:\Users\vazqu\.elan\bin;$env:PATH"
lake build Conjectures.ClaessonMain
lake env lean Conjectures\ClaessonSanity.lean
```

The build of `Conjectures.ClaessonMain` succeeds under the package's pinned
Lean 4.35.0 toolchain and the `-j1 -M4500` library settings.  An axiom audit of
the following declarations reports only `propext`, `Classical.choice` and
`Quot.sound`:

```text
Claesson.claim_of_markedCountIdentity
Claesson.claimExact_of_claim_and_corollary23
Claesson.claim_and_claimExact_of_markedCountIdentity
Claesson.claim_iff_claimBad
Claesson.markedBad_identity
Claesson.claim_iff_claimExact_of_corollary23
Claesson.W_zero
Claesson.six_mul_exactDepthPolynomial
Claesson.card_weakCompositions
Claesson.westStackSort_filter
Claesson.sortingDepth_eq_succ
Claesson.westStackSort_eq_preflush_append_finalStack
```

The full repository audit (`scripts/verify_lean.sh`) and the full root
`Conjectures` build were not run for this checkpoint; only the six Claesson
modules were built and audited locally.  The status label therefore remains
`⬜` until the marked-order identity and the filtered-prefix principle are
formalized and the full replay is run.
