from itertools import combinations_with_replacement

import full_cactus as check


def canonical_palette(state):
    next_color = 0
    for symbol in state:
        color = symbol // check.W
        if color > next_color:
            return False
        if color == next_color:
            next_color += 1
    return True


def multi_theta_ornaments(caps, arity):
    modes = tuple(check.MODES)
    words = tuple(
        word for word in combinations_with_replacement(modes, arity)
        if word.count(0) <= 1
    )
    complete = (1 << len(words)) - 1
    port_count = 3 * check.W
    support = [
        [sum(1 << m for m in modes if check.permits(m, x, y))
         for y in range(port_count)]
        for x in range(port_count)
    ]
    cover = [
        [sum(1 << i for i, word in enumerate(words) if mask >> word[pos] & 1)
         for mask in range(1 << len(modes))]
        for pos in range(arity)
    ]
    domains = [sorted(domain) for domain, _ in caps]

    for i, left in enumerate(domains):
        left = [tuple(support[symbol] for symbol in state)
                for state in left if canonical_palette(state)]
        for j, right in enumerate(domains):
            remaining = complete
            for left_rows in left:
                for state in right:
                    witness = remaining
                    for pos, symbol in enumerate(state):
                        witness &= cover[pos][left_rows[pos][symbol]]
                        if witness == 0:
                            break
                    remaining ^= witness
                    if remaining == 0:
                        break
                if remaining == 0:
                    break
            if remaining:
                index = (remaining & -remaining).bit_length() - 1
                print("INCOMPATIBLE PARALLEL PATHS", arity, caps[i][1], caps[j][1], words[index], flush=True)
                raise SystemExit(1)
    cases = len(caps)**2 * len(words)
    print("parallel-path junction cases",arity,cases,flush=True)
    assert cases == {3: 216832, 4: 2025366}[arity]


def distinct_high_spokes():
    for mode in check.MODES[1:]:
        for a in range(5, check.W+1):
            for b in range(4, check.W+1):
                assert check.permits(mode, a-1, check.W+b-1)
                assert check.permits(mode, b-1, check.W+a-1)


if __name__=='__main__':
    check.normalize_arcs(check.cap_domains_with_petals(2))
    distinct_high_spokes()
    multi_theta_ornaments(check.cap_domains_with_petals(3), 3)
    multi_theta_ornaments(check.cap_domains_with_petals(4), 4)
