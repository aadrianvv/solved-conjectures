"use strict";

// Exhaustive local palette permutations for three-edge cuts.
const palette = [0, 1, 2, 3, 4];
const triplePatterns = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 2]];
const pairPatterns = [[0, 0], [0, 1]];

function cartesian(arrays) {
    if (arrays.length === 0) return [[]];
    const [first, ...rest] = arrays;
    return first.flatMap(value => cartesian(rest).map(row => [value, ...row]));
}

function permutations(colours) {
    if (colours.length === 0) return [[]];
    return colours.flatMap((colour, i) => permutations(colours.filter((_, j) => i !== j))
        .map(rest => [colour, ...rest]));
}

const maps = permutations(palette).map(forward => ({
    forward,
    reverse: palette.map(colour => forward.indexOf(colour)),
}));

function hasSingleton(colours) {
    return colours.some(colour => colours.indexOf(colour) === colours.lastIndexOf(colour));
}

function singleNeighbourChoices(colour) {
    return [-1, ...palette.filter(other => other !== colour)];
}

const tripleStates = triplePatterns.flatMap(colours =>
    cartesian(colours.map(singleNeighbourChoices)).map(bad => ({
        colours,
        bad,
        distinct: new Set(colours).size === 3,
        clean: colours.some((a, i) => colours.some((b, j) => a !== b && bad[i] !== b && bad[j] !== a)),
        cyclic: new Set(colours).size === 3 && new Set(bad).size === 3 && bad.every(a => colours.includes(a)),
    })));

const pairStates = pairPatterns.flatMap(colours => {
    const allowed = palette.filter(colour => colour !== colours[0]);
    const old = allowed.flatMap((colour, i) => [[colour], ...allowed.slice(i + 1).map(other => [colour, other])]);
    return cartesian([old, singleNeighbourChoices(colours[1])]).map(([shared, bad]) => ({colours, shared, bad}));
});

function acceptsOne(colour, bad, arriving) {
    return colour !== arriving && bad !== arriving;
}

function acceptsTwo(side, first, second) {
    return first !== side.colours[0] && second !== side.colours[0]
        && hasSingleton([...side.shared, first, second]);
}

function matching(first, second) {
    return maps.some(({forward, reverse}) => first.colours.every((a, i) =>
        acceptsOne(a, first.bad[i], forward[second.colours[i]])
        && acceptsOne(second.colours[i], second.bad[i], reverse[a])));
}

function starAndEdge(first, second) {
    const [a, b] = first.colours;
    const [x, y, z] = second.colours;
    return maps.some(({forward, reverse}) =>
        acceptsTwo(first, forward[x], forward[y])
        && acceptsOne(b, first.bad, forward[z])
        && acceptsOne(x, second.bad[0], reverse[a])
        && acceptsOne(y, second.bad[1], reverse[a])
        && acceptsOne(z, second.bad[2], reverse[b]));
}

function crossingPath(first, second) {
    const [a, b] = first.colours;
    const [x, y] = second.colours;
    return maps.some(({forward, reverse}) =>
        acceptsTwo(first, forward[x], forward[y])
        && acceptsOne(b, first.bad, forward[x])
        && acceptsTwo(second, reverse[a], reverse[b])
        && acceptsOne(y, second.bad, reverse[a]));
}

let incompatibleMatching = 0;
let requiredMatching = 0;
for (const first of tripleStates) {
    for (const second of tripleStates) {
        const required = (first.clean && (second.clean || second.distinct))
            || (second.clean && first.distinct)
            || (first.distinct && second.distinct && (!first.cyclic || !second.cyclic));
        const possible = matching(first, second);
        if (!possible) incompatibleMatching++;
        if (required) {
            requiredMatching++;
            if (!possible) throw new Error(JSON.stringify({shape: "matching", first, second}));
        }
    }
}

const hubStates = tripleStates.filter(({colours, bad}) =>
    hasSingleton(colours) && palette.some(colour => !colours.includes(colour) && !bad.includes(colour)));
for (const first of pairStates) {
    for (const second of hubStates) {
        if (!starAndEdge(first, second)) throw new Error(JSON.stringify({shape: "star and edge", first, second}));
    }
    for (const second of pairStates) {
        if (!crossingPath(first, second)) throw new Error(JSON.stringify({shape: "path", first, second}));
    }
}

let testedUniversalTerminal = 0;
for (const colours of triplePatterns) {
    const choices = colours.map(colour => {
        const allowed = palette.filter(other => other !== colour);
        return allowed.flatMap((other, i) => [[other], ...allowed.slice(i + 1).map(last => [other, last])]);
    });
    for (const oldNeighbourhoods of cartesian(choices)) {
        const possible = maps.some(({forward}) => {
            const incoming = colours.map(colour => forward[colour]);
            if (incoming.some((colour, i) => colour === i + 1) || !hasSingleton([0, ...incoming])) return false;
            return [1, 2, 3].some(restoredColour => !incoming.includes(restoredColour)
                && oldNeighbourhoods.every((old, i) =>
                    hasSingleton([...old.map(colour => forward[colour]), i + 1, restoredColour])));
        });
        if (!possible) throw new Error(JSON.stringify({shape: "universal terminal", colours, oldNeighbourhoods}));
        testedUniversalTerminal++;
    }
}

console.log(JSON.stringify({
    testedMatching: tripleStates.length ** 2,
    requiredMatching,
    incompatibleMatching,
    testedStarAndEdge: pairStates.length * hubStates.length,
    testedCrossingPath: pairStates.length ** 2,
    testedUniversalTerminal,
}));
