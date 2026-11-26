
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private static bool K4Grid(int slot,Connector[] edges,int[][] decorations,ref long total) {
        if (slot==edges.Length) {
            return CheckHub(4,edges,decorations,ref total);
        }
        var edge=edges[slot];
        for (int len=1;len<=6;++len) {
            edges[slot]=new Connector(edge.U,edge.V,len);
            if (K4Grid(slot+1,edges,decorations,ref total))return true;
        }
        return false;
    }
    public static void K4Search(int count) {
        var ks=(from v in Enumerable.Range(1,3)
                from u in Enumerable.Range(0,v)
                select new Connector(u,v,1)).ToArray();
        int[][] settings=new[]{Array.Empty<int>(),new[]{3},new[]{3,3}};
        long total=0;
        int i=0;
        for(int a=0;a<3;++a)for(int b=a;b<3;++b)
            for(int c=b;c<3;++c)for(int d=c;d<3;++d) {
                ++i;
                if(i>count) break;
                if(K4Grid(0,ks,new[]{settings[a],settings[b],settings[c],settings[d]},ref total))return;
                Console.WriteLine($"K4 petals ({a},{b},{c},{d}), total={total}");
            }
        Console.WriteLine("completed mixed K4 scan; checked="+total);
    }
}

