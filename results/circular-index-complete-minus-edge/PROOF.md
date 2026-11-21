# Circular chromatic index of a complete graph minus an edge (Mazák–Zrubák, Conjecture 2)

**Status:** text proof, not formalised. It has been through one independent referee pass (a second model instance, report summarised under *Verification*). The finite checks in `verify.py`, `verify_sat.py` and `review/` agree with it.

## Statement

A *circular $`r`$-edge-colouring* of a graph $`G`$ is a map $`c:E(G)\to[0,r)`$ such that $`1\le|c(e)-c(f)|\le r-1`$ whenever $`e`$ and $`f`$ share a vertex. The *circular chromatic index* $`\chi'_c(G)`$ is the least $`r`$ for which one exists; it satisfies $`\chi'(G)-1\lt\chi'_c(G)\le\chi'(G)`$. [MZ, Section 1; Zhu01]

**Theorem.** Let $`d\ge 6`$ be even and let $`G`$ be the complete graph $`K_{d+1}`$ with one edge removed. Then $`\chi'_c(G)=d+1`$.

This is Conjecture 2 of Mazák and Zrubák [MZ], who verified it by computer for $`d\in\{6,8,10,12\}`$. For $`d=4`$ the statement is false: $`\chi'_c(K_5-e)=9/2`$ [MZ]. The proof below shows where $`d\ge6`$ is used (last step).

Throughout, $`n=d+1=2h-1`$ with $`h=d/2+1\ge4`$, $`G=K_n-uv`$, and

```math
N=|E(G)|=\binom n2-1=h(2h-3)=2h(h-2)+h .
```

The vertices $`u,v`$ are called *special* (degree $`n-2`$), the others *normal* (degree $`n-1`$). Any two normal vertices are adjacent. Since $`n`$ is odd, a matching has at most $`h-1`$ edges, so $`\chi'(G)\ge N/(h-1)\gt n-1`$, and $`\chi'(G)\le\chi'(K_n)=n`$. Hence $`\chi'(G)=n`$ and $`\chi'_c(G)\le n`$. The task is to exclude $`\chi'_c(G)\lt n`$.

## Step 1. Acyclic colourings

For a proper colouring $`f:V(H)\to\mathbb Z_k`$ of a graph $`H`$ let $`D_f`$ be the digraph on $`V(H)`$ with an arc $`x\to y`$ whenever $`xy\in E(H)`$ and $`f(y)=f(x)+1`$.

**Lemma 1 (Guichard [Gui93]; see [Zhu01, Theorem 3.1]).** If $`\chi_c(H)\lt k=\chi(H)`$, then $`H`$ has a proper colouring $`f:V(H)\to\mathbb Z_k`$ for which $`D_f`$ has no directed cycle.

*Proof (included for completeness).* Since $`\chi_c(H)\lt k`$, there is a circular $`r`$-colouring $`\psi:V(H)\to[0,r)`$ with $`r\lt k`$. Here $`r\gt k-1`$: otherwise $`\lfloor\psi\rfloor`$ would be a proper colouring with the $`k-1`$ colours $`0,\dots,k-2`$. Put $`f(x)=\lfloor\psi(x)\rfloor\in\{0,\dots,k-1\}`$. Adjacent vertices have $`|\psi(x)-\psi(y)|\ge1`$, so $`f`$ is proper. For an arc $`x\to y`$ with $`f(x)\le k-2`$ we get $`\psi(y)\gt\psi(x)`$, hence $`\psi(y)-\psi(x)\ge1`$. For an arc with $`f(x)=k-1`$, $`f(y)=0`$ we get $`\psi(y)-\psi(x)\ge-(r-1)`$. A directed cycle passes through the colours cyclically, so it has $`mk`$ arcs of which $`m`$ are of the second kind. Summing along the cycle gives $`0\ge m(k-1)-m(r-1)=m(k-r)\gt0`$, a contradiction. ∎

Apply this to the line graph of $`G`$. From now on **assume, for a contradiction, that $`\varphi:E(G)\to\mathbb Z_n`$ is a proper edge-colouring whose digraph $`D=D_\varphi`$ is acyclic.** The vertices of $`D`$ are the edges of $`G`$, and $`e\to f`$ means that $`e,f`$ share a vertex and $`\varphi(f)=\varphi(e)+1`$. Write $`M_i=\varphi^{-1}(i)`$.

## Step 2. Colour classes, the source and the sink

**Lemma 2.** After adding a constant to all colours:

