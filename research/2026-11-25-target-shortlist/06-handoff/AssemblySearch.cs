
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

public static partial class BigIrregularSearch {
    private static readonly ulong[] Bow = Make(10,0,1,0,2,0,3,2,3,0,4,0,5,4,5,
                                               1,6,1,7,6,7,1,8,1,9,8,9);

    private static ulong[] CopyWithOneOmitted(ulong[] source,int a,int b) {
        var result=(ulong[])source.Clone();
        result[a]&=~(1UL<<b);
        result[b]&=~(1UL<<a);
        return result;
    }

    private static (ulong[] graph,int[] offsets) Combine(IEnumerable<ulong[]> components) {
        var result = new List<ulong>();
        var offsets = new List<int>();
        foreach (ulong[] component in components) {
            int offset=result.Count;
            offsets.Add(offset);
            foreach (ulong neighbors in component) result.Add(neighbors<<offset);
        }
        return (result.ToArray(),offsets.ToArray());
    }

    private static void Edge(ulong[] graph,int a,int b) {
        if (a==b) return;
        graph[a]|=1UL<<b;
        graph[b]|=1UL<<a;
    }

    private static ulong[] Path(ulong[] graph,int a,int b,int length) {
        if (length==1) {
            var clone=(ulong[])graph.Clone();
            Edge(clone,a,b);
            return clone;
        }
        var result = new ulong[graph.Length+length-1];
        Array.Copy(graph,result,graph.Length);
        for (int v=graph.Length;v<result.Length;++v) {
            Edge(result,a,v);
            a=v;
        }
        Edge(result,a,b);
        return result;
    }

    private static ulong[] MergePorts(ulong[] a,ulong[] b,int leftA,int rightA,int leftB,int rightB) {
        var result=new ulong[a.Length+b.Length-(rightB<0?1:2)];
        Array.Copy(a,result,a.Length);
        var mapping=new int[b.Length];
        int next=a.Length;
        for (int i=0;i<b.Length;++i)
            mapping[i]=i==leftB?leftA:i==rightB?rightA:next++;
        for (int v=1;v<b.Length;++v)
            for (int u=0;u<v;++u)
                if ((b[v]&(1UL<<u))!=0) Edge(result,mapping[u],mapping[v]);
        return result;
    }

    private static bool TestAssembly(ulong[] graph,ref long count) {
        if (graph.Any(row=>BitOperations.PopCount(row)>8)) return false;
        if (IsCactus(graph)) return false;
        ++count;
        var p=new Problem(new Graph(graph),-1,3);
        if (p.Solve(0)!=null) return false;
        Console.WriteLine("NO THREE: "+Format(graph));
        var four = new Problem(p.Graph,-1,4);
        var witness=four.Solve(0);
        Console.WriteLine(witness==null?"No 4-coloring":FormatColored(four,witness));
        return true;
    }

    public static void AssemblySearch(int seed,int trials) {
        long total=0;
        var copies = Combine(new[]{Bow,Bow}).graph;
        var bowFragments=new [] {
            Bow,CopyWithOneOmitted(Bow,0,2),CopyWithOneOmitted(Bow,2,3)
        };
        foreach (var aa in bowFragments) foreach (var bb in bowFragments) {
            var ab=Combine(new[]{aa,bb}).graph;
            for (int a=0;a<10;++a) for (int b=0;b<10;++b)
                for (int c=a;c<10;++c) for (int d=0;d<10;++d) {
                    if (c==a && d<b) continue;
                    for (int x=1;x<=2;++x) for (int y=1;y<=2;++y) {
                        if (a==c && b==d && x==1 && y==1) continue;
                        var graph=Path(Path(ab,a,10+b,x),c,10+d,y);
                        if (TestAssembly(graph,ref total)) return;
                    }
                    if (a!=c && b!=d &&
                        TestAssembly(MergePorts(aa,bb,a,c,b,d),ref total)) return;
                }
        }
        Console.WriteLine("finished exhaustive two-copy assemblies: "+total);
        var modules = new [] {
            Bow,Bow,Bow,bowFragments[1],bowFragments[2],
            Make(3,0,1,1,2,0,2),
            Make(6,0,1,1,2,0,2,0,3,3,4,4,5,3,5),
            Make(9,0,1,1,2,0,2,0,3,3,4,4,5,3,5,5,6,6,7,7,8,6,8),
            Make(7,0,1,1,2,0,2,0,3,3,4,4,5,3,5,5,6),
            Make(5,0,1,1,2,0,2,0,3,0,4,3,4)
        };
        var rng = new Random(seed);
        for (int k=1;k<=trials;++k) {
            int n=rng.Next(3,6);
            var pieces=Enumerable.Range(0,n).Select(_=>modules[rng.Next(modules.Length)]).ToArray();
            var packed=Combine(pieces);
            var graph=packed.graph;
            int[] starts=packed.offsets;
            for(int i=0;i<n;++i) {
                int j=(i+1)%n;
                int a=starts[i]+rng.Next(pieces[i].Length);
                int b=starts[j]+rng.Next(pieces[j].Length);
                graph=Path(graph,a,b,rng.Next(1,4));
            }
            int further=rng.Next(0,n+1);
            while(further-->0 && graph.Length<61) {
                int i=rng.Next(n);
                int j=rng.Next(n-1);
                if(j>=i)++j;
                graph=Path(graph,starts[i]+rng.Next(pieces[i].Length),
                                 starts[j]+rng.Next(pieces[j].Length),rng.Next(1,4));
            }
            if (TestAssembly(graph,ref total)) return;
            if(k%10000==0)Console.WriteLine($"random assembly attempts={k}, checked={total}");
        }
        Console.WriteLine("completed assembly search, checked="+total);
    }
}

