# A matching-relative degree-five theorem for Favaron–Genest–Kouider

**Status: precise partial theorem with a computer-assisted proof; not a resolution of Conjecture 1.** The unrestricted degree-five case, including the triangle-rich case, remains open. This note proves Theorem A, a common generalization of three published degree-five cases, and reduces the diamond-free case to one configuration.

The proof assembles the matched-triangle construction and the square-to-triangle sweep of [the main note](04-regular-path-decomposition.md). It re-proves each collision claim and adds the hypothesis-restricted odd-cycle lemma. That lemma is the only new computer-assisted step. The [pipeline checker](check_regular_path_sweep_pipeline.py) contains the exact finite lemma, symbolic re-partition checks and randomized end-to-end runs.

## Statement

Let \(G\) be a finite simple 5-regular graph and \(M\) a perfect matching of \(G\). An *\(M\)-triangle* is a triangle containing an edge of \(M\). An *\(M\)-square* is a 4-cycle containing exactly one edge of \(M\). A *triangle–square conflict* is an \(M\)-triangle and an \(M\)-square sharing at least one edge. This is not the "bad pair" of Favaron, Genest and Kouider; see the comparison below.

**Theorem A.** If \(G\) has a perfect matching \(M\) with no triangle–square conflict, then \(E(G)\) partitions into paths with exactly five edges.

**Corollaries.** Each of the following hypotheses implies the hypothesis of Theorem A, so each class decomposes.

