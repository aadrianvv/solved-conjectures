# Currie's conjecture on complexity 2n+1 and critical exponent

[Catalogue](../../CONTENTS.md) · [Proof](PROOF.md) · [Exact checks](verify.py) · [Issue #148](https://github.com/1337isnot1337/solved-conjectures/issues/148)

**Status:** Written proof, computer-assisted in finitely many described places, all of which `verify.py` reproduces. It has been through one independent referee pass by a second model instance, which found no error; the minor gaps and notation remarks it raised are addressed in the note. The note is otherwise unrefereed.

**Lean status:** none. No Lean formalization is included.

Primary source: J. D. Currie, *Words with factor complexity $`2n+1`$ and minimal critical exponent*, Electron. J. Combin. 33(3) (2026), #P3.31, [DOI 10.37236/14527](https://doi.org/10.37236/14527), Conjecture 19 (Figures 3 and 4); the same conjecture is Conjecture 1 (Figures 1 and 2) of [arXiv:2507.09387v3](https://arxiv.org/abs/2507.09387v3).

## Result

Let $`\gamma=[01,2,02]`$ be the morphism $`0\mapsto 01`$, $`1\mapsto 2`$, $`2\mapsto 02`$ on $`\{0,1,2\}`$, let $`G=\gamma^\omega(0)`$ be its fixed point and $`G'=(\gamma^R)^\omega(2)`$ the fixed point of the reversed morphism $`\gamma^R=[10,2,20]`$. Let $`\lambda=1.7548776662\ldots`$ be the real root of $`x^3-2x^2+x-1`$ and

```math
\mu=2+\frac{1}{\lambda^2-1}=2.4808627161\ldots
```

**Theorem.** For each of the four morphisms $`h`$ of Figure 3 of the journal version the word $`h(G)`$, and for each of the six morphisms $`h`$ of Figure 4 the word $`h(G')`$, has factor complexity $`p(n)=2n+1`$ for all $`n\ge 0`$ and critical exponent exactly $`\mu`$. The supremum defining the critical exponent is not attained. The same holds for the ten morphisms of Figures 1 and 2 of arXiv v3.

This settles Conjecture 19 of the journal version, equivalently Conjecture 1 of arXiv v3, affirmatively for all twenty listed words. Both lists and the wording of the conjecture were compared with the journal PDF and the arXiv v3 HTML on 21 November 2026.

Up to letter permutations, reversal and conjugation of morphisms, the twenty words have only three languages: those of $`G`$, $`U=a_1(G)`$ and $`V=a_4(G)`$, where $`a_1=[210,20,21]`$ and $`a_4=[102,2,1]`$ are rows of Figure 3. Each arXiv morphism is a conjugate of the corresponding journal morphism composed with a power of $`\gamma`$ or $`\gamma^R`$. The morphisms $`\gamma`$, $`a_1`$ and $`a_4`$ factor into letter permutations and elementary insertions $`b\mapsto ab`$ or $`b\mapsto ba`$. Two self-contained lemmas describe how bispecial factors, their extension graphs and their return words change under one insertion. They show that every nonempty bispecial factor of $`G`$, $`U`$ and $`V`$ is ordinary, lying in two explicit orbits or among seven short exceptions, so Cassaigne's formula gives complexity $`2n+1`$. For the critical exponent, the formula $`E(x)=1+\sup_w|w|/|r_w|`$ over bispecial factors $`w`$ and shortest return words $`r_w`$ (Dolce, Dvořáková and Pelantová; a proof is included) reduces the claim to $`|w|\lt(\mu-1)|r|`$ for every return word $`r`$ of every bispecial factor $`w`$, with ratios tending to $`\mu-1`$. Along the orbits these lengths satisfy linear recurrences, and the inequality is proved for each of 72 families by exact arithmetic in $`\mathbb Q(\lambda)`$.

For $`G`$ itself the complexity and the critical exponent are Lemma 28 and Theorem 29 of Shallit and Shur, re-proved in the note by a different route. The papers of Shallit and Shur and of Dolce, Dvořáková and Pelantová were read only through a summarising web tool; no step of the proof depends on them.

## Verification

Run from the repository root with Python 3.10 or later and no other dependencies:

```sh
python3 results/currie-conjecture-19/verify.py
```

Every check is an assertion and the script ends with `ALL CHECKS PASSED`. It checks the morphism identities of the reduction and the conjugating words for the arXiv rows (S1); the primitivity of $`\gamma`$ and exact factor sets of $`G`$ (S2); the hypotheses of the insertion lemmas along the three chains, the seeds, the explicit forms of the orbits and the short extra bispecial factors (S3); and the exact inequalities in $`\mathbb Q(\lambda)`$ for the 72 families and the seven extra words (S6). As cross-checks, it compares the bispecial factors of $`G`$, $`U`$ and $`V`$ given by the lemmas with an exhaustive enumeration up to length 300 (S4), checks $`p(n)=2n+1`$ for $`n\le 300`$ for $`G`$, $`G'`$ and all twenty images (S5), and searches prefixes of length 60000 for repetitions with period at most 3000, all of exponent below $`\mu`$ (S7). It takes about 15 seconds on an idle core and about 50 seconds under load. An optional argument raises the length bound 300 of S4 and S5; with `600` the script takes a few minutes.

The theorem rests on the written proof together with the finite computations listed in it, which `verify.py` reproduces. The brute-force sections cover bounded lengths and prefixes only.

Optional checks, not run by CI: [`review/`](review) contains the standard-library scripts of the referee pass, which the referee wrote from scratch, independently of `verify.py`. They are run from that folder. [`reduction.py`](review/reduction.py) checks the identities of the reduction and the complexity of all twenty images; [`bisp.py`](review/bisp.py) compares all bispecial factors of $`G`$, $`U`$ and $`V`$ of bounded length with the note's description; [`crit.py`](review/crit.py) checks $`|w|\lt(\mu-1)|r|`$ along every family with a certified enclosure of $`\lambda`$; [`lemma_test.py`](review/lemma_test.py) tests the insertion lemmas by brute force on fixed points of several primitive morphisms, including words with non-ordinary bispecial factors (a test, not a certificate); [`common.py`](review/common.py) holds shared helpers. Two further referee scripts need numpy and are not included.

## Files

- [`PROOF.md`](PROOF.md): statement, reduction to three words, lemmas, proof, verification summary, referee pass and sources.
- [`verify.py`](verify.py): standard-library check of the computer-assisted steps, with brute-force cross-checks.
- [`review/`](review): the referee pass's independent scripts.
