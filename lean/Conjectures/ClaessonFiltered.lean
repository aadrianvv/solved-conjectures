/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Conjectures.ClaessonStack

/-!
# The filtered-prefix identity for West's stack-sorting map

This file proves the structural identity at the heart of the
Claesson–Dukes–Steingrímsson stack-sorting argument: one pass of West's
stack-sorting map transforms the filtered prefix `prefixAbove b w` into the
pre-flush output of that prefix,

  `prefixAbove b (westStackSort w) = preflush (prefixAbove b w)`,

together with its iterated form

  `prefixAbove b ((westStackSort)^[k] w) = (preflush)^[k] (prefixAbove b w)`.

The key intermediate result is a minimum decomposition: if `b` is the least
letter of `w`, then `westStackSort w` begins with `preflush L` followed by `b`,
where `L` is the prefix of `w` before the first occurrence of `b`.

As a consequence we characterise when an iterate of West's map is the identity
word of the same length: this happens exactly when `k` pre-flush passes delete
every filtered prefix.

All words are lists of natural numbers with distinct entries in the
applications; the statements record the necessary `Nodup` hypothesis
explicitly.
-/

namespace Claesson

open LassalleRefinement

/-! ## The stack machine: suffixes, pushes and membership -/

/-- The reversed output after a single push keeps the old output as a suffix. -/
theorem stackPush_snd_suffix (x : ℕ) (s o : List ℕ) :
    ∃ t, (stackPush x s o).2 = t ++ o := by
  induction s generalizing o with
  | nil => exact ⟨[], by simp [stackPush]⟩
  | cons y ys ih =>
    by_cases h : x < y
    · exact ⟨[], by simp [stackPush, h]⟩
    · obtain ⟨t, ht⟩ := ih (y :: o)
      exact ⟨t ++ [y], by simp [stackPush, h, ht, List.append_assoc]⟩

/-- The reversed output of a full run keeps the old output as a suffix. -/
theorem stackRunState_snd_suffix (w s o : List ℕ) :
    ∃ t, (stackRunState w s o).2 = t ++ o := by
  induction w generalizing s o with
  | nil => exact ⟨[], by simp [stackRunState]⟩
  | cons x xs ih =>
    obtain ⟨t, ht⟩ := ih (stackPush x s o).1 (stackPush x s o).2
    obtain ⟨u, hu⟩ := stackPush_snd_suffix x s o
    refine ⟨t ++ u, ?_⟩
    simp only [stackRunState]
    rw [ht, hu]
    simp [List.append_assoc]

/-- Pushing a letter below the whole stack neither pops nor reorders it. -/
theorem stackPush_snd_eq_of_forall_lt (x : ℕ) (s o : List ℕ)
    (h : ∀ y ∈ s, x < y) :
    (stackPush x s o).2 = o ∧ (stackPush x s o).1 = x :: s := by
  cases s with
  | nil => simp [stackPush]
  | cons y ys =>
    have hxy : x < y := h y (by simp)
    simp [stackPush, hxy]

/-- Every letter of the stack after a push was already on the stack or is the
pushed letter. -/
theorem stackPush_fst_mem (x : ℕ) (s o : List ℕ) :
    ∀ y ∈ (stackPush x s o).1, y ∈ s ∨ y = x := by
  induction s generalizing o with
  | nil =>
    intro y hy
    simp only [stackPush, List.mem_singleton] at hy
    exact Or.inr hy
  | cons z zs ih =>
    intro y hy
    by_cases h : x < z
    · have hy' : y = x ∨ y ∈ z :: zs := by simpa [stackPush, h] using hy
      rcases hy' with rfl | hy''
      · exact Or.inr rfl
      · exact Or.inl hy''
    · have hy' : y ∈ (stackPush x zs (z :: o)).1 := by simpa [stackPush, h] using hy
      rcases ih (z :: o) y hy' with hy'' | rfl
      · exact Or.inl (List.mem_cons.mpr (Or.inr hy''))
      · exact Or.inr rfl

