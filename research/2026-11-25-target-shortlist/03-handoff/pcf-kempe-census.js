
"use strict";
const fs = require("node:fs");
const vm = require("node:vm");
const [reference, first = "6", last = "9"] = process.argv.slice(2);
let source = fs.readFileSync(reference, "utf8");
source = source.slice(0, source.indexOf("\ncheckExamples();"));
const {enumerate, bits, findColouring, verifyColouring} = vm.runInNewContext(
    source + "\n({enumerate, bits, findColouring, verifyColouring});", {process: {argv: []}}
);

const palette = [0, 1, 2, 3, 4];
function enumerateLowDefect(neighbours) {
    const order = neighbours.length;
    const lastAt = Array.from({length: order}, () => []);
    const previous = neighbours.map((row, vertex) => row.filter(other => other < vertex));
    for (const [center, row] of neighbours.entries()) lastAt[Math.max(...row)].push(center);
    const colours = new Array(order).fill(-1);
    const states = new Map();
    function color(vertex, used, defects, code) {
        if (vertex === order) {
            states.set(code, {colours: colours.slice(), defects});
            return;
        }
        const excluded = previous[vertex].reduce((mask, other) => mask | (1 << colours[other]), 0);
        for (let colour = 0; colour <= Math.min(used, 4); colour++) {
            if (excluded & (1 << colour)) continue;
            colours[vertex] = colour;
            let count = defects;
            for (const center of lastAt[vertex]) {
                const parity = neighbours[center].reduce((mask, n) => mask ^ (1 << colours[n]), 0);
                if (!parity) count++;
            }
            if (count <= 2) color(vertex + 1, Math.max(used, colour + 1), count, 5 * code + colour);
        }
    }
    color(0, 0, 0, 0);
    return states;
}

function normalize(colours) {
    const renamed = [-1, -1, -1, -1, -1];
    let used = 0;
    let code = 0;
    for (const colour of colours) {
        if (renamed[colour] < 0) renamed[colour] = used++;
        code = 5 * code + renamed[colour];
    }
    return code;
}

function visitKempe(neighbours, colours, visit) {
    const order = colours.length;
    for (const a of palette) for (const b of palette) {
        if (a >= b) continue;
        const components = [];
        const seen = new Uint8Array(order);
        for (let vertex = 0; vertex < order; vertex++) {
            if (seen[vertex] || (colours[vertex] !== a && colours[vertex] !== b)) continue;
            const queue = [vertex];
            seen[vertex] = 1;
            for (const v of queue) for (const other of neighbours[v]) {
                if (seen[other] || (colours[other] !== a && colours[other] !== b)) continue;
                queue.push(other);
                seen[other] = 1;
            }
            components.push(queue);
        }
        if (components.length <= 1) continue;
        for (let mask = 1; mask < 1 << (components.length - 1); mask++) {
            const next = colours.slice();
            for (const [i, component] of components.entries()) if (mask & (1 << i)) {
                for (const v of component) next[v] = a + b - next[v];
            }
            visit(normalize(next));
        }
    }
}

function closure(neighbours, states, cap) {
    const reached = new Map();
    const queue = [];
    let maxDistance = 0;
    for (const [key, state] of states) if (state.defects === 0) {
        queue.push(key);
        reached.set(key, 0);
    }
    for (const key of queue) {
        const distance = reached.get(key) + 1;
        visitKempe(neighbours, states.get(key).colours, other => {
            if (reached.has(other) || !states.has(other) || states.get(other).defects > cap) return;
            reached.set(other, distance);
            queue.push(other);
            maxDistance = Math.max(maxDistance, distance);
        });
    }
    const missed = [...states].filter(([key, state]) => state.defects <= cap && !reached.has(key));
    return {maxDistance, missed};
}

for (let order = Number(first); order <= Number(last); order++) {
    let graphs = 0;
    let oneDefectStates = 0;
    let twoDefectStates = 0;
    let maxDistanceAtOne = 0;
    let maxDistanceAtTwo = 0;
    let oneExample = null;
    let twoExample = null;
    enumerate(order, order, adjacency => {
        const neighbours = Array.from(adjacency, bits);
        const states = enumerateLowDefect(neighbours);
        for (const {defects} of states.values()) {
            if (defects === 1) oneDefectStates++;
            if (defects === 2) twoDefectStates++;
        }
        for (const cap of [1, 2]) {
            const {maxDistance, missed} = closure(neighbours, states, cap);
            if (missed.length) {
                const witness = findColouring(neighbours, 5);
                console.log(JSON.stringify({order, cap, graphs, missed: missed.length, first: missed[0], neighbours, witness}));
                if (!verifyColouring(neighbours, witness, 5)) throw Error("possible PCF obstruction");
                process.exit(2);
            }
            if (cap === 1 && maxDistance > maxDistanceAtOne) {
                maxDistanceAtOne = maxDistance;
                oneExample = neighbours;
            }
            if (cap === 2 && maxDistance > maxDistanceAtTwo) {
                maxDistanceAtTwo = maxDistance;
                twoExample = neighbours;
            }
        }
        if (++graphs % 100 === 0) console.log(JSON.stringify({order, graphs, maxDistanceAtOne, maxDistanceAtTwo}));
    });
    console.log(JSON.stringify({complete: true, order, graphs, oneDefectStates, twoDefectStates,
        maxDistanceAtOne, maxDistanceAtTwo, oneExample, twoExample}));
}

