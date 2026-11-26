from collections import deque
from functools import cache
from itertools import product

W=46
PALETTE=range(3)
TWO_SPOKES=((2,),(1,1))
MAX_PETALS=11

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

def enumerate_domain(cap):
    triangles,squares,arms=cap
    total=2+2*(triangles+squares)+sum(arms)
    out=set()
    for a in range(2,total+1):
        state=((2,),(a,))
        if has_state(state,cap):out.add(state)
    for a in range(1,total//2+1):
        for b in range(a,total-a+1):
            state=((1,1),(a,b))
            if has_state(state,cap):out.add(state)
    return frozenset(out)

def insert_profile(state,cap,table):
    if any(old<=state for old in table):return False
    for old in list(table):
        if state<=old:del table[old]
    table[state]=cap
    return True

def pack(a,b):
    return 1<<((a-1)*W+b-1)

def from_state(domain):
    eq=0
    diff=0
    for p,counts in domain:
        if len(p)==1:
            a,=counts
            eq|=pack(a,a)
        else:
            a,b=counts
            diff|=pack(a,b)|pack(b,a)
    return eq,diff

def row(mask,i):return (mask>>(W*i))&((1<<W)-1)
def mat_compose(a,b):
    res=0
    for i in range(W):
        before=row(a,i)
        if not before:continue
        reach=0
        for j in range(W):
            if before&~(1<<j):reach|=row(b,j)
        res|=reach<<(W*i)
    return res

def combine(a,b):
    aa,ab=a
    ba,bb=b
    both=mat_compose(ab,bb)
    return mat_compose(aa,ba)|both,mat_compose(aa,bb)|mat_compose(ab,ba)|both

def exterior(r):
    out=[]
    for modes in r:
        value=0
        for i in range(W):
            seen=row(modes,i)
            if not seen:continue
            for k in range(W):
                if k==i:continue
                for j in range(W):
                    if seen&~(1<<j):value|=pack(k+1,j+1)
        out.append(value)
    return tuple(out)

def contains(a,b):return all(x&~y==0 for x,y in zip(a,b))

def put_relation(r,representative,table):
    if any(contains(x,r) for x in table):return False
    for x in list(table):
        if contains(r,x):del table[x]
    table[r]=representative
    return True

def main():
    frontier={}
    checked=0
    expanded=0
    for p3 in range(12):
        for p4 in range(7):
            for q in range(14-2*p4):
                for a in range(q+1):
                    for b in range(q-a+1):
                        cap=(p3,p4,(a,b,q-a-b))
                        checked+=1
                        if any(all(has_state(state,cap) for state in p)
                               for p in sorted(frontier,key=len)):
                            continue
                        expanded+=1
                        insert_profile(enumerate_domain(cap),cap,frontier)
        print('triangle count done',p3,'caps',checked,'exact new',expanded,'antichain',len(frontier),flush=True)
    singles={from_state(r):c for r,c in frontier.items()}
    long={}
    pending=deque()
    for a,w in singles.items():
        for b,z in singles.items():
            r=combine(a,b)
            if put_relation(r,(w,z),long):pending.append(r)
    while pending:
        a=pending.popleft()
        if a not in long:continue
        for b,w in singles.items():
            r=combine(a,b)
            z=long[a]+(w,)
            if put_relation(r,z,long):pending.append(r)
    print('single and long relation counts',len(singles),len(long),flush=True)
    for source in (singles,long):
        outer={}
        for r,w in source.items():put_relation(exterior(r),w,outer)
        print('exterior profiles',len(outer),list(outer.values()),flush=True)

if __name__=='__main__':main()

