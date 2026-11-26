import sys
from random import Random
from collections import Counter
from gadget import rand_gadget
from abstract_rand import cherry_system
from anyomega import random_euler, colour_exists
rng=Random(int(sys.argv[1])); tal=Counter()
for t in range(int(sys.argv[2])):
    k=rng.choice([8,10,12]); es=rand_gadget(k,rng,ports=0)
    if es is None: continue
    ch=cherry_system(k,es,rng)
    apex=Counter(x for x,_,_ in ch)
    if any(v==2 for v in apex.values()):
        # drop one cherry at each D2 apex to get a no-D2 instance
        seen=set(); ch2=[]
        for c in ch:
            if c[0] in seen and apex[c[0]]==2: continue
            seen.add(c[0]); ch2.append(c)
        ch=ch2
    head=random_euler(k,es,ch,rng,'cross')
    if head is None: tal['noomega']+=1; continue
    tal[(len(ch)>0, colour_exists(k,es,ch,head))]+=1
print(sorted(tal.items(),key=str))
