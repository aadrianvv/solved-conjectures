/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Mathlib.Data.Finset.Card
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.List.FinRange
import Mathlib.Algebra.Order.Antidiag.FinsuppEquiv
import Conjectures.ClaessonDefs

/-!
# Exact-depth counts for West's stack-sorting map

Claesson, Dukes and Steingrímsson define `E_{n,k} = W_{n,k} \ W_{n,k-1}` to be the
permutations of length `n` that are sorted by exactly `k` passes through West's
stack.  Their Corollary 2.3 gives the total count for `n - 4` passes, and their
Conjecture 2.4 gives the size of the exact-depth layer `E_{n,n-4}`.

This file formalizes the set-theoretic layer `exactDepthSet`, the equivalence of
the two displayed forms of Conjecture 2.4 *conditional* on Corollary 2.3, and
the stars-and-bars completion factor used in the repository proof.  The main
conditional theorem is algebraic bookkeeping, not a new proof of the conjecture.
-/

namespace Claesson

open LassalleRefinement

/-! ## The exact-depth layer -/

/-- The permutations sorted by at most `d` but not by at most `d - 1` passes.
For `d = 0` this is `W n 0` itself, since there is no previous layer. -/
def exactDepthSet (n d : ℕ) : Finset (Equiv.Perm (Fin n)) :=
  if d = 0 then W n 0 else W n d \ W n (d - 1)

/-- The cardinality of a nonzero exact-depth layer is the difference of the
cumulative counts. -/
theorem card_exactDepthSet {n d : ℕ} (hd : 1 ≤ d) :
    (exactDepthSet n d).card = (W n d).card - (W n (d - 1)).card := by
  unfold exactDepthSet
  split_ifs with h
  · exfalso; omega
  · exact Finset.card_sdiff_of_subset (W_mono (by omega : d - 1 ≤ d))

/-- The cumulative count splits as the previous cumulative count plus the new
exact-depth layer. -/
theorem card_W_eq_card_W_pred_add_exactDepthSet {n d : ℕ} (hd : 1 ≤ d) :
    (W n d).card = (W n (d - 1)).card + (exactDepthSet n d).card := by
  unfold exactDepthSet
  split_ifs with h
  · exfalso; omega
  · rw [add_comm]
    exact (Finset.card_sdiff_add_card_eq_card (W_mono (by omega : d - 1 ≤ d))).symm

/-! ## The identity permutation is the unique permutation sorted by zero passes -/

/-- The word of a permutation is injective. -/
theorem permWord_injective {n : ℕ} : Function.Injective (@permWord n) := by
  intro p q h
  simp only [permWord] at h
  have hf : (fun i : Fin n => (p i).val) = fun i : Fin n => (q i).val :=
    List.ofFn_inj.mp h
  ext i
  exact congrFun hf i

/-- The increasing word is the one-line notation of the identity permutation. -/
theorem identityWord_eq_permWord_one (n : ℕ) :
    identityWord n = permWord (1 : Equiv.Perm (Fin n)) := by
  unfold identityWord permWord
  simp only [Equiv.Perm.one_apply]
  rw [List.ofFn_eq_pmap]
  simp

/-- The only permutation sorted by zero passes is the identity. -/
theorem W_zero (n : ℕ) : W n 0 = {1} := by
  ext p
  rw [mem_W, Finset.mem_singleton]
  simp only [sortedAfter, Nat.zero_add, List.range_one, List.any_cons, List.any_nil,
    Bool.or_false, Function.iterate_zero, id_eq, beq_iff_eq]
  constructor
  · intro h
    exact permWord_injective (h.trans (identityWord_eq_permWord_one n))
  · intro h
    rw [h]
    exact (identityWord_eq_permWord_one n).symm

/-- The zero-pass layer has cardinality one. -/
theorem card_W_zero (n : ℕ) : (W n 0).card = 1 := by
  rw [W_zero, Finset.card_singleton]

/-! ## The exact-depth polynomial and the two conjectural statements -/

