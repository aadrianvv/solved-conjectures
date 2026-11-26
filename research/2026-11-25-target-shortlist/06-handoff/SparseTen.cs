
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    public static void SparseTen(string folder,int maxDegree,int maxEdges,int minDegree) {
        string input=Path.Combine(folder,"connected-9-max-8-36.txt");
        var seen=new HashSet<ulong>();
        long old=0;
        foreach(string line in File.ReadLines(input)) {
            ulong packed=Convert.ToUInt64(line,16);
            int size=BitOperations.PopCount(packed);
            if(size+minDegree>maxEdges||size+maxDegree<15)continue;
            uint[] adj=Adj(packed,10);
            int max=0;
            uint available=0,required=0;
            for(int v=0;v<9;++v) {
                int d=BitOperations.PopCount(adj[v]);
                max=Math.Max(max,d);
                if(d<maxDegree)available|=1U<<v;
                if(d<minDegree)required|=1U<<v;
            }
            if(max>maxDegree)continue;
            ++old;
            uint optional=available&~required;
            uint added=optional;
            while(true) {
                uint ns=added|required;
                int degree=BitOperations.PopCount(ns);
                if(degree>=minDegree&&degree<=maxDegree&&size+degree>=15&&size+degree<=maxEdges) {
                    var next=(uint[])adj.Clone();
                    next[9]=ns;
                    for(int v=0;v<9;++v)
                        if((ns&(1U<<v))!=0)next[v]|=1U<<9;
                    if(seen.Add(Canonical(next))) {
                        var graph=new Graph(next);
                        var three=new Problem(graph,-1,3);
                        if(three.Solve(0)==null) {
                            Console.WriteLine("NO 3: "+Format(next));
                            var four=new Problem(graph,-1,4);
                            var witness=four.Solve(0);
                            Console.WriteLine(witness==null?"No FOUR":FormatColored(four,witness));
                            return;
                        }
                        if(seen.Count%100000==0)Console.WriteLine($"ten vertex checked={seen.Count}; old visited={old}");
                    }
                }
                if(added==0)break;
                added=(added-1)&optional;
            }
        }
        Console.WriteLine($"TEN vertex sparse exact complete; tested={seen.Count}, parent graphs={old}, min={minDegree}, max={maxDegree}, edges 15..{maxEdges}");
    }
}

