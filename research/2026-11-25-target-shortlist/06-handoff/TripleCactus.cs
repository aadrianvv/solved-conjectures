
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private sealed class TripleFragment {
        public uint[] Adj;
        public int[] Ports;
        public string Name;
        public ulong[] Domains;
    }
    private static IEnumerable<int[]> CapSymmetries(uint[] adj,int[] map,int index,uint used) {
        if(index==adj.Length) {
            yield return (int[])map.Clone();
            yield break;
        }
        for(int v=0;v<adj.Length;++v) {
            if((used&(1U<<v))!=0||
                System.Numerics.BitOperations.PopCount(adj[v])!=System.Numerics.BitOperations.PopCount(adj[index]))
                continue;
            bool match=true;
            for(int s=0;s<index;++s)
                if(((adj[index]>>s)&1U)!=((adj[v]>>map[s])&1U)) {
                    match=false;
                    break;
                }
            if(!match)continue;
            map[index]=v;
            foreach(var suffix in CapSymmetries(adj,map,index+1,used|(1U<<v)))yield return suffix;
        }
    }
    private static bool BestTriple(int[] vertices,int[][] sym) {
        foreach(var p in sym) {
            int[] moved=vertices.Select(v=>p[v]).OrderBy(x=>x).ToArray();
            for(int k=0;k<3;++k) {
                if(moved[k]<vertices[k])return false;
                if(moved[k]>vertices[k])break;
            }
        }
        return true;
    }
    private static void ProjectTripleRec(Problem problem,int[] touched,
                                         List<(ulong,int[])>[] groups,int index,
                                         ulong partial,HashSet<ulong> domains) {
        if(index==touched.Length) {
            if(problem.Solve(0)==null)return;
            foreach(var map in PalettePermutations) {
                ulong output=0;
                for(int p=0;p<3;++p) {
                    int s=(int)((partial>>(6*p))&63);
                    int r=Width*map[s/Width]+s%Width;
                    output|=(ulong)r<<(6*p);
                }
                domains.Add(output);
            }
            return;
        }
        int v=touched[index];
        foreach(var (state,ids) in groups[index]) {
            problem.Initial[v]=ids;
            ProjectTripleRec(problem,touched,groups,index+1,partial|state,domains);
        }
    }
    private static ulong[] ProjectTriple(Graph graph,int[] ports) {
        int[] touched=ports.Distinct().ToArray();
        var domains=new HashSet<ulong>();
        foreach(var colors in PortPatterns) {
            var slotColors=Enumerable.Range(0,graph.Neighbors.Length).Select(_=>new int[3]).ToArray();
            for(int i=0;i<3;++i)++slotColors[ports[i]][colors[i]];
            States[] local=Enumerable.Range(0,graph.Neighbors.Length)
                .Select(v=>GetExtraStates(graph.Neighbors[v].Length,slotColors[v])).ToArray();
            var problem=new Problem(graph,local);
            var groupList=new List<(ulong,int[])>[touched.Length];
            for(int i=0;i<touched.Length;++i) {
                int root=touched[i];
                var groups=new Dictionary<ulong,List<int>>();
                foreach(int s in local[root].IDs) {
                    ulong code=0;
                    for(int p=0;p<3;++p) {
                        if(ports[p]!=root)continue;
                        int c=colors[p];
                        int val=Width*c+local[root].DegreeByColor[c][s]-1;
                        code|=(ulong)val<<(6*p);
                    }
                    if(!groups.TryGetValue(code,out var ids)) {
                        ids=new List<int>();
                        groups.Add(code,ids);
                    }
                    ids.Add(s);
                }
                groupList[i]=groups.Select(x=>(x.Key,x.Value.ToArray())).ToList();
            }
            ProjectTripleRec(problem,touched,groupList,0,0,domains);
        }
        return domains.ToArray();
    }
    private static uint[] CombineTriple(TripleFragment a,TripleFragment b,int[] perm,int[] links) {
        int baseOrder=a.Adj.Length+b.Adj.Length;
        int total=baseOrder+links.Sum(d=>d==7?5:d-1);
        if(total>31)return null;
        var merged=new uint[baseOrder];
        Array.Copy(a.Adj,merged,a.Adj.Length);
        for(int v=0;v<b.Adj.Length;++v)merged[a.Adj.Length+v]=b.Adj[v]<<a.Adj.Length;
        for(int p=0;p<3;++p) {
            int u=a.Ports[p], v=a.Adj.Length+b.Ports[perm[p]], d=links[p];
            if(d!=7) {
                merged=LinkPath(merged,u,v,d-1);
            } else {
                int junction=merged.Length;
                merged=LinkPath(merged,u,v,1);
                for(int k=0;k<2;++k) {
                    int mid=merged.Length;
                    merged=Attach(merged,junction,3);
                    merged=Attach(merged,mid,3);
                }
            }
        }
        return merged;
    }
    private static ulong PermuteTriple(ulong state,int[] p) {
        ulong reordered=0;
        for(int i=0;i<3;++i)reordered|=((state>>(6*p[i]))&63)<<(6*i);
        return reordered;
    }
    private static bool CompatibleTriple(ulong[] a,ulong[] b,int[] modes) {
        foreach(ulong x in a) {
            int first=(int)(x&63);
            int second=(int)(x>>6&63);
            int third=(int)(x>>12&63);
            ulong allowFirst=PathSupport[modes[0],first];
            ulong allowSecond=PathSupport[modes[1],second];
            ulong allowThird=PathSupport[modes[2],third];
            foreach(ulong y in b)
                if((allowFirst&(1UL<<(int)(y&63)))!=0&&
                   (allowSecond&(1UL<<(int)(y>>6&63)))!=0&&
                   (allowThird&(1UL<<(int)(y>>12&63)))!=0)return true;
        }
        return false;
    }
    public static void CrossThree(int sampleBudget) {
        uint[] bow=Bow();
        (string name,uint[] graph)[] seeds={
            ("bow tie",bow),("bow with spoke removed",Unlink(bow,0,2)),
            ("bow with rim removed",Unlink(bow,2,3)),
            ("one triangle",Make(3,0,1,0,2,1,2)),
            ("two triangles at a shared vertex",Make(5,0,1,0,2,1,2,0,3,0,4,3,4)),
            ("two triangles linked by a bridge",Make(6,0,1,0,2,1,2,0,3,3,4,3,5,4,5)),
            ("three nonadjacent triangles",Make(9,0,1,0,2,1,2,0,3,3,4,3,5,4,5,5,6,6,7,6,8,7,8)),
        };
        var caps=new List<TripleFragment>();
        foreach(var (name,adj) in seeds) {
            var sym=CapSymmetries(adj,new int[adj.Length],0,0).ToArray();
            var g=new Graph(adj);
            int before=caps.Count;
            for(int a=0;a<adj.Length;++a)for(int b=a;b<adj.Length;++b)for(int c=b;c<adj.Length;++c) {
                int[] triple={a,b,c};
                if(!BestTriple(triple,sym))continue;
                caps.Add(new TripleFragment{Adj=adj,Ports=triple,Name=name,Domains=ProjectTriple(g,triple)});
            }
            Console.WriteLine($"three-port profile seeds for {name}: {caps.Count-before}");
        }
        int[] modeList={1,2,3,4,7};
        var rng=new Random(20261125);
        long checkedCases=0;
        for(int i=0;i<caps.Count;++i)for(int j=i;j<caps.Count;++j) {
            var a=caps[i];
            var b=caps[j];
            var permutations=new HashSet<string>();
            foreach(var p in PalettePermutations) {
                if(!permutations.Add(string.Join(",",p.Select(k=>b.Ports[k]))))continue;
                var other=b.Domains.Select(d=>PermuteTriple(d,p)).ToArray();
                int first=0;
                int bound=sampleBudget==0?125:Math.Min(sampleBudget,125);
                for(int code=0;code<bound;++code) {
                    int word=sampleBudget==0?code:code==0?0:rng.Next(125);
                    int[] modes={modeList[word%5],modeList[word/5%5],modeList[word/25]};
                    bool simple=true;
                    for(int v=0;v<3;++v)
                        for(int u=v+1;u<3;++u)
                            if(a.Ports[u]==a.Ports[v]&&b.Ports[p[u]]==b.Ports[p[v]]&&
                               modes[u]==1&&modes[v]==1)simple=false;
                    if(!simple)continue;
                    ++checkedCases;++first;
                    if(CompatibleTriple(a.Domains,other,modes))continue;
                    Console.WriteLine($"INCOMPATIBLE 3-LINK JOIN of {a.Name} and {b.Name}");
                    Console.WriteLine("First: "+Format(a.Adj)+" roots "+string.Join(",",a.Ports));
                    Console.WriteLine("Second: "+Format(b.Adj)+" roots "+string.Join(",",p.Select(k=>b.Ports[k])));
                    Console.WriteLine("Cross-link modes: "+string.Join(",",modes));
                    var actual=CombineTriple(a,b,p,modes);
                    if(actual!=null) {
                        Console.WriteLine("Expanded: "+Format(actual));
                        var graph=new Graph(actual);
                        var three=new Problem(graph,-1,3);
                        Console.WriteLine("Direct three colors="+(three.Solve(0)!=null));
                        var four=new Problem(graph,-1,4);
                        var witness=four.Solve(0);
                        Console.WriteLine(witness==null?"no direct four colors":FormatColored(four,witness));
                    }
                    return;
                }
            }
            if(checkedCases/100000!=(checkedCases-600)/100000)
                Console.WriteLine($"triple joins checked={checkedCases}, caps {i},{j}");
        }
        Console.WriteLine($"three-link scan complete: {caps.Count} marked fragments and {checkedCases} joins");
    }
}

