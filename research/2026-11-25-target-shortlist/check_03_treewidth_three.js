"use strict";

const assert = require("node:assert/strict");

const palette = [0, 1, 2, 3, 4];
const boundary = [0, 1, 2];
const bag = [0, 1, 2, 3];
const pivot = 3;
const facets = boundary.map(excluded => bag.filter(vertex => vertex !== excluded));
const colourPatterns = ["000", "001", "010", "011", "012"];

function edgeBit(left, right, order) {
  const start = order === 3 ? [0, 2] : [0, 3, 5];
  return 1 << (start[left] + right - left - 1);
}

function degrees(mask, order) {
  const result = Array(order).fill(0);
  for (let left = 0; left < order; left += 1) {
    for (let right = left + 1; right < order; right += 1) {
      if (!(mask & edgeBit(left, right, order))) continue;
      result[left] += 1;
      result[right] += 1;
    }
  }
  return result;
}

function inducedMask(mask, vertices) {
  let result = 0;
  for (const left of boundary) for (const right of boundary) {
    if (left >= right) continue;
    if (mask & edgeBit(vertices[left], vertices[right], bag.length)) {
      result |= edgeBit(left, right, boundary.length);
    }
  }
  return result;
}

function singleton(row) {
  return row.slice(1).includes(1);
}

// Degree-four rows have already been checked and need only their own colour.
function satisfied(row, degree) {
  return degree === 4 || singleton(row);
}

function encode(rows, usedDegrees) {
  const activeRows = rows.map((row, vertex) => {
    if (usedDegrees[vertex] < 4) return row;
    // An all-zero count vector is the marker for a previously checked row.
    if (row.slice(1).some(Boolean) && !singleton(row)) return null;
    return [row[0], 0, 0, 0, 0, 0];
  });
  if (activeRows.includes(null)) return null;
  const named = [...new Set(activeRows.map(row => row[0]))];
  const remaining = palette.filter(colour => !named.includes(colour));
  remaining.sort((left, right) => {
    for (const row of activeRows) {
      const difference = row[left + 1] - row[right + 1];
      if (difference) return difference;
    }
    return 0;
  });
  const order = named.concat(remaining);
  return activeRows.map(row => (
    [order.indexOf(row[0]), ...order.map(colour => row[colour + 1])].join("")
  )).join("");
}

function decode(signature) {
  const rows = [];
  for (let offset = 0; offset < signature.length; offset += 6) {
    rows.push([...signature.slice(offset, offset + 6)].map(Number));
  }
  return rows;
}

function bagColourings(mask, usedDegrees) {
  const result = new Set();
  for (const a of palette) for (const b of palette) {
    for (const c of palette) for (const d of palette) {
      const colours = [a, b, c, d];
      const rows = colours.map(colour => [colour, 0, 0, 0, 0, 0]);
      let proper = true;
      for (const left of bag) for (const right of bag) {
        if (left >= right || !(mask & edgeBit(left, right, bag.length))) continue;
        proper &&= colours[left] !== colours[right];
        rows[left][colours[right] + 1] += 1;
        rows[right][colours[left] + 1] += 1;
      }
      if (proper) result.add(encode(rows, usedDegrees));
    }
  }
  return result;
}

function permutations(values) {
  if (values.length === 0) return [[]];
  return values.flatMap(value => (
    permutations(values.filter(other => other !== value)).map(order => [value, ...order])
  ));
}

const alignmentCache = new Map();
function alignments(target, source) {
  const key = target.join("") + source.join("");
  if (alignmentCache.has(key)) return alignmentCache.get(key);
  const fixed = new Map();
  const images = new Set();
  let compatible = true;
  for (const index of boundary) {
    const colour = source[index];
    const image = target[index];
    if (fixed.has(colour)) compatible &&= fixed.get(colour) === image;
    else {
      compatible &&= !images.has(image);
      fixed.set(colour, image);
      images.add(image);
    }
  }
  const mappings = compatible ? permutations(palette.filter(colour => !images.has(colour)))
    .map(order => palette.map(colour => fixed.has(colour) ? fixed.get(colour) : order.shift()))
    : [];
  alignmentCache.set(key, mappings);
  return mappings;
}

