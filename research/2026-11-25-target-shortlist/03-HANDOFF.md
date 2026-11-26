# Proper conflict-free colouring handoff

## Target and status

The remaining target is the ordinary five-colour case of Caro–Petruševski–Škrekovski's Conjecture 6.4 for maximum degree four. A proper colouring must have a colour of multiplicity one in every nonempty open neighbourhood. The original connected-graph conjecture concerns $\Delta\geq3$ and $\Delta+1$ colours. The degree-three case is already settled. The new arguments below establish special cases and restrict a smallest obstruction. The unrestricted degree-four case remains open in this work.

**Second-session status (2026-11-25).** The second session found no unrestricted proof and no counterexample. It closed the order-13 and order-14 censuses, so any counterexample has at least 15 vertices. It added a splitting lemma and recorded explicit barriers for parity covers, Lovász partitions, static witness schemes, reverse-BFS greedy colouring and the six-colour cycle reduction. It also completed the 4-regular order-15 stratum and an exhaustive order-11 Kempe reconfiguration census. The latter shows that three Kempe moves are sometimes needed.

The main [research note](03-conflict-free-colouring.md) has the proofs, precise assumptions and source links. The published general bound located for $\Delta=4$ is seven. The known degree-dependent $(\mathrm{degree}+3)$ list theorem also gives seven. The stronger regular results in Liu–Reed's *Peaceful Colourings* require sufficiently large maximum degree. The bounded literature, formal-library and repository checks located no competing resolution for degree four.

## Results established here

| Result | Scope and proof |
| --- | --- |
| Minimum degree and clique reduction | A minimum-order obstruction is connected, has degrees three or four, and is $K_4$-free. Test one extra neighbour by an at-most-one-colour exclusion. Suppress degree-two vertices and extend across a four-clique by Hall's theorem. |
| Edge and vertex connectivity | A minimum obstruction is 3-connected and has no edge cut of size at most three separating two sets of at least two vertices. For nontrivial three-edge cuts the three crossing shapes are handled by a palette-permutation calculation and small graph caps. |
| Cubic vertices | The induced graph on cubic vertices has maximum degree one. Thus $n_3\leq2n_4$. A triangle with two cubic vertices and one quartic vertex has the further exterior constraints described in the note. |
| Matching four-edge cuts | Several sufficient boundary states allow extension. They include four distinct colours and at most one bad insertion colour on one side. The more general load criterion uses $2m_c+w_c$ for each colour. These results use four distinct terminals on each side. |
| Pathwidth at most three | Every subquartic graph in this class is PCF five-colourable. The minor-closed reductions apply within the class, then the [pathwidth checker](check_03_pathwidth_three.js) closes a three-vertex frontier. |
| Treewidth at most three | Every subquartic graph in this class is PCF five-colourable. The [treewidth checker](check_03_treewidth_three.js) works over 3-tree construction pieces and compares their accepted exterior colour patterns. This result has no graph-order cutoff. |
| Few initial defects | A minimum obstruction with a cubic vertex has a proper five-colouring with exactly one defect. A quartic minimum obstruction has a proper five-colouring with at most two defects, and at most one if it contains two triangles sharing an edge. |
| Neutral Kempe flexibility | On a quartic graph a fixed pair of hues gives linear equations over $\mathbb F_2$ in switches of its induced components. The summed dimensions preserving the exact defect set are at least $n-6d$ for $d$ defects. If this exceeds ten, some neutral simultaneous swap exceeds a global renaming. |
| Dominating-set sufficient condition | A reserved-colour proof works for an independent set of degree-at-most-three vertices such that every nonisolated exterior vertex has a neighbour in the set and exactly one neighbour on one side of the partition. The proof uses Brooks' theorem after adding selected pair edges. |
| Order bound (second session) | No counterexample has at most 14 vertices. The minimum-obstruction reductions restrict each order to the filtered strata, and exhaustive labelled covers at orders 13 and 14 were coloured and independently verified. Finite computation, see the census tables below. |
| Splitting lemma (second session) | Refining a proper colouring never destroys a singleton. A PCF $(4+j)$-colouring may therefore be sought by splitting $j$ classes of a proper four-colouring, subject to $\mathbb F_2$-linear conditions at the defects. |

