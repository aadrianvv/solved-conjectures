from functools import cache
from itertools import combinations_with_replacement

import full_cactus as check


def theta_ornaments(cap3):
    modes = tuple(check.MODES)
    triples = tuple(
        triple for triple in combinations_with_replacement(modes, 3)
        if triple.count(0) <= 1
    )
    complete = (1 << len(triples)) - 1
    port_count = 3 * check.W
    support = [[sum(1 << m for m in modes if check.permits(m, x, y))
                for y in range(port_count)] for x in range(port_count)]
    caps = [sorted(domain) for domain, _ in cap3]

    @cache
    def covered_by(a, b, c):
        return sum(1 << i for i, (x, y, z) in enumerate(triples)
                   if a >> x & b >> y & c >> z & 1)

    for i, left in enumerate(caps):
        palette_representatives = [
            (a, b, c) for a, b, c in left
            if a < check.W and b < 2 * check.W
            and (b >= check.W or c < 2 * check.W)
        ]
        for j, right in enumerate(caps):
            remaining = complete
            for a, b, c in palette_representatives:
                first, second, third = support[a], support[b], support[c]
                for x, y, z in right:
                    remaining &= ~covered_by(first[x], second[y], third[z])
                    if remaining == 0:
                        break
                if remaining == 0:
                    break
            if remaining:
                index = (remaining & -remaining).bit_length() - 1
                print("INCOMPATIBLE THETA", cap3[i][1], cap3[j][1], triples[index], flush=True)
                raise SystemExit(1)
    print("theta junction cases",len(caps)**2*len(triples),flush=True)


if __name__=='__main__':
    check.normalize_arcs(check.cap_domains_with_petals(2))
    theta_ornaments(check.cap_domains_with_petals(3))