// Subtract the boundary edges of the attached piece because the host already
// accounts for them. Group its signatures by the fixed boundary colours.
function interiorCounts(state) {
  const groups = new Map();
  for (const signature of state.rows) {
    const rows = signature.map(row => row.slice());
    for (const left of boundary) for (const right of boundary) {
      if (left >= right || !(state.mask & edgeBit(left, right, boundary.length))) continue;
      rows[left][rows[right][0] + 1] -= 1;
      rows[right][rows[left][0] + 1] -= 1;
    }
    const key = rows.map(row => row[0]).join("");
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(rows);
  }
  return [...groups].map(([key, rows]) => [[...key].map(Number), rows]);
}

function merge(host, attached, positions, usedDegrees) {
  const signatures = new Set();
  for (const left of host.rows) {
    const target = positions.map(vertex => left[vertex][0]);
    for (const [source, options] of attached.interior) {
      const mappings = alignments(target, source);
      for (const right of options) for (const mapping of mappings) {
        const rows = left.map(row => row.slice());
        for (const local of boundary) for (const colour of palette) {
          rows[positions[local]][mapping[colour] + 1] += right[local][colour + 1];
        }
        const signature = encode(rows, usedDegrees);
        if (signature !== null) signatures.add(signature);
      }
    }
  }
  return signatures;
}

const exteriorCache = new Map();
function exteriorCounts(colour, usedDegree) {
  const key = colour + ":" + usedDegree;
  if (exteriorCache.has(key)) return exteriorCache.get(key);
  const allowed = palette.filter(candidate => candidate !== colour);
  const options = [];
  const counts = Array(palette.length).fill(0);
  function generate(remaining, first) {
    if (!remaining) {
      options.push(counts.slice());
      return;
    }
    for (let index = first; index < allowed.length; index += 1) {
      counts[allowed[index]] += 1;
      generate(remaining - 1, index);
      counts[allowed[index]] -= 1;
    }
  }
  for (let count = Math.max(0, 3 - usedDegree); count <= 4 - usedDegree; count += 1) {
    generate(count, 0);
  }
  exteriorCache.set(key, options);
  return options;
}

const witnessCache = new Map();
function acceptingOutside(colour, counts, usedDegree) {
  const key = [colour, usedDegree, ...counts].join("");
  if (witnessCache.has(key)) return witnessCache.get(key);
  const options = exteriorCounts(colour, usedDegree);
  const accepted = [];
  for (const [index, outside] of options.entries()) {
    if (outside.some((count, hue) => count + counts[hue] === 1)) accepted.push(index);
  }
  witnessCache.set(key, accepted);
  return accepted;
}

function exteriorProfile(signatures, usedDegrees) {
  const sizes = usedDegrees.map(degree => exteriorCounts(0, degree).length);
  const block = sizes.reduce((product, size) => product * size, 1);
  const profile = new Uint32Array(Math.ceil(colourPatterns.length * block / 32));
  const filled = Array(colourPatterns.length).fill(0);
  for (const rows of signatures) {
    const colours = rows.map(row => row[0]);
    const pattern = colourPatterns.indexOf(colours.join(""));
    assert(pattern >= 0);
    if (filled[pattern] === block) continue;
    for (const mapping of alignments(colours, colours)) {
      const accepted = rows.map((row, vertex) => {
        const counts = Array(palette.length).fill(0);
        for (const hue of palette) counts[mapping[hue]] = row[hue + 1];
        return acceptingOutside(row[0], counts, usedDegrees[vertex]);
      });
      for (const first of accepted[0]) for (const second of accepted[1]) {
        for (const third of accepted[2]) {
          const index = pattern * block + (first * sizes[1] + second) * sizes[2] + third;
          const word = index >>> 5;
          const bit = 1 << (index & 31);
          if (profile[word] & bit) continue;
          profile[word] |= bit;
          filled[pattern] += 1;
        }
      }
    }
  }
  return profile;
}

function signatureSubset(left, right) {
  return left.size <= right.size && [...left].every(signature => right.has(signature));
}

function profileSubset(left, right) {
  return left.every((word, index) => (word & ~right[index]) === 0);
}

