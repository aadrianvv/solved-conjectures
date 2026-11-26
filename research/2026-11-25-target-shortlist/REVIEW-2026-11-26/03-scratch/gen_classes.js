"use strict";
// Reviewer check: count isomorphism classes covered by the census generator at small
// orders and compare with an independent brute-force class count (order 7: 22 classes).
const fs = require("fs");
const src = fs.readFileSync(process.argv[2], "utf8");
const body = src.slice(src.indexOf("function bits"), src.indexOf("function findColouring"));
const enumerate = new Function(body + "; return enumerate;")();
for (const n of [6, 7, 8]) {
  const perms = [];
  (function rec(p, used) { if (p.length === n) { perms.push(p.slice()); return; }
    for (let v = 0; v < n; v++) if (!(used >> v & 1)) { p.push(v); rec(p, used | 1 << v); p.pop(); } })([], 0);
  const canon = adj => { let best = null; for (const p of perms) { const m = new Array(n);
      for (let i = 0; i < n; i++) { let r = 0; for (let j = 0; j < n; j++) if (adj[i] >> j & 1) r |= 1 << p[j]; m[p[i]] = r; }
      const k = m.join(","); if (best === null || k < best) best = k; } return best; };
  const classes = new Set(); let reps = 0;
  for (let d4 = 1; d4 <= n; d4++) enumerate(n, d4, adj => { reps++; classes.add(canon(Array.from(adj))); });
  console.log(JSON.stringify({order: n, labelledReps: reps, isoClasses: classes.size}));
}
