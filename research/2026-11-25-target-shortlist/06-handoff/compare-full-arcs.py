import full_cactus as check
check.normalize_arcs(check.cap_domains_with_petals(2))
for mode, shape in enumerate(check.ARC_REPRESENTATIVES):
    print(mode,shape)
    for a in [1,2,3,4,5,6,20]:
        print(a,[(b,check.permits(mode,a-1,b-1),check.permits(mode,a-1,check.W+b-1)) for b in [1,2,3,4,5,6,20]])
