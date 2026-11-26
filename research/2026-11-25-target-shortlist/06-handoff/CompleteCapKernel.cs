
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

public static partial class IrregularSearch {
    private sealed class CompleteCap {
        public int[] Shape;
        public ulong[] States;
    }
    private static bool CapsForKernel(Connector[] kernel,CompleteCap[] caps) {
        var dec=Enumerable.Range(0,caps.Length).Select(_=>Array.Empty<int>()).ToArray();
        var core=MakeHubs(caps.Length,kernel,dec,3);
        ulong[][] raw=caps.Select(x=>x.States).ToArray();
        raw[0]=raw[0].Where(s=>(s&63)<Width).ToArray();
        if(SolveHubs(core,raw,(1U<<caps.Length)-1)!=null)return false;
        Console.WriteLine("INCOMPATIBLE ARBITRARY CACTUS CAPS "+string.Join(",",kernel.Select(x=>x.ToString())));
        foreach(var c in caps)Console.WriteLine(string.Join(",",c.Shape));
        return true;
    }
    public static void OuterCactusCaps(string folder,int trials) {
        string[] text=File.ReadAllLines(Path.Combine(folder,"complete-cactus-caps.txt"));
        var caps=new List<CompleteCap>();
        foreach(string line in text) {
            string[] args=line.Split(' ');
            caps.Add(new CompleteCap {
                Shape=args[0].Split(',').Select(int.Parse).ToArray(),
                States=args[1].Split(',').Select(value=>Convert.ToUInt64(value,16)).ToArray()});
        }
        var k4=SignedCore(0,4).Select(e=>new Connector(e.Item1,e.Item2,1)).ToArray();
        long tested=0;
        for(int a=0;a<caps.Count;++a)for(int b=a;b<caps.Count;++b)
            for(int c=b;c<caps.Count;++c)for(int d=c;d<caps.Count;++d) {
                ++tested;
                if(CapsForKernel(k4,new[]{caps[a],caps[b],caps[c],caps[d]}))return;
                if(tested%10000==0)Console.WriteLine($"K4 arbitrary cap choices={tested}");
            }
        Console.WriteLine($"full direct K4 with any cactus branches tested: {tested}");
        var rng=new Random(20261125);
        (int type,int n)[] shapes={(0,4),(1,6),(2,6),(2,8),(4,10)};
        int[] modes={1,1,1,2,3,4,7};
        for(int i=1;i<=trials;++i) {
            var (kind,n)=shapes[rng.Next(shapes.Length)];
            var core=SignedCore(kind,n).Select(e=>new Connector(e.Item1,e.Item2,modes[rng.Next(modes.Length)])).ToArray();
            var choices=Enumerable.Range(0,n).Select(_=>caps[rng.Next(caps.Count)]).ToArray();
            ++tested;
            if(CapsForKernel(core,choices))return;
            if(i%10000==0)Console.WriteLine($"arbitrary mixed caps={i}, total={tested}");
        }
        Console.WriteLine("checked arbitrary cactus-cap placements: "+tested);
    }
}

