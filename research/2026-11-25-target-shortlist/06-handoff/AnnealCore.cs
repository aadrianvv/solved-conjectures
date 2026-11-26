
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private static readonly int[][] HardArms=new[]{
        Array.Empty<int>(),new[]{1},new[]{2},new[]{3},new[]{3,3},new[]{-3},new[]{-3,-3},
        new[]{-3,1},new[]{-3,2},new[]{-3,3},new[]{1,2},new[]{1,1},new[]{2,2},new[]{4},
        new[]{5},new[]{-3,-3,1},new[]{-3,1,2},new[]{-3,-3,-3}
    };
    private static int CountHubSolutions(Hub[] hubs,ulong[][] domains,uint todo,int limit) {
        while(todo!=0) {
            int v=BitOperations.TrailingZeroCount(todo);
            todo^=1U<<v;
            if(domains[v].Length==0)return 0;
            var at=hubs[v];
            for(int p=0;p<at.Other.Length;++p) {
                int u=at.Other[p], q=at.Reverse[p];
                int ps=6*p,qs=6*q;
                ulong available=0;
                foreach(ulong x in domains[v])available|=1UL<<(int)((x>>ps)&63);
                ulong supports=0;
                while(available!=0) {
                    int x=BitOperations.TrailingZeroCount(available);
                    available^=1UL<<x;
                    supports|=PathSupport[at.Lengths[p],x];
                }
                int keep=0;
                foreach(ulong y in domains[u])if((supports&(1UL<<(int)((y>>qs)&63)))!=0)++keep;
                if(keep==0)return 0;
                if(keep==domains[u].Length)continue;
                var narrowed=new ulong[keep];
                int j=0;
                foreach(ulong y in domains[u])if((supports&(1UL<<(int)((y>>qs)&63)))!=0)narrowed[j++]=y;
                domains[u]=narrowed;
                todo|=1U<<u;
            }
        }
        int chosen=-1;
        int best=int.MaxValue;
        for(int v=0;v<domains.Length;++v) {
            int n=domains[v].Length;
            if(n>1&&n<best) {
                best=n;
                chosen=v;
            }
        }
        if(chosen<0)return 1;
        int total=0;
        foreach(ulong state in domains[chosen]) {
            var local=(ulong[][])domains.Clone();
            local[chosen]=new[]{state};
            total+=CountHubSolutions(hubs,local,1U<<chosen,limit-total);
            if(total>=limit)return limit;
        }
        return total;
    }
    private static int CheckProfileCount(Connector[] edges,int[][] arms,int limit) {
        var hubs=MakeHubs(arms.Length,edges,arms,3);
        return CountHubSolutions(hubs,hubs.Select(h=>h.Domain).ToArray(),(1U<<hubs.Length)-1,limit);
    }
    public static void AnnealCore(int seed,int rounds,int steps) {
        var rng=new Random(seed);
        (int shape,int n)[] cores=new[]{(0,4),(1,6),(2,6),(2,8),(3,8),(4,10)};
        int[] modes=new[]{1,1,1,2,2,3,3,3,4,5,6,7};
        long scans=0;
        int best=256;
        for(int k=0;k<rounds;++k) {
            var (shape,n)=cores[k%cores.Length];
            var source=SignedCore(shape,n);
            var accepted=source.Select(e=>new Connector(e.Item1,e.Item2,modes[rng.Next(modes.Length)])).ToArray();
            var arms=Enumerable.Range(0,n).Select(_=>HardArms[rng.Next(HardArms.Length)]).ToArray();
            int current=CheckProfileCount(accepted,arms,256);
            for(int i=0;i<steps;++i) {
                var next=(Connector[])accepted.Clone();
                var nextArms=(int[][])arms.Clone();
                if(rng.Next(2)==0) {
                    int j=rng.Next(next.Length);
                    next[j]=new Connector(next[j].U,next[j].V,modes[rng.Next(modes.Length)]);
                } else {
                    nextArms[rng.Next(n)]=HardArms[rng.Next(HardArms.Length)];
                }
                ++scans;
                int count=CheckProfileCount(next,nextArms,256);
                if(count==0) {
                    CheckHub(n,next,nextArms,ref scans);
                    return;
                }
                if(count<best) {
                    best=count;
                    Console.WriteLine($"profile minimum={best}, checked={scans}, core {shape},{n}");
                    Console.WriteLine("links="+string.Join(",",next.Select(e=>e.ToString()))+
                                      " arcs="+string.Join(";",nextArms.Select(e=>string.Join(",",e))));
                }
                double temperature=0.55-0.5*i/steps;
                if(count<=current || rng.NextDouble()<Math.Exp((Math.Log(current)-Math.Log(count))/temperature)) {
                    accepted=next;
                    arms=nextArms;
                    current=count;
                }
            }
            if((k+1)%10==0)Console.WriteLine($"annealing rounds={k+1}, profiles={scans}, best={best}");
        }
        Console.WriteLine($"annealing completed: {scans} profiles; best={best}");
    }
}

