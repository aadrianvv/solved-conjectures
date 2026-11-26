**Released for anyone to use.** This issue records partial progress on the Favaron–Genest–Kouider conjecture and releases it. Nobody holds a claim on this target. Anyone may use, extend or cite these results toward a full proof or disproof.

## Target

Conjecture 1 of Favaron, Genest and Kouider: every simple odd $d$-regular graph with a perfect matching has an edge partition into paths with exactly $d$ edges. The perfect matching need not be the set of middle edges. The first open case is $d=5$. [O. Favaron, F. Genest, M. Kouider, *Regular path decompositions of odd regular graphs*, J. Graph Theory 63 (2010) 114–128, §6](https://doi.org/10.1002/jgt.20413)

## What has been achieved

The results for $d=5$ are partial.

- **Theorem B′.** Let $G$ be 5-regular with a perfect matching $M$. If no diamond ($K_4^-$) of $G$ contains an edge of $M$, then $E(G)$ partitions into 5-edge paths.
  - **Theorem B**, the special case: every diamond-free 5-regular graph with a perfect matching decomposes.
  - Theorem B′ contains Chu–Fan–Hong–Zhou 2024, Botler–Mota–Wakabayashi 2015, and the existence part of FGK's $C_4$-free theorem.
- **Theorem A**, a companion result with an incomparable hypothesis.
  - **Hypothesis:** some perfect matching $M$ has no $M$-triangle sharing an edge with an $M$-square, where an $M$-square is a 4-cycle with exactly one $M$-edge.
  - **Conclusion:** the same decomposition exists.
  - **Corollary:** if some perfect matching has no edge in a triangle, the graph decomposes.
  - **Comparison:** FGK's Theorems 6–7 use a different "bad pair" hypothesis and conclude more, namely that $M$ is extendable.
- **Theorem C**, a conditional reduction. Suppose the FGK construction data $(M,r,s)$ can be chosen with property (P5): no path $u\to x\to m(u)$ in the first 2-factor. Then $G$ decomposes.
  - A 30-vertex graph shows that (P5) can fail for every choice of $M$, although that graph still decomposes.
  - Theorem C is therefore a tool, not a solved case.

There are also complete answers to three questions in FGK §6. These are constructions for all degrees, checked by scripts.

- **Problem 3.** For every odd $d\ge5$ there is a simple $d$-regular graph with a $d$-path decomposition and no perfect matching.
- **Problem 5.** The answer is no for every odd $d\ge5$. A 2-edge-connected $d$-regular graph with a perfect matching need not have a decomposition whose middle edges form a perfect matching.
  - The $d=5$ example has 288 vertices.
  - It still satisfies Conjecture 1.
- **Problem 6.** For every odd $d\ge7$ there is a path decomposition with a perfect middle matching that is not rainbow-making.

## What has been done

- **Method.** The proofs follow FGK's pipeline: splitting, an Eulerian orientation, and a Petersen 2-factor construction.
  - Two repair sweeps then fix the locally bad configurations.
  - A finite set of local windows is certified by an exhaustive identification engine. This makes Theorems B and B′ computer-assisted.
  - Theorem A's written proof uses one exhaustive finite lemma.
- **Independent review.**
  - Separate reviewer agents refereed Theorems A, B, B′ and C. Every fix they requested is in the current write-ups.
  - Independent checkers reran without failure. One of them, for Theorem B, verified 6,299 end-to-end decompositions.
  - A second review pass rebuilt the Problem 3 and 6 constructions independently.
- **Approaches tried and abandoned.**
  - A stronger form of (P5), called P5\*, is false. The 30-vertex counterexample above refutes it.
  - The case where each $M$-edge lies in at most one triangle was reformulated several ways. These reformulations are internal tools only.

## What a full proof would still need

- **The remaining $d=5$ case:** graphs in which every perfect matching meets a diamond, such as graphs with many $K_4$ or $K_5^-$ subgraphs. Two routes look possible:
  - show that (P5) can be arranged for some $M$, at least when every $M$-edge lies in at most one triangle (exhaustive data up to order 10 support this), and then apply Theorem C;
  - find a repair step for diamonds that contain an $M$-edge.
- **All degrees $d\ge7$.** The local-window certification would have to be generalised, or replaced by an argument that does not depend on $d$.

## Prior work checked

- FGK 2010 (full text, including Theorems 6–7 and Problems 1–7).
- Botler–Mota–Wakabayashi (triangle-free, [Discrete Math. 2015](https://doi.org/10.1016/j.disc.2015.04.018)) and Botler–Mota–Oshiro–Wakabayashi (girth at least $2k$).
- Botler–Hoffmann ([arXiv:2012.05145](https://arxiv.org/abs/2012.05145)).
- Chu–Fan–Hong–Zhou ([Sci. Sin. Math. 2024](https://www.sciengine.com/SSM/doi/10.1360/SSM-2023-0316)).
- Montgomery–Müyesser–Pokrovskiy–Sudakov ([JLMS 2025](https://doi.org/10.1112/jlms.70269)).
- MathOverflow 97683 and West's open-problems page.
- Searches of arXiv, the web and GitHub, including public AI-solution repositories and google-deepmind/formal-conjectures.
- This repository's branches, issues and PRs.

None of these resolves Conjecture 1 or states the results above. The search was bounded.

## Credit and provenance

The construction, the cut identity and the Figure 3 obstruction are due to FGK. The special cases contained above are due to the authors cited.

Claude Opus 5.5 (Anthropic) research agents produced the new results, and separate Claude Opus 5.5 agents reviewed them. No human has refereed them, and there is no Lean formalization. No priority claim is made.

The full write-ups, referee reports and checking scripts are not public yet. They will be linked in a comment on this issue.
