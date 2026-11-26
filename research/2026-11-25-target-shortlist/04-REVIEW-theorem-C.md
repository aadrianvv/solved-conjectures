# Independent review of Theorem C (04g §3, the (P5) route)

**Referee:** independent agent, 2026-11-26. **Scope:** [04g](04g-regular-path-p5-and-m-diamond.md) §3 (Proposition C1, the D-rule family, Lemmas C2–C8 and the proof of Theorem C) as of 2026-11-25 23:27, together with [check_regular_path_p5sweep.py](check_regular_path_p5sweep.py) and the scratch Lemma 4 run `04-handoff/p5_scratch/l4p5.py`. I did not read `check_regular_path_p5_endtoend.py`, so that my implementation would stay independent. §4 (Conjecture P5\*) is out of scope.

## Verdict: ACCEPT WITH FIXES

**Statement.** Let \(G\) be finite, simple and 5-regular, with a perfect matching \(M\). Let \(r,s\) satisfy (P1)–(P3) and (P5), \(m(r^{-1}(x))\ne r(x)\) for all \(x\). Then \(E(G)\) partitions into five-edge paths.

- I found no fatal error and no mathematical gap that I could not close.
- Proposition C1, Lemma C2, the D-rotation endpoint fact and Lemma C6 are correct as written.
- I derived the catalogue of final pieces independently. It agrees with the windows.
- The windows rerun with 0 failures.
- My independent implementation of §3 verified 1,288 decompositions in the strong run with 0 failures, including 696 odd type-2 cycles (197 resolved by the rotation) and 708 D-pendants on them. A control run with (P5) dropped fails as expected.
- The main fix is expository: Lemma C8 is asserted, not proved (M1). The other fixes are minor.

**Scope.** Theorem C is a statement about the data \((M,r,s)\). Its value as a step toward the degree-five case rests on Conjecture P5\*, which §1 already shows is false for a *fixed* \(M\). On its own it gives decompositions for every graph that admits such data, for example every graph with a perfect matching none of whose edges lies in a triangle, since then (P5) holds for every \((r,s)\). It is not a resolution of the degree-five case, and it must not be counted as one.

## 1. Risk points named by the author

**Proposition C1 (first sweep under (P5) leaves only X2).** Correct. Each Lemma 3 exception other than \(s(c)=e\) is an \(R\)-path \(u\to x\to y\) with \(uy\in M\):

- \(A=r(b)=d\) gives \(c\to b\to d\);
- \(r(e)=c\) gives \(d\to e\to c\);
- a G-configuration gives \(f\to c\to b\);
- a failing pair gives \(c_i\to b_i\to d_i\).

The "chord \(ce\) ⇒ \(s(c)=e\)" remark is also correct.

- **End to end.** In every run I checked C1 with the Theorem A referee's own first sweep: every non-simple first-sweep piece was an X2 source \((A,b,e,d,c,e)\), and no realized Lemma 4 block failed outside the exception. My own implementation checks C1 again before the second sweep.
- **Lemma 4 under (P5), own enumeration.** I used the 04d label scheme with pendant kinds unchanged and changed, and excluded only a changed \(A_i=d_i\). The result is 259 closed and 720 open covers, plus 24 open exceptions with \(d_1\in\{A_0,A_2\}\), as stated.
- **Excluded count.** I count 322 exclusions against the author's 286. The difference is only bookkeeping: I exclude before discarding the configurations that repeat an edge.

**X2 sources have no type-2 links (Lemma C2).** Correct.

- **Outgoing.** \(e_Q=c\) forces \(b_Q=s(c)=e=r(d)\), so \(c_Q=d\) and \(Q=T\).
- **Incoming.** An X2 source may have an *incoming* type-2 link from a non-trading recipient, when it sits at an even position at least 2 on a type-2 path. That is harmless, and removing the X2's own trade still never affects the alternation.

**D-rotation endpoint fact \(A_j\ne d_{j+1}\).** Correct.

- **Parity count.** In any partition of \(E(G)\) into \(n/2\) five-edge trails, each vertex has an odd number of trail ends, and there are \(n\) ends in total, so each vertex is an end exactly once.
- **Which partition.** The fact must be applied to a partition that contains both \(S_j\), with its final pendant, and \(S_{j+2}\):
  - for a plain or type-1 pendant, the first-sweep partition;
  - for a D-pendant, the first-sweep partition after that single D-pendant exchange. That exchange does not touch \(S_{j+2}\), because \(S_{j+2}\)'s only D-partner is \(S_{j+3}\).

  The text should say this (m2).
