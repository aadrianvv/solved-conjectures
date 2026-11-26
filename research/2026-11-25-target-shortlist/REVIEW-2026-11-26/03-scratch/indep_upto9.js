"use strict";
// Independent reviewer check (2026-11-26), no structural reductions used:
// generate all isomorphism classes of graphs with max degree <= 4 on n <= MAX vertices
// by vertex augmentation, PCF 5-colour each by plain backtracking, and count the classes
// in the census class (connected, K4-free, degrees in {3,4}, some 4).
const MAX = Number(process.argv[2] || 9);
const pc = x => { let c = 0; while (x) { x &= x - 1; c++; } return c; };
function canon(adj) {
  const n = adj.length; let inv = adj.map((a, v) => pc(a));
  for (let round = 0; round < 3; round++) { // colour refinement
    const sig = adj.map((a, v) => inv[v] + ":" + [...Array(n).keys()].filter(u => a >> u & 1).map(u => inv[u]).sort().join("."));
    const keys = [...new Set(sig)].sort(); inv = sig.map(s => keys.indexOf(s)); }
  const order = [...Array(n).keys()].sort((a, b) => inv[a] - inv[b]);
  const cells = []; for (const v of order) { if (cells.length && inv[cells.at(-1)[0]] === inv[v]) cells.at(-1).push(v); else cells.push([v]); }
  let best = null; const pos = new Array(n);
  function permsOf(a) { if (a.length <= 1) return [a]; return a.flatMap((x, i) => permsOf(a.filter((_, j) => j !== i)).map(r => [x, ...r])); }
  const cellPerms = cells.map(permsOf);
  (function rec(ci, at) {
    if (ci === cells.length) { const m = new Array(n);
      for (let i = 0; i < n; i++) { let r = 0; for (let j = 0; j < n; j++) if (adj[i] >> j & 1) r |= 1 << pos[j]; m[pos[i]] = r; }
      const k = m.join(","); if (best === null || k < best) best = k; return; }
    for (const p of cellPerms[ci]) { p.forEach((v, i) => pos[v] = at + i); rec(ci + 1, at + p.length); }
  })(0, 0);
  return best;
}
function pcf(adj, k) { const n = adj.length, col = new Array(n).fill(-1), nb = adj.map(a => [...Array(n).keys()].filter(u => a >> u & 1));
  const last = nb.map(l => l.length ? Math.max(...l) : -1);
  function good(v) { const c = new Array(k).fill(0); for (const u of nb[v]) c[col[u]]++; return c.includes(1); }
  function go(v, used) { if (v === n) return true;
    for (let c = 0; c < Math.min(used + 1, k); c++) { if (nb[v].some(u => u < v && col[u] === c)) continue; col[v] = c;
      let ok = true; for (let w = 0; w < n && ok; w++) if (last[w] === v && !good(w)) ok = false;
      if (ok && go(v + 1, Math.max(used, c + 1))) return true; }
    col[v] = -1; return false; }
  return go(0, 0); }
function connected(adj) { const n = adj.length; let r = 1, f = 1; while (f) { const b = f & -f; f ^= b; const v = 31 - Math.clz32(b); f |= adj[v] & ~r; r |= adj[v]; } return r === (1 << n) - 1; }
function hasK4(adj) { const n = adj.length; for (let a = 0; a < n; a++) for (let b = a + 1; b < n; b++) if (adj[a] >> b & 1)
  for (let c = b + 1; c < n; c++) if ((adj[a] >> c & 1) && (adj[b] >> c & 1))
  for (let d = c + 1; d < n; d++) if ((adj[a] >> d & 1) && (adj[b] >> d & 1) && (adj[c] >> d & 1)) return true; return false; }
let level = new Map([["0", [0]]]);
for (let n = 2; n <= MAX; n++) {
  const next = new Map();
  for (const g of level.values()) {
    const m = g.length;
    for (let s = 0; s < 1 << m; s++) { if (pc(s) > 4) continue; let ok = true;
      for (let v = 0; v < m; v++) if ((s >> v & 1) && pc(g[v]) >= 4) { ok = false; break; } if (!ok) continue;
      const h = g.map((a, v) => (s >> v & 1) ? a | 1 << m : a); h.push(s);
      const key = canon(h); if (!next.has(key)) next.set(key, h); }
  }
  level = next; let fails = 0, red = 0;
  for (const g of level.values()) { if (!pcf(g, 5)) { fails++; console.log("FAIL", JSON.stringify(g)); }
    const d = g.map(pc); if (connected(g) && !hasK4(g) && d.every(x => x >= 3) && d.includes(4)) red++; }
  console.log(JSON.stringify({order: n, isoClassesMaxDeg4: level.size, pcf5Failures: fails, censusClassIsoClasses: red}));
}
