# Degree five with diamonds: (P5) fails for fixed M; Theorem B′; the (P5) route

**Status (2026-11-25, session 4; review fixes applied 2026-11-26).** Research note. Conjecture 1 remains open in degree five.

- §1 **Negative result:** (P5) cannot always be imposed for a *given* perfect matching. Verified by an independent brute force.
- §2 **Theorem B′** (matching-relative extension of Theorem B): if no diamond contains an edge of \(M\), then \(G\) decomposes. Its proof is the reviewed 04e proof with every diamond appeal replaced by an M-diamond appeal (table mirrors 04e Lemmas 7–8); all windows were re-run. **Independently reviewed (accept with fixes; fixes applied)**, [04-REVIEW-theorem-Bprime.md](04-REVIEW-theorem-Bprime.md). A strengthening inside the Theorem B entry, not a separate result.
- §3 **Theorem C** (computer-assisted; **independently reviewed (accept with fixes; fixes applied)**, [04-REVIEW-theorem-C.md](04-REVIEW-theorem-C.md)); a *conditional reduction*, not a solved case: if \(M\) and \((r,s)\) satisfy (P1)–(P3) and (P5), then \(G\) decomposes. All windows pass (0 failures), including the D-chains (absorption on paths, a new D-rotation on cycles); end-to-end runs verify every output.
- §4 **Conjecture P5\***: every 5-regular graph with a perfect matching has *some* perfect matching \(M\) admitting (P5). Exhaustive at orders 8 and 10. **Update (2026-11-26): P5\* is false.** A 30-vertex graph with three bridges has no perfect matching admitting (P5) ([04i](04i-regular-path-p5star-counterexample.md)). The graph itself decomposes into five-edge paths, so it is not a counterexample to Conjecture 1.

Notation is that of 04d/04e: \(r,s\) fixed-point-free permutations with (P1)–(P3), \(m\) the mate map, canonical trails \(\tau(uv)\), defects \(T=(a,b,c,d,e,b)\).

## 1. (P5) is not always achievable for a fixed matching

(P5): \(m(r^{-1}(x))\ne r(x)\) for all \(x\), i.e. no R-path \(u\to x\to y\) with \(uy\in M\).

**Reformulation.** Choosing \((r,s)\) with (P1)–(P2) is the same as choosing an Euler orientation of \(H=G-M\) and a directed 2-factor \(R\) in it (each vertex one R-in, one R-out arc); \(s(w)\) is the tail of the non-R arc entering \(w\). For an *M-pair* at an apex \(c\) (two H-edges \(cx,cy\) with \(xy\in M\)):

- (P3) ⇔ the two pair edges are not both directed into \(c\);
- (P5) ⇔ the two pair edges are not both in \(R\).

**Counterexample.** \(G\) on \(\{0,\dots,7\}\) with neighbourhoods \(0{:}12347,\ 1{:}03456,\ 2{:}03567,\ 3{:}01245,\ 4{:}01367,\ 5{:}12367,\ 6{:}12457,\ 7{:}02456\) and \(M=\{57,26,13,04\}\). An exhaustive search over all Euler orientations of \(H\) (94 of them) and all choices of \(r\) finds **no** \((r,s)\) with (P1)–(P3) and (P5). Two independent programs agree: the CSP solver `p5solve.py` and the brute force `brute8.py` (scratch, recorded in `04-handoff/p5_scratch/`).

Further data (CSP, exact per instance):

| sample | (P5) infeasible for the given \(M\) |
|---|---|
| random 5-regular, \(n=8\), up to 100 matchings each | 192 of 932 |
| \(n=10\), 60 graphs, ≤60 matchings | 57 of 3,600 |
| \(n=12\), 60 graphs, ≤30 matchings | 3 of 1,800 |
| \(n=12\), matchings with at most one M-pair per vertex | 10 infeasible (so even "≤1 pair per apex" does not suffice) |
| stronger structures: pairs split in/out (V1) | infeasible on random and dense graphs |
| pairs split and one R-edge per pair (V2) | infeasible on most dense graphs |

So the lead "(P5) can always be imposed" is **false for fixed \(M\)**. The handoff observation (feasible on 102 diamond-free graphs) is consistent with this: those graphs are sparse in M-triangles.

## 2. Theorem B′: no diamond through the matching

**Theorem B′.** Let \(G\) be a finite simple 5-regular graph with a perfect matching \(M\) such that no diamond of \(G\) contains an edge of \(M\) (as a side or as the chord). Then \(E(G)\) partitions into paths with five edges.

Equivalently: every triangle through an \(M\)-edge is edge-disjoint from every other triangle. In particular, the ends of an \(M\)-edge have at most one common neighbour.

