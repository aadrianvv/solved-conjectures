import full_cactus as c

def swap(mask):
    return sum(c.pack(b,a) for a in range(1,c.W+1) for b in range(1,c.W+1)
               if mask & c.pack(a,b))

def test(families):
    triangle=(0,sum(c.pack(a,b)
                    for a in range(1,c.W+1) for b in range(1,c.W+1) if not (a==b in (1,2))))
    square=(sum(c.pack(a,a) for a in range(2,c.W+1)),
            sum(c.pack(a,b) for a in range(1,c.W+1) for b in range(1,c.W+1) if (a,b) not in ((1,2),(2,1))))
    count=0
    for (danger,same), domain in families.items():
        if same:
            continue
        for profile, shape in domain.items():
            symmetric = tuple(m | swap(m) for m in c.acceptance_profile(profile))
            assert c.contains(triangle,symmetric) or c.contains(square,symmetric), (danger,shape)
            count+=1
    print('private cactus two-incidence prototypes',count,flush=True)

c.report_minimal_probes=test
c.main()
