# Thread 04 review: Favaron–Genest–Kouider, degree five (2026-11-26)

**Referee:** independent agent, skeptical pass. **Scope:** 04-HANDOFF, 04, 04b, 04c, 04d (Theorem A), 04e (Theorem B), 04g (Theorems B′ and C), 04h, 04i, 04j, the four earlier referee reports, 04-NOVELTY-fgk2010, and the checkers. I read the FGK problem list directly from the local full text (`~/Downloads/favaron2009.pdf`, extracted to `04-scratch/fgk.txt`; not for redistribution). I edited no existing research file. Scratch is in `04-scratch/`.

## Verdicts

| Claim | Verdict | Notes |
|---|---|---|
| FGK Problem 3 (04c): a simple \(d\)-regular graph with a \(d\)-PD and no 1-factor, every odd \(d\ge5\) | **Correct** | Own re-implementation from the text: valid decomposition and two odd-side bridges at \(x\) for \(d=5,\dots,19\). |
| FGK Problem 5 (04b): negative answer for every odd \(d\ge5\) | **Correct** | Hand-checked all steps; author checker rerun (\(d=5,7,9,11\)): 0 bridges, forced connectors as stated. |
| FGK Problem 6 (04c): perfect middle matching but not rainbow-making, every odd \(d\ge7\) | **Correct** | Own re-implementation, \(d=7,\dots,17\): exact partition, middle edges a perfect matching, type-1 degree 3 at some vertex. |
| Theorem A (04d) | **Correct** | All referee fixes m1–m8 are in the text. Independent checker, full run (seed 2026): ALL CHECKS PASSED. |
| Theorem B (04e) | **Correct (computer-assisted)** | M1 (Lemma 8) and m1–m8 are in the text. Independent checker, full run (seed 31): 6,299 verified, 0 failures. The window checker `check_regular_path_gsweep.py` reran with total failures 0. |
| Theorem B′ (04g §2) | **Correct (computer-assisted)** | Fixes m1–m6 present. Lemma 4/4′ own enumeration reproduces 259/564/24 and 205/548/12, with 0 local diamonds avoiding \(M\). End-to-end rerun: 1,708 verified, 0 failures (§3). |
| Theorem C (04g §3) | **Correct as a conditional theorem, with one fixable checker defect** | Fixes M1, m1–m6 present. The independent checker's **default full run fails once**. The cause is an over-strict assertion in the checker, not a gap in the proof (§2). Theorem C has no new unconditional graph-level consequence. |
| P5\* refuted (04i) | **Correct** | Checker rerun (8 s): 2,000 matchings, 142 Euler orientations per restriction, 0 valid \((r,s)\); \(G\) decomposes. |
| 04j (Conjecture J) | No claim to review | No theorem. Reformulations J1–J3 and evidence only. |

## 1. Problems 3, 5 and 6

**Statements.** These match FGK §6 verbatim in substance:

- Problem 3: "Find for every odd \(d\ge7\) a \(d\)-regular graph with a \(d\)-PD but with no 1-factor."
- Problem 5: "Does every 2-edge-connected simple odd \(d\)-regular graph with a 1-factor admit a \(d\)-PD such that the edges of type 0 form a 1-factor?"
- Problem 6: "For each odd \(d\ge7\), find a \(d\)-regular simple graph \(G\) which admits a \(d\)-PD for which the edges of type 0 form a 1-factor but which is not rainbow-making."

**Problem 3.** I rebuilt the construction from 04c's text only (`04-scratch/verify_p3_p6.py`). For \(d=5,7,\dots,19\) it gives an exact partition into simple \(d\)-edge paths of a simple \(d\)-regular connected graph. The vertex \(x\) has two bridges whose far sides have odd order, so no perfect matching exists. The orders run from 136 to 1,606.

**Problem 5.** I checked the proof by hand.

