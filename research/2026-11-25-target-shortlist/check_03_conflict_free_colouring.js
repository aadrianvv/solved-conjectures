"use strict";

// Exhaustive labelled cover of the connected K4-free graphs with degrees 3 and
// 4 and at least one degree-4 vertex. Isomorphic repetitions are allowed.
const firstOrder = Number(process.argv[2] ?? 5);
const lastOrder = Number(process.argv[3] ?? 11);
const cubicMatching = process.argv[4] === "--cubic-matching";
const requestedQuarticCounts = process.argv.slice(5).map(Number);
if (!Number.isInteger(firstOrder) || !Number.isInteger(lastOrder)
    || firstOrder < 5 || lastOrder < firstOrder || lastOrder > 15
    || (process.argv[4] !== undefined && !cubicMatching)
    || requestedQuarticCounts.some(count => !Number.isInteger(count) || count < 1 || count > lastOrder)) {
    throw new Error("Usage: node check_03_conflict_free_colouring.js [first [last [--cubic-matching [quartic count ...]]]], 5 <= first <= last <= 15");
}

function bits(mask) {
    const result = [];
    while (mask) {
        const lowestBit = mask & -mask;
        result.push(31 - Math.clz32(lowestBit));
        mask ^= lowestBit;
    }
    return result;
}

function bitCount(mask) {
    let count = 0;
    while (mask) {
        mask &= mask - 1;
        count++;
    }
    return count;
}

function isConnected(adjacency) {
    let reached = 1;
    let frontier = reached;
    while (frontier) {
        const lowestBit = frontier & -frontier;
        frontier ^= lowestBit;
        const neighbours = adjacency[31 - Math.clz32(lowestBit)];
        frontier |= neighbours & ~reached;
        reached |= neighbours;
    }
    return reached === (1 << adjacency.length) - 1;
}

function hasCliqueAfterAdding(adjacency, first, second) {
    let common = adjacency[first] & adjacency[second];
    while (common) {
        const lowestBit = common & -common;
        common ^= lowestBit;
        if (adjacency[31 - Math.clz32(lowestBit)] & common) return true;
    }
    return false;
}

function enumerate(order, degreeFour, visit, requireCubicMatching = false) {
    const target = Array.from({length: order}, (_, v) => v < degreeFour ? 4 : 3);
    if ((3 * order + degreeFour) % 2) return;
    if (requireCubicMatching && order - degreeFour > 2 * degreeFour) return;
    const residual = target.slice();
    const adjacency = new Int32Array(order);
    const cubicMask = ((1 << order) - 1) ^ ((1 << degreeFour) - 1);

    function add(first, second) {
        adjacency[first] |= 1 << second;
        adjacency[second] |= 1 << first;
        residual[first]--;
        residual[second]--;
    }

    function remove(first, second) {
        adjacency[first] ^= 1 << second;
        adjacency[second] ^= 1 << first;
        residual[first]++;
        residual[second]++;
    }

    function completeFrom(vertex) {
        while (vertex < order && residual[vertex] === 0) vertex++;
        if (vertex === order) {
            if (isConnected(adjacency)) visit(adjacency);
            return;
        }
        let available = 0;
        for (let other = vertex + 1; other < order; other++) {
            if (residual[other] > 0) available |= 1 << other;
        }
        const availableCount = bitCount(available);
        if (residual[vertex] > availableCount) return;
        const groups = new Map();
        const earlier = (1 << vertex) - 1;
        for (const other of bits(available)) {
            if (residual[other] > availableCount) return;
            const key = (target[other] << order) | (adjacency[other] & earlier);
            groups.set(key, (groups.get(key) ?? 0) | (1 << other));
        }
        choose(vertex, available, availableCount, groups);
    }

    function choose(vertex, available, remaining, groups) {
        if (residual[vertex] === 0) {
            completeFrom(vertex + 1);
            return;
        }
        while (remaining >= residual[vertex]) {
            const lowestBit = available & -available;
            const other = 31 - Math.clz32(lowestBit);
            available ^= lowestBit;
            remaining--;
            const validCubicEdge = !requireCubicMatching || target[vertex] === 4 || target[other] === 4
                || !((adjacency[vertex] | adjacency[other]) & cubicMask);
            if (validCubicEdge && !hasCliqueAfterAdding(adjacency, vertex, other)) {
                add(vertex, other);
                choose(vertex, available, remaining, groups);
                remove(vertex, other);
            }
            // Skipping a vertex skips all later vertices of its degree that
            // have the same adjacency to processed vertices. Their labels
            // can be permuted without changing any earlier row.
            const key = (target[other] << order) | (adjacency[other] & ((1 << vertex) - 1));
            const equivalent = available & groups.get(key);
            available ^= equivalent;
            remaining -= bitCount(equivalent);
        }
    }

    // Label the degree-4 vertices first. For each split of vertex 0's
    // neighbours by degree, put its neighbours first within each degree group.
    for (let neighboursOfDegreeFour = 0; neighboursOfDegreeFour <= 4; neighboursOfDegreeFour++) {
        const neighboursOfDegreeThree = 4 - neighboursOfDegreeFour;
        if (neighboursOfDegreeFour >= degreeFour || neighboursOfDegreeThree > order - degreeFour) continue;
        const neighbours = [];
        for (let v = 1; v <= neighboursOfDegreeFour; v++) neighbours.push(v);
        for (let v = degreeFour; v < degreeFour + neighboursOfDegreeThree; v++) neighbours.push(v);
        for (const neighbour of neighbours) add(0, neighbour);
        completeFrom(1);
        for (const neighbour of neighbours) remove(0, neighbour);
    }
}