$K_{2,2,2}$ needs five colours. Two five-cycles sharing a vertex also need five, and already have pathwidth at most two and maximum degree four. The known five-colour adjacent-vertex-distinguishing edge-colouring theorem gives PCF five-colourability of line graphs of simple subcubic graphs.

### Verification receipts

| Check | Exact successful scope |
| --- | --- |
| [Cut permutations](check_03_cut_permutations.js) | 390,625 matching state pairs, 170,565 required matching pairs, 45,800 star-and-edge pairs, 10,000 crossing-path pairs, 5,000 universal-terminal cases. |
| [Pathwidth closure](check_03_pathwidth_three.js) | 5,145 states, 17,812 transitions, 2,392 terminal states, largest signature set 793. |
| [Treewidth closure](check_03_treewidth_three.js) | 1,540 processed states, 1,539 live representatives, 78 three-boundary additions, 1,469 bag additions, 10,669 facet joins, 215 same-boundary joins, 9,442 pivot projections, 4,129 terminal tests. The saved readable checker and the independently run scratch implementation agreed on the counts. The scratch implementation is in [pcf-tw3-language.js](03-handoff/pcf-tw3-language.js). |
| [One-hole obstruction](check_03_one_hole_barrier.js) | Explicit 45-vertex triangle-free quartic graph, all 990 pair deletions connected, 30 closed one-hole states, 60 transitions, and a verified full PCF five-colouring. |
| [Rust census port](03-handoff/pcf-census-rs/src/main.rs) | Brute-force generator cross-check at orders 5 and 6 and example checks. Order totals 1, 8, 75, 666, 6,975, 77,937, 943,509 and 12,148,600 for orders 5 to 12, equal to the JavaScript run. Order 13 strata: 79,484, 10,760,307, 55,989,317, 34,710,163 and 1,934,746, each graph with a verified colouring. |
| [Lovász-partition barrier](03-handoff/pcf-lovasz-partition.py) | Exhaustive check of an 8-vertex $K_4$-free quartic graph: 10 admissible (1,2)-partitions, 6 compatible, the unique $\Phi$-minimiser incompatible, graph PCF 5-colourable. |

## Census and repair experiments

The ordinary [census](check_03_conflict_free_colouring.js) covered all connected $K_4$-free graphs with minimum degree three and maximum degree four through order 12. It uses a prefix-normalized labelled cover, with possible isomorphic repetitions, and independently checks a colouring witness for each representative. Brute-force labelled edge-subset enumeration cross-checks both generator modes at orders five and six. The complete count is 13,177,771, including 12,148,600 at order 12. Together with the low-degree and clique reductions this excludes an obstruction of order at most 12.

| Order 13 filtered quartic count | Status after the second session |
| --- | --- |
| 5 | 79,484 complete, all with a verified colouring. Reproduced by both implementations. |
| 7 | 10,760,307 complete, all with a verified colouring. Reproduced by both implementations. |
| 9 | 55,989,317 complete, all with a verified colouring (Rust port). |
| 11 | 34,710,163 complete, all with a verified colouring (Rust port). |
| 13 | 1,934,746 complete, all with a verified colouring (Rust port). |

Degree parity and the cubic-induced matching reduction exclude the other order-13 quartic counts in a minimum obstruction. **Order 13 is therefore closed: there is no counterexample on at most 13 vertices.** The proof and the trust base are in the main note under Finite census. The [Rust port](03-handoff/pcf-census-rs/src/main.rs) is a line-by-line translation of the JavaScript generator, search and verifier. It repeats the brute-force generator cross-check at orders five and six and reproduced every earlier count exactly, including all order totals from 5 to 12.

| Order 14 filtered quartic count | Status |
| --- | --- |
| 6 | 5,257,511 complete, all verified. |
| 8 | 221,324,586 complete, all verified. |
| 10 | 805,003,145 complete, all verified (140 minutes). |
| 12 | 426,412,767 complete, all verified. |
| 14 | 21,840,153 complete, all verified. |

