#!/usr/bin/env python3
"""Stress-test a long rainbow cycle and consecutive filling replacements.

Loads sibling routines without calling their main functions or writing bytecode.
An independent integer-dart implementation checks every resulting ribbon graph.
Only JSON is printed.
"""

import sys
sys.dont_write_bytecode = True

from collections import Counter
from pathlib import Path
import json
import random


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "verify_ribbon_descent.py"
INDEPENDENT = HERE / "verify_combinatorics.py"


def load_read_only(path):
    namespace = {"__name__": "read_only_audit", "__file__": str(path)}
    exec(compile(path.read_text(), str(path), "exec"), namespace)
    return namespace


author = load_read_only(SOURCE)
independent = load_read_only(INDEPENDENT)


def validate(state):
    edge, rot, labels = state
    darts = list(edge)
    idx = {d: i for i, d in enumerate(darts)}
    alpha = {idx[d]: idx[edge[d]] for d in darts}
    rho = {idx[d]: idx[rot[d]] for d in darts}
    vertices, faces, _, _, _, genus = independent["inspect"](alpha, rho)
    pairs = []
    for vertex in vertices:
        colors = {labels[darts[d]] for d in vertex}
        assert len(colors) == 2
        assert all(labels[darts[rho[rho[d]]]] == labels[darts[d]] for d in vertex)
        pairs.append(tuple(sorted(colors)))
    assert len(set(pairs)) == len(pairs)
    info = author["inspect"](state)
    assert (len(vertices), len(faces), genus) == (info["I"], info["F"], info["genus"])
    assert Counter(c for pair in pairs for c in pair) == info["degree"]
    return info


def find_root():
    rng = random.Random(2026102301)
    for n in range(5, 11):
        for trial in range(10000):
            state = author["random_dense_ribbon"](n, rng)
            data = validate(state)
            b = 2 * data["genus"] - 2
            if data["genus"] < 3 or (n - 1) * (n - 2) // 2 > b or data["F"] < 4:
                continue
            _, dual = author["dual_data"](state, data)
            by_color = {c: [e for e in dual if e[2] == c and e[0] != e[1]]
                        for c in data["colors"]}
            if any(not edges for edges in by_color.values()):
                continue
            for _ in range(10):
                chosen = [rng.choice(by_color[c]) for c in data["colors"]]
                if len({tuple(sorted(e[:2])) for e in chosen}) < n:
                    continue
                cycle = author["shortest_cycle"](chosen, data["F"])
                assert 3 <= len(cycle) <= data["F"] - 1
                augmented = author["insert_dual_cycle"](state, cycle, n)
                crossed = {e[2] for e in cycle}
                for old in data["colors"]:
                    count = data["I"] - data["degree"][old] + len(cycle) - int(old in crossed)
                    if count <= b:
                        continue
                    child = author["remove_curve"](augmented, old)
                    assert child is not None
                    child_data = validate(child)
                    assert child_data["I"] == count < data["I"]
                    if child_data["genus"] == data["genus"]:
                        return state, cycle, {"seed": 2026102301, "n": n, "trial": trial}
                break
    raise AssertionError("No multi-stage filling example found in the deterministic search")


stats = Counter()
operations = []


def descend(state, actual_genus, depth, path, forced_cycle=None):
    data = validate(state)
    b = 2 * actual_genus - 2
    assert data["genus"] <= actual_genus
    stats["visited_nodes"] += 1
    if data["I"] <= b:
        stats["safe_nodes"] += 1
        return
    if data["genus"] < actual_genus:
        stats["nonfilling_boundary_cones"] += 1
        operations.append({"path": path, "depth": depth, "I": data["I"],
                           "operation": "essential-boundary cone (written lemma)"})
        return
    if forced_cycle is None:
        _, cycle, _ = author["choose_curve"](state, actual_genus)
    else:
        cycle = forced_cycle
    r = len(cycle)
    crossed = {e[2] for e in cycle}
    assert len(crossed) == r
    assert len({e[0] for e in cycle}) == r
    assert all(cycle[t][1] == cycle[(t + 1) % r][0] for t in range(r))
    fresh = max(data["colors"]) + 1
    augmented = author["insert_dual_cycle"](state, cycle, fresh)
    after = validate(augmented)
    assert after["genus"] == actual_genus
    assert after["I"] == data["I"] + r
    stats["filling_stellar_steps"] += 1
    stats["maximum_filling_depth"] = max(stats["maximum_filling_depth"], depth)
    child_counts = {old: data["I"] - data["degree"][old] + r - int(old in crossed)
                    for old in data["colors"]}
    assert all(count < data["I"] for count in child_counts.values())
    operations.append({"path": path, "depth": depth, "I": data["I"], "F": data["F"],
                       "rainbow_length": r, "crossed_colors": sorted(crossed),
                       "child_intersection_counts": child_counts})
    for old, count in child_counts.items():
        if count <= b:
            stats["safe_nodes"] += 1
            continue
        child = author["remove_curve"](augmented, old)
        assert child is not None
        assert validate(child)["I"] == count
        descend(child, actual_genus, depth + 1, path + [old])


if __name__ == "__main__":
    state, cycle, root = find_root()
    root_data = validate(state)
    root.update({"genus": root_data["genus"], "I": root_data["I"], "F": root_data["F"]})
    descend(state, root_data["genus"], 0, [], cycle)
    assert stats["maximum_filling_depth"] >= 1
    print(json.dumps({"root": root, "statistics": dict(stats), "operations": operations,
                      "status": "long rainbow and consecutive filling replacements checked",
                      "limits": "Uses the ribbon insertion routines; independent Euler/permutation checks. "
                                "Nonfilling cones use the written essential-boundary lemma."},
                     ensure_ascii=False, indent=2))