1. $`|M_0|=h-2`$ and $`|M_i|=h-1`$ for $`i\ne0`$. So $`M_0`$ misses exactly three vertices, forming a set $`A`$, and each other class misses exactly one vertex.
2. $`D`$ has exactly one source $`f^*`$ and exactly one sink $`g^*`$. Moreover $`\varphi(f^*)=1`$, $`\varphi(g^*)=n-1`$, and both edges have both ends in $`A`$.

*Proof.* (1) Each class is a matching, so has at most $`h-1`$ edges, and $`N=n(h-1)-1`$. Adding a constant to all colours does not change $`D`$. (2) An edge $`xy`$ of colour $`i`$ is a source exactly when no edge at $`x`$ or $`y`$ has colour $`i-1`$, that is when $`M_{i-1}`$ misses both $`x`$ and $`y`$. Then $`i-1=0`$ and $`x,y\in A`$. Two such edges would be disjoint edges of $`M_1`$ inside the three-element set $`A`$. So there is at most one source, and in the same way at most one sink, of colour $`n-1`$ inside $`A`$. A finite acyclic digraph has a source and a sink. ∎

## Step 3. The longest-path levels form a linear order

For an edge $`e`$ let $`L(e)`$ be the number of arcs of a longest directed path of $`D`$ ending at $`e`$.

**Lemma 3.** $`L`$ is a bijection from $`E(G)`$ onto $`\{0,1,\dots,N-1\}`$, and $`\varphi(e)\equiv L(e)+1\pmod n`$. The edges with $`L=\ell`$ and $`L=\ell+1`$ share a vertex. Finally:

> **(P)** if $`e,f`$ share a vertex and $`L(e)\lt L(f)`$, then $`L(f)-L(e)\not\equiv 0,-1\pmod n`$.

*Proof.* A longest path ending at $`e`$ starts at a source (otherwise it could be extended backwards, and in an acyclic digraph the extended walk is again a path), hence at $`f^*`$, and colours increase by one along arcs. So $`\varphi(e)\equiv L(e)+1`$. Write $`L(e)=t(e)+n\,w(e)`$ with $`0\le t(e)\le n-1`$; thus $`t=0,1,\dots,n-2,n-1`$ for the colours $`1,2,\dots,n-1,0`$. For an arc $`e\to f`$ we have $`L(f)\ge L(e)+1`$, which gives

```math
w(f)\ge w(e)\quad\text{always},\qquad w(f)\ge w(e)+1\quad\text{if }\varphi(e)=0 .
```

For $`S\subseteq M_i`$ let $`N^+(S)\subseteq M_{i+1}`$ be the set of edges of colour $`i+1`$ sharing a vertex with an edge of $`S`$. We claim:

- (E1) $`|N^+(S)|\ge|S|`$ for $`S\subseteq M_i`$, $`1\le i\le n-2`$, and for $`S\subseteq M_0`$;
- (E2) $`|N^+(S)|\ge|S|`$ for $`S\subseteq M_{n-1}\setminus\{g^*\}`$.

Indeed, the edges of $`S`$ cover $`2|S|`$ vertices. In (E1) the class $`M_{i+1}`$ misses only one vertex. In (E2) the class $`M_0`$ misses the three vertices of $`A`$, but two of them are the ends of $`g^*\in M_{n-1}`$ and are not covered by $`S`$. So in both cases at least $`2|S|-1`$ of the covered vertices lie on an edge of the next class, and these edges number at least $`\lceil(2|S|-1)/2\rceil=|S|`$.

Let $`a_i(j)`$ be the number of edges $`e\in M_i`$ with $`w(e)\ge j`$. The sets $`\{e\in M_i:w(e)\ge j\}`$ are mapped by $`N^+`$ into the corresponding set of the next class, and into the set with $`j+1`$ when $`i=0`$. With (E1), (E2):

```math
a_1(j)\le a_2(j)\le\dots\le a_{n-1}(j),\qquad a_0(j)\ge a_{n-1}(j)-1,\qquad a_1(j+1)\ge a_0(j).
```

Hence $`a_1(j+1)\ge a_1(j)-1`$. On the other hand every level $`\ell`$ between $`0`$ and $`\Lambda=\max L`$ contains an edge (the predecessor on a longest path has level one less), and level $`nj`$ consists of the edges of colour 1 with $`w=j`$. So $`a_1(j+1)\le a_1(j)-1`$ whenever $`nj\le\Lambda`$. Therefore all the inequalities above are equalities for these $`j`$. Let $`J`$ be the least integer with $`nJ\gt\Lambda`$, so that no edge has $`w\ge J`$. Starting from $`a_1(0)=h-1`$ and going down by one at each step we reach $`a_1(J)=0`$, so $`J=h-1`$. For $`0\le j\le h-2`$ we get $`a_i(j)=h-1-j`$ for $`1\le i\le n-1`$ and $`a_0(j)=h-2-j`$, and $`a_i(h-1)=0`$ for all $`i`$. So for each colour $`i\ne0`$ and each $`0\le j\le h-2`$ there is exactly one edge of colour $`i`$ with $`w=j`$, and for colour 0 exactly one for each $`0\le j\le h-3`$ and none with $`w=h-2`$. These are $`(n-1)(h-1)+(h-2)=N`$ edges on the levels $`0,\dots,N-1`$, one on each.

