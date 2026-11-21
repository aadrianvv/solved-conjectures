# Conjecture 19 of Currie (EJC 33(3) #P3.31): complexity 2n+1 and critical exponent mu for the listed morphic images

Status: **proved** -- text proof, computer-assisted in finitely many described places (all reproduced by `verify.py`), one independent model referee pass, not formalised.
Both versions of the conjecture (journal Conjecture 19, arXiv v3 Conjecture 1) are covered.

## Statement

Alphabet $`A=\{0,1,2\}`$. A morphism $`h`$ is written $`[h(0),h(1),h(2)]`$, and $`h^R=[h(0)^R,h(1)^R,h(2)^R]`$.
Let

```math
\gamma=[01,2,02],\qquad G=\gamma^\omega(0)=0120201020120102012\cdots,\qquad \gamma^R=[10,2,20],\qquad G'=(\gamma^R)^\omega(2)=2010210202\cdots .
```

Let $`\lambda=1.7548776662\ldots`$ be the real root of $`x^3-2x^2+x-1`$ and

```math
\mu = 2+\frac{1}{\lambda^2-1}=2.4808627161\ldots,\qquad \alpha:=\mu-1=\frac{3-\lambda+2\lambda^2}{5}=1.4808627161\ldots
```

(the last identity holds in $`\mathbb Q(\lambda)`$ and is checked exactly in `verify.py`).

**Theorem.** For every morphism $`h`$ of Figure 3 of [Cu-EJC] the word $`h(G)`$, and for every morphism $`h`$ of
Figure 4 the word $`h(G')`$, has factor complexity $`p(n)=2n+1`$ for all $`n\ge 0`$ and critical exponent exactly $`\mu`$
(the supremum is not attained). The same holds for the morphisms of Figures 1 and 2 of arXiv:2507.09387v3.

Figure 3 (applied to $`G`$): $`a_1=[210,20,21]`$, $`a_2=[02,021,02121]`$, $`a_3=[2,0,1]`$, $`a_4=[102,2,1]`$.
Figure 4 (applied to $`G'`$): $`b_1=[2,0,1]`$, $`b_2=[0,2,21]`$, $`b_3=[1,0,2]`$, $`b_4=[12,012,01012]`$, $`b_5=[201,21,01]`$, $`b_6=[102,1,2]`$.
arXiv v3, Figure 1 (applied to $`G`$): $`[1210202, 12102, 1210202102]`$, $`[1210202102, 1210202, 121020210202]`$, $`[021201212, 0212012, 021201212012]`$, $`[21021102211021102, 2102110221102, 2102110221102110221102]`$.
arXiv v3, Figure 2 (applied to $`G'`$): $`[10212, 0212, 0210212]`$, $`[2120210, 20210, 202120210]`$, $`[121201210, 1201210, 120121201210]`$, $`[1201212010, 1212010, 121201212010]`$, $`[1212010, 12010, 1201212010]`$, $`[221102210, 21102210, 2110221102210]`$.

Both lists, the definitions of $`\gamma`$, $`G`$, $`\gamma^R`$, $`G'`$ and the wording of the conjecture were compared on 21 November 2026 with the text of the
journal PDF (Section 7, Figures 3 and 4, Conjecture 19) and of the arXiv v3 HTML (Figures 1 and 2, Conjecture 1). The two lists are also consistent
with each other in the strong sense of Section "Reduction", step R5 (each arXiv row is a conjugate of the
corresponding journal row composed with a power of $`\gamma`$ or $`\gamma^R`$).

For $`G`$ itself, $`p_G(n)=2n+1`$ and $`E(G)=\mu`$ are Lemma 28 and Theorem 29 of Shallit and Shur [SS]†; we re-prove both below
because the proof for the images needs the full list of bispecial factors of $`G`$ anyway.

## Reduction

**Notation.** For an infinite word $`x`$, $`\mathcal L(x)`$ is its set of factors, $`p_x(n)`$ the number of factors of length $`n`$,
and $`E(x)=\sup\{|z|/q : z\in\mathcal L(x)\setminus\{\varepsilon\},\ q\ \text{a period of}\ z\}`$ its critical exponent
(a period of $`z`$ is an integer $`1\le q\le |z|`$ with $`z_i=z_{i+q}`$ for $`0\le i\lt |z|-q`$). For a set of words $`S`$, $`\mathrm{Fact}(S)`$
is the set of factors of elements of $`S`$, and $`S^R=\{s^R: s\in S\}`$.

**R1 (invariance).** $`p_x`$ and $`E(x)`$ depend only on $`\mathcal L(x)`$; they do not change if $`\mathcal L(x)`$ is replaced by
$`\pi(\mathcal L(x))`$ for a letter permutation $`\pi`$, or by $`\mathcal L(x)^R`$ (reversal is a length-preserving bijection of
$`\mathcal L(x)`$ onto $`\mathcal L(x)^R`$ and $`q`$ is a period of $`z`$ iff it is a period of $`z^R`$).
For every morphism $`h`$ and every word $`x`$, $`\mathcal L(h(x))=\mathrm{Fact}(h(\mathcal L(x)))`$ (any factor of $`h(x)`$ lies in the image of a factor of $`x`$),
and $`h(u)^R=h^R(u^R)`$, hence $`\mathrm{Fact}(h(S))^R=\mathrm{Fact}(h^R(S^R))`$.

**R2 ($`\mathcal L(G')=\mathcal L(G)^R`$).** $`\gamma^R(u)=(\gamma(u^R))^R`$, so $`(\gamma^R)^n(2)=(\gamma^n(2))^R`$. The incidence matrix of
$`\gamma`$ has positive cube (`verify.py` S2), so $`\gamma^3(c)`$ contains every letter for every $`c`$; hence
$`\mathcal L(G)=\bigcup_n\mathrm{Fact}(\gamma^n(0))=\bigcup_n\mathrm{Fact}(\gamma^n(2))`$, and
$`\mathcal L(G')=\bigcup_n\mathrm{Fact}((\gamma^R)^n(2))=\mathcal L(G)^R`$.

**R3 (two exact identities between $`G`$ and $`G'`$).** Put $`c_1=[0,2,01]`$, $`c_2=[2,1,01]`$, $`\tau=(0\,1)`$. Then $`c_1c_2=\gamma`$ and
$`c_2c_1=[2,01,21]=\tau\gamma^R\tau`$. Since $`G=c_1(c_2(G))`$, the word $`c_2(G)`$ is a fixed point of $`c_2c_1=\tau\gamma^R\tau`$ beginning with
$`c_2(0)=2`$; a fixed point of $`\tau\gamma^R\tau`$ beginning with $`2`$ is unique (its image of $`2`$ is $`21`$, of length $`\ge 2`$), and
$`\tau(G')`$ is one; so $`c_2(G)=\tau(G')`$. Therefore

```math
G'=\tau c_2(G)=[2,0,10](G),\qquad G=c_1(c_2(G))=c_1\tau(G')=[2,0,01](G').
```

**R4 (conjugate morphisms).** Let $`h,h'`$ be morphisms and $`u`$ a word with $`h'(c)\,u=u\,h(c)`$ for every letter $`c`$, such that $`u`$ is a prefix of
every $`h'(c)`$ and a suffix of every $`h(c)`$. Let $`\mathcal L`$ be the language of a recurrent infinite word. Then
$`\mathrm{Fact}(h(\mathcal L))=\mathrm{Fact}(h'(\mathcal L))`$.
*Proof.* By induction $`h'(z)u=uh(z)`$ for every word $`z`$. For $`z\in\mathcal L`$ pick letters $`d,e`$ with $`zd, ez\in\mathcal L`$ (recurrence).
$`h'(zd)=h'(z)h'(d)`$ has the prefix $`h'(z)u=uh(z)`$, so $`h(z)\in\mathrm{Fact}(h'(\mathcal L))`$; $`h(ez)=h(e)h(z)`$ has the suffix
$`uh(z)=h'(z)u`$, so $`h'(z)\in\mathrm{Fact}(h(\mathcal L))`$. $`\square`$

**R5 (the list reduces to three words).** Let $`\sigma=(0\,2)`$, $`\varrho=(1\,2)`$ and $`\pi_0=[2,0,1]`$ (as letter maps). The following identities of
morphisms are checked character by character in `verify.py` S1:

```math
a_3=b_1=\pi_0,\quad b_3=\tau,\quad b_6=\varrho\circ a_4^R,\quad b_5=\pi_0\circ a_1^R,\quad b_4=\pi_0\circ a_2^R,\quad b_2=\sigma\circ[2,0,01],
```

```math
a_2^R\circ[2,0,10]=[12120,20,12020],\qquad (\tau\circ a_1)\circ\gamma=[20121,20,20120],
```

