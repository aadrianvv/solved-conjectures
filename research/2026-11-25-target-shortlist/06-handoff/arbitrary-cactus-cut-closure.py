from collections import deque
from itertools import combinations_with_replacement, permutations
import importlib.util
import json
from pathlib import Path
import sys

import cactus_cut_closure as core

BASE=Path(__file__).parent
WIDTH=20
core.W=WIDTH
core.COLORS=range(3)

def unpack_caps(arity):
    source=BASE/f'all-cactus-domains-{arity}.json'
    caps=[]
    for domain,structure in json.loads(source.read_text()):
        local=set()
        for parts,counts in domain:
            for rename in permutations(range(3)):
                multiset=[]
                for color,(size,degree) in enumerate(zip(parts,counts)):
                    multiset.extend([WIDTH*rename[color]+degree-1]*size)
                local.update(permutations(multiset))
        caps.append((frozenset(local),structure))
    return caps

def normalize_arcs(caps):
    scalar={}
    for domain,structure in caps:
        core.insert(core.project_pair(domain),structure,scalar)
    long={}
    todo=deque()
    for a,seed in scalar.items():
        for b,next in scalar.items():
            r=core.compose(a,b)
            if core.insert(r,(seed,next),long):todo.append(r)
    while todo:
        a=todo.popleft()
        if a not in long:continue
        for b,next in scalar.items():
            r=core.compose(a,b)
            if core.insert(r,long[a]+(next,),long):todo.append(r)
    def outside(profile):
        result=[]
        for mask in profile:
            out=0
            for u in range(WIDTH):
                for v in range(WIDTH):
                    if any(i!=u and core.row(mask,i)&~(1<<v) for i in range(WIDTH)):
                        out|=core.pack(u+1,v+1)
            result.append(out)
        return tuple(result)
    def symmetrize(mask):
        return mask|sum(
            core.pack(j+1,i+1)
            for i in range(WIDTH) for j in range(WIDTH)
            if mask&core.pack(i+1,j+1)
        )
    independent_modes={}
    original_perm=core.permits
    valid_petal_modes=[]
    for m in (3,4):
        eq=0
        diff=0
        for i in range(1,WIDTH+1):
            if i>=2 and original_perm(m,i-1,i-1):
                eq|=core.pack(i,i)
            for j in range(1,WIDTH+1):
                if original_perm(m,i-1,WIDTH+j-1):diff|=core.pack(i,j)
        valid_petal_modes.append((eq,diff))
    for p,rep in long.items():
        relation=outside(p)
        sym=tuple(symmetrize(m) for m in relation)
        if not any(core.contains(base,sym) for base in valid_petal_modes):
            print('NESTED PETAL BLOCKS TRIANGLE/SQUARE NORMALIZATION',rep,flush=True)
            raise SystemExit(1)
        core.insert(relation,rep,independent_modes)
    for p,rep in scalar.items():
        core.insert(outside(p),(rep,),independent_modes)
    raw=(sum(core.pack(i,j) for i in range(1,WIDTH+1) for j in range(1,WIDTH+1) if i!=j),0)
    all_modes=[raw,*independent_modes]
    representatives=[('direct',),*independent_modes.values()]
    def predicate(mode,x,y):
        c,d=divmod(x,WIDTH)
        e,f=divmod(y,WIDTH)
        return bool(all_modes[mode][c!=e]&core.pack(d+1,f+1))
    core.permits=predicate
    core.MODES=tuple(range(len(all_modes)))
    print('arcs normalized',len(scalar),len(long),len(all_modes),representatives,flush=True)
    return scalar

def cyclic_roots(cap3):
    frontier={}
    for a,b in combinations_with_replacement(core.MODES,2):
        if a==b==0:continue
        for left,l in cap3:
            for right,r in cap3:
                core.insert(core.route(left,right,a,b),('cycle',a,b,l,r),frontier)
        print('cycle modes',a,b,'minimal',len(frontier),flush=True)
    return frontier

def try_all_joins(one,two):
    current={(False,True):one,(True,False):two,(False,False):{},(True,True):{}}
    queue=deque((key,s,tag) for key,d in current.items() for s,tag in d.items())
    trials=0
    while queue:
        group,left,tag=queue.popleft()
        if left not in current[group]:continue
        for kind,right,context in [(k,s,tag) for k,d in current.items() for s,tag in d.items()]:
            if (kind[0] or group[0]) and not(kind[1] and group[1]) and not core.compatible(left,right):
                print('INCOMPATIBLE JOIN',tag,context,core.text_profile(left),core.text_profile(right),flush=True)
                raise SystemExit(1)
            destination=(kind[0] or group[0],False)
            for a,b,story in ((left,right,('series',tag,context)),(right,left,('series',context,tag))):
                trials+=1
                product=core.compose(a,b)
                if core.insert(product,story,current[destination]):
                    queue.append((destination,product,story))
    print('all bridge joins verified',trials,{k:len(v) for k,v in current.items()},flush=True)

def main():
    caps2=unpack_caps(2)
    caps3=unpack_caps(3)
    scalar=normalize_arcs(caps2)
    through=cyclic_roots(caps3)
    try_all_joins(scalar,through)

if __name__=='__main__':main()