The edge of level $`\ell+1`$ has an in-neighbour of level $`\ell`$, so the two share a vertex. For (P): $`L(f)-L(e)\equiv0`$ would give two edges of the same colour at a vertex. If $`L(f)-L(e)\equiv-1`$ then $`\varphi(e)=\varphi(f)+1`$, so $`f\to e`$ is an arc and $`L(e)\gt L(f)`$. ∎

Let $`s_\ell`$ be the edge with $`L=\ell`$. We say that a vertex $`x`$ *is at position* $`\ell`$ if $`x\in s_\ell`$. Every position holds exactly two vertices. Since each edge of $`G`$ has exactly one position:

> **(M)** two normal vertices have exactly one common position; $`u`$ and $`v`$ have none; a normal and a special vertex have exactly one.

## Step 4. Runs

Let $`p_1\lt\dots\lt p_{\deg x}`$ be the positions of a vertex $`x`$. A *run* of $`x`$ is a maximal set of consecutive integers among them, and $`k_x`$ is the number of runs.

**Lemma 4.**

1. For a normal vertex, $`p_{j+1}-p_j\equiv1\pmod n`$ for all $`j`$.
2. For $`0\le\ell\le N-2`$ exactly one vertex is at both positions $`\ell`$ and $`\ell+1`$. Hence $`\sum_x k_x=N+1`$.
3. There is exactly one vertex $`b`$ in $`s_0\cap s_{N-1}`$. It is normal and $`k_b=h-1`$. Every other normal vertex $`x`$ has $`k_x=h-2`$, and its first position $`\alpha_x`$ and last position $`\omega_x`$ satisfy $`\omega_x=\alpha_x+N-2h`$, so $`0\le\alpha_x\le 2h-1`$. For every normal vertex, a run ending at $`e`$ that is not its last run is followed by a run starting at $`e+2h`$; equivalently, a run starting at $`s`$ that is not its first run is preceded by a run ending at $`s-2h`$. All runs of $`u`$ and of $`v`$ have length one.

*Proof.* (1) Let $`\mu`$ be the colour missing at $`x`$ and let $`e_j`$ be the edge at $`x`$ of colour $`\mu+j`$, $`1\le j\le n-1`$. Then $`e_j\to e_{j+1}`$ is an arc, so $`L(e_j)\lt L(e_{j+1})`$ and the difference is $`\equiv1`$.

(2) By Lemma 3, $`s_\ell`$ and $`s_{\ell+1}`$ are distinct edges sharing a vertex. Counting pairs (vertex, position) gives $`\sum_x(\text{sum of run lengths})=2N`$ and $`\sum_x\sum_{\text{runs}}(\text{length}-1)=N-1`$.

(3) Let $`x`$ be normal and write $`\beta_x=N-1-\omega_x`$. By (1), $`\omega_x-\alpha_x=(n-2)+nT_x`$, where $`T_x`$ is the sum of $`(p_{j+1}-p_j-1)/n`$. Steps inside a run contribute 0 and steps between runs at least 1, so $`T_x\ge k_x-1`$, with equality exactly when all steps between runs equal $`n+1=2h`$. Since $`N-1-(n-2)=n(h-2)`$, we get $`\alpha_x+\beta_x=n\,q_x`$ for an integer $`q_x`$, and $`q_x\ge0`$ because $`\alpha_x,\beta_x\ge0`$. Moreover

```math
k_x\le T_x+1=h-1-q_x .
```

Here $`q_x=0`$ only if $`x\in s_0\cap s_{N-1}`$, which holds for at most one vertex. Let $`\varepsilon\in\{0,1\}`$ be the number of normal vertices with $`q_x=0`$. Special vertices have $`k\le n-2`$. With (2):

```math
n(h-1)=N+1=\sum_xk_x\le(n-2)(h-1)-(n-2-\varepsilon)+2(n-2)=(n-2)h+\varepsilon=n(h-1)-1+\varepsilon .
```

