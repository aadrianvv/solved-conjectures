/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Conjectures.ClaessonFiltered

/-!
# The bounded-budget witness for the Claesson–Dukes–Steingrímsson argument

This file formalizes the witness reduction used in the proof of the
Claesson–Dukes–Steingrímsson stack-sorting conjecture.  The paper works with
the one-based labels `1, …, n`; here words use the zero-based labels
`0, …, n - 1`, so every inequality is shifted down by one.

For a word `w` and a value `b`, the paper writes `t_b` for the number of
entries larger than `b` that occur after `b`.  In our notation this is
`afterCount b w`.  The paper's `X_b` is `prefixAbove b w`, and the paper's
`e(X_b)` is `excess (prefixAbove b w)`.

The main results of the file are:

* `prefixAbove_length_add_afterCount`: the count identity
  `|X_b| + t_b = n - 1 - b` for a permutation word of `List.range n`;
* `sortingDepth_gt_of_preflush_ne_nil` (and its order form
  `sortingDepth_ge_of_preflush_ne_nil`): a nonempty `k`-th pre-flush iterate
  forces `k < sortingDepth`;
* `exists_witness_of_not_mem_W`: if `p` is not sorted by `n - 5` passes, then
  some letter `b` of its one-line notation satisfies
  `b + t_b + e(X_b) ≤ 3`.

The last bound is the paper's `b + t_b + e(X_b) ≤ 4` after the zero-based
shift; in particular `b ∈ {0, 1, 2, 3}`.
-/

namespace Claesson

open LassalleRefinement

/-! ## The number of larger entries after a letter -/

/-- The number of entries larger than `b` that occur strictly after `b` in
`w`.  This is the paper's `t_b`. -/
def afterCount (b : ℕ) (w : List ℕ) : ℕ :=
  ((w.drop (w.idxOf b + 1)).filter (fun x => b < x)).length

/-! ## The count identity -/

/-- The prefix cut out by `takeWhile (· ≠ b)` is the same as the prefix of
length `idxOf b`. -/
lemma takeWhile_ne_eq_take_idxOf (b : ℕ) (w : List ℕ) :
    w.takeWhile (fun x => x ≠ b) = w.take (w.idxOf b) := by
  induction w with
  | nil => simp
  | cons a as ih =>
    by_cases ha : a = b
    · subst ha
      simp
    · simp only [ne_eq, decide_not] at ih ⊢
      simp [ha, ih]

/-- The number of elements of `List.range n` that are greater than `b` is
`n - 1 - b`. -/
lemma length_filter_lt_range (b n : ℕ) :
    ((List.range n).filter (fun x => b < x)).length = n - 1 - b := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [List.range_succ, List.filter_append, List.length_append, ih]
    have hsingle : (List.filter (fun x => b < x) [n]).length = if b < n then 1 else 0 := by
      by_cases h : b < n <;> simp [h]
    rw [hsingle]
    by_cases h : b < n <;> simp [h] <;> omega

/-- A permutation of `List.range n` has exactly `n - 1 - b` entries larger
than `b`. -/
lemma length_filter_lt_of_perm_range {w : List ℕ} {b n : ℕ}
    (hw : w.Perm (List.range n)) :
    (w.filter (fun x => b < x)).length = n - 1 - b := by
  have h := (hw.filter (fun x => b < x)).length_eq
  rw [h, length_filter_lt_range]

/-- **Count identity.**  For a permutation word `w` of `List.range n` and a
letter `b ∈ w`, the entries above `b` before `b` plus the entries above `b`
after `b` account for all `n - 1 - b` entries above `b`. -/
theorem prefixAbove_length_add_afterCount {n b : ℕ} {w : List ℕ}
    (hw : w.Perm (List.range n)) (hb : b ∈ w) :
    (prefixAbove b w).length + afterCount b w = n - 1 - b := by
  obtain ⟨R, hR⟩ := exists_eq_takeWhile_append_cons hb
  set P := w.takeWhile (fun x => x ≠ b) with hP
  have hprefix : prefixAbove b w = P.filter (fun x => b < x) := by
    simp only [prefixAbove, hP]
  have hbP : b ∉ P := by
    intro hmem
    rw [hP] at hmem
    exact ne_of_mem_takeWhile_ne hmem rfl
  have hidx : w.idxOf b = P.length := by
    rw [hR, List.idxOf_append_of_notMem hbP]
    simp
  have hdrop : w.drop (w.idxOf b + 1) = R := by
    rw [hidx, hR, List.drop_append]
    simp
  have hafter : afterCount b w = (R.filter (fun x => b < x)).length := by
    simp [afterCount, hdrop]
  have hfilter : w.filter (fun x => b < x) =
      P.filter (fun x => b < x) ++ R.filter (fun x => b < x) := by
    rw [hR, List.filter_append, List.filter_cons]
    simp
  have hsplit : (w.filter (fun x => b < x)).length =
      (P.filter (fun x => b < x)).length + (R.filter (fun x => b < x)).length := by
    rw [hfilter, List.length_append]
  rw [hprefix, hafter]
  have hlen := length_filter_lt_of_perm_range (b := b) hw
  omega

/-! ## Depth from a nonempty iterate -/

/-- The pre-flush map sends the empty word to itself. -/
lemma preflush_nil : preflush ([] : List ℕ) = [] := rfl