At order 14, parity forces $n_4$ even and $n_3\le2n_4$ forces $n_4\ge5$, so these five strata are all. **Order 14 is therefore closed as well: there is no counterexample on at most 14 vertices.** The order-14 total is 1,479,838,162 labelled representatives. Separately, the 4-regular order-15 stratum (262,844,731 representatives) was completed with verified colourings. That stratum alone does not close order 15, whose remaining strata $n_4\in\{5,7,9,11,13\}$ are estimated at well over ten billion representatives.

The exact reconfiguration experiment [pcf-kempe-census.js](03-handoff/pcf-kempe-census.js) enumerated every proper five-colouring up to palette permutation with at most two defective vertices on the quartic labelled cover. Its move swaps any subset of connected components induced by one colour pair. It traverses from all PCF colourings, separately allowing at most one and at most two defects. Moves are reversible. Each tested state reached a full colouring in at most two moves at its tested cap.

| Order | Quartic representatives | One-defect states | Two-defect states |
| --- | ---: | ---: | ---: |
| 6 | 1 | 0 | 3 |
| 7 | 6 | 21 | 21 |
| 8 | 33 | 1,028 | 575 |
| 9 | 245 | 22,323 | 12,514 |
| 10 | 2,027 | 553,725 | 388,414 |
| **Total** | **2,312** | **577,097** | **401,527** |

A separate sample of 94,231 triangle-free twin-free quartic instances passed every recorded one-defect two-step test. The 240 sampled states with no immediate improvement all repaired after one neutral swap and one strict swap. Two sampled two-defect states without immediate improvement also improved in two steps. These are samples, whereas the preceding table is exhaustive for its stated finite cover.

## Barriers and routes tried

