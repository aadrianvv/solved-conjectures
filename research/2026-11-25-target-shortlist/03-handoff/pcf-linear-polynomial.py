import json
import subprocess
import sys
from pathlib import Path


def repeated(pattern, width, count):
    accumulated = 0
    offset = 0
    while count:
        if count & 1:
            accumulated |= pattern << offset
            offset += width
        count >>= 1
        if count:
            pattern |= pattern << width
            width *= 2
    return accumulated


def basis(order):
    shifts = [5 ** i for i in range(order)]
    masks = [
        repeated((1 << (4 * shift)) - 1, 5 * shift, 5 ** (order - i - 1))
        for i, shift in enumerate(shifts)
    ]
    return shifts, masks


def evaluate(adjacency, shifts, masks, deduplicate=True):
    factors = [
        (v, u)
        for v, neighbours in enumerate(adjacency)
        for u in neighbours
        if v < u
    ] + [tuple(neighbours) for neighbours in adjacency]
    if deduplicate:
        factors = list(dict.fromkeys(factors))
    coefficients = 1
    for factor in factors:
        result = 0
        for v in factor:
            result ^= (coefficients & masks[v]) << shifts[v]
        coefficients = result
        if coefficients == 0:
            break
    return coefficients.bit_count()


if __name__ == "__main__":
    K5 = [tuple(j for j in range(5) if j != i) for i in range(5)]
    K44 = [tuple(j for j in range(8) if i // 4 != j // 4) for i in range(8)]
    assert not evaluate(K5, *basis(5))
    assert evaluate(K44, *basis(8)) == 8480
    assert not evaluate(K44, *basis(8), deduplicate=False)
    reference = (
        "C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/"
        "repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/"
        "check_03_conflict_free_colouring.js"
    )
    for order in map(int, sys.argv[1:]):
        code = Path(reference).read_text(encoding="utf-8").split("\ncheckExamples();", 1)[0]
        code += (
            f"\nenumerate({order}, {order}, (a) => "
            "console.log(JSON.stringify(Array.from(a, bits))));\n"
        )
        data = subprocess.Popen(["node", "-"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        data.stdin.write(code)
        data.stdin.close()
        shifts, masks = basis(order)
        count = 0
        zeros = 0
        for line in data.stdout:
            adjacency = json.loads(line)
            if not evaluate(adjacency, shifts, masks):
                if not zeros:
                    print("first zero", order, adjacency, flush=True)
                zeros += 1
            count += 1
            if count % 500 == 0:
                print("progress", order, count, zeros, flush=True)
        assert not data.wait()
        print("done", order, count, zeros, flush=True)
