from itertools import combinations
adj=[[1, 2, 3, 4, 8], [0, 2, 6, 7, 8], [0, 1, 3, 4, 5], [0, 2, 6, 7, 9], [0, 2, 5, 7, 9], [2, 4, 6, 7, 8], [1, 3, 5, 8, 9], [1, 3, 4, 5, 9], [0, 1, 5, 6, 9], [3, 4, 6, 7, 8]]
m={4: 0, 0: 4, 9: 8, 8: 9, 1: 7, 7: 1, 2: 3, 3: 2, 5: 6, 6: 5}
H=[sorted(w for w in adj[v] if w!=m[v]) for v in range(10)]
for x in range(10):
    ch=[(y,z) for y,z in combinations(H[x],2) if m[y]==z]
    print(x,'H-nbrs',H[x],'cherries',ch)
