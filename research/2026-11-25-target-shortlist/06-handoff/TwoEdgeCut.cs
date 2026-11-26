
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private const int MaxPortDegree = 8;
    private sealed class Transfer {
        public uint[] Adj;
        public int Left;
        public int Right;
        public ulong Equal;
        public ulong Different;
        public string Key;
    }

    private static ulong TransferMode(Graph graph, int left, int right, int rightColor) {
        var problem = new Problem(graph, left, right, rightColor, 3);
        ulong possible = 0;
        for (int d = 1; d <= graph.Neighbors[left].Length + (left == right ? 2 : 1); ++d) {
            int rightAllowed = -1;
            while (true) {
                var state = problem.SolvePair(1 << d, rightAllowed);
                if (state == null) break;
                int e = left == right ? problem.States[right].SecondCounts[state[right]] : problem.States[right].StubCounts[state[right]];
                possible |= 1UL << (MaxPortDegree * (d - 1) + e - 1);
                rightAllowed &= ~(1 << e);
            }
        }
        return possible;
    }

    private static bool Compatible(ulong a, ulong b) {
        while (a != 0) {
            int bit = BitOperations.TrailingZeroCount(a);
            a ^= 1UL << bit;
            ulong row = 255UL << (8 * (bit / 8));
            ulong col = 0x0101010101010101UL << (bit % 8);
            if ((b & ~(row | col)) != 0) return true;
        }
        return false;
    }

    private static ulong Transpose(ulong mask) {
        ulong result = 0;
        while (mask != 0) {
            int bit = BitOperations.TrailingZeroCount(mask);
            mask ^= 1UL << bit;
            result |= 1UL << (8 * (bit % 8) + bit / 8);
        }
        return result;
    }

    private static uint[] Glue(Transfer a, Transfer b) {
        int size = a.Adj.Length;
        var adj = new uint[size + b.Adj.Length];
        Array.Copy(a.Adj, adj, size);
        for (int i = 0; i < b.Adj.Length; ++i)
            adj[size + i] = b.Adj[i] << size;
        adj[a.Left] |= 1U << (size + b.Left);
        adj[a.Right] |= 1U << (size + b.Right);
        adj[size + b.Left] |= 1U << a.Left;
        adj[size + b.Right] |= 1U << a.Right;
        return adj;
    }

    private static bool TryTransfer(Transfer a, Dictionary<string, Transfer> catalog, ref long checkedPairs) {
        if (catalog.ContainsKey(a.Key)) return false;
        foreach (var b in catalog.Values.Append(a)) {
            ++checkedPairs;
            if (Compatible(a.Equal, b.Equal) || Compatible(a.Different, b.Different)) continue;
            var glued = Glue(a, b);
            if (IsCactus(glued)) continue;
            Console.WriteLine("INCOMPATIBLE TRANSFERS: " + Format(glued));
            Console.WriteLine("left=" + a.Key + " right=" + b.Key);
            var three = new Problem(new Graph(glued), -1, 3);
            Console.WriteLine("direct 3-coloring=" + (three.Solve(0) != null));
            var four = new Problem(new Graph(glued), -1, 4);
            var witness = four.Solve(0);
            Console.WriteLine(witness == null ? "No 4-coloring" : FormatColored(four, witness));
            return true;
        }
        catalog.Add(a.Key, a);
        return false;
    }

    public static void TwoEdgeCut(int maxOrder, string folder) {
        var catalog = new Dictionary<string, Transfer>();
        var graphs = new List<ulong>();
        long rooted = 0;
        long checkedPairs = 0;
        for (int n = 2; n <= maxOrder; ++n) {
            string cache = Path.Combine(folder, "connected-" + n + "-max-7-30.txt");
            foreach (string line in File.ReadLines(cache)) {
                var adj = Adj(Convert.ToUInt64(line, 16), n);
                var graph = new Graph(adj);
                bool cactus = IsCactus(adj);
                string bridge = cactus ? "c" : "n";
                for (int left = 0; left < n; ++left) {
                    for (int right = left + 1; right < n; ++right) {
                        if (graph.Neighbors[left].Length >= MaxPortDegree ||
                            graph.Neighbors[right].Length >= MaxPortDegree) continue;
                        ++rooted;
                        int count = 0;
                        bool hasTwoPaths = TwoAlternatePaths(adj, left, right, 1U << left, ref count);
                        string shape = bridge + (hasTwoPaths ? "m" : "s");
                        ulong a = TransferMode(graph, left, right, 0);
                        ulong b = TransferMode(graph, left, right, 1);
                        var forward = new Transfer {
                            Adj = adj, Left = left, Right = right, Equal = a, Different = b,
                            Key = shape + ":" + a.ToString("X") + ":" + b.ToString("X")
                        };
                        if (TryTransfer(forward, catalog, ref checkedPairs)) return;
                        a = Transpose(a);
                        b = Transpose(b);
                        var backward = new Transfer {
                            Adj = adj, Left = right, Right = left, Equal = a, Different = b,
                            Key = shape + ":" + a.ToString("X") + ":" + b.ToString("X")
                        };
                        if (TryTransfer(backward, catalog, ref checkedPairs)) return;
                    }
                }
            }
            Console.WriteLine($"two-edge cut: n={n} rooted pairs={rooted} states={catalog.Count} comparisons={checkedPairs}");
        }
    }
}


