# Favaron–Genest–Kouider Problems 3 and 6

Problem 3 asks for a simple odd \(d\)-regular graph with a \(d\)-edge path decomposition and no perfect matching for every odd \(d\ge 7\). The construction below works for every odd \(d\ge 5\). Problem 6 asks whether Theorem 2 extends beyond degree five. The second construction shows that, for every odd \(d\ge 7\), even a simple \(d\)-edge path decomposition whose middle edges form a perfect matching can fail to be rainbow-making. [Favaron, Genest and Kouider, Section 6](https://doi.org/10.1002/jgt.20413) · [Full text](https://www.academia.edu/25437460/Regular_path_decompositions_of_odd_regular_graphs)

These questions concern necessity of a perfect matching and the edge types in a given decomposition. Conjecture 1 concerns sufficiency of a perfect matching and remains unresolved by these constructions.

## Problem 3

Write \(d=2k+1\) with \(k\ge 2\). Let \(H\) be the \(k\)-th power of a cycle with \(8k+1\) vertices, labelled by residues modulo \(8k+1\). For each vertex take the rooted \(k\)-edge path with successive steps

\[
+1,-2,+3,-4,\ldots,(-1)^{k+1}k.
\]

The partial sums \(0,1,-1,2,-2,\ldots\) are distinct and have span \(k\), so these paths are simple. At step \(j\) the starting positions range through all vertices, using every cyclic distance-\(j\) edge exactly once. Every vertex is a root once, a terminal once, and an interior vertex once at each of the \(k-1\) intermediate positions.

Put \(x=0\) and \(y=4k\). Exchange the occurrence of \(x\) at the first intermediate position in the path rooted at \(-1\) with the root occurrence of \(y\) in its own path. The two paths lie in disjoint cyclic intervals before the exchange. Each new edge joins the cyclic radius-\(k\) neighbourhoods of \(x\) and \(y\) and has cyclic distance greater than \(k\), since the other endpoint is within distance \(k\) of one centre and its new neighbour is the other centre. More explicitly, the removed edges are \((-1,0),(0,-2),(y,y+1)\) and the new ones are \((-1,y),(y,-2),(0,y+1)\). They are distinct and absent in \(H\). Thus the modified paths remain simple and edge-disjoint. The modified core has degree \(2k-1\) at \(x\), degree \(2k+1\) at \(y\), and degree \(2k\) elsewhere. The respective numbers of path roots are two, zero and one. The core is connected because the missing cyclic predecessor edges at \(0\) and \(y+1\) have surviving bypasses via the distance-two edges \((-1,1)\) and \((y-1,y+1)\).

For every path root attach one independent odd graph by a bridge at that root. Use the following rooted graph for each attachment. Start with the \(k\)-th power of the cycle on \(2k+3\) vertices. Its complement is a cycle on the edges of cyclic distance \(k+1\), since \(\gcd(k+1,2k+3)=1\). Designate the attachment vertex and add the perfect matching of the complementary cycle with that vertex deleted. The attachment vertex has degree \(d-1\), every other vertex has degree \(d\), and the same alternating-step rule partitions the cycle power into rooted \(k\)-edge paths. The arms at the ends of an added matching edge lie in disjoint cyclic intervals of span \(k\), since their starts have cyclic distance \(k+1\). Join each such pair of arms across its matching edge. This leaves a single rooted \(k\)-edge arm at the attachment vertex and partitions all other attachment edges into \(d\)-edge paths.

The completed graph is simple and \(d\)-regular. Join each core arm to the arm in its dedicated attachment across the bridge to obtain a simple \(d\)-edge path. Together with the paths in the attachments these give an edge partition. Every perfect matching would have to use each bridge because its attached side has odd order. Two bridges meet at \(x\), so no perfect matching exists.

## Problem 6

An edge has type \(j\) if its position in its path is \(j\) steps from the middle edge. Rainbow-making means that edges of each nonzero type form a spanning 2-factor. Consider the following four paths in \(K_8\).

| Path | Middle edge |
|---|---|
| \(0,2,1,4,5,6,3,7\) | \(45\) |
| \(2,4,0,7,6,1,3,5\) | \(76\) |
| \(3,4,7,1,0,5,2,6\) | \(10\) |
| \(1,5,7,2,3,0,6,4\) | \(23\) |

Each of the 28 edges occurs exactly once. The four middle edges form a perfect matching. Vertex \(0\) has three edges of type 1, namely \(07,05,03\), so the decomposition fails the rainbow-making condition.

To extend the construction to \(d=7+2h\), choose an integer \(L>\max(2h,h(h+1)/2)\). Take \(L\) copies of \(K_8\) indexed modulo \(L\). For each \(j=1,\ldots,h\), join each vertex to the corresponding vertex \(j\) copies ahead. These edges form a 2-factor for each \(j\). They are distinct from the original edges and from the other new factors since \(L>2h\). Extend both ends of every original path by keeping the respective endpoint label and successively moving \(+1,+2,\ldots,+h\) copies. The visited copies on either extension are distinct and differ from the original copy because their shifts have strictly increasing positive sums less than \(L\). The two extensions use different labels and so are disjoint. Each label is an original terminal once in each copy. At every step the current copy indices are a translate of all the original indices, so all edges of the added 2-factor are used once. This gives a simple \(d\)-edge path decomposition of the simple \(d\)-regular graph. Middle and type-1 edges are unchanged, which proves the failure in every stated degree.

Targeted searches for the two problem numbers and the matching and rainbow-making formulations found the original statements and a discussion of Problem 3. They found no earlier all-degree solution. [MathOverflow discussion](https://mathoverflow.net/questions/97683/graph-decomposition-into-paths/97693)
