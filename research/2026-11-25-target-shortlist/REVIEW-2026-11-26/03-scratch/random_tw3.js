"use strict";
// Reviewer corroboration (sampling only, not a proof): random maximal subquartic
// K4-free subgraphs of random 3-trees, PCF 5-coloured by an independent backtracking solver.
let seed = Number(process.argv[2] || 1); const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
const COUNT = Number(process.argv[3] || 3000);
function pcf(nb, k) { const n = nb.length, col = new Array(n).fill(-1);
  // BFS order
  const order = [], seen = new Array(n).fill(false);
  for (let s = 0; s < n; s++) if (!seen[s]) { seen[s] = true; const q = [s]; while (q.length) { const v = q.shift(); order.push(v); for (const u of nb[v]) if (!seen[u]) { seen[u] = true; q.push(u); } } }
  const pos = new Array(n); order.forEach((v, i) => pos[v] = i);
  const lastOf = nb.map(l => l.length ? Math.max(...l.map(u => pos[u])) : -1);
  const checksAt = Array.from({length: n}, () => []); nb.forEach((l, v) => { if (l.length) checksAt[lastOf[v]].push(v); });
  let nodes = 0;
  function go(i) { if (i === n) return true; if (++nodes > 5e6) throw Error("budget");
    const v = order[i];
    for (let c = 0; c < k; c++) { if (nb[v].some(u => col[u] === c)) continue; col[v] = c; let ok = true;
      for (const w of checksAt[i]) { const cnt = new Array(k).fill(0); for (const u of nb[w]) cnt[col[u]]++; if (!cnt.includes(1)) { ok = false; break; } }
      if (ok && go(i + 1)) return true; }
    col[v] = -1; return false; }
  const ok = go(0);
  if (ok) for (let v = 0; v < n; v++) { if (nb[v].some(u => col[u] === col[v])) throw Error("improper"); if (nb[v].length) { const cnt = new Array(k).fill(0); for (const u of nb[v]) cnt[col[u]]++; if (!cnt.includes(1)) throw Error("not pcf"); } }
  return ok; }
let tested = 0, fails = 0, quartic = 0, mindeg3 = 0;
for (let t = 0; t < COUNT; t++) {
  const n = 8 + Math.floor(rnd() * 33);
  const edges = [[0,1],[0,2],[1,2]], tris = [[0,1,2]];
  for (let v = 3; v < n; v++) { const T = tris[Math.floor(rnd() * tris.length)]; for (const u of T) edges.push([u, v]);
    tris.push([T[0], T[1], v], [T[0], T[2], v], [T[1], T[2], v]); }
  for (let i = edges.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [edges[i], edges[j]] = [edges[j], edges[i]]; }
  const nb = Array.from({length: n}, () => new Set());
  for (const [a, b] of edges) { if (nb[a].size >= 4 || nb[b].size >= 4) continue;
    const common = [...nb[a]].filter(x => nb[b].has(x)); let k4 = false;
    for (const x of common) for (const y of common) if (x < y && nb[x].has(y)) k4 = true;
    if (k4 && rnd() < 0.9) continue; // mostly K4-free, occasionally allow K4
    nb[a].add(b); nb[b].add(a); }
  const L = nb.map(s => [...s]);
  if (L.every(l => l.length === 4)) quartic++; if (L.every(l => l.length >= 3)) mindeg3++;
  tested++; if (!pcf(L, 5)) { fails++; console.log("FAIL", JSON.stringify(L)); }
}
console.log(JSON.stringify({tested, fails, allDegree4: quartic, minDegree3: mindeg3}));
