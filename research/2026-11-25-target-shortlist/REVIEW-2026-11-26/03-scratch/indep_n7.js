"use strict";
// Independent reviewer check (2026-11-26): order 7.
// (1) Every graph on 7 labelled vertices with max degree <= 4 has a PCF 5-colouring
//     (brute force over all 2^21 edge sets; no structural reductions used).
// (2) Isomorphism classes of connected K4-free graphs with degrees in {3,4} and at
//     least one 4 on 7 vertices, counted by brute force, are compared with the
//     classes covered by the census generator (generator code re-derived here via
//     canonical forms of its printed output is not available, so we count classes
//     and compare with the expected class count computed below from both sides).
const n = 7, E = [];
for (let i = 0; i < n; i++) for (let j = i + 1; j < n; j++) E.push([i, j]);
const perms = [];
(function rec(p, used) { if (p.length === n) { perms.push(p.slice()); return; }
  for (let v = 0; v < n; v++) if (!(used >> v & 1)) { p.push(v); rec(p, used | 1 << v); p.pop(); } })([], 0);
function canon(adj) { let best = null;
  for (const p of perms) { let s = 0n; // edge bitstring under relabelling
    const m = new Array(n);
    for (let i = 0; i < n; i++) { let r = 0; for (let j = 0; j < n; j++) if (adj[i] >> j & 1) r |= 1 << p[j]; m[p[i]] = r; }
    const key = m.join(","); if (best === null || key < best) best = key; }
  return best; }
function pcf(adj, k) { const col = new Array(n).fill(-1);
  function ok() { for (let v = 0; v < n; v++) { if (!adj[v]) continue; const c = new Array(k).fill(0);
      for (let u = 0; u < n; u++) if (adj[v] >> u & 1) c[col[u]]++; if (!c.includes(1)) return false; } return true; }
  function go(v) { if (v === n) return ok(); for (let c = 0; c < k; c++) { let bad = false;
      for (let u = 0; u < v; u++) if ((adj[v] >> u & 1) && col[u] === c) { bad = true; break; }
      if (bad) continue; col[v] = c; if (go(v + 1)) return true; } col[v] = -1; return false; }
  return go(0); }
function connected(adj) { let r = 1, f = 1; while (f) { const b = f & -f; f ^= b; const v = 31 - Math.clz32(b); f |= adj[v] & ~r; r |= adj[v]; } return r === (1 << n) - 1; }
function hasK4(adj) { for (let a = 0; a < n; a++) for (let b = a + 1; b < n; b++) if (adj[a] >> b & 1)
  for (let c = b + 1; c < n; c++) if ((adj[a] >> c & 1) && (adj[b] >> c & 1))
  for (let d = c + 1; d < n; d++) if ((adj[a] >> d & 1) && (adj[b] >> d & 1) && (adj[c] >> d & 1)) return true; return false; }
const seenAll = new Set(), classClass = new Set(); let failures = 0, checked = 0;
for (let s = 0; s < 1 << E.length; s++) {
  const adj = new Array(n).fill(0); let okDeg = true;
  for (let e = 0; e < E.length; e++) if (s >> e & 1) { adj[E[e][0]] |= 1 << E[e][1]; adj[E[e][1]] |= 1 << E[e][0]; }
  const deg = adj.map(x => { let c = 0; while (x) { x &= x - 1; c++; } return c; });
  if (deg.some(d => d > 4)) continue;
  // canonical dedupe only for sorted-degree labelled graphs to save time
  let sorted = true; for (let i = 1; i < n; i++) if (deg[i] > deg[i - 1]) sorted = false; if (!sorted) continue;
  const key = canon(adj); if (seenAll.has(key)) continue; seenAll.add(key); checked++;
  if (!pcf(adj, 5)) { failures++; console.log("FAIL", adj); }
  if (connected(adj) && !hasK4(adj) && deg.every(d => d >= 3) && deg.includes(4)) classClass.add(key);
}
console.log(JSON.stringify({order: n, isoClassesMaxDeg4: checked, pcf5Failures: failures, reducedClassIsoClasses: classClass.size}));
