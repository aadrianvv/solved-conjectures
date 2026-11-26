
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private readonly struct Connector {
        public readonly int U, V, Length;
        public Connector(int u, int v, int length) {
            U = u;
            V = v;
            Length = length;
        }
        public override string ToString() => $"{U}-{V}:{Length}";
    }
    private static bool AllowsPath(int len, int x, int y) {
        int c = x / 16;
        int d = y / 16;
        int a = 1 + x % 16;
        int b = 1 + y % 16;
        bool one = a != 1 && b != 1;
        bool two = a != 2 && b != 2;
        bool mixed = (a != 1 && b != 2) || (a != 2 && b != 1);
        switch (len) {
        case 1: return c == d && a != b;
        case 2: return c == d ? two : one;
        case 3: return c != d && mixed;
        case 4: return one || (c != d && two);
        case 5: return mixed;
                case 6: return one || two;
        default: return c == d || ((a != 1 && b != 3) || (a != 3 && b != 1));
        }
    }

    private sealed class Hub {
        public readonly int[] Other;
        public readonly int[] Reverse;
        public readonly int[] Lengths;
        public readonly int[] Decorations;
        public ulong[] Domain;
        public Hub(int[] other, int[] reverse, int[] lengths, int[] decorations) {
            Other = other;
            Reverse = reverse;
            Lengths = lengths;
            Decorations = decorations;
        }
    }

    private static readonly Dictionary<string, ulong[]> HubStates = new Dictionary<string, ulong[]>();
    private static readonly ulong[,] PathSupport = BuildPathSupport();

    private static ulong[,] BuildPathSupport() {
        var support = new ulong[8,64];
        for (int len = 1; len <= 7; ++len)
            for (int x = 0; x < 64; ++x)
                for (int y = 0; y < 64; ++y)
                    if (AllowsPath(len,x,y)) support[len,x] |= 1UL << y;
        return support;
    }

    private static ulong[] BuildHubDomain(int ports, int[] decorations, int palette) {
        string key = palette + "|" + ports + "|" + string.Join(",",decorations);
        if (HubStates.TryGetValue(key,out var saved)) return saved;
        int degree = ports + decorations.Sum(d => d >= 3 ? 2 : 1);
        var states = GetStates(degree,-1,palette);
        var codes = new HashSet<ulong>();
        foreach (int s in states.IDs) {
            int z = ports;
            bool valid = true;
            foreach (int d in decorations) {
                int x = states.Symbols[z++][s];
                if (d < 3) {
                    if (1 + x % 16 != Math.Abs(d)) continue;
                } else {
                    int y = states.Symbols[z++][s];
                    if (AllowsPath(d,x,y)) continue;
                }
                valid = false;
                break;
            }
            if (!valid) continue;
            ulong code = 0;
            for (int i = 0; i < ports; ++i)
                code |= (ulong)states.Symbols[i][s] << (6 * i);
            codes.Add(code);
        }
        ulong[] result = codes.ToArray();
        HubStates.Add(key,result);
        return result;
    }

    private static Hub[] MakeHubs(int n, Connector[] connectors, int[][] dec, int palette) {
        var neighbor = Enumerable.Range(0,n).Select(_ => new List<int>()).ToArray();
        var reverse = Enumerable.Range(0,n).Select(_ => new List<int>()).ToArray();
        var lengths = Enumerable.Range(0,n).Select(_ => new List<int>()).ToArray();
        foreach (var e in connectors) {
            int uPort = neighbor[e.U].Count;
            int vPort = neighbor[e.V].Count;
            neighbor[e.U].Add(e.V);
            neighbor[e.V].Add(e.U);
            reverse[e.U].Add(vPort);
            reverse[e.V].Add(uPort);
            lengths[e.U].Add(e.Length);
            lengths[e.V].Add(e.Length);
        }
        var hubs = new Hub[n];
        for (int v = 0; v < n; ++v) {
            hubs[v] = new Hub(neighbor[v].ToArray(),reverse[v].ToArray(),lengths[v].ToArray(),dec[v]);
            hubs[v].Domain = BuildHubDomain(hubs[v].Other.Length,dec[v],palette);
        }
        if (hubs[0].Other.Length != 0)
            hubs[0].Domain = hubs[0].Domain.Where(x => (x & 63) < 16).ToArray();
        return hubs;
    }

    private static ulong[] SolveHubs(Hub[] hubs, ulong[][] domains, uint todo) {
        while (todo != 0) {
            int v = BitOperations.TrailingZeroCount(todo);
            todo ^= 1U << v;
            if (domains[v].Length == 0) return null;
            var at = hubs[v];
            for (int p = 0; p < at.Other.Length; ++p) {
                int u = at.Other[p];
                int q = at.Reverse[p];
                int xShift = 6*p;
                int yShift = 6*q;
                int len = at.Lengths[p];
                ulong available = 0;
                foreach (ulong x in domains[v]) available |= 1UL << (int)((x >> xShift) & 63);
                ulong supports = 0;
                while (available != 0) {
                    int x = BitOperations.TrailingZeroCount(available);
                    available ^= 1UL << x;
                    supports |= PathSupport[len,x];
                }
                int cnt = 0;
                foreach (ulong y in domains[u])
                    if ((supports & (1UL << (int)((y >> yShift) & 63))) != 0)
                        ++cnt;
                if (cnt == 0) return null;
                if (cnt == domains[u].Length) continue;
                var reduced = new ulong[cnt];
                int i = 0;
                foreach (ulong y in domains[u])
                    if ((supports & (1UL << (int)((y >> yShift) & 63))) != 0)
                        reduced[i++] = y;
                domains[u] = reduced;
                todo |= 1U << u;
            }
        }
        int vSelected = -1;
        int best = int.MaxValue;
        for (int v = 0; v < domains.Length; ++v) {
            int count = domains[v].Length;
            if (count > 1 && count < best) {
                best = count;
                vSelected = v;
            }
        }
        if (vSelected < 0) return domains.Select(d => d[0]).ToArray();
        foreach (ulong x in domains[vSelected]) {
            var local = (ulong[][])domains.Clone();
            local[vSelected] = new[] {x};
            var result = SolveHubs(hubs,local,1U << vSelected);
            if (result != null) return result;
        }
        return null;
    }
    private static ulong[] SolveHubs(int n, Connector[] connectors, int[][] dec, int palette) {
        var hubs = MakeHubs(n,connectors,dec,palette);
        return SolveHubs(hubs,hubs.Select(h => h.Domain).ToArray(),(1U<<n)-1);
    }

    private static uint[] ExpandSkeleton(int n, Connector[] connectors, int[][] dec) {
        int size = n + connectors.Sum(e => e.Length == 7 ? 5 : e.Length - 1) +
                   dec.Sum(ds => ds.Sum(d => d>=3 ? d-1 : d<0 ? 5 : d));
        if (size > 31) return null;
        var adj = new uint[n];
                foreach (var e in connectors) {
            if (e.Length != 7) {
                adj = LinkPath(adj,e.U,e.V,e.Length-1);
                continue;
            }
            int junction = adj.Length;
            adj = LinkPath(adj,e.U,e.V,1);
            for (int arm = 0; arm < 2; ++arm) {
                int middle = adj.Length;
                adj = Attach(adj,junction,3);
                adj = Attach(adj,middle,3);
            }
        }
        for (int v = 0; v < n; ++v) {
            foreach (int d in dec[v]) {
                                if (d < 0) {
                    int cap = adj.Length;
                    adj = Attach(adj,v,3);
                    adj = Attach(adj,cap,0);
                    adj = Attach(adj,cap,0);
                }
                else if (d >= 3) adj = LinkPath(adj,v,v,d-1);
                else if (d == 1) adj = Attach(adj,v,3);
                else {
                    int end = adj.Length;
                    adj = Attach(adj,v,3);
                    adj = Attach(adj,end,3);
                }
            }
        }
        return adj;
    }

    private static bool CheckHub(int n, Connector[] connectors, int[][] dec, ref long count) {
        ++count;
        if (SolveHubs(n,connectors,dec,3) != null) return false;
        Console.WriteLine($"PORT COUNTEREXAMPLE n={n}, connectors={string.Join(",",connectors.Select(e=>e.ToString()))}");
        Console.WriteLine("decorations=" + string.Join(";",dec.Select(ds=>string.Join(",",ds))));
        Console.WriteLine("compressed four-colouring=" + (SolveHubs(n,connectors,dec,4) != null));
        var full = ExpandSkeleton(n,connectors,dec);
        if (full != null) {
            Console.WriteLine("expanded: " + Format(full));
            Console.WriteLine("cactus=" + IsCactus(full));
            var four = new Problem(new Graph(full), -1, 4);
            var witness = four.Solve(0);
            Console.WriteLine(witness == null ? "No 4-coloring" : FormatColored(four,witness));
        }
        return true;
    }

    private static readonly int[][] FewDecorations = new [] {
        Array.Empty<int>(),new[]{1},new[]{2},new[]{3},new[]{3,3},new[]{1,3},new[]{2,3}
    };
    private static readonly int[][] MoreDecorations = new [] {
        Array.Empty<int>(),Array.Empty<int>(),new[]{1},new[]{2},new[]{3},new[]{3,3},
        new[]{1,3},new[]{2,3},new[]{4},new[]{5},new[]{6},new[]{1,2},new[]{1,1},new[]{2,2},
        new[]{1,1,3},new[]{2,2,3},new[]{3,4},new[]{3,5}
    };

    public static void SkeletonSearch(int seed, int trials) {
        long total = 0;
        var bridge = new [] {new Connector(0,1,1)};
        int[][] bow = new [] {new[]{3,3},new[]{3,3}};
        Console.WriteLine("compressed bow tie 3-colour="+(SolveHubs(2,bridge,bow,3)!=null) +
                          " 4-colour="+(SolveHubs(2,bridge,bow,4)!=null));
        var baseEdges = new Connector[4];
        for (int x = 1; x <= 6; ++x)
            for (int y = Math.Max(x,2); y <= 6; ++y)
                for (int z = 1; z <= 6; ++z)
                    for (int w = 1; w <= 6; ++w) {
                        baseEdges[0] = new Connector(0,1,x);
                        baseEdges[1] = new Connector(0,1,y);
                        baseEdges[2] = new Connector(0,2,z);
                        baseEdges[3] = new Connector(1,2,w);
                        foreach (int[] a in FewDecorations)
                            foreach (int[] b in FewDecorations)
                                foreach (int[] c in FewDecorations) {
                                    if (c.Length == 0) continue;
                                    if (CheckHub(3,baseEdges,new[]{a,b,c},ref total)) return;
                                }
                    }
        Console.WriteLine($"exhausted decorated 3-hub theta: {total}");
        Random rng = new Random(seed);
        for (int test = 1; test <= trials; ++test) {
            int n = rng.Next(3,8);
            var degree = new int[n];
            var edges = new List<Connector>();
            bool[,] direct = new bool[n,n];
            for (int v = 0; v < n; ++v) {
                int u = (v+1)%n;
                int len = rng.Next(1,7);
                edges.Add(new Connector(u,v,len));
                if (len == 1) direct[u,v]=direct[v,u]=true;
                ++degree[u];
                ++degree[v];
            }
            for (int j = rng.Next(1,n+2); j>0; --j) {
                int u = rng.Next(n);
                int v = rng.Next(n-1);
                if (v >= u) ++v;
                if (degree[u] >= 7 || degree[v] >= 7) continue;
                int len = rng.Next(direct[u,v] ? 2 : 1,7);
                edges.Add(new Connector(u,v,len));
                if (len == 1) direct[u,v]=direct[v,u]=true;
                ++degree[u];
                ++degree[v];
            }
            var dec = new int[n][];
            for (int v = 0; v < n; ++v) {
                do {
                    dec[v] = MoreDecorations[rng.Next(MoreDecorations.Length)];
                } while (degree[v] + dec[v].Sum(d=>d>=3?2:1) > 8);
            }
            if (CheckHub(n,edges.ToArray(),dec,ref total)) return;
            if (test % 10000 == 0) Console.WriteLine($"random hub skeleton tests={test}, total={total}");
        }
        Console.WriteLine($"skeleton search complete, total={total}");
    }
}



