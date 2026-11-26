# A negative answer to Favaron–Genest–Kouider Problem 5

For every odd \(d\ge 5\), there is a simple, 2-edge-connected, \(d\)-regular graph with a perfect matching in which the middle edges of a decomposition into \(d\)-edge paths cannot form a perfect matching. The construction has 288 vertices when \(d=5\).

Problem 5 asks whether every 2-edge-connected simple odd \(d\)-regular graph with a perfect matching admits a \(d\)-edge path decomposition whose middle edges form a perfect matching. This requirement allows any perfect matching as the middle edges. Favaron, Genest and Kouider gave examples of edge connectivity one where no matching extends. Their Conjecture 1 asks for an unrestricted decomposition and remains a separate target. [Favaron, Genest and Kouider, J. Graph Theory 63 (2010), 114–128, Section 6](https://doi.org/10.1002/jgt.20413) · [full text, p. 128](https://www.academia.edu/25437460/Regular_path_decompositions_of_odd_regular_graphs)

## A graph that forces both edges of a two-edge cut into every matching

Fix \(d\ge 5\) odd. Start with \(d-2\) vertices \(s_1,\ldots,s_{d-2}\). For each \(i\in\{1,\ldots,d\}\), take a disjoint complete graph on \(d+1\) vertices, delete the edge \(p_iq_i\), and add a vertex \(r_i\) adjacent to \(p_i,q_i\). Connect each \(r_i\) to all the \(s_j\). Delete \(r_1s_1\) and \(r_2s_2\), then add \(s_1s_2\). Call the resulting graph \(H_d\), with ports \(r_1,r_2\).

The two ports have degree \(d-1\), and all other vertices have degree \(d\). The order \(d^2+3d-2\) is even. Deleting the \(s_j\) leaves \(d\) odd components. Each would need an edge to some \(s_j\) in a perfect matching of \(H_d\), and there are only \(d-2\) such vertices. After deleting the two ports, there is a perfect matching. Match \(r_3,\ldots,r_d\) bijectively to the \(s_j\), then match each copy of \(K_{d+1}-p_iq_i\) internally. Such an internal matching exists by matching \(p_i,q_i\) to two distinct other vertices and pairing the rest.

The graph \(H_d\) is connected and has no bridge. The \(s_j\) and \(r_3,\ldots,r_d\) give a complete bipartite graph with \(d-2\ge 3\) vertices in each part. Each of \(r_1,r_2\) attaches to at least two of its vertices. The edge \(s_1s_2\) lies in a triangle through any unmarked \(r_i\). Every edge inside an odd block lies on a cycle, including the two edges at \(r_i\), which lie on a 4-cycle through \(p_i,q_i\) and another vertex of the clique.

To replace an edge \(xy\), delete it, take a fresh copy of \(H_d\), and add \(xr_1,yr_2\). The resulting two-edge cut has an even side \(H_d\). A perfect matching must use zero or two edges of this cut, and zero would require a perfect matching of \(H_d\). Thus both connectors belong to every perfect matching. The explicit matching of \(H_d-\{r_1,r_2\}\) supplies the rest of the matching inside the gadget.

## The host graph and its matchings

Write \(d=2k+1\). Take hubs \(u,v\) and \(2k\) disjoint copies of \(K_d\), denoted \(U_i,V_i\) for \(1\le i\le k\). Label clique vertices \(u_{i,1},\ldots,u_{i,d}\) and \(v_{i,1},\ldots,v_{i,d}\). Add the following edges:

- \(uu_{i,1},uu_{i,2},vv_{i,1},vv_{i,2}\) for every \(i\).
- \(u_{i,j}v_{i,j}\) for every \(i\) and every \(3\le j\le d\).
- \(uv\).

This is the graph in Figure 3 of the original paper. Every edge lies on a cycle. The clique edges and the hub-to-clique edges lie on triangles. Each \(u_{i,j}v_{i,j}\) lies on a 4-cycle using another \(u_{i,j'}v_{i,j'}\). The edge \(uv\) lies on a cycle through any pair of corresponding cliques. [Favaron–Genest–Kouider, Figure 3](https://doi.org/10.1002/jgt.20413)

Replace \(uv\) and every \(u_{i,j}v_{i,j}\) with \(j\ge 3\) by separate copies of the forced-matching construction above. Call the resulting graph \(G_d\). It is simple and \(d\)-regular. Every retained edge of the original graph lies on a cycle obtained by replacing each substituted edge in an original cycle by a path through its gadget. Each connector lies on such a cycle as well. Every edge inside a gadget lies on a cycle in that gadget. Thus \(G_d\) is connected with no bridge.

A perfect matching of \(G_d\) consists of both connectors at every gadget, the explicit port-deleted matching within each gadget, and the edges \(u_{i,1}u_{i,2}\) and \(v_{i,1}v_{i,2}\) for all \(i\). For every perfect matching \(M\) of \(G_d\), the connectors are forced. The first two vertices of each \(U_i\) must be matched to each other, since the hub \(u\) is already matched by its connector and all the other vertices of \(U_i\) are already matched by theirs. The corresponding statement holds in each \(V_i\). In particular, the cut of each clique has exactly two nonmatching edges, and their endpoints inside the clique are the two endpoints of its sole internal matching edge.

## Why the middle edges cannot form a perfect matching

Suppose there is a \(d\)-edge path decomposition of \(G_d\) whose middle edges form a perfect matching \(M\). Each vertex is an endpoint exactly once. Odd degree gives at least one endpoint occurrence at each vertex, and the \(n/2\) paths give exactly \(n\) endpoint occurrences.

Delete the middle edge from each path and orient the two \(k\)-edge halves away from the middle. Give each nonmatching edge the level \(1,\ldots,k\) at which it is traversed in its half. For a vertex set \(W\), let \(n_i\) count the half-path vertices at distance \(i\) from their starts that lie in \(W\), with multiplicity across half-paths. The starts are the endpoints of \(M\), and the ends are the endpoints of the original paths. Thus \(n_0=n_k=|W|\). The sum of degrees of \(G_d-M\) over \(W\) is \(2k|W|\), and it is also \(n_0+n_k+2\sum_{i=1}^{k-1}n_i\). Therefore

\[
\sum_{i=1}^{k-1}(n_i-|W|)=0.
\]

When exactly two nonmatching edges cross the cut of \(W\), their orientations are opposite since \(n_0=n_k\). If their levels differ, \(n_i-|W|\) equals \(1\) or \(-1\) on the nonempty interval between the two levels and vanishes elsewhere, contradicting the sum. The two edges therefore have the same level. This is the needed case of the original paper's cut identity. [Theorem 3](https://doi.org/10.1002/jgt.20413)

Apply this to a clique \(U_i\), whose internal matching edge is \(u_{i,1}u_{i,2}\). The path centered there must leave the clique, since \(K_d\) has only \(d\) vertices. An oriented half of that path first leaves through a nonmatching cut edge. Its tail inside the clique is either \(u_{i,1}\) or \(u_{i,2}\). If the edge had level at least two, that tail would repeat a middle vertex in the same path. Hence the two nonmatching cut edges of \(U_i\) both have level one.

It follows that all \(d-1\) nonmatching edges at \(u\) have level one. But \(u\) is an endpoint of a path and therefore must have an incident edge of level \(k\ge 2\). This is a contradiction. [Corollary 1 and the Figure 3 obstruction](https://doi.org/10.1002/jgt.20413)

## Verification and prior work

Run [check_regular_path_center_counterexample.py](check_regular_path_center_counterexample.py) with ordinary Python 3.12. The checker constructs every adjacency explicitly. It verifies regularity, connectivity, absence of bridges, an explicit perfect matching, the odd-component witnesses for each gadget, and the exact cut and degree conditions used at the cliques and hubs.

| Degree | Vertices | Edges | Perfect-matching edges | Forced connector edges |
|---:|---:|---:|---:|---:|
| 5 | 288 | 720 | 144 | 14 |
| 7 | 1,132 | 3,962 | 566 | 32 |
| 9 | 3,148 | 14,166 | 1,574 | 58 |
| 11 | 7,104 | 39,072 | 3,552 | 92 |

A separate implementation checked the four displayed degrees, including the bridge calculation and the cut conditions. There is also a positive scope check at degree five. The saved certificate partitions the starting 22-vertex graph into eleven five-edge paths and partitions the 38-vertex gadget into internal five-edge paths and two rooted arms of each ordered length pair \((0,4),\ldots,(4,0)\). In a starting path, replace an edge in position \(j\in\{1,\ldots,5\}\) by cutting the path and adjoining connector edges and gadget arms of lengths \(5-j\) and \(j-1\). When several edges are replaced in the same path, each middle fragment also has five edges after adding the two attached arms and connectors. The checker verifies the resulting 144 simple five-edge paths against every edge of \(G_5\). Thus this graph admits an unrestricted decomposition.

The obstruction at the original hubs and the starting graph are due to Favaron, Genest and Kouider. The new step is substituting the connected forced-matching graphs for the designated edges, so that the same obstruction applies to every perfect matching while the ambient graph stays bridgeless. The bounded prior-resolution search checked the original statement and known edge-connectivity-one example, author and title searches for Problem 5, and variants using “extendable matching”, “middle edges”, “type 0”, and “bridgeless” or “2-edge-connected”. No prior resolution of this exact question was found in the inspected sources. The original Conjecture 1 is tracked in the [degree-five research note](04-regular-path-decomposition.md).
