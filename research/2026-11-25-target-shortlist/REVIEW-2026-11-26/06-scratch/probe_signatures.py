from itertools import product
def sig(n, edges):  # edge 0 is the bridge (q=0, p=outside vertex index n-1 ignored)
    res=set()
    for col in product(range(3),repeat=len(edges)):
        d=[[0]*3 for _ in range(n)]
        for (u,v),c in zip(edges,col): d[u][c]+=1; d[v][c]+=1
        if all(d[u][c]!=d[v][c] for k,((u,v),c) in enumerate(zip(edges,col)) if k>0):
            res.add(d[0][col[0]])
    return res
P=9
print('leaf', sig(10,[(0,P)]))
print('2-vertex path', sig(10,[(0,P),(0,1)]))
print('3-vertex path', sig(10,[(0,P),(0,1),(1,2)]))
print('half bow-tie', sig(10,[(0,P),(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)]))
