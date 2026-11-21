# Mazák–Zrubák conjecture on complete graphs minus an edge

[Catalogue](../../CONTENTS.md) · [Proof](PROOF.md) · [Exact checks](verify.py) · [Issue #147](https://github.com/1337isnot1337/solved-conjectures/issues/147)

**Status:** Written proof for every even $`d\ge 6`$. It has been through one independent referee pass by a second model instance, which found no mathematical error; the justifications it asked for are included. The note is otherwise unrefereed. The finite checks cover $`d=4`$ and $`d=6`$ only.

**Lean status:** none. No Lean formalization is included.

Primary source: J. Mazák and F. Zrubák, *Circular chromatic index of small graphs*, [arXiv:2603.08822](https://arxiv.org/abs/2603.08822), Conjecture 2.

## Result

A circular $`r`$-edge-colouring of a graph $`G`$ is a map $`c:E(G)\to[0,r)`$ such that $`1\le|c(e)-c(f)|\le r-1`$ whenever $`e`$ and $`f`$ share a vertex. The circular chromatic index $`\chi'_c(G)`$ is the least $`r`$ for which one exists; it satisfies $`\chi'(G)-1\lt\chi'_c(G)\le\chi'(G)`$.

**Theorem.** Let $`d\ge 6`$ be even and let $`G`$ be the complete graph $`K_{d+1}`$ with one edge removed. Then $`\chi'_c(G)=d+1`$.

This is Conjecture 2 of Mazák and Zrubák, who verified it by computer for $`d\in\{6,8,10,12\}`$. For $`d=4`$ the statement is false: $`\chi'_c(K_5-e)=9/2`$.

Since $`\chi'(G)=d+1`$, it suffices to exclude $`\chi'_c(G)\lt d+1`$. By Guichard's theorem, whose proof is included, such a value would give a proper $`(d+1)`$-edge-colouring whose digraph of consecutive colours is acyclic. The proof shows that the longest-path levels of that digraph order the edges linearly with rigid constraints. It then arranges the positions of each vertex in a table with $`d+2`$ columns and locates where each vertex changes rows. For $`d\ge 6`$ two vertices of degree $`d`$ are forced to share two positions, although they are joined by exactly one edge. For $`d=4`$ this last step has nothing to compare, in accordance with the value $`9/2`$.

Lemma 1 is Guichard's theorem and is not new. Guichard's paper is quoted through Zhu's survey and was not read directly. A literature search on 21 November 2026 found no proof of the conjecture.

## Verification

Run from the repository root with Python 3.10 or later and no other dependencies:

```sh
python3 results/circular-index-complete-minus-edge/verify.py
```

Part A enumerates all 2160 proper 5-edge-colourings of $`K_5-e`$, finds the 180 with acyclic digraph, and checks on each the statements of Lemmas 2, 3, 4 and 5(1). Part B searches exhaustively, up to automorphisms of the graph, for edge orderings with the properties of Lemma 3. There are 3 for $`d=4`$, matching the 180 colourings of Part A, and none for $`d=6`$. The script takes about 10 to 20 seconds.

The proof does not depend on any of the scripts. They check its statements on small cases. Our scripts cover $`d=6`$ directly; a run for $`d=8`$ was not completed. The computer check of Mazák and Zrubák covers $`d\le 12`$. The theorem for general $`d`$ rests on the written proof.

Optional checks, not run by CI:

- [`verify_sat.py`](verify_sat.py) needs `python-sat`. Run as `python3 results/circular-index-complete-minus-edge/verify_sat.py 4 6`, it checks directly from the definition, without using any lemma, that $`K_7-e`$ has no proper 7-edge-colouring with acyclic digraph and that $`K_5-e`$ has one.
- [`review/`](review) contains the scripts of the referee pass, which share no code with the two above. [`d4_check.py`](review/d4_check.py) checks every statement from Lemma 2 to Lemma 7 on all 180 acyclic colourings of $`K_5-e`$. [`sat_levels.py`](review/sat_levels.py), run as `python3 results/circular-index-complete-minus-edge/review/sat_levels.py 4 6`, is a second SAT check from the definition with a different encoding and needs `python-sat`. [`relaxed.py`](review/relaxed.py), run as `python3 results/circular-index-complete-minus-edge/review/relaxed.py 3 4 5`, tests the implications of Lemmas 6 and 7 on relaxed configurations. [`arith.py`](review/arith.py) checks the arithmetic identities for $`3\le h\le 20`$.

## Files

- [`PROOF.md`](PROOF.md): statement, proof, the remark on $`d=4`$, the verification summary and sources.
- [`verify.py`](verify.py): standard-library check of the lemmas for $`d=4`$ and of the ordering obstruction for $`d=6`$.
- [`verify_sat.py`](verify_sat.py): SAT check from the definition.
- [`review/`](review): the referee pass's independent scripts.
