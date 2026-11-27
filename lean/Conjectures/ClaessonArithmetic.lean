/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Conjectures.ClaessonDefs
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Fintype.Perm
import Mathlib.Data.Finset.Card
import Mathlib.Data.Rat.Defs
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Intervals
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Push
import Mathlib.Tactic.IntervalCases

/-!
# Exact arithmetic for the Claesson–Dukes–Steingrímsson count

This module isolates the purely arithmetic part of the repository proof of
Conjecture 2.4 of Claesson, Dukes and Steingrímsson.

* `factorial_eq_factorial_sub_mul` is the identity
  `n! = (n-5)! * n * (n-1) * (n-2) * (n-3) * (n-4)` for `n ≥ 5`.
* `claim_iff_claimBad` shows that the cleared-denominator form `Claim` of the
  conjecture is equivalent to its complement form `ClaimBad`, using
  `Finset.card_sdiff_of_subset` and `Fintype.card_perm`.
* `markedBad` is the exact ten-term count of `verify.py`, and
  `markedBad_identity` proves that for every `n ≥ 11` it equals
  `(n-5)! * (1594 n^3 - 14241 n^2 + 39809 n - 34236) / 60`.
* `badPolynomial_values_small` records the boundary values at `n = 8, 9, 10`.

The polynomial comparison is performed after factoring out `(n-11)!`: the
binomial coefficient `(N - j + u - 1).choose (u - 1)`, `N = n - 11`, is
rewritten with `Nat.ascFactorial_eq_factorial_mul_choose'` as
`(N - j + 1).ascFactorial (u - 1) / (u - 1)!`, and the ascending factorial is
expanded into an explicit product.  What remains is a polynomial identity in
`n` over `ℚ`, discharged by `ring`.
-/

namespace Claesson

open Finset
open scoped BigOperators

/-! ## The factorial identity -/

/-- For `n ≥ 5`, `n! = (n-5)! * n * (n-1) * (n-2) * (n-3) * (n-4)`. -/
theorem factorial_eq_factorial_sub_mul (n : ℕ) (hn : 5 ≤ n) :
    (Nat.factorial n : ℤ) =
      (Nat.factorial (n - 5) : ℤ) *
        ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4)) := by
  have hd : n.descFactorial 5 = (n - 4) * ((n - 3) * ((n - 2) * ((n - 1) * n))) := by
    simp [Nat.descFactorial]
  have hdZ : (n.descFactorial 5 : ℤ) =
      (n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4) := by
    rw [hd]
    push_cast
    rw [Nat.cast_sub (by omega : 4 ≤ n), Nat.cast_sub (by omega : 3 ≤ n),
      Nat.cast_sub (by omega : 2 ≤ n), Nat.cast_sub (by omega : 1 ≤ n)]
    ring
  have h := Nat.factorial_mul_descFactorial (n := n) (k := 5) hn
  have hZ : ((Nat.factorial (n - 5) : ℤ) * (n.descFactorial 5 : ℤ)) =
      (Nat.factorial n : ℤ) := by
    exact_mod_cast h
  rw [← hZ, hdZ]