/-- Every letter of the final stack is either an initial stack letter or an
input letter. -/
theorem stackRunState_fst_mem (w s o : List ℕ) :
    ∀ y ∈ (stackRunState w s o).1, y ∈ s ∨ y ∈ w := by
  induction w generalizing s o with
  | nil =>
    intro y hy
    simp only [stackRunState] at hy
    exact Or.inl hy
  | cons x xs ih =>
    intro y hy
    simp only [stackRunState] at hy
    rcases ih (stackPush x s o).1 (stackPush x s o).2 y hy with h1 | h2
    · rcases stackPush_fst_mem x s o y h1 with h3 | rfl
      · exact Or.inl h3
      · exact Or.inr (List.mem_cons.mpr (Or.inl rfl))
    · exact Or.inr (List.mem_cons.mpr (Or.inr h2))

/-- Running on a concatenation is running on the two parts in succession. -/
theorem stackRunState_append (u v s o : List ℕ) :
    stackRunState (u ++ v) s o =
      stackRunState v (stackRunState u s o).1 (stackRunState u s o).2 := by
  induction u generalizing s o with
  | nil => simp [stackRunState]
  | cons x xs ih =>
    simp only [List.cons_append, stackRunState]
    exact ih (stackPush x s o).1 (stackPush x s o).2

/-! ## The minimum decomposition -/

/-- When the next letter `r` is at least `b`, the stack letter `b` is popped
immediately, so it appears in the reversed output in front of the old output. -/
theorem stackRunState_cons_snd_eq_suffix (b r : ℕ) (R S o : List ℕ)
    (hr : ¬ r < b) :
    ∃ u, (stackRunState (r :: R) (b :: S) o).2 = u ++ b :: o := by
  have hpush : stackPush r (b :: S) o = stackPush r S (b :: o) := by
    simp [stackPush, hr]
  obtain ⟨w, hw⟩ := stackPush_snd_suffix r S (b :: o)
  obtain ⟨u, hu⟩ :=
    stackRunState_snd_suffix R (stackPush r S (b :: o)).1 (stackPush r S (b :: o)).2
  refine ⟨u ++ w, ?_⟩
  simp only [stackRunState, hpush]
  rw [hu, hw, List.append_assoc]

