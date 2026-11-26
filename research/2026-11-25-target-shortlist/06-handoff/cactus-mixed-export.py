"""Exact finite checker for the two-cactus-side theorem.

The mathematical reduction in the research note establishes the finite
junction bounds and reduces all private cycles to triangles or squares.
Every relation here uses a three-color palette and exact monochromatic degrees.
"""
from itertools import combinations_with_replacement, permutations

from collections import deque
from functools import cache
from itertools import product

W=20
PALETTE=range(3)

def binary_sums(old,increments):
    return frozenset(tuple(sum(pair) for pair in zip(a,b))
                     for a in old for b in increments)

@cache
def blossom_use(pattern,triangles,squares):
    if triangles==squares==0:
        return frozenset(((0,0,0),))
    pure=triangles>0
    steps=set()
    for a in PALETTE:
        for b in range(a,3):
            da,db=pattern[a],pattern[b]
            if pure and (a==b or da==db in (1,2)):continue
            if not pure and (a==b and da==1 or a!=b and {da,db}=={1,2}):continue
            steps.add(tuple(int(i==a)+int(i==b) for i in PALETTE))
    if pure:
        return binary_sums(blossom_use(pattern,triangles-1,squares),steps)
    return binary_sums(blossom_use(pattern,triangles,squares-1),steps)

def permitted_extra(buckets,core,triangles,squares,arms):
    extra=tuple(d-k for d,k in zip(buckets,core))
    if min(extra)<0:return False
    group=tuple(d if d in (1,2) else 3 for d in buckets)
    q=sum(arms)
    for use in blossom_use(group,triangles,squares):
        if any(v>n for v,n in zip(use,extra)):continue
        spare=tuple(n-v for n,v in zip(extra,use))
        if all(arms[j-1] <= q-sum(s for s,d in zip(spare,buckets) if d==j)
               for j in (1,2,3)):
            return True
    return False

