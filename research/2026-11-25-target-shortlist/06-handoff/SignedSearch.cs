
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private static (int,int)[] SignedCore(int kind,int n) {
        var result=new List<(int,int)>();
        var seen=new HashSet<(int,int)>();
        Action<int,int> add=(int a,int b)=>{
            var pair=a<b?(a,b):(b,a);
            if(seen.Add(pair))result.Add(pair);
        };
        if(kind==0) {
            for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)add(a,b);
        } else if(kind==1) {
            for(int a=0;a<n/2;++a)for(int b=n/2;b<n;++b)add(a,b);
        } else if(kind==2) {
            for(int a=0;a<n/2;++a) {
                add(a,(a+1)%(n/2));
                add(a+n/2,(a+1)%(n/2)+n/2);
                add(a,a+n/2);
            }
        } else if(kind==3) {
            for(int a=0;a<n;++a) {
                add(a,(a+1)%n);
                add(a,(a+n/2)%n);
            }
        } else {
            for(int a=0;a<n/2;++a) {
                add(a,(a+1)%(n/2));
                add(a+n/2,(a+2)%(n/2)+n/2);
                add(a,a+n/2);
            }
        }
        return result.ToArray();
    }

    public static void SignedSearch(int seed,int attempts) {
        var shapes=new (int kind,int n)[] {
            (0,4),(1,6),(2,6),(2,8),(3,8),(2,10),(3,10),(4,10),
            (2,12),(3,12),(4,12)
        };
        var modes=new[]{1,2,3,3,3,4,7,7,7};
        var rng=new Random(seed);
        long total=0;
        foreach(var (kind,n) in shapes) {
            var type=SignedCore(kind,n);
            var dec=Enumerable.Range(0,n).Select(_=>Array.Empty<int>()).ToArray();
            var edges=new Connector[type.Length];
            for(int word=0;word<(1<<type.Length);++word) {
                for(int i=0;i<type.Length;++i)
                    edges[i]=new Connector(type[i].Item1,type[i].Item2,(word&(1<<i))==0?3:7);
                if(CheckHub(n,edges,dec,ref total))return;
            }
            Console.WriteLine($"signed cubic core {kind},{n} exhausted; total={total}");
        }
        for(int iter=1;iter<=attempts;++iter) {
            var (kind,n)=shapes[rng.Next(shapes.Length)];
            var type=SignedCore(kind,n);
            var edges=type.Select(x=>new Connector(x.Item1,x.Item2,modes[rng.Next(modes.Length)])).ToArray();
            int[][] dec=new int[n][];
            for(int v=0;v<n;++v)
                dec[v]=rng.Next(3)==0?MoreDecorations[rng.Next(MoreDecorations.Length)]:Array.Empty<int>();
            if(CheckHub(n,edges,dec,ref total))return;
            if(iter%10000==0) Console.WriteLine($"signed random={iter}, total={total}");
        }
        Console.WriteLine($"signed completed, total={total}");
    }
}