/-- The polynomial in the exact-depth form of Conjecture 2.4 of
Claesson–Dukes–Steingrímsson (arXiv:0812.0143v2):
`854 * C(n-8,3) + 5099 * C(n-8,2) + 12545 * C(n-8,1) + 16130`. -/
def exactDepthPolynomial (n : ℕ) : ℤ :=
  854 * (((n - 8).choose 3 : ℕ) : ℤ) +
    5099 * (((n - 8).choose 2 : ℕ) : ℤ) +
    12545 * (((n - 8 : ℕ) : ℤ)) + 16130

/-- The exact-depth form of Conjecture 2.4: for `n ≥ 8`,
`|E_{n,n-4}| = (n-5)! / 10 * (854 C(n-8,3) + ... + 16130)`. -/
def ClaimExact : Prop :=
  ∀ n : ℕ, 8 ≤ n →
    ((exactDepthSet n (n - 4)).card : ℤ) * 10 =
      (Nat.factorial (n - 5) : ℤ) * exactDepthPolynomial n

/-- The quartic in Corollary 2.3 of Claesson–Dukes–Steingrímsson:
`3 n^4 - 18 n^3 - 4 n^2 + 158 n - 192`. -/
def corollaryPolynomial (n : ℤ) : ℤ :=
  3 * n ^ 4 - 18 * n ^ 3 - 4 * n ^ 2 + 158 * n - 192

/-- Corollary 2.3 of Claesson–Dukes–Steingrímsson (arXiv:0812.0143v2): for
`n ≥ 6`, the number of permutations sorted by at most `n - 4` passes is
`(n-4)! (3 n^4 - 18 n^3 - 4 n^2 + 158 n - 192) / 3`.  The division is cleared
by multiplying by `3`. -/
def Corollary23 : Prop :=
  ∀ n : ℕ, 6 ≤ n →
    ((W n (n - 4)).card : ℤ) * 3 =
      (Nat.factorial (n - 4) : ℤ) * corollaryPolynomial (n : ℤ)

/-- Theorem 2.1 of Claesson–Dukes–Steingrímsson (the exact `n - 3` layer):
for `n ≥ 6`,
`|E_{n,n-3}| = (n-4)! / 3 * (47 C(n-6,2) + 194 C(n-6,1) + 297)`.
This is recorded for cross-reference only; its proof is outside this file. -/
def Theorem21 : Prop :=
  ∀ n : ℕ, 6 ≤ n →
    ((exactDepthSet n (n - 3)).card : ℤ) * 3 =
      (Nat.factorial (n - 4) : ℤ) *
        (47 * (((n - 6).choose 2 : ℕ) : ℤ) +
          194 * (((n - 6 : ℕ) : ℤ)) + 297)

/-! ## Clearing the binomial coefficients -/

/-- `6 * C(m,3) = m (m-1) (m-2)` over the integers. -/
theorem six_mul_choose_three_cast (m : ℕ) :
    6 * ((m.choose 3 : ℕ) : ℤ) = (m : ℤ) * ((m : ℤ) - 1) * ((m : ℤ) - 2) := by
  rcases m with _ | _ | m
  · decide
  · decide
  · have hdesc : (m + 2).descFactorial 3 = (m + 2) * (m + 1) * m := by
      rw [show 3 = 2 + 1 by norm_num, Nat.descFactorial_succ,
        show 2 = 1 + 1 by norm_num, Nat.descFactorial_succ, Nat.descFactorial_one]
      have h0 : m + 2 - 2 = m := by omega
      have h1 : m + 2 - 1 = m + 1 := by omega
      rw [h0, h1]
      ring
    have h6 : ((m + 2).descFactorial 3 : ℤ) =
        6 * (((m + 2).choose 3 : ℕ) : ℤ) := by
      rw [Nat.descFactorial_eq_factorial_mul_choose]
      push_cast
      norm_num
    have hcast : ((m + 2).descFactorial 3 : ℤ) =
        ((m + 2 : ℕ) : ℤ) * ((m + 1 : ℕ) : ℤ) * (m : ℤ) := by
      rw [hdesc]
      push_cast
      ring
    rw [← h6, hcast]
    push_cast
    ring