function verifyClosure() {
  const queue = [];
  const classes = new Map();
  const trianglesByMask = Array.from({length: 8}, () => []);
  const facetsByMask = Array.from({length: 8}, () => []);
  const stats = {
    states: 0, representatives: 0, boundaryStates: 0, bagStates: 0,
    facetJoins: 0, boundaryJoins: 0, projections: 0, terminalTests: 0,
  };

  function save(state) {
    const key = [state.isBag, state.mask, ...state.degrees, state.lastFacet].join(":");
    const group = classes.get(key) ?? [];
    const subset = state.isBag
      ? (left, right) => signatureSubset(left.signatures, right.signatures)
      : (left, right) => profileSubset(left.profile, right.profile);
    if (group.some(known => known.live && subset(known, state))) return;
    for (const known of group) {
      if (known.live && subset(state, known)) known.live = false;
    }
    state.live = true;
    group.push(state);
    classes.set(key, group);
    queue.push(state);
    if (state.isBag) stats.bagStates += 1;
    else stats.boundaryStates += 1;
  }

  function saveBoundary(mask, usedDegrees, singleInterior, signatures) {
    const boundaryDegrees = degrees(mask, boundary.length);
    const contributions = usedDegrees.map((degree, index) => degree - boundaryDegrees[index]);
    if (contributions.some(count => count < 1)) return;
    if (!singleInterior && contributions.reduce((sum, count) => sum + count, 0) < 4) return;
    assert(signatures.size > 0, "boundary without a partial colouring");
    const rows = [...signatures].map(decode);
    if (usedDegrees.every(degree => degree >= 3)) {
      stats.terminalTests += 1;
      assert(rows.some(signature => (
        signature.every((row, index) => satisfied(row, usedDegrees[index]))
      )), "boundary without a full colouring");
    }
    if (usedDegrees.includes(4)) return;
    const profile = exteriorProfile(rows, usedDegrees);
    save({isBag: false, mask, degrees: usedDegrees, signatures, rows, profile});
  }

  function project(mask, usedDegrees, lastFacet, rows) {
    if (usedDegrees[pivot] < 3) return;
    stats.projections += 1;
    const projected = usedDegrees.slice(0, pivot);
    const signatures = new Set();
    for (const signature of rows) {
      if (!satisfied(signature[pivot], usedDegrees[pivot])) continue;
      signatures.add(encode(signature.slice(0, pivot), projected));
    }
    saveBoundary(inducedMask(mask, boundary), projected, lastFacet < 0, signatures);
  }

  function saveBag(mask, usedDegrees, lastFacet, signatures) {
    assert(signatures.size > 0, "bag without a partial colouring");
    const rows = [...signatures].map(decode);
    const untreated = boundary.filter(index => (
      index > lastFacet && facets[index].every(vertex => usedDegrees[vertex] < 4)
    ));
    if (untreated.length === 0) {
      project(mask, usedDegrees, lastFacet, rows);
      return;
    }
    const boundaryDegrees = degrees(inducedMask(mask, boundary), boundary.length);
    if (boundary.some(vertex => usedDegrees[vertex] === boundaryDegrees[vertex]
      && !untreated.some(index => facets[index].includes(vertex)))) return;
    save({isBag: true, mask, degrees: usedDegrees, lastFacet, signatures, rows});
  }

  function join(host, attached, positions, lastFacet) {
    const usedDegrees = host.degrees.slice();
    const countedDegrees = degrees(attached.mask, boundary.length);
    for (const local of boundary) {
      const vertex = positions[local];
      usedDegrees[vertex] += attached.degrees[local] - countedDegrees[local];
      if (usedDegrees[vertex] > 4) return;
    }
    const signatures = merge(host, attached, positions, usedDegrees);
    if (host.isBag) {
      stats.facetJoins += 1;
      saveBag(host.mask, usedDegrees, lastFacet, signatures);
    } else {
      stats.boundaryJoins += 1;
      saveBoundary(host.mask, usedDegrees, false, signatures);
    }
  }

  for (let mask = 0; mask < 63; mask += 1) {
    const usedDegrees = degrees(mask, bag.length);
    saveBag(mask, usedDegrees, -1, bagColourings(mask, usedDegrees));
  }
  for (const state of queue) {
    if (!state.live) continue;
    stats.states += 1;
    if (state.isBag) {
      project(state.mask, state.degrees, state.lastFacet, state.rows);
      for (let index = state.lastFacet + 1; index < facets.length; index += 1) {
        const mask = inducedMask(state.mask, facets[index]);
        for (const attached of trianglesByMask[mask]) {
          if (attached.live) join(state, attached, facets[index], index);
        }
        facetsByMask[mask].push({host: state, index});
      }
    } else {
      state.interior = interiorCounts(state);
      for (const host of trianglesByMask[state.mask]) {
        if (host.live) join(host, state, boundary, -1);
      }
      join(state, state, boundary, -1);
      for (const {host, index} of facetsByMask[state.mask]) {
        if (host.live) join(host, state, facets[index], index);
      }
      trianglesByMask[state.mask].push(state);
    }
  }
  stats.representatives = queue.filter(state => state.live).length;
  return stats;
}

console.log(JSON.stringify(verifyClosure()));
