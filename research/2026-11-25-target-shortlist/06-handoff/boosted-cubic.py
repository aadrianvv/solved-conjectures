from affine_cubic import cubic_graph, standard_graph, center_type
from collections import deque
from itertools import combinations, product
from random import Random

COLORS=range(3)

def orient_centers(graph,sinks,source):
    outer=set(range(len(graph)))-sinks
    centers=[tuple(u for u in row if u in outer) for row in graph]
    parents={}
    cycles=[]
    while outer:
        start=next(iter(outer))
        stack=[start]; outer.remove(start)
        component={start}
        while stack:
            v=stack.pop()
            for u in centers[v]:
                if u in outer:
                    outer.remove(u);stack.append(u);component.add(u)
        if source in component:
            parents[source]=None
            seeds=[source]
        else:
            degree={v:len(centers[v]) for v in component}
            leaves=[v for v in component if degree[v]==1]
            while leaves:
                v=leaves.pop()
                for u in centers[v]:
                    if degree[u]>0:
                        degree[u]-=1
                        if degree[u]==1:leaves.append(u)
                degree[v]=0
            core={v for v in component if degree[v]==2}
            v=min(core)
            first=v
            prev=None
            ring=[]
            while True:
                ring.append(v)
                neighbor=min(u for u in centers[v] if u in core and u!=prev)
                if neighbor==first:break
                prev,v=v,neighbor
            cycles.append(tuple(ring));seeds=list(core)
        marked=set(seeds)
        stack=list(seeds)
        while stack:
            v=stack.pop()
            for u in centers[v]:
                if u not in marked:
                    marked.add(u)
                    parents[u]=v
                    stack.append(u)
    for switches in product((1,-1),repeat=len(cycles)):
        out=dict(parents)
        for ring,step in zip(cycles,switches):
            for i,v in enumerate(ring):
                out[v]=ring[(i+step)%len(ring)]
        yield out

def boosted_labels(graph,sinks,source,parent):
    n=len(graph)
    centers=tuple(sorted(parent))
    conditions=[]
    table_edge2=tuple((1<<a,1<<b) for a,b in product(COLORS,repeat=2) if a!=b)
    table_edge3=tuple((1<<a,1<<b,1<<c) for a,b,c in product(COLORS,repeat=3)
                      if not(a==b==c))
    for v in centers:
        p=parent[v]
        if p is None:continue
        gp=parent[p]
        if gp is None:
            conditions.append(((p,v),table_edge2))
        else:
            conditions.append(((gp,p,v),table_edge3))
    for s in sinks:
        neighbors=graph[s]
        scope=tuple(dict.fromkeys((*neighbors,*(parent[v] for v in neighbors if parent[v] is not None))))
        indexes=tuple(scope.index(v) for v in neighbors)
        upstream=tuple(scope.index(parent[v]) if parent[v] is not None else -1 for v in neighbors)
        demands=[]
        for assignment in product(COLORS,repeat=len(scope)):
            local=tuple(assignment[i] for i in indexes)
            needed=tuple(local.count(c) for c in local)
            actual=tuple(
                (3 if j<0 else 2+(assignment[i]==assignment[j]))
                for i,j in zip(indexes,upstream)
            )
            if all(a!=b for a,b in zip(needed,actual)):
                demands.append(tuple(1<<c for c in assignment))
        conditions.append((scope,tuple(demands)))
    incident=[[] for _ in range(n)]
    for i,(where,_) in enumerate(conditions):
        for v in where:incident[v].append(i)
    initial=[7]*n
    initial[centers[0]]=1
    def dfs(domains,check):
        work=set(check)
        while work:
            which=work.pop()
            scope,allowed=conditions[which]
            current=tuple(domains[v] for v in scope)
            keeps=[0]*len(scope)
            for witness in allowed:
                if all(a&b for a,b in zip(current,witness)):
                    for i,c in enumerate(witness):keeps[i]|=c
            for v,k in zip(scope,keeps):
                if k==0:return
                if k!=domains[v]:
                    domains[v]=k
                    work.update(incident[v])
        candidates=[(domains[v].bit_count(),-len(incident[v]),v)
                    for v in centers if domains[v].bit_count()>1]
        if not candidates:return domains
        _,_,v=min(candidates)
        for c in (1,2,4):
            if c&domains[v]:
                trial=list(domains)
                trial[v]=c
                good=dfs(trial,incident[v])
                if good is not None:return good
    answer=dfs(initial,range(len(conditions)))
    if answer is None:return
    witness={}
    for v in centers:
        for u in graph[v]:
            if u in sinks or parent[u]==v:witness[tuple(sorted((u,v)))]=answer[v]
    assert len(witness)==3*n//2
    saturated=[[0]*3 for _ in graph]
    for (u,v),b in witness.items():
        color=b.bit_length()-1
        saturated[u][color]+=1;saturated[v][color]+=1
    assert all(saturated[u][c.bit_length()-1]!=saturated[v][c.bit_length()-1]
               for (u,v),c in witness.items())
    return witness

def exact_test(graph):
    n=len(graph)
    failures=0
    for raw in combinations(range(n),(n+2*(n%4!=0))//4):
        sinks=set(raw)
        if any(u in sinks for v in sinks for u in graph[v]):continue
        sources=(None,) if n%4==0 else [v for v in range(n) if v not in sinks]
        for root in sources:
            if not center_type(graph,sinks,root):continue
            for parent in orient_centers(graph,sinks,root):
                answer=boosted_labels(graph,sinks,root,parent)
                if answer is not None:return answer,failures
                failures+=1
    return None,failures

def main():
    for kind,size in [('complete',4),('prism',6),('prism',8),('petersen',10),('prism',12)]:
        found,fails=exact_test(standard_graph(size,kind))
        print(kind,size,found is not None,fails,flush=True)
    rng=Random(20261125)
    for size in (10,12,14,16,18):
        failures=0
        for i in range(300):
            graph=cubic_graph(size,rng)
            answer,tried=exact_test(graph)
            failures+=tried
            if answer is None:
                print('NO MONOCHROME-TAIL ORIENTATION',size,graph,tried,flush=True)
                return
        print('relaxed cubic size',size,'passed',300,'failed fixed choices',failures,flush=True)

if __name__=='__main__':main()


