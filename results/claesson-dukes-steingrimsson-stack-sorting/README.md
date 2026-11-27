# Claesson–Dukes–Steingrímsson’s stack-sorting conjecture

**Proved by exact computation.** For every $n\ge8$, the number of permutations of length $n$ sorted by at most $n-5$ passes through West’s stack is

$$
\frac{(n-5)!}{60}\bigl(60n^5-600n^4+506n^3+11241n^2-38369n+34236\bigr).
$$

This proves [Conjecture 2.4](https://arxiv.org/abs/0812.0143v2) in *Permutations Sortable by n − 4 Passes Through a Stack*. The proof reduces the count at every order to eleven marked values, at most six constrained unmarked entries, and an exact polynomial identity.

- [Complete proof and coefficient table](PROOF.md)
- [Review, prior work and attribution](AUDIT.md)
- [Reproduce the enumeration, arithmetic and base cases](verify.ps1)

**Lean status:** partially formalized. The statement, the complement form, the filtered-prefix principle, the ten-row polynomial identity, the exact-depth equivalence and the stars-and-bars factor are checked in `lean/Conjectures/Claesson*.lean`; the marked-order enumeration remains an explicit hypothesis. See the [Lean checkpoint](../../docs/claesson-formalization.md) and the [assembly module](../../lean/Conjectures/ClaessonMain.lean).
