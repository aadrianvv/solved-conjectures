from collections import deque
from functools import cache
from itertools import combinations_with_replacement, permutations, product

W=15
COLORS=range(3)
MODES=(1,2,3,4,7)
PERMS=tuple(permutations(COLORS))

def pack(x,y):return 1<<((x-1)*W+y-1)

def contains(a,b):
    return all(x&~y==0 for x,y in zip(a,b))

def dominates(domain,catalog):
    return any(old<=domain for old in catalog)

def symbols(arity,counts):
    q=sum(counts)
    result=set()
    # Canonical partitions of the port colours; expand the same six
    # renamings after the degree-bucket checks.
    for port in product(COLORS,repeat=arity):
        seen=set()
        canonical=True
        for c in port:
            if c not in seen and c!=len(seen):
                canonical=False
                break
            seen.add(c)
        if not canonical:continue
        base=tuple(port.count(c) for c in COLORS)
        for a in range(q+1):
            for b in range(q-a+1):
                n=(a,b,q-a-b)
                degrees=tuple(x+y for x,y in zip(n,base))
                if any(counts[i-1]>q-sum(n[c] for c in COLORS if degrees[c]==i)
                       for i in range(1,4)):continue
                for relabel in PERMS:
                    result.add(tuple(W*relabel[c]+degrees[c]-1 for c in port))
    return frozenset(result)

def cap_domains(arity):
    frontier={}
    for q in range(12):
        for a in range(q+1):
            for b in range(q-a+1):
                counts=(a,b,q-a-b)
                domain=symbols(arity,counts)
                if dominates(domain,frontier):continue
                for old in list(frontier):
                    if domain<=old:del frontier[old]
                frontier[domain]=counts
    return list(frontier.items())

def permits(kind,x,y):
    c,a=divmod(x,W)
    d,b=divmod(y,W)
    a+=1;b+=1
    if kind==1:return c==d and a!=b
    if kind==2:return (a!=2 and b!=2) if c==d else (a!=1 and b!=1)
    if kind==3:return c!=d and (a,b) not in ((1,1),(2,2))
    if kind==4:return (a!=1 and b!=1) or (c!=d and a!=2 and b!=2)
    if kind==7:return c==d or (a,b) not in ((1,1),(3,3))
    raise AssertionError(kind)

def project_pair(domain):
    out=[0,0]
    for x,y in domain:
        a,b=divmod(x,W),divmod(y,W)
        out[a[0]!=b[0]]|=pack(a[1]+1,b[1]+1)
    return tuple(out)

def insert(r,word,state):
    if any(contains(old,r) for old in state):return False
    for old in list(state):
        if contains(r,old):del state[old]
    state[r]=word
    return True

def petty(rank):
    result={}
    for domain,types in rank:
        for mode in (3,4):
            r=project_pair((x,y) for x,y,a,b in domain if permits(mode,a,b))
            insert(r,(mode,types),result)
    return result

@cache
def placement(domain,external_color,kind_a,kind_b):
    s=tuple((p,u,v) for p,u,v in domain if p//W==external_color)
    a=[0]*(3*W);b=[0]*(3*W);counts=[0]*W
    pairs_a=[tuple(x for x in range(3*W) if permits(kind_a,x,y)) for y in range(3*W)]
    pairs_b=[tuple(x for x in range(3*W) if permits(kind_b,x,y)) for y in range(3*W)]
    for i,(p,u,v) in enumerate(s):
        mark=1<<i
        for x in pairs_a[u]:a[x]|=mark
        for y in pairs_b[v]:b[y]|=mark
        counts[p%W]|=mark
    return a,b,counts

def route(left,right,one,two):
    out=[]
    for target_color in (0,1):
        a,b,degrees=placement(right,target_color,one,two)
        through=[0]*W
        for p,u,v in left:
            if p<W:through[p]|=a[u]&b[v]
        relation=0
        for i,reachable in enumerate(through):
            if not reachable:continue
            for j,degree in enumerate(degrees):
                if reachable&degree:relation|=pack(i+1,j+1)
        out.append(relation)
    return tuple(out)

def row(mask,i):return (mask>>(W*i))&((1<<W)-1)

def join(a,b):
    result=0
    for i in range(W):
        aa=row(a,i)
        if aa:
            reach=0
            for j in range(W):
                if aa&~(1<<j):reach|=row(b,j)
            result|=reach<<(W*i)
    return result

def compose(a,b):
    xe,xd=a
    ye,yd=b
    both=join(xd,yd)
    return join(xe,ye)|both,join(xe,yd)|join(xd,ye)|both

def compatible(a,b):
    for x,y in zip(a,b):
        for i in range(W):
            for j in range(W):
                if x&pack(i+1,j+1):
                    for k in range(W):
                        if i!=k and row(y,k)&~(1<<j):return True
    return False

def text_profile(r):
    return [[(i+1,j+1) for i in range(W) for j in range(W) if mask&pack(i+1,j+1)] for mask in r]

def main():
    domains=[None,None]+[cap_domains(t) for t in (2,3,4)]
    print('local minimal domains',*(len(d) for d in domains[2:]),flush=True)
    same_root={}
    for domain,counts in domains[2]:
        insert(project_pair(domain),('junction',counts),same_root)
    for r,w in petty(domains[4]).items():insert(r,('petal',w),same_root)
    print('single coincident modules',len(same_root),flush=True)
    route_cycle={}
    for one,two in combinations_with_replacement(MODES,2):
        if one==two==1:continue
        for l,lc in domains[3]:
            for r,rc in domains[3]:
                modes=route(l,r,one,two)
                insert(modes,('cycle',one,two,lc,rc),route_cycle)
        print('paths complete',one,two,'route minima',len(route_cycle),flush=True)
    state={(False,True):same_root,(True,False):route_cycle,
           (False,False):{},(True,True):{}}
    queue=deque((flag,mode,word) for flag,t in state.items() for mode,word in t.items())
    tests=0
    while queue:
        kind,here,word=queue.popleft()
        if here not in state[kind]:continue
        all_now=[(t,mode,w) for t,d in state.items() for mode,w in d.items()]
        for side,other,description in all_now:
            if (kind[0] or side[0]) and not(kind[1] and side[1]) and not compatible(here,other):
                print('INCOMPATIBLE!',word,description,text_profile(here),text_profile(other),flush=True)
                return
            outcome=(kind[0] or side[0],False)
            for a,b,record in ((here,other,('series',word,description)),(other,here,('series',description,word))):
                tests+=1
                composed=compose(a,b)
                if insert(composed,record,state[outcome]):
                    queue.append((outcome,composed,record))
    print('complete closure',tests,{k:len(v) for k,v in state.items()},flush=True)
    for kind,t in state.items():
        for r,w in t.items():print(kind,w,text_profile(r))

if __name__=='__main__':main()

