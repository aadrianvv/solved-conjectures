# Independent review of Theorem B (04e, diamond-free degree five)

**Referee:** independent agent, 2026-11-25. **Scope:** [04e](04e-regular-path-diamond-free.md) in full. The parts of [04d](04d-regular-path-matching-relative-theorem.md) it depends on are Lemma 1, the sweep, Lemma 3, Section 3, Lemma 4 and Proposition B with the G-rule. I also audited [check_regular_path_label_engine.py](check_regular_path_label_engine.py) and [check_regular_path_gsweep.py](check_regular_path_gsweep.py). Theorem A of 04d was reviewed separately ([04-REVIEW-theorem-A.md](04-REVIEW-theorem-A.md)), and I did not redo that review.

## Verdict: ACCEPT WITH FIXES

I found no fatal error and no mathematical gap that I could not close. Every exchange rule is a correct edge exchange. Here are the main findings.

- I re-derived the case split α/β/γ, Lemma 5, Lemma 7, the Gtarget resolution and the rotation by hand.
- I derived the catalogue of final pieces independently from the written rules. It agrees with W1–W8 plus L4′.
- The label engine enforces only valid axioms, and every window inequality is justified by the text.
- I reran the windows: 0 failures.
- My own enumeration of Lemma 4′ reproduces the author's counts exactly.
- I wrote an independent end-to-end implementation from the text. It ran on graph constructions and on adversarial planted generic data, and every output verified. The data exercised every rule, including 442 odd Gtarget cycles that the rotation resolved. These cycles come from generic data that satisfies (P1)–(P3); the author had observed no odd Gtarget cycle.

The fixes are expository. The written §4 does not by itself prove the completeness of the catalogue (M1). Several small facts the proof needs are missing or misargued (m1–m8).

## 1. Line-by-line check

**Proposition B (04d §4).**

- I rechecked the Lemma 3 exceptions. \(A=d\) gives the triangles \(bcd,bde\), which share \(bd\). \(s(c)=e\) or \(r(e)=c\) give \(cde,cbe\), which share \(ce\). Both are diamonds.
- At a type-0 target, the only remaining exception is \(b=m(f)\), the G-configuration. Two exceptional ends would give the triangles \(bcf,fbh\), which share \(fb\), another diamond.
- A failing pair replacement is the chord \(b_id_i\), a diamond.
- The Lemma 4 diamond-free counts reproduce (259 closed and 564 open covers, 24 exceptions). The rotation completion is unchanged.
- Correct.

**Lemma 5.**

