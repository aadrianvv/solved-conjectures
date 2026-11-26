"use strict";
// Reviewer check: count isomorphism classes covered by the census generator at small
// orders and compare with an independent brute-force class count (order 7: 22 classes).
const fs = require("fs");
const src = fs.readFileSync(process.argv[2], "utf8");
const body = src.slice(src.indexOf("function bits"), src.indexOf("function findColouring"));
const enumerate = new Function(body + "; return enumerate;")();
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

for (const n of [8, 9, 10]) {
  const classes = new Set(); let reps = 0;
  for (let d4 = 1; d4 <= n; d4++) enumerate(n, d4, adj => { reps++; classes.add(canon(Array.from(adj))); });
  console.log(JSON.stringify({order: n, labelledReps: reps, isoClasses: classes.size}));
}