- **One-hole recolouring.** The 45-vertex graph in the main note has a closed set even when the moved hole may go anywhere. The graph itself is five-colourable. This rules out a universal argument using only these moves on arbitrary one-hole states. The closure example and certificate are persistent. A smaller reconfiguration census and the construction search are in [pcf-hole-reconfiguration.js](03-handoff/pcf-hole-reconfiguration.js) and [pcf-45-closed-hole.js](03-handoff/pcf-45-closed-hole.js).
- **Simultaneous Kempe swaps.** The note gives a 12-vertex triangle-free twin-free 3-connected quartic example with one defect that no single simultaneous swap repairs. It has a two-step repair shifting the defect once. The rank bound guarantees some neutral motion at sufficiently large order, but allows that motion to be remote from the defect. A general repair theorem or a counterexample to the two-step bound is still needed. **Second session:** the exhaustive order-11 run (18,577 quartic representatives, 15,358,623 one-defect and 12,086,773 two-defect states) found every state Kempe-connected to a PCF colouring, but with maximal distance three. An explicit witness that needs three moves is in the note and [pcf-kempe-distance3.py](03-handoff/pcf-kempe-distance3.py). The Rust port is `pcf-kempe` in the census crate.
- **Four-terminal cuts.** The two-side abstract palette problem has incompatible signature families even after the tested small caps. Such abstract families have no verified realizing fragments. Among 1,152 sampled small quartic fragments, all met a sufficient condition and 19,680 tests on the most constrained interfaces glued successfully. Scripts beginning `pcf-four-` and [pcf-fragment-gluing.js](03-handoff/pcf-fragment-gluing.js) preserve the experiments. Repeated terminals are outside the matching four-cut proof.
- **Near-$K_5$ forcing.** A standalone fragment with two spare-degree ports cannot force equality in a minimum obstruction, because adding the port edge gives a proper interior colouring with different port colours. $K_5$ minus two disjoint edges has four flexible ports for arbitrary exterior colours, as shown in the note. A useful forcing construction needs conditional exterior constraints or more connectivity.
- **Bipartite private palettes.** The Fano-complement incidence graph requires at least four colours on each shore, so two private colours per shore plus one shared hue cannot work universally. One private hue per shore and three shared hues remains plausible. Exhaustive tested shore sizes four through seven and 1,800 larger sampled graphs passed that stronger restriction. Use [pcf-bipartite-private.js](03-handoff/pcf-bipartite-private.js) and [pcf-fano-complement.js](03-handoff/pcf-fano-complement.js).
- **Characteristic-two product.** Affinely independent palette labels turn a quartic's singleton condition into a nonzero neighbour sum. The raw product can vanish modulo $(x_v^5)$ even on $K_{4,4}$. Deduplicating the factors succeeds across the tested 2,312 quartic representatives through order 10. General nonvanishing remains unproved. See the two `pcf-linear-polynomial` scripts.
- **Quadratic factors in odd characteristic.** $(x_i-x_j)(x_i+x_j-x_k-x_l)$ vanishes on every bad quartic tuple. Choosing and combining these factors introduces free coefficients. The balanced coefficient was nonzero modulo 251 on $K_5$, $K_{4,4}$, $K_{2,2,2}$ and four sampled quartic graphs through order 12. A universal proof would imply fixed five-list PCF colourability. The formula and the precise role of Sidon palette labels are in the note.
- **Colour refinement barriers.** The $3\times3$ rook graph cannot obtain PCF five-colouring by splitting one class of a proper four-colouring. Acyclic and PCF simultaneously require six colours on $K_{4,4}$. The explicit checks and proofs are in the note and [pcf-split-replay.js](03-handoff/pcf-split-replay.js).
- **Brooks and domination.** The unrestricted independent-set variant fails as an argument because a chosen unequal neighbour pair at a quartic centre can still leave a $2+2$ pattern. The proved version restricts the reserved set to degree at most three.
- **Structured counterexample search.** No counterexample appeared among 7,200 sampled regular, mixed and switched octahedron-chain candidates, or 6,660 sampled subdivision-port octahedron and cycle-ring candidates. [pcf-random-csp.js](03-handoff/pcf-random-csp.js), [pcf-ring-gadgets.js](03-handoff/pcf-ring-gadgets.js) and the `pcf-hardest-*.json` datasets preserve this work. These samples do not bound the unrestricted order.
- **Parity covers (second session).** On 4-regular graphs PCF equals odd colouring. A set $S$ meeting every open neighbourhood oddly, with $G[S]$ bipartite and $G-S$ 3-colourable, gives a PCF 5-colouring with palettes $\{4,5\}$ and $\{1,2,3\}$. Such $S$ cannot exist for odd $n$, by counting, and does not exist for $K_{2,2,2}$. The closed-neighbourhood system $(A+I)z=\mathbf 1$ is always solved by $S=V$ on 4-regular graphs, so Sutner's existence theorem gives nothing useful there.
- **Lovász partitions (second session).** Minimise $2e(V_1)+e(V_2)$ and colour $V_1$ from two colours and $V_2$ from three. An explicit 8-vertex $K_4$-free quartic graph has a unique minimiser with no compatible PCF colouring. See [pcf-lovasz-partition.py](03-handoff/pcf-lovasz-partition.py).
- **Static witness schemes (second session).** Fixing a free neighbour $f(w)$ and demanding that $N(w)\setminus f(w)$ be rainbow gives an auxiliary graph with exactly $5n$ edges on every quartic graph of girth at least five. It is never 5-degenerate, so such schemes cannot even certify six colours greedily.
- **Reverse-BFS greedy (second session).** With layers coloured from the deepest, a non-root vertex has at most $2|E(y)|+1$ forbidden colours, and six or more occur only at critical vertices or at the vertex completing the root. With soft rainbow preferences, [pcf-bfs-greedy.py](03-handoff/pcf-bfs-greedy.py) failed on 345 of 1,000 random quartic graphs with five colours. With six colours it failed on 1, 1, 1, 1 and 2 of 1,000 for seeds 1 to 5, at critical, root and root-completing vertices. It is not a proof route as it stands.
- **Six colours by splitting two classes (second session).** A PCF 6-colouring refining a proper four-colouring existed for all 100 sampled random quartic graphs. About 89% of the sampled four-colourings were splittable, by [pcf-two-class-split.py](03-handoff/pcf-two-class-split.py). The general statement is unproved.
- **Kashima–Škrekovski–Xu cycle reduction at six colours (second session).** Quartic cycle vertices keep lists of size two, and the abstract two-list cycle problem with blocked outside pairs is often unsolvable. An explicit 5-cycle instance is in the note, and sampling with [pcf-cycle-two-lists.py](03-handoff/pcf-cycle-two-lists.py) finds unsolvable instances of both parities. Realisability or recolouring outside the cycle would be needed.