So $`\varepsilon=1`$ and equality holds everywhere: one normal vertex $`b`$ has $`q_b=0`$ and $`k_b=h-1`$; every other normal $`x`$ has $`q_x=1`$, that is $`\alpha_x+\beta_x=n`$, and $`k_x=h-2`$; all steps between runs of normal vertices equal $`2h`$; and $`k_u=k_v=n-2`$, which is the number of edges at $`u`$ and at $`v`$. ∎

For $`1\le\ell\le N-1`$ let $`\mathrm{start}(\ell)`$ be the vertex of $`s_\ell`$ not in $`s_{\ell-1}`$, and for $`0\le\ell\le N-2`$ let $`\mathrm{end}(\ell)`$ be the vertex of $`s_\ell`$ not in $`s_{\ell+1}`$. By Lemma 4(3), a special vertex at position $`\ell`$ equals $`\mathrm{start}(\ell)`$ and $`\mathrm{end}(\ell)`$ whenever these are defined. In particular:

> **(C)** the vertex common to $`s_\ell`$ and $`s_{\ell+1}`$ is always normal; and if $`\ell`$ is a position of a special vertex and $`y`$ is the normal vertex of $`s_\ell`$, then $`y\in s_{\ell-1}`$ (if $`\ell\ge1`$) and $`y\in s_{\ell+1}`$ (if $`\ell\le N-2`$).

## Step 5. The table with $`2h`$ columns

Write every position as $`\ell=2h\rho+c`$ with *row* $`\rho\ge0`$ and *column* $`c\in\{0,\dots,2h-1\}`$. Since $`N=2h(h-2)+h`$, the columns $`c\le h-1`$ (the *left half*) have the rows $`0,\dots,h-2`$ and the columns $`c\ge h`$ (the *right half*) have the rows $`0,\dots,h-3`$. A position is *special* if it holds $`u`$ or $`v`$.

**Lemma 5.**

1. The special positions are exactly the positions in four columns $`r_1,r_2,r_1+h,r_2+h`$ with $`r_1\ne r_2`$ in $`\{0,\dots,h-1\}`$.
2. Let $`P=\{0,\dots,h-1\}\setminus\{r_1,r_2\}`$, so $`|P|=h-2`$. Every column $`\alpha\in P\cup(P+h)`$ is the first position of exactly one normal vertex $`x_\alpha\ne b`$, and these are all the normal vertices other than $`b`$.
3. Let $`x`$ be normal with first position $`\alpha`$, and put $`g_{\max}=h`$ if $`x\ne b`$ and $`g_{\max}=h-1`$ if $`x=b`$. There are integers $`0=i^-(0)\le i^+(0)=i^-(1)\le i^+(1)=\dots\le i^+(g_{\max})=k_x-1`$ such that the positions of $`x`$ are exactly

```math
\alpha+g+2h\,i,\qquad 0\le g\le g_{\max},\quad i^-(g)\le i\le i^+(g),
```

and $`x`$ is at both $`\ell`$ and $`\ell+1`$ exactly for $`\ell=\alpha+g+2h\,i^+(g)`$, $`0\le g\lt g_{\max}`$. If the column of $`\alpha+g`$ is special, then $`i^-(g)=i^+(g)`$.

*Proof.* We first prove the description of the positions in (3), then (1) except for the form $`r_1+h,r_2+h`$ of the right special columns, then (2) together with that form, and finally the last sentence of (3).

*Positions in (3).* By Lemma 4 the steps $`p_{j+1}-p_j`$ of $`x`$ are 1 or $`2h`$, and there are $`k_x-1`$ steps of the second kind. Let $`g`$ count the steps of the first kind and $`i`$ those of the second kind made so far. This gives the description; the final value of $`g`$ is $`(n-2)-(k_x-1)`$, which is $`h`$ for $`x\ne b`$ and $`h-1`$ for $`b`$.

*(1), closure and count.* Let $`\ell`$ be special, holding the special vertex $`\sigma`$, and let $`\ell+2h\le N-1`$. Put $`z=\mathrm{start}(\ell+2h)`$. If $`z`$ were normal, its run starting at $`\ell+2h`$ would not be its first, since first positions are at most $`2h-1`$. So its previous run ends at $`\ell`$ (Lemma 4(3)), hence $`z=\mathrm{end}(\ell)=\sigma`$, a contradiction. So $`\ell+2h`$ is special. Symmetrically, if $`\ell-2h\ge0`$ then $`z=\mathrm{end}(\ell-2h)`$ is special: a normal $`z`$ would not be in its last run, since last positions are at least $`N-2h`$, and its next run would start at $`\ell`$, giving $`z=\mathrm{start}(\ell)=\sigma`$. Hence the set of special positions is a union of whole columns. There are $`2(n-2)=4h-6`$ special positions, a left column has $`h-1`$ positions and a right column $`h-2`$. If there are $`\sigma_1`$ left and $`\sigma_2`$ right special columns, then $`\sigma_1(h-1)+\sigma_2(h-2)=4h-6`$, that is $`(h-2)(\sigma_1+\sigma_2-4)=2-\sigma_1`$. With $`0\le\sigma_1,\sigma_2\le h`$ and $`h\ge4`$ the only solution is $`\sigma_1=\sigma_2=2`$: the right side lies between $`2-h`$ and $`2`$ and is divisible by $`h-2\ge2`$, so it is $`0`$ (giving $`\sigma_1=2`$, $`\sigma_2=2`$) or $`-(h-2)`$ (giving $`\sigma_1=h`$, $`\sigma_2=3-h\lt0`$), or, for $`h=4`$ only, $`2`$ (giving $`\sigma_1=0`$, $`\sigma_2=5\gt h`$).

