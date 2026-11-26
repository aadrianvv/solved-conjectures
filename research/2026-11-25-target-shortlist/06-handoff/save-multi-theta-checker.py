from pathlib import Path
import sys

source, target = map(Path, sys.argv[1:3])
checker = target/'06-local-irregularity-cut-check.py'
code = checker.read_text(encoding='utf-8-sig')
code = code.replace('Exact finite checker for the two-cactus-side theorem.', 'Exact finite checker for cactus cuts and cactus attachments.')
addition = (source/'multi-theta-ornaments.py').read_text(encoding='utf-8-sig')
addition = addition[addition.index('def canonical_palette'):addition.index("if __name__")].replace('check.', '')
addition += '''def check_high_degree_arc_states():
    bare = (0, 0, (0, 0, 0))
    strict = ARC_REPRESENTATIVES.index((bare, bare))
    for a in range(5, W + 1):
        for b in range(1, W + 1):
            assert permits(strict, a - 1, W + b - 1)
            assert permits(strict, b - 1, W + a - 1)
        for b in range(5, W + 1):
            for mode in MODES[1:]:
                if mode != strict:
                    assert permits(mode, a - 1, b - 1)
                    assert permits(mode, a - 1, W + b - 1)


'''
code = code.replace('def main():', addition + 'def main():', 1)
code = code.replace('    traversed=initial_and_step(caps[1],caps[2])','''    distinct_high_spokes()
    check_high_degree_arc_states()
    multi_theta_ornaments(caps[1], 3)
    multi_theta_ornaments(caps[2], 4)
    traversed=initial_and_step(caps[1],caps[2])''',1)
checker.write_text(code, encoding='utf8')
