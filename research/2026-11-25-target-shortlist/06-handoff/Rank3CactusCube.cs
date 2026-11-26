using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static class Rank3CactusCube
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
        private readonly UInt128[] patterns;
        private readonly bool[] fullSuffix;
        public int Root;

        private readonly bool[] paired;

        public Frontier(int[] capWidths, (int,int)[] edges)
        {
            widths = capWidths.Concat(edges.Select(_ => 8)).ToArray();
            paired = new bool[widths.Length];
            for (int i=1; i<edges.Length; ++i)
                paired[capWidths.Length + i - 1] = edges[i] == edges[i-1];
            branches = widths.Select(n => new List<Branch> { new Branch(new int[n], 0) }).ToArray();
            seen = widths.Select(n => new Dictionary<int[], int>(new ArrayComparer())).ToArray();
            patterns = new UInt128[widths.Length];
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
                options[i] = Seed(depth + 1, paired[depth] ? Math.Max(1,i) : 0);
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
            UInt128 included = patterns[depth];
            while (included != 0)
            {
                int i = (int)UInt128.TrailingZeroCount(included);
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

        public void RemoveCube(UInt128[] cube)
        {
            for (int i = widths.Length - 1; i >= 0; --i)
            {
                patterns[i] = cube[i];
                fullSuffix[i] = fullSuffix[i+1] && cube[i] == ((UInt128)1 << widths[i]) - 1;
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


    private sealed class Engine
    {
        private readonly (int,int)[] edges;
        private readonly byte[][] modes;
        private readonly int[][][] capDomains;
        private readonly Dictionary<int,UInt128>[] capMembership;
        private readonly int[] arity;
        private readonly int[,] positions;
        private readonly int[][] incoming;
        private readonly int order;
        private readonly int[] word;
        private readonly int[] chosen;

        public Engine((int,int)[] connectors, int[][] cap3, int[][] cap4, byte[][] modes)
        {
            this.edges = connectors;
            this.modes = modes;
            order = edges.Max(e => e.Item2) + 1;
            arity = new int[order];
            positions = new int[order, edges.Length];
            incoming = Enumerable.Range(0,order)
                .Select(v => Enumerable.Range(0,edges.Length)
                    .Where(i => edges[i].Item2 == v).ToArray()).ToArray();
            for (int i=0; i<edges.Length; ++i)
            {
                var (u,v) = edges[i];
                positions[u,i] = arity[u]++;
                positions[v,i] = arity[v]++;
            }
            capDomains = arity.Select(d => (d == 3 ? cap3 : cap4).ToArray()).ToArray();
            capMembership = arity.Select(_ => new Dictionary<int,UInt128>()).ToArray();
            for (int v=0; v<order; ++v)
            {
                int[][] domains = capDomains[v];
                var memberships = capMembership[v];
                for (int i=0; i<domains.Length; ++i)
                    foreach (int state in domains[i])
                        memberships[state] = memberships.GetValueOrDefault(state) | ((UInt128)1 << i);
                for (int i=0; i<domains.Length; ++i)
                    domains[i] = domains[i].OrderByDescending(s => UInt128.PopCount(memberships[s])).ToArray();
            }
            word = new int[order+edges.Length];
            chosen = new int[order];
        }

        private static int Symbol(int state, int position) => state >> (position * 6) & 63;

        private static bool Canonical(int state, int degree)
        {
            int next = 0;
            for (int i=0; i<degree; ++i)
            {
                int color = Symbol(state,i)/20;
                if (color > next) return false;
                if (color == next) ++next;
            }
            return true;
        }

        private bool Find(int v)
        {
            if (v == order) return true;
            foreach (int state in capDomains[v][word[v]])
            {
                if (v == 0 && !Canonical(state, arity[v])) continue;
                bool valid = true;
                foreach (int i in incoming[v])
                {
                    int u = edges[i].Item1;
                    int x = Symbol(chosen[u], positions[u,i]);
                    int y = Symbol(state, positions[v,i]);
                    if ((modes[x][y] & (1 << word[order + i])) == 0)
                    {
                        valid = false;
                        break;
                    }
                }
                if (!valid) continue;
                chosen[v] = state;
                if (Find(v+1)) return true;
            }
            return false;
        }

        private (int[],int[])[] Automorphisms()
        {
            var assignments = new List<(int[],int[])>();
            var p = new int[order];
            var q = new int[edges.Length];
            void Links(int pos, int used)
            {
                if (pos == edges.Length)
                {
                    assignments.Add(((int[])p.Clone(),(int[])q.Clone()));
                    return;
                }
                var (a,b) = edges[pos];
                var image = (Math.Min(p[a],p[b]), Math.Max(p[a],p[b]));
                for (int i=0; i<edges.Length; ++i)
                {
                    if ((used & (1<<i)) != 0 || edges[i] != image) continue;
                    q[pos] = i;
                    Links(pos+1, used | (1<<i));
                }
            }
            void Vertices(int pos, int used)
            {
                if (pos == order)
                {
                    Links(0, 0);
                    return;
                }
                for (int i=0; i<order; ++i)
                {
                    if ((used & (1<<i)) != 0 || arity[i] != arity[pos]) continue;
                    p[pos] = i;
                    Vertices(pos+1, used | (1<<i));
                }
            }
            Vertices(0,0);
            return assignments.ToArray();
        }

        public void Check(string folder, string name)
        {
            var frontier = new Frontier(capDomains.Select(x=>x.Length).ToArray(),edges);
            long total = frontier.Count;
            var perms = Automorphisms();
            Console.WriteLine($"initial case {name}: {total}; permutations={perms.Length}");
            var watch = System.Diagnostics.Stopwatch.StartNew();
            var witness = new UInt128[word.Length];
            var permuted = new UInt128[word.Length];
            var certificate = new List<string>();
            int steps = 0;
            while (frontier.Count != 0)
            {
                frontier.First(word);
                if (!Find(0))
                {
                    Console.WriteLine($"INCOMPATIBLE {name}: " + string.Join(",", word));
                    return;
                }
                certificate.Add(string.Join(",",chosen));
                for (int i=0; i<order; ++i) witness[i] = capMembership[i][chosen[i]];
                for (int i=0; i<edges.Length; ++i)
                {
                    var (u,v) = edges[i];
                    int x = Symbol(chosen[u], positions[u,i]);
                    int y = Symbol(chosen[v], positions[v,i]);
                    witness[i+order] = modes[x][y];
                }
                foreach (var (p,q) in perms)
                {
                    for (int i=0; i<order; ++i) permuted[i] = witness[p[i]];
                    for (int i=0; i<edges.Length; ++i) permuted[order+i] = witness[order+q[i]];
                    frontier.RemoveCube(permuted);
                }
                if (++steps % 1000 == 0)
                {
                    frontier.Compact();
                    Console.WriteLine($"witnesses={steps} remaining={frontier.Count} stored={frontier.Stored} seconds={watch.Elapsed.TotalSeconds:F1}");
                }
            }
            File.WriteAllLines(Path.Combine(folder,name+"-witnesses.txt"), certificate);
            Console.WriteLine($"all {name} cases complete: total={total} witnesses={steps} seconds={watch.Elapsed.TotalSeconds:F1}");
        }
    }

    private static int[][] ReadDomains(string path) =>
        File.ReadLines(path).Select(line => line.Split(',').Select(int.Parse).ToArray()).ToArray();

    public static void Check(string folder)
    {
        int[][] cap3 = ReadDomains(Path.Combine(folder,"k4-cactus-domains.txt"));
        int[][] cap4 = ReadDomains(Path.Combine(folder,"rank3-arity4-cactus-domains.txt"));
        byte[][] modes = File.ReadLines(Path.Combine(folder,"k4-cactus-edge-table.txt"))
            .Select(line => line.Split(',').Select(byte.Parse).ToArray()).ToArray();
        for (int x=0; x<modes.Length; ++x)
            for (int y=0; y<modes.Length; ++y)
                if (modes[x][y] != modes[y][x]) throw new InvalidOperationException("Nonsymmetric modes");

        new Engine(new[] {(0,1),(0,1),(0,2),(0,2),(1,2)},cap3,cap4,modes).Check(folder,"rank3-triangle");
        new Engine(new[] {(0,1),(0,1),(0,2),(1,3),(2,3),(2,3)},cap3,cap4,modes).Check(folder,"rank3-double-square");
    }
}