/-- For `n ≥ 11`, `(n-5)! = (n-11)! * (n-10) * (n-9) * (n-8) * (n-7) * (n-6) * (n-5)`. -/
theorem factorial_eq_factorial_sub_mul_six (n : ℕ) (hn : 11 ≤ n) :
    (Nat.factorial (n - 5) : ℚ) =
      (Nat.factorial (n - 11) : ℚ) *
        (((n : ℚ) - 10) * ((n : ℚ) - 9) * ((n : ℚ) - 8) *
         ((n : ℚ) - 7) * ((n : ℚ) - 6) * ((n : ℚ) - 5)) := by
  have hd : (n - 5).descFactorial 6 =
      (n - 10) * (n - 9) * (n - 8) * (n - 7) * (n - 6) * (n - 5) := by
    simp [Nat.descFactorial]
    rw [show n - 5 - 5 = n - 10 by omega, show n - 5 - 4 = n - 9 by omega,
      show n - 5 - 3 = n - 8 by omega, show n - 5 - 2 = n - 7 by omega,
      show n - 5 - 1 = n - 6 by omega]
    ring
  have h := Nat.factorial_mul_descFactorial (n := n - 5) (k := 6) (by omega : 6 ≤ n - 5)
  have hsub : (n - 5) - 6 = n - 11 := by omega
  rw [hsub] at h
  have hQ : ((Nat.factorial (n - 11) : ℚ) * ((n - 5).descFactorial 6 : ℚ)) =
      (Nat.factorial (n - 5) : ℚ) := by
    exact_mod_cast h
  rw [← hQ, hd]
  push_cast
  rw [Nat.cast_sub (by omega : 10 ≤ n), Nat.cast_sub (by omega : 9 ≤ n),
    Nat.cast_sub (by omega : 8 ≤ n), Nat.cast_sub (by omega : 7 ≤ n),
    Nat.cast_sub (by omega : 6 ≤ n), Nat.cast_sub (by omega : 5 ≤ n)]
  ring

/-! ## The complement form of the claim -/

/-- The algebraic heart of the complement computation:
`nearTopPolynomial n + badPolynomial n = 60 n (n-1) (n-2) (n-3) (n-4)`. -/
theorem nearTopPolynomial_add_badPolynomial (n : ℤ) :
    nearTopPolynomial n + badPolynomial n =
      60 * (n * (n - 1) * (n - 2) * (n - 3) * (n - 4)) := by
  simp only [nearTopPolynomial, badPolynomial]
  ring

