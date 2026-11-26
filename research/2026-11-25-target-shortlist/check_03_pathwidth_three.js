"use strict";

// Exact frontier search for the structural pathwidth-three class in the note.
const assert = require("node:assert/strict");
const boundary = [0, 1, 2];
const palette = [0, 1, 2, 3, 4];
const allBoundary = 7;
const introduced = 3;

function countBits(mask) {
  let count = 0;
  for (let bits = mask; bits; bits &= bits - 1) count += 1;
  return count;
}

function pairBit(left, right) {
  if (left === 0) return 1 << (right - 1);
  return 4;
}

function edgeCountAt(mask, vertex) {
  return boundary.filter(other => (
    other !== vertex &&
    (mask & pairBit(Math.min(vertex, other), Math.max(vertex, other)))
  )).length;
}

function hasSingleton(row) {
  return row.slice(1).includes(1);
}

// A row contains the vertex colour and the counts of the five neighbour colours.
// Active vertex colours are named in first-appearance order. Colours not on
// active vertices are then ordered by their count vectors across the boundary.
function encode(rows) {
  const present = [];
  for (const [colour] of rows) {
    if (!present.includes(colour)) present.push(colour);
  }
  const absent = palette.filter(colour => !present.includes(colour));
  absent.sort((left, right) => {
    for (const row of rows) {
      const difference = row[left + 1] - row[right + 1];
      if (difference) return difference;
    }
    return 0;
  });
  const order = present.concat(absent);
  return rows.map(row => (
    [order.indexOf(row[0]), ...order.map(colour => row[colour + 1])].join("")
  )).join("");
}

function decode(signature) {
  return boundary.map(index => [...signature.slice(6 * index, 6 * index + 6)].map(Number));
}

function firstSignatures(edgeMask) {
  const neighbours = [[], [], [], boundary.slice()];
  for (const left of boundary) {
    neighbours[left].push(introduced);
    for (const right of boundary) {
      if (left < right && (edgeMask & pairBit(left, right))) {
        neighbours[left].push(right);
        neighbours[right].push(left);
      }
    }
  }
  const signatures = new Set();
  for (const a of palette) for (const b of palette) {
    for (const c of palette) for (const d of palette) {
      const colours = [a, b, c, d];
      if (neighbours.some((adjacent, vertex) => (
        adjacent.some(other => colours[other] === colours[vertex])
      ))) continue;
      const rows = neighbours.map((adjacent, vertex) => {
        const row = [colours[vertex], 0, 0, 0, 0, 0];
        for (const other of adjacent) row[colours[other] + 1] += 1;
        return row;
      });
      if (hasSingleton(rows.pop())) signatures.add(encode(rows));
    }
  }
  return signatures;
}

function extendSignatures(signatures, attachMask, retire) {
  const result = new Set();
  for (const rows of signatures) for (const colour of palette) {
    if (rows.some((row, index) => (attachMask & (1 << index)) && row[0] === colour)) continue;
    const updated = rows.map(row => row.slice());
    const newRow = [colour, 0, 0, 0, 0, 0];
    for (const index of boundary) {
      if (!(attachMask & (1 << index))) continue;
      updated[index][colour + 1] += 1;
      newRow[updated[index][0] + 1] += 1;
    }
    updated.push(newRow);
    if (!hasSingleton(updated[retire])) continue;
    updated.splice(retire, 1);
    result.add(encode(updated));
  }
  return result;
}

function updatedEdgeMask(edgeMask, attachMask, retire) {
  const remaining = [0, 1, 2, 3].filter(index => index !== retire);
  let result = 0;
  for (const left of boundary) for (const right of boundary) {
    if (left >= right) continue;
    const originalLeft = remaining[left];
    const originalRight = remaining[right];
    const adjacent = originalRight === introduced
      ? attachMask & (1 << originalLeft)
      : edgeMask & pairBit(originalLeft, originalRight);
    if (adjacent) result |= pairBit(left, right);
  }
  return result;
}

function verifyClosure() {
  const states = [];
  const seen = new Set();
  let largestSignatureSet = 0;
  let transitions = 0;
  let terminalStates = 0;

  function save(mask, degrees, signatures, singleRetired) {
    assert(signatures.size > 0, "reachable frontier without a surviving colouring");
    const sorted = [...signatures].sort();
    const key = [mask, ...degrees, Number(singleRetired), ...sorted].join(":");
    if (seen.has(key)) return;
    seen.add(key);
    largestSignatureSet = Math.max(largestSignatureSet, sorted.length);
    states.push({mask, degrees, signatures: sorted.map(decode), singleRetired});
  }

  for (let mask = 0; mask < allBoundary; mask += 1) {
    const degrees = boundary.map(vertex => 1 + edgeCountAt(mask, vertex));
    save(mask, degrees, firstSignatures(mask), true);
  }

  for (const {mask, degrees, signatures, singleRetired} of states) {
    if (degrees.every(degree => degree >= 3)) {
      terminalStates += 1;
      assert(signatures.some(rows => rows.every(hasSingleton)), "bad terminal frontier");
    }
    if (degrees.includes(4)) continue;
    if (!singleRetired && degrees.reduce((sum, degree) => sum + degree, 0) > 9) continue;

    for (let attachMask = 1; attachMask <= allBoundary; attachMask += 1) {
      if (mask === allBoundary && attachMask === allBoundary) continue;
      for (let retire = 0; retire <= introduced; retire += 1) {
        if (retire !== introduced && !(attachMask & (1 << retire))) continue;
        const newDegrees = degrees.map((degree, index) => degree + ((attachMask >> index) & 1));
        newDegrees.push(countBits(attachMask));
        if (newDegrees[retire] < 3) continue;
        newDegrees.splice(retire, 1);
        const newMask = updatedEdgeMask(mask, attachMask, retire);
        const degreeSum = newDegrees.reduce((sum, degree) => sum + degree, 0);
        if (degreeSum - 2 * countBits(newMask) < 4) continue;
        if (newDegrees.some(degree => degree < 3) && (newDegrees.includes(4) || degreeSum > 9)) {
          continue;
        }
        transitions += 1;
        save(newMask, newDegrees, extendSignatures(signatures, attachMask, retire), false);
      }
    }
  }

  return {states: states.length, transitions, terminalStates, largestSignatureSet};
}

console.log(JSON.stringify(verifyClosure()));
