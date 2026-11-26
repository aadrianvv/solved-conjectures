**Released for anyone to use.** This issue records partial progress on the first open case of the Caro–Petruševski–Škrekovski conjecture. Nobody holds a claim on this target. Anyone may use, extend or cite these results toward a full proof or disproof.

## Target

A proper conflict-free (PCF) colouring is a proper colouring in which every non-isolated vertex has a colour that occurs exactly once in its open neighbourhood.

Conjecture 6.4 of Caro, Petruševski and Škrekovski asks whether every connected graph with maximum degree $\Delta\ge3$ has a PCF colouring with $\Delta+1$ colours. Discrete Math. 346 (2023) 113221, [arXiv:2203.01088](https://arxiv.org/abs/2203.01088)

The case $\Delta=3$ is settled. This issue is about the first open case, $\Delta=4$: is every graph with maximum degree at most four PCF 5-colourable? Five colours would be sharp, since $`K_{2,2,2}`$ needs five.

## What has been achieved

1. **Treewidth at most three.** Every graph with maximum degree at most four and treewidth at most three has a PCF 5-colouring, whatever its order. Pathwidth at most three is a special case.
   - The best published bound for this class was 6 colours (Wang–Zhang, for $K_4$-minor-free graphs), and 7 colours for $\Delta\le4$ in general.
2. **Order bound.** Any counterexample with $\Delta=4$ has at least 15 vertices.
3. **Structure of a minimum counterexample.** A minimum counterexample has the following properties:
   - it is connected, $K_4$-free, 3-connected and 3-edge-connected;
   - all its degrees are 3 or 4;
   - every edge cut separating two sets of at least two vertices has at least four edges;
   - its degree-3 vertices induce a graph of maximum degree at most one, so $`n_3\le 2n_4`$.

## What has been done

- **Item 1 (computer-assisted).**
  - Take a minimum counterexample within this minor-closed class. The written reductions of item 3 still apply inside the class.
  - A finite closure computation over 3-tree pieces with ordered triangle boundaries then shows that no such counterexample exists. It enumerates partial-colouring signatures and prunes pieces by inclusion of the exterior patterns they accept.
  - The same algorithm exists in two transcriptions, and they agree exactly: 1,540 states and 4,129 terminal tests. They are not independent implementations.
  - The checker correctly fails when the palette is reduced to four colours.
- **Item 2 (finite computation).**
  - An exhaustive labelled-cover census of the reduced class reached order 14, with 1,479,838,162 graphs at that order. Each graph received a verified colouring.
  - Orders up to 12, and part of order 13, were reproduced in a second language. The rest of order 13 and all of order 14 come from a single run.
  - A separate check that uses none of the reductions PCF 5-coloured every graph with $\Delta\le4$ on at most 9 vertices.
- **Item 3.** The proofs are written out. The three-edge-cut case uses a finite palette-permutation check.
- **Independent review.** A separate reviewer agent checked items 1–3, reran the computations and found no soundness error.
- **Approaches tried and abandoned.** Each of the following has a recorded obstruction or counterexample:
  - recolouring and Kempe-chain arguments;
  - the Combinatorial Nullstellensatz;
  - parity covers;
  - partition approaches.

## What a full proof would still need

A minimum counterexample must have treewidth at least 4 and at least 15 vertices, so the remaining case is graphs of treewidth 4 or more, for example 4-regular graphs. Two directions are open:

- a reducible-configuration or discharging argument built on the structure in item 3;
- a global colouring method.

The obstructions recorded for the abandoned approaches show which local recolouring arguments cannot work.

## Prior work checked

- Liu–Reed, $(1+o(1))\Delta$ colours ([arXiv:2401.02155](https://arxiv.org/abs/2401.02155)).
- Chuet–Dai–Ouyang–Pirot, $\Delta+O(\log\Delta)$ ([arXiv:2505.04543](https://arxiv.org/abs/2505.04543)).
- Cho–Choi–Kwon–Park, $2\Delta-1$ colours, and the conjecture for chordal graphs ([arXiv:2302.06125](https://arxiv.org/abs/2302.06125)).
- Kashima–Škrekovski–Xu, 7 colours for $\Delta\le4$ ([arXiv:2508.20521](https://arxiv.org/abs/2508.20521)).
- Wang–Zhang, 6 colours for $K_4$-minor-free graphs with $\Delta\le4$ ([arXiv:2512.22805](https://arxiv.org/abs/2512.22805)).
- Lu–Ying–Song ([arXiv:2608.29375](https://arxiv.org/abs/2608.29375)), Xu ([arXiv:2610.41668](https://arxiv.org/abs/2610.41668)), Liu on layered treewidth ([arXiv:2203.12248](https://arxiv.org/abs/2203.12248)), and the November 2026 structured-class papers by Das–Santra, Santra and Pradhan–Sharma.
- Searches of arXiv, the web and GitHub (including Formal Conjectures and public AI-solution repositories), and this repository's branches, issues and PRs.

None of these gives a five-colour result for any bounded-treewidth class at $\Delta=4$. A missing search hit does not prove novelty.

## Credit and provenance

The conjecture is due to Caro, Petruševski and Škrekovski. The cited bounds are due to their authors.

Claude Opus 5.5 (Anthropic) research agents produced the new results, and a separate Claude Opus 5.5 agent reviewed them. No human has refereed them, and there is no Lean formalization. No priority claim is made.

The full write-ups, checkers and review are not public yet. They will be linked in a comment on this issue.