function findColouring(neighbours, paletteSize) {
    const order = neighbours.length;
    const colours = new Int8Array(order).fill(-1);
    const checks = Array.from({length: order}, () => []);
    for (const neighbourhood of neighbours) {
        if (neighbourhood.length) checks[neighbourhood.at(-1)].push(neighbourhood);
    }

    function visit(vertex, used) {
        if (vertex === order) return true;
        let forbidden = 0;
        for (const other of neighbours[vertex]) {
            if (other < vertex) forbidden |= 1 << colours[other];
        }
        const choices = ((1 << Math.min(used + 1, paletteSize)) - 1) & ~forbidden;
        for (let remaining = choices; remaining; remaining &= remaining - 1) {
            const colour = 31 - Math.clz32(remaining & -remaining);
            colours[vertex] = colour;
            let valid = true;
            for (const neighbourhood of checks[vertex]) {
                let present = 0;
                let repeated = 0;
                for (const other of neighbourhood) {
                    const bit = 1 << colours[other];
                    repeated |= present & bit;
                    present |= bit;
                }
                if ((present & ~repeated) === 0) {
                    valid = false;
                    break;
                }
            }
            if (valid && visit(vertex + 1, Math.max(used, colour + 1))) return true;
        }
        colours[vertex] = -1;
        return false;
    }

    return visit(0, 0) ? colours : null;
}

function verifyColouring(neighbours, colours, paletteSize) {
    if (colours === null || colours.length !== neighbours.length) return false;
    return neighbours.every((neighbourhood, vertex) => {
        const colour = colours[vertex];
        if (colour < 0 || colour >= paletteSize) return false;
        const multiplicities = new Uint8Array(paletteSize);
        for (const other of neighbourhood) {
            if (colour === colours[other]) return false;
            multiplicities[colours[other]]++;
        }
        return neighbourhood.length === 0 || multiplicities.includes(1);
    });
}

function checkExamples() {
    const cycleFive = [[1, 4], [0, 2], [1, 3], [2, 4], [0, 3]];
    const completeFive = Array.from({length: 5}, (_, i) => [0, 1, 2, 3, 4].filter(j => j !== i));
    const octahedron = Array.from({length: 6}, (_, i) => [0, 1, 2, 3, 4, 5].filter(j => (j >> 1) !== (i >> 1)));
    for (const graph of [cycleFive, completeFive, octahedron]) {
        if (findColouring(graph, 4) !== null || !verifyColouring(graph, findColouring(graph, 5), 5)) {
            throw new Error("Example check failed");
        }
    }
}

