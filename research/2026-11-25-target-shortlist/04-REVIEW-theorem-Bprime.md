# Independent review of Theorem B′ (04g §2, no diamond through the matching)

**Referee:** independent agent, 2026-11-26. **Scope:** [04g](04g-regular-path-p5-and-m-diamond.md) §2, with every part of [04d](04d-regular-path-matching-relative-theorem.md) and [04e](04e-regular-path-diamond-free.md) on which it relies, and the checker [check_regular_path_mdiamond.py](check_regular_path_mdiamond.py). Theorem B itself was reviewed separately ([04-REVIEW-theorem-B.md](04-REVIEW-theorem-B.md)); I did not redo that review, except where a step touches the hypothesis.

## Verdict: ACCEPT WITH FIXES

I found no fatal or major error. Every appeal to diamond-freeness in 04d and 04e exhibits a diamond that contains an edge of \(M\), so the weaker hypothesis suffices. The engine patch encodes the hypothesis exactly, and my own filter, written with a different algorithm, reproduces every window count. My end-to-end checker ran on graphs and generic data containing many diamonds that avoid \(M\). Every output verified, and a control run with the hypothesis switched off fails as it should. The fixes are expository (m1–m6).

**Statement checked.** Let \(G\) be a finite simple 5-regular graph and \(M\) a perfect matching such that no diamond contains an edge of \(M\), as a side or as the chord. Then \(E(G)\) partitions into paths with five edges. The stated equivalent form is correct: an \(M\)-chord means two triangles share the \(M\)-edge, and an \(M\)-side means a triangle through the \(M\)-edge shares another edge with a second triangle. The clause "ends of an \(M\)-edge have at most one common neighbour" is implied by the first clause (m3).

## 1. Every diamond appeal in 04d and 04e (Task 1)

I searched both texts for "diamond", "triangle", "chord", \(K_4\), and for every inequality justified by a coincidence of three vertices, and I reread the window facts of 04e §4 and the scenario inequalities in `check_regular_path_gsweep.py`. Below, \(\in M\) is read off the defining facts.

