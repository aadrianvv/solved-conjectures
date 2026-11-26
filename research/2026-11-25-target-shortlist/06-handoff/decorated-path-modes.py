from itertools import product, combinations_with_replacement
from collections import deque

W=5
MASK=(1<<(W*W))-1
UNIT=(1<<W)-1

def packed(a,b):
    return 1<<(W*(a-1)+b-1)

def row(mask,i):
    return (mask>>(W*i))&UNIT

def compose(a,b):
    out=0
    for i in range(W):
        h=row(a,i)
        if not h: continue
        for j in range(W):
            if h & ~(1<<j): out|=row(b,j)<<(W*i)
    return out

def series(a,b):
    e,d=a
    f,g=b
    both=compose(d,g)
    return (compose(e,f)|both,compose(e,g)|compose(d,f)|both)

def boundary(a):
    shift=0
    for x in range(W):
        for y in range(W):
            if x!=y:shift|=1<<(W*x+y)
    # Compose with equality-colour disequality-degree link via ordinary
    # Boolean multiplication for an already built relation.
    def mult(r,s):
        value=0
        for i in range(W):
            h=row(r,i)
            for j in range(W):
                if h&(1<<j):value|=row(s,j)<<(W*i)
        return value
    return tuple(mult(mult(shift,r),shift) for r in a)

def local(types):
    output=[]
    for same in (True,False):
        colors=(0,0) if same else (0,1)
        valid=0
        for additional in product(range(3),repeat=len(types)):
            full=colors+additional
            degrees=[full.count(i) for i in range(3)]
            if any(t==degrees[c] for t,c in zip(types,additional)):continue
            valid|=packed(degrees[colors[0]],degrees[colors[1]])
        output.append(valid)
    return tuple(output)

def profile(r):
    return tuple(tuple((i+1,j+1) for i in range(W) for j in range(W) if m&packed(i+1,j+1)) for m in r)

def subset(a,b):
    return all((x&~y)==0 for x,y in zip(a,b))

def insert(r,v,table):
    if any(subset(old,r) for old in table):return False
    for old in list(table):
        if subset(r,old):del table[old]
    table[r]=v
    return True

minima={1:{},2:{}}
queue=deque()
for count in range(3):
    for types in combinations_with_replacement(range(3),count):
        r=local(types)
        if insert(r,(types,),minima[1]):queue.append((1,r,(types,)))
while queue:
    idx,r,w=queue.popleft()
    if r not in minima[idx]:continue
    for ar,t,v in [(key,a,b) for key,d in minima.items() for a,b in d.items()]:
        for first,second,ww in ((r,t,w+v),(t,r,v+w)):
            x=series(first,second)
            if insert(x,ww,minima[2]):queue.append((2,x,ww))
print('internal antichains:',*[len(d) for d in minima.values()])
for minimum in (1,2):
    final={}
    for idx,d in minima.items():
        if idx<minimum:continue
        for inner,words in d.items():
            insert(boundary(inner),words,final)
    print('boundary minimum length',minimum+1,'modes',len(final))
    for a,w in final.items():
        print(w,len(profile(a)[0]),len(profile(a)[1]))