/-- `2 * C(m,2) = m (m-1)` over the integers. -/
theorem two_mul_choose_two_cast (m : ℕ) :
    2 * ((m.choose 2 : ℕ) : ℤ) = (m : ℤ) * ((m : ℤ) - 1) := by
  rcases m with _ | _ | m
  · decide
  · decide
  · have hdesc : (m + 2).descFactorial 2 = (m + 2) * (m + 1) := by
      rw [show 2 = 1 + 1 by norm_num, Nat.descFactorial_succ, Nat.descFactorial_one]
      have h1 : m + 2 - 1 = m + 1 := by omega
      rw [h1]
      ring
    have h2 : ((m + 2).descFactorial 2 : ℤ) =
        2 * (((m + 2).choose 2 : ℕ) : ℤ) := by
      rw [Nat.descFactorial_eq_factorial_mul_choose]
      push_cast
      norm_num
    have hcast : ((m + 2).descFactorial 2 : ℤ) =
        ((m + 2 : ℕ) : ℤ) * ((m + 1 : ℕ) : ℤ) := by
      rw [hdesc]
      push_cast
      ring
    rw [← h2, hcast]
    push_cast
    ring

/-- For `n ≥ 8`, six times the exact-depth polynomial is the integer polynomial
`854 m^3 + 12735 m^2 + 61681 m + 96780`, where `m = n - 8`. -/
theorem six_mul_exactDepthPolynomial (n : ℕ) (hn : 8 ≤ n) :
    6 * exactDepthPolynomial n =
      854 * ((n : ℤ) - 8) ^ 3 + 12735 * ((n : ℤ) - 8) ^ 2 +
        61681 * ((n : ℤ) - 8) + 96780 := by
  have h3 := six_mul_choose_three_cast (n - 8)
  have h2 := two_mul_choose_two_cast (n - 8)
  have hm : ((n - 8 : ℕ) : ℤ) = (n : ℤ) - 8 := by
    exact Nat.cast_sub hn
  unfold exactDepthPolynomial
  rw [hm] at h3 h2 ⊢
  have h3' : 6 * (854 * (((n - 8).choose 3 : ℕ) : ℤ)) =
      854 * (((n : ℤ) - 8) * (((n : ℤ) - 8) - 1) * (((n : ℤ) - 8) - 2)) := by
    rw [show 6 * (854 * (((n - 8).choose 3 : ℕ) : ℤ)) =
        854 * (6 * (((n - 8).choose 3 : ℕ) : ℤ)) by ring, h3]
  have h2' : 6 * (5099 * (((n - 8).choose 2 : ℕ) : ℤ)) =
      5099 * (3 * (((n : ℤ) - 8) * (((n : ℤ) - 8) - 1))) := by
    rw [show 6 * (5099 * (((n - 8).choose 2 : ℕ) : ℤ)) =
        5099 * (3 * (2 * (((n - 8).choose 2 : ℕ) : ℤ))) by ring, h2]
  calc
    6 * (854 * (((n - 8).choose 3 : ℕ) : ℤ) +
          5099 * (((n - 8).choose 2 : ℕ) : ℤ) +
          12545 * ((n : ℤ) - 8) + 16130)
        = 6 * (854 * (((n - 8).choose 3 : ℕ) : ℤ)) +
            6 * (5099 * (((n - 8).choose 2 : ℕ) : ℤ)) +
            6 * (12545 * ((n : ℤ) - 8)) + 6 * 16130 := by ring
    _ = 854 * (((n : ℤ) - 8) * (((n : ℤ) - 8) - 1) * (((n : ℤ) - 8) - 2)) +
          5099 * (3 * (((n : ℤ) - 8) * (((n : ℤ) - 8) - 1))) +
          6 * (12545 * ((n : ℤ) - 8)) + 6 * 16130 := by rw [h3', h2']
    _ = 854 * ((n : ℤ) - 8) ^ 3 + 12735 * ((n : ℤ) - 8) ^ 2 +
          61681 * ((n : ℤ) - 8) + 96780 := by ring

/-- The polynomial relation behind the equivalence of the two forms of
Conjecture 2.4:
`20 (n-4) (3n^4 - 18n^3 - 4n^2 + 158n - 192)
   = P(n) + 6 E(n)`. -/
theorem twenty_mul_corollaryPolynomial (n : ℕ) (hn : 8 ≤ n) :
    20 * (((n : ℤ) - 4) * corollaryPolynomial (n : ℤ)) =
      nearTopPolynomial (n : ℤ) + 6 * exactDepthPolynomial n := by
  have h6 := six_mul_exactDepthPolynomial n hn
  unfold corollaryPolynomial nearTopPolynomial
  rw [h6]
  ring

