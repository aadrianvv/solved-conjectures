
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private sealed class Probe {
        public int ID;
        public bool SameRoot;
        public ulong Equal;
        public ulong Different;
    }
    private static List<Probe> MinimalMixedProbes(IEnumerable<Probe> source) {
        var active=new List<Probe>();
        foreach(var p in source) {
            if(active.Any(q=>(q.Equal&~p.Equal)==0&&(q.Different&~p.Different)==0))continue;
            active.RemoveAll(q=>(p.Equal&~q.Equal)==0&&(p.Different&~q.Different)==0);
            active.Add(p);
        }
        return active;
    }
    private static bool AcceptedMixed(Problem problem,ulong allowed,int leftMax,int rightMax,
                                       ref ulong seen,ref ulong good,ref long calls) {
        if((allowed&good)!=0)return true;
        for(int d=1;d<=leftMax;++d) {
            int row=(int)((allowed&~seen)>>(8*(d-1))&255UL);
            row&=(1<<rightMax)-1;
            if(row==0)continue;
            ++calls;
            int[] state=problem.SolvePair(1<<d,row<<1);
            if(state==null) {
                seen|=(ulong)row<<(8*(d-1));
                continue;
            }
            int at=problem.Other;
            int other=problem.States[at].StubCounts[state[at]];
            if(at==problem.Root)other=problem.States[at].SecondCounts[state[at]];
            ulong flag=1UL<<(8*(d-1)+other-1);
            seen|=flag;
            good|=flag;
            return true;
        }
        return false;
    }
    public static void MixedCactusProbes(string folder,int through) {
        var raw=new List<Probe>();
        foreach(string line in File.ReadLines(Path.Combine(folder,"cactus-pair-probes.txt"))) {
            string[] row=line.Split(' ');
            raw.Add(new Probe {ID=int.Parse(row[0]), SameRoot=row[1]=="1",
                               Equal=Convert.ToUInt64(row[2],16),Different=Convert.ToUInt64(row[3],16)});
        }
        var unrestricted=MinimalMixedProbes(raw);
        var distinct=MinimalMixedProbes(raw.Where(s=>!s.SameRoot));
        Console.WriteLine($"noncactus probes: {unrestricted.Count} unrestricted and {distinct.Count} distinct");
        long tested=0,calls=0;
        for(int n=4;n<=through;++n) {
            foreach(string row in File.ReadLines(Path.Combine(folder,"connected-"+n+"-max-7-30.txt"))) {
                uint[] adj=Adj(Convert.ToUInt64(row,16),n);
                if(IsCactus(adj))continue;
                var graph=new Graph(adj);
                for(int a=0;a<n;++a)for(int b=0;b<n;++b) {
                    int extra=a==b?2:1;
                    int da=graph.Neighbors[a].Length+extra;
                    int db=graph.Neighbors[b].Length+extra;
                    if(da>8||db>8)continue;
                    ++tested;
                    var same=new Problem(graph,a,b,0,3);
                    var diff=new Problem(graph,a,b,1,3);
                    ulong se=0,sd=0,ge=0,gd=0;
                    foreach(var p in a==b?distinct:unrestricted) {
                        if(AcceptedMixed(same,p.Equal,da,db,ref se,ref ge,ref calls)||
                           AcceptedMixed(diff,p.Different,da,db,ref sd,ref gd,ref calls))continue;
                        Console.WriteLine("FOUND INCOMPATIBLE MIXED 2-CUT");
                        Console.WriteLine($"profile {p.ID}, ports {a} {b}, fragment={Format(adj)}");
                        return;
                    }
                }
            }
            Console.WriteLine($"mixed cactus/noncactus order={n}, roots={tested}, solver queries={calls}");
        }
    }
}

