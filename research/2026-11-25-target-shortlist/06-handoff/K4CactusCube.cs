using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static class K4CactusCube
{
    private sealed class ArrayComparer : IEqualityComparer<int[]>
    {
        public bool Equals(int[] left, int[] right) => left.AsSpan().SequenceEqual(right);

        public int GetHashCode(int[] row)
        {
            unchecked
            {
                int hash = 17;
                foreach (int id in row) hash = 31 * hash + id;
                return hash;
            }
        }
    }

    private sealed record Branch(int[] Children, long Count);

    private sealed class Frontier
    {
        private readonly int[] widths;
        private readonly List<Branch>[] branches;
        private readonly Dictionary<int[], int>[] seen;
        private readonly Dictionary<long, int> removing = new();
        private readonly Dictionary<(int, int), int> seeding = new();
        private readonly ulong[] patterns;
        private readonly bool[] fullSuffix;
        public int Root;

        public Frontier(int capCount)
        {
            widths = new[] { capCount, capCount, capCount, capCount, 8, 8, 8, 8, 8, 8 };
            branches = widths.Select(n => new List<Branch> { new Branch(new int[n], 0) }).ToArray();
            seen = widths.Select(n => new Dictionary<int[], int>(new ArrayComparer())).ToArray();
            patterns = new ulong[widths.Length];
            fullSuffix = new bool[widths.Length + 1];
            fullSuffix[widths.Length] = true;
            Root = Seed(0, 0);
        }

        public long Count => Size(0, Root);
        public int Stored => branches.Sum(bins => bins.Count);

        private long Size(int depth, int id)
        {
            if (id == 0) return 0;
            return depth == widths.Length ? 1 : branches[depth][id].Count;
        }

        private int Intern(int depth, int[] children)
        {
            long count = children.Sum(id => Size(depth + 1, id));
            if (count == 0) return 0;
            if (seen[depth].TryGetValue(children, out int existing)) return existing;
            int index = branches[depth].Count;
            branches[depth].Add(new Branch(children, count));
            seen[depth].Add(children, index);
            return index;
        }

        private int Seed(int depth, int minimum)
        {
            if (depth == widths.Length) return 1;
            if (seeding.TryGetValue((depth,minimum), out int existing)) return existing;
            var options = new int[widths[depth]];
            for (int i = minimum; i < options.Length; ++i)
                options[i] = Seed(depth + 1, depth < 3 ? i : 0);
            int index = Intern(depth, options);
            seeding.Add((depth, minimum), index);
            return index;
        }

        public void First(int[] selected)
        {
            int node = Root;
            for (int depth = 0; depth < selected.Length; ++depth)
            {
                int[] children = branches[depth][node].Children;
                int first = Array.FindIndex(children, child => child != 0);
                selected[depth] = first;
                node = children[first];
            }
        }

        private int Remove(int depth, int id)
        {
            if (id == 0 || fullSuffix[depth]) return 0;
            long key = (long)depth << 32 | (uint)id;
            if (removing.TryGetValue(key, out int previous)) return previous;
            int[] old = branches[depth][id].Children;
            int[] modified = old;
            ulong included = patterns[depth];
            while (included != 0)
            {
                int i = BitOperations.TrailingZeroCount(included);
                included &= included - 1;
                if (old[i] == 0) continue;
                int child = Remove(depth + 1, old[i]);
                if (child == old[i]) continue;
                if (modified == old) modified = (int[])old.Clone();
                modified[i] = child;
            }
            int answer = modified == old ? id : Intern(depth, modified);
            removing.Add(key, answer);
            return answer;
        }

        public void RemoveCube(ulong[] cube)
        {
            for (int i = widths.Length - 1; i >= 0; --i)
            {
                patterns[i] = cube[i];
                fullSuffix[i] = fullSuffix[i+1] && cube[i] == (1UL << widths[i]) - 1;
            }
            removing.Clear();
            Root = Remove(0, Root);
        }

        public void Compact()
        {
            var remap = new Dictionary<int, int>[widths.Length];
            for (int i = 0; i < widths.Length; ++i)
                remap[i] = new Dictionary<int, int> { [0] = 0 };
            int Visit(int depth, int id)
            {
                if (depth == widths.Length) return id;
                if (remap[depth].TryGetValue(id, out int previous)) return previous;
                remap[depth][id] = remap[depth].Count;
                foreach (int child in branches[depth][id].Children)
                    Visit(depth + 1, child);
                return remap[depth][id];
            }
            Root = Visit(0, Root);
            for (int depth = 0; depth < widths.Length; ++depth)
            {
                List<Branch> original = branches[depth];
                branches[depth] = new List<Branch>();
                seen[depth].Clear();
                foreach (var pair in remap[depth])
                {
                    Branch old = original[pair.Key];
                    int[] row = depth == widths.Length - 1 ? old.Children
                        : old.Children.Select(id => remap[depth + 1][id]).ToArray();
                    branches[depth].Add(new Branch(row, old.Count));
                    if (pair.Value != 0) seen[depth].Add(row, pair.Value);
                }
            }
        }
    }

    private static readonly (int,int)[] Edges = {(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)};
    private static readonly int[,] Positions = {{-1,0,1,2},{0,-1,1,2},{0,1,-1,2},{0,1,2,-1}};
    private static readonly int[,] EdgeIndex = {{-1,0,1,2},{0,-1,3,4},{1,3,-1,5},{2,4,5,-1}};

    private static int Symbol(int state, int position) => state >> (position * 6) & 63;

    private static bool Canonical(int state)
    {
        int next = 0;
        for (int i = 0; i < 3; ++i)
        {
            int color = Symbol(state,i)/20;
            if (color > next) return false;
            if (color == next) ++next;
        }
        return true;
    }

    private static bool Search(int v, int[] word, int[] chosen, int[][] capDomains, byte[][] modes)
    {
        if (v == 4) return true;
        foreach (int state in capDomains[word[v]])
        {
            if (v == 0 && !Canonical(state)) continue;
            bool valid = true;
            for (int u = 0; u < v; ++u)
            {
                int x = Symbol(chosen[u], Positions[u,v]);
                int y = Symbol(state, Positions[v,u]);
                if ((modes[x][y] & (1 << word[4 + EdgeIndex[u,v]])) == 0)
                {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;
            chosen[v] = state;
            if (Search(v + 1, word, chosen, capDomains, modes)) return true;
        }
        return false;
    }

    public static void Check(string folder)
    {
        int[][] domains = File.ReadLines(Path.Combine(folder,"k4-cactus-domains.txt"))
            .Select(line => line.Split(',').Select(int.Parse).ToArray()).ToArray();
        byte[][] modes = File.ReadLines(Path.Combine(folder,"k4-cactus-edge-table.txt"))
            .Select(line => line.Split(',').Select(byte.Parse).ToArray()).ToArray();
        for (int x=0; x<modes.Length; ++x)
            for (int y=0; y<modes.Length; ++y)
                if (modes[x][y] != modes[y][x]) throw new InvalidOperationException("Nonsymmetric modes");
        var uses = new Dictionary<int, ulong>();
        for (int i = 0; i < domains.Length; ++i)
            foreach (int state in domains[i]) uses[state] = uses.GetValueOrDefault(state) | (1UL << i);
        for (int i = 0; i < domains.Length; ++i)
            domains[i] = domains[i].OrderByDescending(state => BitOperations.PopCount(uses[state])).ToArray();
        var perms = (from a in Enumerable.Range(0,4) from b in Enumerable.Range(0,4)
                     from c in Enumerable.Range(0,4) from d in Enumerable.Range(0,4)
                     where new[] {a,b,c,d}.Distinct().Count() == 4 select new[] {a,b,c,d}).ToArray();
        var frontier = new Frontier(domains.Length);
        Console.WriteLine("initial K4 combinations: " + frontier.Count);
        var watch = System.Diagnostics.Stopwatch.StartNew();
        var word = new int[10];
        var chosen = new int[4];
        var witness = new ulong[10];
        var permuted = new ulong[10];
        long steps = 0; var certificate = new List<string>();
        while (frontier.Count != 0)
        {
            frontier.First(word);
            if (!Search(0, word, chosen, domains, modes))
            {
                Console.WriteLine("INCOMPATIBLE normalized K4 " + string.Join(",", word));
                return;
            }
            certificate.Add(string.Join(',', chosen)); for (int i=0; i<4; ++i) witness[i] = uses[chosen[i]];
            for (int i=0; i<6; ++i)
            {
                var (u,v) = Edges[i];
                int x = Symbol(chosen[u], Positions[u,v]);
                int y = Symbol(chosen[v], Positions[v,u]);
                witness[i+4] = modes[x][y];
            }
            foreach (int[] p in perms)
            {
                for (int i=0; i<4; ++i) permuted[i] = witness[p[i]];
                for (int i=0; i<6; ++i)
                {
                    var (u,v) = Edges[i];
                    permuted[4+i] = witness[4+EdgeIndex[p[u],p[v]]];
                }
                frontier.RemoveCube(permuted);
            }
            if (++steps % 1000 == 0)
            {
                frontier.Compact();
                Console.WriteLine($"witnesses={steps} remaining={frontier.Count} stored={frontier.Stored} seconds={watch.Elapsed.TotalSeconds:F1}");
            }
        }
        File.WriteAllLines(Path.Combine(folder,"k4-cactus-witnesses.txt"),certificate); Console.WriteLine($"all decorated K4 cases complete, witnesses={steps} seconds={watch.Elapsed.TotalSeconds:F1}");
    }
}
