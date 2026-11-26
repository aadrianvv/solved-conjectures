import full_cactus as c

c.normalize_arcs(c.cap_domains_with_petals(2))
caps = c.cap_domains_with_petals(3)

def mask(mode, outside, reverse=False):
    return sum(1 << s for s in range(3*c.W)
               if (c.permits(mode,s,outside) if reverse else c.permits(mode,outside,s)))

left = {mask(mode, a-1): (mode,a) for mode in c.MODES for a in range(5,c.W+1)}
right = {mask(mode, c.W+b-1, True): (mode,b) for mode in c.MODES for b in range(4,c.W+1)}
failures = 0
for domain, shape in caps:
    for L, left_data in left.items():
        for R, right_data in right.items():
            degrees = {op % c.W + 1 for a,b,op in domain if L>>a&1 and R>>b&1}
            if len(degrees) >= 2:
                continue
            if failures < 20:
                print('FAIL',shape,left_data,right_data,sorted(degrees))
            failures += 1
print('tests', len(caps)*len(left)*len(right), 'failures', failures)
