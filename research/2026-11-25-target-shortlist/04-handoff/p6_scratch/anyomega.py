"""For random Euler orientations Omega with no cherry both-in (P3-form), test whether a directed 2-factor R of Omega
avoiding every cherry exists (exhaustive over B-trail phases).  Abstract disjoint-target instances."""
import sys
from random import Random
from collections import Counter
from itertools import product
from gadget import rand_gadget
from abstract_rand import cherry_system
def random_euler(k, es, ch, rng, mode, tries=200):
    # random orientation by random search: each vertex out-degree 2; cherries not both-in
    # mode 'cross': every cherry cross; 'any': no cherry both-in
    inc=[[] for _ in range(k)]
    for i,(a,b) in enumerate(es): inc[a].append(i); inc[b].append(i)
    for _ in range(tries):
        # random Euler orientation via random Euler circuit-ish: random walk pairing transitions
        trans={}
        for v in range(k):
            l=inc[v][:]; rng.shuffle(l); trans[(v,l[0])]=l[1]; trans[(v,l[1])]=l[0]; trans[(v,l[2])]=l[3]; trans[(v,l[3])]=l[2]
        head=[None]*len(es)  # orientation: head vertex
        for e0 in range(len(es)):
            if head[e0] is not None: continue
            e=e0; v=es[e0][1] if rng.random()<0.5 else es[e0][0]
            while head[e] is None:
                head[e]=v; e=trans[(v,e)]; a,b=es[e]; v=b if a==v else a
        ok=True
        for x,e1,e2 in ch:
            i1=head[e1]==x; i2=head[e2]==x
            if mode=='cross' and i1==i2: ok=False
            if i1 and i2: ok=False
        if ok: return head
    return None
def colour_exists(k, es, ch, head):
    # B-trails: nodes (v,'out'),(v,'in'); arc e: tail_out -- head_in
    tail=lambda e: es[e][0] if head[e]==es[e][1] else es[e][1]
    ins=[[] for _ in range(k)]; outs=[[] for _ in range(k)]
    for e in range(len(es)): ins[head[e]].append(e); outs[tail(e)].append(e)
    # trail phase: walk
    trail=[None]*len(es); pos=[None]*len(es); nt=0
    for e0 in range(len(es)):
        if trail[e0] is not None: continue
        e=e0; p=0; side='in'
        while trail[e] is None:
            trail[e]=nt; pos[e]=p%2; p+=1
            if side=='in':
                v=head[e]; e=[f for f in ins[v] if f!=e][0]; side='out'
            else:
                v=tail(e); e=[f for f in outs[v] if f!=e][0]; side='in'
        nt+=1
    # R = arcs with pos == phase[trail]
    for ph in product((0,1),repeat=nt):
        inR=lambda e: pos[e]==ph[trail[e]]
        if all(not(inR(e1) and inR(e2)) for x,e1,e2 in ch): return True
    return False
if __name__=="__main__":
    rng=Random(int(sys.argv[1])); T=int(sys.argv[2]); Ns=[int(a) for a in sys.argv[3].split(',')]; mode=sys.argv[4]
    tal=Counter()
    for t in range(T):
        k=rng.choice(Ns); es=rand_gadget(k,rng,ports=0)
        if es is None: continue
        ch=cherry_system(k,es,rng)
        head=random_euler(k,es,ch,rng,mode)
        if head is None: tal['noomega']+=1; continue
        ok=colour_exists(k,es,ch,head)
        tal[(k,ok)]+=1
    print(sorted(tal.items(),key=str))
