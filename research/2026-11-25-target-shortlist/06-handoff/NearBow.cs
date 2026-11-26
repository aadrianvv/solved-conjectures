
using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private static uint[] Bow() {
        return Make(10, 0,1, 0,2, 0,3, 2,3, 0,4, 0,5, 4,5,
                    1,6, 1,7, 6,7, 1,8, 1,9, 8,9);
    }

    private static uint[] LinkPath(uint[] start, int u, int v, int newVertices) {
        if (newVertices == 0 && (start[u] & (1U << v)) != 0) return null;
        var adj = new uint[start.Length + newVertices];
        Array.Copy(start, adj, start.Length);
        for (int i = start.Length; i < adj.Length; ++i) {
            adj[u] |= 1U << i;
            adj[i] |= 1U << u;
            u = i;
        }
        adj[u] |= 1U << v;
        adj[v] |= 1U << u;
        return adj;
    }

    private static uint[] Unlink(uint[] start, int u, int v) {
        var adj = (uint[])start.Clone();
        adj[u] &= ~(1U << v);
        adj[v] &= ~(1U << u);
        return adj;
    }

    private static uint[] Attach(uint[] start, int root, int kind) {
        int n = start.Length;
        switch (kind) {
        case 0: return LinkPath(start, root, root, 2);
        case 1: return LinkPath(start, root, root, 3);
        case 2: return LinkPath(start, root, root, 4);
        case 3:
            var leaf = new uint[n + 1];
            Array.Copy(start, leaf, n);
            leaf[root] |= 1U << n;
            leaf[n] |= 1U << root;
            return leaf;
        default:
            var spoke = Attach(start, root, 3);
            return LinkPath(spoke, n, n, 2);
        }
    }

    private static bool FindWhole(uint[] adj, HashSet<string> tested, ref long count) {
        if (adj == null || adj.Any(row => BitOperations.PopCount(row) > 8)) return false;
        // Use the labelled adjacency key so no approximation can discard a graph.
        if (tested != null && !tested.Add(string.Join(",", adj))) return false;
        uint seen = 1;
        uint queue = 1;
        while (queue != 0) {
            int v = BitOperations.TrailingZeroCount(queue);
            queue ^= 1U << v;
            uint added = adj[v] & ~seen;
            seen |= added;
            queue |= added;
        }
        if (BitOperations.PopCount(seen) != adj.Length || IsCactus(adj)) return false;
        ++count;
        var g = new Graph(adj);
        var problem = new Problem(g, -1, 3);
        if (problem.Solve(0) != null) return false;
        Console.WriteLine("GRAPH no 3-coloring: " + Format(adj));
        var four = new Problem(g, -1, 4);
        var witness = four.Solve(0);
        Console.WriteLine(witness == null ? "No 4-coloring" : FormatColored(four, witness));
        return true;
    }

    private static IEnumerable<(int u, int v)> Edges(uint[] adj) {
        for (int v = 1; v < adj.Length; ++v)
            for (int u = 0; u < v; ++u)
                if ((adj[u] & (1U << v)) != 0) yield return (u, v);
    }

    private static IEnumerable<uint[]> Ears(uint[] adj, int maxNew) {
        for (int u = 0; u < adj.Length; ++u)
            for (int v = u + 1; v < adj.Length; ++v)
                for (int added = 0; added <= maxNew; ++added) {
                    var ear = LinkPath(adj, u, v, added);
                    if (ear != null) yield return ear;
                }
    }

    private static IEnumerable<uint[]> Subdivide(uint[] graph, (int u, int v)[] edges,
                                                  int slot, int budget) {
        if (budget == 0 || slot >= edges.Length) {
            yield return graph;
            yield break;
        }
        foreach (var sub in Subdivide(graph, edges, slot + 1, budget)) yield return sub;
        var e = edges[slot];
        for (int cost = 1; cost <= budget; ++cost) {
            var added = LinkPath(Unlink(graph, e.u, e.v), e.u, e.v, cost);
            foreach (var sub in Subdivide(added, edges, slot + 1, budget - cost))
                yield return sub;
        }
    }

    public static void NearBow(int seed, int samples) {
        var start = Bow();
        var tested = new HashSet<string>();
        long count = 0;
        foreach (var one in Ears(start, 4)) {
            if (FindWhole(one, tested, ref count)) return;
            foreach (var two in Ears(one, 2))
                if (FindWhole(two, tested, ref count)) return;
        }
        Console.WriteLine("all one/two bounded ears attempted: " + count);
        foreach (var sub in Subdivide(start, Edges(start).ToArray(), 0, 3))
            foreach (var ear in Ears(sub, 2)) {
                if (FindWhole(ear, tested, ref count)) return;
                foreach (var e in Edges(start))
                    if (FindWhole(Unlink(ear, e.u, e.v), tested, ref count)) return;
            }
        Console.WriteLine("all bounded subdivisions and ears, optional deleted original edge attempted: " + count);
        var rng = new Random(seed);
        for (int i = 1; i <= samples; ++i) {
            var current = start;
            for (int changes = rng.Next(1,7); changes > 0 && current.Length < 24; --changes) {
                var edges = Edges(current).ToArray();
                var e = edges[rng.Next(edges.Length)];
                switch (rng.Next(5)) {
                case 0:
                    current = LinkPath(Unlink(current, e.u, e.v), e.u, e.v, rng.Next(1,4));
                    break;
                case 1:
                    current = Unlink(current, e.u, e.v);
                    break;
                case 2:
                case 3:
                    int u = rng.Next(current.Length);
                    int v = rng.Next(current.Length - 1);
                    if (v >= u) ++v;
                    current = LinkPath(current, u, v, rng.Next(0,5)) ?? current;
                    break;
                default:
                    current = Attach(current, rng.Next(current.Length), rng.Next(5));
                    break;
                }
            }
            if (FindWhole(current, null, ref count)) return;
            if (i % 10000 == 0) Console.WriteLine("random near-bow attempts: " + i + ", cumulative checked=" + count);
        }
        Console.WriteLine("no candidates in near-bow checks: " + count);
    }
}