| place | diamond | \(M\)-edge | status |
|---|---|---|---|
| 04d Lemma 3 / Prop. B, \(A=r(b)=d\) | \(bcd\), \(bde\) share \(bd\) | side \(cd\) | ok |
| 04d Prop. B, \(s(c)=e\) or \(r(e)=c\) | \(cde\), \(cbe\) share \(ce\) | side \(cd\) | ok |
| 04d Prop. B, both ends of a type-0 target exceptional | \(bcf\), \(bfh\) share \(fb\) | chord \(fb=m(f)\) | ok |
| 04d pair replacement, \(A_i=r(b_i)=d_i\) | \(b_ic_id_i\), \(b_id_ie_i\) share \(b_id_i\) | side \(c_id_i\) | ok |
| 04d Lemma 4, "no local diamond" | computer step | local \(c_id_i\) | rerun, §2 |
| 04d G-rule "proved subcase": \(s(f)\ne h\) | \(fbh\), \(bcf\) share \(fb\) | chord \(fb\) | ok; **not in the 04g table** (m1) |
| 04d G-rule "proved subcase": \(b\ne u\) | chord \(ce\) | side \(cd\) | ok; **not in the 04g table** (m1) |
| 04e Lemma 8 Step 1 | \(bcf\), \(bhf\) share \(fb\) | chord \(fb\) | ok |
| 04e Lemma 8 Step 2, \(f'=q\) | \(gqp\), \(gpf\) share \(gp\) | side \(qp=m(p)\) | ok, and redundant (m2) |
| 04e Lemma 8 Step 4 (and the §3 remark "pendant at a Gtarget node is plain") | \(fhb\), \(bcf\) share \(fb\) | chord \(fb\) | ok |
| 04e Lemma 4′ | computer step | \(c_id_i\), \(b_im(b_i)\) | rerun, §2 |
| 04e W1–W8 engine axiom | computer step | known \(M\)-edges | rerun, §2 |
| 04e Γ′ remark "no alternative for changed/G-pendant in W6/W7" | depends on the windows | — | holds under B′, §2 |

**No hidden appeal.** I found none.

- **Window facts.** None of the window facts or scenario inequalities of `check_regular_path_gsweep.py` is derived from a diamond. These are non-defectiveness, case α/β/γ, \(Z\ne p\), \(q\ne e\), \(h\ne q\), \(c_3\ne q\) and \(a_1\ne h_0\).
- **Lemma-level facts.** Lemma 5, Lemma 7 (a) and (b), the Gtarget degree bounds, the alternation, the rotation telescoping, and (o1)–(o5) use only (P1)–(P3), injectivity and uniqueness of canonical trails.
- **The 04d G-rule proved subcase.** Its two diamond appeals are absent from the 04g table. 04e does not use the subcase, because windows W1 and W3 replace it, and both diamonds contain an \(M\)-edge anyway.
- **Lemma 8 Step 2.** Its diamond appeal is a second proof. Lemma 5(i) already shows that \(\{q,s(q)\}\) is not a partner edge without any diamond.

No appeal produces a diamond free of \(M\).

## 2. The computer steps (Task 2)

**Engine patch `MState`.**

- **Soundness.** `add` rejects only when the new edge \(XY\) lies in a diamond of known edges, one of whose five edges is a known \(M\)-edge. Edge labels are fixed when an edge is created, because the base engine refuses relabelling. So such a diamond is a real diamond of \(G\) through an \(M\)-edge, and the patch is no stronger than the hypothesis.
- **Completeness.** The incremental test is also complete. Every diamond is created when its last edge appears, and that edge is either the chord (first loop: two common neighbours) or a side \(PQ\) with \(P\) a chord end (second loop over \(Z\in N(X)\cap N(Y)\) and \(W\in N(P)\cap N(Z)\setminus\{Q\}\)).
- **Hooking.** It is correct. `G.enumerate_partitions` is rebound in the gsweep namespace, and the generator body runs while `engine._State` is patched.
- **Lemma 4/4′ re-runs.** `local_m_diamond` uses only the \(M\)-edges \(c_id_i\), plus \(b_iA_i\) for G-pendants. These are true \(M\)-edges, and the local edges are true edges.

**Independent confirmation of the patch** (`check_regular_path_theoremBprime_independent.py`, parts `exact` and `windows`).

- **Own filter.** I switched off the engine's diamond axiom and added my own filter, a different algorithm. After each new edge \(XY\), it rejects iff some 4-set \(\{X,Y,Z,W\}\) with \(Z,W\in N(X)\cup N(Y)\) spans at least 5 known edges, one of which is a known \(M\)-edge.
- **Exactness.** On all 17 W1–W5 windows, the identification sets of the own filter and of the unpatched engine with a brute-force post-filter are **identical** (e.g. Q\* α received: 8,428 = 8,428, against 7,747 under full diamond-freeness). A 7-case self-test also passes, including a K4 without \(M\) (kept) and an \(M\)-side added last (rejected).
- **Window rerun.** I reran all of W1–W8 with the own filter (log `04-handoff/review-theoremBprime/own_windows.log`): **0 failures**. The identification count of every window **equals** that of the author's patched run, for example 809,516 for Γ type-2 received/type1 and 173,831 for the Gtarget linked/plain window. So the two filters agree exactly.
- **W7 exclusions.** The excluded counts are 532, 17,021 and 18,779, as stated. The changed-pendant and G-pendant Gtarget windows still have 0 identifications.
- **Γ′ interface.** The type-1 and G-pendant Γ windows use no alternative and no exclusion, so the Γ′ interface argument of 04e still holds.
- **Author's checker.** I reran `python -B check_regular_path_mdiamond.py` (log `04-handoff/review-theoremBprime/mdiamond_rerun.log`). The self-test passed, the total was 0 failures, and Lemma 4 gave 259/564/24 with 442 excluded and Lemma 4′ gave 205/548/12 with 243 excluded, all as stated.

**Lemma 4 and 4′, own enumeration.** I used the label scheme of the B referee, rewritten, with the M-diamond filter.

- The counts are 259/564/24 with 442 excluded without G-pendants, and 205/548/12 with 243 excluded with G-pendants. There is no other uncovered case.
- **Every local diamond in these schemes contains a known \(M\)-edge:** 0 cases have a local diamond that avoids \(M\).
- So Lemma 4 and Lemma 4′ under B′ are literally the same finite statements as under diamond-freeness. This explains the identical counts.

## 3. End-to-end evidence (Task 3)

`check_regular_path_theoremBprime_independent.py` imports nothing from 04g. It reuses three pieces of earlier referee code: the Theorem A referee's Lemma 1, (P1)–(P3) check, path cover and first sweep; the Theorem B referee's `procedure` (04d plus the 04e second sweep, which asserts Lemma 5, Lemma 7, the Gtarget claims and the absence of pendant feedback) and planter. Generators, hypothesis tests and the final verifier are its own. For each instance it checks two things.

- **Proposition B′.** After the first sweep, run with the A referee's own sweep, every non-simple piece is a G-configuration \((b,c,f,b,h,Y)\) with \(fb\in M\), and no realized Lemma 4 block fails outside the exception.
- **Decomposition.** The full procedure's output is an exact partition into simple five-edge paths.

**Inputs.**

- **Graphs.** These are 5-regular graphs with a fixed \(M\), annealed by switching non-\(M\) edges toward many diamonds avoiding \(M\) and many \(M\)-triangles, subject to no \(M\)-diamond. The starting points are \(C_n(a,b)\) or \(C_n(1,2)\) plus \(M\), and disjoint \(K_5\)'s plus \(M\).
- **Planted data.** These are generic \((M,r,s)\) data with (P1)–(P3) and the hypothesis, built from the B referee's planted G-configurations of every case plus 1–6 planted diamonds, or \(K_4\)'s, on \(R\cup S\) edges at existing configuration vertices. They are annealed with a reward for diamonds that avoid \(M\).

**Results.** Evidence only.

| run | verified | failures | non-\(M\) diamonds | of them touching an \(M\)-triangle | diamonds through \(M\) |
|---|---|---|---|---|---|
| `--quick --seed 5` | 103 planted + 75 graph | 0 | 878 | 429 | 0 |
| `--seed 77 --graphs 6 --planted 600` | 421 planted + 280 graph | 0 | 2,664 | 1,441 | 0 |

The seed-77 run exercised every rule:

- 1,874 first-sweep G-configurations;
- 286 α, 358 β and 869 γ surviving configurations, with 716 G-pendants;
- 82 type-2 Γ uses, 8 Γ′ uses and 382 cancellations;
- 77 odd Gtarget cycles, 29 of them resolved by the rotation;
- 75 odd type-2 cycles with G-pendants.

Logs: `04-handoff/review-theoremBprime/quick_seed5.log`, `strong_seed77.log`.

**Control (sensitivity).** With the hypothesis off, the same generators produced \(M\)-diamonds and **57 failures** against 57 verified runs. These are first-sweep defects such as \(A=d\) and \(s(c)=e\), and non-simple final pieces. So the end-to-end check is not vacuous, and the hypothesis is used.

## 4. Containment and novelty (Task 4)

- **B ⊂ B′.** A diamond-free graph has no \(M\)-diamond for any \(M\). Correct.
- **Corollary 4 ⊂ B′.** If no \(M\)-edge lies in a triangle, no \(M\)-edge lies in a diamond, because every edge of a diamond lies in one of its triangles. Correct.
- **Chu–Fan–Hong–Zhou 2024 ⊂ B ⊂ B′.** This holds given a perfect matching.
- **FGK 2010 Theorems 6–7.** The two results are incomparable, by the same comparison as [04-NOVELTY-fgk2010.md](04-NOVELTY-fgk2010.md).
  - B′ contains the 408-vertex example (no \(M\)-triangle, so Corollary 4), which FGK do not cover.
  - Conversely, two \(M\)-triangles sharing their \(M\)-edge (an \(M\)-chord diamond) form no FGK bad pair, since their union minus \(M\) is a 4-cycle. FGK Theorem 6 can allow such an \(M\), but B′ cannot.
  - FGK's conclusion, that \(M\) is the middle-edge set, is stronger where it applies.
- **Novelty.** B′ is new as a statement exactly to the extent that Theorem B is, given B's bounded search (04-REVIEW-theorem-B §5). I did no further literature search, since B′ is a matching-relative strengthening of B by the same method.
- **Significance.** The extension over B and Corollary 4 is modest. It enlarges the class, but it still excludes every graph in which each perfect matching meets a diamond, such as \(K_6\) and \(C_k[K_2]\). I checked that every edge of \(C_k[K_2]\) lies in a diamond. Under the repository's significance policy it should be published, if at all, as a strengthening within the Theorem B entry, not as a separate count.

## 5. Issues

None fatal, none major.

- **m1 (minor, completeness of the table).** The 04g table omits the two diamond appeals in 04d's G-rule "proved subcase", \(s(f)\ne h\) and \(b\ne u\). Both contain \(M\)-edges, and 04e supersedes the subcase by W1/W3, but the claim "every occurrence" should list them or say that they are superseded.
- **m2 (minor).** In the row for 04e Lemma 8 Step 2, note that the appeal is redundant, because Lemma 5(i) already gives the conclusion.
- **m3 (minor, statement).** In "Equivalently: … and the ends of an \(M\)-edge have at most one common neighbour", the second clause is implied by the first. Write "in particular".
- **m4 (minor, stale status).** The status line says that B′ "depends on 04e being correct (under review)". 04e has been reviewed: accept with fixes, fixes applied.
- **m5 (minor, presentation).** §2 should say explicitly that the Lemma 4 and 4′ schemes contain no local diamond avoiding \(M\). This is why the counts coincide, which a reader may otherwise find suspicious.
- **m6 (minor, scope wording).** Publish B′ as a strengthening of the Theorem B entry, with B′'s own audit, and do not increment the count. Keep "Theorem B′ contains Corollary 4" next to the 04d statement of Theorem A, which B′ does not contain.

## 6. Reproduction

```powershell
Set-Location research/2026-11-25-target-shortlist
python -B check_regular_path_mdiamond.py                                          # author, ~25 min
python -B check_regular_path_theoremBprime_independent.py --quick --parts lemma4 exact graphs control   # ~2 min
python -B check_regular_path_theoremBprime_independent.py --parts windows        # own-filter W1-W8, long
python -B check_regular_path_theoremBprime_independent.py --seed 77 --graphs 6 --planted 600 --parts graphs
```