*(2), and the form of the special columns.* The first positions of the $`n-3=2h-4`$ normal vertices other than $`b`$ lie in $`\{0,\dots,2h-1\}`$ (Lemma 4). They are distinct, because for $`\ell\ge1`$ only $`\mathrm{start}(\ell)`$ can have first position $`\ell`$, and position 0 holds $`b`$ and one other vertex. None of them is special: at a special position $`\ell\ge1`$ the starting vertex is special, and a special position 0 holds $`b`$ and a special vertex. As exactly $`2h-4`$ columns are not special, each of them is the first position of exactly one such vertex. The last position of $`x_\alpha`$ is $`\alpha+N-2h\equiv\alpha+h\pmod{2h}`$. It is not special: otherwise it is not $`N-1`$ (because $`s_{N-1}`$ would then consist of $`b`$ and the normal vertex $`x_\alpha`$), and then (C) puts $`x_\alpha`$ at the next position as well. So the set of non-special columns is closed under adding $`h`$ modulo $`2h`$, which gives the form of the special columns in (1) and of $`P`$.

*Last sentence of (3).* Let the column of $`\alpha+g`$ (that is, $`(\alpha+g)\bmod 2h`$) be special. By (1) the position $`\alpha+g+2h\,i^-(g)`$ is then special. If $`i^+(g)\gt i^-(g)`$, then $`x`$ is not at the next position, against (C). ∎

For $`p\in P`$ we call $`x_p`$ *unwrapped* and $`x_{p+h}`$ *wrapped*. By Lemma 5(3):

- $`b`$ has its positions in the columns $`0,\dots,h-1`$;
- $`x_p`$ in the columns $`p,\dots,p+h`$, and its position $`p+g+2hi`$ is in row $`i`$;
- $`x_{p+h}`$ in the columns $`p+h,\dots,2h-1`$ (row $`i`$) and $`0,\dots,p`$ (row $`i+1`$).

In every column that a normal vertex visits, its rows form an interval. Each of these intervals begins in the row where the previous one ends, except that for a wrapped vertex the interval in column 0 begins one row below the end of its interval in column $`2h-1`$ (position $`2h\rho+2h-1`$ is followed by position $`2h(\rho+1)`$). We call $`j_x(g)=i^+(g)-i^-(g)`$ the number of *junctions* of $`x`$ at $`g`$. Thus $`\sum_gj_x(g)=h-3`$ for $`x\ne b`$, and junctions occur only in non-special columns.

**Rows at a boundary.** For a column $`c\in\{0,\dots,h-2\}`$ and a normal vertex $`z`$ that is at positions $`2h\rho+c`$ and $`2h\rho+c+1`$ for some $`\rho`$, this $`\rho`$ is unique by Lemma 5(3); call it $`\rho_c(z)`$. By Lemma 5(3) the vertices for which it exists are $`b`$, the $`x_p`$ with $`p\le c`$ and the $`x_{p+h}`$ with $`p\gt c`$ ($`p\in P`$). These are $`h-1`$ vertices. For each of them the value lies in $`\{0,\dots,h-2\}`$, because the left column $`c`$ has exactly these rows. Conversely, each of the $`h-1`$ positions $`2h\rho+c`$, $`0\le\rho\le h-2`$, is at most $`2h(h-2)+h-2=N-2`$, so it has exactly one vertex in common with the next position (Lemma 4(2)); this vertex is normal by (C), hence it is one of the vertices listed, with $`\rho_c`$ equal to $`\rho`$. So:

> **(B)** for $`0\le c\le h-2`$, $`\rho_c`$ is a bijection from $`\{b\}\cup\{x_p:p\le c\}\cup\{x_{p+h}:p\gt c\}`$ onto $`\{0,\dots,h-2\}`$.

