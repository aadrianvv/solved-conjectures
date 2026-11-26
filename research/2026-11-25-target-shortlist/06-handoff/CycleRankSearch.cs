
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private static IEnumerable<int[]> DegreeSequences(int size,int sum,int minimum,List<int> prefix) {
        if (size==1) {
            if (sum>=minimum) yield return prefix.Append(sum).ToArray();
            yield break;
        }
        for(int d=minimum;d*size<=sum;++d) {
            prefix.Add(d);
            foreach(var seq in DegreeSequences(size-1,sum-d,d,prefix))yield return seq;
            prefix.RemoveAt(prefix.Count-1);
        }
    }
    private static IEnumerable<int[,]> FillKernel(int[,] matrix,int[] rest,int row,int col) {
        int n=rest.Length;
        if (row==n) {
            yield return (int[,])matrix.Clone();
            yield break;
        }
        if (col==n) {
            if (rest[row]==0)
                foreach (var child in FillKernel(matrix,rest,row+1,row+1))yield return child;
            yield break;
        }
        int max=col==row?rest[row]/2:Math.Min(rest[row],rest[col]);
        for(int number=0;number<=max;++number) {
            matrix[row,col]=matrix[col,row]=number;
            rest[row]-=number;
            rest[col]-=number;
            foreach(var child in FillKernel(matrix,rest,row,col+1))yield return child;
            rest[col]+=number;
            rest[row]+=number;
        }
        matrix[row,col]=matrix[col,row]=0;
    }
    private static bool ConnectedKernel(int[,] m) {
        int n=m.GetLength(0);
        var seen=new bool[n];
        var todo=new Queue<int>();
        seen[0]=true;
        todo.Enqueue(0);
        while(todo.Count>0) {
            int v=todo.Dequeue();
            for(int u=0;u<n;++u) {
                if(m[u,v]==0||seen[u])continue;
                seen[u]=true;
                todo.Enqueue(u);
            }
        }
        return seen.All(x=>x);
    }
    private static void KernelKey(int[,] matrix,int[] degree,int[] perm,int pos,
                                  int used,ref string best) {
        int n=degree.Length;
        if(pos==n) {
            var chars=new char[n*(n+1)/2];
            int k=0;
            for(int row=0;row<n;++row)
                for(int col=row;col<n;++col)
                    chars[k++]=(char)('0'+matrix[perm[row],perm[col]]);
            string here=new string(chars);
            if(best==null||string.CompareOrdinal(here,best)<0)best=here;
            return;
        }
        for(int v=0;v<n;++v) {
            if((used&(1<<v))!=0||degree[v]!=degree[pos])continue;
            perm[pos]=v;
            KernelKey(matrix,degree,perm,pos+1,used|(1<<v),ref best);
        }
    }

    private static bool KernelPaths(int index,Connector[] edges,int[][] loops,ref long total) {
        if(index==edges.Length) {
            return CheckHub(loops.Length,edges,loops,ref total);
        }
        var edge=edges[index];
        int min=1;
        if(index!=0 && edges[index-1].U==edge.U && edges[index-1].V==edge.V)
            min=Math.Max(2,edges[index-1].Length);
        for(int len=min;len<=4;++len) {
            edges[index]=new Connector(edge.U,edge.V,len);
            if(KernelPaths(index+1,edges,loops,ref total))return true;
        }
        return false;
    }

    private static bool KernelLoops(int vertex,Connector[] edges,int[] loopCounts,
                                    int[][] layouts,ref long total) {
        if(vertex==loopCounts.Length)return KernelPaths(0,edges,layouts,ref total);
        int count=loopCounts[vertex];
        for(int triangles=0;triangles<=count;++triangles) {
            layouts[vertex]=Enumerable.Repeat(3,triangles).Concat(Enumerable.Repeat(4,count-triangles)).ToArray();
            if(KernelLoops(vertex+1,edges,loopCounts,layouts,ref total))return true;
        }
        return false;
    }

    public static void CycleRankSearch(int maxRank) {
        long total=0;
        for(int rank=2;rank<=maxRank;++rank) {
            for(int hubs=2;hubs<=2*(rank-1);++hubs) {
                int size=hubs+rank-1;
                var used = new HashSet<string>();
                int noncacti=0;
                foreach(var deg in DegreeSequences(hubs,2*size,3,new List<int>())) {
                    foreach(var kernel in FillKernel(new int[hubs,hubs],(int[])deg.Clone(),0,0)) {
                        if (!ConnectedKernel(kernel)) continue;
                        string key=null;
                        KernelKey(kernel,deg,new int[hubs],0,0,ref key);
                        if (!used.Add(key)) continue;
                        var connectors=new List<Connector>();
                        var loops=new int[hubs];
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
                        if(KernelLoops(0,connectors.ToArray(),loops,new int[hubs][],ref total))return;
                        Console.WriteLine($"cycle rank={rank}, hubs={hubs}, noncactus kernel={noncacti}, tested={total}");
                    }
                }
                Console.WriteLine($"finished rank={rank}, hubs={hubs}, kernels={used.Count}, noncacti={noncacti}, tested={total}");
            }
        }
        Console.WriteLine($"cycle-rank screen complete; tested={total}");
    }
}

