
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;

public static partial class IrregularSearch {
    private const int Width = 16;
    private const ulong DegreeMask = (1UL << Width) - 1;
    private sealed class Graph {
        public int[][] Neighbors;
        public int[][] Reverse;
        public Graph(uint[] adj) {
            int n = adj.Length;
            Neighbors = new int[n][];
            Reverse = new int[n][];
            for (int v = 0; v < n; ++v) {
                var ns = new List<int>();
                for (int u = 0; u < n; ++u)
                    if ((adj[v] & (1U << u)) != 0) ns.Add(u);
                Neighbors[v] = ns.ToArray();
            }
            for (int v = 0; v < n; ++v) {
                Reverse[v] = new int[Neighbors[v].Length];
                for (int i = 0; i < Reverse[v].Length; ++i)
                    Reverse[v][i] = Array.IndexOf(Neighbors[Neighbors[v][i]], v);
            }
        }
    }
    private sealed class States {
        public byte[][] Symbols;
        public byte[] StubCounts;
        public byte[] SecondCounts;
        public byte[][] DegreeByColor;
        public int[] IDs;
        public States(int degree, int stubColor, int palette, int secondColor, int[] extras = null) {
            int size = 1;
            for (int p = 0; p < degree; ++p) size *= palette;
            Symbols = new byte[degree][];
            for (int p = 0; p < degree; ++p) Symbols[p] = new byte[size];
            StubCounts = new byte[size];
            SecondCounts = new byte[size];
            DegreeByColor = Enumerable.Range(0,palette).Select(_=>new byte[size]).ToArray();
            IDs = new int[size];
            var counts = new int[palette];
            var colors = new int[degree];
            for (int s = 0; s < size; ++s) {
                IDs[s] = s;
                Array.Clear(counts, 0, palette);
                if (stubColor >= 0) ++counts[stubColor];
                if (secondColor >= 0) ++counts[secondColor];
                if(extras != null) Array.Copy(extras,counts,palette);
                int tmp = s;
                for (int p = 0; p < degree; ++p) {
                    int c = tmp % palette;
                    tmp /= palette;
                    colors[p] = c;
                    ++counts[c];
                }
                StubCounts[s] = (byte)counts[Math.Max(0, stubColor)];
                for(int c=0;c<palette;++c)DegreeByColor[c][s]=(byte)counts[c];
                SecondCounts[s] = (byte)counts[Math.Max(0, secondColor)];
                for (int p = 0; p < degree; ++p) {
                    int c = colors[p];
                    Symbols[p][s] = (byte)(Width * c + counts[c] - 1);
                }
            }
        }
    }

    private static readonly Dictionary<int, States> Tables = new Dictionary<int, States>();

    private static States GetStates(int degree, int stubColor, int palette, int secondColor = -1) {
        int key = degree + 1024 * palette + 16 * (stubColor + 1) + 128 * (secondColor + 1);
        if (!Tables.TryGetValue(key, out var states)) {
            states = new States(degree, stubColor, palette, secondColor);
            Tables.Add(key, states);
        }
        return states;
    }

    private sealed class Problem {
        public readonly Graph Graph;
        public readonly States[] States;
        public readonly int[][] Initial;
        public readonly int Root;
        public readonly int Other;
        public Problem(Graph graph, int root, int palette) : this(graph, root, -1, -1, palette) {}
        public Problem(Graph graph, int root, int other, int otherColor, int palette) {
            Other = other;
            Graph = graph;
            Root = root;
            int n = graph.Neighbors.Length;
            States = new States[n];
            Initial = new int[n][];
            for (int v = 0; v < n; ++v) {
                States[v] = GetStates(graph.Neighbors[v].Length, v == root ? 0 : v == other ? otherColor : -1, palette, v == root && v == other ? otherColor : -1);
                Initial[v] = States[v].IDs;
            }
            if (root < 0 && n != 0 && graph.Neighbors[0].Length > 0)
                Initial[0] = Initial[0].Where(s => States[0].Symbols[0][s] < Width).ToArray();
        }

