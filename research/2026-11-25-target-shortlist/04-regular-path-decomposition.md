# Favaron–Genest–Kouider path decomposition

The exact conjecture and its unrestricted degree-five case remain open in the sources checked on 2026-11-25. This note gives a reduction to one defective trail shape in degree five, a sufficient condition for simultaneous repairs, an obstruction to a two-trail repair, and a bounded exact-cover check.

The [separate negative answer to Problem 5](04b-regular-path-center-counterexample.md) rules out a representative strategy even for 2-edge-connected graphs. It proves that the middle edges cannot always be required to form a perfect matching. The degree-five witness admits an unrestricted path decomposition.

**Update.** The sufficient condition below is superseded by [the matching-relative theorem](04d-regular-path-matching-relative-theorem.md). That note proves that a perfect matching with no \(M\)-triangle sharing an edge with an \(M\)-square suffices. This hypothesis drops hypothesis 1 of the parallel-repair condition below, and the result contains the FGK, Botler–Mota–Wakabayashi and Chu–Fan–Hong–Zhou degree-five theorems. That note also reduces the diamond-free case to a single configuration.

[Separate constructions for Problems 3 and 6](04c-regular-path-problems-3-and-6.md) give path decompositions without perfect matchings, and non-rainbow decompositions whose middle edges form perfect matchings, in every odd degree those questions request.

## Source and eligibility