and $`[20121,20,20120]`$, $`[12120,20,12020]`$ satisfy the hypothesis of R4 with $`u=20`$. Put $`U=a_1(G)`$ and $`V=a_4(G)`$. Using R1-R4:

* $`a_3(G)=\pi_0(G)`$; $`b_1(G')=\pi_0(G')`$ and $`b_3(G')=\tau(G')`$ have the language $`\pi(\mathcal L(G)^R)`$; $`b_2(G')=\sigma([2,0,01](G'))=\sigma(G)`$.
* $`\mathcal L(b_6(G'))=\varrho(\mathrm{Fact}(a_4^R(\mathcal L(G)^R)))=\varrho(\mathcal L(V)^R)`$, and likewise $`\mathcal L(b_5(G'))=\pi_0(\mathcal L(U)^R)`$.
* $`\mathcal L(a_2(G))^R=\mathrm{Fact}(a_2^R(\mathcal L(G')))=\mathrm{Fact}(a_2^R[2,0,10](\mathcal L(G)))=\mathrm{Fact}(\tau a_1\gamma(\mathcal L(G)))=\tau(\mathcal L(U))`$,
  using R3, R4 and $`\mathrm{Fact}(\gamma(\mathcal L(G)))=\mathcal L(G)`$. Then $`\mathcal L(b_4(G'))=\pi_0(\mathcal L(a_2(G))^R)=\pi_0\tau(\mathcal L(U))`$.
* arXiv v3: for each row $`h`$ of its Figure 1 (resp. 2), `verify.py` S1 finds a word $`u`$ such that $`h`$ and $`h_j\circ\gamma^k`$ (resp. $`h_j\circ(\gamma^R)^k`$)
  satisfy the hypothesis of R4 (in one of the two orders), with $`(j,k)=(1,2),(2,2),(3,4),(4,4)`$ for Figure 1 (where $`h_j=a_j`$) and
  $`(1,3),(2,3),(3,4),(4,2),(5,2),(6,3)`$ for Figure 2 (where $`h_j=b_j`$). Since $`\gamma^k(G)=G`$ and $`(\gamma^R)^k(G')=G'`$, each arXiv word has
  the same language as the corresponding journal word.

Hence, by R1, **the Theorem is equivalent to: $`G`$, $`U=a_1(G)`$ and $`V=a_4(G)`$ have complexity $`2n+1`$ and critical exponent $`\mu`$**
(classes: $`G`$: $`a_3,b_1,b_2,b_3`$; $`U`$: $`a_1,a_2,b_4,b_5`$; $`V`$: $`a_4,b_6`$).

**Elementary decompositions.** For distinct letters $`a,b`$ let $`\mathrm L_{ab}`$ (left insertion) and $`\mathrm R_{ab}`$ (right insertion) be the morphisms

```math
\mathrm L_{ab}:\ b\mapsto ab,\qquad \mathrm R_{ab}:\ b\mapsto ba,\qquad c\mapsto c\ \ (c\ne b),
```

and $`f_{ab}:A\to A`$ the letter map $`b\mapsto a`$, $`c\mapsto c`$ ($`c\ne b`$). Writing letter permutations as words $`[\pi(0)\pi(1)\pi(2)]`$, one checks directly (and `verify.py` S1):

```math
\gamma=[120]\circ\mathrm L_{20}\circ\mathrm R_{12},\qquad a_4=[021]\circ\mathrm R_{10}\circ\mathrm L_{20},\qquad a_1=[021]\circ\mathrm L_{12}\circ\mathrm R_{01}\circ\mathrm L_{20}.
```

## Lemmas

Throughout, $`x`$ is a uniformly recurrent infinite word over $`A`$ in which all three letters occur, $`\mathcal L=\mathcal L(x)`$. For $`w\in\mathcal L`$:

```math
E^-(w)=\{e: ew\in\mathcal L\},\quad E^+(w)=\{d: wd\in\mathcal L\},\quad E(w)=\{(e,d): ewd\in\mathcal L\},\quad m(w)=|E(w)|-|E^-(w)|-|E^+(w)|+1 .
```

$`w`$ is *bispecial* if $`|E^\pm(w)|\ge 2`$; *ordinary* if moreover $`|E^-(w)|=|E^+(w)|=2`$ and $`|E(w)|=3`$ (then $`m(w)=0`$).
$`\mathrm{Bisp}^*(x)`$ is the set of nonempty bispecial factors. A *return word* to $`w`$ is $`x[i,j)`$ for two consecutive occurrences $`i\lt j`$
of $`w`$ in $`x`$; equivalently, $`r`$ is a return word to $`w`$ iff $`rw\in\mathcal L`$, $`w`$ is a prefix of $`rw`$ and $`rw`$ has exactly two
occurrences of $`w`$ (so the set $`\mathrm{Ret}(w)`$ depends only on $`\mathcal L`$; it is finite by uniform recurrence).
$`\Psi(v)`$ denotes the Parikh vector $`(|v|_0,|v|_1,|v|_2)^T`$, $`M_h`$ the incidence matrix of $`h`$ (column $`c`$ is $`\Psi(h(c))`$), so $`\Psi(h(v))=M_h\Psi(v)`$.

