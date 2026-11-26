from cactus_cut_closure import *
from functools import cache

def union_rows(table,bits):
    value=0
    while bits:
        bit=bits&-bits
        bits^=bit
        value|=table[bit.bit_length()-1]
    return value

def relational_product(left,right):
    return tuple(union_rows(right,row) for row in left)

def pair_spaces(cap3,cap4):
    found=set()
    for domain,_ in cap3:
        found.update((u,v) for _,u,v in domain)
    for domain,_ in cap4:
        found.update((a,b) for a,b,c,d in domain)
        found.update((c,d) for a,b,c,d in domain)
    pairs=tuple(sorted(found))
    return pairs,{pair:i for i,pair in enumerate(pairs)}

def link_matrix(pairs,first,second):
    out=[]
    for x,y in pairs:
        row=0
        for i,(a,b) in enumerate(pairs):
            if permits(first,x,a) and permits(second,y,b):row|=1<<i
        out.append(row)
    return tuple(out)

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
    return tuple(sum(word<<(W*i) for i,word in enumerate(relational_product(history,table)))
                 for table in final)

def compare_final(seed_domains,petal_domains,through_profiles):
    rooted={}
    for domain,counts in seed_domains:insert(project_pair(domain),('junction',counts),rooted)
    for r,w in petty(petal_domains).items():insert(r,('petal',w),rooted)
    state={(False,True):rooted,(True,False):through_profiles,
           (False,False):{},(True,True):{}}
    queue=deque((flag,mode,word) for flag,t in state.items() for mode,word in t.items())
    attempts=0
    while queue:
        kind,r,word=queue.popleft()
        if r not in state[kind]:continue
        for side,other,description in [(p,key,desc) for p,d in state.items()
                                        for key,desc in d.items()]:
            if (kind[0] or side[0]) and not(kind[1] and side[1]) and not compatible(r,other):
                print('INCOMPATIBLE',word,description,text_profile(r),text_profile(other),flush=True)
                raise SystemExit(1)
            destination=(kind[0] or side[0],False)
            for a,b,record in ((r,other,('series',word,description)),
                                (other,r,('series',description,word))):
                attempts+=1
                composed=compose(a,b)
                if insert(composed,record,state[destination]):
                    queue.append((destination,composed,record))
    print('bridge closure',attempts,{k:len(v) for k,v in state.items()},flush=True)

def main():
    cap2,cap3,cap4=(cap_domains(t) for t in (2,3,4))
    pairs,indices=pair_spaces(cap3,cap4)
    print('pair alphabet',len(pairs),flush=True)
    start={}
    for domain,counts in cap3:
        insert(first_matrix(domain,indices),('first',counts),start)
    mids={}
    for domain,counts in cap4:
        insert(middle_matrix(domain,indices),('middle',counts),mids)
    link_types=tuple((a,b) for a,b in combinations_with_replacement(MODES,2) if (a,b)!=(1,1))
    transitions={}
    ends={}
    for first,second in link_types:
        link=link_matrix(pairs,first,second)
        for state,desc in mids.items():
            insert(relational_product(link,state),(first,second,desc),transitions)
        for domain,counts in cap3:
            final=tuple(relational_product(link,last_matrix(domain,indices,c)) for c in (0,1))
            # These are two matrices on the same pair alphabet. Dominance
            # can be tested in their concatenated lists of rows.
            insert(final[0]+final[1],('end',first,second,counts),ends)
        print('link transitions',first,second,len(transitions),len(ends),flush=True)
    histories={}
    queue=deque()
    for state,begin in start.items():
        for next,choice in transitions.items():
            r=relational_product(state,next)
            if insert(r,(begin,choice),histories):queue.append(r)
    print('first shared-vertex histories',len(histories),flush=True)
    computed=0
    while queue:
        here=queue.popleft()
        if here not in histories:continue
        for step,choice in transitions.items():
            computed+=1
            r=relational_product(here,step)
            if insert(r,(*histories[here],choice),histories):queue.append(r)
        if computed%10000==0:print('history status',computed,len(histories),len(queue),flush=True)
    print('shared-vertex closure',computed,len(histories),flush=True)
    through={}
    for current in (start,histories):
        for profile,begin in current.items():
            for last,choice in ends.items():
                finished=(last[:len(pairs)],last[len(pairs):])
                insert(output_relation(profile,finished),(begin,choice),through)
    print('final through-cycle profiles',len(through),flush=True)
    compare_final(cap2,cap4,through)
if __name__=='__main__':main()

