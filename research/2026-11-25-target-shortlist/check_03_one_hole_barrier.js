"use strict";

const order = 45;
const cycleLength = 5;
const palette = [0, 1, 2, 3, 4];
const graph = Array.from({length: order}, () => []);

function addEdge(first, second) {
    graph[first].push(second);
    graph[second].push(first);
}

function layerVertex(branch, layer, index) {
    return cycleLength + 20 * branch + 5 * layer + index % cycleLength;
}

for (let i = 0; i < cycleLength; i++) {
    addEdge(i, (i + 1) % cycleLength);
    for (let branch = 0; branch < 2; branch++) {
        addEdge(i, layerVertex(branch, 0, i));
        addEdge(layerVertex(branch, 1, i), layerVertex(branch, 2, i));
        for (let shift = 0; shift < 3; shift++) {
            addEdge(layerVertex(branch, 0, i), layerVertex(branch, 1, i + shift));
            addEdge(layerVertex(branch, 2, i), layerVertex(branch, 3, i + shift));
        }
    }
    addEdge(layerVertex(0, 3, i), layerVertex(1, 3, i));
}

function isPartialPCF(colours) {
    return graph.every((neighbours, vertex) => {
        if (colours[vertex] === -1) return true;
        if (neighbours.some(other => colours[other] === colours[vertex])) return false;
        if (neighbours.some(other => colours[other] === -1)) return true;
        const counts = new Uint8Array(palette.length);
        for (const other of neighbours) counts[colours[other]]++;
        return counts.includes(1);
    });
}

function connectedAfterRemoving(first, second) {
    const start = graph.findIndex((_, vertex) => vertex !== first && vertex !== second);
    const reached = new Set([start]);
    const queue = [start];
    for (const vertex of queue) {
        for (const other of graph[vertex]) {
            if (other === first || other === second || reached.has(other)) continue;
            reached.add(other);
            queue.push(other);
        }
    }
    return reached.size === order - 2;
}

let testedVertexPairs = 0;
for (let vertex = 0; vertex < order; vertex++) {
    const neighbours = graph[vertex];
    if (new Set(neighbours).size !== 4 || neighbours.length !== 4 || neighbours.includes(vertex)
        || neighbours.some(other => graph[other].some(third => neighbours.includes(third)))) {
        throw new Error("The graph must be simple, quartic and triangle-free");
    }
    for (let other = vertex + 1; other < order; other++) {
        if (!connectedAfterRemoving(vertex, other)) throw new Error("Found a vertex cut");
        testedVertexPairs++;
    }
}

const ordinaryColouring = [
    0, 1, 0, 1, 2,
    1, 0, 1, 0, 0, 2, 2, 2, 2, 3, 0, 0, 1, 0, 0, 2, 1, 2, 2, 4,
    1, 2, 2, 0, 0, 3, 3, 3, 3, 3, 2, 1, 2, 2, 0, 1, 3, 0, 3, 3,
];
if (!isPartialPCF(ordinaryColouring)) throw new Error("The full colouring certificate failed");

const layerColours = [[0, 1, 2, 3], [0, 1, 2, 4]];
const scaffold = Array(order).fill(-1);
for (let branch = 0; branch < 2; branch++) {
    for (let layer = 0; layer < 4; layer++) {
        for (let i = 0; i < cycleLength; i++) {
            scaffold[layerVertex(branch, layer, i)] = layerColours[branch][layer];
        }
    }
}

const cycleColours = [2, 3, 4];
const family = new Set();
for (let hole = 0; hole < cycleLength; hole++) {
    for (const endpointColour of cycleColours) {
        for (const firstMiddleColour of cycleColours.filter(colour => colour !== endpointColour)) {
            const otherMiddleColour = cycleColours.find(colour => colour !== endpointColour && colour !== firstMiddleColour);
            const assignment = scaffold.slice();
            const pathColours = [endpointColour, firstMiddleColour, otherMiddleColour, endpointColour];
            for (let i = 0; i < pathColours.length; i++) {
                assignment[(hole + i + 1) % cycleLength] = pathColours[i];
            }
            if (!isPartialPCF(assignment)) throw new Error("Invalid one-hole state");
            family.add(assignment.join(","));
        }
    }
}

let transitions = 0;
for (const encoded of family) {
    const colours = encoded.split(",").map(Number);
    const hole = colours.indexOf(-1);
    for (const colour of palette) {
        const filled = colours.slice();
        filled[hole] = colour;
        if (isPartialPCF(filled)) throw new Error("A state has a direct full extension");
        for (let other = 0; other < order; other++) {
            if (other === hole) continue;
            const moved = filled.slice();
            moved[other] = -1;
            if (!isPartialPCF(moved)) continue;
            if (!family.has(moved.join(","))) throw new Error("Found an exit from the one-hole family");
            transitions++;
        }
    }
}

console.log(JSON.stringify({order, testedVertexPairs, closedStates: family.size, transitions}));
