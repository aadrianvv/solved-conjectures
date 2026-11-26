# Degree five with diamonds: exception catalogue and plan

**Status: research plan with exploratory data. No new theorem.** This note extends [04e](04e-regular-path-diamond-free.md), which treats the diamond-free case, to graphs containing diamonds.

## 1. Exceptions after the first sweep in general graphs

Lemma 3 and Section 3 of 04d, without the diamond-free hypothesis, leave the following non-path pieces. Each comes from a triangle that shares an edge with the defect's \(M\)-square.

| Code | Piece | Condition | Local structure |
|---|---|---|---|
| X1 | Source \((d,b,e,d,c,s(c))\) or recipient \((d,b,c,d,e,r(e))\) | changed pendant \(A=r(b)=d\) | (P5) fails at \(b\): \(c\to b\to d\) in \(R\), \(cd\in M\) |
| X2 | Source \((A,b,e,d,c,e)\) | \(s(c)=e\) | Diamond \(bcde\) with chord \(ce\). At the apex \(e\) the matched pair is \(\{R\text{-in},S\text{-out}\}=\{d,c\}\) |
| X3 | Recipient \((A,b,c,d,e,c)\) | \(r(e)=c\) | (P5) fails at \(e\) |
| X4 | G-configuration \((b,c,f,b,h,Y)\) | as in 04e | Now also diamonds; the windows fail only through \(s(f)=h\) |
| X5 | Type-0 target with G-configurations at both ends \((g,c,f,g,h,f)\) | triangles \(cfg\) and \(fgh\) share \(fg\in M\) | Diamond with \(M\)-spine |
| X6 | Odd type-2 cycles | pair chord \(A_i=d_i\), Lemma 4 failures, rotation exceptions | — |

So X1, X3, X4 and X5 all come from (P5) violations, and X2 from the pair \(\{R\text{-in},S\text{-out}\}\).

**Exploratory frequencies.** In 400 random general graphs of the square, dense, \(K_5\)-block and random styles, the non-path pieces after the sweep were:

- 189 X2, the dominant case;
- 17 X1;
- 2 X1+X2 together;
- 4 X3;
- 53 single X4;
- 1 X5.

## 2. Local repair: empirical status

- A single lollipop exchange removed most non-path pieces. For a lollipop \((x,y,z,x,w,v)\), it moves the triangle edge \(xz\) into a piece \((t,z,\dots)\) and takes \(zt\).
- Adding a 2-cover or 3-cover fallback by exhaustive search solved **400/400** graphs.
- For X2 in particular, a single exchange worked in 131 of 189 cases, another 2-cover in 32, and 3 pieces were needed in 26.

These runs are evidence only. The scratch scripts were `lolli*.py` in the session scratchpad.

## 3. The D-rule for X2, a first window

Reverse the X2 piece to \((e,c,d,e,b,A)\). Its partner is the canonical trail \(W_d=\tau(\delta\,m(\delta))\) with \(\delta=r^{-1}(d)\), which has \(d\) as a red head. The \(d\)-end of \(W_d\) is never changed by the first sweep: the only source with \(c\)-label \(d\) would be \(T\) itself, oriented the other way.

The rule is
\[
(A,b,e,d,c,e)\ \mapsto\ (s(d),d,c,e,b,A),\qquad W_d:\ s(d)\mapsto e.
\]

Label-engine run without diamond-freeness, with \(W_d\) not defective:

- \(S'\) is always simple.
- \(W_d'\) fails only when \(e=m(\delta)\), so (P5) fails at \(d\), or when \(W_d=Q_T\) is \(T\)'s own target.

The cases with \(W_d\) defective (β-like and γ-like) had no failure of \(S'\) in the plain setting.

## 4. Plan

1. Define partner rules for X1–X5, as the 04e case split did for X4. Classify partners into α/β/γ-like cases, and record which rules can share pieces.
2. Run the 04e window engine with `diamond_free = False`. The engine supports this through `Scenario.diamond_free`.
3. Redo Lemma 4 for the general local structure. The 12 non-diamond-free exceptions with \(d_1\in\{A_0,A_2\}\) are known, but in general there are failures caused by conflicts, and these need new rules.
4. Extend [check_regular_path_diamond_free.py](check_regular_path_diamond_free.py) to the general case, as an end-to-end test.

Alternative route: if (P5) can be imposed, which is open even in the diamond-free case (see 04-HANDOFF.md), then X1, X3, X4 and X5 disappear, and only X2 and X6 remain.

**D-rule, further window data (engine without diamond-freeness).** \(W_d\) is not defective, its far end is plain, and \(W_d\ne Q_T\). Then 78 of 252 identifications fail, all with \(e=m(\delta)\). This is a (P5) violation at \(d\): the \(R\)-path \(\delta\to d\to e\) has \(\delta e\in M\).

When the far end received \(b_z=r(u_2)\) from a source, the failures are:

- \(e=m(\delta)\): 918 identifications;
- \(\delta=b_z\): 914 identifications. Here \(W_d\) is itself a G-configuration at its far end, the analogue of the 04e α2 chain;
- both together: 345 identifications.

The general case will therefore need a second exchange at \(d\) when (P5) fails there, and the chain/alternation handling of 04e.

**A possible unified matching-relative theorem.** Theorem A forbids every triangle–square conflict. Theorem B forbids diamonds. The 04e machinery seems to need only that the first-sweep exceptions are G-configurations and that the windows contain no diamond identifications. A matching-relative hypothesis such as "no diamond contains an edge of an \(M\)-square" may suffice. Checking it would need the windows rerun with that local hypothesis in place of global diamond-freeness. Not yet attempted.