**Lemma 1 (Cassaigne's formula).** Let $`s(n)=p(n+1)-p(n)`$. Then $`s(n+1)-s(n)=\sum_{|w|=n}m(w)`$, and $`m(w)=0`$ unless $`w`$ is bispecial.
Consequently, if all three letters occur and $`m(w)=0`$ for every bispecial $`w`$ (including $`\varepsilon`$), then $`p(n)=2n+1`$ for all $`n`$.
*Proof.* Every factor of length $`n+1`$ is uniquely $`wd`$ with $`d\in E^+(w)`$, so $`s(n)=\sum_{|w|=n}(|E^+(w)|-1)`$. Every factor of length $`n+1`$ is
uniquely $`ew`$, $`e\in E^-(w)`$, and $`E^+(ew)=\{d:(e,d)\in E(w)\}`$; hence $`s(n+1)=\sum_{|w|=n}\sum_{e\in E^-(w)}(|E^+(ew)|-1)=\sum_{|w|=n}(|E(w)|-|E^-(w)|)`$.
Subtracting gives the formula. If $`|E^-(w)|=1`$ then $`|E(w)|=|E^+(w)|`$, so $`m(w)=0`$; symmetrically if $`|E^+(w)|=1`$. Finally $`p(0)=1`$,
$`p(1)=3`$, so $`s(0)=2`$ and $`s\equiv 2`$. $`\square`$

**Lemma 2 (exact factor sets, used by `verify.py`).** Let $`n\ge 1`$ and let $`S`$ be a set of words of length $`n`$ such that (a) $`S`$ contains the
length-$`n`$ factors of $`\gamma^k(0)`$ for every $`k\ge0`$ with $`k=0`$ or $`|\gamma^{k-1}(0)|\lt n`$, and (b) every length-$`n`$ factor of $`\gamma(v)`$, $`v\in S`$,
lies in $`S`$. Then $`S\supseteq\mathcal L_n(G)`$; if $`S`$ is the set of length-$`n`$ factors of a prefix of $`G`$, then $`S=\mathcal L_n(G)`$.
*Proof.* A factor $`f`$ of length $`n`$ of $`G`$ is a factor of some $`\gamma^k(0)`$; induct on $`k`$. If $`k=0`$ or $`|\gamma^{k-1}(0)|\lt n`$ use (a). Otherwise $`f`$
lies in $`\gamma(t)`$ for a factor $`t`$ of $`\gamma^{k-1}(0)`$ with $`|t|\le n`$ (each letter of $`t`$ contributes at least one letter to $`f`$);
extend $`t`$ inside $`\gamma^{k-1}(0)`$ to a factor $`t'`$ of length exactly $`n`$; $`t'\in S`$ by induction and $`f\in S`$ by (b). $`\square`$
The factors of length $`n`$ of $`h(G)`$ are the length-$`n`$ factors of $`h(v)`$, $`v\in\mathcal L_n(G)`$ (images are nonempty). By hand, $`n=2`$:
$`\gamma(01)=012`$, $`\gamma(02)=0102`$, $`\gamma(10)=201`$, $`\gamma(12)=202`$, $`\gamma(20)=0201`$ give

```math
\mathcal L_2(G)=\{01,02,10,12,20\},\qquad\text{so}\quad E^+(2)=\{0\},\ E^-(1)=\{0\},\ E^+(1)=\{2\},\ E^-(2)=\{0,1\},\ E^\pm(0)=\{1,2\}.
```

**Lemma 3 (critical exponent via bispecial factors; Dolce-Dvořáková-Pelantová [DDP, Thm 3]†).** If $`x`$ is uniformly recurrent and not periodic,

```math
E(x)=1+\sup\Big\{\frac{|w|}{|r_w|}:\ w\ \text{bispecial factor of}\ x,\ r_w\ \text{a shortest return word to}\ w\Big\}.
```

*Proof (self-contained).* ($`\ge`$) If $`r`$ is a shortest return word to $`w`$, $`w`$ occurs at $`i`$ and $`i+|r|`$, so $`z=x[i,i+|r|+|w|)`$ has period $`|r|`$
and $`|z|/|r|=1+|w|/|r|`$. ($`\le`$) Let $`z\in\mathcal L(x)`$ have period $`q`$, $`|z|\gt q`$ (if $`|z|\le q`$ the ratio is $`\le 1`$). As $`x`$ is not periodic,
there is $`i_0`$ with $`x_{i_0}\ne x_{i_0+q}`$. Take an occurrence of $`z`$ at a position $`i\gt i_0+q`$ (recurrence) and the maximal interval
$`[s,t)\supseteq[i,i+|z|)`$ on which $`x`$ has period $`q`$. It is finite on the right: otherwise $`x[s,\infty)`$ has period $`q`$; every prefix of $`x`$ occurs in $`x[s,\infty)`$ (recurrence), so every prefix of $`x`$ has period $`q`$ and $`x`$ is periodic. And $`s\ge 1`$: otherwise $`[0,t)\ni i_0,i_0+q`$. Put $`w=x[s,t-q)`$. Then $`w`$ occurs at $`s`$ and
at $`s+q`$; by maximality $`x_{s-1}\ne x_{s-1+q}`$ and $`x_{t-q}\ne x_t`$, so $`w`$ is left and right special. Occurrences at distance $`q`$ give
$`|r_w|\le q`$, so $`|z|/q\le (t-s)/q=1+|w|/q\le 1+|w|/|r_w|`$. $`\square`$

**Lemma 4 (left insertion).** Let $`a\ne b`$, $`h=\mathrm L_{ab}`$, $`f=f_{ab}`$, $`y=h(x)`$, and assume

```math
\text{(H)}\qquad E^+_x(a)=\{a^+\}\ \text{is a single letter.}
```

(a) The nonempty bispecial factors of $`y`$ are exactly the following words, and they are pairwise distinct:
 (i) $`h(u)`$, for $`u\in\mathrm{Bisp}^*(x)`$ with $`|f(E^+(u))|\ge 2`$; then $`E_y(h(u))=\{(e,f(d)):(e,d)\in E_x(u)\}`$;
 (ii) $`h(u)a`$, for $`u\in\mathcal L(x)`$ (possibly empty) with $`\{a,b\}\subseteq E^+(u)`$ and $`|E^-(ua)\cup E^-(ub)|\ge 2`$; then

```math
E_y(h(u)a)=\{(e,f(a^+)):(e,a)\in E_x(u)\}\cup\{(e,b):(e,b)\in E_x(u)\}.
```

(b) Let $`u\in\mathrm{Bisp}^*(x)`$ be ordinary. Put $`\Lambda_h(u)=h(u)a`$ if $`E^+(u)=\{a,b\}`$ and $`\Lambda_h(u)=h(u)`$ otherwise. Then $`\Lambda_h(u)`$ is
the only one of $`h(u),h(u)a`$ that is bispecial in $`y`$; it is ordinary, $`E^-_y(\Lambda_h(u))=E^-_x(u)`$, and
$`\mathrm{Ret}_y(\Lambda_h(u))=h(\mathrm{Ret}_x(u))`$ (bijectively). Moreover $`|u|\le|\Lambda_h(u)|\le 2|u|+1`$, and $`\Lambda_h`$ is injective.

(c) If every non-ordinary word of $`\mathrm{Bisp}^*(x)`$ has length $`\le m`$ ($`m=0`$ if there is none), then every $`v\in\mathrm{Bisp}^*(y)`$ that is not of the form
$`\Lambda_h(u)`$ with $`u\in\mathrm{Bisp}^*(x)`$ ordinary has length $`\le 2m+1`$; for $`m=0`$ the only possible such $`v`$ is the letter $`a`$, and $`a`$ is bispecial in $`y`$
iff $`|E^-_x(a)\cup E^-_x(b)|\ge 2`$.

*Proof.* Write $`y=h(x_0)h(x_1)\cdots`$ and call $`|h(x_0\cdots x_{i-1})|`$ ($`i\ge 0`$) the *cuts*. The blocks are $`a`$, $`ab`$ and $`c`$
(the third letter). Their first letters are never $`b`$ and their second letters are $`b`$; hence **a position $`p`$ is a cut iff $`y_p\ne b`$**. Every block ends with
the letter it codes ($`h(e)`$ ends with $`e`$), and the first letter of $`h(d)`$ is $`f(d)`$. $`h`$ is injective on words ($`\{a,ab,c\}`$ is a suffix code).

*Factors starting with $`b`$.* An occurrence of $`b`$ at $`p\ge 1`$ is preceded by $`a`$; so a factor starting with $`b`$ has $`E^-=\{a\}`$ and is not left special.

*Desubstitution.* Let $`v`$ be a nonempty factor of $`y`$ not starting with $`b`$, occurring at $`p`$. Then $`p`$ is a cut. If $`v`$ does not end with $`a`$, the position
$`p+|v|`$ is a cut (the last letter of $`v`$ is $`b`$, the end of a block $`ab`$, or the third letter, a whole block); so $`y[p,p+|v|)=h(x[i,j))`$ and, by injectivity,
$`v=h(u)`$ with $`u=x[i,j)`$ independent of the occurrence. Thus the occurrences of $`v`$ are exactly the positions $`|h(x[0,i))|`$, $`i`$ an occurrence of $`u`$
(conversely $`h(u)`$ occurs there). The letter before (when $`p\ge 1`$) is the last letter of $`h(x_{i-1})`$, i.e. $`x_{i-1}`$, the letter after is $`f(x_j)`$. Hence
$`E_y(h(u))=\{(e,f(d)):(e,d)\in E_x(u)\}`$, using that every factor of $`x`$ has occurrences at positions $`\ge1`$ (recurrence).
If $`v`$ ends with $`a`$, that last $`a`$ is at a cut (it is not $`b`$), so $`v=h(u)a`$ where $`y[p,p+|v|-1)=h(x[i,j))`$, $`u=x[i,j)`$, and the block starting at
$`p+|v|-1`$ is $`a`$ or $`ab`$, i.e. $`x_j\in\{a,b\}`$. So the occurrences of $`h(u)a`$ correspond to the occurrences of $`ua`$ and of $`ub`$; the letter after is
$`b`$ in the second case and $`f(x_{j+1})=f(a^+)`$ in the first case, by (H). This gives the formula in (ii); in particular $`E^+_y(h(u)a)\subseteq\{f(a^+),b\}`$, two distinct letters
($`b`$ is not in the image of $`f`$).

*(a).* By the above a nonempty bispecial $`v`$ is either $`h(u)`$ ($`v`$ not ending with $`a`$) or $`h(u)a`$. In the first case $`E^-_y(v)=E^-_x(u)`$ and
$`E^+_y(v)=f(E^+_x(u))`$, so $`v`$ is bispecial iff $`u`$ is left special and $`|f(E^+(u))|\ge 2`$ (which forces $`u`$ right special); $`u\ne\varepsilon`$ since $`v\ne\varepsilon`$.
In the second case $`v`$ is right special iff both $`ua`$ and $`ub`$ occur, and then left special iff $`|E^-(ua)\cup E^-(ub)|\ge2`$. Conversely the words listed are factors with the stated graphs.
Distinctness: by (H) a word ending with $`a`$ has the single right extension $`a^+`$, so a right special $`u`$ in (i) does not end with $`a`$, hence $`h(u)`$ does not end with $`a`$,
while the words in (ii) do; within each family use injectivity of $`\lambda`$.

*(b).* Let $`u`$ be ordinary, $`E^+(u)=\{d_1,d_2\}`$. If $`\{d_1,d_2\}\ne\{a,b\}`$, $`f`$ is injective on $`E^+(u)`$, so $`h(u)`$ is bispecial with a graph isomorphic to
$`E(u)`$, and $`h(u)a`$ is not right special ($`ub`$ or $`ua`$ is missing). If $`E^+(u)=\{a,b\}`$, $`h(u)`$ has $`|f(E^+(u))|=1`$, while $`h(u)a`$ is bispecial:
every $`e\in E^-(u)`$ has an edge to $`a`$ or $`b`$, so $`E^-(ua)\cup E^-(ub)=E^-(u)`$, and its graph is $`E(u)`$ with the right vertex $`a`$ renamed $`f(a^+)`$
($`\ne b`$), again isomorphic. In both cases $`E^-`$ is unchanged. Return words: in both cases the occurrences of $`\Lambda_h(u)`$ are exactly the positions $`|h(x[0,i))|`$
with $`i`$ an occurrence of $`u`$ (in case (ii) because every occurrence of $`u`$ is followed by $`a`$ or $`b`$). This map is increasing, so consecutive occurrences
correspond and the return word between them is $`h(x[i,i'))`$. Length bounds: $`|u|\le|h(u)|\le 2|u|`$. Injectivity: $`\Lambda_h(u)`$ determines whether
it ends with $`a`$, and then $`u`$.

*(c).* By (a), such a $`v`$ is $`h(u)`$ or $`h(u)a`$ with $`u\in\{\varepsilon\}\cup\mathrm{Bisp}^*(x)`$ ($`u`$ in (ii) is left and right special or empty).
If $`u`$ is ordinary and nonempty, (b) gives $`v=\Lambda_h(u)`$. If $`u=\varepsilon`$ then $`v=a`$ (the form (i) needs $`u\ne\varepsilon`$). Otherwise $`u`$ is non-ordinary, $`|u|\le m`$ and $`|v|\le 2m+1`$.
The criterion for $`a`$ is (ii) with $`u=\varepsilon`$. $`\square`$

**Lemma 5 (right insertion).** Let $`a\ne b`$, $`h=\mathrm R_{ab}`$, $`f=f_{ab}`$, $`y=h(x)`$, and assume (H') $`E^-_x(a)=\{a^-\}`$ is a single letter. Then
(a) the nonempty bispecial factors of $`y`$ are exactly, and pairwise distinct: (i) $`h(u)`$, $`u\in\mathrm{Bisp}^*(x)`$, $`|f(E^-(u))|\ge2`$, with
$`E_y(h(u))=\{(f(e),d):(e,d)\in E_x(u)\}`$; (ii) $`a\,h(u)`$, $`u\in\mathcal L(x)`$, $`\{a,b\}\subseteq E^-(u)`$, $`|E^+(au)\cup E^+(bu)|\ge2`$, with

```math
E_y(a\,h(u))=\{(f(a^-),d):(a,d)\in E_x(u)\}\cup\{(b,d):(b,d)\in E_x(u)\}.
```

(b) For ordinary $`u\in\mathrm{Bisp}^*(x)`$ put $`\Lambda_h(u)=a\,h(u)`$ if $`E^-(u)=\{a,b\}`$, else $`h(u)`$. $`\Lambda_h(u)`$ is the only bispecial one of the two, it is ordinary,
$`E^+_y(\Lambda_h(u))=E^+_x(u)`$, $`|u|\le|\Lambda_h(u)|\le 2|u|+1`$, $`\Lambda_h`$ is injective, and there is a bijection $`\mathrm{Ret}_x(u)\to\mathrm{Ret}_y(\Lambda_h(u))`$,
$`r\mapsto r'`$, with $`\Psi(r')=M_h\Psi(r)`$ (in fact $`r'`$ is $`h(r)`$ or a conjugate of it).
(c) As in Lemma 4(c), with $`a`$ bispecial in $`y`$ (when $`m=0`$) iff $`|E^+_x(a)\cup E^+_x(b)|\ge2`$.

*Proof.* By reversal. $`\mathcal L^R`$ is factorial, extendable and uniformly recurrent, so it is the language of a uniformly recurrent word $`\tilde x`$
(take a right-infinite word all of whose prefixes lie in $`\mathcal L^R`$, König; its language is contained in $`\mathcal L^R`$ and, by uniform recurrence, contains it).
Since $`\mathrm R_{ab}(w)^R=\mathrm L_{ab}(w^R)`$, $`\mathcal L(y)^R=\mathrm{Fact}(\mathrm L_{ab}(\mathcal L^R))=\mathcal L(\mathrm L_{ab}(\tilde x))`$. Reversal exchanges
$`E^-`$ and $`E^+`$ (and transposes $`E`$), preserves bispeciality and ordinarity, and maps the complete return words $`rw`$ to $`w`$ bijectively onto the
complete return words $`(rw)^R`$ to $`w^R`$, so the Parikh vectors of return words are preserved. (H') for $`x`$ is (H) for $`\tilde x`$. Apply Lemma 4 to $`\tilde x`$ and reverse; note $`M_{\mathrm R_{ab}}=M_{\mathrm L_{ab}}`$. $`\square`$

**Lemma 6 (letter permutations).** For a permutation $`\pi`$, $`\mathrm{Bisp}^*(\pi(x))=\pi(\mathrm{Bisp}^*(x))`$ with $`E(\pi(w))=(\pi\times\pi)(E(w))`$ and
$`\mathrm{Ret}(\pi(w))=\pi(\mathrm{Ret}(w))`$. (Obvious.)

## Proof

### Step 1: the bispecial factors of $`G`$

Put $`x_1=\mathrm R_{12}(G)`$, $`x_2=\mathrm L_{20}(x_1)`$, so that $`G=\gamma(G)=\pi_1(x_2)`$ with $`\pi_1=[120]`$ ($`0\mapsto1,1\mapsto2,2\mapsto0`$).
Hypotheses: (H') for $`\mathrm R_{12}`$ on $`G`$ holds with $`1^-=0`$ ($`E^-_G(1)=\{0\}`$, Lemma 2); (H) for $`\mathrm L_{20}`$ on $`x_1`$ holds with $`2^+=1`$ (every $`2`$ of $`x_1`$ lies in a block $`\mathrm R_{12}(2)=21`$).
From $`\mathcal L_2(G)`$ one gets $`\mathcal L_2(x_1)=\{01,02,10,12,21\}`$.

For a nonempty ordinary bispecial factor $`w`$ of $`G`$ define $`\Phi(w)=\pi_1(\Lambda_{\mathrm L_{20}}(\Lambda_{\mathrm R_{12}}(w)))`$, where $`\Lambda_{\mathrm R_{12}}`$, $`\Lambda_{\mathrm L_{20}}`$ are the maps of Lemma 5(b) (for $`\mathrm R_{12}`$) and Lemma 4(b) (for $`\mathrm L_{20}`$).
Composing the two case distinctions (Lemma 5(b) leaves $`E^+`$ unchanged, Lemma 4(b) leaves $`E^-`$ unchanged) and using $`\pi_1\mathrm L_{20}\mathrm R_{12}=\gamma`$, $`\pi_1(1)=2`$, $`\pi_1(2)=0`$:

```math
\Phi(w)=s\,\gamma(w)\,t,\qquad s=\begin{cases}2&E^-(w)=\{1,2\}\\ \varepsilon&\text{otherwise}\end{cases},\qquad t=\begin{cases}0&E^+(w)=\{0,2\}\\ \varepsilon&\text{otherwise.}\end{cases}
```

The graphs transform by a relabelling $`E(\Phi(w))=\{(\phi^-(e),\phi^+(d)):(e,d)\in E(w)\}`$ where (from the formulas in Lemmas 4, 5 and $`\pi_1`$)
$`\phi^-`$ is $`1\mapsto1,2\mapsto0`$ if $`E^-(w)=\{1,2\}`$; $`0\mapsto1,1\mapsto2`$ if $`E^-(w)=\{0,1\}`$; $`0\mapsto1,2\mapsto2`$ if $`E^-(w)=\{0,2\}`$; and
$`\phi^+`$ is $`0\mapsto1,2\mapsto2`$ if $`E^+(w)=\{0,2\}`$; $`1\mapsto2,2\mapsto0`$ if $`E^+(w)=\{1,2\}`$; $`0\mapsto0,1\mapsto2`$ if $`E^+(w)=\{0,1\}`$.
The return words of $`\Phi(w)`$ correspond bijectively to those of $`w`$, with $`\Psi(r')=M\Psi(r)`$, where

```math
M=M_\gamma=\begin{pmatrix}1&0&1\\1&0&0\\0&1&1\end{pmatrix},\qquad \det(xI-M)=x^3-2x^2+x-1 .
```

**Proposition 1.** (1) Every nonempty bispecial factor of $`G`$ is ordinary. (2) $`\mathrm{Bisp}^*(G)`$ is the disjoint union of the two orbits
$`\{\Phi^k(20):k\ge0\}`$ ("orbit A") and $`\{\Phi^k(0):k\ge0\}`$ ("orbit B"), with

```math
E(20)=\{(0,1),(1,1),(1,2)\},\ \mathrm{Ret}(20)=\{20,201,2010\};\qquad E(0)=\{(1,2),(2,1),(2,2)\},\ \mathrm{Ret}(0)=\{01,02,012\}.
```

(3) Along orbit A the pair $`(E^-,E^+)`$ alternates $`(\{0,1\},\{1,2\})`$ (k even) and $`(\{1,2\},\{0,2\})`$ (k odd); along orbit B it alternates
$`(\{1,2\},\{1,2\})`$ and $`(\{0,1\},\{0,2\})`$; $`E(\Phi^{k+4}(s))=E(\Phi^k(s))`$. Hence $`\Phi(w)=\gamma(w)`$, $`2\gamma(w)0`$ (orbit A, k even/odd) and
$`2\gamma(w)`$, $`\gamma(w)0`$ (orbit B, k even/odd).

*Proof.* Seeds. By Lemma 5(a)(ii) with $`u=\varepsilon`$, $`1`$ is bispecial in $`x_1`$ ($`E^+_G(1)\cup E^+_G(2)=\{2,0\}`$) with
$`E_{x_1}(1)=\{(f_{12}(0),d):(1,d)\in E_G(\varepsilon)\}\cup\{(2,d):(2,d)\in E_G(\varepsilon)\}=\{(0,0),(0,2),(2,0)\}`$ (ordinary).
By Lemma 4(a)(ii), $`2`$ is bispecial in $`x_2`$ with $`E_{x_2}(2)=\{(e,f_{20}(1)):(e,2)\in E_{x_1}(\varepsilon)\}\cup\{(e,0):(e,0)\in E_{x_1}(\varepsilon)\}=\{(0,1),(1,1),(1,0)\}`$ (ordinary).

(1) Let $`w`$ be a shortest non-ordinary word of $`\mathrm{Bisp}^*(G)`$. The bispecial factors of $`G`$ of length $`\le 2`$ are $`0`$ and $`20`$ (enumeration of $`\mathcal L_4(G)`$), both ordinary, so $`|w|\ge3`$.
$`v=\pi_1^{-1}(w)`$ is non-ordinary bispecial in $`x_2`$. By Lemma 4(a), $`v=\mathrm L_{20}(u)`$ or $`\mathrm L_{20}(u)2`$ with $`u\in\{\varepsilon\}\cup\mathrm{Bisp}^*(x_1)`$;
$`u=\varepsilon`$ gives $`|v|=1`$, and an ordinary nonempty $`u`$ gives the ordinary $`v=\Lambda_{\mathrm L_{20}}(u)`$ (Lemma 4(b)); so $`u`$ is non-ordinary, $`|u|\le|v|`$.
By Lemma 5(a), $`u=\mathrm R_{12}(t)`$ or $`1\mathrm R_{12}(t)`$ with $`t\in\{\varepsilon\}\cup\mathrm{Bisp}^*(G)`$; $`t=\varepsilon`$ gives $`u=1`$, which is ordinary; an ordinary nonempty $`t`$ gives an ordinary $`u`$.
So $`t\in\mathrm{Bisp}^*(G)`$ is non-ordinary and $`|t|\le|u|\le|w|`$, whence $`|t|=|u|=|v|=|w|`$ by minimality. The forms with an added letter are longer, so $`u=\mathrm R_{12}(t)`$ with no $`2`$ in $`t`$, and $`v=\mathrm L_{20}(u)`$ with no $`0`$
in $`u`$, so $`t\in 1^+`$; as $`11\notin\mathcal L(G)`$, $`t=1`$, which is not bispecial ($`E^-(1)=\{0\}`$). Contradiction.

(2) By (1) and Lemma 5(c) with $`m=0`$: $`\mathrm{Bisp}^*(x_1)=\Lambda_{\mathrm R_{12}}(\mathrm{Bisp}^*(G))\sqcup\{1\}`$, all ordinary. By Lemma 4(c) with $`m=0`$:
$`\mathrm{Bisp}^*(x_2)=\Lambda_{\mathrm L_{20}}(\mathrm{Bisp}^*(x_1))\sqcup\{2\}`$. Applying $`\pi_1`$ (Lemma 6):

```math
\mathrm{Bisp}^*(G)=\Phi(\mathrm{Bisp}^*(G))\ \sqcup\ \{\pi_1(\Lambda_{\mathrm L_{20}}(1)),\ \pi_1(2)\}=\Phi(\mathrm{Bisp}^*(G))\sqcup\{20,\,0\},
```

since $`E^+_{x_1}(1)=\{0,2\}`$ gives $`\Lambda_{\mathrm L_{20}}(1)=\mathrm L_{20}(1)2=12`$. $`\Phi`$ is injective. For $`w\in\mathrm{Bisp}^*(G)`$ we have $`w\ne1`$, so $`w`$ contains $`0`$ or $`2`$ and
$`|\Phi(w)|\ge|\gamma(w)|=|w|+|w|_0+|w|_2\gt|w|`$. By induction on the length, every element of $`\mathrm{Bisp}^*(G)`$ is $`\Phi^k(s)`$ for a unique $`s\in\{20,0\}`$ and $`k\ge0`$.
The graphs of the seeds: $`E(20)`$ is the image of $`E_{x_2}(12)`$, $`E(0)=\pi_1(E_{x_2}(2))`$, as displayed. Return words: $`\mathrm{Ret}(0)=\{01,02,012\}`$ because after
$`0`$ comes $`1`$ or $`2`$, after $`1`$ comes $`0`$ or $`2`$ and after $`2`$ comes $`0`$ (Lemma 2), and $`010,0120,020`$ all occur in the prefix $`0120201020`$; $`\mathrm{Ret}(20)`$
is obtained by Lemmas 4(b) and 6 as $`\pi_1(\mathrm L_{20}(\mathrm{Ret}_{x_1}(1)))`$, where $`\mathrm{Ret}_{x_1}(1)`$ was enumerated from the exact factor set
$`\mathcal L_{60}(x_1)`$ (`verify.py` S3); `verify.py` S4 compares the result with a direct enumeration in $`G`$, and the three words are visible in the prefix $`012020102012010201`$.
(3) follows from (2) and the relabelling rules (finite check, `verify.py` S3). $`\square`$

The first bispecial factors of $`G`$ (lengths $`1,2,3,4,6,9,12,16,22,30,40,53,71,95,126,\ldots`$), with the lengths of their three return words:

| $`\lvert w\rvert`$ | orbit, k | $`E^-`$ | $`E^+`$ | return-word lengths | $`\lvert w\rvert/\lvert r_{\min}\rvert`$ | $`w`$ |
|---|---|---|---|---|---|---|
| 1 | B,0 | 12 | 12 | 2,2,3 | 0.5 | `0` |
| 2 | A,0 | 01 | 12 | 2,3,4 | 1 | `20` |
| 3 | B,1 | 01 | 02 | 3,4,5 | 1 | `201` |
| 4 | A,1 | 12 | 02 | 4,5,7 | 1 | `0201` |
| 6 | B,2 | 12 | 12 | 5,7,9 | 1.2 | `020120` |
| 9 | A,2 | 01 | 12 | 7,9,12 | 1.2857 | `201020120` |
| 12 | B,3 | 01 | 02 | 9,12,16 | 1.3333 | `201020120201` |
| 16 | A,3 | 12 | 02 | 12,16,21 | 1.3333 | `0201201020120201` |
| 22 | B,4 | 12 | 12 | 16,21,28 | 1.375 | |
| 30 | A,4 | 01 | 12 | 21,28,37 | 1.4286 | |
| 40 | B,5 | 01 | 02 | 28,37,49 | 1.4286 | |
| 53 | A,5 | 12 | 02 | 37,49,65 | 1.4324 | |
| 71 | B,6 | 12 | 12 | 49,65,86 | 1.4490 | |
| 95 | A,6 | 01 | 12 | 65,86,114 | 1.4615 | |

### Step 2: the bispecial factors of $`V=a_4(G)`$ and $`U=a_1(G)`$

**Chain for $`V`$:** $`G\xrightarrow{\mathrm L_{20}}y_1\xrightarrow{\mathrm R_{10}}y_2\xrightarrow{[021]}V`$. Hypotheses: $`E^+_G(2)=\{0\}`$ ((H), $`2^+=0`$); in $`y_1`$ every $`1`$ comes from a $`1`$ of $`G`$,
which is preceded in $`G`$ by $`0`$, whose image $`\mathrm L_{20}(0)=20`$ ends with $`0`$: $`E^-_{y_1}(1)=\{0\}`$ ((H'), $`1^-=0`$).

**Chain for $`U`$:** $`G\xrightarrow{\mathrm L_{20}}y_1\xrightarrow{\mathrm R_{01}}z_2\xrightarrow{\mathrm L_{12}}z_3\xrightarrow{[021]}U`$. Hypotheses: $`2^+=0`$ in $`G`$; every $`0`$ of $`y_1`$ lies in a block $`20`$, so
$`E^-_{y_1}(0)=\{2\}`$; every $`1`$ of $`z_2`$ lies in a block $`\mathrm R_{01}(1)=10`$, so $`E^+_{z_2}(1)=\{0\}`$.

For $`w\in\mathrm{Bisp}^*(G)`$ let $`\Theta_V(w)`$, $`\Theta_U(w)`$ be the composites of the maps $`\Lambda_h`$ of Lemmas 4(b), 5(b), 6 along these chains (defined since all words involved are ordinary).
We track the case distinctions of Lemmas 4(b) and 5(b); $`E^-(w),E^+(w)`$ are 2-subsets of $`A`$.

* $`\mathrm L_{20}`$ ($`a=2`$, $`b=0`$, $`2^+=0`$): it appends $`2`$ iff $`E^+(w)=\{0,2\}`$. In that case the new right letters are $`f_{20}(2^+)=f_{20}(0)=2`$ and $`0`$,
  so $`E^+`$ stays $`\{0,2\}`$; otherwise $`E^+`$ becomes $`f_{20}(E^+(w))=\{1,2\}`$ (from $`\{0,1\}`$ or $`\{1,2\}`$). $`E^-`$ is unchanged.
* $`V`$: $`\mathrm R_{10}`$ ($`a=1`$, $`b=0`$) prepends $`1`$ iff the current $`E^-`$, i.e. $`E^-(w)`$, is $`\{0,1\}`$. Then $`[021]`$ maps the prepended $`1`$ to $`2`$ and the
  appended $`2`$ to $`[021](\mathrm R_{10}(2))=1`$, and $`[021]\circ\mathrm R_{10}\circ\mathrm L_{20}=a_4`$.
* $`U`$: $`\mathrm R_{01}`$ ($`a=0`$, $`b=1`$) prepends $`0`$ iff $`E^-(w)=\{0,1\}`$ and leaves $`E^+`$ unchanged. $`\mathrm L_{12}`$ ($`a=1`$, $`b=2`$) appends $`1`$ iff the
  current $`E^+`$ is $`\{1,2\}`$, i.e. iff $`E^+(w)\ne\{0,2\}`$. Under $`[021]\circ\mathrm L_{12}`$ the prepended $`0`$ stays $`0`$, the $`2`$ appended at the first step becomes
  $`[021](\mathrm L_{12}(\mathrm R_{01}(2)))=[021](12)=21`$, the $`1`$ appended at the third step becomes $`2`$, and $`[021]\circ\mathrm L_{12}\circ\mathrm R_{01}\circ\mathrm L_{20}=a_1`$.
  Exactly one of the two suffixes occurs.

This gives

```math
\Theta_V(w)=[2\ \text{if}\ E^-(w)=\{0,1\}]\ a_4(w)\ [1\ \text{if}\ E^+(w)=\{0,2\}],
```

```math
\Theta_U(w)=[0\ \text{if}\ E^-(w)=\{0,1\}]\ a_1(w)\ [21\ \text{if}\ E^+(w)=\{0,2\},\ \text{else}\ 2],
```

where $`[s\ \text{if}\ P]`$ is $`s`$ or $`\varepsilon`$. The return words of $`\Theta_h(w)`$ correspond bijectively to those of $`w`$, with Parikh vectors multiplied by $`M_h`$ ($`h=a_4,a_1`$),
because the product of the elementary incidence matrices along the chain is $`M_h`$.

**Proposition 2.**

```math
\mathrm{Bisp}^*(V)=\Theta_V(\mathrm{Bisp}^*(G))\sqcup\{1,\,2,\,21\},\qquad \mathrm{Bisp}^*(U)=\Theta_U(\mathrm{Bisp}^*(G))\sqcup\{2,\,02,\,21,\,021\},
```

and all these bispecial factors are ordinary. The extra ones have

| word | factor of | $`E(w)`$ | Parikh vectors of return words |
|---|---|---|---|
| `1` | V | (1,0),(2,0),(2,1) | (0,1,0),(1,1,1),(1,1,2) |
| `2` | V | (0,1),(0,2),(2,1) | (0,0,1),(1,1,1),(1,2,1) |
| `21` | V | (0,1),(2,0),(2,1) | (1,1,1),(1,2,1),(1,2,2) |
| `2` | U | (0,0),(0,1),(1,1) | (0,1,1),(1,0,1),(1,1,1) |
| `02` | U | (1,0),(1,1),(2,1) | (1,0,1),(1,1,1),(1,2,2) |
| `21` | U | (0,0),(0,2),(1,0) | (0,1,1),(1,1,1),(2,1,2) |
| `021` | U | (1,2),(2,0),(2,2) | (1,1,1),(1,2,2),(2,2,3) |

*Proof.* By Proposition 1 all nonempty bispecial factors of $`G`$ are ordinary, so by Lemma 4(c) ($`m=0`$) the only nonempty bispecial factor of $`y_1=\mathrm L_{20}(G)`$
not of the form $`\Lambda_h(u)`$ is the letter $`2`$, with (Lemma 4(a)(ii), $`u=\varepsilon`$) $`E_{y_1}(2)=\{(e,f_{20}(0)):(e,2)\in\mathcal L_2(G)\}\cup\{(e,0):(e,0)\in\mathcal L_2(G)\}=\{(0,2),(1,2),(1,0),(2,0)\}`$;
it is not ordinary ($`E^-=\{0,1,2\}`$). Also $`\mathcal L_2(y_1)=\{01,02,12,20,22\}`$. By Lemma 5(a), with $`m=1`$, the new bispecial factors after the next step come from $`u=\varepsilon`$ or $`u=2`$:

* $`V`$, step $`\mathrm R_{10}`$ ($`a=1`$, $`b=0`$, $`1^-=0`$, $`f_{10}:0\mapsto1`$): case (i) for $`u=2`$ gives $`2`$ with graph $`\{(1,2),(1,0),(2,0)\}`$;
  case (ii) for $`u=2`$ gives $`12`$ with graph $`\{(1,2),(1,0),(0,2)\}`$ (here $`|E^+(12)\cup E^+(02)|=2`$); case (ii) for $`u=\varepsilon`$ gives $`1`$ with graph
  $`\{(f_{10}(0),2)\}\cup\{(0,1),(0,2)\}=\{(1,2),(0,1),(0,2)\}`$. All three are ordinary, and $`[021]`$ turns them into $`1,21,2`$ with the graphs of the table.
* $`U`$, step $`\mathrm R_{01}`$ ($`a=0`$, $`b=1`$, $`0^-=2`$, $`f_{01}:1\mapsto0`$): case (i) for $`u=2`$ gives $`2`$ with graph $`\{(0,2),(0,0),(2,0)\}`$; case (ii) for $`u=2`$
  gives $`02`$ with graph $`\{(2,2),(1,2),(1,0)\}`$; case (ii) for $`u=\varepsilon`$ gives $`0`$ with graph $`\{(2,1),(2,2),(1,2)\}`$. All are ordinary, so in $`z_2`$ every nonempty
  bispecial factor is ordinary. At the step $`\mathrm L_{12}`$ ($`a=1`$, $`b=2`$, $`1^+=0`$), Lemma 4(b) maps these three to $`\Lambda_h(2)=12`$, $`\Lambda_h(0)=01`$, $`\Lambda_h(02)=012`$, and by
  Lemma 4(c) ($`m=0`$) the only other new one is the letter $`1`$, with graph $`\{(0,0),(0,2),(2,2)\}`$ (from $`\mathcal L_2(z_2)=\{01,10,02,20,22\}`$). $`[021]`$ turns
  $`12,01,012,1`$ into $`21,02,021,2`$ with the graphs of the table.

The Parikh vectors of the return words of these seven short words were computed by enumeration from exact factor sets (`verify.py` S3); they are used only for the finite check in Step 4.
*Computer cross-check.* Independently of this hand derivation, `verify.py` applies Lemmas 4-6 step by step, starting from $`G`$ where all nonempty bispecial factors are ordinary (Proposition 1).
At each elementary step, Lemma 4(c)/5(c) says that the bispecial factors that are not images $`\Lambda_h(u)`$ of ordinary ones have length $`\le 2m+1`$, $`m`$ the maximal length of
non-ordinary bispecial factors of the previous word, and the non-ordinary bispecial factors of the new word are among these (the $`\Lambda_h(u)`$ are ordinary). The bound is propagated along
the chain, and all bispecial factors of the intermediate words of length up to the bound (plus 2) were enumerated from exact factor sets (Lemma 2), separating the images $`\Lambda_h(u)`$ from the new ones
(`verify.py` S3, function `walk_chain`). Results: $`V`$-chain: after $`\mathrm L_{20}`$ the only new one is $`2`$, non-ordinary with
$`E_{y_1}(2)=\{(0,2),(1,2),(1,0),(2,0)\}`$ (as Lemma 4(a)(ii) predicts); after $`\mathrm R_{10}`$ (bound $`3`$) the new ones are $`2,1,12`$, all ordinary; after $`[021]`$: $`2,1,21`$.
$`U`$-chain: after $`\mathrm L_{20}`$: $`2`$ (non-ordinary, as above); after $`\mathrm R_{01}`$ (bound 3): $`2,0,02`$, ordinary; after $`\mathrm L_{12}`$ (bound 1): the new letter $`1`$ and the images
$`12,01,012`$ of the previous new ones; after $`[021]`$: $`2,21,02,021`$. Their graphs and return words were computed from exact factor sets. $`\square`$

Every word of Propositions 1-2 of length $`\le 600`$ was also compared with an exhaustive enumeration of all bispecial factors of $`G`$, $`U`$, $`V`$ of length $`\le 600`$ (extension graphs and Parikh vectors of all return words agree; `verify.py` S4).

### Step 3: complexity

In $`G`$, $`U`$, $`V`$ all three letters occur, $`|\mathcal L_2|=5`$ so $`m(\varepsilon)=5-3-3+1=0`$, and every nonempty bispecial factor is ordinary, hence $`m(w)=0`$ (Propositions 1, 2).
By Lemma 1, $`p_G(n)=p_U(n)=p_V(n)=2n+1`$ for all $`n`$. (For $`G`$ this is [SS, Lemma 28]†.) In particular the three words are not eventually periodic. They are uniformly recurrent:
$`G`$ is the fixed point of the primitive morphism $`\gamma`$ ($`M^3\gt0`$) — every factor $`w`$ of $`G`$ lies in some $`\gamma^n(0)`$, hence in every $`\gamma^{n+3}(c)`$, and $`G`$ is a concatenation of blocks $`\gamma^{n+3}(c)`$ —
and nonerasing morphic images of uniformly recurrent words are uniformly recurrent. By the Reduction, **all ten words of Figures 3-4 and all ten words of arXiv Figures 1-2 have complexity $`2n+1`$.**

### Step 4: critical exponent

By Lemma 3 it suffices to show, for $`x\in\{G,U,V\}`$:

```math
\text{(I)}\quad |w|\lt\alpha|r|\ \ \text{for every bispecial}\ w\ \text{and every}\ r\in\mathrm{Ret}(w),\qquad\text{(II)}\quad \sup_w |w|/|r_w|\ge\alpha .
```

Then $`E(x)=1+\alpha=\mu`$ and the supremum is not attained. For $`w=\varepsilon`$ (I) is trivial; for the seven extra words of Proposition 2 it is a finite check
(the largest ratio is $`1`$). It remains to treat the families

```math
w_k=\Phi^k(s)\ (x=G),\qquad \Theta_h(\Phi^k(s))\ (x=U,V),\qquad s\in\{20,0\},\ k\ge0 .
```

*Linear recurrences.* Let $`P_k=\Psi(\Phi^k(s))`$ and, for a fixed return word $`r`$ of $`s`$, $`Q_k=M^k\Psi(r)`$ (the Parikh vector of the corresponding return word of $`\Phi^k(s)`$).
By Proposition 1, $`P_{k+1}=MP_k+c_k`$ with $`c_k=\Psi(s_k)+\Psi(t_k)`$ depending only on $`k\bmod 2`$ (orbit A: $`0`$, $`(1,0,1)^T`$; orbit B: $`(0,0,1)^T`$, $`(1,0,0)^T`$).
Fix a residue $`\nu\in\{0,1,2,3\}`$ and set $`N=M^4`$, $`P'_j=P_{4j+\nu}`$, $`Q'_j=Q_{4j+\nu}`$; then $`P'_{j+1}=NP'_j+C`$, $`Q'_{j+1}=NQ'_j`$ with a constant integer vector $`C`$.
The length of the bispecial factor and of the return word are $`g\cdot P'_j+\kappa`$ and $`g\cdot Q'_j`$, where $`g=(1,1,1)`$, $`\kappa=0`$ for $`G`$, $`g=(1,1,1)M_{a_1}=(3,2,2)`$ for $`U`$,
$`g=(1,1,1)M_{a_4}=(3,1,1)`$ for $`V`$, and $`\kappa=|s|+|t|`$ from the explicit forms of $`\Theta_U,\Theta_V`$. Since $`(E^-(w_k),E^+(w_k))`$ depends only on $`k\bmod 2`$
(Proposition 1(3)), $`c_k`$ and $`\kappa`$ are in fact 2-periodic in $`k`$; so $`C`$, $`\kappa`$ and $`m_0`$ below are the same for the residues $`\nu`$ and $`\nu+2`$
(asserted in `verify.py` S6). We group by $`k\bmod 4`$ only because the graphs $`E(w_k)`$ are 4-periodic. So we must show $`D_j\lt0`$ for all $`j\ge0`$, where

```math
D_j=\kappa+g\cdot P'_j-\alpha\,g\cdot Q'_j .
```

*Closed form.* $`1`$ is not an eigenvalue of $`N`$ (the eigenvalues of $`M`$ are $`\lambda`$ and $`\beta,\bar\beta`$ with $`\beta\bar\beta=1/\lambda`$), so $`X=(I-N)^{-1}C\in\mathbb Q^3`$ exists and
$`P'_j=X+N^j(P'_0-X)`$. Hence

```math
D_j=m_0+g\,N^jZ,\qquad m_0=\kappa+g\cdot X\in\mathbb Q,\qquad Z=P'_0-X-\alpha Q'_0\in\mathbb Q(\lambda)^3 .
```

Over $`\mathbb Q(\lambda)`$, $`x^3-2x^2+x-1=(x-\lambda)q(x)`$ with $`q(x)=x^2-(2-\lambda)x+(\lambda-1)^2`$ (roots $`\beta,\bar\beta`$). Let $`Z_\lambda=q(M)Z/q(\lambda)`$
(an eigenvector for $`\lambda`$; $`q(\lambda)=3\lambda^2-4\lambda+1\ne0`$) and $`Z_W=Z-Z_\lambda\in\ker q(M)`$. Then

```math
D_j=m_0+\theta\,\lambda^{4j}+e_j,\qquad \theta=g\cdot Z_\lambda\in\mathbb Q(\lambda),\qquad e_j=g\,N^jZ_W=2\,\mathrm{Re}(c\,\beta^{4j}),
```

and from $`e_0,e_1`$ one gets $`4|c|^2=B:=e_0^2+(e_0\,\mathrm{Re}\beta^4-e_1)^2/(\mathrm{Im}\beta^4)^2\in\mathbb Q(\lambda)`$, hence $`e_j^2\le B\,\lambda^{-4j}`$.
Here $`\beta+\bar\beta=2-\lambda`$, $`\beta\bar\beta=(\lambda-1)^2=1/\lambda`$, $`\beta^4+\bar\beta^4`$ and $`|\beta|^8`$ are polynomials in these, and $`(\mathrm{Im}\beta^4)^2=|\beta|^8-(\mathrm{Re}\beta^4)^2\gt0`$.
If $`\theta\le0`$, $`J\ge0`$, $`\delta_J:=-(m_0+\theta\lambda^{4J})\gt0`$ and $`\delta_J^2\gt B\lambda^{-4J}`$, then for all $`j\ge J`$: $`-(m_0+\theta\lambda^{4j})\ge\delta_J\gt|e_j|`$, i.e. $`D_j\lt0`$.

*Computation (exact; computer-assisted).* `verify.py` S6 does all of this in exact arithmetic in $`\mathbb Q(\lambda)=\mathbb Q[x]/(x^3-2x^2+x-1)`$; signs of elements of $`\mathbb Q(\lambda)`$ are decided with certified
rational enclosures of $`\lambda`$ obtained by bisection (the polynomial is increasing on $`[3/2,2]`$). For each of the 72 families (3 words, 2 orbits, 4 residues, and the 3 return words of $`\Phi^\nu(s)`$, which correspond bijectively to the 3 return words of the seed $`s`$ by Proposition 1) it checks
$`q(M)Z_W=0`$, $`\theta\le0`$, finds $`J\le1`$ with the two inequalities above (asserted; $`J=1`$ occurs only for the family with $`\theta=0`$ in the classes $`(U,A,0)`$, $`(U,B,1)`$, $`(V,A,0)`$, $`(V,B,1)`$, otherwise $`J=0`$), verifies $`D_j\lt0`$ directly (exact sign of an element $`\ell_1-\alpha\ell_2`$, $`\ell_i\in\mathbb Z`$) for $`j\le J+3`$,
and checks that the closed form equals $`D_j`$ exactly for these $`j`$. This proves (I).
In every one of the 24 (word, orbit, residue) classes exactly one of the three return-word families has $`\theta=0`$ (asserted in `verify.py` S6), namely the one coming from the return word $`20`$ of the seed $`20`$ (orbit A) resp. $`01`$ of the seed $`0`$ (orbit B); for it $`D_j\to m_0`$, so $`|w|/|r|=\alpha+D_j/|r|\to\alpha`$; as $`|r_w|\le|r|`$, (II) follows.
The limits $`m_0`$ (for the return word with $`\theta=0`$) are:

| word | orbit A, k = 0,1,2,3 mod 4 | orbit B, k = 0,1,2,3 mod 4 |
|---|---|---|
| G | -6/5, -9/5, -6/5, -9/5 | -8/5, -7/5, -8/5, -7/5 |
| U | -4/5, -11/5, -4/5, -11/5 | -12/5, -3/5, -12/5, -3/5 |
| V | -1, -2, -1, -2 | -2, -1, -2, -1 |

So $`|w|-\alpha|r_w|`$ tends to these negative constants along the respective subsequences (for $`U`$ the best gap is $`-3/5`$, for $`V`$ it is $`-1`$, for $`G`$ it is $`-6/5`$).
Hence $`E(G)=E(U)=E(V)=\mu`$, not attained (for $`G`$ this is [SS, Theorem 29]†). With the Reduction this proves the Theorem. $`\blacksquare`$

## What is new

* Conjecture 19 of [Cu-EJC] (equivalently Conjecture 1 of arXiv:2507.09387v3) is settled affirmatively for all twenty listed words: complexity $`2n+1`$ and critical exponent exactly $`\mu`$.
* The twenty words fall into three language classes up to letter permutation and reversal: that of $`G`$ ($`a_3,b_1,b_2,b_3`$), of $`U=a_1(G)`$ ($`a_1,a_2,b_4,b_5`$) and of $`V=a_4(G)`$ ($`a_4,b_6`$); each arXiv morphism is a conjugate of the corresponding journal morphism composed with $`\gamma^k`$ or $`(\gamma^R)^k`$.
* Complete description of the bispecial factors of $`G,U,V`$: two $`\Phi`$-orbits with explicit forms $`s\gamma(w)t`$, $`s\,a_1(w)t`$, $`s\,a_4(w)t`$, all ordinary (neutral), three return words each, and the exact asymptotic gaps $`|w|-\alpha|r_w|\to m_0\in\frac15\mathbb Z`$.
* The method (left/right insertion lemmas under the hypothesis "the inserted letter has a unique neighbour on the relevant side") is standard in spirit (S-adic descriptions of bispecial factors, as in work of Cassaigne, Labbé, Leroy and of Klouda); the self-contained Lemmas 4-5 are written for exactly the hypotheses used here.
* The proof re-derives Lemma 28 and Theorem 29 of [SS] by a different route.

## Verification

`verify.py` (Python 3, standard library only; `python3 verify.py [NB]`, default NB = 300, 15 s on an idle core and about 50 s under load; NB = 600 about 2-5 min). All checks are assertions; it ends with `ALL CHECKS PASSED`.

* S1: all morphism identities of the Reduction and the elementary decompositions; for each arXiv row, the conjugating word for R4.
* S2: primitivity of $`\gamma`$ ($`M^3\gt0`$); exact factor sets of $`G`$ by Lemma 2, asserting both condition (a) (the words $`\gamma^k(0)`$ concerned are prefixes of the prefix used) and the closure condition (b); $`\mathcal L_2(G)`$.
* S3: hypotheses (H)/(H') at every step of the three chains; the seeds $`1\in x_1`$, $`2\in x_2`$ and their data; $`\Phi(w)=s\gamma(w)t`$, $`\Theta_U`$, $`\Theta_V`$ explicit forms; the extra short bispecial factors of $`U`$, $`V`$ with the length bounds of Lemmas 4(c), 5(c).
* S4: the lemma-generated lists of bispecial factors of $`G,U,V`$ (extension graphs, Parikh vectors of all return words) coincide with exhaustive enumeration for lengths $`\le`$ NB (run with NB = 600: 20 nonempty bispecial factors for $`G`$, 21 each for $`U`$ and $`V`$).
* S5: brute-force complexity $`p(n)=2n+1`$ for $`n\le`$ NB for $`G`$, $`G'`$ and all 20 images (exact factor sets).
* S6: the certified inequality of Step 4 for all 72 families and the seven extra words, exact arithmetic in $`\mathbb Q(\lambda)`$; asserts $`J\le1`$, exactly one family with $`\theta=0`$ in each of the 24 classes, and the 2-periodicity of $`m_0`$.
* S7: independent brute force: largest repetition exponent with period $`\le3000`$ in a prefix of length 60000 of each of the 20 images and of $`G`$ (bitset method); all are $`\lt\mu`$, the largest found being $`4919/1983=2.480585\ldots`$ ($`U`$-class), $`6233/2513=2.480302\ldots`$ ($`G`$-class), $`1255/506=2.480237\ldots`$ ($`V`$-class).


**Referee pass.** One independent referee pass was made by a separate model instance, which reviewed `verify.py` and wrote its own code from scratch (without reading the scratch scripts).
It checked by hand every lemma and proposition (R1-R5, Lemmas 1-6, Propositions 1-2, Steps 3-4, including boundary cases and the six relabelling rules) and found no error.
Its seven minor gaps (the derivation of $`\Theta_U,\Theta_V`$, a hand proof of the extra bispecial factors of Proposition 2, the sentence on $`\mathrm{Ret}(20)`$, the wording on the
return words of the seed, and three assertions missing in `verify.py`) and its notation remarks are addressed in this version.
Its independent numerical checks: all bispecial factors of $`G,U,V`$ of length $`\le450`$ (from exact factor sets of length 1500), compared with Propositions 1-2;
all identities of the Reduction, and $`p(n)=2n+1`$ for $`n\le1000`$ for $`G`$, $`G'`$ and all 20 images; $`|w|\lt\alpha|r|`$ for $`k\le400`$ along every family, decided with a certified
1500-bit enclosure of $`\lambda`$, reproducing the table of $`m_0`$; a brute-force test of Lemmas 4(a)/5(a) and 4(b)/5(b) on words with many non-ordinary bispecial factors (a test, not a certificate);
and repetitions with periods $`\le5000`$ in prefixes of length 400000 (largest exponents found: $`10939/4410`$ for the $`G`$ class, $`5718/2305`$ for $`U`$, $`11597/4675`$ for $`V`$, all $`\lt\mu`$).
Its standard-library scripts are in `review/` and are run from that folder: `common.py` (helpers), `reduction.py [NMAX]` (default 400; 18 s with 1000), `bisp.py [NB] [N]`
(default 400 1300; 10 s with 450 1500), `crit.py [KMAX]` (default 400; about 1 s), `lemma_test.py` (about 3 s). Its two other scripts, `closed_form.py` (numerical eigen-decomposition)
and `reps.py` (the repetition search), need numpy and are not included.

## Sources

* [Cu-EJC] J. D. Currie, Words with factor complexity $`2n+1`$ and minimal critical exponent, Electron. J. Combin. 33(3) (2026), #P3.31, DOI 10.37236/14527. Conjecture 19, Figures 3 and 4, definitions of $`\gamma,G,\gamma^R,G'`$ (Section 7; read in the journal PDF).
* [Cu-arXiv] J. D. Currie, same title, arXiv:2507.09387v3 (13 March 2026), Conjecture 1, Figures 1 and 2 (read in the HTML version; strings taken from its TeX annotations).
* [SS] J. Shallit, A. M. Shur, Subword complexity and power avoidance, arXiv:1801.05376 (DOI 10.1016/j.tcs.2018.09.010), Lemma 28 ($`p_G(n)=2n+1`$) and Theorem 29 ($`E(G)=2+1/(\lambda^2-1)`$). † Only used as a cross-check; both results are re-proved here.
* [DDP] F. Dolce, L. Dvořáková, E. Pelantová, On balanced sequences and their critical exponent, Theoret. Comput. Sci. 939 (2023), 18-47; arXiv:2108.07503. Theorem 3. † A self-contained proof of the statement used is given (Lemma 3).
* [CLL] J. Cassaigne, S. Labbé, J. Leroy, Almost everywhere balanced sequences of complexity $`2n+1`$, arXiv:2102.10093, DOI 10.2140/moscow.2022.11.287. † Background only; not used.

† marks a source that we read only through a summarising web tool, not directly. No step of the proof depends on a source marked †.
