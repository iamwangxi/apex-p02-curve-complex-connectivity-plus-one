#!/usr/bin/env python3
"""Offline exhaustive sanity check; not an input to the mathematical proof.

Enumerate oriented ribbon realizations of K4 and K4 minus one edge as
intersection graphs. Cyclic orders along each labelled oriented curve and
the two alternating rotations at each crossing determine the ribbon graph.
The program prints JSON to standard output and writes no files.
"""

from collections import Counter
from itertools import permutations, product
import json


def cycles(perm):
    unseen = set(perm)
    result = []
    while unseen:
        start = min(unseen)
        orbit = []
        x = start
        while x in unseen:
            unseen.remove(x)
            orbit.append(x)
            x = perm[x]
        assert x == start
        result.append(orbit)
    return result


def cyclic_orders(neighbors):
    first = min(neighbors)
    return [(first,) + p for p in permutations(x for x in neighbors if x != first)]


def check(edges):
    neighbors = {i: sorted(j if i == k else k for k, j in edges if i in (k, j))
                 for i in range(4)}
    total = 0
    genus_hist = Counter()
    target_loop_hist = Counter()
    target_face_length_hist = Counter()
    target_count = 0
    witness = None
    for orders in product(*(cyclic_orders(neighbors[i]) for i in range(4))):
        edge_flip = {}
        for i, order in enumerate(orders):
            for pos, j in enumerate(order):
                nxt = order[(pos + 1) % len(order)]
                a, b = (i, j, 1), (i, nxt, -1)
                edge_flip[a] = b
                edge_flip[b] = a
        assert len(edge_flip) == 4 * len(edges)
        assert all(edge_flip[edge_flip[d]] == d for d in edge_flip)
        for signs in product((-1, 1), repeat=len(edges)):
            rotation = {}
            for (i, j), sign in zip(edges, signs):
                around = [(i, j, 1), (j, i, sign), (i, j, -1), (j, i, -sign)]
                for a, b in zip(around, around[1:] + around[:1]):
                    rotation[a] = b
            assert all(rotation[rotation[d]] == (d[0], d[1], -d[2])
                       for d in rotation)
            face_perm = {d: rotation[edge_flip[d]] for d in edge_flip}
            faces = cycles(face_perm)
            face_id = {d: k for k, face in enumerate(faces) for d in face}
            twice_genus = len(edges) - len(faces) + 2
            assert twice_genus % 2 == 0
            genus = twice_genus // 2
            genus_hist[genus] += 1
            total += 1
            if genus != 3:
                continue
            target_count += 1
            graph_edges = [(d, edge_flip[d]) for d in edge_flip if d < edge_flip[d]]
            loops = [(a, b) for a, b in graph_edges if face_id[a] == face_id[b]]
            target_loop_hist[len(loops)] += 1
            target_face_length_hist[tuple(sorted(map(len, faces)))] += 1
            assert loops, "Counterexample to the same-face edge claim"
            assert len(faces) == len(edges) - 4
            if witness is None:
                witness = {
                    "cyclic_orders_along_curves": orders,
                    "alternating_crossing_signs": signs,
                    "face_cycles": faces,
                    "same_face_graph_edge": loops[0],
                }
    assert target_count > 0
    return {
        "intersection_edges": edges,
        "total_rotation_systems": total,
        "capped_genus_histogram": dict(sorted(genus_hist.items())),
        "genus_three_systems": target_count,
        "same_face_graph_edge_count_histogram": dict(sorted(target_loop_hist.items())),
        "genus_three_face_length_histogram": {
            str(k): v for k, v in sorted(target_face_length_hist.items())
        },
        "representative_genus_three_certificate": witness,
    }


def main():
    complete = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    result = {
        "scope": "Labelled oriented ribbon graphs; not isotopy classification or formal proof.",
        "missing_edge_reduction": "All six missing-edge choices are equivalent by relabelling.",
        "five_intersections": check([e for e in complete if e != (2, 3)]),
        "six_intersections": check(complete),
        "mathematical_dependency": "None. The written proof is independent of this enumeration.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
