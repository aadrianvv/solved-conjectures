# Johnson–Kaya–Matzke conjecture on Babai spectra of paths

[Catalogue](../../CONTENTS.md) · [Proof](PROOF.md) · [Brute-force checks](verify.py) · [Issue #146](https://github.com/1337isnot1337/solved-conjectures/issues/146)

**Status:** Elementary written proof, checked by brute force for $`n\le 14`$. It settles Conjecture 2.1 of Johnson, Kaya and Matzke for every $`n`$. The note is unrefereed.

**Lean status:** none. No Lean formalization is included.

Primary source: P. Johnson, C. Kaya and R. W. Matzke, *Babai numbers and Babai spectra of paths and cycles*, [arXiv:2409.04869](https://arxiv.org/abs/2409.04869), Conjecture 2.1.

## Result

For a finite connected graph $`H`$ and a set $`D\subseteq\{1,\dots,\mathop{\mathrm{diam}}H\}`$, let $`\chi(H,D)`$ be the chromatic number of the graph on $`V(H)`$ in which two vertices are adjacent when their distance in $`H`$ lies in $`D`$. The Babai $`k`$-spectrum $`\mathop{\mathrm{Spec}}(H,k)`$ is the set of the values $`\chi(H,D)`$ with $`|D|=k`$. For the path $`P_n`$ with vertices $`1,\dots,n`$, every $`n\ge 2`$ and every $`1\le k\le n-1`$,

```math
\mathop{\mathrm{Spec}}(P_n,k)=\Big\{\Big\lceil \frac{n}{n-k}\Big\rceil,\ \Big\lceil \frac{n}{n-k}\Big\rceil+1,\ \dots,\ k+1\Big\}.
```

For $`k\le n/2`$ the lower end is 2 and this is Theorem 2.2 of Johnson, Kaya and Matzke. For $`\lfloor n/2\rfloor\lt k\le n-1`$ it is exactly their Conjecture 2.1. They proved the inclusion "$`\supseteq`$" and left "$`\subseteq`$" open.

The missing inclusion follows from a bound on independent sets. If $`S`$ is independent in the distance graph, the differences $`x-\min S`$ with $`x\in S\setminus\{\min S\}`$ are $`|S|-1`$ distinct elements of $`\{1,\dots,n-1\}`$ outside $`D`$, so $`|S|\le n-k`$. Hence at least $`\lceil n/(n-k)\rceil`$ colours are needed. Greedy colouring gives the upper bound $`k+1`$, and every value in between is attained by the construction of Johnson, Kaya and Matzke. The closed form $`\lceil n/(n-k)\rceil`$ covers both ranges of $`k`$ at once.

A literature search on 21 November 2026 found no later paper or arXiv version containing this argument.

## Verification

Run from the repository root with Python 3.10 or later and no other dependencies:

```sh
python3 results/babai-spectrum-paths/verify.py
```

The script computes $`\chi(P_n,D)`$ for every distance set with $`2\le n\le 14`$, 16,369 sets in all. It checks that the values for each $`(n,k)`$ form the interval of the theorem. It also checks the independence bound by exhaustive search for $`n\le 10`$, and the integer $`m`$ of Johnson–Kaya–Matzke's Theorem 2.3 against the closed form. It takes a few seconds and prints one line per $`n`$. An optional argument raises the bound on $`n`$.

The theorem for general $`n`$ rests on the written proof; the script confirms it in the stated range.

## Files

- [`PROOF.md`](PROOF.md): statement, lemmas, proof and sources.
- [`verify.py`](verify.py): standard-library brute-force check.
