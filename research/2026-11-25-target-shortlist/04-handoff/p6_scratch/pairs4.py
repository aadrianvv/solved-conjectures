import sys, pickle
from itertools import permutations
COMP={'Ri':'Ro','Ro':'Ri','Si':'So','So':'Si'}
G=pickle.load(open(sys.argv[1],'rb'))
G=[g for g in G if len(g[3])<36]
G.sort(key=lambda g:len(g[3]))
found=0
for i,A in enumerate(G):
    for j,B in enumerate(G):
        if j<i: continue
        for pi in permutations(range(4)):
            ok=False
            for t in A[3]:
                s=[None]*4
                for a in range(4): s[pi[a]]=COMP[t[a]]
                if tuple(s) in B[3]: ok=True; break
            if not ok:
                print("INCOMPATIBLE", i, j, pi, len(A[3]), len(B[3])); found+=1
                pickle.dump((A,B,pi),open('incompat_%d.pkl'%found,'wb'))
                break
        if found>=3: sys.exit()
print("pairs checked; found",found)
