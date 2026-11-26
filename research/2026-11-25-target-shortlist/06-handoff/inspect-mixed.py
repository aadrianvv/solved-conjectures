import json
from pathlib import Path
root = Path(__file__).parent
_, groups = json.loads((root / 'cactus-pair-representatives.json').read_text())
rows = [(int(i), int(c), int(e,16), int(d,16)) for i,c,e,d in (line.split() for line in (root/'cactus-pair-probes.txt').read_text().splitlines())]
def bad(mask):
    return [(i//8+1,i%8+1) for i in range(64) if mask>>i&1==0]
for want_distinct in (False,True):
    active=[]
    for row in rows:
        i,c,e,d=row
        if c and want_distinct: continue
        if any(pe&~e==pd&~d==0 for _,_,pe,pd in active): continue
        active=[p for p in active if not(e&~p[2]==d&~p[3]==0)]
        active.append(row)
    print('only distinct' if want_distinct else 'all')
    for i,c,e,d in active:
        print(i,c,bad(e),bad(d))
        print('       ',groups[i])