- Endpoint uniqueness follows from parity and counting.
- The cut identity \(\sum_{i=1}^{k-1}(n_i-|W|)=0\) holds, and two nonmatching crossing edges must have equal level.
- \(H_d\) has no perfect matching (Tutte: delete the \(d-2\) vertices \(s_j\); this leaves \(d\) odd blocks). \(H_d-\{r_1,r_2\}\) has one. So both connectors of every gadget lie in every perfect matching.
- Hence \(u_{i,1}u_{i,2}\in M\) for every \(M\). The path centred there leaves \(U_i\) through \(uu_{i,1}\) or \(uu_{i,2}\) at level 1. So all \(2k\) nonmatching edges at \(u\) have level 1, which contradicts \(u\) being an endpoint.

The author's checker reran in 3 s (0 bridges; 144 paths at \(d=5\)).

**Problem 6.** I rebuilt the \(K_8\) paths and the copy-shift extension. It passes for \(d=7,\dots,17\). The type-1 degree is 3 at 6 of the 8 labels in each copy.

**Status upstream.** There are no hits in `origin/main` or `origin/research` for Favaron, Genest, Kouider, Kotzig, `jgt.20413`, "path decomposition" (except an unrelated Althöfer note), "rainbow-making" or "five-edge path". There are no hits in upstream issues or PRs for Favaron, Genest, Kotzig, "regular path", "path decomposition", "five-edge paths" or "P5-decomposition". **Unpublished.**

**Prior resolution.** None found (§4). The MathOverflow thread 97683, read through the Stack Exchange API, discusses only the main conjecture and Kotzig's cubic case.

**Significance, stated plainly.**

- These are complete answers to three open questions from a 2010 JGT paper. All three are elementary constructions.
- Problems 3 and 6 are "find an example" exercises. FGK expected positive answers: for Problem 3 they wrote "we think that a similar example can be constructed for every odd \(d>5\)", and for Problem 6, "we do not think that Theorem 2 holds for \(d>5\)".
- Problem 5 is a genuine yes/no question. The answer is a gadget substitution into FGK's own Figure 3 obstruction.
- They are correct and new as far as I can tell. They are **not** a bigger deal than the degree-five partial theorem, and none touches Conjecture 1.

**Minor fixes for 04b/04c before publication.**

1. 04c, opening: say explicitly that Problem 3 asks only for \(d\ge7\), that \(d=5\) is FGK's own Figure 7 graph \(G_1\), and that the construction covers \(d\ge5\) uniformly. It nearly says this already.
2. 04c, Problem 6: quote the exact problem wording. "Asks whether Theorem 2 extends beyond degree five" paraphrases its preamble.
3. 04b: name the second implementation ("A separate implementation checked…") or point to its file. Otherwise it is not reproducible.
4. Both: add a reproducible checker for 04c. Only "independent JS" is mentioned, and no file is given. `04-scratch/verify_p3_p6.py` can serve.

## 2. Theorems A, B, B′ and C: fresh read and reruns

**Earlier fixes.** Every requested fix appears in the current text:

- A: m1–m8;
- B: M1, now Lemma 8 with a proof, and m1–m7; m8 is a code change;
- B′: m1–m6;
- C: M1, now the proof of Lemma C8, and m1–m6.

I checked each change against the report wording.

**Theorem B, skeptical points re-derived.**

