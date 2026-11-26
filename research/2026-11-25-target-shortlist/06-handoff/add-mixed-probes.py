from pathlib import Path
folder = Path(__file__).parent
base = (folder/'full-cactus-bounds.py').read_text(encoding='utf-8-sig')
insertion = '''
def acceptance_profile(relation):
    """Each output mask contains exactly the exterior states compatible with its orbit."""
    masks = []
    for orbit in relation:
        allowed = 0
        for a in range(W):
            for b in range(W):
                if any(i != a and row(orbit, i) & ~(1 << b) for i in range(W)):
                    allowed |= 1 << (a * W + b)
        masks.append(allowed)
    return tuple(masks)


def minimal_probe_representatives(families, distinct_only):
    """Minimize accepted exterior states while using actual realizable probes."""
    probes = {}
    for (_, coincident), family in families.items():
        if coincident and distinct_only:
            continue
        for relation, tag in family.items():
            mask = acceptance_profile(relation)
            previous = probes.get(mask)
            if previous is not None and representative_vertices(previous) <= representative_vertices(tag):
                continue
            if previous is not None:
                del probes[mask]
            insert(mask, tag, probes)
    return probes


def report_minimal_probes(families):
    expected = {True: (3, (2, 3, 9)), False: (7, (1, 2, 3, 5, 5, 8, 13))}
    for distinct_only in (True, False):
        probes = minimal_probe_representatives(families, distinct_only)
        sizes = tuple(sorted(map(representative_vertices, probes.values())))
        print('probe sizes', distinct_only, sizes, flush=True)
        for tag in probes.values():
            print('  probe', representative_vertices(tag), repr(tag), flush=True)

'''
base = base.replace('\ndef main():', '\n' + insertion + '\ndef main():')
base = base.replace('print("prototype sizes", flags, min(sizes), max(sizes), flush=True)','print("prototype sizes", flags, min(sizes), max(sizes), flush=True)\n    report_minimal_probes(current)')
(folder/'full-cactus-probes.py').write_text(base, encoding='utf8')
