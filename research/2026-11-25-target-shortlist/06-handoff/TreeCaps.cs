
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    private static StarCap TreeCap(int one,int two) {
        var found=new HashSet<ulong>();
        int total=one+two;
        foreach(var ports in PortPatterns) {
            var portCounts=new int[3];
            foreach(int c in ports)++portCounts[c];
            for(int a=0;a<=total;++a)for(int b=0;b<=total-a;++b) {
                int[] slot=new[]{a,b,total-a-b};
                int[] degrees=new int[3];
                int avoidOne=0,avoidTwo=0;
                for(int c=0;c<3;++c) {
                    degrees[c]=slot[c]+portCounts[c];
                    if(degrees[c]==1)avoidOne+=slot[c];
                    if(degrees[c]==2)avoidTwo+=slot[c];
                }
                if(one>total-avoidOne||two>total-avoidTwo)continue;
                foreach(var permutation in PalettePermutations) {
                    ulong code=0;
                    for(int p=0;p<3;++p) {
                        int c=ports[p];
                        int symbol=Width*permutation[c]+degrees[c]-1;
                        code|=(ulong)symbol<<(6*p);
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
        return new StarCap{Adj=adj,Root=0,Domain=found,States=found.ToArray()};
    }
    private static bool CheckTreeKernel(Connector[] kernel,StarCap[] caps,ref long calls) {
        var covered=new ulong[(1<<(2*kernel.Length))/64];
        var empty=Enumerable.Range(0,caps.Length).Select(_=>Array.Empty<int>()).ToArray();
        var domains=caps.Select(c=>c.States).ToArray();
        domains[0]=domains[0].Where(code=>(code&63)<Width).ToArray();
        var mode=new int[kernel.Length];
        var slots=new int[caps.Length];
        for(int w=0;w<covered.Length*64;++w) {
            if((covered[w>>6]&(1UL<<(w&63)))!=0)continue;
            int tmp=w;
            for(int e=kernel.Length-1;e>=0;--e) {
                var link=kernel[e];
                kernel[e]=new Connector(link.U,link.V,1+(tmp&3));
                tmp>>=2;
            }
            var hubs=MakeHubs(caps.Length,kernel,empty,3);
            ++calls;
            var colored=SolveHubs(hubs,(ulong[][])domains.Clone(),(1U<<caps.Length)-1);
            if(colored==null) {
                long ignores=0;
                return TestCaps(kernel,caps,ref ignores);
            }
            Array.Clear(slots,0,slots.Length);
            for(int e=0;e<kernel.Length;++e) {
                var link=kernel[e];
                int x=(int)((colored[link.U]>>(6*slots[link.U]++))&63);
                int y=(int)((colored[link.V]>>(6*slots[link.V]++))&63);
                mode[e]=0;
                for(int len=1;len<=4;++len)if(AllowsPath(len,x,y))mode[e]|=1<<(len-1);
                if((mode[e]&(1<<(link.Length-1)))==0)
                    throw new InvalidOperationException("Witness did not cover its own connector.");
            }
            CoverWords(covered,mode,0,0);
        }
        return false;
    }
    public static void K4TreeArms() {
        var caps=new List<StarCap>();
        for(int q=0;q<=11;++q)for(int a=0;a<=q;++a)InsertCap(TreeCap(a,q-a),caps);
        Console.WriteLine($"K4 kernel: {caps.Count} minimal caps among 78 bounded tree-arm patterns");
        var kernel=SignedCore(0,4).Select(e=>new Connector(e.Item1,e.Item2,1)).ToArray();
        long cases=0,calls=0;
        for(int a=0;a<caps.Count;++a)
            for(int b=a;b<caps.Count;++b)
                for(int c=b;c<caps.Count;++c)
                    for(int d=c;d<caps.Count;++d) {
                        if(CheckTreeKernel(kernel,new[]{caps[a],caps[b],caps[c],caps[d]},ref calls))return;
                        ++cases;
                        if(cases%1000==0)Console.WriteLine($"K4 tree-arm assignments={cases}; witnesses={calls}");
                    }
        Console.WriteLine($"K4 arbitrary tree-arm screen complete: {cases} hub assignments; witnesses={calls}");
    }
}

