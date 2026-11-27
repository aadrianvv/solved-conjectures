/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Mathlib.Data.Int.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Conjectures.LassalleStackSorting

/-!
# The Claesson–Dukes–Steingrímsson near-top stack-sorting count

This file fixes the definitions and the exact statement of Conjecture 2.4 of
Claesson, Dukes and Steingrímsson, *Permutations Sortable by n − 4 Passes
Through a Stack*, for West's deterministic stack-sorting map.

The counting statement is the proposition `Claesson.Claim`.  Its proof is
developed in the companion modules `Conjectures.ClaessonBasic` and
`Conjectures.ClaessonMain`.
-/

namespace Claesson

open LassalleRefinement

/-- The increasing word `0, 1, ..., n - 1`.  We use zero-based labels so that
words are exactly the one-line notation of permutations of `Fin n`. -/
def identityWord (n : ℕ) : List ℕ := List.range n

/-- A permutation is sorted after at most `t` passes if some iterate
`s^k`, `k ≤ t`, is the identity word.  This is Boolean-valued so that small
instances can be evaluated by kernel reduction. -/
def sortedAfter {n : ℕ} (t : ℕ) (p : Equiv.Perm (Fin n)) : Bool :=
  (List.range (t + 1)).any fun k =>
    ((westStackSort^[k]) (permWord p)) == identityWord n

/-- The set `W_{n,t}` of permutations of length `n` sorted by at most `t`
passes through West's stack. -/
def W (n t : ℕ) : Finset (Equiv.Perm (Fin n)) :=
  Finset.univ.filter fun p => sortedAfter t p = true

/-- Membership in `W` in terms of the iterated map. -/
theorem mem_W {n t : ℕ} {p : Equiv.Perm (Fin n)} :
    p ∈ W n t ↔ sortedAfter t p = true := by
  simp [W]

/-- The set `W` is monotone in the number of permitted passes. -/
theorem W_mono {n : ℕ} {t t' : ℕ} (h : t ≤ t') : W n t ⊆ W n t' := by
  intro p hp
  rw [mem_W] at hp ⊢
  simp only [sortedAfter, List.any_eq_true] at hp ⊢
  obtain ⟨k, hk, hkp⟩ := hp
  exact ⟨k, List.mem_range.mpr (by have := List.mem_range.mp hk; omega), hkp⟩

/-- The polynomial in the Claesson–Dukes–Steingrímsson formula. -/
def nearTopPolynomial (n : ℤ) : ℤ :=
  60 * n ^ 5 - 600 * n ^ 4 + 506 * n ^ 3 + 11241 * n ^ 2 - 38369 * n + 34236

/-- The exact integer form of the conjecture, with the division by `60`
cleared.  For `n ≥ 8` the factor `(n - 5)!` is divisible by `60` precisely
when the displayed product is. -/
def Claim : Prop :=
  ∀ n : ℕ, 8 ≤ n →
    ((W n (n - 5)).card : ℤ) * 60 =
      (Nat.factorial (n - 5) : ℤ) * nearTopPolynomial (n : ℤ)

/-- The complementary count of permutations that are **not** sorted by
`n - 5` passes, in the closed form derived from the conjecture. -/
def badPolynomial (n : ℤ) : ℤ :=
  1594 * n ^ 3 - 14241 * n ^ 2 + 39809 * n - 34236

/-- The complement form of the conjecture: the bad count is
`(n - 5)! / 60` times a cubic. -/
def ClaimBad : Prop :=
  ∀ n : ℕ, 8 ≤ n →
    ((Finset.univ \ W n (n - 5)).card : ℤ) * 60 =
      (Nat.factorial (n - 5) : ℤ) * badPolynomial (n : ℤ)

end Claesson
