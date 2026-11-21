# The Babai k-spectrum of a path (Johnson–Kaya–Matzke, Conjecture 2.1)

**Status:** text proof, checked by brute force for $`n\le 14`$. Not formalised.

## Statement

For a finite connected graph $`H`$ and a set $`D\subseteq\{1,\dots,\mathop{\mathrm{diam}}H\}`$, let $`\chi(H,D)`$ be the chromatic number of the graph on $`V(H)`$ in which two vertices are adjacent when their distance in $`H`$ lies in $`D`$. The Babai $`k`$-spectrum is

```math
\mathop{\mathrm{Spec}}(H,k)=\{\chi(H,D): D\subseteq\{1,\dots,\mathop{\mathrm{diam}}H\},\ |D|=k\}.
```

Take the path $`P_n`$ with vertices $`1,\dots,n`$, so that the distance is $`|u-v|`$ and the diameter is $`n-1`$. [JKM, Definitions 1.1 and 1.2]

**Theorem.** For all integers $`n\ge 2`$ and $`1\le k\le n-1`$,

```math
\mathop{\mathrm{Spec}}(P_n,k)=\Big\{\Big\lceil \frac{n}{n-k}\Big\rceil,\ \Big\lceil \frac{n}{n-k}\Big\rceil+1,\ \dots,\ k+1\Big\}.
```

For $`k\le n/2`$ the lower end is 2, and the statement is [JKM, Theorem 2.2]. For $`\lfloor n/2\rfloor\lt k\le n-1`$ the lower end equals $`m+1`$, where $`m`$ is the integer of [JKM, Theorem 2.3] (Lemma 4 below), so the statement is exactly **Conjecture 2.1 of Johnson, Kaya and Matzke**. They proved the inclusion "$`\supseteq`$" and left "$`\subseteq`$" open.

## Proof

Write $`G_D`$ for the graph on $`\{1,\dots,n\}`$ with $`u\sim v`$ when $`|u-v|\in D`$, and let $`|D|=k`$.

**Lemma 1 (independent sets).** Every independent set $`S`$ of $`G_D`$ has $`|S|\le n-k`$.

*Proof.* Let $`a=\min S`$. The numbers $`x-a`$ for $`x\in S\setminus\{a\}`$ are $`|S|-1`$ distinct elements of $`\{1,\dots,n-1\}`$, and none of them lies in $`D`$. So $`|S|-1\le (n-1)-k`$. ∎

**Lemma 2 (lower bound).** $`\chi(P_n,D)\ge\lceil n/(n-k)\rceil`$.

*Proof.* The colour classes are independent, so by Lemma 1 a proper colouring with $`c`$ colours covers at most $`c(n-k)`$ vertices. ∎

**Lemma 3 (upper bound).** $`\chi(P_n,D)\le k+1`$. [JKM, Theorem 2.1]

*Proof.* Colour $`1,2,\dots,n`$ in this order. A vertex $`v`$ has at most $`k`$ neighbours among the earlier vertices, namely the $`v-d`$ with $`d\in D`$, so one of $`k+1`$ colours is free. ∎

**Lemma 4 (the integer $`m`$ of the conjecture).** Let $`\lfloor n/2\rfloor\lt k\le n-1`$ and let $`m`$ be an integer with $`n-\lceil n/m\rceil\lt k\le n-\lceil n/(m+1)\rceil`$. Then $`\lceil n/(n-k)\rceil=m+1`$.

*Proof.* The right inequality gives $`n-k\ge n/(m+1)`$, so $`n/(n-k)\le m+1`$. The left one gives $`n-k\lt\lceil n/m\rceil`$, so $`n-k\le\lceil n/m\rceil-1\lt n/m`$ and $`n/(n-k)\gt m`$. ∎

**Lemma 5 (every value occurs).** Let $`\lceil n/(n-k)\rceil\le s\le k+1`$. Then there is a set $`D`$ with $`|D|=k`$ and $`\chi(P_n,D)=s`$.

*Proof.* This is the construction used in [JKM, proofs of Theorems 2.2 and 2.3]. The number of multiples of $`s`$ in $`\{1,\dots,n-1\}`$ is $`\lfloor (n-1)/s\rfloor`$. Since $`s\ge n/(n-k)`$, we have $`(n-1)/s\le (n-1)(n-k)/n\lt n-k`$, so there are at most $`n-k-1`$ such multiples and at least $`k`$ integers in $`\{1,\dots,n-1\}`$ that are not divisible by $`s`$. Because $`s-1\le k`$, we can choose $`D`$ of size $`k`$ consisting of $`1,\dots,s-1`$ and $`k-s+1`$ further integers not divisible by $`s`$. Then $`v\mapsto v \bmod s`$ is a proper colouring of $`G_D`$, as no element of $`D`$ is divisible by $`s`$. The vertices $`1,\dots,s`$ are pairwise adjacent, as their differences lie in $`\{1,\dots,s-1\}\subseteq D`$, and $`s\le k+1\le n`$. So $`\chi(P_n,D)=s`$. ∎

**Proof of the Theorem.** Lemmas 2 and 3 give "$`\subseteq`$" and Lemma 5 gives "$`\supseteq`$". ∎

**Remark (the bounds of Lemmas 1 and 2 are attained by one explicit set).** For $`D=\{n-k,\dots,n-1\}`$ the set $`\{1,\dots,n-k\}`$ is independent, and the colouring $`v\mapsto\lceil v/(n-k)\rceil`$ is proper with $`\lceil n/(n-k)\rceil`$ colours.

## What is new

- The inclusion "$`\subseteq`$" for $`k\gt n/2`$, that is Lemmas 1 and 2. With [JKM, Theorem 2.3] this settles Conjecture 2.1.
- The closed form $`\lceil n/(n-k)\rceil`$ for the lower end, which covers both ranges of $`k`$ at once.

The argument is short. We found no later paper or later arXiv version that contains it (searched 21 November 2026).

## Verification

`python3 verify.py 14` computes $`\chi(P_n,D)`$ for every $`D`$ with $`2\le n\le 14`$ (16,369 distance sets) and checks that the set of values for each $`(n,k)`$ is the interval of the Theorem. It also checks Lemma 1 by exhaustive search for $`n\le 10`$ and Lemma 4 against the definition of $`m`$ in the paper. Standard library only; it takes a few seconds.

## Sources

- **[JKM]** P. Johnson, C. Kaya and R. W. Matzke, *Babai numbers and Babai spectra of paths and cycles*, [arXiv:2409.04869](https://arxiv.org/abs/2409.04869) (August 2024). Definitions 1.1 and 1.2, Theorems 2.1 to 2.3, Conjecture 2.1.