        public Problem(Graph graph,int extraRoot,States rootStates) {
            Graph=graph;
            Root=-1;
            Other=-1;
            int n=graph.Neighbors.Length;
            States=new States[n];
            Initial=new int[n][];
            for(int v=0;v<n;++v) {
                States[v]=v==extraRoot?rootStates:GetStates(graph.Neighbors[v].Length,-1,3);
                Initial[v]=States[v].IDs;
            }
        }

        public Problem(Graph graph,States[] options) {
            Graph=graph;
            Root=-1;
            Other=-1;
            States=options;
            Initial=options.Select(o=>o.IDs).ToArray();
        }

        public int[] Solve(int allowed) => SolvePair(allowed, -1);

        public int[] SolvePair(int allowed, int otherAllowed) {
            int[][] domains = (int[][])Initial.Clone();
            if (Root >= 0)
                domains[Root] = domains[Root].Where(s =>
                    (allowed & (1 << States[Root].StubCounts[s])) != 0).ToArray();
            if (Other >= 0)
                domains[Other] = domains[Other].Where(s =>
                    (otherAllowed & (1 << (Other == Root ? States[Other].SecondCounts[s] : States[Other].StubCounts[s]))) != 0).ToArray();
            if ((Root >= 0 && domains[Root].Length == 0) ||
                (Other >= 0 && domains[Other].Length == 0))
                return null;
            return Search(domains, (1U << domains.Length) - 1);
        }

        private int[] Search(int[][] domains, uint work) {
            while (work != 0) {
                int v = BitOperations.TrailingZeroCount(work);
                work ^= 1U << v;
                for (int p = 0; p < Graph.Neighbors[v].Length; ++p) {
                    int u = Graph.Neighbors[v][p];
                    int q = Graph.Reverse[v][p];
                    ulong available = 0;
                    byte[] vSymbols = States[v].Symbols[p];
                    foreach (int s in domains[v]) available |= 1UL << vSymbols[s];
                    ulong supports = 0;
                    for (int c = 0; c < 4; ++c) {
                        ulong block = DegreeMask << (Width * c);
                        ulong present = available & block;
                        if (present != 0)
                            supports |= (present & (present - 1)) != 0 ? block : block ^ present;
                    }
                    byte[] uSymbols = States[u].Symbols[q];
                    int[] us = domains[u];
                    int valid = 0;
                    foreach (int s in us)
                        if ((supports & (1UL << uSymbols[s])) != 0) ++valid;
                    if (valid == 0) return null;
                    if (valid == us.Length) continue;
                    var filtered = new int[valid];
                    int i = 0;
                    foreach (int s in us)
                        if ((supports & (1UL << uSymbols[s])) != 0) filtered[i++] = s;
                    domains[u] = filtered;
                    work |= 1U << u;
                }
            }
            int chosen = -1;
            int count = int.MaxValue;
            for (int v = 0; v < domains.Length; ++v) {
                int size = domains[v].Length;
                if (size > 1 && size < count) {
                    count = size;
                    chosen = v;
                }
            }
            if (chosen < 0) return domains.Select(d => d[0]).ToArray();
            foreach (int s in domains[chosen]) {
                var branch = (int[][])domains.Clone();
                branch[chosen] = new[] { s };
                var result = Search(branch, 1U << chosen);
                if (result != null) return result;
            }
            return null;
        }
    }

    private static int Bit(int u, int v) {
        if (u > v) { int tmp = u; u = v; v = tmp; }
        return v * (v - 1) / 2 + u;
    }

    private static uint[] Adj(ulong mask, int n) {
        var adj = new uint[n];
        for (int v = 1; v < n; ++v)
            for (int u = 0; u < v; ++u)
                if ((mask & (1UL << Bit(u, v))) != 0) {
                    adj[u] |= 1U << v;
                    adj[v] |= 1U << u;
                }
        return adj;
    }

    private static bool TwoAlternatePaths(uint[] adj, int from, int to, uint seen, ref int count) {
        if (from == to) return ++count == 2;
        uint choices = adj[from] & ~seen;
        while (choices != 0) {
            int step = BitOperations.TrailingZeroCount(choices);
            choices ^= 1U << step;
            if (TwoAlternatePaths(adj, step, to, seen | (1U << step), ref count)) return true;
        }
        return false;
    }

