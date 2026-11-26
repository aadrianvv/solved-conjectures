"use strict";

const fs = require("node:fs");
const vm = require("node:vm");
const filepath = "C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/check_03_conflict_free_colouring.js";
const text = fs.readFileSync(filepath, "utf8");
const {enumerate, bits} = vm.runInNewContext(text.slice(0, text.indexOf("\ncheckExamples();"))
    + "\n({enumerate, bits});", {process: {argv: []}});

function polynomial(neighbours, deduplicate) {
    const factors = neighbours.flatMap((list, v) => list.filter(w => w > v).map(w => [v, w]));
    factors.push(...neighbours);
    const activeFactors = deduplicate ? [...new Map(factors.map(row => [row.join(","), row])).values()] : factors;
    let coefficients = new Set([0]);
    for (const factor of activeFactors) {
        const next = new Set();
        for (const exponent of coefficients) {
            for (const v of factor) {
                const shift = 3 * v;
                if (((exponent >> shift) & 7) >= 4) continue;
                const monomial = exponent + (1 << shift);
                if (next.has(monomial)) next.delete(monomial);
                else next.add(monomial);
            }
        }
        coefficients = next;
        if (!coefficients.size) break;
    }
    return coefficients.size;
}

const completeFive = Array.from({length: 5}, (_, i) => [0, 1, 2, 3, 4].filter(j => j !== i));
const biclique = Array.from({length: 8}, (_, i) => [0, 1, 2, 3, 4, 5, 6, 7].filter(j => (j >> 2) !== (i >> 2)));
for (const [name, adjacency] of [["K5", completeFive], ["K4,4", biclique]]) {
    console.log(JSON.stringify({name, raw: polynomial(adjacency, false), unique: polynomial(adjacency, true)}));
}

const end = Number(process.argv[2] ?? 8);
for (let order = 5; order <= end; order++) {
    let count = 0;
    let zeros = 0;
    let example;
    enumerate(order, order, adjacency => {
        const neighbours = Array.from(adjacency, bits);
        if (!polynomial(neighbours, true)) {
            zeros++;
            example ??= neighbours;
        }
        count++;
    });
    console.log(JSON.stringify({order, count, zeros, example}));
}
