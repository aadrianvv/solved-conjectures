from collections import deque
from itertools import combinations_with_replacement
from pathlib import Path
import importlib.util

BASE=Path(__file__).parent

def read_module(name,filename):
    spec=importlib.util.spec_from_file_location(name,BASE/filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

base=read_module('all_caps','arbitrary-cactus-cut-closure.py')
shared=read_module('shared_steps','shared-cycle-cut-closure.py')
core=base.core


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
    width=3*base.WIDTH
    for mode in core.MODES:
        compatible=tuple(
            frozenset(y for y in range(width) if core.permits(mode,x,y))
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
    shared.W=base.WIDTH
    shared.MODES=core.MODES
    shared.permits=core.permits
    symbols,index=shared.pair_spaces(caps3,caps4)
    print('arbitrary cactus pair alphabet',len(symbols),flush=True)
    first={}
    middle={}
    last={}
    for d,record in caps3:
        core.insert(shared.first_matrix(d,index),record,first)
        pair=tuple(shared.last_matrix(d,index,c) for c in (0,1))
        core.insert(pair[0]+pair[1],record,last)
    for d,record in caps4:
        core.insert(shared.middle_matrix(d,index),record,middle)
    links={}
    axes=link_axes(symbols)
    for a,b in combinations_with_replacement(core.MODES,2):
        if a==b==0:continue
        core.insert(tuple(axes[a][0][x] & axes[b][1][y] for x,y in symbols),(a,b),links)
    print('matrices first, middle, last, link',*(len(x) for x in (first,middle,last,links)),flush=True)
    queue=deque()
    jobs={}
    solve=fast_product
    for r,initial in first.items():
        for link,paths in links.items():
            ready=solve(r,link)
            if core.insert(ready,(initial,paths),jobs):queue.append(ready)
    print('initial incidence matrices',len(jobs),flush=True)
    runs=0
    records=0
    while queue:
        old=queue.popleft()
        if old not in jobs:continue
        record=jobs[old]
        shell={}
        for d,description in middle.items():
            core.insert(solve(old,d),description,shell)
        for r,d in shell.items():
            for link,paths in links.items():
                ready=solve(r,link)
                runs+=1
                if core.insert(ready,record+(d,paths),jobs):queue.append(ready)
        records+=1
        if records%10==0:
            print('cactus incidence status',records,runs,len(jobs),len(queue),flush=True)
    print('cactus cycle closure',runs,len(jobs),flush=True)
    shared.relational_product=fast_product
    through={}
    for final,desc in last.items():
        end=(final[:len(symbols)],final[len(symbols):])
        for r,history in jobs.items():
            core.insert(shared.output_relation(r,end),('chain',history,desc),through)
    print('whole cactus traversed components',len(through),flush=True)
    return through

def main():
    cap2=base.unpack_caps(2)
    cap3=base.unpack_caps(3)
    cap4=base.unpack_caps(4)
    scalar=base.normalize_arcs(cap2)
    through=initial_and_step(cap3,cap4)
    base.try_all_joins(scalar,through)

if __name__=='__main__':main()
