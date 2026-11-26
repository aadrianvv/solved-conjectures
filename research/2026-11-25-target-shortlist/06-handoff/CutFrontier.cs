
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private static bool SameCutClass(Series a,Series b) =>
        a.HasOverlappingCycle==b.HasOverlappingCycle && a.SameRoot==b.SameRoot;

    private static bool CutCompat(Series a,Series b) =>
        Compatible(a.Equal,b.Equal)||Compatible(a.Different,b.Different);

    private static bool AddCut(Series state,List<Series> active,Queue<Series> pending) {
        foreach(var old in active) {
            if(SameCutClass(old,state)&&(old.Equal&~state.Equal)==0&&
               (old.Different&~state.Different)==0) return false;
        }
        foreach(var b in active.Append(state)) {
            if(!(state.HasOverlappingCycle||b.HasOverlappingCycle)||state.SameRoot&&b.SameRoot)
                continue;
            if(CutCompat(state,b))continue;
            Console.WriteLine("INCOMPATIBLE TWO-CUT FRAGMENTS");
            ShowCut(state);
            ShowCut(b);
            int size=state.Size+b.Size;
            if(size<=31) {
                var data=new uint[size];
                int offset=0;
                var a=Unpack(state,data,ref offset);
                var c=Unpack(b,data,ref offset);
                data[a.first]|=1U<<c.first;
                data[c.first]|=1U<<a.first;
                data[a.last]|=1U<<c.last;
                data[c.last]|=1U<<a.last;
                Console.WriteLine("expanded "+Format(data));
                Console.WriteLine("is cactus="+IsCactus(data));
                var g=new Graph(data);
                Console.WriteLine("direct 3-colouring="+(new Problem(g,-1,3).Solve(0)!=null));
                var four = new Problem(g,-1,4);
                var witness=four.Solve(0);
                Console.WriteLine(witness==null?"no 4-coloring":FormatColored(four,witness));
            }
            return true;
        }
        foreach(var old in active.Where(old=>SameCutClass(old,state)&&
                    (state.Equal&~old.Equal)==0&&(state.Different&~old.Different)==0).ToArray()) {
            active.Remove(old);
            old.Active=false;
        }
        active.Add(state);
        pending.Enqueue(state);
        return false;
    }

    private static void ShowCut(Series cap) {
        if(cap.Leaf!=null) {
            Console.WriteLine($"ports {cap.Leaf.Left},{cap.Leaf.Right}/{cap.Size}: {Format(cap.Leaf.Adj)}");
            return;
        }
        ShowCut(cap.A);
        ShowCut(cap.B);
    }
    private static bool HasModes(Problem problem,ulong modes,ref ulong checkedModes,
                                 ref ulong possibleModes,ref long solves) {
        while(modes!=0) {
            int bit=BitOperations.TrailingZeroCount(modes);
            ulong flag=1UL<<bit;
            modes^=flag;
            if((checkedModes&flag)==0) {
                ++solves;
                checkedModes|=flag;
                if(problem.SolvePair(1<<(bit/8+1),1<<(bit%8+1))!=null)
                    possibleModes|=flag;
            }
            if((possibleModes&flag)==0)return false;
        }
        return true;
    }

    private static bool CutSeed(uint[] adj,Graph graph,int left,int right,bool danger,
                                List<Series> active,Queue<Series> pending,
                                ref long solves,ref long full) {
        int dt=(left==right?2:1);
        int lmax=graph.Neighbors[left].Length+dt;
        int rmax=graph.Neighbors[right].Length+dt;
        ulong local=0;
        for(int a=0;a<lmax;++a)for(int b=0;b<rmax;++b)local|=1UL<<(8*a+b);
        ulong potential=~local;
        var same=new Problem(graph,left,right,0,3);
        var diff=new Problem(graph,left,right,1,3);
        ulong checkedSame=potential, checkedDiff=potential;
        ulong gotSame=0,gotDiff=0;
        var baseShape=new Series{SameRoot=left==right,HasOverlappingCycle=danger};
        foreach(var rep in active.Where(x=>SameCutClass(x,baseShape))
                                 .OrderBy(x=>BitOperations.PopCount(x.Equal)+BitOperations.PopCount(x.Different))) {
            if((rep.Equal&potential)!=0||(rep.Different&potential)!=0)continue;
            if(HasModes(same,rep.Equal,ref checkedSame,ref gotSame,ref solves)&&
               HasModes(diff,rep.Different,ref checkedDiff,ref gotDiff,ref solves))
                return false;
        }

        ++full;
        for(int a=1;a<=lmax;++a) {
            for(int b=1;b<=rmax;++b) {
                ulong pair=1UL<<(8*(a-1)+b-1);
                HasModes(same,pair,ref checkedSame,ref gotSame,ref solves);
                HasModes(diff,pair,ref checkedDiff,ref gotDiff,ref solves);
            }
        }
        var leaf=new Transfer{Adj=adj,Left=left,Right=right,Equal=gotSame,Different=gotDiff};
        baseShape.Leaf=leaf;
        baseShape.Equal=gotSame;
        baseShape.Different=gotDiff;
        baseShape.Size=adj.Length;
        return AddCut(baseShape,active,pending);
    }

    private static bool CloseCuts(List<Series> active,Queue<Series> pending,ref long trials) {
        while(pending.Count>0) {
            var a=pending.Dequeue();
            if(!a.Active)continue;
            foreach(var b in active.ToArray()) {
                ++trials;
                if(AddCut(Compose(a,b),active,pending))return true;
                ++trials;
                if(AddCut(Compose(b,a),active,pending))return true;
            }
        }
        return false;
    }

    public static void CutFrontier(int order,string folder) {
        long seeded=0,solved=0,full=0,tried=0;
        var active=new List<Series>();
        var pending=new Queue<Series>();
        var single=new uint[1];
        if(CutSeed(single,new Graph(single),0,0,false,active,pending,ref solved,ref full))
            return;
        for(int n=2;n<=order;++n) {
            string input=Path.Combine(folder,"connected-"+n+"-max-7-30.txt");
            foreach(string line in File.ReadLines(input)) {
                var adj=Adj(Convert.ToUInt64(line,16),n);
                var g=new Graph(adj);
                bool nc=!IsCactus(adj);
                for(int a=0;a<n;++a)for(int b=0;b<n;++b) {
                    int extra=a==b?2:1;
                    if(g.Neighbors[a].Length+extra>8||g.Neighbors[b].Length+extra>8)continue;
                    ++seeded;
                    int alternatives=0;
                    bool danger=nc||a!=b&&TwoAlternatePaths(adj,a,b,1U<<a,ref alternatives);
                    if(CutSeed(adj,g,a,b,danger,active,pending,ref solved,ref full))return;
                }
            }
            Console.WriteLine($"weak-parent filters order={n}: seeds={seeded}, prototype tests={solved}, exact new profiles={full}, minima={active.Count}");
            if(CloseCuts(active,pending,ref tried))return;
            Console.WriteLine($"closure order={n}: minima={active.Count} exact compositions={tried}");
        }
        foreach(var s in active.OrderBy(x=>x.SameRoot).ThenBy(x=>x.HasOverlappingCycle)
                 .ThenBy(x=>x.Equal).ThenBy(x=>x.Different)) {
            Console.WriteLine($"frontier danger={s.HasOverlappingCycle} same={s.SameRoot} order={s.Size} " +
                              $"eq {EqualPairs(s.Equal)} diff {EqualPairs(s.Different)}");
            ShowCut(s);
        }
    }
}

