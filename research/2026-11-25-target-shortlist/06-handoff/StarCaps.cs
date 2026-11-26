
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public static partial class IrregularSearch {
    private sealed class StarCap {
        public uint[] Adj;
        public int Root;
        public HashSet<ulong> Domain;
        public ulong[] States;
    }

    private static readonly int[][] PortPatterns = new [] {
        new[]{0,0,0},new[]{0,0,1},new[]{0,1,0},new[]{0,1,1},new[]{0,1,2}
    };
    private static readonly int[][] PalettePermutations = new [] {
        new[]{0,1,2},new[]{0,2,1},new[]{1,0,2},new[]{1,2,0},new[]{2,0,1},new[]{2,1,0}
    };
    private static readonly Dictionary<(int,int,int,int),States> ExtraStates =
        new Dictionary<(int,int,int,int),States>();

    private static States GetExtraStates(int degree,int[] extras) {
        var key=(degree,extras[0],extras[1],extras[2]);
        if(!ExtraStates.TryGetValue(key,out var states)) {
            states=new States(degree,-1,3,-1,extras);
            ExtraStates.Add(key,states);
        }
        return states;
    }
    private static StarCap ProjectCap(uint[] adj,Graph graph,int root) {
        var found=new HashSet<ulong>();
        foreach(var ports in PortPatterns) {
            var extras=new int[3];
            foreach(int c in ports)++extras[c];
            var rootStates=GetExtraStates(graph.Neighbors[root].Length,extras);
            var exact=new Problem(graph,root,rootStates);
            var groups=new Dictionary<ulong,List<int>>();
            foreach(int s in rootStates.IDs) {
                ulong code=0;
                for(int k=0;k<3;++k) {
                    int c=ports[k];
                    int symbol=Width*c+rootStates.DegreeByColor[c][s]-1;
                    code|=(ulong)symbol<<(6*k);
                }
                if(!groups.TryGetValue(code,out var ids)) {
                    ids=new List<int>();
                    groups.Add(code,ids);
                }
                ids.Add(s);
            }
            foreach(var candidate in groups) {
                exact.Initial[root]=candidate.Value.ToArray();
                if(exact.Solve(0)==null)continue;
                foreach(var map in PalettePermutations) {
                    ulong output=0;
                    for(int k=0;k<3;++k) {
                        int symbol=(int)((candidate.Key>>(6*k))&63);
                        int moved=Width*map[symbol/Width]+symbol%Width;
                        output|=(ulong)moved<<(6*k);
                    }
                    found.Add(output);
                }
            }
        }
        return new StarCap {Adj=adj,Root=root,Domain=found,States=found.ToArray()};
    }

    private static bool TestCaps(Connector[] core,StarCap[] caps,ref long checks) {
        ++checks;
        var decorations=Enumerable.Range(0,caps.Length).Select(_=>Array.Empty<int>()).ToArray();
        var hubs=MakeHubs(caps.Length,core,decorations,3);
        var domains=caps.Select(c=>c.States).ToArray();
        domains[0]=domains[0].Where(w=>(w&63)<Width).ToArray();
        if(SolveHubs(hubs,domains,(1U<<hubs.Length)-1)!=null)return false;
        Console.WriteLine("OBSTRUCTION core="+string.Join(",",core.Select(e=>e.ToString())));
        for(int v=0;v<caps.Length;++v)
            Console.WriteLine($"cap {v}, root={caps[v].Root} states={caps[v].States.Length}: {Format(caps[v].Adj)}");
        int size=caps.Length+caps.Sum(c=>c.Adj.Length-1);
        if(size<=31 && core.All(e=>e.Length==1)) {
            var combined=new uint[size];
            foreach(var e in core) {
                combined[e.U]|=1U<<e.V;
                combined[e.V]|=1U<<e.U;
            }
            int next=caps.Length;
            for(int v=0;v<caps.Length;++v) {
                var cap=caps[v];
                var map=new int[cap.Adj.Length];
                for(int i=0;i<map.Length;++i)map[i]=i==cap.Root?v:next++;
                for(int j=1;j<map.Length;++j)
                    for(int i=0;i<j;++i)
                        if((cap.Adj[j]&(1U<<i))!=0) {
                            combined[map[i]]|=1U<<map[j];
                            combined[map[j]]|=1U<<map[i];
                        }
            }
            Console.WriteLine("expanded "+Format(combined));
            var g=new Graph(combined);
            Console.WriteLine("direct 3-colouring="+(new Problem(g,-1,3).Solve(0)!=null));
            var four=new Problem(g,-1,4);
            var witness=four.Solve(0);
            Console.WriteLine(witness==null?"No 4-coloring":FormatColored(four,witness));
        }
        return true;
    }

    private static bool InsertCap(StarCap cap,List<StarCap> options) {
        if(options.Any(c=>c.Domain.IsSubsetOf(cap.Domain)))return false;
        options.RemoveAll(c=>cap.Domain.IsSubsetOf(c.Domain));
        options.Add(cap);
        return true;
    }
    public static void JoinedStarCaps(int maxOrder,int trials,string folder) {
        var k4=SignedCore(0,4).Select(e=>new Connector(e.Item1,e.Item2,1)).ToArray();
        long checkedCaps=0;
        long testedGraphs=0;
        var options=new List<StarCap>();
        uint[] isolated=new uint[1];
        var plain=ProjectCap(isolated,new Graph(isolated),0);
        InsertCap(plain,options);
        if(TestCaps(k4,new[]{plain,plain,plain,plain},ref testedGraphs))return;
        for(int n=2;n<=maxOrder;++n) {
            string cache=Path.Combine(folder,"connected-"+n+"-max-7-30.txt");
            foreach(var line in File.ReadLines(cache)) {
                uint[] adj=Adj(Convert.ToUInt64(line,16),n);
                var g=new Graph(adj);
                for(int root=0;root<n;++root) {
                    ++checkedCaps;
                    var cap=ProjectCap(adj,g,root);
                    if(!InsertCap(cap,options))continue;
                    if(TestCaps(k4,new[]{cap,cap,cap,cap},ref testedGraphs))return;
                }
            }
            Console.WriteLine($"three-port caps n={n}, tried={checkedCaps}, minimal={options.Count}, whole tests={testedGraphs}");
        }
        options=options.OrderBy(x=>x.Domain.Count).ToList();
        var seen=options.Take(Math.Min(32,options.Count)).ToArray();
        for(int a=0;a<seen.Length;++a)
            for(int b=a;b<seen.Length;++b)
                for(int c=b;c<seen.Length;++c)
                    for(int d=c;d<seen.Length;++d)
                        if(TestCaps(k4,new[]{seen[a],seen[b],seen[c],seen[d]},ref testedGraphs))return;
        Console.WriteLine("smallest cap K4 mixtures tested="+testedGraphs);
        var rng=new Random(20261125);
        for(int it=1;it<=trials;++it) {
            int n=it%3==0?4:it%3==1?6:10;
            int kind=n==4?0:n==6?rng.Next(1,3):4;
            var source=SignedCore(kind,n);
            var core=source.Select(e=>new Connector(e.Item1,e.Item2,it%4<2?1:new[]{1,1,3,7}[rng.Next(4)])).ToArray();
            var caps=Enumerable.Range(0,n).Select(_=>options[rng.Next(options.Count)]).ToArray();
            if(TestCaps(core,caps,ref testedGraphs))return;
            if(it%10000==0)Console.WriteLine($"cap mixtures sampled={it}; exact tests={testedGraphs}");
        }
        Console.WriteLine($"star-cap search completed; checked caps={checkedCaps}, tested graphs={testedGraphs}");
    }
}

