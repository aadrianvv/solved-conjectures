
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private static UInt128 EncodeKernel(int[,] matrix,int[] perm) {
        UInt128 mask=0;
        int bits=matrix.GetLength(0)>=8?2:4;
        for(int i=0;i<perm.Length;++i)
            for(int j=i;j<perm.Length;++j)
                mask=(mask<<bits)|(uint)matrix[perm[i],perm[j]];
        return mask;
    }
    private static void SeenRelabelings(int[,] matrix,int[] degree,int[] perm,int pos,int used,
                                        HashSet<UInt128> seen) {
        if(pos==degree.Length) {
            seen.Add(EncodeKernel(matrix,perm));
            return;
        }
        for(int v=0;v<degree.Length;++v) {
            if((used&(1<<v))!=0||degree[v]!=degree[pos])continue;
            perm[pos]=v;
            SeenRelabelings(matrix,degree,perm,pos+1,used|(1<<v),seen);
        }
    }

    private static void CoverWords(ulong[] bits,int[] allowed,int pos,int word) {
        if(pos==allowed.Length) {
            bits[word>>6] |= 1UL<<(word&63);
            return;
        }
        int mask=allowed[pos];
        for(int m=0;m<4;++m)
            if((mask&(1<<m))!=0) CoverWords(bits,allowed,pos+1,(word<<2)|m);
    }
    private static bool KernelPathCubes(Connector[] edges,int[][] loops,ref long candidates,
                                       ref long solverCalls) {
        int words=1<<(2*edges.Length);
        var covered=new ulong[(words+63)/64];
        var slot=new int[loops.Length];
        var modes=new int[edges.Length];
        for(int w=0;w<words;++w) {
            if((covered[w>>6]&(1UL<<(w&63)))!=0)continue;
            int tmp=w;
            for(int e=edges.Length-1;e>=0;--e) {
                var old=edges[e];
                edges[e]=new Connector(old.U,old.V,1+(tmp&3));
                tmp>>=2;
            }
            bool valid=true;
            for(int e=1;e<edges.Length;++e) {
                if(edges[e].U==edges[e-1].U && edges[e].V==edges[e-1].V &&
                   (edges[e].Length==1 || edges[e].Length<edges[e-1].Length)){
                    valid=false;
                    break;
                }
            }
            if(!valid)continue;
            ++solverCalls;
            var coloring=SolveHubs(loops.Length,edges,loops,3);
            if(coloring==null) {
                long test=0;
                return CheckHub(loops.Length,edges,loops,ref test);
            }
            Array.Clear(slot,0,slot.Length);
            for(int e=0;e<edges.Length;++e) {
                var link=edges[e];
                int x=(int)((coloring[link.U]>>(6*slot[link.U]++))&63);
                int y=(int)((coloring[link.V]>>(6*slot[link.V]++))&63);
                int mask=0;
                for(int type=1;type<=4;++type)
                    if(AllowsPath(type,x,y))mask|=1<<(type-1);
                modes[e]=mask;
            }
            CoverWords(covered,modes,0,0);
            if((covered[w>>6]&(1UL<<(w&63)))==0)
                throw new InvalidOperationException("A computed coloring did not cover its own length word.");
        }
        candidates += words;
        return false;
    }
    private static bool KernelLoopCubes(int vertex,Connector[] edges,int[] loopCounts,
                                       int[][] layouts,ref long candidates,ref long solverCalls) {
        if(vertex==loopCounts.Length)return KernelPathCubes(edges,layouts,ref candidates,ref solverCalls);
        int count=loopCounts[vertex];
        for(int triangles=0;triangles<=count;++triangles) {
            layouts[vertex]=Enumerable.Repeat(3,triangles).Concat(Enumerable.Repeat(4,count-triangles)).ToArray();
            if(KernelLoopCubes(vertex+1,edges,loopCounts,layouts,ref candidates,ref solverCalls))return true;
        }
        return false;
    }
    public static void CubeCycleRank(int minRank,int maxRank) {
        long candidates=0;
        long solverCalls=0;
        for(int rank=minRank;rank<=maxRank;++rank)
            for(int hubs=2;hubs<=2*(rank-1);++hubs) {
                int size=hubs+rank-1;
                var used=new HashSet<UInt128>();
                int kernels=0;
                int noncacti=0;
                int[] identity=Enumerable.Range(0,hubs).ToArray();
                foreach(var deg in DegreeSequences(hubs,2*size,3,new List<int>()))
                    foreach(var kernel in FillKernel(new int[hubs,hubs],(int[])deg.Clone(),0,0)) {
                        if(!ConnectedKernel(kernel)||used.Contains(EncodeKernel(kernel,identity)))continue;
                        SeenRelabelings(kernel,deg,new int[hubs],0,0,used);
                        ++kernels;
                        var connectors=new List<Connector>();
                        int[] loops=new int[hubs];
                        for(int v=0;v<hubs;++v) {
                            loops[v]=kernel[v,v];
                            for(int u=0;u<v;++u)
                                for(int times=kernel[u,v];times>0;--times)
                                    connectors.Add(new Connector(u,v,2));
                        }
                        var expanded=ExpandSkeleton(hubs,connectors.ToArray(),
                            loops.Select(n=>Enumerable.Repeat(3,n).ToArray()).ToArray());
                        if(IsCactus(expanded))continue;
                        ++noncacti;
                        if(KernelLoopCubes(0,connectors.ToArray(),loops,new int[hubs][],
                                           ref candidates,ref solverCalls))return;
                    }
                Console.WriteLine($"cube cycle rank={rank}, hubs={hubs}, kernels={kernels}, noncacti={noncacti}, raw words={candidates}, solves={solverCalls}");
            }
        Console.WriteLine($"CUBE cycle-rank screen complete; raw words={candidates}, solved witnesses={solverCalls}");
    }
}