- **The rotation itself.** The telescoping is right: \(S_j\) loses \(d_{j-1}d_j\) and gains \(d_jd_{j+1}\). The trade edge \(\{c_j,s(c_j)\}=\{c_j,d_{j-1}\}\) stays, so every target keeps its received edge.

**Odd type-2 cycles under (P5).** These are now covered end to end.

- **Lemma C6.** The D-pendant facts are correct: a D-pendant is not a local \(b\)-, \(c\)-, \(d\)- or \(e\)-label, not \(d_i\) (by (P5)), and differs from changed pendants. If it equals an unchanged pendant, then \(b_k=c\), so \(T_k=Q_T\) receives \(T\)'s type-1 trade.
- **Data.** My planted data contain odd type-2 cycles of lengths 3, 5 and 7, with D-pendants (X2 with \(d\)-label \(b_i\)) and type-1 pendants. They also include cycles forced into the uniform rotation (\(A_i=d_{i+1}\) for all \(i\)).
- **Checks.** Lemma C6 is asserted in every case: the D-pendant is not a local label, and (o5) holds. Every realized block that failed was an exception case. When no block had a cover, a uniform rotation existed.

## 2. Catalogue (Lemma C8): independent derivation

Lemma C8 ends with "Each kind is covered by the table above. \(\square\)", which is not a proof (M1). I derived the following from the rules, and it agrees with the windows.