In the same way the rows in which the $`x_p`$ ($`p\in P`$) pass from column $`h-1`$ to column $`h`$ are distinct and at most $`h-3`$; call them $`\rho_{h-1}(x_p)`$. And the rows in which the $`x_{p+h}`$ arrive in column 0 are distinct and at least 1; call them $`\rho_{-1}(x_{p+h})`$. Put also $`\rho_{-1}(b)=0`$, $`\rho_{h-1}(b)=h-2`$, $`\rho_{p-1}(x_p)=0`$ and $`\rho_p(x_{p+h})=h-2`$. These conventions do not clash with the values defined before: the list in (B) for the column $`p-1`$ does not contain $`x_p`$, the list for the column $`p`$ does not contain $`x_{p+h}`$, and $`b`$ occurs neither among the vertices passing from column $`h-1`$ to column $`h`$ nor among those arriving in column 0 from column $`2h-1`$. With these conventions, for every normal vertex $`z`$ and every left column $`c`$ that it visits:

> **(R)** the set $`R_c(z)`$ of rows of $`z`$ in column $`c`$ is the interval $`[\rho_{c-1}(z),\rho_c(z)]`$.

(For $`x_p`$ in its first column this says that it starts in row 0; for $`x_{p+h}`$ in its last column $`p`$, that it ends in row $`h-2`$, the row of its last position; for $`b`$, that it starts at position 0 and ends at $`N-1`$.) A consequence:

> **(O)** if $`y,z`$ both visit the left column $`c`$ and $`\rho_{c-1}(y)\lt\rho_{c-1}(z)`$ while $`\rho_c(y)\gt\rho_c(z)`$, then $`R_c(z)\subseteq R_c(y)`$, so $`y`$ and $`z`$ have a common position in column $`c`$.

## Step 6. The vertex $`b`$ separates unwrapped from wrapped vertices

Let $`\pi(c)=|P\cap\{0,\dots,c\}|`$, with $`\pi(-1)=0`$.

**Lemma 6.** Let $`0\le c\le h-2`$ and $`p\in P`$. If $`p\le c`$ then $`\rho_c(x_p)\lt\rho_c(b)`$. If $`p\gt c`$ then $`\rho_c(x_{p+h})\gt\rho_c(b)`$. Consequently $`\rho_c(b)=\pi(c)`$, the $`x_p`$ with $`p\le c`$ occupy the rows $`0,\dots,\pi(c)-1`$ at this boundary, and the $`x_{p+h}`$ with $`p\gt c`$ occupy the rows $`\pi(c)+1,\dots,h-2`$.

*Proof.* By (B), distinct vertices have distinct values of $`\rho_c`$, so in the comparisons below "not greater" means "smaller" and conversely. Suppose $`\rho_{c_0}(x_p)\gt\rho_{c_0}(b)`$ for some $`c_0\in[p,h-2]`$ and take $`c_0`$ minimal. Then $`b`$ and $`x_p`$ have a common position in column $`c_0`$: for $`c_0=p`$ because $`R_p(x_p)=[0,\rho_p(x_p)]\supseteq[\rho_{p-1}(b),\rho_p(b)]`$, and for $`c_0\gt p`$ by (O). If $`\rho_c(x_p)\lt\rho_c(b)`$ for some $`c\in(c_0,h-2]`$, the least such $`c`$ gives, by (O), a common position in column $`c\ne c_0`$. Otherwise $`\rho_{h-2}(x_p)\gt\rho_{h-2}(b)`$, and then $`R_{h-1}(x_p)=[\rho_{h-2}(x_p),\rho_{h-1}(x_p)]\subseteq[\rho_{h-2}(b),h-2]=R_{h-1}(b)`$ because $`\rho_{h-1}(x_p)\le h-3`$; this is a common position in column $`h-1\ne c_0`$. Both cases contradict (M).

Suppose $`\rho_{c_0}(x_{p+h})\lt\rho_{c_0}(b)`$ for some $`c_0\in[0,p-1]`$ and take $`c_0`$ maximal. Then there is a common position in column $`c_0+1`$: for $`c_0+1=p`$ because $`R_p(x_{p+h})=[\rho_{p-1}(x_{p+h}),h-2]\supseteq R_p(b)`$, and otherwise by (O). If $`\rho_c(x_{p+h})\gt\rho_c(b)`$ for some $`c\in[0,c_0)`$, the largest such $`c`$ gives a common position in column $`c+1\le c_0`$. Otherwise $`\rho_0(x_{p+h})\lt\rho_0(b)`$ and $`R_0(x_{p+h})=[\rho_{-1}(x_{p+h}),\rho_0(x_{p+h})]\subseteq[0,\rho_0(b)]=R_0(b)`$, a common position in column $`0\ne c_0+1`$. Again (M) is contradicted.