/-- The cleared-denominator conjecture is equivalent to its complement form. -/
theorem claim_iff_claimBad : Claim ↔ ClaimBad := by
  have hpoly : ∀ n : ℕ,
      nearTopPolynomial (n : ℤ) + badPolynomial (n : ℤ) =
        60 * ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4)) :=
    fun n => nearTopPolynomial_add_badPolynomial (n : ℤ)
  constructor
  · intro h n hn
    have hW := h n hn
    have hle : (W n (n - 5)).card ≤ Nat.factorial n := by
      calc
        (W n (n - 5)).card ≤ Finset.univ.card :=
          Finset.card_le_card (Finset.subset_univ _)
        _ = Fintype.card (Equiv.Perm (Fin n)) := Finset.card_univ
        _ = Nat.factorial (Fintype.card (Fin n)) := Fintype.card_perm
        _ = Nat.factorial n := by rw [Fintype.card_fin]
    have hcard : ((Finset.univ \ W n (n - 5)).card : ℤ) =
        (Nat.factorial n : ℤ) - ((W n (n - 5)).card : ℤ) := by
      rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ,
        Fintype.card_perm, Fintype.card_fin, Nat.cast_sub hle]
    have hfacZ := factorial_eq_factorial_sub_mul n (by omega : 5 ≤ n)
    calc
      ((Finset.univ \ W n (n - 5)).card : ℤ) * 60
          = ((Nat.factorial n : ℤ) - ((W n (n - 5)).card : ℤ)) * 60 := by rw [hcard]
      _ = ((Nat.factorial (n - 5) : ℤ) *
              ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4))) * 60
            - ((W n (n - 5)).card : ℤ) * 60 := by rw [hfacZ]; ring
      _ = ((Nat.factorial (n - 5) : ℤ) *
              ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4))) * 60
            - (Nat.factorial (n - 5) : ℤ) * nearTopPolynomial (n : ℤ) := by rw [hW]
      _ = (Nat.factorial (n - 5) : ℤ) * badPolynomial (n : ℤ) := by
            have hb : badPolynomial (n : ℤ) =
                60 * ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4))
                  - nearTopPolynomial (n : ℤ) := by
              linarith [hpoly n]
            rw [hb]; ring
  · intro h n hn
    have hB := h n hn
    have hle : (W n (n - 5)).card ≤ Nat.factorial n := by
      calc
        (W n (n - 5)).card ≤ Finset.univ.card :=
          Finset.card_le_card (Finset.subset_univ _)
        _ = Fintype.card (Equiv.Perm (Fin n)) := Finset.card_univ
        _ = Nat.factorial (Fintype.card (Fin n)) := Fintype.card_perm
        _ = Nat.factorial n := by rw [Fintype.card_fin]
    have hcard : ((Finset.univ \ W n (n - 5)).card : ℤ) =
        (Nat.factorial n : ℤ) - ((W n (n - 5)).card : ℤ) := by
      rw [Finset.card_sdiff_of_subset (Finset.subset_univ _), Finset.card_univ,
        Fintype.card_perm, Fintype.card_fin, Nat.cast_sub hle]
    have hWcard : ((W n (n - 5)).card : ℤ) =
        (Nat.factorial n : ℤ) - ((Finset.univ \ W n (n - 5)).card : ℤ) := by
      rw [hcard]; ring
    have hfacZ := factorial_eq_factorial_sub_mul n (by omega : 5 ≤ n)
    calc
      ((W n (n - 5)).card : ℤ) * 60
          = ((Nat.factorial n : ℤ) - ((Finset.univ \ W n (n - 5)).card : ℤ)) * 60 := by
            rw [hWcard]
      _ = ((Nat.factorial (n - 5) : ℤ) *
              ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4))) * 60
            - ((Finset.univ \ W n (n - 5)).card : ℤ) * 60 := by rw [hfacZ]; ring
      _ = ((Nat.factorial (n - 5) : ℤ) *
              ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4))) * 60
            - (Nat.factorial (n - 5) : ℤ) * badPolynomial (n : ℤ) := by rw [hB]
      _ = (Nat.factorial (n - 5) : ℤ) * nearTopPolynomial (n : ℤ) := by
            have hn' : nearTopPolynomial (n : ℤ) =
                60 * ((n : ℤ) * ((n : ℤ) - 1) * ((n : ℤ) - 2) * ((n : ℤ) - 3) * ((n : ℤ) - 4))
                  - badPolynomial (n : ℤ) := by
              linarith [hpoly n]
            rw [hn']; ring

/-! ## The ten-term marked count -/

/-- The binomial polynomial
`(N - j + 1) (N - j + 2) ⋯ (N - j + u - 1) / (u - 1)!`. -/
def binomialPolynomial (j u : ℕ) (N : ℚ) : ℚ :=
  (∏ i ∈ Finset.range (u - 1), (N - (j : ℚ) + (i : ℚ) + 1)) /
    (Nat.factorial (u - 1) : ℚ)

/-- The ascending factorial, cast to `ℚ`, is the explicit product
`a (a+1) ⋯ (a+k-1)`. -/
theorem ascFactorial_cast_eq_prod (a k : ℕ) :
    (Nat.ascFactorial a k : ℚ) = ∏ i ∈ Finset.range k, ((a : ℚ) + (i : ℚ)) := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [Nat.ascFactorial_succ, Finset.prod_range_succ]
      push_cast
      rw [ih]
      ring

/-- `∏_{i<k} (i+1) = k!`, cast to `ℚ`. -/
theorem prod_range_succ_cast_eq_factorial (k : ℕ) :
    (∏ i ∈ Finset.range k, ((i : ℚ) + 1)) = (Nat.factorial k : ℚ) := by
  induction k with
  | zero => simp
  | succ k ih =>
      rw [Finset.prod_range_succ, ih, Nat.factorial_succ]
      push_cast
      ring

/-- Casting the binomial coefficient `(N - j + u - 1).choose (u - 1)` to `ℚ`
gives the explicit binomial polynomial. -/
theorem choose_cast_eq_binomialPolynomial {N j u : ℕ} (hj : j ≤ N) (hu : 1 ≤ u) :
    (Nat.choose (N - j + u - 1) (u - 1) : ℚ) = binomialPolynomial j u (N : ℚ) := by
  have hfac : (Nat.factorial (u - 1) : ℚ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero (u - 1)
  have hidx : (N - j + 1) + (u - 1) - 1 = N - j + u - 1 := by omega
  have hkey : (Nat.choose (N - j + u - 1) (u - 1) : ℚ) =
      (Nat.ascFactorial (N - j + 1) (u - 1) : ℚ) / (Nat.factorial (u - 1) : ℚ) := by
    have h := Nat.ascFactorial_eq_factorial_mul_choose' (N - j + 1) (u - 1)
    have hcast : (Nat.ascFactorial (N - j + 1) (u - 1) : ℚ) =
        (Nat.factorial (u - 1) : ℚ) *
          (Nat.choose ((N - j + 1) + (u - 1) - 1) (u - 1) : ℚ) := by
      exact_mod_cast h
    rw [hidx] at hcast
    rw [eq_div_iff hfac, hcast]
    ring
  rw [hkey, binomialPolynomial, ascFactorial_cast_eq_prod]
  have hNcast : ((N - j + 1 : ℕ) : ℚ) = (N : ℚ) - (j : ℚ) + 1 := by
    rw [Nat.cast_add, Nat.cast_one, Nat.cast_sub hj]
  rw [hNcast]
  congr 1
  apply Finset.prod_congr rfl
  intro i _
  ring

/-- One term `a * (N! / j!) * (N - j + u - 1).choose (u - 1)` of the marked
count, with `N = n - 11`.  The term is zero when `N < j`. -/
def markedTerm (n j u a : ℕ) : ℚ :=
  if j ≤ n - 11 then
    (a : ℚ) * ((Nat.factorial (n - 11) : ℚ) / (Nat.factorial j : ℚ)) *
      (Nat.choose (n - 11 - j + u - 1) (u - 1) : ℚ)
  else 0

/-- The exact ten-term marked bad count of the repository verifier, with
`N = n - 11`.  For `n < 11` it is set to zero. -/
def markedBad (n : ℕ) : ℚ :=
  if 11 ≤ n then
    markedTerm n 0 7 1653120 + markedTerm n 0 8 2676240 +
      markedTerm n 0 9 2973600 + markedTerm n 0 10 2322432 +
      markedTerm n 1 8 4808160 + markedTerm n 1 9 5443200 +
      markedTerm n 1 10 3144960 + markedTerm n 2 9 9192960 +
      markedTerm n 2 10 5443200 + markedTerm n 3 10 8709120
  else 0

/-- The ten-row table of `coefficients.csv`, with the common factor `N!`
removed. -/
def markedBadPolynomial (N : ℚ) : ℚ :=
  (1653120 : ℚ) / (Nat.factorial 0 : ℚ) * binomialPolynomial 0 7 N +
    (2676240 : ℚ) / (Nat.factorial 0 : ℚ) * binomialPolynomial 0 8 N +
    (2973600 : ℚ) / (Nat.factorial 0 : ℚ) * binomialPolynomial 0 9 N +
    (2322432 : ℚ) / (Nat.factorial 0 : ℚ) * binomialPolynomial 0 10 N +
    (4808160 : ℚ) / (Nat.factorial 1 : ℚ) * binomialPolynomial 1 8 N +
    (5443200 : ℚ) / (Nat.factorial 1 : ℚ) * binomialPolynomial 1 9 N +
    (3144960 : ℚ) / (Nat.factorial 1 : ℚ) * binomialPolynomial 1 10 N +
    (9192960 : ℚ) / (Nat.factorial 2 : ℚ) * binomialPolynomial 2 9 N +
    (5443200 : ℚ) / (Nat.factorial 2 : ℚ) * binomialPolynomial 2 10 N +
    (8709120 : ℚ) / (Nat.factorial 3 : ℚ) * binomialPolynomial 3 10 N

/-- A term of `markedBad` equals `N!` times the corresponding term of
`markedBadPolynomial`, as soon as `j ≤ N` and `u ≥ 1`. -/
theorem markedTerm_eq {n j u a : ℕ} (hn : 11 ≤ n) (hj : j ≤ n - 11) (hu : 1 ≤ u) :
    markedTerm n j u a =
      (Nat.factorial (n - 11) : ℚ) *
        ((a : ℚ) / (Nat.factorial j : ℚ) * binomialPolynomial j u ((n : ℚ) - 11)) := by
  unfold markedTerm
  rw [ite_eq_left hj, choose_cast_eq_binomialPolynomial hj hu]
  have hcast : ((n - 11 : ℕ) : ℚ) = (n : ℚ) - 11 := by
    rw [Nat.cast_sub hn]; norm_num
  rw [hcast]
  have hfacj : (Nat.factorial j : ℚ) ≠ 0 := by
    exact_mod_cast Nat.factorial_ne_zero j
  field_simp

/-- For `n ≥ 14` all ten table rows satisfy `j ≤ n - 11`, so the marked count
factors as `(n-11)!` times the ten-row polynomial. -/
theorem markedBad_eq_factorial_mul (n : ℕ) (hn : 14 ≤ n) :
    markedBad n = (Nat.factorial (n - 11) : ℚ) * markedBadPolynomial ((n : ℚ) - 11) := by
  have h0 : (0 : ℕ) ≤ n - 11 := by omega
  have h1 : (1 : ℕ) ≤ n - 11 := by omega
  have h2 : (2 : ℕ) ≤ n - 11 := by omega
  have h3 : (3 : ℕ) ≤ n - 11 := by omega
  rw [markedBad, ite_eq_left (by omega : 11 ≤ n)]
  simp only [markedBadPolynomial]
  rw [markedTerm_eq (n := n) (j := 0) (u := 7) (a := 1653120) (by omega) h0 (by norm_num),
    markedTerm_eq (n := n) (j := 0) (u := 8) (a := 2676240) (by omega) h0 (by norm_num),
    markedTerm_eq (n := n) (j := 0) (u := 9) (a := 2973600) (by omega) h0 (by norm_num),
    markedTerm_eq (n := n) (j := 0) (u := 10) (a := 2322432) (by omega) h0 (by norm_num),
    markedTerm_eq (n := n) (j := 1) (u := 8) (a := 4808160) (by omega) h1 (by norm_num),
    markedTerm_eq (n := n) (j := 1) (u := 9) (a := 5443200) (by omega) h1 (by norm_num),
    markedTerm_eq (n := n) (j := 1) (u := 10) (a := 3144960) (by omega) h1 (by norm_num),
    markedTerm_eq (n := n) (j := 2) (u := 9) (a := 9192960) (by omega) h2 (by norm_num),
    markedTerm_eq (n := n) (j := 2) (u := 10) (a := 5443200) (by omega) h2 (by norm_num),
    markedTerm_eq (n := n) (j := 3) (u := 10) (a := 8709120) (by omega) h3 (by norm_num)]
  ring

/-- The algebraic heart: the ten-row polynomial is the cubic
`1594 n^3 - 14241 n^2 + 39809 n - 34236` over `60`, multiplied by the six
factors `(n-10) ⋯ (n-5)`. -/
theorem markedBadPolynomial_identity (n : ℕ) :
    markedBadPolynomial ((n : ℚ) - 11) =
      ((badPolynomial (n : ℤ) : ℚ)) / 60 *
        (((n : ℚ) - 10) * ((n : ℚ) - 9) * ((n : ℚ) - 8) *
         ((n : ℚ) - 7) * ((n : ℚ) - 6) * ((n : ℚ) - 5)) := by
  simp only [markedBadPolynomial, binomialPolynomial, badPolynomial, Finset.prod_range_succ]
  push_cast
  ring

/-- The exact identity for the ten-term marked bad count, for every `n ≥ 11`. -/
theorem markedBad_identity {n : ℕ} (hn : 11 ≤ n) :
    markedBad n = (Nat.factorial (n - 5) : ℚ) * (badPolynomial (n : ℤ) : ℚ) / 60 := by
  by_cases h14 : 14 ≤ n
  · rw [markedBad_eq_factorial_mul n h14, markedBadPolynomial_identity n,
      factorial_eq_factorial_sub_mul_six n hn]
    ring
  · interval_cases n <;>
      norm_num [markedBad, markedTerm, badPolynomial, Nat.factorial, Nat.choose]

/-- The same identity written with the displayed cubic. -/
theorem markedBad_identity_explicit {n : ℕ} (hn : 11 ≤ n) :
    markedBad n = (Nat.factorial (n - 5) : ℚ) *
      (1594 * (n : ℚ) ^ 3 - 14241 * (n : ℚ) ^ 2 + 39809 * (n : ℚ) - 34236) / 60 := by
  rw [markedBad_identity hn]
  simp only [badPolynomial]
  push_cast
  ring

/-! ## Boundary values -/

/-- The cubic part at the three small lengths gives the directly enumerated
bad counts `8! - 21426`, `9! - 229860`, `10! - 2561292`. -/
theorem badPolynomial_values_small :
    (Nat.factorial (8 - 5) : ℚ) * (badPolynomial (8 : ℤ) : ℚ) / 60 = 18894 ∧
    (Nat.factorial (9 - 5) : ℚ) * (badPolynomial (9 : ℤ) : ℚ) / 60 = 133020 ∧
    (Nat.factorial (10 - 5) : ℚ) * (badPolynomial (10 : ℤ) : ℚ) / 60 = 1067508 := by
  norm_num [badPolynomial, Nat.factorial]

/-- The boundary values expressed as `n!` minus the directly enumerated
sortable counts. -/
theorem badPolynomial_values_small' :
    (18894 : ℚ) = (Nat.factorial 8 : ℚ) - 21426 ∧
    (133020 : ℚ) = (Nat.factorial 9 : ℚ) - 229860 ∧
    (1067508 : ℚ) = (Nat.factorial 10 : ℚ) - 2561292 := by
  norm_num [Nat.factorial]

/-- The identity specializes to the seven boundary lengths `11 ≤ n ≤ 17`. -/
theorem markedBad_values_11_to_17 :
    markedBad 11 = (Nat.factorial 6 : ℚ) * (badPolynomial (11 : ℤ) : ℚ) / 60 ∧
    markedBad 12 = (Nat.factorial 7 : ℚ) * (badPolynomial (12 : ℤ) : ℚ) / 60 ∧
    markedBad 13 = (Nat.factorial 8 : ℚ) * (badPolynomial (13 : ℤ) : ℚ) / 60 ∧
    markedBad 14 = (Nat.factorial 9 : ℚ) * (badPolynomial (14 : ℤ) : ℚ) / 60 ∧
    markedBad 15 = (Nat.factorial 10 : ℚ) * (badPolynomial (15 : ℤ) : ℚ) / 60 ∧
    markedBad 16 = (Nat.factorial 11 : ℚ) * (badPolynomial (16 : ℤ) : ℚ) / 60 ∧
    markedBad 17 = (Nat.factorial 12 : ℚ) * (badPolynomial (17 : ℤ) : ℚ) / 60 := by
  refine ⟨markedBad_identity (by norm_num), markedBad_identity (by norm_num),
    markedBad_identity (by norm_num), markedBad_identity (by norm_num),
    markedBad_identity (by norm_num), markedBad_identity (by norm_num),
    markedBad_identity (by norm_num)⟩

end Claesson
