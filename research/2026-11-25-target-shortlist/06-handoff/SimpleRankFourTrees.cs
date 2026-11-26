
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private static IEnumerable<int[]> PortShapes(int[] ports,int i,int used) {
        if(i==ports.Length) {
            yield return (int[])ports.Clone();
            yield break;
        }
        for(int c=0;c<Math.Min(3,used+1);++c) {
            ports[i]=c;
            foreach(var next in PortShapes(ports,i+1,Math.Max(used,c+1)))yield return next;
        }
    }
    private static StarCap TreeCapArity(int arity,int one,int two) {
        if(arity==3)return TreeCap(one,two);
        var found=new HashSet<ulong>();
        int total=one+two;
        foreach(var ports in PortShapes(new int[arity],0,0)) {
            var coreCount=new int[3];
            foreach(int c in ports)++coreCount[c];
            for(int a=0;a<=total;++a)for(int b=0;b<=total-a;++b) {
                int[] slot={a,b,total-a-b};
                var degree=new int[3];
                int avoidOne=0,avoidTwo=0;
                for(int c=0;c<3;++c) {
                    degree[c]=slot[c]+coreCount[c];
                    if(degree[c]==1)avoidOne+=slot[c];
                    if(degree[c]==2)avoidTwo+=slot[c];
                }
                if(one>total-avoidOne||two>total-avoidTwo)continue;
                foreach(var permutation in PalettePermutations) {
                    ulong code=0;
                    for(int p=0;p<arity;++p) {
                        int c=ports[p];
                        code|=(ulong)(Width*permutation[c]+degree[c]-1)<<(6*p);
                    }
                    found.Add(code);
                }
            }
        }
        uint[] adj=new uint[1];
        for(int i=0;i<one;++i)adj=Attach(adj,0,3);
        for(int i=0;i<two;++i) {
            int first=adj.Length;
            adj=Attach(adj,0,3);
            adj=Attach(adj,first,3);
        }
        return new StarCap {Adj=adj, Root=0, Domain=found, States=found.ToArray()};
    }
    private static IEnumerable<int[]> Automorphisms(int[] order,int i,int used,bool[,] adjacency) {
        if(i==order.Length) {
            yield return (int[])order.Clone();
            yield break;
        }
        for(int u=0;u<order.Length;++u) {
            if((used&(1<<u))!=0)continue;
            bool okay=true;
            for(int j=0;j<i;++j)
                if(adjacency[i,j]!=adjacency[u,order[j]]) {
                    okay=false;
                    break;
                }
            if(!okay)continue;
            order[i]=u;
            foreach(var next in Automorphisms(order,i+1,used|(1<<u),adjacency))yield return next;
        }
    }
    private static bool DomainCases(int i,int[] selected,StarCap[][] choices,
                                    int[][] sym,Connector[] kernel,ref long done,ref long calls) {
        if(i==selected.Length) {
            foreach(var p in sym) {
                for(int k=0;k<selected.Length;++k) {
                    if(selected[p[k]]<selected[k])return false;
                    if(selected[p[k]]>selected[k])break;
                }
            }
            var caps=Enumerable.Range(0,selected.Length).Select(v=>choices[v][selected[v]]).ToArray();
            if(CheckTreeKernel(kernel,caps,ref calls))return true;
            ++done;
            if(done%100==0)Console.WriteLine($"completed hub patterns={done}; witnesses={calls}");
            return false;
        }
        for(int k=0;k<choices[i].Length;++k) {
            selected[i]=k;
            if(DomainCases(i+1,selected,choices,sym,kernel,ref done,ref calls))return true;
        }
        return false;
    }

    public static void SimpleRankFourWithTrees(int kind) {
        int size=kind==0?5:6;
        var edges=kind==0
            ? SignedCore(0,5).Where(e=>e!=(1,2)&&e!=(3,4)).ToArray()
            : SignedCore(kind,6);
        var kernel=edges.Select(e=>new Connector(e.Item1,e.Item2,1)).ToArray();
        var adjacency=new bool[size,size];
        var degree=new int[size];
        foreach(var (u,v) in edges) {
            adjacency[u,v]=adjacency[v,u]=true;
            ++degree[u];
            ++degree[v];
        }
        var capsBySize=new Dictionary<int,StarCap[]>();
        foreach(int d in degree.Distinct()) {
            var options=new List<StarCap>();
            for(int q=0;q<=d+8;++q)
                for(int first=0;first<=q;++first)
                    InsertCap(TreeCapArity(d,first,q-first),options);
            capsBySize.Add(d,options.ToArray());
            Console.WriteLine($"port count={d}, minimal tree caps={options.Count}");
        }
        var sym=Automorphisms(new int[size],0,0,adjacency).ToArray();
        Console.WriteLine($"simple kernel kind={kind}, order={size}, symmetries={sym.Length}");
        long checkedDomains=0;
        long solverCalls=0;
        if(DomainCases(0,new int[size],degree.Select(d=>capsBySize[d]).ToArray(),sym,kernel,
                       ref checkedDomains,ref solverCalls))return;
        Console.WriteLine($"Simple rank-four kernel {kind} complete; tested hub patterns={checkedDomains}; solves={solverCalls}");
    }
}