/-- **Minimum decomposition.** If every letter of `L` and `R` is larger than
`b`, then West's sort of `L ++ b :: R` starts with the pre-flush output of `L`
followed by `b`. -/
theorem westStackSort_eq_preflush_append_cons_of_lt (b : ℕ) (L R : List ℕ)
    (hL : ∀ x ∈ L, b < x) (hR : ∀ x ∈ R, b < x) :
    ∃ t, westStackSort (L ++ b :: R) = preflush L ++ b :: t := by
  have hS : ∀ y ∈ (stackRunState L [] []).1, b < y := by
    intro y hy
    rcases stackRunState_fst_mem L [] [] y hy with h | h
    · exact absurd h (by simp)
    · exact hL y h
  obtain ⟨hpush2, hpush1⟩ :=
    stackPush_snd_eq_of_forall_lt b (stackRunState L [] []).1 (stackRunState L [] []).2 hS
  have hstep : stackRunState (L ++ b :: R) [] [] =
      stackRunState R (b :: (stackRunState L [] []).1) (stackRunState L [] []).2 := by
    rw [stackRunState_append]
    simp only [stackRunState]
    rw [hpush1, hpush2]
  cases R with
  | nil =>
    refine ⟨(stackRunState L [] []).1, ?_⟩
    rw [westStackSort_eq_preflush_append_finalStack]
    simp only [preflush, finalStack]
    rw [hstep]
    rfl
  | cons r R' =>
    have hr : ¬ r < b := by
      have := hR r (by simp)
      omega
    obtain ⟨u, hu⟩ :=
      stackRunState_cons_snd_eq_suffix b r R' (stackRunState L [] []).1
        (stackRunState L [] []).2 hr
    refine ⟨u.reverse ++ (stackRunState (L ++ b :: r :: R') [] []).1, ?_⟩
    rw [westStackSort_eq_preflush_append_finalStack]
    simp only [preflush, finalStack]
    rw [hstep, hu]
    simp [List.reverse_append, List.append_assoc]

/-- Every letter of the pre-flush output is an input letter. -/
theorem mem_preflush {x : ℕ} {w : List ℕ} (hx : x ∈ preflush w) : x ∈ w := by
  have h1 : x ∈ westStackSort w := by
    rw [westStackSort_eq_preflush_append_finalStack]
    exact List.mem_append_left _ hx
  have hperm : (westStackSort w).Perm w :=
    Multiset.coe_eq_coe.mp (westStackSort_multiset w)
  exact hperm.mem_iff.mp h1

/-! ## The filtered prefix and small rewriting lemmas -/

/-- The filtered prefix of `a :: as` when `a < b`: the head is invisible. -/
theorem prefixAbove_cons_of_lt {a b : ℕ} (hab : a < b) (as : List ℕ) :
    prefixAbove b (a :: as) = prefixAbove b as := by
  have hne : a ≠ b := by omega
  have hnlt : ¬ b < a := by omega
  simp [prefixAbove, hne, hnlt]

/-- The filtered prefix of `a :: as` when `b < a`: the head is retained. -/
theorem prefixAbove_cons_of_gt {a b : ℕ} (hab : b < a) (as : List ℕ) :
    prefixAbove b (a :: as) = a :: prefixAbove b as := by
  have hne : a ≠ b := by omega
  simp [prefixAbove, hne, hab]

/-- The filtered prefix stops at the head `b`. -/
theorem prefixAbove_cons_self (b : ℕ) (as : List ℕ) :
    prefixAbove b (b :: as) = [] := by
  simp [prefixAbove]

/-- If every letter of `A` is above `b`, then the filtered prefix of
`A ++ b :: t` is exactly `A`. -/
theorem prefixAbove_append_cons_of_lt (b : ℕ) {A t : List ℕ}
    (hA : ∀ x ∈ A, b < x) :
    prefixAbove b (A ++ b :: t) = A := by
  induction A with
  | nil => simp [prefixAbove]
  | cons a as ih =>
    have hba : b < a := hA a (by simp)
    have htail : ∀ x ∈ as, b < x := fun x hx => hA x (by simp [hx])
    rw [List.cons_append, prefixAbove_cons_of_gt hba, ih htail]

/-- Every letter of a `takeWhile` is retained by the predicate. -/
theorem ne_of_mem_takeWhile_ne {b x : ℕ} {v : List ℕ}
    (hx : x ∈ v.takeWhile (fun y => y ≠ b)) : x ≠ b := by
  induction v with
  | nil => simp at hx
  | cons a as ih =>
    by_cases ha : a = b
    · subst ha
      simp at hx
    · rw [List.takeWhile_cons_of_pos (p := fun y => y ≠ b) (by simpa using ha)] at hx
      rcases List.mem_cons.mp hx with rfl | hx
      · exact ha
      · exact ih hx

/-- Deleting all letters below `b` does not change the filtered prefix at `b`. -/
theorem prefixAbove_filter_above (b : ℕ) (u : List ℕ) :
    prefixAbove b u = prefixAbove b (u.filter (above b)) := by
  induction u with
  | nil => simp [prefixAbove]
  | cons a as ih =>
    by_cases hle : b ≤ a
    · by_cases hEq : a = b
      · subst hEq
        simp [prefixAbove]
      · have hlt : b < a := lt_of_le_of_ne hle (Ne.symm hEq)
        have hfilter : (a :: as).filter (above b) = a :: as.filter (above b) := by
          have ha : above b a = true := by simpa using hle
          simp [ha]
        simp only [hfilter, prefixAbove_cons_of_gt hlt, ih]
    · have hlt : a < b := Nat.lt_of_not_le hle
      have hfilter : (a :: as).filter (above b) = as.filter (above b) := by
        have ha : above b a = false := by simp [above, hle]
        simp [ha]
      simp only [hfilter, prefixAbove_cons_of_lt hlt]
      exact ih

/-! ## Splitting a word at its first occurrence of a letter -/

/-- If `b` occurs in `v`, then `v` splits as the prefix before the first `b`,
then `b`, then the rest. -/
theorem exists_eq_takeWhile_append_cons {b : ℕ} {v : List ℕ} (hb : b ∈ v) :
    ∃ R, v = v.takeWhile (fun x => x ≠ b) ++ b :: R := by
  induction v with
  | nil => simp at hb
  | cons a as ih =>
    by_cases ha : a = b
    · subst ha
      exact ⟨as, by simp⟩
    · have hb' : b ∈ as := by
        rcases List.mem_cons.mp hb with h | h
        · exact absurd h.symm ha
        · exact h
      obtain ⟨R, hR⟩ := ih hb'
      refine ⟨R, ?_⟩
      rw [List.takeWhile_cons_of_pos (p := fun x => x ≠ b) (by simpa using ha)]
      simp only [List.cons_append, ← hR]

/-! ## Strictly increasing words and filtered prefixes -/

/-- A strictly increasing word has empty filtered prefix at each of its
letters. -/
theorem prefixAbove_eq_nil_of_pairwise_lt {w : List ℕ} {b : ℕ}
    (hs : w.Pairwise (· < ·)) (hb : b ∈ w) : prefixAbove b w = [] := by
  induction w with
  | nil => simp at hb
  | cons a as ih =>
    rcases List.mem_cons.mp hb with hEq | hb'
    · rw [hEq]
      exact prefixAbove_cons_self a as
    · have hs' := List.pairwise_cons.mp hs
      have hab : a < b := hs'.1 b hb'
      rw [prefixAbove_cons_of_lt hab]
      exact ih hs'.2 hb'

/-- A nodup word all of whose filtered prefixes are empty is strictly
increasing. -/
theorem pairwise_lt_of_prefixAbove_eq_nil {u : List ℕ}
    (hnd : u.Nodup) (h : ∀ b ∈ u, prefixAbove b u = []) : u.Pairwise (· < ·) := by
  induction u with
  | nil => exact List.Pairwise.nil
  | cons a as ih =>
    have hnd' := List.nodup_cons.mp hnd
    have ha_notin : a ∉ as := hnd'.1
    have hnd_tail : as.Nodup := hnd'.2
    have hforall : ∀ x ∈ as, a < x := by
      intro x hx
      have hxmem : x ∈ a :: as := List.mem_cons.mpr (Or.inr hx)
      have hne : x ≠ a := fun hxa => ha_notin (hxa ▸ hx)
      by_contra hnot
      have hxlt : x < a := by omega
      have ha_mem : a ∈ prefixAbove x (a :: as) := by
        rw [prefixAbove_cons_of_gt hxlt]
        exact List.mem_cons_self
      rw [h x hxmem] at ha_mem
      simp at ha_mem
    have htail : ∀ b ∈ as, prefixAbove b as = [] := by
      intro b hb
      have hb_mem : b ∈ a :: as := List.mem_cons.mpr (Or.inr hb)
      have hb_eq : prefixAbove b (a :: as) = prefixAbove b as :=
        prefixAbove_cons_of_lt (hforall b hb) as
      rw [← hb_eq]
      exact h b hb_mem
    exact List.pairwise_cons.mpr ⟨hforall, ih hnd_tail htail⟩

/-- A strictly increasing permutation of `List.range n` is `List.range n`. -/
theorem eq_range_of_perm_of_sortedLT {u : List ℕ} {n : ℕ}
    (hu : u.SortedLT) (hp : u.Perm (List.range n)) : u = List.range n :=
  List.Perm.eq_of_sortedLE hu.sortedLE (List.sortedLT_range n).sortedLE hp

/-! ## The one-pass filtered-prefix identity -/

/-- **One-pass filtered-prefix identity.** For a nodup word containing `b`, one
pass of West's stack sort sends the filtered prefix at `b` to the pre-flush
output of that prefix. -/
theorem prefixAbove_westStackSort_eq_preflush (b : ℕ) (w : List ℕ)
    (hnd : w.Nodup) (hb : b ∈ w) :
    prefixAbove b (westStackSort w) = preflush (prefixAbove b w) := by
  set v := w.filter (above b) with hv
  have hvnd : v.Nodup := hnd.filter (above b)
  have hb_v : b ∈ v := by
    rw [hv]
    exact List.mem_filter.mpr ⟨hb, by simp⟩
  have hle_v : ∀ x ∈ v, b ≤ x := by
    intro x hx
    rw [hv] at hx
    exact above_eq_true.mp (List.mem_filter.mp hx).2
  obtain ⟨R, hdec⟩ := exists_eq_takeWhile_append_cons hb_v
  set L := v.takeWhile (fun x => x ≠ b) with hL
  have hdec' : v = L ++ b :: R := hdec
  have hL_lt : ∀ x ∈ L, b < x := by
    intro x hx
    rw [hL] at hx
    have hxv : x ∈ v := List.takeWhile_subset (p := fun y => y ≠ b) hx
    have hne : x ≠ b := ne_of_mem_takeWhile_ne hx
    exact lt_of_le_of_ne (hle_v x hxv) (Ne.symm hne)
  have hbR : b ∉ R := by
    have hnd_append : (L ++ b :: R).Nodup := hdec' ▸ hvnd
    have hnd_cons : (b :: R).Nodup := hnd_append.of_append_right
    exact (List.nodup_cons.mp hnd_cons).1
  have hR_lt : ∀ x ∈ R, b < x := by
    intro x hx
    have hxv : x ∈ v := by
      rw [hdec']
      exact List.mem_append.mpr (Or.inr (List.mem_cons.mpr (Or.inr hx)))
    have hne : b ≠ x := fun h => hbR (h ▸ hx)
    exact lt_of_le_of_ne (hle_v x hxv) hne
  obtain ⟨t, ht⟩ := westStackSort_eq_preflush_append_cons_of_lt b L R hL_lt hR_lt
  have hsort : westStackSort v = preflush L ++ b :: t := by
    rw [hdec']
    exact ht
  have hpfx_v : prefixAbove b v = L := by
    have h1 : prefixAbove b v = L.filter (fun x => b < x) := by
      unfold prefixAbove
      rw [← hL]
    rw [h1]
    rw [List.filter_eq_self]
    intro x hx
    simpa using hL_lt x hx
  have hpfx_w : prefixAbove b v = prefixAbove b w := by
    rw [hv]
    exact (prefixAbove_filter_above b w).symm
  have hpre_lt : ∀ x ∈ preflush L, b < x :=
    fun x hx => hL_lt x (mem_preflush hx)
  have hpre_sort : prefixAbove b (westStackSort v) = preflush L := by
    rw [hsort]
    exact prefixAbove_append_cons_of_lt b hpre_lt
  have habove : (fun x : ℕ => decide (b ≤ x)) = above b := rfl
  have hv' : v = w.filter (fun x : ℕ => decide (b ≤ x)) := hv
  calc
    prefixAbove b (westStackSort w)
        = prefixAbove b ((westStackSort w).filter (above b)) :=
            prefixAbove_filter_above b (westStackSort w)
    _ = prefixAbove b ((westStackSort w).filter (fun x : ℕ => decide (b ≤ x))) := by
          rw [← habove]
    _ = prefixAbove b (westStackSort (w.filter (fun x : ℕ => decide (b ≤ x)))) := by
          rw [westStackSort_filter b w]
    _ = prefixAbove b (westStackSort v) := by rw [hv']
    _ = preflush L := hpre_sort
    _ = preflush (prefixAbove b v) := by rw [hpfx_v]
    _ = preflush (prefixAbove b w) := by rw [hpfx_w]

/-! ## The iterated identity -/

/-- West's map preserves the permutation class of a word at every iterate. -/
theorem westStackSort_iterate_perm (w : List ℕ) (k : ℕ) :
    ((westStackSort^[k]) w).Perm w := by
  induction k generalizing w with
  | zero => simp
  | succ k ih =>
    rw [Function.iterate_succ_apply]
    exact (ih (westStackSort w)).trans
      (Multiset.coe_eq_coe.mp (westStackSort_multiset w))

/-- **Iterated filtered-prefix identity.** After `k` passes of West's map, the
filtered prefix at `b` is the `k`-fold pre-flush output of the original filtered
prefix. -/
theorem prefixAbove_westStackSort_iterate (b : ℕ) :
    ∀ (k : ℕ) (w : List ℕ), w.Nodup → b ∈ w →
      prefixAbove b ((westStackSort^[k]) w) = (preflush^[k]) (prefixAbove b w) := by
  intro k
  induction k with
  | zero =>
    intro w _ _
    simp
  | succ k ih =>
    intro w hnd hb
    have hperm : (westStackSort w).Perm w :=
      Multiset.coe_eq_coe.mp (westStackSort_multiset w)
    have hnd' : (westStackSort w).Nodup := hperm.nodup_iff.mpr hnd
    have hb' : b ∈ westStackSort w := hperm.mem_iff.mpr hb
    rw [Function.iterate_succ_apply, Function.iterate_succ_apply]
    rw [ih (westStackSort w) hnd' hb', prefixAbove_westStackSort_eq_preflush b w hnd hb]

/-! ## Sorting-depth characterisation -/

/-- **Sorting characterisation.** A word is sorted after `k` passes if and only
if `k` pre-flush passes delete every filtered prefix of the word. -/
theorem westStackSort_iterate_eq_identity_iff (w : List ℕ)
    (hw : w.Perm (List.range w.length)) (k : ℕ) :
    (westStackSort^[k]) w = identityWord w.length ↔
      ∀ b ∈ w, (preflush^[k]) (prefixAbove b w) = [] := by
  constructor
  · intro hsort b hb
    have hnd : w.Nodup := hw.nodup_iff.mpr List.nodup_range
    have hiter := prefixAbove_westStackSort_iterate b k w hnd hb
    rw [hsort] at hiter
    have hnil : prefixAbove b (identityWord w.length) = [] := by
      have hb_range : b ∈ List.range w.length := hw.mem_iff.mp hb
      have := prefixAbove_eq_nil_of_pairwise_lt
        (List.pairwise_lt_range (n := w.length)) hb_range
      simpa [identityWord] using this
    rw [← hiter, hnil]
  · intro hprefix
    have hnd : w.Nodup := hw.nodup_iff.mpr List.nodup_range
    have hperm_iter : ((westStackSort^[k]) w).Perm w := westStackSort_iterate_perm w k
    have hperm_range : ((westStackSort^[k]) w).Perm (List.range w.length) :=
      hperm_iter.trans hw
    have hprefix_iter : ∀ b ∈ (westStackSort^[k]) w,
        prefixAbove b ((westStackSort^[k]) w) = [] := by
      intro b hb
      have hbw : b ∈ w := hperm_iter.mem_iff.mp hb
      rw [prefixAbove_westStackSort_iterate b k w hnd hbw, hprefix b hbw]
    have hsorted : ((westStackSort^[k]) w).Pairwise (· < ·) :=
      pairwise_lt_of_prefixAbove_eq_nil
        (hperm_range.nodup_iff.mpr List.nodup_range) hprefix_iter
    have hsortedLT : ((westStackSort^[k]) w).SortedLT :=
      List.sortedLT_iff_pairwise.mpr hsorted
    have huniq : (westStackSort^[k]) w = List.range w.length :=
      eq_range_of_perm_of_sortedLT hsortedLT hperm_range
    simpa [identityWord] using huniq

end Claesson