- (i): a moved \(S\)-edge \(\{x,s(x)\}\) equal to \(\{f,g\}\) needs \(x=f\), which makes the source \(Q_c\), not defective. Otherwise it needs \(s(g)=f\), which violates (P2). Odd-cycle replacements can move a β-pendant edge, but the G-pendant moves \(\{g,f\}\) out first. Correct.
- (ii): labels verified.
  - β: \(c'=p\), \(d'=q\), \(e'=u\), \(s(u)=f\).
  - γ: \(d'=p\), \(c'=q\), \(b'=g=r(q)\).
  - "No type-1 trade into a β W0" and "no incoming type-2 link into a γ W0" both reduce to the source with \(c\)-label \(f\), which is \(Q_c\). Correct.
- (iii): correct.

**Rules.** I verified each exchange by multiset of edges.

- G-rule: \(fb\leftrightarrow fg\).
- G-pendant: \(\{g,f\}\leftrightarrow\{f,b\}\).
- Absorption: the closing edge \(fg\) is replaced by \(fb\).
- Γ and Γ′: the ten edges of \(Q'_c\cup W\) match exactly. For Γ′ the edge \(\{h,g\}=\{A',g\}\) becomes interior, which is legitimate only when \(A'\) is the plain pendant; see the W6/W7 results.
- Rotation: \(\bigcup_k(Q'_k\cup W_k)\) and \(\bigcup_k(R_k\cup P_k)\) differ only by \(\{c_{k+1}c_k\}_k\) versus \(\{c_{k+1}c_{k+2}\}_k\). These are equal multisets around the cycle (telescoping). The partition is correct, but it holds only cycle-wide, not per window (m2).

**Interactions.** These are the cases I checked by hand. Each is impossible, a diamond, or listed in §4.

- At most one config per \(T\), per \(f\) and per \(Q\); two configs on one \(Q\) give a diamond.
- Per \(W_0\), the only possible pairs are (α,α) with two partner ends, and (β for \(c\), γ for \(c_2\)) with \(f_2=u\) and \(g_2=f\).
- \(T_c\) as a β-partner gives the triangles \(fhb,bcf\), a diamond.
- \(T_c\) as a γ-partner is exactly a Gtarget edge.
- \(Q_c\) is only ever an α-partner, and only at its \(h\)-end.
- A received end and an α-partner end cannot coincide.
- A Γ source piece has no second partner end.
- A cancelled \(Q_{c^*}\) is a canonical trail, and its use as an α-partner is in W3.
- Removing a trade through absorption or cancellation leaves a standard first-sweep piece. Lemma 3 is per end, and no recipient loses its source, because type-2 links are never absorbed.

**Gtarget graph.** In-degree and out-degree are both at most 1. The alternation is right on paths and even cycles. On an odd cycle with Γ at \(j\), the nodes \(j+1,j+3,\dots,j-2\) absorb and \(j+2,\dots,j-1\) are cancelled. So \(T_{c_j}\) trades (\(c_j\) exists) and \(T_{c_{j+1}}\) trades (\(c_{j+1}\) exists). This is consistent. Absorbed W0s with type-1 links change other pendants. The odd-cycle choice involves only type-0 links, so it never feeds back into the pendants. My implementation checks this explicitly.

**Odd type-2 cycle with a G-pendant.** Lemma 7 is true. One step is misargued and one needed fact is missing (m1).

## 2. Catalogue completeness (the author's highest-risk point)

I derived the set of final pieces from the rules independently. A final piece is one of the following.

1. An unaffected first-sweep piece, possibly with a trade removed.
2. \(Q_c\) of an existing configuration:
   - \(Q^*\) in case α or β (W1);
   - absorbed γ (W2);
   - Γ or Γ′ (W6, W7);
   - rotation (W8).
   Its \(h\)-end may be plain, received or α-linked.
3. A non-defective α-partner (W3), whose other end may be plain, received or α-linked. A received end with \(Z=p\) is itself a G-configuration and falls under W1.
4. A β-W0: source or recipient (W4); odd cycle (L4′); also γ for \(c_2\) (W5, W6, W7 with \(A=m(g)\)).
5. A γ-W0: absorbed (W5), with \(A^*\in\{s(g),r(g),m(g)\}\), or a Γ/rotation piece.

This matches W1–W8 and L4′ exactly. I found no missing shape.

**Engine audit.** The engine enforces fixed-point-freeness, injectivity of \(r,s\), \(m\) as an involution, pairwise distinct edges of distinct classes (this gives (P2)), (P3) in all three insertion orders, and diamond-freeness. The diamond test is incremental and complete: a new edge \(XY\) changes the common-neighbour counts only on \(XY\), \(XZ\) and \(YZ\). The restricted-growth enumeration generates every partition, so the engine is sound as a superset.

**Window audit.** Every scenario inequality is a true consequence.

- Non-defectiveness of \(Q_c\), \(W_0\) and \(Q_{c^*}\).
- \(q\ne e\) for type 2.
- \(h\ne q\) and \(c_3\ne q\) for absorbed γ.
- \(c_3\ne q\) at Gtarget nodes, because \(c^*\) is γ.
- \(Z\ne p\) in W3.
- \(a_1\ne h_0\) in W8.

None is stronger than proved. Rerun of `check_regular_path_gsweep.py` (12 min 56 s): 0 failures in every window.

- Gtarget with a changed pendant: 0 identifications.
- L4′: 205 closed and 548 open covers, plus 12 open \(d_1\in\{A_0,A_2\}\) exceptions.

## 3. Independent checker

The checker is [check_regular_path_theoremB_independent.py](check_regular_path_theoremB_independent.py). It is written from the text. It does not import any 04e code; it reuses only the audited Lemma 1, (P1)–(P3) and path-cover code of the Theorem A referee. It also asserts the text's intermediate claims, for example Lemma 5, Lemma 7, plain pendants at odd Gtarget nodes, and the absence of pendant feedback.

- **Lemma 4′ (own enumeration).** It matches exactly: G-pendant triples gave 205 closed and 548 open covers and 12 exceptions; no-G triples gave 259 closed and 564 open covers and 24 exceptions. No other uncovered case occurred.
- **Planted generic data.** Generic \((M,r,s)\) data satisfying (P1)–(P3) and diamond-freeness, with planted structures:
  - α configurations, including α-links and two partner ends;
  - β configurations, including on odd type-2 cycles of lengths 3, 5 and 7;
  - γ configurations with type-0, type-1 and type-2 links;
  - β and γ at one W0;
  - Gtarget paths and cycles of lengths 2–7, with and without (F1);
  - random extra coincidences of \(r\), \(s\) and \(m\).

  The random choice of the Γ node \(j\) and of the even-cycle offset tests each admissible choice.
- **Graphs.** Random diamond-free 5-regular graphs, near the maximum triangle density of \(2n/3\), with triangle-preferring matchings, and \(L(\text{cubic})+\)matching. 15 Lemma 1 constructions per graph.
- **Results.** There were two runs, seeds 31 and 77, about 25 min in total. Every output was an exact partition into simple five-edge paths, with 0 failures. Evidence only.
  - Planted generic data: 5,916 verified decompositions.
    - G-configurations: 5,404 α, 5,133 β and 16,813 γ.
    - 10,140 G-pendants.
    - 995 odd type-2 cycles with a G-pendant, all covered by Lemma 4′ blocks.
    - 1,009 type-2 Γ uses.
    - 1,910 type-0 and 1,032 type-1 absorptions.
    - 5,330 cancellations.
    - 886 α-partners with two partner ends.
    - 459 α-linked and 598 received \(h\)-ends.
    - 1,935 Gtarget cycles with lengths 2–7 and 1,060 Gtarget paths with lengths 1–7. The odd cycles were resolved by Γ at one node (575 times) or by the rotation (442 times).
    - Γ′ used 119 times.
  - Graphs: 5,760 verified decompositions from 384 diamond-free graphs on 12–48 vertices, with 4,848 triangles in total. These real constructions contained 536 α, 37 β and 28 γ configurations and a few Gtarget edges and type-2 Γ uses, but no odd Gtarget cycle.
- **Cross-check.** I also ran the author's end-to-end code on my planted instances (scratch file `04-handoff/review-theoremB/cross_author_code_scratch.py`). On 502 instances it verified all 502, including 32 rotations and 53 odd-node Γ uses. On my graph seeds the author's own default run also verified 479 of 479. I found no discrepancy between the text and the author's code. The author's code takes the first valid Γ node and a fixed offset for even cycles. Mine chooses at random, and both are allowed by the text.

## 4. Issues

**M1 (major, expository).** §4's "Completeness of the catalogue" is a list. It is not an argument, and the proof of Theorem B rests on it. Add the classification of §2 above as a lemma with proofs:

- per-W0 combinations: only (α,α) and (β,γ);
- per-\(Q\) and per-\(T\) uniqueness;
- the received/α-link exclusivity at every end, not only at the \(h\)-end;
- the diamond for "\(T_c\) is a β-partner";
- the fact that removing trades never strands a recipient.

Mathematically I found the list complete. The written proof should still not leave this to the reader.

**m1 (minor).** Lemma 7 (§3) has two problems.

- The step "If it were a \(b\)-label, then \(b_i\) would equal some \(d\)-label" is a non sequitur, since \(m(b_j)\) is not a \(d\)-label. Correct argument: \(m(b_i)=b_j\) gives \(r(c)=r(c_j)\) for the apex \(c=r(b_i)\). So \(T_c=T_j\) lies on the odd cycle, while \(T_c\) is a source.
- The conclusion "a fresh vertex or another trail's fresh unchanged pendant" also needs the fact that a G-pendant never equals a *changed* pendant \(r(b_k)\). Proof: equality forces the apex \(c=b_k\). Then \(T_c\) is the external type-1 source into \(T_k\), whose target is defective, not \(Q_c\).

The L4′ code assumes both facts.

**m2 (minor).** In the proof of Theorem B, "Γ′ and the rotation are checked by edge count in the windows" is inaccurate for the rotation. `window_rotation` calls `run` without `before`, so it compares no edges. The rotation re-partition holds only around the whole cycle. Write the telescoping argument of §1 into the text.

**m3 (minor).** §3, Γ-rule. State explicitly that Γ′ is used only with the plain pendant. The windows prove that \(A'=h\) is impossible for a changed pendant or a G-pendant, so the interior edge \(\{h,g\}\) is never a moved pendant edge. The "Interfaces" bullet claims every \(\{g,A'\}\) edge is terminal, which is false in Γ′.

**m4 (minor).** §4, W3. The exclusion \(Z\ne p\) (`sc.ne(Z, p)`) is justified only in a code comment. Add to the text that \(Z=r(u)=p\) means \(W_0=Q_u\) is a G-configuration, handled by W1.

**m5 (minor).** The partner-end argument "\(\{q,s(q)\}\) would need \(r(g)=p\)" is correct, but it omits the \(s(s(q))=q\) orientation, which (P2) excludes. One clause fixes it.

**m6 (minor, scope wording).** "Strictly contains" FGK: FGK's \(C_4\) theorem, and their wider class, assert extendability of every 1-factor. Theorem B contains only the existence part. Say so, as 04d already does.

**m7 (minor, stale).** 04e "Scope", last bullet, says the FGK full text has not been read (M1). 04d and [04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md) record that it has been read. Update the bullet.

**m8 (minor, code hygiene).** In `check_regular_path_diamond_free.py`, `solve_one` contains unreachable search code after `if True: raise`. Its docstring speaks of trying choices, but the code applies only the deterministic rule. It is harmless, but it should be removed or the docstring corrected.

## 5. Novelty (bounded search, 2026-11-25)

I searched for path or \(P_5\) decompositions of diamond-free (\(K_4^-\)-free) 5-regular graphs. I also searched for later work on FGK and Chu–Fan–Hong–Zhou.

- Chu, Fan, Hong and Zhou, *Path decompositions of 5-regular graphs*, Sci. Sin. Math. 54(11) (2024) 1787–1794, [doi:10.1360/SSM-2023-0316](https://www.sciengine.com/SSM/doi/10.1360/SSM-2023-0316). Hypothesis: no 3-cycle and 4-cycle share an edge, plus a perfect matching. This is weaker than diamond-free, and the containment argument is correct.
- Botler, Mota and Wakabayashi, [Discrete Math. 338 (2015)](https://www.sciencedirect.com/science/article/pii/S0012365X1500151X): the triangle-free case.
- Botler, Mota, Oshiro and Wakabayashi: girth results.
- [arXiv:2012.05145](https://arxiv.org/abs/2012.05145): spanning Cayley subgraphs.
- Montgomery et al., approximate decompositions, [arXiv:2406.02514](https://arxiv.org/pdf/2406.02514).
- Chu and Wang, [arXiv:2510.12806](https://arxiv.org/abs/2510.12806): Eulerian graphs, not relevant.

None states the diamond-free case. I found no 2025–2026 paper on FGK for degree five. Citation lists could not be retrieved, because the SSM PDF returned HTTP 429. This is a bounded search, not a certificate.

## 6. Remaining risk

- The proof is computer-assisted. Its soundness rests on the label engine and the window facts, both audited here, and on the written case analysis.
- The planted runs show that the rotation and the Γ choice at odd Gtarget nodes occur in generic \((M,r,s)\) data. I did not determine whether they occur with Lemma 1 constructions. This does not matter, because the proof uses only (P1)–(P3).
- No Lean formalization exists.
