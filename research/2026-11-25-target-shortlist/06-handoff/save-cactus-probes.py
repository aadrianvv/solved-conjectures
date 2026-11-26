from pathlib import Path
import sys

source = Path(sys.argv[1])
target = Path(sys.argv[2])
new_checker = (source/'full-cactus-probes.py').read_text(encoding='utf-8-sig')
start = new_checker.index('def report_minimal_probes')
end = new_checker.index('def main()', start)
new_checker = new_checker[:start] + '''def report_minimal_probes(families):
    expected = {True: (2, 3, 9, 9), False: (1, 2, 3, 5, 5, 8, 13)}
    for distinct_only in (True, False):
        probes = minimal_probe_representatives(families, distinct_only)
        sizes = tuple(sorted(map(representative_vertices, probes.values())))
        print('probe sizes', distinct_only, sizes, flush=True)
        assert sizes == expected[distinct_only]


''' + new_checker[end:]
(target/'06-local-irregularity-cut-check.py').write_text(new_checker, encoding='utf8')
note = target/'06-revised-local-irregularity.md'
body = note.read_text(encoding='utf-8-sig')
old_start = body.index('**Corollary.** In a vertex-minimal')
old_end = body.index('## Computation checkpoint', old_start)
addition = r'''For replacing a side while the exterior graph is fixed, one can compress further. In each palette orbit map a side's relation $R$ to its acceptance relation
$$
\{(a,b):\text{ some }(x,y)\in R\text{ satisfies }x\ne a\text{ and }y\ne b\}.
$$
This map is monotone and the exterior degree sentinel still represents all degrees above 19. An exterior witness accepted by a replacement is enough, even if the replacement's own terminal degrees differ from those of the original side. Retaining acceptance-minimal realizable probes among distinct-terminal representatives gives four probes of orders $2,3,9,9$. Retaining them among all representatives gives seven probes of orders $1,2,3,5,5,8,13$. The checker confirms both calculations. As before, applying the original-side relation may require restoring deletions by degree avoidance.

**Corollary.** In a vertex-minimal counterexample to the revised conjecture, any cactus side of a genuine two-edge cut has at most nine vertices with distinct terminals, and at most 13 when its terminals coincide. Both sides cannot be cacti by the theorem, so the exterior side is noncactus. A replacement probe can always preserve simplicity. For a distinct-terminal side choose a distinct-terminal probe. If the original terminals coincide, the other side has distinct terminals and any of the seven probes may be used. The new graph stays noncactus because the exterior side already contains an edge in two cycles. A strictly smaller replacement would be 3-colorable by minimality. Its exterior coloring is accepted by the original side, giving a 3-coloring of the alleged counterexample.

If a single bridge has a cactus side and a noncactus side, the same argument gives a bound of five vertices on its cactus side in a vertex-minimal counterexample. The rooted cactus signature is nonempty, and the leaf, the two-vertex path, or the five-vertex half of the bow-tie forbids degrees one, two, or three respectively. A singleton signature uses its corresponding probe. A signature with more than one value allows every exterior degree and can use the leaf.

'''
body = body[:old_start] + addition + body[old_end:]
needle = 'An independent direct enumeration of complete path-edge color sequences'
advance = '''- The mixed two-cut search tested 42,246 marked connected noncactus fragments through order seven against all the cactus probe classes, in 133,306 exact queries. Every compatible simple join was 3-colorable. A separate three-link search projected 227 three-port fragments from seven bow-tie and triangle-chain seeds. It checked 13,504,026 simple joins over all terminal matchings and the five normalized path modes, with no obstruction.\n- A direct $K_4$ with an arbitrary rooted cactus at each vertex is covered by the four arity-three junction relations and their attachment normalization. All 178,365 multisets of four out of the 44 minimal junction domains passed. A further 100,000 mixed-connector and cubic-core samples, using the same rooted cactus domains, passed.\n\n'''
advance = advance.replace('the four arity-three junction relations', 'one arity-three junction relation per vertex')
body = body.replace(needle, advance + needle)
note.write_text(body, encoding='utf8')
