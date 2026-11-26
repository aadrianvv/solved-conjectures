"""(P5) CSP with restricted strategies at singly-paired apexes (original form: R-in's pair partner must be T-out).
mode 'full': no restriction; 'TC': T-out edge lies in the cherry; 'R0': R-in edge not in the cherry."""
import p5solve
from itertools import combinations
_orig=p5solve.local_domain
MODE=['full']
def local_domain(w, nb, mate, p5=True, p3=True):
    dom=_orig(w,nb,mate,p5,p3)
    pairs=[(x,y) for x,y in combinations(nb,2) if mate[x]==y]
    if len(pairs)!=1 or MODE[0]=='full': return dom
    i,j=nb.index(pairs[0][0]),nb.index(pairs[0][1])
    out=[]
    for a in dom:
        # a[k]=(inR,incoming)
        tout=[k for k in range(4) if (not a[k][0]) and not a[k][1]][0]
        rin=[k for k in range(4) if a[k][0] and a[k][1]][0]
        if MODE[0]=='TC' and tout not in (i,j): continue
        if MODE[0]=='R0' and rin in (i,j): continue
        out.append(a)
    return out
p5solve.local_domain=local_domain
def solve(adj,m,mode,**k):
    MODE[0]=mode
    return p5solve.solve(adj,m,**k)
