/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Conjectures.ClaessonArithmetic
import Conjectures.ClaessonExactDepth
import Conjectures.ClaessonStack

/-!
# Assembly of the Claesson–Dukes–Steingrímsson formalization

This module ties together the verified pieces of the formalization of
Conjecture 2.4 of Claesson, Dukes and Steingrímsson,
*Permutations Sortable by n − 4 Passes Through a Stack* (arXiv:0812.0143v2):

* `Conjectures.ClaessonStack`: the pre-flush map, deletion commutation and the
  sorting-depth statistics;
* `Conjectures.ClaessonArithmetic`: the complement cubic, the ten-row
  coefficient table from `coefficients.csv`, and the exact polynomial identity
  for every `n ≥ 11`;
* `Conjectures.ClaessonExactDepth`: the exact-depth layer, the stars-and-bars
  completion factor, and the algebraic equivalence of the two displayed forms
  of Conjecture 2.4 assuming the paper's Corollary 2.3.

The one mathematical input not formalized here is the marked-order
inclusion–exclusion identity turning the finite `11!` enumeration into the
closed form `markedBad`.  It is stated explicitly as `MarkedCountIdentity`.
The three base counts `n = 8, 9, 10` are also kept there, because kernel
enumeration over `10!` permutations is not feasible.  Nothing in this file
assumes the conjecture it proves.
-/

namespace Claesson

open LassalleRefinement

/-- The finite part of the repository proof that has not been formalized:
the marked-order inclusion–exclusion count equals the number of permutations
that need more than `n - 5` passes, together with the three directly
enumerated base counts.

The first conjunct is the content of `counter.cs`: eleven marked labels, at
most six constrained generic entries, ten free gaps, and inclusion–exclusion
over the witness values.  The other three are reproduced by `check-base.js`
and by the direct stack simulator in the repository. -/
def MarkedCountIdentity : Prop :=
  (∀ n : ℕ, 11 ≤ n →
    (((Finset.univ \ W n (n - 5)).card : ℚ) = markedBad n)) ∧
  (Finset.univ \ W 8 3).card = 18894 ∧
  (Finset.univ \ W 9 4).card = 133020 ∧
  (Finset.univ \ W 10 5).card = 1067508

/-- The bad count at `n = 8, 9, 10` in the cleared-denominator form used by
`ClaimBad`, obtained from the directly enumerated values. -/
theorem bad_count_small
    (h8 : (Finset.univ \ W 8 3).card = 18894)
    (h9 : (Finset.univ \ W 9 4).card = 133020)
    (h10 : (Finset.univ \ W 10 5).card = 1067508) :
    ((Finset.univ \ W 8 3).card : ℤ) * 60 =
        (Nat.factorial (8 - 5) : ℤ) * badPolynomial (8 : ℤ) ∧
    ((Finset.univ \ W 9 4).card : ℤ) * 60 =
        (Nat.factorial (9 - 5) : ℤ) * badPolynomial (9 : ℤ) ∧
    ((Finset.univ \ W 10 5).card : ℤ) * 60 =
        (Nat.factorial (10 - 5) : ℤ) * badPolynomial (10 : ℤ) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [h8]; norm_num [badPolynomial, Nat.factorial]
  · rw [h9]; norm_num [badPolynomial, Nat.factorial]
  · rw [h10]; norm_num [badPolynomial, Nat.factorial]

/-- **Main assembly.**  The marked-order identity implies Conjecture 2.4 in
the complement form `ClaimBad`, hence in the near-top form `Claim`.

The proof is exactly the arithmetic step of the repository proof: for
`n ≥ 11`, replace the bad count by the ten-row marked count, use the exact
`markedBad` polynomial identity, and clear the factor `60`; the three small
lengths are checked from the direct counts. -/
theorem claim_of_markedCountIdentity (h : MarkedCountIdentity) : Claim := by
  obtain ⟨hmarked, h8, h9, h10⟩ := h
  refine claim_iff_claimBad.mpr ?_
  intro n hn
  by_cases hn11 : 11 ≤ n
  · have hq : ((Finset.univ \ W n (n - 5)).card : ℚ) =
        (Nat.factorial (n - 5) : ℚ) * (badPolynomial (n : ℤ) : ℚ) / 60 := by
      rw [hmarked n hn11, markedBad_identity hn11]
    have hq60 : (((Finset.univ \ W n (n - 5)).card : ℚ) * 60) =
        (Nat.factorial (n - 5) : ℚ) * (badPolynomial (n : ℤ) : ℚ) := by
      rw [hq]
      field_simp
    have hbad : ((Finset.univ \ W n (n - 5)).card : ℤ) * 60 =
        (Nat.factorial (n - 5) : ℤ) * badPolynomial (n : ℤ) := by
      apply Int.cast_injective (α := ℚ)
      push_cast
      exact hq60
    exact hbad
  · have hn' : n = 8 ∨ n = 9 ∨ n = 10 := by omega
    rcases hn' with rfl | rfl | rfl
    · exact (bad_count_small h8 h9 h10).1
    · exact (bad_count_small h8 h9 h10).2.1
    · exact (bad_count_small h8 h9 h10).2.2

/-- The exact-depth form of Conjecture 2.4 follows from the near-top form and
the paper's Corollary 2.3. -/
theorem claimExact_of_claim_and_corollary23
    (h23 : Corollary23) (h : Claim) : ClaimExact :=
  (claim_iff_claimExact_of_corollary23 h23).mp h

/-- Conversely, the exact-depth form plus Corollary 2.3 gives the near-top
form. -/
theorem claim_of_claimExact_and_corollary23
    (h23 : Corollary23) (h : ClaimExact) : Claim :=
  (claim_iff_claimExact_of_corollary23 h23).mpr h

/-- Both displayed forms of Conjecture 2.4, starting from the marked-order
identity and Corollary 2.3. -/
theorem claim_and_claimExact_of_markedCountIdentity
    (h23 : Corollary23) (h : MarkedCountIdentity) : Claim ∧ ClaimExact :=
  let hc := claim_of_markedCountIdentity h
  ⟨hc, claimExact_of_claim_and_corollary23 h23 hc⟩

end Claesson
