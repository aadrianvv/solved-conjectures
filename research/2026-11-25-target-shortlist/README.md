# Research files for issues #886, #887 and #888

This folder holds the working notes, proofs, checkers and review reports behind three issues in [1337isnot1337/solved-conjectures](https://github.com/1337isnot1337/solved-conjectures). The results were produced by Claude Opus 5.5 (Anthropic) research agents and reviewed by separate Claude Opus 5.5 agents. No human has refereed them and none is Lean-formalised. They are released for anyone to use.

Absolute paths inside scripts and notes were written on the original machine and have been anonymised. Run the checkers from this folder.

## Favaron–Genest–Kouider conjecture ([#886](https://github.com/1337isnot1337/solved-conjectures/issues/886))

Start with `04-HANDOFF.md`.

- **Theorem A:** `04d-regular-path-matching-relative-theorem.md`
- **Theorem B:** `04e-regular-path-diamond-free.md`
- **Theorems B′ and C:** `04g-regular-path-p5-and-m-diamond.md`, with `04h` (reformulations of (P5)) and `04i` (P5\* counterexample)
- **FGK Problems 3, 5 and 6:** `04b-regular-path-center-counterexample.md` and `04c-regular-path-problems-3-and-6.md`
- **Reviews:** `04-REVIEW-theorem-*.md`, `REVIEW-2026-11-26/04-review.md` and `04-NOVELTY-fgk2010.md`
- **Checkers:** `check_regular_path_*.py`, with the independent referee checkers `check_regular_path_theorem*_independent.py`

The second reviewer's Problem 3/6 checker is `REVIEW-2026-11-26/04-scratch/verify_p3_p6.py`.

**Known checker issue.** Line 299 of `check_regular_path_theoremC_independent.py` rejects a D-pendant equal to any d-label. Lemma C6 only excludes the trail's own d-label, so the default full run reports one false failure. With that test relaxed (`REVIEW-2026-11-26/04-scratch/thmC_relaxed.py`), the flagged instance decomposes and further full runs pass. See `REVIEW-2026-11-26/04-review.md` §2.

## Caro–Petruševski–Škrekovski proper conflict-free colouring, Δ = 4 ([#887](https://github.com/1337isnot1337/solved-conjectures/issues/887))

- **Notes and proofs:** `03-conflict-free-colouring.md` (start there) and `03-HANDOFF.md`
- **Review:** `REVIEW-2026-11-26/03-review.md`, with rerun logs in `REVIEW-2026-11-26/03-scratch/`

Checkers (Node.js):

- `check_03_treewidth_three.js` and `check_03_pathwidth_three.js` (treewidth/pathwidth ≤ 3)
- `check_03_cut_permutations.js` and `check_03_one_hole_barrier.js` (reductions)
- `check_03_conflict_free_colouring.js` (small-order census)

The order-14 census implementation is the Rust crate `03-handoff/pcf-census-rs`.

## Revised Local Irregularity Conjecture, subcubic case ([#888](https://github.com/1337isnot1337/solved-conjectures/issues/888))

- **Notes and proofs:** `06-revised-local-irregularity.md` and `06-HANDOFF.md`
- **Checkers:** `06-local-irregularity-cut-check.py` and `06-local-irregularity-rank-check.py`
- **Search programs and certificates:** `06-handoff/` (C# and Python sources, plus witness and domain tables)
- **Review:** `REVIEW-2026-11-26/06-review.md`, with tests in `REVIEW-2026-11-26/06-scratch/`
