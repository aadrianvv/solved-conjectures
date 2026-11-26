from itertools import product
import full_cactus as c

PORTS = tuple(product(range(2), range(1,4), range(1,4)))


def acceptance(mask):
    return sum(1<<i for i,(orbit,a,b) in enumerate(PORTS)
               if mask[orbit] & c.pack(a,b))


def bits(n):
    while n:
        bit = n & -n
        yield bit
        n ^= bit


def hitting_minima(conditions):
    minima = {0}
    conditions = sorted(set(conditions),key=int.bit_count)
    for accepted in conditions:
        if accepted == 0:
            return ()
        updated = set()
        for stored in minima:
            if stored & accepted:
                updated.add(stored)
            else:
                updated.update(stored | b for b in bits(accepted))
        minima = set()
        for candidate in sorted(updated,key=int.bit_count):
            if not any(candidate & old == old for old in minima):
                minima.add(candidate)
    return sorted(minima)


def show(mask):
    return tuple(p for i,p in enumerate(PORTS) if mask >> i & 1)


def compatible(a,b):
    return any(w == x and y != u and z != v for w,y,z in show(a) for x,u,v in show(b))


def inspect(families):
    for kind, candidates in families.items():
        print(kind,len(candidates))
    all_cases = {}
    for kind in ('coincident','distinct','nonadjacent'):
        valid = (1 << len(PORTS)) - 1
        if kind == 'coincident':
            valid = sum(1<<i for i,(orb,a,b) in enumerate(PORTS)
                        if orb == 0 and a == b and a >= 2 or orb == 1 and a+b <= 3)
        required = [
            acceptance(c.acceptance_profile(p)) & valid
            for (danger,same), domain in families.items()
            if not (kind == 'coincident' and same)
            for p in domain
        ]
        for a,b in product(range(1,4), repeat=2):
            required.append(sum(1<<i for i,(_,x,y) in enumerate(PORTS) if a != x and b != y) & valid)
        if kind == 'nonadjacent':
            required.append(sum(1<<i for i,(orb,x,y) in enumerate(PORTS) if orb == 0 and x != y))
        minima = hitting_minima(required)
        if kind == 'coincident':
            robust=[]
            for case in minima:
                mirrored=sum(1 << PORTS.index((r,y,x)) for r,x,y in show(case))
                robust.append(case|mirrored)
            minima=list(set(robust))
        print('minima',kind,len(minima),flush=True)
        all_cases[kind]=minima

    for a,A in all_cases.items():
      for b,B in all_cases.items():
        if a==b=='coincident': continue
        bad=[(x,y) for x in A for y in B if not compatible(x,y)]
        print(a,b,'bad',len(bad),'with both flexibly self-compatible',sum(compatible(x,x) and compatible(y,y) for x,y in bad))
        for x,y in bad[:3]:
            print('    ',show(x), show(y))
        for x,y in bad:
            if compatible(x,x) and compatible(y,y):
                print('    self compatible witness',show(x),show(y))
                break

c.report_minimal_probes=inspect
c.main()