    private static bool IsCactus(uint[] adj) {
        for (int v = 1; v < adj.Length; ++v)
            for (int u = 0; u < v; ++u) {
                if ((adj[v] & (1U << u)) == 0) continue;
                adj[v] ^= 1U << u;
                adj[u] ^= 1U << v;
                int count = 0;
                bool two = TwoAlternatePaths(adj, u, v, 1U << u, ref count);
                adj[v] ^= 1U << u;
                adj[u] ^= 1U << v;
                if (two) return false;
            }
        return true;
    }

    private static List<uint> Refine(uint[] adj) {
        var cells = new List<uint> { (1U << adj.Length) - 1 };
        while (true) {
            var refined = new List<uint>();
            foreach (uint cell in cells) {
                var sub = new SortedDictionary<ulong, uint>();
                uint todo = cell;
                while (todo != 0) {
                    int v = BitOperations.TrailingZeroCount(todo);
                    todo ^= 1U << v;
                    ulong code = 0;
                    foreach (uint other in cells)
                        code = (code << 4) | (uint)BitOperations.PopCount(adj[v] & other);
                    sub.TryGetValue(code, out uint old);
                    sub[code] = old | (1U << v);
                }
                foreach (var pair in sub) refined.Add(pair.Value);
            }
            if (cells.Count == refined.Count) return refined;
            cells = refined;
        }
    }

    private static void CanonicalSearch(uint[] adj, List<uint> cells, int cell, uint candidates,
                                        int[] order, int pos, ulong partial, ref ulong best) {
        if (partial >= best) return;
        if (pos == order.Length) {
            best = partial;
            return;
        }
        uint tried = 0;
        while (candidates != 0) {
            int v = BitOperations.TrailingZeroCount(candidates);
            candidates ^= 1U << v;
            bool duplicate = false;
            uint old = tried;
            while (old != 0) {
                int u = BitOperations.TrailingZeroCount(old);
                old ^= 1U << u;
                if (((adj[u] ^ adj[v]) & ~((1U << u) | (1U << v))) == 0) {
                    duplicate = true;
                    break;
                }
            }
            tried |= 1U << v;
            if (duplicate) continue;
            ulong next = partial;
            for (int j = 0; j < pos; ++j)
                if ((adj[v] & (1U << order[j])) != 0) next |= 1UL << Bit(j, pos);
            order[pos] = v;
            uint left = candidates | (tried ^ (1U << v));
            if (left != 0)
                CanonicalSearch(adj, cells, cell, left, order, pos + 1, next, ref best);
            else
                CanonicalSearch(adj, cells, cell + 1,
                                cell + 1 < cells.Count ? cells[cell + 1] : 0,
                                order, pos + 1, next, ref best);
        }
    }

    private static ulong Canonical(uint[] adj) {
        var cells = Refine(adj);
        ulong best = ulong.MaxValue;
        CanonicalSearch(adj, cells, 0, cells[0], new int[adj.Length], 0, 0, ref best);
        return best;
    }

    private static string Format(uint[] adj) {
        var items = new List<string>();
        for (int v = 1; v < adj.Length; ++v)
            for (int u = 0; u < v; ++u)
                if ((adj[v] & (1U << u)) != 0) items.Add(u + "-" + v);
        return string.Join(",", items);
    }

    private static string FormatColored(Problem p, int[] state) {
        var items = new List<string>();
        for (int v = 0; v < state.Length; ++v)
            for (int port = 0; port < p.Graph.Neighbors[v].Length; ++port) {
                int u = p.Graph.Neighbors[v][port];
                if (v < u) items.Add(v + "-" + u + ":" + p.States[v].Symbols[port][state[v]] / Width);
            }
        return string.Join(",", items);
    }

