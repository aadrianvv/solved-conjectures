from pathlib import Path
folder = Path(__file__).parent
code = (folder/'Rank3CactusCube.cs').read_text(encoding='utf-8-sig')
code = code.replace('Rank3CactusCube','PortCactusCube')
code = code.replace('widths = capWidths.Concat(edges.Select(_ => 8)).ToArray();',
                    'widths = capWidths.Concat(edges.Select((_,i) => i == edges.Length - 1 ? 1 : 8)).ToArray();')
code = code.replace('capDomains = arity.Select(d => (d == 3 ? cap3 : cap4).ToArray()).ToArray();',
'''var external = Enumerable.Range(0,20).Select(d => new[] { d, 20+d, 40+d }).ToArray();
            capDomains = arity.Select(d => (d == 1 ? external : d == 3 ? cap3 : cap4).ToArray()).ToArray();''')
code = code.replace('witness[i+order] = modes[x][y];', 'witness[i+order] = (UInt128)(modes[x][y] & (i == edges.Length - 1 ? 1 : 255));')
code = code[:code.index('        new Engine(new[] {(0,1)')]
code += '''        new Engine(new[] {(0,1),(0,1),(0,1),(0,2)},cap3,cap4,modes).Check(folder,"port-theta-hub");
        new Engine(new[] {(0,1),(0,1),(0,2),(1,2),(2,3)},cap3,cap4,modes).Check(folder,"port-theta-arc");
        new Engine(new[] {(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4)},cap3,cap4,modes).Check(folder,"port-k4-hub");
        new Engine(new[] {(0,1),(0,2),(0,3),(1,2),(1,4),(2,3),(3,4),(4,5)},cap3,cap4,modes).Check(folder,"port-k4-arc");
    }
}
'''
(folder/'PortCactusCube.cs').write_text(code, encoding='utf8')
