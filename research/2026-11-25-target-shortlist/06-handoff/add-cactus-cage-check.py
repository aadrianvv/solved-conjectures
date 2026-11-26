from pathlib import Path
import sys

checker = Path(sys.argv[1])
body = checker.read_text(encoding='utf-8-sig')
basis = '''    arc_modes = {
        tuple(sum(pack(a, b)
                  for a in range(1, W + 1) for b in range(1, W + 1)
                  if permits(mode, a - 1, orbit * W + b - 1))
              for orbit in (0, 1))
        for mode in MODES[1:]
    }
    assert set(minimal_probe_representatives(families, False)) == arc_modes
    print('all two-ended cactus connectors use the same seven arc modes', flush=True)

'''
if 'same seven arc modes' not in body:
    body = body.replace('def canonical_palette(state):', basis+'\ndef canonical_palette(state):',1)
checker.write_text(body,encoding='utf8')
