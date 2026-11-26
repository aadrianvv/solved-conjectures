from pathlib import Path
folder = Path(__file__).parent
code = (folder/'K4CactusCube.cs').read_text(encoding='utf-8-sig')
code = code[:code.index('    private static readonly (int,int)[] Edges')]
code = code.replace('K4CactusCube','Rank3CactusCube').replace('ulong','UInt128')
code = code.replace('1UL << widths[i]','(UInt128)1 << widths[i]')
code = code.replace('BitOperations.TrailingZeroCount(included)','(int)UInt128.TrailingZeroCount(included)')
code = code.replace('        public Frontier(int capCount)\n        {\n            widths = new[] { capCount, capCount, capCount, capCount, 8, 8, 8, 8, 8, 8 };',
'''        private readonly bool[] paired;

        public Frontier(int[] capWidths, (int,int)[] edges)
        {
            widths = capWidths.Concat(edges.Select(_ => 8)).ToArray();
            paired = new bool[widths.Length];
            for (int i=1; i<edges.Length; ++i)
                paired[capWidths.Length + i - 1] = edges[i] == edges[i-1];''')
code = code.replace('Seed(depth + 1, depth < 3 ? i : 0)','Seed(depth + 1, paired[depth] ? Math.Max(1,i) : 0)')
(folder/'Rank3CactusCube.cs').write_text(code, encoding='utf8')
