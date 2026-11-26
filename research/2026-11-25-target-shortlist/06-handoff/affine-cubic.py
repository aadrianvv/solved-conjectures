from collections import deque
from itertools import combinations, product
from random import Random

PALETTE=7

def cubic_graph(n,rng):
    stubs=[v for v in range(n) for _ in range(3)]
    while True:
        rng.shuffle(stubs)
        edges=set()
        bad=False
        for start in range(0,3*n,2):
            a,b=sorted(stubs[start:start+2])
            if a==b or (a,b) in edges:
                bad=True
                break
            edges.add((a,b))
        if not bad:
            graph=[set() for _ in range(n)]
            for a,b in edges:
                graph[a].add(b)
                graph[b].add(a)
            found={0}
            todo=[0]
            while todo:
                v=todo.pop()
                new=graph[v]-found
                todo.extend(new)
                found.update(new)
            if len(found)==n:
                return tuple(tuple(sorted(row)) for row in graph)

def standard_graph(n,name):
    edges=set()
    def add(a,b):
        edges.add(tuple(sorted((a,b))))
    if name=="complete":
        for a,b in combinations(range(n),2):
            add(a,b)
    else:
        h=n//2
        for a in range(h):
            add(a,(a+1)%h)
            add(a,a+h)
            step=2 if name=="petersen" else 1
            add(a+h,(a+step)%h+h)
    return tuple(tuple(v if u==a else u for u,v in sorted(edges) if a in (u,v)) for a in range(n))

def masks_for_constraint(kind):
    if kind==2:
        return tuple((1<<a,1<<b) for a,b in product(range(3),repeat=2) if a!=b)
    return tuple(
        (1<<a,1<<b,1<<c)
        for a,b,c in product(range(3),repeat=3)
        if (a+b+c)%3==0 and (kind==3 or len({a,b,c})==3)
    )

TABLES={kind:masks_for_constraint(kind) for kind in (2,3,4)}

def affine_label(graph,sinks,source=None):
    n=len(graph)
    active=tuple(v for v in range(n) if v not in sinks)
    constraints=[]
    for v in active:
        for u in graph[v]:
            if v<u and u not in sinks:
                constraints.append(((v,u),2))
    for s in sinks:
        constraints.append((graph[s],4 if source in graph[s] else 3))
    incident=[[] for _ in range(n)]
    for slot,(group,_) in enumerate(constraints):
        for v in group:
            incident[v].append(slot)
    initial=[PALETTE]*n
    initial[active[0]]=1
    def dfs(domains,work):
        pending=set(work)
        while pending:
            j=pending.pop()
            scope,kind=constraints[j]
            supports=[0]*len(scope)
            for record in TABLES[kind]:
                if all(domains[v]&c for v,c in zip(scope,record)):
                    for i,c in enumerate(record):supports[i]|=c
            for v,supported in zip(scope,supports):
                if not supported:
                    return None
                if supported!=domains[v]:
                    domains[v]=supported
                    pending.update(incident[v])
        choices=[(domains[v].bit_count(),-len(incident[v]),v) for v in active if domains[v].bit_count()>1]
        if not choices:return domains
        _,_,v=min(choices)
        for d in (1,2,4):
            if d&domains[v]:
                branch=list(domains)
                branch[v]=d
                out=dfs(branch,incident[v])
                if out is not None:return out
        return None
    return dfs(initial,range(len(constraints)))

def center_type(graph,sinks,source=None):
    active=set(range(len(graph)))-sinks
    while active:
        first=next(iter(active))
        work=[first]
        active.remove(first)
        m2=0
        n=0
        has_source=False
        while work:
            v=work.pop()
            n+=1
            if v==source:has_source=True
            for u in graph[v]:
                if u in sinks:continue
                m2+=1
                if u in active:
                    active.remove(u);work.append(u)
        if m2!=2*(n-has_source):return False
    return True

def exact_test(graph):
    n=len(graph)
    first_failure=None
    faults=0
    for choice in combinations(range(n),(n+2*(n%4!=0))//4):
        sinks=set(choice)
        if any(u in sinks for v in sinks for u in graph[v]):continue
        sources=(None,) if n%4==0 else [a for a in range(n) if a not in sinks]
        for root in sources:
            if not center_type(graph,sinks,root):continue
            labels=affine_label(graph,sinks,root)
            if labels is not None:return True,first_failure,faults
            faults+=1
            if first_failure is None:first_failure=(tuple(sorted(sinks)),root)
    return False,first_failure,faults

def main():
    rng=Random(20261125)
    for kind,size in [('complete',4),('prism',6),('prism',8),('petersen',10),('prism',12)]:
        result=exact_test(standard_graph(size,kind))
        print(kind,size,result,flush=True)
    tally=0
    fault_graphs=0
    for size in (10,12,14,16,18,20,22,24):
        for i in range(1000):
            graph=cubic_graph(size,rng)
            status,first,count=exact_test(graph)
            tally+=1
            if not status:
                print("NO AFFINE ORIENTATION",size,graph,"failed configurations",count,flush=True)
                return
            if count:
                fault_graphs+=1
                if fault_graphs==1:
                    print("nonworking fixed orientation",size,graph,first,flush=True)
        print("affine cubic size",size,"tested",tally,"having a failed first orientation",fault_graphs,flush=True)

if __name__=='__main__':main()