1. \(G\) has no 4-cycle and has a perfect matching. Then there is no \(M\)-square. Favaron, Genest and Kouider proved a stronger statement, for a wider class. If no 4-cycle of \(G\) shares an edge with a triangle or with another 4-cycle, then every 1-factor is *extendable*: it is the middle-edge set of some decomposition. [J. Graph Theory 63 (2010)](https://doi.org/10.1002/jgt.20413) For such graphs Theorem A recovers only the existence of a decomposition.
2. \(G\) is triangle-free and has a perfect matching. Then there is no \(M\)-triangle. This is the Botler–Mota–Wakabayashi theorem. [Discrete Math. 338 (2015)](https://doi.org/10.1016/j.disc.2015.04.018)
3. \(G\) has a perfect matching and no triangle shares an edge with a 4-cycle. This is Chu–Fan–Hong–Zhou Theorem 2.2. [Sci. Sin. Math. 54 (2024)](https://www.sciengine.com/cfs/files/pdfs/view/1674-7216/9A038B7537554B7284033EDD2D967FFB.pdf)
4. **New special case.** \(G\) has a perfect matching \(M\) none of whose edges lies in a triangle. Equivalently, the two ends of every edge of \(M\) have no common neighbour. Every other triangle may share edges with any number of 4-cycles, and \(M\)-squares may overlap arbitrarily.
5. The 408-vertex example in the main note, which falls outside the hypotheses of cases 1–3.

**Comparison with FGK Theorems 6–7.** The full-text comparison is in [04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md).

- **FGK's bad pair.** FGK call two \(M\)-cycles a *bad pair* if they share an edge and their union minus \(M\) has a vertex of degree 3.
- **FGK Theorem 6.** If \(M\) induces no bad pair in their sense, then \(M\) itself is extendable.
- **FGK Theorem 7.** The same conclusion holds if the bad-pair graph is a star.
- **The hypotheses are incomparable.**
  - Theorem A allows any square–square or triangle–triangle overlaps. The 408-vertex example has 68 FGK bad pairs, all square–square, and its bad-pair graph is not a star, so FGK do not cover it.
  - FGK allow an \(M\)-triangle and an \(M\)-square that share only their \(M\)-edge, but this is a triangle–square conflict here.
- **Conclusions.** Where FGK apply, their conclusion is stronger: \(M\) is the middle-edge set. Theorem A only gives the existence of some decomposition.

The theorem does **not** cover graphs in which every perfect matching has a triangle–square conflict. For example, in \(K_6\) with \(M=\{01,23,45\}\), the \(M\)-triangle \(012\) shares the edges \(01,12\) with the \(M\)-square \((0,1,2,4)\), whose only matching edge is \(01\). All perfect matchings of \(K_6\) are equivalent under symmetry. The decomposition produced need not have its middle edges in \(M\).

## 1. The canonical construction

Write \(m(v)\) for the mate of \(v\) in \(M\) and \(H=G-M\), a 4-regular graph.

**Lemma 1** (the construction in FGK's proof of Theorem 6: vertex splitting along prescribed pairs, an Eulerian orientation, and a Petersen 2-factorization; there one 2-factor is then reversed). There are fixed-point-free permutations \(r,s\) of \(V(G)\) with the following properties.

- (P1) The edge sets \(R=\{\{v,r(v)\}\}\) and \(S=\{\{v,s(v)\}\}\) each have \(n\) edges, are disjoint, and partition \(E(H)\).
- (P2) \(r(r(v))\ne v\) and \(s(s(v))\ne v\) for every \(v\).
- (P3) \(s(r(u))\ne m(u)\) for every \(u\).

*Proof.* At each vertex \(w\), pair its four \(H\)-edges so that \(wx,wy\) are paired whenever \(xy\in M\). These prescribed pairs are disjoint because \(M\) is a matching. Split each vertex into one copy per pair. The resulting graph is 2-regular. Orient each of its cycles and identify the copies again. This gives an Eulerian orientation of \(H\) in which paired edges have opposite directions at \(w\). The bipartite graph of out-copies and in-copies, with one edge per arc, is 2-regular. Hence it is the union of two perfect matchings \(P_1,P_2\). Let \(r(u)\) be the head of the \(P_1\)-arc leaving \(u\), and let \(s(w)\) be the tail of the \(P_2\)-arc entering \(w\). Property (P1) is immediate. A 2-cycle of \(r\) or \(s\) would orient one edge of the simple graph \(H\) both ways, proving (P2). If \(s(r(u))=v=m(u)\), put \(w=r(u)\). Both arcs \(u\to w\) and \(v\to w\) enter \(w\). Since \(uv\in M\), the edges \(wu,wv\) were paired at \(w\) and are oppositely directed, a contradiction. \(\square\)

The following consequences of (P1) are used repeatedly. For every \(v\), \(r(v),s(v)\ne m(v)\), \(r(v)\ne s(v)\), \(s(r(v))\ne v\) and \(r(s(v))\ne v\). Each equality would make one edge lie in two of \(M,R,S\). Each vertex is \(r(u)\) for exactly one \(u\) (its unique *red head* role), and \(s\circ r\) is a permutation.

For an edge \(uv\in M\), the *canonical trail* is

\[
\tau(uv)=(s(r(u)),\,r(u),\,u,\,v,\,r(v),\,s(r(v))).
\]

**Lemma 2.** The canonical trails partition \(E(G)\). Each vertex is an endpoint of exactly one of them. Each is a simple path, unless exactly one of \(s(r(v))=r(u)\) and \(s(r(u))=r(v)\) holds.

*Proof.* The matching edges, the edges \(\{u,r(u)\}\) and the edges \(\{r(u),s(r(u))\}\) are each used once, because \(r\) and \(s\circ r\) are permutations. Distinctness of the six vertices follows from the listed consequences, injectivity, and (P3), except for the two displayed equalities. Both cannot hold, by (P2) for \(s\). \(\square\)

A non-path canonical trail is *defective*. Orient it so the repetition is at its right end and label it

\[
T=(a,b,c,d,e,b),\qquad cd\in M,\ b=r(c),\ e=r(d),\ a=s(b),\ s(e)=b.
\]

The labels \(a,b,c,d,e\) are distinct, and \(a\ne e\) by (P2). The cycle \((b,c,d,e)\) is an \(M\)-square, since \(bc,de\in R\) and \(eb\in S\).

## 2. The sweep

For a defective \(T\), put \(f=r^{-1}(c)\). Its *target* is \(\tau(f\,m(f))\), the canonical trail in which \(c\) is a red head. We have \(f\notin\{c,d\}\) because \(r(d)=e\ne c\), so the target is not \(T\). If the target is defective with labels \((a',b',c',d',e')\), then \(c\in\{b',e'\}\). The link is *type 1* if \(c=b'\), *type 2* if \(c=e'\), and *type 0* if the target is not defective.

Each defective trail has at most one outgoing type-2 link. A type-2 link into \(T'\) must come from the trail whose matching edge contains \(e'\), so each trail has at most one incoming type-2 link. The type-2 links therefore form vertex-disjoint directed paths and cycles. Each cycle has length at least two.

Choose the first vertex and every second vertex of each path as *sources*. Choose alternate vertices of every even cycle as sources. Set aside the trails on odd cycles. Every remaining non-source defective trail is a *recipient*, which has an incoming type-2 link from a source. No source has an incoming type-2 link from a source.

**Trades.** Each source \(T\) gives its edge \(\{b,c\}\in R\) to its target and takes the edge \(\{c,s(c)\}\in S\) from the target. The taken edge is the terminal edge at the \(c\)-end of a type-0 target. It is the pendant \(\{b',a'\}\) of a type-1 target and the closing edge \(\{e',b'\}\) of a type-2 target. Given edges are distinct \(R\)-edges, and taken edges are distinct \(S\)-edges. Thus no edge moves twice. The new pieces are as follows.

| Piece | New sequence |
|---|---|
| Source | \((A,b,e,d,c,s(c))\) |
| Recipient | \((A,b,c,d,e,r(e))\) |
| Trail on an odd type-2 cycle | \((A,b,c,d,e,b)\) for now |
| Type-0 target \((x,c,f,g,h,y)\) | The terminal at each end that received an edge is replaced by the corresponding source's \(b=r(c)\) |

Here \(A=a\) unless the trail is the type-1 target of a source \(T''\). In that case \(c''=b\), and \(A=r(b)\). A recipient's incoming type-2 source has \(c''=e\) and \(b''=r(e)\).

**Lemma 3 (collisions).** Outside the odd cycles, every new piece is a simple path except in the following cases. Each exception produces a triangle–square conflict.

- A source or a recipient can have \(A=d\). This happens only for a changed pendant \(A=r(b)\), since an unchanged \(a=s(r(c))\ne m(c)=d\) by (P3). Then \(bd\) is an edge, and the \(M\)-triangle \(bcd\) shares \(bc,cd\) with the \(M\)-square \((b,c,d,e)\).
- A source can have \(s(c)=e\), and a recipient can have \(r(e)=c\). Then \(ce\) is an edge, and the \(M\)-triangle \(cde\) shares \(cd\) with the \(M\)-square.
- In a type-0 target \(Q=(x,c,f,g,h,y)\), the new terminal can satisfy \(b=g\). Then \(fb\in M\), and the \(M\)-triangle \(bcf\) shares \(bc\) with the source's \(M\)-square. The opposite end has the symmetric exception.

*Proof.* Write the source sequence as \((A,b,e,d,c,x)\) with \(x=s(c)\). The vertices \(b,e,d,c\) are distinct. We have \(A\ne b\) for either choice of \(A\). The equality \(a=e\) would contradict (P2), and \(r(b)=e=r(d)\) would give \(b=d\). The equality \(a=s(b)=c\) would put \(bc\) in both \(R\) and \(S\), and \(r(b)=c\) would contradict (P2). The vertex \(x\) differs from \(b=s(e)\) by injectivity, from \(d\) because \(cd\in M\), and from \(c\). For the endpoints, \(s(c)=a=s(b)\) is impossible. If \(A=r(b)\), then \(A=b''\) for the type-1 source \(T''\), and \(s(e'')=b''\). Thus \(s(c)=A\) would give \(c=e''\), making \(T\to T''\) a type-2 link. Then \(T''\) would be the non-source successor of the source \(T\), so it would not trade, contrary to its type-1 input. The remaining equalities are \(A=d\) and \(x=e\).

Write the recipient sequence as \((A,b,c,d,e,y)\) with \(y=r(e)\). The inequalities for \(A\) are the same, apart from \(A=d\). For \(y\), \(r(e)\ne e\), \(r(e)\ne d\) by (P2), and \(r(e)\ne b=r(c)\). The endpoints differ. Indeed \(y=b''\) is an original terminal of the type-2 source \(T''\ne T\), while \(a\) is an original terminal of \(T\). Canonical terminals are distinct, and if \(A=r(b)\) then \(r(b)=r(e)\) would give \(b=e\). The remaining equality is \(y=c\).

For a type-0 target \(Q=(x,c,f,g,h,y)\), let \(f=r^{-1}(c)\), \(g=m(f)\), \(h=r(g)\) and \(y=s(h)\). Let the new terminal be \(b=r(c)\). It differs from \(c\), from \(f\) by (P2), and from \(h\). Otherwise \(c=g\), so \(f=d\) and \(r(d)=c\ne e\), a contradiction. It also differs from \(y=s(h)\). Otherwise \(b=s(e)\) gives \(h=e\), so \(g=d\) and \(f=c\). If the opposite end also receives \(\tilde b=r(h)\), then \(b\ne\tilde b\) since \(c\ne h\). The analysis of \(\tilde b\) is symmetric. Its only exception is \(\tilde b=f\). For a received terminal against an unchanged opposite terminal, \(\tilde b=s(\tilde e)=x=s(c)\) would give \(\tilde e=c\), hence \(\tilde d=f\) and \(\tilde c=g\). This contradicts \(\tilde c=h\ne g\). In each exception, the stated triangle has an edge of \(M\) and three distinct vertices, and \((b,c,d,e)\) is an \(M\)-square. \(\square\)

## 3. Odd type-2 cycles

Let \(T_0,\ldots,T_{L-1}\) be an odd type-2 cycle, with \(L\ge3\), indices modulo \(L\), and \(c_i=e_{i+1}\). Each \(T_i\) may have received a type-1 pendant change from an external source, giving the pendant terminal \(A_i\). The following facts hold.

- (o1) The \(b_i\), the \(c_i\) and the \(d_i\) are each pairwise distinct. They are distinct red heads and distinct matching endpoints.
- (o2) No \(b_i\) equals any \(c_j\). Since \(c_j=e_{j+1}=r(d_{j+1})\), equality would give \(c_i=d_{j+1}\), so two different trails would share a matching edge.
- (o3) \(d_i\notin\{b_{i-1},b_i,b_{i+1}\}\). The case \(b_{i+1}=s(e_{i+1})=s(c_i)\) would put \(c_id_i\) in \(S\). The case \(b_{i-1}=r(c_{i-1})=r(e_i)\) would form a 2-cycle of \(r\) with \(r(d_i)=e_i\).
- (o4) Every \(A_i\) avoids all \(b_j\), its own \(c_i\) and its own \(e_i\). An unchanged \(a_i=s(b_i)\) equal to \(b_j=s(e_j)\) would give \(b_i=e_j\), that is \(r(c_i)=r(d_j)\), hence \(c_i=d_j\), contrary to (o2) via \(e_j=c_{j-1}\). A changed \(A_i=r(b_i)\) comes from an external source with \(c''=b_i\). Its equality with \(r(c_j)\) or \(r(d_{j+1})\) would make \(b_i\) a matching endpoint of a trail on the cycle. A changed \(A_i\) therefore avoids every \(c_j\) and \(e_j\). An unchanged \(a_i\ne d_i\) by (P3). The equality \(A_i=r(b_i)=d_i\) produces the bad chord \(b_id_i\).
- (o5) The \(A_i\) are distinct. Unchanged values are distinct canonical terminals, changed values are distinct images under \(r\), and a changed value \(r(b_i)=b''\) is a terminal of an external trail.

**Pair replacement.** For consecutive \(i,i+1\), replace \(T_i,T_{i+1}\) by

\[
(A_i,b_i,e_i,d_i,c_i,b_{i+1}),\qquad (A_{i+1},b_{i+1},c_{i+1},d_{i+1},c_i,b_i).
\]

These pieces use the same ten edges. By (o1)–(o5), the pieces are simple unless \(A_i=d_i\) or \(A_{i+1}=d_{i+1}\). Either equality gives the bad chord described in (o4).

**Lemma 4 (exact finite check).** Consider three consecutive trails of an odd type-2 cycle. Use every label identification allowed by (o1)–(o5): \(e_0=c_2\) when \(L=3\), and \(d_0=b_2\) and/or \(d_2=b_0\) when \(L\ge5\). Suppose the 15 local edges contain no \(M\)-triangle through some \(c_id_i\) that shares an edge with one of the three local \(M\)-squares. Then the three trails can be replaced by three simple five-edge paths. The only exception is an open block, \(L\ge5\), with \(d_1\in\{A_0,A_2\}\).

*Verification.* `verify_odd_triples()` in [the pipeline checker](check_regular_path_sweep_pipeline.py) enumerates the label scheme of the main note's 344 closed and 945 open configurations. It excludes configurations violating the local hypothesis. It finds simple covers in 125 closed and 386 open cases and asserts the exception pattern for the other 12 open cases. Each cover is rechecked as an exact edge partition. The enumeration is a superset of the realizable configurations because it imposes only (o1)–(o5).

**Completion for one cycle.** If \(L=3\), apply Lemma 4. Suppose \(L\ge5\) and some block of three consecutive trails has a simple cover. Use it, then pair the remaining even chain. Otherwise every index is the middle index of a failing block, so \(d_i\in\{A_{i-1},A_{i+1}\}\) for every \(i\). Define \(\varphi(i)=j\) when \(A_j=d_i\). This map is well defined and injective by (o1) and (o5). If \(\varphi(i)=i+1\) and \(\varphi(i+2)=i+1\), injectivity fails. Hence a step of \(+1\) at \(i\) forces a step of \(+1\) at \(i+2\). Since \(L\) is odd, all steps are equal. If \(A_i=d_{i+1}\) for all \(i\), use

\[
(A_i,b_i,c_{i-1},d_{i-1},c_{i-2},b_{i-2}).
\]

If \(A_i=d_{i-1}\) for all \(i\), use

\[
(A_i,b_i,c_i,d_{i+1},c_{i+1},b_{i+2}).
\]

Under the hypothesis of Theorem A, the second rotation is never needed. Since \(b_i=s(e_i)=s(c_{i-1})\), the equality \(A_i=d_{i-1}\) makes \(b_id_{i-1}\) an edge, and the \(M\)-triangle \(b_ic_{i-1}d_{i-1}\) shares \(c_{i-1}d_{i-1}\) with the \(M\)-square of \(T_{i-1}\). So under that hypothesis the Lemma 4 exception is exactly \(d_1=A_0\). The second rotation is kept because Proposition B uses it. (Independent review, issue m2.)

`verify_pair_and_rotations()` checks symbolically that both rotations re-partition the cycle edges for \(L=3,5,7,9\). The general index computation is identical. In each piece the two \(b\)-labels differ and avoid the \(c\)-labels by (o2). The \(d\)-label avoids both adjacent \(b\)-labels by (o3). The pendant \(A_i\) is the \(d\)-label of another trail, so it differs from the displayed \(d\)-label and every \(c\)-label. It avoids all \(b\)-labels by (o4).

*Proof of Theorem A.* Apply Lemma 1, the sweep, Lemma 3, and Section 3. Without triangle–square conflicts, every exceptional case in Lemma 3, every bad pendant in a pair, and every local violation in Lemma 4 is excluded. Every final piece is therefore a simple five-edge path, and the pieces partition \(E(G)\). \(\square\)

## 4. The diamond-free case

A *diamond* is \(K_4\) minus an edge, or equivalently two triangles sharing an edge. Graphs satisfying the Chu–Fan–Hong–Zhou hypothesis are diamond-free. A diamond yields a 4-cycle sharing edges with its triangles. Diamond-free graphs may have triangles sharing edges with unchorded 4-cycles.

**Proposition B.** Let \(G\) be diamond-free and \(M\) any perfect matching. After the sweep, every piece is a simple path except possibly type-0 targets of the form

\[
Q'=(b,c,f,b,h,Y),\qquad fb\in M,\ r(f)=c,\ r(c)=b,\ h=r(b),
\]

where \(Y\) is \(s(h)\) or \(r(h)\). Such a piece is called a G-configuration. It has exactly one repetition.

*Proof.* In Lemma 3, \(A=d\) gives triangles \(bcd,bde\) sharing \(bd\). The cases \(s(c)=e\) and \(r(e)=c\) give triangles \(cde,cbe\) sharing \(ce\). Both are diamonds. A pair-replacement failure is the chord case. `verify_odd_triples()` also runs Lemma 4 with "no local diamond" in place of the conflict condition. All 259 closed and 564 open admissible cases have simple covers, except 24 open cases with \(d_1\in\{A_0,A_2\}\). The rotation argument then applies. Both ends of one type-0 target cannot be exceptional. That would require triangles \(bcf,bfh\) sharing \(fb\), another diamond. \(\square\)

**The G-rule.** Let \(W_0=\tau(pq)\) be the canonical trail with \(f\) as a red head, where \(p=r^{-1}(f)\). Write its post-sweep piece as \(W=(s(f),f,p,q,u,Z)\). Replace \(Q',W\) by

\[
Q''=(s(f),f,c,b,h,Y),\qquad W'=(b,f,p,q,u,Z).
\]

This exchanges \(\{f,b\}\in M\) with \(\{s(f),f\}\in S\).

*Proved subcase.* Suppose \(W_0\) is not defective and \(W\) is not itself a G-configuration. Then both new pieces are simple paths. The terminal \(s(f)\) differs from \(f,c,b\) by (P1). It differs from \(h\) because the triangle \(fbh\) would share \(fb\) with \(bcf\). If \(Y=s(h)\), then \(s(f)\ne Y\) because \(f\ne h\). If \(Y=r(h)\), equality would make the source at \(h\) have \(e\)-label \(f\), so that source would be \(W_0\). In \(W'\), \(b\ne p\) because \(r(b)=h\ne f\), and \(b\ne q\) because \(q=b\) would give \(p=f\). Next, \(b=u\) would give \(q=c\), \(p=d\) and \(e=f\), making \(ce\) a diamond chord. Finally, \(b=s(u)\) would give \(u=e\) and then \(r(c)=f\). The equality \(b=r(u)\) would give \(u=c\), then \(q=f\) and \(r(b)=f\). Both are contradictions.

*Open subcases.* The remaining cases are \(f=b_{W_0}\), where \(W_0\) is defective with repeated vertex \(f\), and \(f=e_{W_0}\). In the second case \(W_0\) is necessarily a source, and \(f\) sits at position 2 of its piece, so the rule as stated does not apply. Other open cases are \(W_0\) on an odd cycle and chains in which \(W\) is itself a G-configuration. A proof of the diamond-free case needs a second sweep with link analysis for these cases. This analogue of Section 2 has not been done.

*Evidence.* Diamond-free random graphs were generated with planted triangles and matchings preferring triangle edges. With `--diamond-free 40`, the run used 160 graphs. The sweep left 14 G-configurations and no other defect. Applying the G-rule sequentially gave verified decompositions in all 160. An earlier scratch run gave 27 more graphs with 28 G-configurations, all fixed. This is evidence, not proof.

## Verification

```powershell
Set-Location research/2026-11-25-target-shortlist
python check_regular_path_sweep_pipeline.py                    # about 45 s
python check_regular_path_sweep_pipeline.py --diamond-free 40  # adds about 1 min
```

The checker reimplements the construction and sweep from the text, independently of the earlier scratch code. Each run verifies the edge partition, the endpoint condition and the five-edge trail shape. It requires every piece to be a path or to repeat only at distance three from an endpoint.

**Scope of the end-to-end runs.** These runs are evidence only, and they do not implement Section 3 as written. The odd-cycle branch of `sweep()` always uses the block \((0,1,2)\) and accepts a triangle cover. It never searches other blocks or applies the rotations. In the default run, the only hypothesis-satisfying runs were the 300 far3 runs, which have no \(M\)-triangle, and 9 \(K_5\)-style runs. None of the eight odd type-2 cycles occurred in a hypothesis-satisfying run. So these runs give no evidence for Section 3 or for \(M\)-triangle-rich inputs. That coverage comes from the independent reviewer's checker, [check_regular_path_theoremA_independent.py](check_regular_path_theoremA_independent.py). It plants odd type-2 cycles in generic \((M,r,s)\) data satisfying (P1)–(P3), applies Section 3 as written, and verified 1,600 planted and 1,348 generic hypothesis instances. See [the review](04-REVIEW-theorem-A.md). The proof relies only on Lemmas 1–4 and the symbolic checks.

## Self-review

- **Scope.** The theorem is matching-relative. Corollary 4 is the cleanest graph-level consequence. Theorem A says nothing about graphs whose every perfect matching has a triangle–square conflict. Examples include \(K_6\) components, many \(K_4\)-rich graphs and the Problem 5 graph.
- **Dependence on earlier claims.** Lemma 3 was rederived line by line. Its source-endpoint argument uses the alternation rule that no source receives from a source. Lemma 4 reuses the earlier label scheme. Its completeness rests on (o1)–(o5), which were reproved here, including the external-terminal argument (o4) for changed pendants.
- **An earlier gap checked.** The rotation for \(A_i=d_{i+1}\) needs \(A_i\ne b_{i-2}\). This holds by (o4) for both unchanged and changed pendants.
- **Computer assistance.** Lemma 4 is an exhaustive finite enumeration. All other steps are written arguments. Random tests are not used as proof.
- **Novelty (updated).** The coordinator read the FGK full text; see [04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md). Theorem A is not in FGK, and the two results are incomparable. This closes review issue M1 subject to the presentation fixes above, which have been applied. Later citers of FGK were checked only to a bounded extent. *Earlier note:* this is a bounded search, not a certificate. FGK's Theorems 6–7 concern extendability of a prescribed matching as the middle-edge set. Theorem A gives unrestricted decompositions, so it is a different statement. No source checked states Theorem A or Corollary 4. Sources checked: FGK via secondary descriptions, since the full text returned 403; BMW 2015 and its Eurocomb abstract; Chu–Fan–Hong–Zhou 2024; Botler–Hoffmann 2022; Montgomery–Müyesser–Pokrovskiy–Sudakov 2025; Patel–Yıldız arXiv:2411.06982; and web searches for 2025–2026 preprints. (The earlier M1 risk, raised from the FGK abstract's terms "\(M\)-triangles", "\(M\)-squares" and "bad pairs of \(M\)-cycles", is resolved by the full-text comparison.)
- **Independent review.** [04-REVIEW-theorem-A.md](04-REVIEW-theorem-A.md) (2026-11-25) found no fatal or major mathematical error. Its verdict was ACCEPT WITH FIXES. Minor fixes m1–m8 have been applied here.
