from itertools import product

symbols=tuple(product(range(3),range(1,3)))
allbits=(1<<len(symbols))-1

def relation(pred):
    return tuple(sum(1<<j for j,y in enumerate(symbols) if pred(x,y)) for x in symbols)

def compose(A,B):
    return tuple(sum_product(B,row) for row in A)

def sum_product(B,choices):
    result=0
    for i,row in enumerate(B):
        if choices&(1<<i):result|=row
    return result

def matrix_contains(A,B):
    return all(x&~y==0 for x,y in zip(A,B))

def bits_allowed(pred):
    return sum(1<<i for i,x in enumerate(symbols) if pred(x))

def node(a):
    def allow(x,y):
        cx,dx=x
        cy,dy=y
        if cx==a and cy==a:return False
        cxdeg=1+(cx==cy)+(cx==a)
        cydeg=1+(cy==cx)+(cy==a)
        return cxdeg==dx and cydeg==dy
    return relation(allow)

def connector(length):
    def allow(x,y):
        c,a=x
        d,b=y
        if length==2:return (a==b==1 and c==d) or (a==b==2 and c!=d)
        if length==3:return c!=d and a!=b
        return (a==b==2) or (a==b==1 and c!=d)
    return relation(allow)

def endpoint_sets(a):
    # A triangle with one exterior edge; a pendant of type 1 or 2;
    # a link to a high neighbour of given main colour (count at least 3).
    patterns={bits_allowed(lambda x:x[0]!=a):'triangle or odd pendant'}
    patterns[bits_allowed(lambda x:(x[0]==a)==(x[1]==2))]='even pendant'
    for c in range(3):
        for kind in range(2,5):
            def external(x):
                k,d=x
                if kind==2:return (d==1)==(k==c)
                if kind==3:return k!=c
                return k!=c or d==2
            arm=bits_allowed(external)
            # drop either slot at this low head, then project onto other
            possible=0
            for s,opts in enumerate(node(a)):
                if arm&opts:possible|=1<<s
            patterns[possible]=f'length-{kind} to high color {c}'
    return patterns

leftsets=[endpoint_sets(a) for a in range(3)]
print('endpoint set sizes',[[x.bit_count() for x in a] for a in leftsets])
for a,b,d in product(range(3),range(3),range(2,5)):
    for x,y in product(leftsets[a],leftsets[b]):
        if not(sum_product(connector(d),x)&y):
            print('single low edge blocked',a,b,d,leftsets[a][x],leftsets[b][y])

# Track minimal products, inducing arbitrary paths of low hubs and
# arbitrary cycles once we take the trace.
import collections
nodes=[node(a) for a in range(3)]
links=[connector(l) for l in range(2,5)]
bases={}
for a,l in product(range(3),range(3)):
    bases[compose(nodes[a],links[l])]=(a,l+2)
minimal={}
queue=collections.deque()
for x,y in product(bases,bases):
    r=compose(x,y)
    if any(matrix_contains(old,r) for old in minimal):continue
    for old in tuple(minimal):
        if matrix_contains(r,old):del minimal[old]
    minimal[r]=(bases[x],bases[y])
    queue.append(r)
while queue:
    r=queue.popleft()
    if r not in minimal:continue
    for a in bases:
        z=compose(r,a)
        if any(matrix_contains(old,z) for old in minimal):continue
        for old in tuple(minimal):
            if matrix_contains(z,old):del minimal[old]
        minimal[z]=(*minimal[r],bases[a])
        queue.append(z)
print('final cyclic matrix minima',len(minimal))
for r,w in minimal.items():
    if not any(row&(1<<i) for i,row in enumerate(r)):
        print('cycle blocked',w,r)