/-! ## The conditional equivalence of the two forms of Conjecture 2.4 -/

/-- The factorial step `(n-4)! = (n-4) (n-5)!` for `n ≥ 8`. -/
theorem factorial_four_eq (n : ℕ) (hn : 8 ≤ n) :
    (Nat.factorial (n - 4) : ℤ) = ((n : ℤ) - 4) * (Nat.factorial (n - 5) : ℤ) := by
  have hnat : Nat.factorial (n - 4) = (n - 4) * Nat.factorial (n - 5) := by
    rw [show n - 4 = (n - 5) + 1 by omega, Nat.factorial_succ]
  calc
    (Nat.factorial (n - 4) : ℤ) =
        (((n - 4) * Nat.factorial (n - 5) : ℕ) : ℤ) := by rw [hnat]
    _ = ((n - 4 : ℕ) : ℤ) * (Nat.factorial (n - 5) : ℤ) := by push_cast; ring
    _ = ((n : ℤ) - 4) * (Nat.factorial (n - 5) : ℤ) := by
      rw [Nat.cast_sub (by omega : (4 : ℕ) ≤ n)]
      norm_num

/-- Under Corollary 2.3, the cumulative count for `n - 4` passes is governed by
`P(n) + 6 E(n)`, where `P` is the near-top polynomial of the conjecture and `E`
is the exact-depth polynomial. -/
theorem sixty_mul_card_W_eq (h23 : Corollary23) (n : ℕ) (hn : 8 ≤ n) :
    ((W n (n - 4)).card : ℤ) * 60 =
      (Nat.factorial (n - 5) : ℤ) *
        (nearTopPolynomial (n : ℤ) + 6 * exactDepthPolynomial n) := by
  have h23n := h23 n (by omega)
  have hfac := factorial_four_eq n hn
  have hpoly := twenty_mul_corollaryPolynomial n hn
  calc
    ((W n (n - 4)).card : ℤ) * 60 =
        (((W n (n - 4)).card : ℤ) * 3) * 20 := by ring
    _ = ((Nat.factorial (n - 4) : ℤ) * corollaryPolynomial (n : ℤ)) * 20 := by
      rw [h23n]
    _ = ((((n : ℤ) - 4) * (Nat.factorial (n - 5) : ℤ)) *
          corollaryPolynomial (n : ℤ)) * 20 := by
      rw [hfac]
    _ = (Nat.factorial (n - 5) : ℤ) *
          (20 * (((n : ℤ) - 4) * corollaryPolynomial (n : ℤ))) := by ring
    _ = (Nat.factorial (n - 5) : ℤ) *
          (nearTopPolynomial (n : ℤ) + 6 * exactDepthPolynomial n) := by
      rw [hpoly]

/-- The cumulative count for `n - 4` passes splits into the `n - 5` layer and
the new `n - 4` exact-depth layer, for `n ≥ 8`. -/
theorem card_W_four_split (n : ℕ) (hn : 8 ≤ n) :
    ((W n (n - 4)).card : ℤ) =
      ((W n (n - 5)).card : ℤ) +
        ((exactDepthSet n (n - 4)).card : ℤ) := by
  have hsum := card_W_eq_card_W_pred_add_exactDepthSet
    (n := n) (d := n - 4) (by omega : 1 ≤ n - 4)
  have hpred : n - 4 - 1 = n - 5 := by omega
  rw [hpred] at hsum
  exact_mod_cast hsum

