
using System;
using System.Collections.Generic;
using System.Linq;

public static partial class IrregularSearch {
    public static void BowTransfers(string folder) {
        var start = Bow();
        var catalog = new Dictionary<string, Transfer>();
        long checkedPairs = 0;
        foreach (var edge in Edges(start)) {
            if (edge.u == 0 && edge.v == 1) continue;
            var adj = Unlink(start, edge.u, edge.v);
            var graph = new Graph(adj);
            string shape = "c";
            int paths = 0;
            shape += TwoAlternatePaths(adj, edge.u, edge.v, 1U << edge.u, ref paths) ? "m" : "s";
            ulong equal = TransferMode(graph, edge.u, edge.v, 0);
            ulong different = TransferMode(graph, edge.u, edge.v, 1);
            Console.WriteLine($"bow minus {edge.u}-{edge.v}:  equal={EqualPairs(equal)} different={EqualPairs(different)}");
            var here = new Transfer {
                Adj = adj, Left = edge.u, Right = edge.v, Equal = equal, Different = different,
                Key = shape + ":" + equal.ToString("X") + ":" + different.ToString("X")
            };
            if (TryTransfer(here, catalog, ref checkedPairs)) return;
            var reversed = new Transfer {
                Adj = adj, Left = edge.v, Right = edge.u,
                Equal = Transpose(equal), Different = Transpose(different),
                Key = shape + ":" + Transpose(equal).ToString("X") + ":" + Transpose(different).ToString("X")
            };
            if (TryTransfer(reversed, catalog, ref checkedPairs)) return;
        }
        var original = catalog.Values.ToArray();
        foreach (var one in original)
            foreach (var e in Edges(one.Adj)) {
                if (e.u == 0 && e.v == 1) continue;
                var subdivided = one.Adj;
                for (int l = 1; l <= 3; ++l) {
                    subdivided = LinkPath(Unlink(one.Adj, e.u, e.v), e.u, e.v, l);
                    var reversed = new Graph(subdivided);
                    ulong equal = TransferMode(reversed, one.Left, one.Right, 0);
                    ulong different = TransferMode(reversed, one.Left, one.Right, 1);
                    var next = new Transfer {
                        Adj = subdivided, Left = one.Left, Right = one.Right,
                        Equal = equal, Different = different,
                        Key = "cs:" + equal.ToString("X") + ":" + different.ToString("X")
                    };
                    if (TryTransfer(next, catalog, ref checkedPairs)) return;
                }
            }
        Console.WriteLine($"closed bow transfer variants: {catalog.Count} distinct profiles {checkedPairs} comparisons");
    }

    private static string EqualPairs(ulong possible) {
        var shapes = new List<string>();
        for (int row = 0; row < 8; ++row)
            for (int col = 0; col < 8; ++col)
                if ((possible & (1UL << (8 * row + col))) != 0)
                    shapes.Add($"({row + 1},{col + 1})");
        return string.Join(",", shapes);
    }
}

