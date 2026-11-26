
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private sealed class Series {
        public Transfer Leaf;
        public Series A;
        public Series B;
        public ulong Equal;
        public ulong Different;
        public int Size;
        public bool HasOverlappingCycle;
        public bool SameRoot;
        public bool ClosingEdgePresent;
        public bool Active = true;
        public int Class => (HasOverlappingCycle ? 1 : 0) + (SameRoot ? 2 : 0) +
                            (ClosingEdgePresent ? 4 : 0);
    }
    private static ulong ComposeMode(ulong a, ulong b) {
        ulong result = 0;
        for (int left = 0; left < 8; ++left) {
            int rowA = (int)(255UL & (a >> (8 * left)));
            if (rowA == 0) continue;
            int singleton = (rowA & (rowA - 1)) == 0 ? BitOperations.TrailingZeroCount((uint)rowA) : -1;
            int column = 0;
            for (int right = 0; right < 8; ++right)
                if (right != singleton)
                    column |= (int)(255UL & (b >> (8 * right)));
            result |= (ulong)column << (8 * left);
        }
        return result;
    }
    private static Series Compose(Series a, Series b) {
        ulong dd = ComposeMode(a.Different, b.Different);
        return new Series {
            A = a, B = b, Size = a.Size + b.Size,
            HasOverlappingCycle = a.HasOverlappingCycle || b.HasOverlappingCycle,
            SameRoot = false, ClosingEdgePresent = a.SameRoot && b.SameRoot,
            Equal = dd | ComposeMode(a.Equal, b.Equal),
            Different = dd | ComposeMode(a.Different, b.Equal) | ComposeMode(a.Equal, b.Different)
        };
    }
    private static (int first, int last) Unpack(Series x, uint[] adj, ref int offset) {
        if (x.Leaf != null) {
            int start = offset;
            for (int v = 0; v < x.Leaf.Adj.Length; ++v)
                adj[start + v] = x.Leaf.Adj[v] << start;
            offset += x.Leaf.Adj.Length;
            return (start + x.Leaf.Left, start + x.Leaf.Right);
        }
        var a = Unpack(x.A, adj, ref offset);
        var b = Unpack(x.B, adj, ref offset);
        adj[a.last] |= 1U << b.first;
        adj[b.first] |= 1U << a.last;
        return (a.first, b.last);
    }
    private static bool AddSeries(Series x, List<Series> options, Queue<Series> pending) {
        const ulong diagonal = 0x8040201008040201UL;
        if (x.HasOverlappingCycle && !x.SameRoot && !x.ClosingEdgePresent &&
            (x.Equal & ~diagonal) == 0) {
            uint[] adj = new uint[x.Size];
            int offset = 0;
            var ends = Unpack(x, adj, ref offset);
            adj[ends.first] |= 1U << ends.last;
            adj[ends.last] |= 1U << ends.first;
            Console.WriteLine($"INCOMPATIBLE SERIES (n={x.Size}): " + Format(adj));
            var three = new Problem(new Graph(adj), -1, 3);
            Console.WriteLine("direct 3-coloring=" + (three.Solve(0) != null));
            var four = new Problem(new Graph(adj), -1, 4);
            var witness = four.Solve(0);
            Console.WriteLine(witness == null ? "No 4-coloring" : FormatColored(four, witness));
            return true;
        }
        foreach (var y in options)
            if (y.Active && y.Class == x.Class && y.Size <= x.Size &&
                (y.Equal & ~x.Equal) == 0 && (y.Different & ~x.Different) == 0)
                return false;
        foreach (var y in options)
            if (y.Active && y.Class == x.Class && x.Size <= y.Size &&
                (x.Equal & ~y.Equal) == 0 && (x.Different & ~y.Different) == 0)
                y.Active = false;
        options.Add(x);
        pending.Enqueue(x);
        return false;
    }
    private static bool AddLeaf(uint[] adj, Graph graph, int left, int right, bool cactus,
                                List<Series> options, Queue<Series> pending) {
        int count = 0;
        bool multiple = left != right &&
            TwoAlternatePaths(adj, left, right, 1U << left, ref count);
        var t = new Transfer {
            Adj = adj, Left = left, Right = right,
            Equal = TransferMode(graph, left, right, 0),
            Different = TransferMode(graph, left, right, 1)
        };
        var x = new Series {
            Leaf = t, Size = adj.Length, SameRoot = left == right,
            ClosingEdgePresent = (adj[left] & (1U << right)) != 0,
            HasOverlappingCycle = !cactus || multiple,
            Equal = t.Equal, Different = t.Different
        };
        if (AddSeries(x, options, pending)) return true;
        if (left == right || (t.Equal == Transpose(t.Equal) &&
                              t.Different == Transpose(t.Different))) return false;
        var s = new Transfer {
            Adj = adj, Left = right, Right = left, Equal = Transpose(t.Equal),
            Different = Transpose(t.Different)
        };
        return AddSeries(new Series {
            Leaf = s, Size = x.Size, SameRoot = false,
            ClosingEdgePresent = x.ClosingEdgePresent,
            HasOverlappingCycle = x.HasOverlappingCycle,
            Equal = s.Equal, Different = s.Different
        }, options, pending);
    }
    public static void SeriesClosure(int maxOrder, int maxSize, string folder) {
        var options = new List<Series>();
        var pending = new Queue<Series>();
        var one = new uint[1];
        if (AddLeaf(one, new Graph(one), 0, 0, true, options, pending)) return;
        Console.WriteLine("isolated two-stub control eq=" + EqualPairs(options[0].Equal) +
                          " neq=" + EqualPairs(options[0].Different));
        long pairs = 1;
        for (int n = 2; n <= maxOrder; ++n) {
            string cache = Path.Combine(folder, "connected-" + n + "-max-7-30.txt");
            foreach (string line in File.ReadLines(cache)) {
                var adj = Adj(Convert.ToUInt64(line, 16), n);
                var graph = new Graph(adj);
                bool cactus = IsCactus(adj);
                for (int left = 0; left < n; ++left)
                    for (int right = left; right < n; ++right) {
                        if (graph.Neighbors[left].Length + (left == right ? 2 : 1) > 8 ||
                            graph.Neighbors[right].Length + (left == right ? 2 : 1) > 8)
                            continue;
                        ++pairs;
                        if (AddLeaf(adj, graph, left, right, cactus, options, pending)) return;
                    }
            }
            Console.WriteLine($"series seeds n={n} pairs={pairs}, antichain={options.Count(x => x.Active)}");
        }
        var b = Bow();
        foreach (var e in Edges(b)) {
            if (e.u == 0 && e.v == 1) continue;
            var minus = Unlink(b, e.u, e.v);
            if (AddLeaf(minus, new Graph(minus), e.u, e.v, true, options, pending)) return;
        }
        long compositions = 0;
        while (pending.Count > 0) {
            Series a = pending.Dequeue();
            if (!a.Active) continue;
            var earlier = options.Where(x => x.Active && a.Size + x.Size <= maxSize).ToArray();
            foreach (var x in earlier) {
                ++compositions;
                if (AddSeries(Compose(a, x), options, pending)) return;
                ++compositions;
                if (AddSeries(Compose(x, a), options, pending)) return;
            }
        }
        Console.WriteLine($"closure complete, {compositions} compositions with size≤{maxSize}, {options.Count(x => x.Active)} minimal profiles");
    }
}

