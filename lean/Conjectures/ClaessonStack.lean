/-
Copyright (c) 2026 The solved-conjectures contributors.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: a small swarm of DeepSeek V4.1 Flash 1017
-/
import Conjectures.ClaessonDefs
import Mathlib.Data.List.Basic
import Mathlib.Data.List.MinMax
import Mathlib.Data.Multiset.Basic

/-!
# Structural theory of West's stack-sorting map

This file develops the parts of the structural theory of West's deterministic
stack-sorting map `westStackSort` that are used in the proof of the
Claesson–Dukes–Steingrímsson stack-sorting conjecture.

We isolate the *pre-flush* output `preflush w` (everything emitted before the
final flush of the stack) and the final stack `finalStack w`, and prove

  `westStackSort w = preflush w ++ finalStack w`.

The main structural results are:

* deletion of all letters below a threshold commutes with one pass
  (`westStackSort_filter`);
* the pre-flush output strictly shortens every nonempty word
  (`preflush_lt_length`).

We also define the filtered prefix `prefixAbove b w` (the paper's `X_b`), the
sorting depth `sortingDepth` (the least number of pre-flush passes that empties
a word) and the excess `excess`, together with the basic recurrence
`sortingDepth w = sortingDepth (preflush w) + 1` for nonempty words.
-/

namespace Claesson

open LassalleRefinement

/-! ## The pre-flush output and the final stack -/

/-- Run the stack machine on `w` starting from stack `s` and reversed output
`o`, returning the final pair `(stack, reversed output)`. -/
def stackRunState : List ℕ → List ℕ → List ℕ → List ℕ × List ℕ
  | [], s, o => (s, o)
  | x :: xs, s, o =>
    let z := stackPush x s o
    stackRunState xs z.1 z.2

/-- The output emitted before the final flush of the stack. -/
def preflush (w : List ℕ) : List ℕ := (stackRunState w [] []).2.reverse

/-- The contents of the stack at the end of the run, which are flushed out in
increasing order (top to bottom). -/
def finalStack (w : List ℕ) : List ℕ := (stackRunState w [] []).1

/-- Relating the stack loop to the state-passing run. -/
theorem stackLoop_eq_state (w s o : List ℕ) :
    stackLoop w s o = (stackRunState w s o).2.reverse ++ (stackRunState w s o).1 := by
  induction w generalizing s o with
  | nil => simp [stackLoop, stackRunState]
  | cons x xs ih =>
    simp only [stackLoop, stackRunState]
    exact ih (stackPush x s o).1 (stackPush x s o).2

/-- The output of West's stack sort splits into the pre-flush output and the
final stack. -/
theorem westStackSort_eq_preflush_append_finalStack (w : List ℕ) :
    westStackSort w = preflush w ++ finalStack w := by
  unfold westStackSort preflush finalStack
  simpa using stackLoop_eq_state w [] []

/-- Length effect of one push. -/
theorem stackPush_length (x : ℕ) (s o : List ℕ) :
    (stackPush x s o).1.length + (stackPush x s o).2.length = s.length + o.length + 1 := by
  induction s generalizing o with
  | nil => simp [stackPush]; omega
  | cons y ys ih =>
    by_cases h : x < y
    · simp only [stackPush, if_pos h]
      simp
      omega
    · simp only [stackPush, if_neg h]
      rw [ih (y :: o)]
      simp
      omega

/-- Lengths of the two state components. -/
theorem stackRunState_length (w s o : List ℕ) :
    (stackRunState w s o).1.length + (stackRunState w s o).2.length =
      s.length + o.length + w.length := by
  induction w generalizing s o with
  | nil => simp [stackRunState]
  | cons x xs ih =>
    simp only [stackRunState]
    rw [ih (stackPush x s o).1 (stackPush x s o).2, stackPush_length]
    simp
    omega

/-- The pre-flush output and the final stack together have the length of the
word. -/
theorem preflush_length_add_finalStack_length (w : List ℕ) :
    (preflush w).length + (finalStack w).length = w.length := by
  have h : (stackRunState w [] []).1.length + (stackRunState w [] []).2.length = w.length := by
    simpa using stackRunState_length w [] []
  simp only [preflush, finalStack, List.length_reverse]
  omega

/-- The stack after a push is never empty. -/
theorem stackPush_fst_ne_nil (x : ℕ) (s o : List ℕ) : (stackPush x s o).1 ≠ [] := by
  induction s generalizing o with
  | nil => simp [stackPush]
  | cons y ys ih =>
    by_cases h : x < y
    · simp [stackPush, h]
    · simp only [stackPush, if_neg h]
      exact ih (y :: o)

/-- After processing a nonempty word the stack is nonempty. -/
theorem stackRunState_fst_ne_nil (w s o : List ℕ) (hw : w ≠ []) :
    (stackRunState w s o).1 ≠ [] := by
  induction w generalizing s o with
  | nil => exact absurd rfl hw
  | cons x xs ih =>
    cases xs with
    | nil =>
      simp only [stackRunState]
      exact stackPush_fst_ne_nil x s o
    | cons y ys =>
      simp only [stackRunState]
      exact ih (stackPush x s o).1 (stackPush x s o).2 (by simp)

/-- The final stack of a nonempty word is nonempty. -/
theorem finalStack_ne_nil {w : List ℕ} (hw : w ≠ []) : finalStack w ≠ [] := by
  unfold finalStack
  exact stackRunState_fst_ne_nil w [] [] hw

/-- The pre-flush output is no longer than the input. -/
theorem preflush_length_le (w : List ℕ) : (preflush w).length ≤ w.length := by
  have h := preflush_length_add_finalStack_length w
  omega

/-- The pre-flush output strictly shortens every nonempty word. -/
theorem preflush_lt_length {w : List ℕ} (hw : w ≠ []) : (preflush w).length < w.length := by
  have h := preflush_length_add_finalStack_length w
  have hpos : 0 < (finalStack w).length := by
    rw [List.length_pos_iff]
    exact finalStack_ne_nil hw
  omega

/-! ## Deletion of letters below a threshold -/

/-- The threshold predicate `b ≤ x`, as a boolean. -/
def above (b : ℕ) : ℕ → Bool := fun x => decide (b ≤ x)

@[simp] theorem above_eq_true {b x : ℕ} : above b x = true ↔ b ≤ x := by
  simp [above]

/-- Pushing a retained letter commutes with filtering the stack and output. -/
theorem stackPush_filter_of_le (b x : ℕ) (s o : List ℕ) (hx : b ≤ x) :
    (stackPush x s o).1.filter (above b) =
        (stackPush x (s.filter (above b)) (o.filter (above b))).1 ∧
      (stackPush x s o).2.filter (above b) =
        (stackPush x (s.filter (above b)) (o.filter (above b))).2 := by
  induction s generalizing o with
  | nil =>
    have hx' : above b x = true := by simpa using hx
    simp [stackPush, hx']
  | cons y ys ih =>
    by_cases hxy : x < y
    · have hy : b ≤ y := le_trans hx (le_of_lt hxy)
      have hx' : above b x = true := by simpa using hx
      have hy' : above b y = true := by simpa using hy
      have hf : (y :: ys).filter (above b) = y :: ys.filter (above b) := by
        simp [List.filter_cons, hy']
      simp [stackPush, hxy, hx', hy', hf]
    · obtain ⟨h1, h2⟩ := ih (y :: o)
      by_cases hy : b ≤ y
      · have hy' : above b y = true := by simpa using hy
        have hf : (y :: ys).filter (above b) = y :: ys.filter (above b) := by
          simp [List.filter_cons, hy']
        have hfy : (y :: o).filter (above b) = y :: o.filter (above b) := by
          simp [List.filter_cons, hy']
        rw [hf]
        simp only [stackPush, if_neg hxy]
        rw [hfy] at h1 h2
        exact ⟨h1, h2⟩
      · have hy' : above b y = false := by simp [above, hy]
        have hf : (y :: ys).filter (above b) = ys.filter (above b) := by
          simp [List.filter_cons, hy']
        have hfy : (y :: o).filter (above b) = o.filter (above b) := by
          simp [List.filter_cons, hy']
        rw [hf]
        simp only [stackPush, if_neg hxy]
        rw [hfy] at h1 h2
        exact ⟨h1, h2⟩

/-- Pushing a deleted letter leaves the filtered state unchanged. -/
theorem stackPush_filter_of_lt (b x : ℕ) (s o : List ℕ) (hx : ¬ b ≤ x) :
    (stackPush x s o).1.filter (above b) = s.filter (above b) ∧
      (stackPush x s o).2.filter (above b) = o.filter (above b) := by
  induction s generalizing o with
  | nil =>
    have hx' : above b x = false := by simp [above, hx]
    simp [stackPush, hx']
  | cons y ys ih =>
    by_cases hxy : x < y
    · have hx' : above b x = false := by simp [above, hx]
      simp [stackPush, hxy, hx']
    · have hy : ¬ b ≤ y := by omega
      have hy' : above b y = false := by simp [above, hy]
      obtain ⟨h1, h2⟩ := ih (y :: o)
      have hf : (y :: ys).filter (above b) = ys.filter (above b) := by
        simp [hy']
      have hfy : (y :: o).filter (above b) = o.filter (above b) := by
        simp [hy']
      rw [hf]
      simp only [stackPush, if_neg hxy]
      rw [hfy] at h2
      exact ⟨h1, h2⟩

/-- The state of the run commutes with filtering at a threshold. -/
theorem stackRunState_filter (b : ℕ) (w s o : List ℕ) :
    (stackRunState w s o).1.filter (above b) =
        (stackRunState (w.filter (above b)) (s.filter (above b)) (o.filter (above b))).1 ∧
      (stackRunState w s o).2.filter (above b) =
        (stackRunState (w.filter (above b)) (s.filter (above b)) (o.filter (above b))).2 := by
  induction w generalizing s o with
  | nil => simp [stackRunState]
  | cons x xs ih =>
    by_cases hx : b ≤ x
    · obtain ⟨h1, h2⟩ := stackPush_filter_of_le b x s o hx
      have hx' : above b x = true := by simpa using hx
      simp only [stackRunState, List.filter_cons, hx', if_true]
      obtain ⟨i1, i2⟩ := ih (s := (stackPush x s o).1) (o := (stackPush x s o).2)
      refine ⟨?_, ?_⟩
      · simp only [i1, h1, h2]
      · simp only [i2, h1, h2]
    · obtain ⟨h1, h2⟩ := stackPush_filter_of_lt b x s o hx
      have hx' : above b x = false := by simp [above, hx]
      simp [stackRunState, List.filter_cons, hx']
      obtain ⟨i1, i2⟩ := ih (s := (stackPush x s o).1) (o := (stackPush x s o).2)
      refine ⟨?_, ?_⟩
      · simp only [i1, h1, h2]
      · simp only [i2, h1, h2]

/-- **Deletion commutes with one pass.** Deleting all letters below a threshold
before or after applying West's stack sort gives the same result. -/
theorem westStackSort_filter (b : ℕ) (w : List ℕ) :
    westStackSort (w.filter (fun x => b ≤ x)) =
      (westStackSort w).filter (fun x => b ≤ x) := by
  change westStackSort (w.filter (above b)) = (westStackSort w).filter (above b)
  have h := stackRunState_filter b w [] []
  simp only [westStackSort_eq_preflush_append_finalStack, List.filter_append,
    preflush, finalStack, List.filter_reverse] at h ⊢
  rw [h.2, h.1]
  rfl

/-! ## The filtered-prefix construction -/

/-- For a value `b`, the entries larger than `b` that occur before `b` in `w`.
This is the paper's `X_b`. -/
def prefixAbove (b : ℕ) (w : List ℕ) : List ℕ :=
  (w.takeWhile (fun x => x ≠ b)).filter (fun x => b < x)

/-- The filtered prefix is a sublist of the original word. -/
theorem prefixAbove_sublist (b : ℕ) (w : List ℕ) : (prefixAbove b w).Sublist w :=
  (List.filter_sublist (p := fun x => b < x)).trans
    (List.takeWhile_sublist (p := fun x => x ≠ b))

/-- The filtered prefix is no longer than the original word. -/
theorem prefixAbove_length_le (b : ℕ) (w : List ℕ) :
    (prefixAbove b w).length ≤ w.length :=
  (prefixAbove_sublist b w).length_le

/-! ## Sorting depth and excess -/

/-- After `m` steps of the pre-flush map, every word of length at most `m`
has become empty. -/
theorem preflush_iterate_eq_nil_of_length_le (m : ℕ) :
    ∀ w : List ℕ, w.length ≤ m → (preflush^[m]) w = [] := by
  induction m with
  | zero =>
    intro w hw
    have hw0 : w.length = 0 := Nat.le_zero.mp hw
    have hw' : w = [] := List.length_eq_zero_iff.mp hw0
    subst hw'
    rfl
  | succ m ih =>
    intro w hw
    cases w with
    | nil =>
      rw [Function.iterate_succ_apply]
      exact ih [] (by simp)
    | cons a as =>
      rw [Function.iterate_succ_apply]
      apply ih
      have h1 := preflush_lt_length (by simp : (a :: as) ≠ [])
      have h2 := hw
      simp only [List.length_cons] at h1 h2
      omega

/-- The sorting depth `h(w)`: the least number of pre-flush passes needed to
empty `w`. -/
noncomputable def sortingDepth (w : List ℕ) : ℕ :=
  Nat.find (p := fun k => (preflush^[k]) w = [])
    ⟨w.length, preflush_iterate_eq_nil_of_length_le w.length w le_rfl⟩

/-- The defining property of the sorting depth. -/
theorem sortingDepth_spec (w : List ℕ) : (preflush^[sortingDepth w]) w = [] := by
  unfold sortingDepth
  exact Nat.find_spec (p := fun k => (preflush^[k]) w = []) _

/-- Minimality of the sorting depth. -/
theorem sortingDepth_min (w : List ℕ) {k : ℕ} (hk : (preflush^[k]) w = []) :
    sortingDepth w ≤ k := by
  unfold sortingDepth
  exact Nat.find_min' (p := fun k => (preflush^[k]) w = []) _ hk

/-- The sorting depth is at most the length. -/
theorem sortingDepth_le_length (w : List ℕ) : sortingDepth w ≤ w.length :=
  sortingDepth_min w (preflush_iterate_eq_nil_of_length_le w.length w le_rfl)

/-- The excess `e(w) = |w| - h(w)` of the paper. -/
noncomputable def excess (w : List ℕ) : ℕ := w.length - sortingDepth w

/-- For a nonempty word, one pre-flush pass lowers the sorting depth by
exactly one. -/
theorem sortingDepth_eq_succ (w : List ℕ) (hw : w ≠ []) :
    sortingDepth w = sortingDepth (preflush w) + 1 := by
  apply le_antisymm
  · apply sortingDepth_min
    rw [Function.iterate_succ_apply]
    exact sortingDepth_spec (preflush w)
  · cases h : sortingDepth w with
    | zero =>
      exfalso
      have := sortingDepth_spec w
      rw [h, Function.iterate_zero_apply] at this
      exact hw this
    | succ k =>
      have hle : sortingDepth (preflush w) ≤ k := by
        apply sortingDepth_min
        have := sortingDepth_spec w
        rw [h, Function.iterate_succ_apply] at this
        exact this
      omega

end Claesson