**Scope.** It contains Theorem B (diamond-free graphs, every \(M\)) and Corollary 4 of Theorem A (no \(M\)-edge in a triangle). It allows arbitrarily many diamonds, K4's and K5-minus-edge blocks as long as \(M\) avoids their edges. It does not cover graphs in which every perfect matching meets a diamond (e.g. \(K_6\), \(C_k[K_2]\)). B′ and Theorem A of 04d are incomparable: B′ allows an \(M\)-triangle to share its \(M\)-edge with an \(M\)-square (a triangle–square conflict, but no diamond), while Theorem A allows two \(M\)-triangles with a common \(M\)-edge (an \(M\)-chord diamond) when no \(M\)-square meets them. B′ contains Corollary 4 of Theorem A. B′ is presented as a strengthening within the Theorem B entry, with its own audit; it is not counted as a separate result.

**Proof.** Follow 04d and the reviewed 04e (Sections 1–4, Lemmas 5, 7 and 8, the proof of Theorem B) word for word, with "diamond" replaced by "diamond through an \(M\)-edge" at each appeal listed below. In every case the diamond that the text exhibits already contains an edge of \(M\), so the hypothesis of Theorem B′ excludes it. No other step of 04d or 04e uses diamond-freeness. (Checked by reading every occurrence of "diamond" in 04d and in 04e as revised after its review, which accepted 04e with fixes, now applied; 04d and 04e are not edited here. The independent referee of B′ repeated this search, including triangle, chord and \(K_4\) appeals, and found no further appeal.)