/-- **Conditional equivalence of the two forms of Conjecture 2.4.**  Assuming
Corollary 2.3 of Claesson–Dukes–Steingrímsson, the near-top form `Claim` and the
exact-depth form `ClaimExact` are equivalent.  This is purely algebraic
bookkeeping: the two statements differ by subtracting the `n - 5` layer from
the cumulative `n - 4` count. -/
theorem claim_iff_claimExact_of_corollary23 (h23 : Corollary23) :
    Claim ↔ ClaimExact := by
  constructor
  · intro hClaim n hn
    have h60 := sixty_mul_card_W_eq h23 n hn
    have hsplit := card_W_four_split n hn
    have hA := hClaim n hn
    have hB60 : ((exactDepthSet n (n - 4)).card : ℤ) * 60 =
        (Nat.factorial (n - 5) : ℤ) * (6 * exactDepthPolynomial n) := by
      rw [hsplit] at h60
      nlinarith
    have hB10 : ((exactDepthSet n (n - 4)).card : ℤ) * 10 =
        (Nat.factorial (n - 5) : ℤ) * exactDepthPolynomial n := by
      have h6 : 6 * (((exactDepthSet n (n - 4)).card : ℤ) * 10) =
          6 * ((Nat.factorial (n - 5) : ℤ) * exactDepthPolynomial n) := by
        calc
          6 * (((exactDepthSet n (n - 4)).card : ℤ) * 10) =
              ((exactDepthSet n (n - 4)).card : ℤ) * 60 := by ring
          _ = (Nat.factorial (n - 5) : ℤ) * (6 * exactDepthPolynomial n) := hB60
          _ = 6 * ((Nat.factorial (n - 5) : ℤ) * exactDepthPolynomial n) := by ring
      exact mul_left_cancel₀ (by norm_num : (6 : ℤ) ≠ 0) h6
    exact hB10
  · intro hExact n hn
    have h60 := sixty_mul_card_W_eq h23 n hn
    have hsplit := card_W_four_split n hn
    have hB := hExact n hn
    have hA60 : ((W n (n - 5)).card : ℤ) * 60 =
        (Nat.factorial (n - 5) : ℤ) * nearTopPolynomial (n : ℤ) := by
      rw [hsplit] at h60
      nlinarith
    exact hA60

/-! ## Stars and bars: the completion factor -/

/-- A weak composition of `m` into `u` parts, modelled as a finitely supported
function on `Fin u` with total sum `m`. -/
def weakCompositions (m u : ℕ) : Finset (Fin u →₀ ℕ) :=
  (Finset.univ : Finset (Fin u)).finsuppAntidiag m

/-- The stars-and-bars count: the number of weak compositions of `m` into `u`
nonnegative parts is `C(m + u - 1, u - 1)`. -/
theorem card_weakCompositions (m u : ℕ) (hu : 1 ≤ u) :
    (weakCompositions m u).card = (m + u - 1).choose (u - 1) := by
  unfold weakCompositions
  rw [Finset.card_finsuppAntidiag_nat_eq_choose]
  simp only [Finset.card_univ, Fintype.card_fin]
  have h1 : u + m - 1 = m + u - 1 := by omega
  rw [h1]
  exact (Nat.choose_symm_of_eq_add (by omega : m + u - 1 = (u - 1) + m)).symm

/-- The binomial coefficient in the completion factor is a multichoose. -/
theorem choose_eq_multichoose (m u : ℕ) (hu : 1 ≤ u) :
    (m + u - 1).choose (u - 1) = Nat.multichoose (m + 1) (u - 1) := by
  rw [Nat.multichoose_eq]
  congr 1
  omega

/-- The weak-composition count in multichoose form. -/
theorem card_weakCompositions_multichoose (m u : ℕ) (hu : 1 ≤ u) :
    (weakCompositions m u).card = Nat.multichoose (m + 1) (u - 1) := by
  rw [card_weakCompositions m u hu, choose_eq_multichoose m u hu]

/-- Choosing `j` of `N` labelled values and fixing their relative order leaves
`N! / j!` ways to arrange the remaining values relative to that order. -/
theorem choose_mul_factorial_eq_factorial_div (N j : ℕ) (hj : j ≤ N) :
    N.choose j * (N - j).factorial = N.factorial / j.factorial := by
  apply Nat.eq_div_of_mul_eq_right (Nat.factorial_ne_zero j)
  rw [← Nat.choose_mul_factorial_mul_factorial hj]
  ring

/-- **The completion factor of the repository proof.**  With `N` generic values,
`j` constrained ones, and `u ≥ 1` unconstrained ordered gaps, the number of
completions is
`C(N,j) (N-j)! C(N-j+u-1, u-1) = N!/j! C(N-j+u-1, u-1)`. -/
theorem completion_factor (N j u : ℕ) (_hu : 1 ≤ u) (hj : j ≤ N) :
    (N.choose j) * (N - j).factorial *
        (N - j + u - 1).choose (u - 1) =
      N.factorial / j.factorial * (N - j + u - 1).choose (u - 1) := by
  rw [choose_mul_factorial_eq_factorial_div N j hj]