Conjecture 1 asks whether every finite simple odd \(d\)-regular graph with a perfect matching has an edge partition into simple paths of exactly \(d\) edges. In the notation \(d=2k+1\), it asks for all \(k\ge 1\). Kotzig settled \(k=1\). The conjecture allows the middle edges of the paths to differ from the given perfect matching. The original paper gives counterexamples to the stronger claim that each prescribed matching can serve as the set of middle edges. [Favaron, Genest and Kouider, J. Graph Theory 63 (2010), 114–128](https://doi.org/10.1002/jgt.20413) · [full text](https://www.academia.edu/25437460/Regular_path_decompositions_of_odd_regular_graphs)

- Favaron, Genest and Kouider give sufficient conditions on pairs of short cycles containing exactly one edge of a prescribed matching. In particular, Theorem 6 implies that every perfect matching extends to a degree-five path decomposition if no 4-cycle shares an edge with a triangle or another 4-cycle. Two matched triangles cannot form a bad pair. [Theorems 6–7](https://doi.org/10.1002/jgt.20413)
- Botler, Mota and Wakabayashi proved the degree-five triangle-free case. Botler, Mota, Oshiro and Wakabayashi proved the matched \((2k+1)\)-regular case for girth at least \(2k\). [2015 article](https://doi.org/10.1016/j.disc.2015.04.018) · [2017 article](https://doi.org/10.1016/j.ejc.2017.06.011)
- Botler and Hoffmann proved the case containing the \(k\)-th power of a spanning cycle, and additional degree-five cases containing certain 4-regular Cayley spanning subgraphs. [2022 article](https://doi.org/10.1016/j.disc.2022.112906)
- Chu, Fan, Hong and Zhou proved the degree-five case when no triangle shares an edge with a 4-cycle. Their theorem allows both kinds of cycle. The unresolved degree-five target includes graphs with overlapping triangles and 4-cycles. [Theorem 2.2, Scientia Sinica Mathematica 54 (2024), 1787–1794](https://www.sciengine.com/cfs/files/pdfs/view/1674-7216/9A038B7537554B7284033EDD2D967FFB.pdf)
- Montgomery, Müyesser, Pokrovskiy and Sudakov still treat Favaron–Genest–Kouider as conjectural. Their 2025 theorem leaves at most \(\varepsilon nd\) edges uncovered by paths of length \(\lceil(1-\varepsilon)d\rceil\) when \(d\) is sufficiently large. Chu and Wang's 2026 paper bounds the number of paths, allowing lengths to vary, in Eulerian graphs with sufficiently separated triangles. Fernandes, Naia, Santos and Stein's 2025 tree-packing result uses complete bipartite hosts. The Barát–Thomassen theorem uses a high edge-connectivity threshold, and the specialized five-edge-path result gives 48 even for bipartite hosts. [Approximate decomposition](https://doi.org/10.1112/jlms.70269) · [Eulerian decomposition](https://arxiv.org/abs/2510.12806) · [Bipartite tree packing](https://doi.org/10.1016/j.disc.2025.114641) · [Five-edge-path connectivity theorem](https://arxiv.org/abs/1505.04309)

The web checks included author names and spelling variants, Conjecture 1, DOI aliases, five-edge path decomposition, Kotzig, and newer papers on regular graph and tree decomposition. Local searches of both permanent branches and the remote catalogue and tracker found no matching result. Targeted Mathlib, Isabelle AFP and graph-conjecture catalogue searches found no formal resolution. Mathlib's paths and matchings modules supply relevant primitives. [West's problems list](https://dwest.web.illinois.edu/openp/) · [Mathlib paths](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Paths.html) · [Mathlib matching](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/SimpleGraph/Matching.html)

## Trail reduction

Every finite simple 5-regular graph \(G\) with a perfect matching \(M\) has an edge partition into simple five-edge paths and five-edge trails consisting of a 4-cycle with a pendant edge. The middle edges of these trails are the edges of \(M\), and each vertex occurs as a terminal of exactly one trail.

Let \(H=G-M\). For every vertex \(v\), partition the four incident \(H\)-edges into two pairs. Whenever neighbors \(x,y\) of \(v\) in \(H\) satisfy \(xy\in M\), put \(vx,vy\) in the same pair. All prescribed pairs at \(v\) are disjoint because \(M\) is a matching, so the partition exists even when two pairs are prescribed. Split \(v\) into one vertex per pair and orient each cycle of the resulting 2-regular graph cyclically. Identifying the split vertices gives an Eulerian orientation of \(H\) with oppositely directed edges at each prescribed pair.

Factor this orientation into two directed spanning cycle covers by applying Hall's theorem to the 2-regular bipartite graph of outgoing and incoming vertex copies. Reverse the second cover and let \(r,s\) denote the successor permutations in the first and reversed second covers, respectively. For each \(uv\in M\) take the trail

\[
s(r(u)),\,r(u),\,u,\,v,\,r(v),\,s(r(v)).
\]

The middle edges use \(M\) once, the adjacent edges use each \(r\)-edge once, and the terminal edges use each \(s\)-edge once because \(r\) is a permutation. The map \(s\circ r\) is a permutation, so the terminals occur once each.

Injectivity excludes collisions at the same distance from the middle edge. A repetition within one arm would require a loop or a common edge of the two factors. Between arms the remaining equalities are \(s(r(u))=v\), \(s(r(v))=u\), \(s(r(u))=r(v)\), and \(s(r(v))=r(u)\). The first two would traverse a matched triangle. For the first equality, \(ur(u)\), \(r(u)v\) were a prescribed pair at \(r(u)\). The equality after reversing the second cover would mean both edges pointed into \(r(u)\) before the reversal, which contradicts the prescribed pairing. The second equality is symmetric. The last two equalities each give a 4-cycle with a pendant edge. They cannot both hold because \(s\) cannot direct an undirected edge both ways.

The factor-based construction comes from Favaron–Genest–Kouider, Proposition 2 and Theorem 2. The proof extracts the triangle-elimination step of Chu–Fan–Hong–Zhou, Lemma 2.1, using the matching to pair the incident edges for all matched triangles even when two occur at one vertex. This removes the short-cycle intersection hypothesis from the initial step. [Original factor construction](https://doi.org/10.1002/jgt.20413) · [Triangle elimination](https://www.sciengine.com/cfs/files/pdfs/view/1674-7216/9A038B7537554B7284033EDD2D967FFB.pdf)

## A sufficient condition for parallel repairs

For a chosen perfect matching \(M\), call a triangle or square an \(M\)-triangle or \(M\)-square if it contains exactly one edge of \(M\). Let \(U\) be the union of the endpoints of the matching edges in all \(M\)-squares. Suppose that

1. no edge of \(G-M\) joins two vertices of \(U\), and
2. no \(M\)-triangle shares an edge with any \(M\)-square.

Then \(G\) has a five-edge path decomposition. The second hypothesis permits an overlap if either cycle uses zero or two matching edges.

Apply the trail reduction. Write a defective trail as \(T=(a,b,c,d,e,b)\), where \(cd\in M\), \(r(c)=b\), \(r(d)=e\), \(s(b)=a\), and \(s(e)=b\). Put \(f=r^{-1}(c)\), write \(fg\in M\), and set \(x=s(c)\), \(h=r(g)\), \(y=s(h)\). Since \(c\in U\) and \(fc\notin M\), hypothesis 1 gives \(f\notin U\). Thus \(Q=(x,c,f,g,h,y)\) is a simple path in the initial decomposition. Exchange \(bc\) and \(cx\) between \(T\) and \(Q\), making

\[
T'=(a,b,e,d,c,x),\qquad Q'=(b,c,f,g,h,y).
\]

The vertex \(x\) differs from \(a,b\) by injectivity of \(s\), from \(c\) by simplicity, and from \(d\) because \(cd\in M\). If \(x=e\), the \(M\)-triangle \(cde\) shares an edge with the \(M\)-square of \(T\), which hypothesis 2 excludes. For \(Q'\), \(b\ne c\), \(b\ne f\) because \(r\) has no 2-cycle, and \(b\ne h\) because \(r(c)=b\) and \(g\ne c\). Indeed, \(g=c\) would force \(f=d\) by the matching, contrary to \(f\notin U\). If \(b=y\), injectivity of \(s\) gives \(h=e\), hence \(g=d\) and \(f=c\), impossible. If \(b=g\), the \(M\)-triangle \(bcf\) shares \(bc\) with the \(M\)-square, also excluded.

Apply the exchanges simultaneously. Distinct defective trails have distinct vertices \(c\) because those vertices belong to their disjoint middle edges. A receiving path can receive at most one exchange at each of its two internal vertices adjacent to a terminal. Each exchange replaces the corresponding terminal, and the collision check ensures the replacement avoids the four retained internal vertices. If both terminals are replaced, the replacements differ because they were terminals of distinct defective trails in the initial partition. Every exchanged edge still occurs exactly once. The exchange is the \(\alpha\)-operation of Chu–Fan–Hong–Zhou. The matching-relative hypotheses here allow all repairs to use simple receiving paths. [Chu–Fan–Hong–Zhou, Section 2](https://www.sciengine.com/cfs/files/pdfs/view/1674-7216/9A038B7537554B7284033EDD2D967FFB.pdf)

### Example with overlapping triangles and squares

Take 68 indexed copies of \(u,v,a,b,c,d\), with indices modulo 68. Give each copy residual edges \(ua,vb,vc,ab,ac,bc\) and matching edge \(uv\). For every index \(j\), add the following undirected residual edges. The first letter belongs to copy \(j\), and the second belongs to copy \(j+\text{shift}\).

| Types | Shift |
|---|---:|
| \(u,a\) | 6 |
| \(u,b\) | 8 |
| \(u,d\) | 9 |
| \(v,c\) | 10 |
| \(v,d\) | 11 |
| \(d,d\) | 7 |

Complete the matching by matching each remaining vertex to the same letter 34 copies away. The residual degree is four at every vertex. The residual graph is connected because the \(d,d\) edges cycle through all copies and the remaining types connect to a \(d\) vertex. The graph and the matching are simple.

Any \(M\)-triangle or \(M\)-square would have a residual path of length two or three between the endpoints of its matching edge. The total absolute shift is at most 33 along such a path, so it cannot use a matching edge of shift 34. A path joining the endpoints of an in-copy matching edge must have net shift zero. A sum of at most three moves of sizes between 6 and 11, with signs, can be zero only when two moves of equal size cancel. The two cancelling moves use the same type pair in reverse, since each nonzero shift size belongs to only one type pair. With at most one intervening in-copy edge, this is impossible in a simple path. Consecutive cancelling moves revisit the same vertex, and an intervening in-copy edge would have to be a loop. Therefore all the short residual partners of an \(M\)-edge stay in its copy.

The only \(M\)-squares in each copy are \(uabvu\) and \(uacvu\). There is no \(M\)-triangle, so \(U\) consists of the copies of \(u,v\) and spans no residual edge. The residual triangle \(abc\) shares edges with the two squares, so the Chu–Fan–Hong–Zhou hypothesis fails. The displayed matching has a bad pair in each copy in the sense of Favaron–Genest–Kouider. The two \(M\)-squares share \(ua\) and their residual union has degree three at \(a\). Its bad-pair graph consists of 68 disjoint edges, so it satisfies neither the empty nor the star condition. This example separates the new sufficient condition from those hypotheses for the displayed matching.

## A two-trail repair obstruction

Consider \(T=(a,b,c,d,e,b)\) and \(Q=(e,c,f,g,h,i)\) on nine distinct named vertices. Their union has no partition into two five-edge paths. A five-edge path using \(hi\) must follow the four-edge chain \(i,h,g,f,c\) because \(i\) has degree one and the three internal chain vertices have degree two in this union.

| Final edge | Shape of the five unused edges |
|---|---|
| \(cb\) | Triangle \(cde\) with the two-edge chain \(e,b,a\) attached at \(e\) |
| \(cd\) | Triangle \(bce\) with pendant edges \(ba\) and \(ed\) |
| \(ce\) | The original square and pendant edge \(T\) |

The configuration occurs within an initial trail partition of a simple 5-regular graph. Take ten indexed copies of the nine labels, with indices modulo 10. Within each copy prescribe matching edges \(cd,fg\), first-factor arcs \(c\to b,d\to e,f\to c,g\to h\), and second-factor arcs \(b\to a,e\to b,c\to e,h\to i\). In each factor separately, list in alphabetical order the labels missing an outgoing arc and the labels missing an incoming arc. Pair the lists in order. Add the paired arcs from copy \(j\) to copy \(j+1\) in the first factor and \(j+3\) in the second. Match the remaining labels to the same label in copy \(j+5\), taking each unordered matching edge once. The three intercopy edge types have distinct absolute shifts modulo 10. The resulting graph is simple with the required factors and matching. A directed two-edge arm changes the copy index by \(0,1,3\), or \(4\). It can reach a matched neighbor only if both moves stay in the initial copy, where the prescribed arcs introduce no such triangle closure. The gluing produces \(T,Q\) at every copy. A rule using only the two trails of this exchange therefore cannot handle all configurations.

## Exact-cover check

Run [check_regular_path_decomposition.py](check_regular_path_decomposition.py) with Python 3.12. The default run considers all simple 5-regular graphs of orders 6, 8 and 10. The generator builds their \((n-6)\)-regular complements by choosing counts of neighbors among unprocessed vertices with identical adjacency to the previously processed vertices. Every isomorphism class survives, since those vertices can be permuted before choosing the next row. A full adjacency-preserving bijection search within invariance buckets removes repeated classes. [Meringer's independent order counts](https://mathe2.uni-bayreuth.de/markus/reggraphs.html)

For each graph with a perfect matching, exact cover uses one column per edge and one column per terminal vertex. Each vertex has odd degree, so it must be an endpoint at least once. The \(n/2\) paths have exactly \(n\) endpoints in total, giving the terminal condition. Each candidate row uses six distinct vertices along existing edges, up to reversal. A separate verification pass checks the matching, six distinct vertices per path, exact edge coverage, and the terminal counts.

| Order | Isomorphism classes | With a perfect matching | Triangle and square share an edge | Verified decompositions |
|---:|---:|---:|---:|---:|
| 6 | 1 | 1 | 1 | 1 |
| 8 | 3 | 3 | 3 | 3 |
| 10 | 60 | 60 | 59 | 60 |

The run with arguments **--orders 12 14 --sample 60** verifies 52 graphs of order 12 and 51 graphs of order 14 after removing duplicate labeled samples. Each has a triangle and a square sharing an edge. This sampling starts with the square of a cycle and adds a planted perfect matching, then applies selected degree-preserving switches outside the matching. The samples may include distinct labelings of isomorphic graphs.

The unrestricted overlapping case remains open. A broader repair argument must handle interactions with additional trails, or choose an initial partition that avoids the two-trail obstruction.

## Further repair and cut reductions

### Orienting a fixed pair of 2-factors

For fixed ordered 2-factors \(R,S\) of \(G-M\), the search over their cyclic orientations for a square- and triangle-free gluing is a 2-SAT instance. Use one Boolean variable per cycle of each factor. For \(uv\in M\), the successors \(r(u),r(v)\) are distinct for every orientation of \(R\). The square collision is equivalent to adjacency of those successors in the undirected factor \(S\). Either orientation of that \(S\)-edge makes one of the two arms end at the other arm's intermediate vertex. Forbid each combination of the at most two \(R\)-cycle signs that gives such adjacency. For the triangle collisions, \(s(r(u))=v\) depends on the sign of one \(R\)-cycle and one \(S\)-cycle after a choice of \(r(u)\); forbid each offending combination, and do the same for \(v\). This gives constantly many clauses per matching edge. Repeated variables reduce a clause to a unit condition or a tautology. Satisfiability characterizes the orientations for the fixed factors. The original matching-center obstruction still applies when the factors are allowed to vary. [Favaron–Genest–Kouider, Theorem 2 and Section 4](https://doi.org/10.1002/jgt.20413)

### A three-trail repair through a matched triangle

Use the trail reduction's matching and ordered factor permutations \(r,s\). Let \(T=(a,b,c,d,e,b)\) be defective, and suppose the connector's companion is \(Q=(e,c,f,g,h,y)\) with \(b\ne g\). Here the blue arc \(c\to e\) is present, so the simple two-trail exchange at \(c\) would create a collision at \(e\). The triangle \(cde\) shares edges with the square of \(T\).

Let \(D=(z,d,i,j,k,\ell)\) be the original trail with \(d\) as its first vertex adjacent to a terminal, so \(i=r^{-1}(d)\) and \(z=s(d)\). If \(h=d\), then \(D\) is \(Q\) in reverse, and partition the edges of \(T,Q\) into

\[
(a,b,e,c,d,y), \qquad (b,c,f,g,d,e).
\]

If \(h\ne d\) and \(j\ne e\), replace \(T,Q,D\) by

\[
(a,b,e,c,d,z),\qquad (b,c,f,g,h,y),\qquad (e,d,i,j,k,\ell).
\]

The first path is simple. The value \(s(d)\) differs from \(a,b,e\) by injectivity since these are \(s(b),s(e),s(c)\). It differs from \(c,d\) by the matching edge \(cd\) and simplicity. This also proves simplicity for the first path in the case \(h=d\).

In the second piece, \(b\ne f\) because a red 2-cycle would result, \(b\ne h\) by red injectivity, and \(b\ne y\) by blue followed by red injectivity. The hypotheses give \(b\ne g\). If \(h=d\), appending \(e\) after \(d\) makes a simple path because \(f\ne e\) by disjointness of the red and blue edges on \(ce\), and \(g\ne e\) because the original trails contain no triangle. If \(h\ne d\), the second piece is simple unless \(y=c\), in which case it retains the original square of \(Q\).

In the third piece, \(e\ne i\) because \(r(d)=e\) precludes a red 2-cycle, and \(e\ne k\) because \(r(j)=e\) would give \(j=d\), hence \(i=c\), contrary to \(r(c)=b\). If \(e=\ell\), then \(k=c\) since \(s(c)=e\), so \(j=f\), \(i=g\), and \(h=d\). This contradicts the case under consideration. Thus the third piece is simple unless \(\ell=d\), in which case it retains the original square of \(D\). In either case the replacements preserve the edge partition and strictly decrease the square-trail count. All blue arcs continue to have tails of degree at least two in their assigned pieces. This preserves the directed-edge condition used in the triangle-free disentangling method. The companion positions in this argument still rely on the original factor construction. [Botler–Mota–Wakabayashi, Sections 3–5](https://doi.org/10.1016/j.disc.2015.04.018)

### Cycles of original defective trails

Let \(T_i=(a_i,b_i,c_i,d_i,e_i,b_i)\) be distinct defective trails of the original factor construction, indexed cyclically. Link each to the original trail using \(c_i\) as a vertex adjacent to a terminal. If the links form a cycle among the \(T_i\), every link has the form \(c_i=b_{i+1}\) or \(c_i=e_{i+1}\). A cycle all of whose links use the same form can be replaced entirely by simple five-edge paths, allowing triangles. The replacements preserve the condition that the tail of each blue arc is internal to its containing path.

For a cycle with \(c_i=b_{i+1}\) throughout, use

\[
(a_i,b_i,e_i,d_i,c_i,c_{i+1})
\]

at each index. A cycle of length two would repeat a red edge in reverse, so its length is at least three. The new terminal \(c_{i+1}=b_{i+2}\) already has degree three in \(T_{i+2}\) and two in \(T_{i+1}\), forcing it outside \(T_i\). The discarded edge \(b_i c_i\) at each index is the appended edge at the preceding index. This is the endpoint rotation of Botler–Mota–Wakabayashi, with the degree-five condition excluding vertex repetitions in this setting. [Lemma 4.2](https://doi.org/10.1016/j.disc.2015.04.018)

For a cycle with \(c_i=e_{i+1}\) throughout, the \(b_i\) are pairwise distinct, and no \(b_i\) equals any \(c_j\). In fact the sets of red heads \(\{b_i\}\) and \(\{e_i\}=\{c_i\}\) are disjoint. Each adjacent pair has the replacement

\[
(a_i,b_i,e_i,d_i,c_i,b_{i+1}),
\qquad
(a_{i+1},b_{i+1},c_{i+1},d_{i+1},c_i,b_i).
\]

The new terminals avoid the old terminals by terminal uniqueness, and avoid all \(c_j,e_j\) by the red-head observation. Also \(b_{i+1}\ne d_i\), since otherwise the blue edge \(c_i b_{i+1}\) would be the matching edge \(c_i d_i\). Likewise \(b_i\ne d_{i+1}\), since otherwise a red edge would be used in reverse. The exchange covers the same edges and leaves blue tails internal. Pairing successive indices handles even cycles. The same pair repair works at a link \(c_i=e_{i+1}\) in a mixed cycle of length at least three. Here \(c_{i+1}\) is either \(b_{i+2}\) or \(e_{i+2}\), and neither can equal \(b_i\).

For a pure cycle of odd length, a finite role-identification check handles the needed triples. The matching vertices \(c_i,d_i\) are distinct. The index restrictions on \(d_i\) are \(d_i\ne b_{i-1},b_i,b_{i+1}\), by red edges, distinct vertices in \(T_i\), and blue edges, respectively. The terminal \(a_i\) is distinct from the other terminals and from \(c_i,d_i,e_i\). In a block of three consecutive trails, the only possible identifications of a \(d\)-label with a \(b\)-label are between the first and third positions when the cycle length is at least five. Assign \(a_i\) to a permitted existing label or a distinct fresh label. The [repair checker](check_regular_path_repair_obstruction.py) enumerates these role identifications, checks their edge and factor compatibility, and solves the local cover with blue tails kept internal. The 52 valid length-three cycle cases all decompose. For a three-piece block in a longer cycle, all but four of the 173 compatible patterns decompose. Each failing pattern satisfies \(d_i\in\{a_{i-1},a_{i+1}\}\) for the middle index \(i\).

If there is a successful triple in the longer odd cycle, pair the remaining even chain. If every triple fails, the distinct \(d_i\) and \(a_i\) give a bijection \(i\mapsto i\pm1\) from matching positions to pendant positions. A step \(+1\) at \(i\) forces \(+1\) at \(i+2\) by injectivity. Odd cycle length therefore forces uniform steps. If \(a_i=d_{i+1}\) throughout, use

\[
(a_i,b_i,c_{i-1},d_{i-1},c_{i-2},b_{i-2}).
\]

If \(a_i=d_{i-1}\) throughout, use

\[
(a_i,b_i,c_i,d_{i+1},c_{i+1},b_{i+2}).
\]

Each rotation uses each pendant edge once, both classes of red edges once, each matching edge once, and each square's blue edge once. In each path the \(b\)-labels are distinct and disjoint from the \(c\)-labels. The displayed \(d\)-label differs from both \(b\)-labels by the red- and blue-edge exclusions. Under the chosen sign, the new \(a_i\) differs from that \(d\)-label and every \(c\)-label by distinctness of the matching vertices. All blue tails are internal. This completes the pure-cycle result. Mixed components and the attachments of other defective trails to the repaired cycles are still required for a general proof.

A sample check generated one generic cycle for each of 134 mixed link words of lengths three through nine modulo rotation, then tested 100 random label identifications per word subject to edge and factor compatibility. Every test found a path partition preserving blue tails. This does not establish a universal repair rule for mixed cycles.

### Removing the pure square defects

Every matched simple 5-regular graph has an edge partition into simple five-edge paths and open five-edge trails containing triangles. In addition to the initial partition with only pure square defects, this gives a reduction in the opposite direction. It uses simultaneous exchanges on the original canonical partition, followed by the finite triple check described below.

For a defective trail \(T=(a,b,c,d,e,b)\), its target is the original trail in which \(c\) is a red head. If the target is defective, its red head \(c\) is either its repeated vertex (a type-1 link) or the other red head (a type-2 link). A defective trail has a single target, and no two defective trails have the same \(c\). Thus the type-2 links form directed paths and cycles. On each path choose the first and every other vertex as a source, and on each even cycle choose alternate vertices. Set aside the odd cycles for the moment. Every remaining defective trail that is not a source gets exactly one type-2 link from a source, and a source never sends to a source through a type-2 link.

Each source trades its red edge \(bc\) for the blue arc \(c\to s(c)\) from its target. The source loses the red edge of its square and receives a new final edge. A target of a type-1 link trades its pendant, while a target of a type-2 link loses the closing blue edge of its square. A good target receives terminal-edge exchanges. If a target has both types of input, they use different blue arcs. Apply all trades simultaneously.

For a source, the resulting sequence is \((A,b,e,d,c,s(c))\), with \(A=a\) or \(A=r(b)\) depending on whether it receives a type-1 link. The only possible collisions with the retained internal vertices are \(A=d\) and \(s(c)=e\). The exclusions for \(s(c)\) follow from blue injectivity, simplicity and the matching. When \(A=r(b)\), it differs from \(c\) by the absence of a red 2-cycle and from \(e\) by red injectivity. The endpoints are distinct. In particular \(r(b)\) is an original square terminal of the incoming source, so equality with \(s(c)\) would require that incoming source to be its own target through a type-2 link from the current source. Such a source-to-source type-2 link was excluded.

For a recipient, the sequence is \((A,b,c,d,e,r(e))\), with the same choice of \(A\). Red injectivity and the absence of red 2-cycles leave only \(A=d\) or \(r(e)=c\) as possible repetitions. Its two endpoint labels are distinct original terminal labels. For a good target, write the original path as \((x,c,f,g,h,y)\) and consider an incoming source with old terminal \(b=r(c)\) at that side. The same exclusions as in the parallel repair show that the new terminal \(b\) can meet the four retained internal vertices only at \(g\). The opposite-end exchange is symmetric. New terminal labels are distinct from each other and from any retained opposite terminal. In all three cases, any repetition gives a triangle, and all arcs at terminal positions point toward the terminal.

An odd type-2 cycle has no incoming type-2 link from outside. Apply its incoming type-1 trades to the pendants first. In the notation \(c_i=e_{i+1}\), let \(A_i\) be its old or changed pendant terminal. The old \(a_i=s(b_i)\) differs from every \(b_j\), since \(b_j=s(e_j)\) and all red heads \(b_i,e_j\) are distinct. A replacement \(A_i=r(b_i)\) differs from every \(b_j,c_j\), since the red tail \(b_i\) is then a matching endpoint of an external source. The same argument excludes equality with any \(e_j\). The \(A_i\) are distinct because each remains an original terminal label, and the exchanges move different terminal labels.

For two consecutive pieces of the cycle, use the two-piece replacement above with \(A_i,A_{i+1}\) in place of the old pendant terminals. Each new sequence is simple unless its pendant terminal equals the retained matching endpoint \(d_i\) or \(d_{i+1}\) at distance three, which gives a triangle. Choose any block of three consecutive pieces and pair the remaining even chain. On the triple, the only possible identification of a \(d\)-label with a \(b\)-label is between the first and third indices in an open block. In a closed three-cycle these sets are disjoint. The \(c,d\) labels are distinct matching endpoints, and the \(b\)-labels are distinct and avoid all \(c\)-labels. Each \(A_i\) can be an allowed corner label or a distinct fresh label. It differs from its own \(c_i,e_i\) and all \(b\)-labels. If changed, it avoids every \(c,e\)-label, and if unchanged, it differs from its own \(d_i\).

The [repair checker](check_regular_path_repair_obstruction.py) enumerates all such triple identifications and change flags with 15 distinct edges, including patterns that need not extend to a full canonical graph. All 344 closed cases and 945 open cases have exact covers by three suitable trails. It enumerates every nonclosed five-edge walk with distinct edges and accepts it if it is simple or its first or last three edges make a triangle. It also checks the direction of each blue terminal arc and verifies the exact edge counts of each selected cover. This handles the odd cycles and finishes the reduction. Each remaining repetition is between an endpoint and a vertex three edges away in its trail. Eliminating these repetitions would still be necessary to settle the conjecture.

### Exact bridge and two-edge-cut reductions

For \(d=2k+1\), every bridge in a \(d\)-regular graph separates odd-order sides and belongs to every perfect matching. In a \(d\)-edge path decomposition the crossing path must contain \(k\) edges in each side. Indeed, on a side of odd order \(n\) there are \((dn-1)/2\equiv k\pmod d\) internal edges. All other paths on that side use \(d\) edges at a time. This central-bridge property is Favaron–Genest–Kouider's Proposition 1. [Original paper](https://doi.org/10.1002/jgt.20413)

The smallest possible side at a bridge has order \(d+2\). Regularity of vertices other than the port requires \(n\ge d+1\) and \(n\) is odd. At \(n=d+2\), the complement of the side has degree two at the port and degree one elsewhere, so the rooted side is unique up to isomorphism. It admits a partition into \(d\)-edge paths and a \(k\)-edge path starting at the port. To see this, take the \(k\)-th power of \(C_{2k+3}\). Its complement is the cycle of steps \(k+1\), since \(\gcd(k+1,2k+3)=1\). Add an alternating matching of the complementary cycle with the port deleted. In the \(k\)-th power orient the distance-\(j\) edges by step \(+j\) for odd \(j\) and step \(-j\) for even \(j\). Starting at each vertex, follow these factors in order. The cumulative steps \(0,1,-1,2,-2,\ldots\) are distinct and lie in an interval of span \(k\). Hence the arms at endpoints of any added matching edge, at cyclic distance \(k+1\), are disjoint. Their joins give simple \(d\)-edge paths. The unpaired arm is the required rooted path. At each stage the starting vertices of the distance-\(j\) edges form a permutation, so this covers all edges. This is an instance of the spanning-cycle-power construction. [Botler–Hoffmann](https://doi.org/10.1016/j.disc.2022.112906)

Consequently, in any minimum-order counterexample to the original conjecture at a fixed \(d\), each bridge has a side of order exactly \(d+2\). If both sides were larger, attach an independent smallest cap to each side by a new bridge. The original matching restricts to a matching that misses only the port of each side, so both capped graphs have perfect matchings. Both graphs are smaller. The two decompositions guaranteed by minimality give rooted \(k\)-edge paths at the original ports, which can be joined across the original bridge.

Attaching a smallest bridge cap to every vertex of a simple \(2k\)-regular graph \(H\) gives a matched \(d\)-regular graph \(G\). A \(d\)-edge path decomposition of \(G\) is equivalent to a \(k\)-edge path decomposition of \(H\) in which each vertex is an endpoint twice. Every cut bridge forces one rooted \(k\)-edge arm in \(H\). There are \(|V(H)|\) such arms, already using all \(k|V(H)|\) edges of \(H\). In the full decomposition each vertex of \(G\) is a path endpoint exactly once, since total endpoint occurrences equal \(|V(G)|\) and odd degree requires an odd number at each vertex. Thus the arms begin and end once at each core vertex. Conversely, given the balanced decomposition of \(H\), form a multigraph with an edge between the endpoints of each arm. The multigraph is 2-regular, including possible cycles of two parallel edges. Orient its cycles to choose one arm starting at every vertex, then join those arms across the bridges to the cap arms. The balanced decomposition property here is the conjecture of Kouider and Lonc. Consequently a counterexample to that conjecture would also disprove Favaron-Genest-Kouider. [Botler-Talon, Discrete Mathematics 340 (2017), 2275-2285](https://doi.org/10.1016/j.disc.2017.04.024)

A two-edge cut separates even-order sides. If both cut edges were in one \(d\)-edge path, that path would use at most \(d-2\) internal edges on either side, but the number of internal edges on either side is \(-1\) modulo \(d\). Therefore each cut edge belongs to a separate crossing path. Mark the two cut incidences on each side. Each side's two partial path lengths sum to \(d-1\), by the same residue and the bound \(2(d-1)\). Conversely, decompositions on both sides into internal \(d\)-edge paths and rooted simple segments glue precisely when the lengths at opposite ends of each cut edge sum to \(d-1\). Each glued path is simple because its segments lie on disjoint sides.

In degree five I verified rooted length two for the 1, 28 and 3,749 eligible one-port graphs of orders 7, 9 and 11. Eligibility means the port-deleted graph admits a perfect matching. All 1,802 eligible two-port graphs with distinct ordered ports of orders 6, 8 and 10 realized all five ordered length pairs. The 181 two-port graphs with the same port twice at orders 8 and 10 also realized all five. These runs used a complete degree-sequence generator modulo vertex isomorphism preserving the marked ports and a path exact cover including one column for each port and each terminal. The counts are finite checks.

In a minimum-order degree-five counterexample, no two-edge cut can have a side of order 8 or 10. Replace that side by \(K_6\) minus an edge, attaching the distinct endpoints of the deleted edge to the opposite cut incidences. This is a smaller simple matched graph. The six-vertex side supports an internal matching and a matching with both ports deleted, so the new cut allows the original matching status. The smaller graph's path partition gives a signature on the opposite side. The original small side has every signature by the finite checks, so it glues back. This argument also applies to larger sides once all their signatures are established. If the small side has order six and the opposite incidences are distinct and nonadjacent, replacing the small side by the single missing edge between the incidences gives the same reduction.

For odd \(d=2k+1\), a cap with two distinct ports and an internal perfect matching can disprove the conjecture if it forbids both orders of some pair \((k-j,k+j)\), \(1\le j\le k\). Use \(k\) copies of the cap, with a hub \(u\) joined to both ports of each copy, and attach one matched bridge cap at \(u\). The graph has a perfect matching. In a supposed decomposition, the bridge at \(u\) is a middle edge. In each pair of cap connectors, both edges occupy the same level away from their path's middle edges, since their inside arm lengths add to \(d-1\). For \(i=0,\ldots,k\), let \(c_i\) count the appearances of \(u\) at level \(i\) in path halves, with level zero at a middle vertex and level \(k\) at a terminal. Then \(c_k=1\), \(\sum_{i=0}^{k-1}c_i=k\), and the incident edge count at any nonzero level \(i\) is \(c_{i-1}+c_i\), which is even. All \(c_i\) are odd and thus equal one. The middle incidence is exactly the bridge, and there must be exactly one pair of cap connectors at each nonzero level. The forbidden pair would make this impossible. The explicit noncentral cap below forbids the middle pair, which does not trigger this criterion.

### Endpoint counts for cuts

For a side \(W\) with \(r\) cut incidences, split cross-cut paths at those incidences. Let \(t\) count the resulting local segments with one terminal in \(W\). There are \(t\) rooted segments and \((r-t)/2\) transit segments with two cut incidences. Every vertex is the endpoint of exactly one full path, so there are \((|W|-t)/2\) full paths wholly inside \(W\). Subtracting their total length from the \( (d|W|-r)/2\) internal edges shows that the sum of lengths of the rooted and transit segments is

\[
\frac{dt-r}{2}.
\]

For a three-edge cut in degree five this means either three rooted arms of total length six or one rooted arm and a transit segment of total length one. In particular, distinct nonadjacent ports cannot be joined by a transit segment. This supplies a counterexample criterion. Suppose a simple near-5-regular graph with three port deficits at distinct vertices admits matching after deletion of one designated port and after deletion of at least one other port. If the designated port is adjacent to neither other port and cannot supply length four in a rooted-arm cover, use five copies as follows. Connect all designated ports to a common hub \(x\). Take four other hubs \(a,b,c,d\) with internal graph \(K_4-cd\), so their remaining degrees for cap connectors are \(2,2,3,3\) in the order \(a,b,c,d\). In four copies attach the alternative matchable port to \(a,b,c,d\) respectively and the remaining port to \(c,d,a,b\) respectively. Attach the final copy's two other ports to \(c,d\). Match \(x\) through that final copy and each of the four other hubs through its designated copy. No path can end at \(x\). After entering an attached copy it would have to use a forbidden transit or supply the missing length-four arm. The small instance search has so far found compatible length-four arms.

### A noncentral two-port cap

Take \(K_6-56\) on vertices \(1,\ldots,6\), add a vertex \(0\) adjacent to \(5,6\), attach the smallest one-bridge cap at \(0\), and reserve two connectors at \(0\). In any \(5\)-edge path decomposition of a graph containing this side, the pair of inside lengths cannot be \((2,2)\). Three distinct paths would have middle edges incident to \(0\), namely the bridge and the two connectors. Each would use two incidences at \(0\), exceeding degree five.

All other pairs are attainable. For inside lengths \((0,4)\), use rooted segments \((0)\), \((0,6,2,4,3)\), the bridge arm \((0,5,1)\), and internal paths \((2,3,1,6,4,5)\), \((4,1,2,5,3,6)\) in the seven-vertex core. For lengths \((1,3)\), use \((0,5)\), take the second connector and the attached bridge in the same path through \(0\) with the cap's two-edge arm supplying the remaining inside length, and use internal paths \((0,6,1,2,3,4)\), \((1,3,5,4,2,6)\), \((2,5,1,4,6,3)\). Reversing the order of connectors gives the other two pairs. A matching of the core minus \(0\) extends across the attached bridge. In any perfect matching of a graph containing the side neither connector can be used, because the bridge already matches \(0\).

This cap turns a pair of connectors at two core vertices into terminal stubs of lengths \((1,5)\) or \((2,4)\), in either order. The lengths include the two connector edges. A core decomposition thus consists of simple segments in the genuine core edges, joined at each end to at most one stub, with one terminal role at every core vertex. Each paired set of stubs contributes a total length of six. Each separately attached bridge cap contributes a single stub of length three. The two-edge-cut argument prevents a path from entering such a cap and then returning to the core through its second connector, so this model is exact for this construction. The complete-core substitution search passed all 16,384 configurations derived from \(K_6\) by replacing chosen nonmatching edges with pairs of stubs and chosen matching edges with two bridge caps. It also passed 4,000 samples with planted matchings at core orders 8, 10, 12 and 14.

### One forbidden ordered noncentral pair would suffice

For any odd \(d=2k+1\), a single absent ordered pair \((i,2k-i)\), \(i\ne k\), in an internally matched two-port cap suffices. Take two copies of the cap, reverse the order of the ports in the second, and join the copies in series. To join in series, add an edge between the second port of the first cap and the first port of the second cap, and retain the other two ports. The joined cap has an internal matching and distinct ports, even if the two ports in an original cap share a vertex. Its allowed ordered pairs are the intersection of the original set with its reversal. Each original cap is still the even side of a two-edge cut, so the joining edge belongs to a separate crossing path. If the first cap's ordered pair is \((i,2k-i)\), that joining path contains arms of lengths \(2k-i\) and \(i\), requiring the second cap to have pair \((i,2k-i)\) as well. Conversely, these arms concatenate into a simple path across the two disjoint caps. Both orders of the missing noncentral pair therefore fail in the joined cap. The hub construction above applies with \(j=|k-i|\).

In particular, the original conjecture at degree \(d\) would imply the availability of every ordered noncentral pair in every internally matched two-port cap, regardless of whether the central pair is available. The search has yet to produce a cap violating this consequence.

One way to search for such a cap is to join an odd three-port graph \(B\) to the seven-vertex graph \(K_6-56\) plus vertex \(0\) adjacent to \(5,6\), now with three cut incidences sharing \(0\). Join two of those incidences to distinct ports \(x,y\) of \(B\), and keep the remaining incidence at \(0\) and the third port \(z\) of \(B\). Choose \(z\) nonadjacent to either \(x\) or \(y\), and assume \(B\) has a matching after deleting \(x\) or after deleting \(y\). The joined cap is internally matched by the corresponding joining edge. All three segments on the \(B\) side must be rooted. A transit from \(z\) would have length at most one, and a transit between \(x,y\) would repeat \(0\) in the resulting path.

On the side with shared port \(0\), separate paths yield length tuples given by permutations of \((0,2,4)\) or \((0,3,3)\). Alternatively two connectors use a zero-length transit and the remaining rooted arm has length one. All these states occur, as follows from the seven-vertex certificates above and the additional rooted arms \((0),(0,5,1,2),(0,6,3,4)\) with internal paths \((1,6,2,4,5,3),(5,2,3,1,4,6)\). If \(B\)'s exterior arm at \(z\) is \(0,1\), or \(4\), each possible pair of its other rooted lengths can join to one of these states. If the exterior arm at \(z\) has length \(3\), its other two arms have lengths summing to three. Lengths \(0,3\) can use a transit involving the exterior incidence at \(0\). Arms of lengths \(1,2\) must be vertex-disjoint so their join through \(0\) is simple. Therefore the joined cap lacks an ordered noncentral pair when the corresponding exterior length on \(B\) is unavailable, or for length three when both types of joining fail. A computational search can use the rooted-arm exact cover with an added disjointness condition on the two arms in the last test.

### A limit of repairing a specified trail

The bound of three pieces can also fail for the canonical factor construction. In the same notation as above, let \(Q=(g,f,e,h,i,j)\) be the canonical trail centred at the matching edge \(eh\), with \(f=r(e)\), \(g=s(f)\), \(i=r(h)\) and \(j=s(i)\). Another repair option is to replace \(T\) and \(Q\) with

\[
(a,b,e,h,i,j),\qquad (b,c,d,e,f,g).
\]

The option gives two simple paths exactly when \(h,i\ne a\), \(f\ne c\), and \(g\ne c,d\). In the first path \(h\ne b\) since \(eb\) is blue, \(i\ne b,e\) by red injectivity and the matching, and \(j\ne a,b\) by blue injectivity. The only other new equality there, \(j=e\), would be a canonical matched-triangle repetition. In the second path \(f\ne b,d,e\) by red injectivity, absence of red 2-cycles and simplicity. Also \(g\ne b,e,f\) by blue injectivity, edge disjointness of the factors and simplicity. Each blue tail remains internal and the middle edges become \(eh\) and \(de\).

The [repair obstruction checker](check_regular_path_repair_obstruction.py) gives a canonical partial assignment of six trails, starting with \((0,1,2,3,4,1)\). At each vertex of these trails it fills any missing canonical role using fresh vertices. A vertex has three such roles, as a middle-edge endpoint, as a red head, and as a blue head. This assigns all edges at every vertex in the initial six trails. It takes ten indexed copies of the resulting assignment and pairs remaining red and blue outgoing stubs to incoming stubs using intercopy shifts \(+1\) and \(+3\). It pairs unmatched labels with the same label at shift \(+5\). The three shifts use disjoint undirected edge classes. The possible shifts of a red-then-blue walk are \(0,1,3,4\) modulo ten, so a new matching edge cannot close a triangle of the forbidden orientation. An old in-copy matching edge can close such a triangle only via two old arcs. The checker verifies simplicity, degree five, the perfect matching, the absence of forbidden repetitions, and the edge partition into canonical paths and square trails on 1,880 vertices.

The designated trail meets five other trails. Exact cover rules out simple path partitions for all five pairs and all 45 triples containing it whose trail intersection graph is connected. A disconnected selection cannot help, since any simple replacement must lie within one connected component of the edge union. This obstruction permits all simple replacement paths, including ones using a blue tail as an endpoint. The checker finds and independently verifies a four-piece repair that keeps all blue tails internal, so the minimum repair size for this trail is four.

The proposed assertion that *each specified defective trail in an arbitrary partition into paths and square trails can be repaired using at most three pieces* is false. The [repair obstruction checker](check_regular_path_repair_obstruction.py) constructs a 7,232-vertex simple 5-regular graph with a perfect matching and verifies the initial trail partition. The designated trail has seven adjacent pieces. Every possible union containing it and one or two other pieces that could participate in a connected replacement fails the exact path cover test. The checker tries seven two-piece and 455 three-piece unions, including some disconnected unions. A disconnected union cannot help unless its component containing the designated trail already admits the repair.

The construction starts with seven square trails. For the designated trail \(a,b,c,d,e,b\), use \(c,e\) as the repeated vertices of two other square trails. Repeat this at their corresponding corners. At each of the top three squares, attach simple five-edge paths at the opposite corner \(d\), one meeting it at a terminal and the other meeting it one edge from a terminal. Attach two more paths at the pendant \(a\), and one at the first repeated vertex \(b\). Each attachment uses fresh vertices outside its attachment point. The degree-five repeated vertices obstruct a two-piece repair, and the short chains and repeated vertices restrict the three-piece candidate sets.

The checker saturates all vertices of this initial assembly using paths attached one vertex at a time. It selects a partial matching covering those vertices. Then it fills the remaining terminal and interior roles using simple paths through cyclically indexed copies of the assembly. The filler paths do not touch the saturated vertices. A reserved odd shift between equal labels supplies a perfect matching on their copies for every label omitted by the partial matching. The checker reconstructs all edges and verifies regularity, distinct edges, the matching, and the path and square-trail forms. Its local search enumerates simple five-edge paths in each candidate union and uses exact cover with one column per edge. This limit concerns a chosen defective trail in an arbitrary intermediate partition. An iteration that chooses a different defective trail, or imposes a stronger invariant, remains possible.