## Restart commands

From this shortlist directory, with Node.js 24 or compatible:

```powershell
node .\check_03_cut_permutations.js
node .\check_03_one_hole_barrier.js
node .\check_03_pathwidth_three.js
node .\check_03_treewidth_three.js
node .\check_03_conflict_free_colouring.js 5 12
node .\check_03_conflict_free_colouring.js 13 13 --cubic-matching 9 11 13
python .\03-handoff\pcf-lovasz-partition.py
python .\03-handoff\pcf-bfs-greedy.py 1 1000 6 quartic
python .\03-handoff\pcf-two-class-split.py 1 100
python .\03-handoff\pcf-cycle-two-lists.py 1 200000
node .\03-handoff\pcf-kempe-census.js .\check_03_conflict_free_colouring.js 6 10
node .\03-handoff\pcf-kempe-census.js .\check_03_conflict_free_colouring.js 11 11
```

The Rust census port needs only a stable Rust toolchain (`rustc` 1.99 was used). Build outside the repository and run the strata separately in parallel:

```powershell
$env:CARGO_TARGET_DIR = "$env:TEMP\pcf-census-target"
cargo build --release --manifest-path .\03-handoff\pcf-census-rs\Cargo.toml
& "$env:CARGO_TARGET_DIR\release\pcf-census.exe" 5 12
& "$env:CARGO_TARGET_DIR\release\pcf-census.exe" 13 13 --cubic-matching 5 7 9 11 13
& "$env:CARGO_TARGET_DIR\release\pcf-census.exe" 14 14 --cubic-matching 6 8 10 12 14
& "$env:CARGO_TARGET_DIR\release\pcf-census.exe" 15 15 --cubic-matching 15
& "$env:CARGO_TARGET_DIR\release\pcf-kempe.exe" 6 11
python .\03-handoff\pcf-kempe-distance3.py
```

On the four-core machine used, order 12 took 96 seconds, the order-13 strata took between 19 seconds and 6.5 minutes each, and each process verifies about 10 million representatives in 2 to 4 minutes when four run together.

The treewidth checker is the complete unbounded-order result for that class. The exact reconfiguration search at order 11 is complete and took 27 minutes. Order 12 has 183,257 quartic representatives and would take many hours. The order-13 and order-14 strata are complete. Order 15 would need its remaining odd strata, estimated at tens of hours on this machine. Earlier experimental scripts in [03-handoff](03-handoff) are unchanged scratch copies and some refer to temporary paths or the original working directory. Their headers show the original arguments. The principal restart commands above refer to the durable checkers directly.

For an unrestricted proof, the strongest open route from this work is to repair the one- or two-defect proper five-colourings obtained by vertex minimality. Start with the exact linear constraint system for a selected pair and test whether a neutral switch can release a second pair that sees the defect. Two-defect states from the construction have the defects close to the removed vertex, giving a more targeted family than arbitrary low-defect states. A different route is to prove that every fragment on a small separator admits enough exterior patterns for gluing, beyond the matching four-edge conditions already proved. Neither route currently supplies an unrestricted proof.

**Second-session assessment and recommended next steps.** None of the global schemes tried in the second session (parity covers, Lovász partitions, static witnesses, reverse-BFS greedy) can work unchanged, and each failure is recorded with an explicit instance or counting argument. Two directions remain worth effort. (1) A PCF 6-colouring theorem for all graphs of maximum degree at most four would improve the published bound of seven. It is implied by the open $(\mathrm{degree}+2)$-choosability question of Kashima–Škrekovski–Xu. In locally tree-like regions the soft-rainbow accounting leaves exactly one spare colour with six colours. A proof needs dynamic control of the rare critical-vertex and root failures, for example a local recolouring step at a critical vertex, or the splitting lemma applied to two classes of a Brooks four-colouring with a bipartite constraint graph. (2) For the five-colour conjecture itself, the defect-repair route of the first session remains the most concrete. The order bound is now 15, and the order-11 Kempe census shows that a repair lemma must allow at least three moves. Both are evidence only and not a substitute for a proof.