| place in 04d / 04e | diamond exhibited | M-edge in it | how \(M\) membership is known |
|---|---|---|---|
| 04d Prop. B / Lemma 3, \(A=r(b)=d\) | triangles \(bcd,bde\) share \(bd\) | \(cd\) (side) | \(m(c)=d\) |
| 04d Prop. B / Lemma 3, \(s(c)=e\) or \(r(e)=c\) | triangles \(cde,cbe\) share \(ce\) | \(cd\) (side) | \(m(c)=d\) |
| 04d Prop. B, both ends of a type-0 target exceptional | triangles \(bcf,bfh\) share \(fb\) | \(fb\) (chord) | \(m(f)=b\) |
| 04d Prop. B, pair replacement \(A_i=r(b_i)=d_i\) | triangles \(b_ic_id_i,b_id_ie_i\) share \(b_id_i\) | \(c_id_i\) (side) | \(m(c_i)=d_i\) |
| 04d Prop. B, Lemma 4 (diamond-free run) | any local diamond | — | **replaced by the computer run below** (local diamond through a known \(c_id_i\)) |
| 04d G-rule "proved subcase", \(s(f)
e h\) | triangles \(fbh,bcf\) share \(fb\) | \(fb\) (chord) | \(m(f)=b\); superseded in 04e by windows W1/W3 |
| 04d G-rule "proved subcase", \(b
e u\) | chord \(ce\) of the square \(bcde\) | \(cd\) (side) | \(m(c)=d\); superseded in 04e by windows W1/W3 |
| 04e Lemma 8, Step 1 (one configuration per \(Q\)) | triangles \(bcf,bhf\) share \(fb\) | \(fb\) (chord) | \(m(f)=b\) |
| 04e Lemma 8, Step 2 (Γ-source \(W\) has no other partner end, \(f'=q\)) | \(gp\) chord of \((g,q,p,f)\); triangles \(gqp,gpf\) | \(qp\) (side) | \(m(p)=q\); the appeal is redundant, since Lemma 5(i) of 04e already shows that \(\{q,s(q)\}\) is not a partner edge |
| 04e Lemma 8, Step 4 (no G-pendant at \(T_c\)) | triangles \(fhb,bcf\) share \(fb\) | \(fb\) (chord) | \(m(f)=b\) |
| 04e Lemma 7 (a), (b) | none: the proof uses only (o2), injectivity of \(r\) and uniqueness of the trail with a given \(c\)-label | — | — |
| 04e Lemma 4′ (243 cases excluded by local diamonds) | any local diamond | — | **replaced by the computer run below**; the M-edges known locally are the \(c_id_i\) and the G-pendant edges \(b_iA_i\) (\(A_i=m(b_i)\)) |
| 04e windows W1–W8 (engine axiom "known edges diamond-free") | any diamond in the known edges | — | **replaced by the computer run below** (engine axiom: no diamond through a known \(M\)-edge) |
| 04e Section 3 rules, Lemma 5, Γ′ wording, rotation telescoping, (P2) clause | none | — | — |

The proof of Theorem B's final paragraph (partition and shape) then applies unchanged, since its only inputs are Lemma 8, Lemma 4, Lemma 4′, the symbolic exchange checks and the windows. The window facts of 04e §4 (including the W3 fact \(Z\ne p\)) use no diamond appeal.

The computer steps were re-run with the engine's diamond test replaced by "the known edges contain no diamond through a known \(M\)-edge" — a necessary condition under the hypothesis, so the enumeration remains a superset and a pass is sound. [check_regular_path_mdiamond.py](check_regular_path_mdiamond.py) (imports and patches the audited 04e checkers without modifying them):

- Lemma 4 (M-diamond form): 259 closed and 564 open simple covers; 24 open exceptions with \(d_1\in\{A_0,A_2\}\); 442 excluded. (Same counts as the diamond-free run. This is expected: in the Lemma 4 and 4′ label schemes every local diamond contains a known \(M\)-edge, \(c_id_i\) or a G-pendant edge \(b_iA_i\); the referee's own enumeration found 0 local diamonds avoiding \(M\). So under B′ these are literally the same finite statements as under diamond-freeness.)
- Lemma 4′ (G-pendants; their edges \(b_iA_i\) count as known \(M\)-edges): 205 closed, 548 open covers, 12 open exceptions, 243 excluded.
- Windows W1–W8 of 04e: **0 failures** in every window. Identification counts grow where expected (e.g. the W7 excluded counts are 532, 17,021, 18,779 against 527, 16,365, 18,467 under full diamond-freeness), confirming that the hypothesis is genuinely weaker.

The run used the current `check_regular_path_gsweep.py` (last modified 22:14, before the run; it already contains the W3 fact \(Z\ne p\)) and the unchanged engine. Run: `python check_regular_path_mdiamond.py` (about 25 min; log in `04-handoff/p5_scratch/mdiamond_run1.log`). Rerun after the review fixes (2026-11-26, log `04-handoff/p5_scratch/mdiamond_rerun_fixes.log`): self-test passed, Lemma 4 259/564/24 with 442 excluded, Lemma 4′ 205/548/12 with 243 excluded, all windows 0 failures, total failures 0.

**Status:** independently reviewed (accept with fixes; fixes applied), [04-REVIEW-theorem-Bprime.md](04-REVIEW-theorem-Bprime.md). The referee reran the author's checker and all of W1–W8 with an independently written M-diamond filter, which gave identical identification sets, and verified 701 end-to-end decompositions on data with many diamonds avoiding \(M\) (a control run with the hypothesis off fails). It rests on the reviewed 04e plus the substitutions above. Points a reviewer should check: (i) that the table lists every diamond appeal in 04d/04e; (ii) that the engine patch `MState.m_diamond_through` detects exactly the diamonds through a known \(M\)-edge among the known edges (both the chord and the side positions of the new edge); `selftest()` (run first by `main()`) confirms on four small scenarios that a diamond with an \(M\)-chord or an \(M\)-side is rejected while a diamond without an \(M\)-edge, or with an \(M\)-edge outside it, is kept, and that the unpatched engine keeps all four; (iii) that `local_m_diamond` in the Lemma 4/4′ re-runs uses only the \(M\)-edges known in those label schemes.

## 3. Theorem C program: (P5) reduces everything to X2

**Proposition C1.** If \((r,s)\) satisfy (P1)–(P3) and (P5), then after the first sweep (04d §2–3) every piece is a simple path except X2 sources \((A,b,e,d,c,e)\) with \(s(c)=e\).

*Proof.* Lemma 3's exceptions: \(A=r(b)=d\) gives the R-path \(c\to b\to d\) with \(cd\in M\); \(r(e)=c\) gives \(d\to e\to c\); a G-configuration has \(f\to c\to b\) with \(fb\in M\). All violate (P5). The remaining exception is \(s(c)=e\). On odd type-2 cycles, a pair fails only for a changed pendant \(r(b_i)=d_i\), again \(c_i\to b_i\to d_i\). Lemma 4 was re-run with (P5) as the only extra restriction (changed \(A_i\ne d_i\)): 259 closed and 720 open covers, 286 excluded, and exactly 24 open exceptions with \(d_1\in\{A_0,A_2\}\); the rotation completion of 04d §3 uses only (o1)–(o5). \(\square\)

Under (P5) there are no G-configurations, so none of the 04e machinery is needed. Moreover, for a defective \(T\), if \(ce\) is an edge then \(s(c)=e\): \(ce\notin M\); \(ce\in R\) would give \(r(e)=c\) (a (P5) violation at \(e\)) or \(r(c)=e\ne b\); and \(ce\in S\) with \(s(e)=c\) contradicts \(s(e)=b\). So X2 is exactly a source whose square \(bcde\) has the chord \(ce\).

**Second sweep for X2 (D-rule family).** Let \(\delta=r^{-1}(d)\), \(\mu=m(\delta)\), \(u=r(\mu)\), and \(W_d=\tau(\delta\mu)\) (the trail in which \(d\) is a red head). Its terminal edge \(\{d,s(d)\}\) is never moved by the first sweep.

- (α) \(W_d\) not defective: \(S'=(s(d),d,c,e,b,A)\), \(W'_d=(e,d,\delta,\mu,u,Z)\) (exchange \(ed\leftrightarrow d\,s(d)\)).
- (β) \(W_d\) defective with \(b'=d\): before \(W_d\) is processed its pendant \(s(d)\) is replaced by \(e=r(d)\) (a *D-pendant*, of the same form \(r(b')\) as a type-1 pendant); \(T\) becomes \(S'\).
- (γ) \(W_d\) defective with \(e'=d\), so \(W_d=(s(u),u,\mu,\delta,d,u)\), \(u=s(d)\). \(W_d\) has no incoming type-2 link, so it is a source.
  - link of type 0 or 1: **absorption** — \(W_d\) does not trade and becomes \((A',u,\mu,\delta,d,e)\); \(T\) becomes \(S'\).
  - link of type 2: **Γ_D** — \(N_1=(s(\mu),\mu,\delta,d,c,e)\), \(N_2=(A,b,e,d,u,A')\).
  - type 2 with (F1) \(s(\mu)=c\): then \(W_d\)'s recipient is \(X=Q_T\) (with \(b_X=c\), \(e_X=\mu\)), and **rule F**: \((A,b,c,d,u,A')\), \((b,e,d,\delta,\mu,c)\), \((e,c,f,d_X,\mu,u)\).

Pendant options everywhere: plain \(s(\cdot)\), type-1 \(r(\cdot)\), D-pendant \(r(\cdot)\); far-end options: plain, received, D-linked. "Plain" is encoded as: no named source has that c-label and no named X2 has that d-label.

**Checks** ([check_regular_path_p5sweep.py](check_regular_path_p5sweep.py), engine + (P5) axiom, diamond-freeness off): \(S'\) (3 options), α (3), β source/recipient, γ-absorbed (3), Γ_D (9 option pairs, up to 25,065 identifications each): **0 failures**, with exactly one allowed exclusion each: (F1) in Γ_D, and in \(S'\) the identification \(\mu=b\) of case γ (there \(W_d\) is absorbed, so \(T\)'s pendant is plain). Rule F was found by the symbolic re-partition search `find_rules` and is uniform over all 9 option pairs (11,530 identifications, 0 uncovered).

### 3.1 Theorem C

**Theorem C** (independently reviewed, accept with fixes; fixes applied, [04-REVIEW-theorem-C.md](04-REVIEW-theorem-C.md)). Let \(G\) be a finite simple 5-regular graph with a perfect matching \(M\), and let \(r,s\) satisfy (P1)–(P3) and (P5). Then \(E(G)\) partitions into paths with five edges.

**Scope: a conditional reduction, not a solved case.** (P5) is a property of the data \((M,r,s)\), and §1 shows that it can fail for every \((r,s)\) with a fixed \(M\). Theorem C would give the degree-five case only together with Conjecture P5\* (§4), and **P5\* is false in general**: [04i](04i-regular-path-p5star-counterexample.md) gives a 30-vertex graph, with bridges, in which no perfect matching admits (P5). Theorem C must not be counted as a solved conjecture. Its unconditional by-product: if no edge of \(M\) lies in a triangle, every \((r,s)\) from Lemma 1 satisfies (P5) (an R-path \(u\to x\to m(u)\) would give the triangle \(u\,x\,m(u)\)), which recovers Corollary 4 of 04d. It needs none of the 04e machinery (no G-configurations exist under (P5)).

### 3.2 Lemmas

**Lemma C2 (X2 sources have link type 0 or 1).** Let \(T\) be X2, so \(s(c)=e\). If its target \(Q\) (the trail with red head \(c\)) were defective with \(e_Q=c\), then \(b_Q=s(e_Q)=s(c)=e=r(d)\) and \(b_Q=r(c_Q)\), so \(c_Q=d\) and \(Q=\tau(dc)=T\). But a target is never its own source. \(\square\)

Consequently, removing the trade of an X2 source (absorption, cancellation) never changes the type-2 alternation, the recipients or the odd type-2 cycles. An X2 source may still have an *incoming* type-2 link, from a non-trading recipient (when it sits at an even position \(\ge2\) on a type-2 path). This is harmless: that recipient does not trade, so nothing is given to or taken from the X2, and removing the X2's own (type 0 or 1) trade does not affect the alternation.

**Lemma C3 (partner structure).**

- (i) The edge \(\{d,s(d)\}\) is not moved by the first sweep: a source taking it would have \(c\)-label \(d\) (but the defect \(\tau(dc)=T\) has \(c\)-label \(c\)), or \(c\)-label \(x=s(d)\) with \(s(x)=d\), contrary to (P2).
- (ii) \(W_d\ne T\), since \(d\) is not a red head of \(T\) (its red heads are \(b,e\)).
- (iii) A trail \(W\) is the D-partner of at most two X2 sources, one per red head: the X2 with \(d\)-label equal to that red head (the defect \(\tau(x\,m(x))\) has one orientation). A non-defective \(W\) can be α at both ends; a defective \(W=(a',b',c',d',e',b')\) can be β (at \(b'\)) and γ (at \(e'\)).
- (iv) The pendant of a defective trail is changed by at most one rule: the type-1 trade of the source with \(c\)-label \(b'\), or the D-pendant of the X2 with \(d\)-label \(b'\). Both are orientations of \(\tau(b'm(b'))\), so they exclude each other. A type-1 trade into \(W_d\) in case β would need a source with \(c\)-label \(d\): none.
- (v) In case γ, \(W_d\) has no incoming type-2 link (it would need a source with \(c\)-label \(e'=d\)), so it is a source and lies on no type-2 cycle.

**Lemma C4 (D-chains).** Write \(T\to T^*\) when the γ-partner of the X2 source \(T\) is itself X2 (i.e. \(s(\mu)=d\)). Out-degree ≤ 1 (one partner) and in-degree ≤ 1 (\(T^*\) is γ-partner only of the X2 with \(d\)-label \(e_{T^*}\)). So the D-chain graph is a union of directed paths and cycles. Along an edge, \(b_{j+1}=s(d_j)\), \(c_{j+1}=\mu_j\), \(d_{j+1}=r^{-1}(d_j)\), \(e_{j+1}=d_j\). A cycle has length \(L\ge3\): \(L=2\) would give an R-2-cycle \(d_0\to d_1\to d_0\), contrary to (P2).

- **Paths:** the first node *exists*; existing and *cancelled* nodes alternate. An existing node absorbs its cancelled successor (legitimate by Lemma C2); a cancelled node applies no rule and does not trade.
- **Cycles (any length):** the **D-rotation**
  \[
  S_j=(A_j,b_j,d_{j-1},d_j,c_j,d_{j-1})\ \longmapsto\ P_j=(A_j,b_j,d_{j-1},c_j,d_j,d_{j+1}).
  \]
  Each \(S_j\) gives away its R-edge \(d_{j-1}d_j\) and receives \(d_jd_{j+1}\) from \(S_{j+1}\); summed over the cycle this telescopes (`symbolic_rotation`, \(L=3,\dots,9\); the index computation is uniform in \(L\)). Simplicity: window "D-rotation" on three consecutive nodes (open, \(L\ge4\)) and on the closed \(L=3\) cycle. It uses one extra fact, \(A_j\ne d_{j+1}\), which holds because \(d_{j+1}=e_{j+2}\) is the endpoint of \(S_{j+2}\ne S_j\), and in any partition of a 5-regular graph into 5-edge trails every vertex is an endpoint exactly once (degree parity and counting: \(n/2\) trails, \(n\) endpoint slots, each vertex needs an odd number). The partition used must contain both \(S_j\), with its final pendant, and \(S_{j+2}\): it is the first-sweep partition (all of whose pieces are trails) when \(A_j\) is plain or a type-1 pendant, and the first-sweep partition after the single D-pendant exchange when \(A_j\) is a D-pendant. That exchange does not touch \(S_{j+2}\), whose only D-partner is \(S_{j+3}\).

  Without this fact the open window fails exactly when \(A_j=d_{j+1}\), so the fact is essential and must be checked by a reviewer.

**Rule choice for an existing X2 \(T\)** (cancelled X2 do nothing):

| partner | rule | window |
|---|---|---|
| α | D-rule | \(S'\), α |
| β | D-pendant on \(W_d\), \(T\mapsto S'\) | \(S'\), β (non-X2 \(W_d\)); \(S'\) with A=Dpend (X2 \(W_d\)); Lemma 4 under (P5) (odd-cycle \(W_d\)) |
| γ, \(W_d\) cancelled X2 | absorption | \(S'\), γ-absorbed (no constraint on \(s(\mu)\)) |
| γ, \(W_d\) non-X2, link 0/1 | absorption (\(W_d\)'s trade removed) | \(S'\), γ-absorbed |
| γ, link 2, \(s(\mu)\ne c\) | Γ_D | Γ_D (9 option pairs) |
| γ, link 2, \(s(\mu)=c\) | rule F (uses \(X=Q_T\) whole) | rule F (9 option pairs) |
| T on a D-cycle | D-rotation | D-rotation |

**Lemma C5 (removed trades).** Only trades of type 0 or 1 are removed (Lemma C2 for X2; the absorption rule is used only for links 0/1). A removed type-0 trade leaves the target's end plain; a removed type-1 trade leaves the pendant plain. These are the "plain" options of the windows; Lemma 3 of 04d is per end and per pendant.

**Lemma C6 (D-pendants on odd type-2 cycles).** A D-pendant \(r(b_i)=e\) (with \(b_i=d\) the \(d\)-label of an existing X2 \(T\)) satisfies the facts used for changed pendants in Lemma 4: it is not a \(c\)- or \(e\)-label (\(r(b_i)=r(c_j)\) gives \(b_i=c_j\), contrary to (o2); \(r(b_i)=r(d_j)\) gives \(b_i=d_j\), but \(b_i=d\) is a matching endpoint of \(T\), which is a source and not on the cycle); not a \(b\)-label (\(r(b_i)=r(c_j)\)); not \(d_i\) (P5 at \(b_i\)); distinct from changed pendants (\(r\) injective) and from unchanged ones: \(e=s(b_k)\) gives \(b_k=c\), so \(T_k=Q_T\), into which the trading \(T\) makes a type-1 trade, so \(T_k\)'s pendant is not unchanged. The Lemma 4 run under (P5) enumerates changed pendants with exactly these restrictions.

**Lemma C7 (interfaces).** All rules are applied simultaneously; D-pendants are applied before odd type-2 cycles are processed.

- A rule acting on a piece acts at its own end: the D-rule at the \(d\)-end of \(W_d\), the D-pendant at \(b'\), γ-rules on the whole of \(W_d\) (whose only other modifiable edge is the pendant, an option of the windows), rule F on the whole of \(X=Q_T\) (whose red heads \(c\), \(\mu\) admit no other rule: an X2 with \(d\)-label \(c\) or \(\mu\) would be \(T\) or \(W_d\) in the other orientation).
- New terminal edges: \(N_1\) ends in \(\{\mu,s(\mu)\}\) and \(\{c,e\}\); rule F creates \(\{b,e\}=\{e,s(e)\}\) and \(\{c,\mu\}=\{\mu,s(\mu)\}\). The only rule that could want \(\{e,s(e)\}\) is the X2 with \(d\)-label \(e\), whose γ-partner would be \(T\); then \(T\) is on a D-chain and is either cancelled (and uses no rule F), on a D-cycle (rotation, not rule F), or an existing node of a D-path whose predecessor is cancelled. A cancelled predecessor applies no rule, so it does not want \(\{e,s(e)\}\) either. The X2 with \(d\)-label \(\mu\) would be \(W_d\) itself, impossible.
- Absorption of a non-X2 \(W_d\) with a D-pendant (β for another X2) is the γ-absorbed window with A′=Dpend; Γ_D and F likewise.

**Lemma C8 (classification).** Every final piece is one of: (K1) a first-sweep piece unchanged except for removed trades (simple by Proposition C1, or Lemma 4 under (P5) on an odd cycle, with D-pendants by Lemma C6); (K2) a rebuilt X2 piece: \(S'\), \(N_1\), \(N_2\), the three rule-F pieces, or \(P_j\); (K3) an α-partner piece \(W'_d\); (K4) a β-partner piece (source, recipient, X2, or odd-cycle); (K5) a γ-partner piece (absorbed, or part of Γ_D / F); (K6) the target \(X=Q_T\) of a rule F. Every combination of modifications that a single piece can receive is one of the window options.

*Proof* (following the referee's independent derivation, 04-REVIEW-theorem-C §2). Fix a first-sweep piece \(W\) and list every rule that can modify it.

1. *\(W\) is the piece of an X2 source \(T\).* If \(T\) exists it applies exactly one rule (the rule-choice table: the partner case α/β/γ is determined by \(W_d\); in case γ, by the link type of \(W_d\) and by whether \(s(\mu)=c\)); its own piece becomes \(S'\), \(N_2\), the first rule-F piece or \(P_j\) (K2). If \(T\) is cancelled, it is the γ-partner of its predecessor on a D-path, which exists (the first node exists and existing and cancelled nodes alternate), and that predecessor absorbs it (K5); absorption is legitimate because \(T\)'s link has type 0 or 1 (Lemma C2). Other rules touching \(T\)'s piece: its \(c\)-end edge \(\{c,s(c)\}=\{c,e\}\) is the taken edge and is never given again; its pendant may be plain, type-1 changed or a D-pendant, and the last two exclude each other (Lemma C3(iv)); \(T\) is never an α-partner (it is defective); as a γ-partner it lies on a D-chain, so it is cancelled or on a D-cycle. All these combinations are pendant options of the windows \(S'\), Γ_D, F and D-rotation.
2. *\(W\) is the D-partner \(W_d\) of an existing X2 \(T\).* By Lemma C3(iii) it serves at most one X2 per red head. In case α its piece is \(W'_d\) (K3) and its far end is plain, received or D-linked; a received end and a D-linked end at the same red head \(x\) exclude each other, since both would be the defective trail \(\tau(x\,m(x))\), whose orientation (so whether \(x\) is its \(c\)- or its \(d\)-label) is unique. In case β the piece is a source, recipient, X2 or odd-cycle piece with the D-pendant (K4); a type-1 trade into it is impossible (C3(iv)). In case γ, \(W_d\) is a source with no incoming type-2 link (C3(v)); its piece is absorbed, \(N_1\), or the second rule-F piece (K5), and its pendant is plain, type-1 or a D-pendant, the last when \(W_d\) is also the β-partner of another X2. These are the far-end and A′ options of the windows α, β, γ-absorbed, Γ_D and F.
3. *\(W\) is the target \(X=Q_T\) of a rule F.* It is a recipient (of \(W_d\)), so it is neither a γ-partner (those are sources) nor an α-partner (it is defective). Its red heads are \(c\) and \(\mu\); an X2 with \(d\)-label \(c\) or \(\mu\) would be \(T\) or \(W_d\) in the other orientation, so no D-rule other than this rule F acts on it, and rule F uses it whole (K6).
4. *Every other piece* is a first-sweep piece, possibly with a removed trade (K1). Only type-0 and type-1 trades are removed (Lemma C5: X2 cancellation by Lemma C2, absorption only for links 0 and 1), so no recipient loses its source and the type-2 structure is unchanged. Such a piece is simple by Proposition C1, or, on an odd type-2 cycle, by Lemma 4 under (P5) with D-pendants (Lemma C6), the D-pendants having been applied first.

Finally, no new terminal edge (\(\{e,s(e)\}\), \(\{c,\mu\}\), \(\{c,e\}\), \(\{\mu,u\}\) from rule F; \(\{\mu,s(\mu)\}\), \(\{c,e\}\) from Γ_D) is wanted by another rule (Lemma C7). So each piece receives exactly one of the listed combinations, and each is a window option. The windows encode "plain" by inequalities saying that no named source has that \(c\)-label and no named X2 has that \(d\)-label. This is sound because every named source in each window trades, except the absorbed \(W_d\), whose \(c\)-label \(\mu\) the windows never add to the list; the single case where a non-trading named source matters (\(\mu=b\) with a type-1 pendant in \(S'\)) is the allowed exclusion. \(\square\)

*Proof of Theorem C.* Proposition C1, the rule choice, Lemmas C2–C8, the windows and the symbolic exchange checks. Every rule exchanges edges between the pieces it rebuilds (`symbolic_exchanges_c`, rule F by the window's edge-multiset assertion, D-rotation by telescoping), distinct X2 rules exchange distinct edges, and every piece is a simple five-edge path. \(\square\)

### 3.3 Checks

[check_regular_path_p5sweep.py](check_regular_path_p5sweep.py) (`python check_regular_path_p5sweep.py`, about 25 s): Lemma 4 under (P5) for Proposition C1 (moved from the scratch file `04-handoff/p5_scratch/l4p5.py` into the checker; the counts 259 closed and 720 open covers and 24 open exceptions with \(d_1\in\{A_0,A_2\}\) are asserted, 286 excluded), symbolic exchanges, telescoping, and windows \(S'\), α, β, γ-absorbed, Γ_D, rule F, D-rotation: **0 failures**. Two allowed exclusions, both justified in the code: (F1) in Γ_D (handled by rule F) and \(\mu=b\) in \(S'\) with a type-1 pendant (the type-1 source is the absorbed \(W_d\), whose trade is removed, so the pendant is plain).

[check_regular_path_p5_endtoend.py](check_regular_path_p5_endtoend.py) implements §3 exactly as written and verifies each output (edge partition, endpoint condition, simple paths). Evidence only:

- graphs (square, dense, K5-block, random; orders 12–40) with (P5) found by the CSP: 266 verified decompositions (98 α, 11 β, 3 absorptions, 2 D-paths);
- annealed generic \((M,r,s)\) data with (P1)–(P3)+(P5), seed 3: 59 verified, with 14 D-cycles (67 rotation uses), 82 D-paths, 132 absorptions, 38 β, 10 Γ_D, 2 rule F.
- larger runs (logs in `04-handoff/p5_scratch/`): generic seed 7, **400/400 verified** (121 D-cycles with 497 rotation uses, 502 D-paths, 797 absorptions, 229 β, 100 Γ_D, 17 rule F, 5 α); graphs seed 5, **539 verified** (180 α, 16 β, 5 absorptions, 1 Γ_D, 1 D-path), with one CSP timeout skipped. No failure in any run.
- Odd type-2 cycles did not occur in these runs (the code would use Lemma 4 block covers; rotations are not implemented there). They are covered by the referee's independent checker [check_regular_path_theoremC_independent.py](check_regular_path_theoremC_independent.py): the run `--seed 11 --planted 1200 --graphs 8` gave 1,288 verified decompositions with 0 failures, including 696 odd type-2 cycles (499 resolved by block covers, 197 by the rotation) and 998 D-pendants. A control run without (P5) fails at Proposition C1, as it should.
- **Rerun after the review fixes (2026-11-26).** `python -B check_regular_path_p5sweep.py`: Lemma 4 under (P5) 259/720/24 with 286 excluded, and all windows, 0 failures (log `04-handoff/p5_scratch/p5sweep_rerun_fixes.log`). `python -B check_regular_path_theoremC_independent.py --quick --seed 3`: ALL CHECKS PASSED (187 planted decompositions).

**Review notes.** (1) The encoding of "plain" was checked window by window by the referee (end of the proof of Lemma C8). (2) Endpoint uniqueness is the only fact used beyond the engine axioms; the partition it applies to is named in Lemma C4. (3) Catalogue completeness is now Lemma C8 with a proof; the referee derived the catalogue independently and found it complete.

## 4. Conjecture P5\*: some matching admits (P5)

**Refuted (2026-11-26).** See [04i](04i-regular-path-p5star-counterexample.md): a 30-vertex 5-regular graph with three bridges to 7-vertex caps in which every perfect matching fails (P5). P5\*\* fails with it. Possible rescues (bridgeless P5\*; a weak (P5) that ignores cherries at bridge-end apexes) are discussed there. The text below is the original session-4 record.

**Conjecture P5\*.** Every 5-regular graph with a perfect matching has a perfect matching \(M\) and \((r,s)\) satisfying (P1)–(P3) and (P5).

Evidence (exact CSP per instance):

- **Exhaustive:** all 3 graphs of order 8 and all 60 of order 10, every perfect matching tried: every graph has feasible matchings (at least 73% of its matchings).
- **Every matching minimising the number of (apex, M-pair) incidences** was feasible: all 63 graphs of orders 8, 10; 541 such matchings on 150 random order-12 graphs and 271 on 60 order-14 graphs. (Random graphs are triangle-sparse, so the order-12/14 data are weak.)
- \(K_6\) and \(C_k[K_2]\) (the only graphs where every vertex is an apex of two M-pairs: the M-edges are the fibres, and the super-graph must be 2-regular) are feasible by an explicit parity argument: all transition trails are the 4-cycles \(K_{2,2}\) between consecutive fibres, and orienting R from fibre \(i\) to fibre \(i+1\) is consistent.

- Dense families (`04-handoff/p5_scratch/p5mintri_dense.py`): 90 graphs (K5-block orders 10, 20; square-of-cycle and dense orders 12, 16), all perfect matchings enumerated, and up to 10 triangle-minimal matchings each: all **355** were feasible. In 82 of the graphs, even the minimum number of M-pair incidences was positive.

For the 8-vertex obstruction graph of §1 (`obstruction8_tri.py`), the 31 perfect matchings split by M-pair incidence count as follows. Count 8, the minimum: 7 matchings, all feasible. Count 9: 8, all feasible. Count 10: 12, of which 4 are infeasible. Count 12: 4, all infeasible. So the obstruction occurs only for non-minimal matchings.

**Sharper form (P5\*\*), suggested by the data:** *every perfect matching minimising the number of (apex, M-pair) incidences admits (P5).* No counterexample in any test (all 63 graphs of orders ≤ 10, 812 random and 355 dense instances). A proof would presumably use minimality through local matching switches: an obstruction to (P5) should yield an alternating cycle that lowers the incidence count. This has not been attempted.

Theorem C + Conjecture P5\* ⇒ every 5-regular graph with a perfect matching decomposes into five-edge paths.

## Files

- [check_regular_path_mdiamond.py](check_regular_path_mdiamond.py) — Theorem B′ checks.
- [check_regular_path_p5sweep.py](check_regular_path_p5sweep.py) — Theorem C windows and `find_rules`.
- `04-handoff/p5_scratch/` — (P5) feasibility CSP, brute force and census scripts.

## Changelog

- **2026-11-26 (review fixes, exposition only; no mathematical change).** Applied the referee fixes of [04-REVIEW-theorem-Bprime.md](04-REVIEW-theorem-Bprime.md) and [04-REVIEW-theorem-C.md](04-REVIEW-theorem-C.md).
  - B′ m1: added the two diamond appeals of 04d's G-rule "proved subcase" to the table (both through an \(M\)-edge, superseded by 04e W1/W3). m2: Lemma 8 Step 2 appeal marked redundant via Lemma 5(i). m3: "in particular" for the common-neighbour clause. m4: status updated (04e reviewed, fixes applied). m5: explained why the Lemma 4/4′ counts coincide. m6: B′ presented as a strengthening within the Theorem B entry; incomparability with Theorem A stated.
  - C M1: Lemma C8 now has a proof (per-piece roles, exclusivities, absorption of cancelled X2s, removed trades, terminal-edge interfaces, "plain" encoding). m1: the Lemma 4 run under (P5) moved from `04-handoff/p5_scratch/l4p5.py` into `check_regular_path_p5sweep.py` (`lemma4_p5`, counts asserted). m2: partition for the endpoint fact named. m3: Lemma C7 D-path case completed. m4: harmless incoming type-2 link to an X2 source stated. m5: referee runs covering odd type-2 cycles and rotations cited. m6: Theorem C labelled a conditional reduction; unconditional by-product (Corollary 4) stated.
  - Reruns: `check_regular_path_p5sweep.py` 0 failures (Lemma 4 under (P5): 259/720/24, 286 excluded); `check_regular_path_mdiamond.py` 0 failures; `check_regular_path_theoremC_independent.py --quick --seed 3` all checks passed.
- **2026-11-26 (status update, after the review fixes).** Conjecture P5\* (and P5\*\*) refuted by a 30-vertex graph with bridges ([04i](04i-regular-path-p5star-counterexample.md)). Status lines in the header, §3.1 (scope of Theorem C) and §4 updated accordingly. No change to the mathematics of §2–3.