    private static bool Check(uint[] adj, bool checkFull, ref long rooted, ref long noncacti) {
        if (IsCactus(adj)) return false;
        ++noncacti;
        var g = new Graph(adj);
        if (checkFull) {
            var problem = new Problem(g, -1, 3);
            if (problem.Solve(0) == null) {
                Console.WriteLine("GRAPH no 3-coloring: " + Format(adj));
                var four = new Problem(g, -1, 4);
                var witness = four.Solve(0);
                Console.WriteLine(witness == null ? "No 4-coloring" : FormatColored(four, witness));
                return true;
            }
        }
        for (int root = 0; root < adj.Length; ++root) {
            ++rooted;
            var problem = new Problem(g, root, 3);
            int[] state = problem.Solve(-1);
            if (state == null) {
                Console.WriteLine("CAP rejected for every degree: r=" + root + " " + Format(adj));
                return true;
            }
            int d = problem.States[root].StubCounts[state[root]];

            if (problem.Solve(~(1 << d)) == null) {
                Console.WriteLine("CAP signature {" + d + "}: r=" + root + " " + Format(adj));
                return true;
            }
        }
        return false;
    }

    public static void Exhaust(int maxOrder, int maxDegree, int maxEdges, string folder) {
        var prev = new HashSet<ulong> { 0 };
        long rooted = 0;
        long noncacti = 0;
        for (int n = 2; n <= maxOrder; ++n) {
            string cache = Path.Combine(folder, "connected-" + n + "-max-" + maxDegree + "-" + maxEdges + ".txt");
            var next = new HashSet<ulong>();
            if (File.Exists(cache)) {
                foreach (string line in File.ReadLines(cache)) next.Add(Convert.ToUInt64(line, 16));
            } else {
                foreach (ulong graph in prev) {
                    int edges = BitOperations.PopCount(graph);
                    uint[] adj = Adj(graph, n);
                    uint allowed = 0;
                    for (int v = 0; v < n - 1; ++v)
                        if (BitOperations.PopCount(adj[v]) < maxDegree) allowed |= 1U << v;
                    for (uint neighbors = allowed; neighbors != 0; neighbors = (neighbors - 1) & allowed) {
                        int degree = BitOperations.PopCount(neighbors);
                        if (degree > maxDegree || edges + degree > maxEdges) continue;
                        var extended = (uint[])adj.Clone();
                        extended[n - 1] = neighbors;
                        for (int v = 0; v < n - 1; ++v)
                            if ((neighbors & (1U << v)) != 0) extended[v] |= 1U << (n - 1);
                        next.Add(Canonical(extended));
                    }
                }
                File.WriteAllLines(cache, next.Select(graph => graph.ToString("X")));
            }
            Console.WriteLine($"connected n={n}, count={next.Count}");
            if (n >= 4) {
                foreach (ulong graph in next)
                    if (Check(Adj(graph, n), true, ref rooted, ref noncacti)) return;
            }
            Console.WriteLine($"cumulative tested noncacti={noncacti}, rooted={rooted}");
            prev = next;
        }
    }

    private static uint[] Make(int n, params int[] all) {
        var adj = new uint[n];
        for (int pos = 0; pos < all.Length; pos += 2) {
            int u = all[pos];
            int v = all[pos + 1];
            adj[u] |= 1U << v;
            adj[v] |= 1U << u;
        }
        return adj;
    }

    public static void Control() {
        var cap = Make(5, 0,1, 0,2, 1,2, 0,3, 0,4, 3,4);
        var graph = new Graph(cap);
        for (int root = 0; root < 2; ++root) {
            var problem = new Problem(graph, root, 3);
            var ds = Enumerable.Range(1, graph.Neighbors[root].Length + 1)
                .Where(d => problem.Solve(1 << d) != null);
            Console.WriteLine("control cap root=" + root + " signature: " + string.Join(",", ds));
        }
        var bow = new Graph(Make(10, 0,1, 0,2, 0,3, 2,3, 0,4, 0,5, 4,5,
                                1,6, 1,7, 6,7, 1,8, 1,9, 8,9));
        var three = new Problem(bow, -1, 3);
        var four = new Problem(bow, -1, 4);
        var solution = four.Solve(0);
        Console.WriteLine("control bow tie, 3-coloring=" + (three.Solve(0) != null));
        Console.WriteLine("control bow tie, 4-coloring=" + FormatColored(four, solution));
    }
}






