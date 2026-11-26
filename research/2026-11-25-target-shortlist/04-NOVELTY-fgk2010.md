# Novelty check of Theorem A against Favaron–Genest–Kouider (2010)

Checked by the coordinator on 2026-11-25 against the full text of O. Favaron, F. Genest and M. Kouider, *Regular path decompositions of odd regular graphs*, J. Graph Theory 63 (2010) 114–128, [doi:10.1002/jgt.20413](https://doi.org/10.1002/jgt.20413). The full text was supplied by the repository owner. It is kept locally, not in the repository.

**Verdict.** Theorem A is not in FGK, and the two results are incomparable. FGK's Theorems 6 and 7 use a different notion of "bad pair" and prove a stronger matching-specific conclusion under a hypothesis that neither contains nor is contained in ours. This closes reviewer issue M1 of [04-REVIEW-theorem-A.md](04-REVIEW-theorem-A.md), subject to the presentation fixes below.

## What FGK prove

- **Definitions, §5.** For a 1-factor M of a simple 5-regular graph, an *M-triangle* (or *M-square*) is a cycle of length 3 (or 4) with exactly one edge of M. These are the same as ours. A pair of M-cycles is a **bad pair (FGK)** if the two cycles share at least one edge and the graph with edge set (E(C₁) ∪ E(C₂)) \ M has a vertex of degree 3.
- **Theorem 6.** If M induces no bad pair (FGK) of M-cycles, then M is *extendable*: G has a 5-path decomposition whose middle edges are exactly the edges of M.
- **Theorem 7.** Let H be the graph whose vertices are the M-cycles in some bad pair, with an edge for each bad pair. If H is a star, then M is extendable.
- **Corollary.** If no two cycles of length 3 or 4 share an edge, then every 1-factor is extendable.
- **Introduction.** In a 5-regular graph where no 4-cycle shares an edge with a triangle or with another 4-cycle, every 1-factor is extendable. FGK also show that the C₄-free case follows.
- **Method.** The proof of Theorem 6 splits vertices along M-cycle edge pairs, takes an Eulerian orientation, applies Petersen's 2-factorization, and reverses one 2-factor.

## Comparison with Theorem A

Ours forbids an M-triangle and an M-square from sharing any edge, and concludes only that some 5-path decomposition exists; its middle edges need not be M.

1. **Theorem A covers cases FGK do not.** Square–square and triangle–triangle overlaps are unrestricted in Theorem A, but FGK forbid them whenever they form an FGK bad pair. Exact computation (`04-handoff/review-theoremA/fgk_badpairs.py`):
   - With its stated matching, the **408-vertex example** has 136 M-squares, no M-triangles and no triangle–square conflict, so Theorem A applies. It has **68 FGK bad pairs, all square–square**, and its bad-pair graph H is **not a star**, so FGK Theorems 6 and 7 do not apply.
   - **K₅,₅** with a perfect matching has 420 square–square FGK bad pairs. It is triangle-free, so it is already covered by Botler–Mota–Wakabayashi; it is included only to illustrate the definition.
2. **FGK cover cases Theorem A does not.**
   - Take an M-triangle uva and an M-square uvbc with uv ∈ M that share only the M-edge uv. Every vertex of their union minus M has degree 2, so this is not an FGK bad pair, but it is a conflict for Theorem A.
   - FGK's conclusion is also stronger: M itself is extendable.
3. **Graph-level classes.** FGK's introduction family (no 4-cycle shares an edge with a triangle or another 4-cycle) has no triangle–square conflict for any M. So, given a perfect matching, Theorem A contains it, as does the Chu–Fan–Hong–Zhou 2024 class. Corollary 4 (some perfect matching lies in no triangle) is not covered by FGK Theorems 6 and 7, as the 408-vertex example shows at the matching level.

## Required fixes before publication

- **Rename our "bad pair"**, for example to *triangle–square conflict*. Otherwise it collides with FGK's established term for a different notion.
- **Cite FGK Theorems 6 and 7 in the Statement** and add the comparison above: the hypotheses are incomparable, and FGK's conclusion is stronger where it applies.
- **Credit the construction.** If Lemma 1's splitting, Eulerian orientation and Petersen 2-factorization follow FGK's proof of Theorem 6 (and its cited source [8]), say so explicitly.
- **Restate Corollary 1 precisely.** FGK's own statement is stronger: every 1-factor is extendable, for a class larger than the C₄-free graphs.
- A literature check of later citers of FGK for the same matching-relative statement remains bounded (see the review); no source found states Theorem A.