The last sentence follows from (B). ∎

So $`R_c(b)=[\pi(c-1),\pi(c)]`$ for every left column $`c`$: one row if $`c\notin P`$, and the two rows $`k-1,k`$ if $`c`$ is the $`k`$-th element of $`P`$.

## Step 7. Where the other vertices have their junctions

Write $`P=\{p_1\lt p_2\lt\dots\lt p_{h-2}\}`$.

**Lemma 7.** For $`1\le m\le h-2`$:

1. $`R_{p_m}(x_{p_m})=[0,m-1]`$ and $`R_{p_m}(x_{p_m+h})=[m,h-2]`$;
2. $`x_{p_m}`$ has $`m-1`$ junctions at $`g=0`$, $`h-2-m`$ junctions at $`g=h`$, and no others. So it occupies the rows $`0,\dots,m-1`$ of column $`p_m`$, row $`m-1`$ of the columns $`p_m+1,\dots,p_m+h-1`$, and the rows $`m-1,\dots,h-3`$ of column $`p_m+h`$.

*Proof.* (1) By (M), $`b`$ and $`x_{p_m}`$ have exactly one common position, in a left column $`c\ge p_m`$. By Lemma 6 and the bound $`\rho_{h-1}(x_{p_m})\le h-3=\pi(h-1)-1`$, the rows of $`x_{p_m}`$ in column $`c`$ are at most $`\pi(c)-1`$. So a common row exists only if $`c=p_k`$ for some $`k\ge m`$ and $`\rho_{p_k}(x_{p_m})=k-1`$. For a given $`k`$ at most one $`m`$ has this property, by (B) (and by the distinctness of the $`\rho_{h-1}(x_p)`$ when $`p_k=h-1`$). So $`m\mapsto k`$ is an injective map of $`\{1,\dots,h-2\}`$ into itself with $`k\ge m`$, hence the identity. Thus $`\rho_{p_m}(x_{p_m})=m-1`$.

Likewise $`b`$ and $`x_{p_m+h}`$ have exactly one common position, in a left column $`c\le p_m`$, and the rows of $`x_{p_m+h}`$ in column $`c`$ are at least $`\pi(c-1)+1`$. (For $`c\ge1`$ this is Lemma 6 at the column $`c-1`$; for $`c=0`$ it is the bound $`\rho_{-1}(x_{p_m+h})\ge1`$ of Step 5.) A common row exists only if $`c=p_k`$ with $`k\le m`$ and $`\rho_{p_k-1}(x_{p_m+h})=k`$. For a given $`k`$ at most one $`m`$ qualifies, by (B) at the column $`p_k-1`$ (and by the distinctness of the arrival rows $`\rho_{-1}(x_{p+h})`$ when $`p_k=0`$). So $`m\mapsto k`$ is injective with $`k\le m`$, hence the identity, and $`\rho_{p_m-1}(x_{p_m+h})=m`$.

(2) The vertices $`x=x_{p_m}`$ and $`y=x_{p_m+h}`$ visit the columns $`p_m,\dots,p_m+h`$ and $`p_m+h,\dots,2h-1,0,\dots,p_m`$ respectively, so their common columns are $`p_m`$ and $`p_m+h`$. By (1) they have no common row in column $`p_m`$, so by (M) they have one in column $`p_m+h`$. There $`x`$ has the rows $`[h-3-j_x(h),\,h-3]`$ and $`y`$ the rows $`[0,j_y(0)]`$. By (1), $`j_x(0)=m-1`$ and $`j_y(h)=h-2-m`$, so $`j_x(h)\le h-2-m`$ and $`j_y(0)\le m-1`$, that is

```math
h-3-j_x(h)\ \ge\ m-1\ \ge\ j_y(0).
```

A common row forces equality in both places. Then all $`h-3`$ junctions of $`x`$ are at $`g=0`$ and $`g=h`$. ∎

## Step 8. The contradiction

Since $`h\ge4`$, the set $`P`$ has at least two elements $`p_1\lt p_2`$. By Lemma 7(2):

- $`x_{p_1}`$ is in row 0 of every column $`p_1,\dots,p_1+h-1`$ and in the rows $`0,\dots,h-3`$ of column $`p_1+h`$;
- $`x_{p_2}`$ is in the rows $`0,1`$ of column $`p_2`$, in row 1 of the columns $`p_2+1,\dots,p_2+h-1`$, and in the rows $`1,\dots,h-3`$ of column $`p_2+h`$.

