import Conjectures.ClaessonDefs

open Claesson

-- Sanity checks for the definitions.  These are deliberately tiny: the
-- full finite checks at n = 8, 9, 10 belong to the counting proof.
example : (W 0 0).card = 1 := by decide
example : (W 1 0).card = 1 := by decide
example : (W 2 0).card = 1 := by decide
example : (W 2 1).card = 2 := by decide
example : (W 3 0).card = 1 := by decide
example : (W 3 1).card = 5 := by decide
example : (W 4 0).card = 1 := by decide
example : (W 4 1).card = 14 := by decide

-- The polynomial evaluates to the paper's n = 8 value.
example : nearTopPolynomial 8 = 214260 := by decide