/-- The completion factor with the gap count expressed as a multichoose. -/
theorem completion_factor_multichoose (N j u : ℕ) (hu : 1 ≤ u) (hj : j ≤ N) :
    (N.choose j) * (N - j).factorial *
        Nat.multichoose (N - j + 1) (u - 1) =
      N.factorial / j.factorial * (N - j + u - 1).choose (u - 1) := by
  rw [← choose_eq_multichoose (N - j) u hu]
  exact completion_factor N j u hu hj

/-! ## Numerical checks at `n = 8, 9, 10` -/

/-- The exact-depth polynomial at `n = 8`. -/
theorem exactDepthPolynomial_eight : exactDepthPolynomial 8 = 16130 := by
  have h := six_mul_exactDepthPolynomial 8 (by norm_num)
  norm_num at h
  omega

/-- The exact-depth polynomial at `n = 9`. -/
theorem exactDepthPolynomial_nine : exactDepthPolynomial 9 = 28675 := by
  have h := six_mul_exactDepthPolynomial 9 (by norm_num)
  norm_num at h
  omega

/-- The exact-depth polynomial at `n = 10`. -/
theorem exactDepthPolynomial_ten : exactDepthPolynomial 10 = 46319 := by
  have h := six_mul_exactDepthPolynomial 10 (by norm_num)
  norm_num at h
  omega

/-- Corollary 2.3 at `n = 8`: the total number sorted by `4` passes is
`24 * 3888 / 3 = 31104`. -/
theorem corollary23_total_eight :
    (3 : ℤ) * 31104 = (Nat.factorial (8 - 4) : ℤ) * corollaryPolynomial 8 := by
  unfold corollaryPolynomial
  norm_num

/-- Corollary 2.3 at `n = 9`: the total number sorted by `5` passes is
`120 * 7467 / 3 = 298680`. -/
theorem corollary23_total_nine :
    (3 : ℤ) * 298680 = (Nat.factorial (9 - 4) : ℤ) * corollaryPolynomial 9 := by
  unfold corollaryPolynomial
  norm_num

/-- Corollary 2.3 at `n = 10`: the total number sorted by `6` passes is
`720 * 12988 / 3 = 3117120`. -/
theorem corollary23_total_ten :
    (3 : ℤ) * 3117120 = (Nat.factorial (10 - 4) : ℤ) * corollaryPolynomial 10 := by
  unfold corollaryPolynomial
  norm_num

/-- Numerical check at `n = 8`.  Direct stack sorting gives `21426`
permutations sorted by `3` passes, and Corollary 2.3 gives `31104` sorted by
`4` passes, so the exact layer has `9678` elements.  The formula predicts
`3! * 16130 / 10 = 9678`. -/
theorem exactDepth_formula_eight :
    (10 * (31104 - 21426) : ℤ) =
      (Nat.factorial (8 - 5) : ℤ) * exactDepthPolynomial 8 := by
  rw [exactDepthPolynomial_eight]
  norm_num

/-- Numerical check at `n = 9`.  Direct stack sorting gives `229860`
permutations sorted by `4` passes, and Corollary 2.3 gives `298680` sorted by
`5` passes, so the exact layer has `68820` elements.  The formula predicts
`4! * 28675 / 10 = 68820`. -/
theorem exactDepth_formula_nine :
    (10 * (298680 - 229860) : ℤ) =
      (Nat.factorial (9 - 5) : ℤ) * exactDepthPolynomial 9 := by
  rw [exactDepthPolynomial_nine]
  norm_num

/-- Numerical check at `n = 10`.  Direct stack sorting gives `2561292`
permutations sorted by `5` passes, and Corollary 2.3 gives `3117120` sorted by
`6` passes, so the exact layer has `555828` elements.  The formula predicts
`5! * 46319 / 10 = 555828`. -/
theorem exactDepth_formula_ten :
    (10 * (3117120 - 2561292) : ℤ) =
      (Nat.factorial (10 - 5) : ℤ) * exactDepthPolynomial 10 := by
  rw [exactDepthPolynomial_ten]
  norm_num

end Claesson