/-- Every iterate of the pre-flush map on the empty word is empty. -/
lemma preflush_iterate_nil (k : ℕ) : (preflush^[k]) ([] : List ℕ) = [] := by
  induction k with
  | zero => rfl
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    simpa [preflush_nil] using ih

/-- If some iterate of the pre-flush map is nonempty, then its index is below
the sorting depth.  Once the word is empty it stays empty. -/
theorem sortingDepth_gt_of_preflush_ne_nil {w : List ℕ} {k : ℕ}
    (h : (preflush^[k]) w ≠ []) : k < sortingDepth w := by
  by_contra hcon
  have hsk : sortingDepth w ≤ k := Nat.le_of_not_lt hcon
  apply h
  have hk : k = (k - sortingDepth w) + sortingDepth w := (Nat.sub_add_cancel hsk).symm
  rw [hk, Function.iterate_add_apply, sortingDepth_spec, preflush_iterate_nil]

/-- Order form of `sortingDepth_gt_of_preflush_ne_nil`. -/
theorem sortingDepth_ge_of_preflush_ne_nil {w : List ℕ} {k : ℕ}
    (h : (preflush^[k]) w ≠ []) : k + 1 ≤ sortingDepth w :=
  Nat.succ_le_of_lt (sortingDepth_gt_of_preflush_ne_nil h)

/-- Conversely, if the sorting depth is at most `k`, then the `k`-th
pre-flush iterate is empty. -/
theorem preflush_eq_nil_of_sortingDepth_le {w : List ℕ} {k : ℕ}
    (h : sortingDepth w ≤ k) : (preflush^[k]) w = [] := by
  have hk : k = (k - sortingDepth w) + sortingDepth w := (Nat.sub_add_cancel h).symm
  rw [hk, Function.iterate_add_apply, sortingDepth_spec, preflush_iterate_nil]

/-! ## The witness bound -/

/-- `sortedAfter` is the Boolean statement that some iterate `k ≤ t` of West's
map is the identity word. -/
lemma sortedAfter_eq_true_iff {n t : ℕ} {p : Equiv.Perm (Fin n)} :
    sortedAfter t p = true ↔
      ∃ k ≤ t, (westStackSort^[k]) (permWord p) = identityWord n := by
  simp [sortedAfter, List.any_eq_true, List.mem_range, beq_iff_eq]

/-- **Witness reduction, word form.**  If a permutation word of `List.range n`
is not sent to the identity by `n - 5` passes of West's map, then some letter
`b` satisfies `b + t_b + e(X_b) ≤ 3`. -/
theorem exists_witness_of_not_sortedAfter {n : ℕ} (hn : 8 ≤ n) (w : List ℕ)
    (hperm : w.Perm (List.range n))
    (hne : (westStackSort^[n - 5]) w ≠ identityWord n) :
    ∃ b ∈ w, b + afterCount b w + excess (prefixAbove b w) ≤ 3 := by
  have hlen : w.length = n := by simpa using hperm.length_eq
  have hperm' : w.Perm (List.range w.length) := by
    simpa [hlen] using hperm
  have hchar := westStackSort_iterate_eq_identity_iff w hperm' (n - 5)
  have hnotall : ¬ ∀ b ∈ w, (preflush^[n - 5]) (prefixAbove b w) = [] := by
    intro h
    apply hne
    simpa [hlen] using hchar.mpr h
  push Not at hnotall
  obtain ⟨b, hb, hbne⟩ := hnotall
  have hdepth : n - 4 ≤ sortingDepth (prefixAbove b w) := by
    have := sortingDepth_ge_of_preflush_ne_nil hbne
    omega
  have hlenX : n - 4 ≤ (prefixAbove b w).length :=
    le_trans hdepth (sortingDepth_le_length (prefixAbove b w))
  have hcount := prefixAbove_length_add_afterCount (n := n) hperm hb
  have hbudget : b + afterCount b w ≤ 3 := by
    omega
  have hexcess : excess (prefixAbove b w) ≤ 3 - b - afterCount b w := by
    unfold excess
    omega
  exact ⟨b, hb, by omega⟩

/-- **Witness reduction, permutation form.**  A permutation `p` that is not
sorted by `n - 5` passes has a letter `b` in its one-line notation with
`b + t_b + e(X_b) ≤ 3`.

The paper's corresponding bound is `b + t_b + e(X_b) ≤ 4` with one-based
labels.  After the zero-based shift `b ↦ b - 1` the bound becomes `≤ 3`, and
`b` ranges over `{0, 1, 2, 3}`. -/
theorem exists_witness_of_not_mem_W {n : ℕ} (hn : 8 ≤ n) {p : Equiv.Perm (Fin n)}
    (hp : p ∉ W n (n - 5)) :
    ∃ b ∈ permWord p,
      b + afterCount b (permWord p) +
        excess (prefixAbove b (permWord p)) ≤ 3 := by
  have hs : sortedAfter (n - 5) p ≠ true := fun h => hp (mem_W.mpr h)
  have hs' : ¬ ∃ k ≤ n - 5, (westStackSort^[k]) (permWord p) = identityWord n := by
    rintro ⟨k, hk, hkeq⟩
    exact hs (sortedAfter_eq_true_iff.mpr ⟨k, hk, hkeq⟩)
  have hne : (westStackSort^[n - 5]) (permWord p) ≠ identityWord n :=
    fun h => hs' ⟨n - 5, le_rfl, h⟩
  exact exists_witness_of_not_sortedAfter hn (permWord p) (permWord_perm_range p) hne

end Claesson