1. **Pieces rebuilt by an existing X2 \(T\).**
   - **The piece of \(T\) itself:** \(S'\) (in case α, β or γ-absorbed), \(N_2\), the first piece of rule F, or \(P_j\).
   - **Who else can change it.** Its \(c\)-end edge \(\{c,s(c)\}=\{c,e\}\) is the taken edge and is fixed. Its pendant may be plain, type-1 changed, or a D-pendant; the last two exclude each other, since both are orientations of \(\tau(b\,m(b))\). \(T\) is never an α-partner, because it is defective. As a γ-partner it lies on a D-chain, so it is cancelled (and absorbed) or on a D-cycle.
2. **The D-partner \(W_d\).**
   - **α.** The piece is \(W'_d\), with far end plain, received or D-linked. A received end and a D-linked end at the same \(x\) exclude each other, since both are \(\tau(x\,m(x))\).
   - **β.** The piece is a source, recipient, X2 or odd-cycle piece with the D-pendant.
   - **γ.** \(W_d\) is a source with no incoming link (C3(v)). The piece is absorbed, \(N_1\), or the second piece of rule F; its pendant is plain, type-1 or a D-pendant, the last when \(W_d\) is also a β-partner. \(W_d\) serves at most one X2 per red head.
3. **The target \(X=Q_T\) under rule F.** This is the recipient piece \((b,c,f,d_X,\mu,u)\). Its red heads \(c\) and \(\mu\) admit no other D-rule.
4. **Everything else.** Any other piece is a first-sweep piece, possibly with a removed type-0 or type-1 trade. It is simple by C1 or by Lemma 4 under (P5) together with C6.

**Removed trades.** Only type-0 and type-1 trades are ever removed, through X2 cancellation (C2) or absorption of a link-0/1 partner. So no recipient loses its source.

**New terminal edges.** I checked every new terminal edge: \(\{e,s(e)\}\), \(\{c,\mu\}\), \(\{c,e\}\) and \(\{\mu,u\}\) from rule F, and \(\{\mu,s(\mu)\}\) and \(\{c,e\}\) from Γ_D. None is wanted by another rule.

**How the windows encode "plain".** A window treats an end as plain by adding inequalities: no named source has that \(c\)-label and no named X2 has that \(d\)-label. This is sound only when every named source actually trades. I checked each window.

- In the windows that list them, \(T\), the received sources and the D-linked X2's all trade.
- An absorbed \(W_d\) does not trade, but the windows never add its \(c\)-label \(\mu\) to the list.
- The one case where a non-trading named source matters, \(\mu=b\) with a type-1 pendant in \(S'\), is exactly the allowed exclusion, and it is justified.

My implementation (§3) asserts that every rebuilt piece has the stated pre-image form before replacing it (`expect`). In 1,288 runs no form mismatch and no "defective trail with no role" occurred.

## 3. Checks

**Windows.** I reran `python -B check_regular_path_p5sweep.py` (log `04-handoff/review-theoremC/p5sweep_rerun.log`): 0 failures.

- The windows are \(S'\) (3 options), α (3), β source and recipient, γ-absorbed (3), Γ_D (9), rule F (9; the `before` assertion checks the exchange in every identification) and the D-rotation (open and \(L=3\), 3 options each).
- **The (P5) axiom.** The axiom added in `P5State` is complete for known facts: the check covers whichever of \(r(u)=x\), \(r(x)=y\), \(m(u)=y\) is added last. It is also sound.

**Own end-to-end checker** (`check_regular_path_theoremC_independent.py`). It is written from the text and implements the first sweep, the X2 case split, D-chains (alternation on paths, the rotation on cycles), the D-pendant before odd cycles, absorption, Γ_D, rule F and odd cycles (blocks, then rotations). It asserts the following:

- Lemma C2 and C3(ii), (iv) and (v);
- the C4 relations and degree bounds, and that D-cycles have length at least 3;
- Lemma C6 and C1;
- that removed trades are of type 0 or 1;
- the pre-image form of every rebuilt piece.

It verifies each output exactly. The planted generic \((M,r,s)\) data satisfy (P1)–(P3) and (P5). They contain X2 sources in cases α, β and γ (links 0, 1, 2, and (F1)), D-paths of lengths 1–5 and D-cycles of lengths 3–7, odd type-2 cycles with D-pendants and type-1 pendants, uniform-rotation odd cycles, and random glue. The graph runs use Lemma 1 constructions on dense graphs (circulants and \(K_5\)-blocks) that happen to satisfy (P5).

| run | verified | failures | notable coverage |
|---|---|---|---|
| `--quick --seed 3` | 187 planted + 57 graph | 0 | 83 D-cycles, 47 rule F, 30 Γ_D, 174 absorptions, 99 D-pendants on odd cycles, 30 odd-cycle rotations |
| `--seed 11 --planted 1200 --graphs 8` | 1,135 planted + 153 graph | 0 | 475 D-cycles (2,396 rotation uses), 250 D-paths, 225 rule F, 242 Γ_D, 896 absorptions, 636 α, 998 D-pendants, 696 odd type-2 cycles (499 block, 197 rotation) |

**Control.** With (P5) dropped from the planted data, the checker fails at once, at Proposition C1: G-configurations appear. So it is sensitive. Graph runs give few X2s (mostly α), so the planted data carry the proof-relevant coverage. Logs: `04-handoff/review-theoremC/`.

## 4. Issues

**M1 (major, expository).** Lemma C8 is a list with "Each kind is covered by the table above". Add a proof along the lines of §2:

- the per-piece roles (own piece; D-partner with at most one X2 per red head; \(Q_T\) only under rule F);
- exclusivity of received and D-linked ends, and of type-1 and D-pendants;
- that cancelled X2's are always absorbed by an existing predecessor;
- that only type-0 and type-1 trades are removed;
- the interface check for every new terminal edge.

Mathematically I found the list complete.

**m1 (minor, reproducibility).** The Lemma 4 run under (P5), which C1 cites, lives only in the scratch file `04-handoff/p5_scratch/l4p5.py`. Move it into `check_regular_path_p5sweep.py` and record its counts. My independent count agrees on 259/720/24; the excluded totals differ (286 against 322) only by bookkeeping.

**m2 (minor).** For the D-rotation endpoint fact, name the partition used: the first-sweep partition, after the D-pendant exchange when \(A_j\) is a D-pendant. Note that all its pieces are trails.

**m3 (minor, Lemma C7 wording).** The sentence "then \(T\) is either cancelled … or on a D-cycle" is incomplete. \(T\) can also exist on a D-path with a cancelled predecessor. That predecessor applies no rule, so the conclusion stands.

**m4 (minor).** The Lemma C2 consequence should say explicitly that an X2 source may still have an incoming type-2 link from a non-trading recipient, and that this is harmless.

**m5 (minor, evidence statement).** §3.3 says that odd type-2 cycles never occurred end to end, and that the author's code does not implement odd-cycle rotations. Cite the referee runs, which cover both, or implement the rotations.

**m6 (minor, status and scope).** Keep "candidate" until M1 is fixed. State plainly that Theorem C is a conditional reduction: degree five follows from Theorem C plus P5\*, which is open and false in its fixed-\(M\) form. Mention the unconditional by-product: every \((r,s)\) satisfies (P5) when no \(M\)-edge lies in a triangle, which recovers Corollary 4. Theorem C should not be counted as a solved conjecture.

## 5. Reproduction

```powershell
Set-Location research/2026-11-25-target-shortlist
python -B check_regular_path_p5sweep.py                                                # author windows, ~2 min
python -B check_regular_path_theoremC_independent.py --quick --seed 3                  # ~10 s
python -B check_regular_path_theoremC_independent.py --seed 11 --planted 1200 --graphs 8   # ~1 min
python -B check_regular_path_theoremC_independent.py --quick --seed 4 --control --skip-lemma --graphs 0   # failures expected
```