- Γ-rule edge multiset. \(Q'_c\cup W\) and \(N_1\cup N_2\) both consist of \(bc,cf,fb,bh,hY^*\) and \(A'g,gf,fp,pq,q\,s(q)\). In case γ the source piece is \((A',g,f,p,q,s(q))\), which is consistent with the labels \(a=s(g),b=g,c=q,d=p,e=f\).
- Rotation telescoping. It is correct as written. \(c_{k+1}=q_k\), \(b_{k+1}=g_k\) and \(e_{k+1}=f_k\) are consistent with the Gtarget definition. The edge \(\{c_{k+1},c_{k+2}\}\) is \(W_{k+1}\)'s terminal edge by (F1).
- Lemma 5(ii). A case-γ \(W_0\) has no incoming type-2 link, so it heads its type-2 path and is a source. Absorption, Γ and Gtarget therefore exhaust case γ.
- Lemma 7 and the rotation. A G-pendant is never a \(d\)-label, so G-pendants never meet the uniform rotation.
- Soundness of the engine. The windows list true facts only, and identifications range over all set partitions. A pass is therefore sound, and the soundness rests on the facts being true. Both the B and B′ referees audited every fact. I spot-checked W3 (\(Z\ne p\)) and the type-2 fact \(q\ne e\); both are correct.

I found no new gap. The proof remains a large case analysis certified by a custom enumeration engine, with no Lean and no external referee. That is the main residual risk.

**Theorem C: one new finding (checker defect, not a proof gap).** The default full run `python -B check_regular_path_theoremC_independent.py`, with seed 3 and 1,200 planted instances, which no earlier session ran, reports **FAILURES: 1**: "Lemma C6: D-pendant is a local label".

- **Diagnosis** (`04-scratch/thmC_diag.py`, instance in `04-scratch/C_failures_seed3.pkl`). The instance satisfies (P1)–(P3) and (P5). It has an odd type-2 cycle with \(L=7\), on which a D-pendant satisfies \(A_2=d_5\), the \(d\)-label of a non-adjacent trail. Lemma C6 claims only that a D-pendant is not a \(b\)-, \(c\)- or \(e\)-label and not its **own** \(d_i\). Lemma 4 allows a changed pendant to equal another trail's \(d\)-label; the uniform rotation needs exactly that. The checker line 299 (`if A_[i] in loc`, with `loc` containing **all** \(d\)-labels) is stricter than the lemma.
- **Confirmation.** With that assertion corrected to \(B\cup C\cup E\cup\{d_i\}\), the same instance gives a verified decomposition under 10 RNG seeds. Two further full runs (seed 21, and seed 3 with `--skip-lemma`) passed with 1,116 and 1,141 verified decompositions (`04-scratch/thmC_relaxed.py`, logs `run_C_relaxed_*.log`).
- **Fixes required:**
  - (i) Correct line 299 of `check_regular_path_theoremC_independent.py`.
  - (ii) Correct 04-REVIEW-theorem-C §1. It says the D-pendant "is not a local \(b\)-, \(c\)-, \(d\)- or \(e\)-label", and that "Lemma C6 is asserted in every case: the D-pendant is not a local label". Both should exclude only its own \(d_i\).
  - (iii) Record the default-run result in 04g §3.3. The earlier published reruns used `--quick --seed 3` and `--seed 11`, which happened to avoid this case.
- **Side note.** The run wrote `04-handoff/review-theoremC/failures.pkl` on failure. I moved it into `04-scratch/` so that no research directory was altered.

**Theorem C, scope.** (P5) is a property of \((M,r,s)\), not of \(G\). P5\* is false (04i), and Conjecture J is open (04j). So the only graph class Theorem C currently certifies is "no \(M\)-edge in a triangle", which is Corollary 4 of Theorem A and is also contained in B′. Theorem C is a correct and reusable *reduction*, but at present it has **no new unconditional consequence**. It belongs in the research record, not in a catalogue entry.

**Best result.** It is **Theorem B′**: no diamond of \(G\) contains an edge of the perfect matching \(M\). B′ contains Theorem B (diamond-free, any \(M\)), Corollary 4, Chu–Fan–Hong–Zhou 2024, Botler–Mota–Wakabayashi 2015, and the existence part of FGK's \(C_4\)-free theorem. Theorem A is a separate, incomparable matching-relative companion and should be published in the same entry.

## 3. Reruns (this session, Python 3.12, Windows)

| Checker | Mode | Result |
|---|---|---|
| `check_regular_path_theoremA_independent.py` | full, seed 2026 | ALL CHECKS PASSED; Lemma 4 766/125/386/12 reproduced |
| `check_regular_path_theoremB_independent.py` | full, seed 31 | ALL CHECKS PASSED; 6,299 verified (2,519 planted, 3,780 graph); 188 odd Gtarget rotations, 248 Γ-at-node, 436 odd type-2 cycles with G-pendant |
| `check_regular_path_theoremBprime_independent.py` | full default parts, 25-min cap | lemma4: 259/564/24 and 205/548/12, 0 local diamonds avoiding \(M\); exact: 0 mismatches; end-to-end: **1,708 verified, 0 failures** (280 K5-block, 416 circulant, 1,012 planted); control with the hypothesis off fails as intended. The windows part was **cut off by the cap** after the first 20 windows (Q\*, P\*, W0-absorbed, Q\*γ and the first Γ type-2 options), all with 0 failures. The remaining windows were not rerun with the own filter this session. |
| `check_regular_path_theoremC_independent.py` | full, seed 3 | **1 failure**: a checker assertion, see §2. After the fix: seeds 21 and 3 ALL PASSED |
| `check_regular_path_p5sweep.py` | full | total failures 0 (67 s) |
| `check_regular_path_gsweep.py` | full (Theorem B windows W1–W8, L4′) | **total failures 0** in 10 min 30 s. L4′: 205/548/12 with 243 excluded; W7 excluded counts 527/16,365/18,467, exactly as in 04e |
| `check_regular_path_center_counterexample.py` | \(d=5,7,9,11\) | as stated in 04b (3 s) |
| `check_regular_path_p5star_counterexample.py` | full | P5\* fails; \(G\) decomposes (8 s) |
| own `04-scratch/verify_p3_p6.py` | P3 \(d=5..19\), P6 \(d=7..17\) | all pass |

Not rerun: `check_regular_path_mdiamond.py` (about 25 min). The B′ referee had already reproduced its window identification counts with an independent filter.

## 4. Prior-resolution and novelty log (2026-11-26)

**arXiv API** (newest first, spaced calls):

| Query | Result |
|---|---|
| `abs:"path decomposition" AND abs:regular AND abs:"perfect matching"` | 0 |
| `all:Favaron AND all:Kouider` | 2510.12806 (Eulerian graphs; not relevant); 2012.05145 (spanning Cayley subgraphs) |
| `abs:"paths of length" AND regular AND "perfect matching"` | 1510.02526 (2k-regular, Kouider–Lonc); 1211.2374 |
| `abs:"5-regular" AND decomposition AND path` | 2012.05145 |
| `abs:"path decompositions" AND abs:regular` | nothing relevant (2411.06982 oriented graphs) |
| `"P_5-decomposition" OR "paths of length five"` | 2604.11664 (paths with equal-degree endpoints; unrelated); 1910.02819 (quartic planar) |
| `abs:"odd regular" AND path AND decomposition` | 0 |
| `au:Botler AND abs:path` | 13 hits, all known (1505.04309 highly connected P5; 1509.06393; 1607.01456; 2012.05145; Gallai papers) |
| `"regular graph" AND "paths of length" AND decomposition` | 1607.01456; unrelated |

**Web** (three extended searches). The hits were FGK 2010, BMW 2015, Botler–Mota–Oshiro–Wakabayashi (girth \(\ge 2k\)), Chu–Fan–Hong–Zhou 2024 (SSM-2023-0316), Botler–Hoffmann (DM 2022), Montgomery et al. (JLMS 2025, approximate), West's open-problems page (lists the conjecture as open), Botler's thesis summary, and MathOverflow 97683. Nothing addresses FGK Problems 3, 5 or 6. Nothing proves the diamond-free or M-diamond-free degree-five case. Nothing resolves Conjecture 1.

**GitHub code search** (spaced at 8 s):

- `"Favaron" "Kouider"`, `"Genest" "Kouider" path`, `"jgt.20413"`, `"5-regular" "path decomposition"`, `"regular path decomposition"`, `"rainbow-making"`, `Favaron path decomposition`, `"paths of length five" regular`, `"odd regular" "path decomposition"`, `Favaron Genest` and `"perfect matching" "paths of length" regular conjecture`: 0 relevant hits.
- `"P5-decomposition"`: one unrelated hit (a SystemVerilog page).
- `Kouider`: only unrelated namesakes.

**GitHub repository search.** `path decomposition regular graph`, `Favaron conjecture` and `P5 decomposition 5-regular` gave 0.

**AI-solution repos.** I grepped the file trees for favaron, kouider, path-decomp, regular-path, kotzig, five-edge and lichiardopol, and searched issues and PRs.

| Repo | Result |
|---|---|
| s66lem/conjectures | 0 |
| chy4pro/automath | only `tdn_r1_census_p5.out` (unrelated) |
| the-omega-institute/trureturing | unrelated "P5" Potts folders; issue search hits unrelated |
| ai-math-edu-lab/math-agents | unrelated Kourovka "a5-p5" |
| google-deepmind/formal-conjectures | `Paper/KotzigConjecture.lean` is Kotzig's *graceful/cyclic tree* conjecture (unrelated); issue/PR search "Favaron" gave #8309 (WOWII Graffiti, a different Favaron context) and #4413 (unrelated) |

**Conclusion.** No prior resolution of Problems 3, 5 or 6 was found. Theorems A, B and B′ are not stated in any source checked, and Conjecture 1 remains open in degree five. This is a bounded search, not a certificate. The citation lists of CFHZ 2024 and Montgomery et al. still could not be retrieved; SSM returned rate limits in earlier sessions.

## 5. Significance and placement

**Policy (AGENTS.md).** A special case is not a resolution. Do not farm narrow targets. FGK Conjecture 1 (2010) is a genuine named conjecture with a small but steady literature: FGK 2010, BMW 2015, BMOW 2017, Botler–Hoffmann 2022, CFHZ 2024, and Montgomery–Müyesser–Pokrovskiy–Sudakov 2025. It is not a major problem. The degree-five case is its first open case.

**Theorem B′ (with A and B) as a partial result.**

- It strictly extends the most recent published special case, CFHZ 2024, as well as BMW 2015, to an infinite natural class: every diamond-free 5-regular graph with a perfect matching, and more generally every \(M\) that avoids diamonds.
- That is a real but incremental advance. It is computer-assisted through a custom engine, with no Lean and no external referee.
- **Listable, but low.** It qualifies for "Partial results on open problems" as a precise partial theorem.
- **Placement:** immediately **below "Erdős essential-component conjecture"** and immediately **above "Erdős–Gyárfás power-of-two cycles"**.
- **Reason.** It settles a broad natural graph class rather than one sporadic family or instance, which is more than the abelian-cover bound below it, Erdős–Oler on lattices or the single order 2396. But it concerns a niche conjecture, \(d=5\) only, by a computer-assisted case analysis, so it sits below the general quantitative or structural results on Erdős-type problems above.
- Theorem C and the P5\* refutation are issue-only. Theorem A goes in the same entry as B′. Do not count it separately.

**Problems 3, 5 and 6 in the Results table.**

- If they are published, use **one combined entry**, "Favaron–Genest–Kouider Problems 3, 5 and 6". Problem 5 carries the content; 3 and 6 are exercises.
- Rank it in the bottom tier. Insert it immediately **after "Rectangle partition asymptotics" (last of the rank-140 tie group) and before "Alexandersson’s parking-function excedance conjecture" (rank 148)**.
- **Reason.** These are elementary constructions answering open questions from one paper. They are comparable to Graffiti.pc 318 and Mazák–Zrubák, and below every entry with a general theorem.
- Under a strict reading of the significance policy, a maintainer could reasonably keep Problems 3 and 6 issue-only and publish Problem 5 alone at that rank.

## 6. Readiness

**Ready after listed fixes.**

1. Theorem C checker line 299 and the C-review wording (§2). This does not block B′, but the package should not ship a checker whose default run fails.
2. 04b/04c items 1–4 (§1).
3. Optionally, rerun `check_regular_path_mdiamond.py` (author, about 25 min) and the B′ own-filter windows on the publication tree. This session's 25-minute cap cut off the own-filter windows (§3). `check_regular_path_gsweep.py` was rerun in full: 0 failures.

No mathematical gap was found in A, B, B′, C or in Problems 3, 5 and 6.