def has_state(state,cap):
    partition,boundary=state
    triangles,squares,arms=cap
    arity=sum(partition)
    total=arity+2*(triangles+squares)+sum(arms)
    free=total-sum(boundary)
    if free<0:return False
    core=partition+(0,)*(3-len(partition))
    if len(partition)==3:
        return not free and permitted_extra(boundary,core,triangles,squares,arms)
    if len(partition)==2:
        return permitted_extra(boundary+(free,),core,triangles,squares,arms)
    return any(permitted_extra(boundary+(a,free-a),core,triangles,squares,arms)
               for a in range(free//2+1))



def degree_vectors(total,partition,index=0,prefix=()):
    if index==len(partition):
        if len(partition)<3 or total==0:
            yield prefix
        return
    threshold=partition[index]
    if index and partition[index]==partition[index-1]:
        threshold=max(threshold,prefix[-1])
    for first in range(threshold,total-sum(partition[index+1:])+1):
        yield from degree_vectors(total-first,partition,index+1,prefix+(first,))

def variants(arity,cap):
    partitions={
        2:((2,),(1,1)),
        3:((3,),(2,1),(1,1,1)),
        4:((4,),(3,1),(2,2),(2,1,1)),
    }[arity]
    petals,squares,arms=cap
    total=arity+2*(petals+squares)+sum(arms)
    return frozenset((partition,vector)
                     for partition in partitions for vector in degree_vectors(total,partition)
                     if has_state((partition,vector),cap))



TRIANGLE_LIMITS={2:4,3:6,4:7}
def cap_domains_with_petals(arity):
    frontier={}
    for triangles in range(TRIANGLE_LIMITS[arity]):
        # Larger attachments can be restored by degree avoidance after
        # coloring the rest, as explained in the research note.
        free_limit=max(arity,12-2*triangles)
        for squares in range((free_limit-1)//2+1):
            for count in range(free_limit-2*squares):
                for ones in range(count+1):
                    for twos in range(count-ones+1):
                        cap=(triangles,squares,(ones,twos,count-ones-twos))
                        if any(all(has_state(state,cap) for state in profile)
                               for profile in sorted(frontier,key=len)):
                            continue
                        profile=variants(arity,cap)
                        for dominated in tuple(frontier):
                            if profile<=dominated:
                                del frontier[dominated]
                        frontier[profile]=cap
    output=[]
    for profile,cap in frontier.items():
        all_states=set()
        for parts,counts in profile:
            for relabel in permutations(range(3)):
                multiset=[]
                for color,(size,degree) in enumerate(zip(parts,counts)):
                    multiset.extend([W*relabel[color]+degree-1]*size)
                all_states.update(permutations(multiset))
        output.append((frozenset(all_states),cap))
    return output


def pack(x,y):return 1<<((x-1)*W+y-1)

def contains(a,b):
    return all(x&~y==0 for x,y in zip(a,b))



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



def normalize_arcs(caps):
    global permits, MODES, ARC_REPRESENTATIVES
    scalar={}
    for domain,structure in caps:
        insert(project_pair(domain),structure,scalar)
    long={}
    todo=deque()
    for a,seed in scalar.items():
        for b,next in scalar.items():
            r=compose(a,b)
            if insert(r,(seed,next),long):todo.append(r)
    while todo:
        a=todo.popleft()
        if a not in long:continue
        for b,next in scalar.items():
            r=compose(a,b)
            if insert(r,long[a]+(next,),long):todo.append(r)
    def outside(profile):
        result=[]
        for mask in profile:
            out=0
            for u in range(W):
                for v in range(W):
                    if any(i!=u and row(mask,i)&~(1<<v) for i in range(W)):
                        out|=pack(u+1,v+1)
            result.append(out)
        return tuple(result)
    def symmetrize(mask):
        return mask|sum(
            pack(j+1,i+1)
            for i in range(W) for j in range(W)
            if mask&pack(i+1,j+1)
        )
    independent_modes={}
    original_perm=permits
    valid_petal_modes=[]
    for m in (3,4):
        eq=0
        diff=0
        for i in range(1,W+1):
            if i>=2 and original_perm(m,i-1,i-1):
                eq|=pack(i,i)
            for j in range(1,W+1):
                if original_perm(m,i-1,W+j-1):diff|=pack(i,j)
        valid_petal_modes.append((eq,diff))
    for p,rep in long.items():
        relation=outside(p)
        sym=tuple(symmetrize(m) for m in relation)
        if not any(contains(base,sym) for base in valid_petal_modes):
            print('NESTED PETAL BLOCKS TRIANGLE/SQUARE NORMALIZATION',rep,flush=True)
            raise SystemExit(1)
        insert(relation,rep,independent_modes)
    for p,rep in scalar.items():
        insert(outside(p),(rep,),independent_modes)
    raw=(sum(pack(i,j) for i in range(1,W+1) for j in range(1,W+1) if i!=j),0)
    all_modes=[raw,*independent_modes]
    representatives=[('direct',),*independent_modes.values()]
    ARC_REPRESENTATIVES=tuple(representatives)
    def predicate(mode,x,y):
        c,d=divmod(x,W)
        e,f=divmod(y,W)
        return bool(all_modes[mode][c!=e]&pack(d+1,f+1))
    permits=predicate
    MODES=tuple(range(len(all_modes)))
    print('arcs normalized',len(scalar),len(long),len(all_modes),representatives,flush=True)
    return scalar



def pair_spaces(cap3,cap4):
    found=set()
    for domain,_ in cap3:
        found.update((u,v) for _,u,v in domain)
    for domain,_ in cap4:
        found.update((a,b) for a,b,c,d in domain)
        found.update((c,d) for a,b,c,d in domain)
    pairs=tuple(sorted(found))
    return pairs,{pair:i for i,pair in enumerate(pairs)}

def middle_matrix(domain,indices):
    out=[0]*len(indices)
    for a,b,c,d in domain:out[indices[a,b]]|=1<<indices[c,d]
    return tuple(out)

def first_matrix(domain,indices):
    out=[0]*W
    for p,a,b in domain:
        if p<W:out[p]|=1<<indices[a,b]
    return tuple(out)

def last_matrix(domain,indices,color):
    out=[0]*len(indices)
    for p,a,b in domain:
        hue,degree=divmod(p,W)
        if hue==color:out[indices[a,b]]|=1<<degree
    return tuple(out)

def output_relation(history,final):
    return tuple(sum(word<<(W*i) for i,word in enumerate(fast_product(history,table)))
                 for table in final)



def fast_product(left,right):
    highest=0
    for candidate in right:
        highest|=candidate
    cache={0:0}
    out=[]
    for row in left:
        if row not in cache:
            result=0
            bits=row
            while bits and result!=highest:
                bit=bits&-bits
                bits^=bit
                result|=right[bit.bit_length()-1]
            cache[row]=result
        out.append(cache[row])
    return tuple(out)

def link_axes(pair_symbols):
    matrices={}
    width=3*W
    for mode in MODES:
        compatible=tuple(
            frozenset(y for y in range(width) if permits(mode,x,y))
            for x in range(width)
        )
        left=[]
        right=[]
        for x_set in compatible:
            left.append(sum(1<<i for i,(a,b) in enumerate(pair_symbols) if a in x_set))
            right.append(sum(1<<i for i,(a,b) in enumerate(pair_symbols) if b in x_set))
        matrices[mode]=left,right
    return matrices

def initial_and_step(caps3,caps4):
    symbols,index=pair_spaces(caps3,caps4)
    print('arbitrary cactus pair alphabet',len(symbols),flush=True)
    first={}
    middle={}
    last={}
    for d,record in caps3:
        insert(first_matrix(d,index),record,first)
        pair=tuple(last_matrix(d,index,c) for c in (0,1))
        insert(pair[0]+pair[1],record,last)
    for d,record in caps4:
        insert(middle_matrix(d,index),record,middle)
    links={}
    axes=link_axes(symbols)
    for a,b in combinations_with_replacement(MODES,2):
        if a==b==0:continue
        insert(tuple(axes[a][0][x] & axes[b][1][y] for x,y in symbols),(a,b),links)
    print('matrices first, middle, last, link',*(len(x) for x in (first,middle,last,links)),flush=True)
    queue=deque()
    jobs={}
    solve=fast_product
    for r,initial in first.items():
        for link,paths in links.items():
            ready=solve(r,link)
            if insert(ready,(initial,paths),jobs):queue.append(ready)
    print('initial incidence matrices',len(jobs),flush=True)
    runs=0
    records=0
    while queue:
        old=queue.popleft()
        if old not in jobs:continue
        record=jobs[old]
        shell={}
        for d,description in middle.items():
            insert(solve(old,d),description,shell)
        for r,d in shell.items():
            for link,paths in links.items():
                ready=solve(r,link)
                runs+=1
                if insert(ready,record+(d,paths),jobs):queue.append(ready)
        records+=1
        if records%10==0:
            print('cactus incidence status',records,runs,len(jobs),len(queue),flush=True)
    print('cactus cycle closure',runs,len(jobs),flush=True)
    through={}
    for final,desc in last.items():
        end=(final[:len(symbols)],final[len(symbols):])
        for r,history in jobs.items():
            insert(output_relation(r,end),('chain',history,desc),through)
    print('whole cactus traversed components',len(through),flush=True)
    return through




def junction_vertices(description):
    triangles,squares,arms=description
    return 1+2*triangles+3*squares+arms[0]+2*arms[1]+5*arms[2]

def connector_vertices(mode):
    atoms=ARC_REPRESENTATIVES[mode]
    if atoms==('direct',):
        return 0
    return sum(junction_vertices(d) for d in atoms)

def representative_vertices(tag):
    if tag[0]=='series':
        return representative_vertices(tag[1])+representative_vertices(tag[2])
    if tag[0]=='chain':
        history=tag[1]
        end=tag[2]
        return (sum(junction_vertices(d) for d in history[::2])
                + junction_vertices(end)
                + sum(connector_vertices(m) for pair in history[1::2] for m in pair))
    return junction_vertices(tag)

def try_all_joins(one,two):
    current={(False,True):one,(True,False):two,(False,False):{},(True,True):{}}
    queue=deque((key,s,tag) for key,d in current.items() for s,tag in d.items())
    trials=0
    while queue:
        group,left,tag=queue.popleft()
        if left not in current[group]:continue
        for kind,right,context in [(k,s,tag) for k,d in current.items() for s,tag in d.items()]:
            if (kind[0] or group[0]) and not(kind[1] and group[1]) and not compatible(left,right):
                print('INCOMPATIBLE JOIN',tag,context,text_profile(left),text_profile(right),flush=True)
                raise SystemExit(1)
            destination=(kind[0] or group[0],False)
            for a,b,story in ((left,right,('series',tag,context)),(right,left,('series',context,tag))):
                trials+=1
                product=compose(a,b)
                if insert(product,story,current[destination]):
                    queue.append((destination,product,story))
    print('all bridge joins verified',trials,{k:len(v) for k,v in current.items()},flush=True)
    for flags,domain in current.items():
        sizes=tuple(representative_vertices(tag) for tag in domain.values())
        if sizes:
            print("prototype sizes", flags, min(sizes), max(sizes), flush=True)




    import json
    from pathlib import Path
    rows=[]
    catalog=[]
    for flags,domain in current.items():
        for relation,tag in domain.items():
            values=[]
            for orbit in relation:
                allowed=0
                for i in range(1,9):
                    for j in range(1,9):
                        if any(
                            old_i!=i and row(orbit,old_i-1)&~(1<<(j-1))
                            for old_i in range(1,W+1)
                        ):
                            allowed|=1<<((i-1)*8+j-1)
                values.append(allowed)
            ordinal=len(catalog)
            catalog.append([flags,tag])
            rows.append(' '.join((str(ordinal),str(int(flags[1])),format(values[0],'x'),format(values[1],'x'))))
    folder=Path(__file__).parent
    (folder/'cactus-pair-probes.txt').write_text('\n'.join(rows)+'\n')
    (folder/'cactus-pair-representatives.json').write_text(json.dumps([ARC_REPRESENTATIVES,catalog]))

def main():
    caps=[cap_domains_with_petals(arity) for arity in (2,3,4)]
    counts=tuple(map(len,caps))
    print('junction domain counts',counts,flush=True)
    assert counts==(8,44,83)
    coincident=normalize_arcs(caps[0])
    traversed=initial_and_step(caps[1],caps[2])
    try_all_joins(coincident,traversed)

if __name__=='__main__':
    main()