function checkGenerator() {
    // Compare the exact representative sets with independent enumeration of
    // all labelled edge subsets at orders where this is fast.
    for (const order of [5, 6]) {
        const edges = [];
        for (let first = 0; first < order; first++) {
            for (let second = first + 1; second < order; second++) edges.push([first, second]);
        }
        const bruteForce = new Set();
        const bruteCubicMatching = new Set();
        for (let subset = 0; subset < 1 << edges.length; subset++) {
            const adjacency = Array.from({length: order}, () => new Set());
            for (let edge = 0; edge < edges.length; edge++) {
                if (!(subset & (1 << edge))) continue;
                const [first, second] = edges[edge];
                adjacency[first].add(second);
                adjacency[second].add(first);
            }
            const degrees = adjacency.map(neighbourhood => neighbourhood.size);
            if (degrees[0] !== 4 || degrees.some((degree, v) => degree < 3 || degree > 4
                || (v > 0 && degree > degrees[v - 1]))) continue;
            const masks = adjacency.map(neighbourhood => [...neighbourhood].reduce((mask, v) => mask | (1 << v), 0));
            if (!isConnected(masks)) continue;
            let valid = true;
            for (let right = 1; right < order && valid; right++) {
                for (let left = 0; left < right && valid; left++) {
                    if (degrees[left] !== degrees[right]) continue;
                    // The first row at which two vertices can be
                    // distinguished must put the neighbour first.
                    for (let row = 0; row < left; row++) {
                        if (adjacency[row].has(left) === adjacency[row].has(right)) continue;
                        valid = adjacency[row].has(left);
                        break;
                    }
                }
            }
            if (!valid) continue;
            let hasClique = false;
            for (let first = 0; first < order; first++) {
                for (let second = first + 1; second < order; second++) {
                    if (!adjacency[first].has(second)) continue;
                    for (let third = second + 1; third < order; third++) {
                        if (!adjacency[first].has(third) || !adjacency[second].has(third)) continue;
                        for (let fourth = third + 1; fourth < order; fourth++) {
                            if ([first, second, third].every(v => adjacency[v].has(fourth))) hasClique = true;
                        }
                    }
                }
            }
            if (!hasClique) {
                const key = masks.join(",");
                bruteForce.add(key);
                if (adjacency.every((neighbours, v) => degrees[v] === 4
                    || [...neighbours].filter(u => degrees[u] === 3).length <= 1)) {
                    bruteCubicMatching.add(key);
                }
            }
        }
        for (let degreeFour = 1; degreeFour <= order; degreeFour++) {
            enumerate(order, degreeFour, adjacency => {
                if (!bruteForce.delete(adjacency.join(","))) throw new Error("Unexpected or repeated representative");
            });
            enumerate(order, degreeFour, adjacency => {
                if (!bruteCubicMatching.delete(adjacency.join(","))) throw new Error("Unexpected or repeated filtered representative");
            }, true);
        }
        if (bruteForce.size || bruteCubicMatching.size) throw new Error("Generator omitted representatives");
    }
}

checkExamples();
checkGenerator();
for (let order = firstOrder; order <= lastOrder; order++) {
    const byDegreeFour = [];
    for (let degreeFour = 1; degreeFour <= order; degreeFour++) {
        if (requestedQuarticCounts.length && !requestedQuarticCounts.includes(degreeFour)) continue;
        let checked = 0;
        enumerate(order, degreeFour, adjacency => {
            const neighbours = Array.from(adjacency, bits);
            if (cubicMatching && neighbours.some(row =>
                row.length === 3 && row.filter(v => neighbours[v].length === 3).length > 1)) {
                throw new Error("Cubic filter accepted a restricted representative");
            }
            const colours = findColouring(neighbours, 5);
            if (!verifyColouring(neighbours, colours, 5)) {
                throw new Error("No verified colouring for " + JSON.stringify(neighbours));
            }
            checked++;
            if (cubicMatching && checked % 1000000 === 0) {
                console.log(JSON.stringify({order, degreeFour, progress: checked}));
            }
        }, cubicMatching);
        if (checked > 0) byDegreeFour.push([degreeFour, checked]);
    }
    const total = byDegreeFour.reduce((sum, [, count]) => sum + count, 0);
    console.log(JSON.stringify({order, total, byDegreeFour}));
}