Now $`p_1\lt p_2\le h-1\lt p_1+h\lt p_2+h`$. So both vertices are at the position in row 0 and column $`p_2`$, and both are at the position in row 1 and column $`p_1+h`$ (note $`1\le h-3`$). These are two different positions, which contradicts (M). Hence no proper $`n`$-edge-colouring of $`G`$ has an acyclic digraph, and by Lemma 1, $`\chi'_c(G)=n=d+1`$. ∎

**Remark ($`d=4`$).** For $`h=3`$ the set $`P`$ has one element and Step 8 has nothing to compare. Steps 2 to 4 remain valid for $`h=3`$, and acyclic colourings exist (for $`h=3`$ the counting argument in Lemma 5(1) is not conclusive, but `verify.py` confirms its statement on all acyclic colourings). With vertices $`u,v,b,x,y`$, the order

```math
ub,\ xb,\ vx,\ ux,\ xy,\ vy,\ uy,\ yb,\ vb
```

with colours $`1,2,3,4,0,1,2,3,4`$ is one. By the converse direction of Guichard's theorem [Zhu01, Theorem 3.1], which we do not prove here, an acyclic colouring gives $`\chi'_c(K_5-uv)\lt5`$, in accordance with the value $`9/2`$ of [MZ].

## What is new

The Theorem, for all even $`d\ge6`$. Mazák and Zrubák state it as a conjecture and report a computer verification for $`d\le12`$ [MZ, Conjecture 2 and the sentence after it]. Lemma 1 is Guichard's theorem and is not new. We found no proof of the conjecture in the literature (search of 21 November 2026).

## Verification

The proof does not depend on any of the scripts. They check its statements on small cases.

- `verify.py` (standard library; `python3 verify.py` takes about 10 seconds). Part A enumerates all 2160 proper 5-edge-colourings of $`K_5-e`$, finds the 180 with acyclic digraph, and checks on each the statements of Lemmas 2, 3, 4 and 5(1). Part B searches exhaustively, up to automorphisms of the graph, for edge orderings with the properties of Lemma 3 (consecutive edges share a vertex, and (P)): there are 3 for $`d=4`$ (and $`5\cdot12\cdot3=180`$, with 5 rotations of the colours and 12 automorphisms), and none for $`d=6`$.
- `verify_sat.py` (needs `python-sat`) checks directly from the definition, without using any lemma, that $`K_7-e`$ has no proper 7-edge-colouring with acyclic digraph (38 s), and that $`K_5-e`$ has one. Acyclicity is encoded by a transitive order on the edges.
- `review/` contains the scripts of the referee pass, which share no code with the two above:
  - `d4_check.py`: on all 180 acyclic colourings of $`K_5-e`$, every statement from Lemma 2 to Lemma 7, including (E1), (E2), (M), (C), (B), (R).
  - `sat_levels.py 4 6`: a second SAT check from the definition, with acyclicity encoded by an integer potential; $`d=6`$ is unsatisfiable (224 s).
  - `relaxed.py 3 4 5`: enumerates, for $`h=3,4,5`$, all configurations that satisfy the conclusions of Lemmas 4 and 5 for the normal vertices, without imposing (M). There are 3, 66 and 13380. On all of them (B) holds, the conclusions of Lemmas 6 and 7 follow from their hypotheses, and for $`h=4,5`$ none has every pair of normal vertices meeting exactly once.
  - `arith.py`: the identities for $`N`$ and the counting in Lemma 5(1) for $`3\le h\le20`$.

The referee pass found no mathematical error. It asked for the justifications that are now in the proofs of Lemma 1, Lemma 5 (order of the argument), (B), Lemma 6 (distinctness) and Lemma 7(1) (the case $`p_k=0`$), and for the correction of one sentence in Step 5 that was not used.

The computer check of [MZ] covers $`d\le12`$; our scripts cover only $`d=6`$ directly (we did not complete a run for $`d=8`$).

## Sources

- **[MZ]** J. Mazák and F. Zrubák, *Circular chromatic index of small graphs*, [arXiv:2603.08822](https://arxiv.org/abs/2603.08822) (March 2026). Conjecture 2; the value $`9/2`$ for $`K_5-e`$; definitions.
- **[Gui93]** D. R. Guichard, *Acyclic graph coloring and the complexity of the star chromatic number*, J. Graph Theory 17 (1993), 129–134. Lemma 1. † Quoted through [Zhu01].
- **[Zhu01]** X. Zhu, *Circular chromatic number: a survey*, Discrete Math. 229 (2001), 371–410. Basic facts on $`\chi_c`$ and the statement of Guichard's theorem.

† marks a source we did not read directly.
