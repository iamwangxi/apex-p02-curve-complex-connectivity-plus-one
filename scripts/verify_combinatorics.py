#!/usr/bin/env python3
"""Independent finite graph, multigraph, arithmetic and covering checks.

Prints JSON only; uses no ribbon insertion routines. Infinite topological and
homotopy conclusions require the accompanying written proof.
"""

from collections import Counter, deque
from itertools import combinations, combinations_with_replacement
from math import comb, isqrt
import json


def orbits(p):
    assert set(p) == set(p.values())
    todo = set(p)
    result = []
    while todo:
        start = min(todo)
        x, out = start, []
        while x in todo:
            todo.remove(x)
            out.append(x)
            x = p[x]
        assert x == start
        result.append(out)
    return result


def arithmetic():
    rows = []
    for g in range(3, 100001):
        b = 2 * g - 2
        h = (isqrt(16 * g - 15) - 1) // 2
        a = (1 + isqrt(16 * g - 15)) // 2
        assert a == h + 1
        assert comb(a, 2) <= b < comb(a + 1, 2)
        assert 3 <= a <= 2 * g - 3
        if g in (3, 4, 5, 6, 8, 9, 16, 25):
            rows.append([g, h, a])
    for m in range(2, 10001):
        assert (1 + isqrt(16 * m * m - 15)) // 2 == 2 * m
    for k in range(3, 10001):
        t = comb(k + 1, 2)
        assert comb(k, 2) <= t - 1
        if k % 2:
            assert comb(k, 2) <= t - 2
    return {"g_range": [3, 100000], "table_g_baseline_improved": rows,
            "square_m_range": [2, 10000]}


def all_dense_intersection_graphs():
    """Enumerate every dense labelled graph and each admissible even threshold."""
    rows = []
    total = Counter()
    for n in range(4, 9):
        pairs = list(combinations(range(n), 2))
        t = len(pairs)
        facet_bound = comb(n - 1, 2)
        bmin = max(4, facet_bound + facet_bound % 2)
        cases, graph_count = Counter(), 0
        for missing_number in range(t - bmin):
            for missing in combinations(range(t), missing_number):
                graph_count += 1
                degree = [n - 1] * n
                for e in missing:
                    a, b = pairs[e]
                    degree[a] -= 1
                    degree[b] -= 1
                i = t - missing_number
                for b in range(bmin, i, 2):
                    f = i - b
                    assert 1 <= f < n
                    assert all(d >= f for d in degree)
                    if f >= 3:
                        cases["F>=3"] += 1
                        r = f - 1
                        assert all(i - d + r < i for d in degree)
                    elif f == 2 and min(degree) >= 3:
                        cases["F=2,min_degree>=3"] += 1
                        assert all(i - d + 2 < i for d in degree)
                    elif f == 2:
                        cases["F=2,min_degree=2"] += 1
                        assert min(degree) == 2
                        assert b == facet_bound
                        assert any(d % 2 for d in degree)
                        assert all(i - d + 1 < i for d in degree)
                    elif min(degree) >= 2:
                        cases["F=1,min_degree>=2"] += 1
                        assert all(i - d + 1 < i for d in degree)
                    else:
                        cases["F=1,leaf"] += 1
                        leaves = [v for v, d in enumerate(degree) if d == 1]
                        assert len(leaves) == 1
                        assert b == facet_bound
                        assert all(i - d + 1 - int(v == leaves[0]) < i
                                   for v, d in enumerate(degree))
        total.update(cases)
        rows.append({"n": n, "labelled_graphs": graph_count,
                     "admissible_graph_B_pairs": sum(cases.values()),
                     "case_counts": dict(cases)})
    return {"rows": rows, "total_case_counts": dict(total)}


def girth(edges, f):
    if any(a == b for a, b in edges):
        return 1
    if len(set(edges)) < len(edges):
        return 2
    adj = [[] for _ in range(f)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    best = f + 1
    for start in range(f):
        distance, parent = {start: 0}, {start: -1}
        queue = deque([start])
        while queue:
            a = queue.popleft()
            for b in adj[a]:
                if b not in distance:
                    distance[b], parent[b] = distance[a] + 1, a
                    queue.append(b)
                elif parent[a] != b:
                    best = min(best, distance[a] + distance[b] + 1)
    return best


def multigraphs():
    rows = []
    for f in range(1, 6):
        kinds = list(combinations_with_replacement(range(f), 2))
        counts = Counter()
        for ids in combinations_with_replacement(range(len(kinds)), f + 1):
            length = girth([kinds[e] for e in ids], f)
            assert length <= (f - 1 if f >= 3 else f)
            counts[length] += 1
        rows.append({"F": f, "edges": f + 1,
                     "multigraphs": sum(counts.values()),
                     "girth_histogram": dict(counts)})
    return rows


def bipartite_ribbon(p, q):
    alpha, rho, color = {}, {}, {}
    for i in range(p):
        for j in range(q):
            eps = (-1) ** j
            around = [(0, i, j, 1), (1, i, j, eps),
                      (0, i, j, -1), (1, i, j, -eps)]
            for a, b in zip(around, around[1:] + around[:1]):
                rho[a] = b
            for s in (-1, 1):
                a, b = (0, i, j, s), (1, i, j, s)
                alpha[a] = (0, i, (j + s) % q, -s)
                alpha[b] = (1, (i + s) % p, j, -s)
                color[a], color[b] = (0, i), (1, j)
    return alpha, rho, color


def inspect(alpha, rho):
    assert all(alpha[alpha[d]] == d != alpha[d] for d in alpha)
    vertices = orbits(rho)
    assert all(len(v) == 4 for v in vertices)
    faces = orbits({d: rho[alpha[d]] for d in alpha})
    v_id = {d: i for i, v in enumerate(vertices) for d in v}
    f_id = {d: i for i, face in enumerate(faces) for d in face}
    edges = [(d, alpha[d]) for d in alpha if d < alpha[d]]
    assert (2 - len(vertices) + len(edges) - len(faces)) % 2 == 0
    genus = (2 - len(vertices) + len(edges) - len(faces)) // 2
    return vertices, faces, v_id, f_id, edges, genus


def bipartite_checks():
    count = 0
    for p in range(3, 22, 2):
        for q in range(2, 23, 2):
            alpha, rho, color = bipartite_ribbon(p, q)
            vertices, faces, _, f_id, edges, genus = inspect(alpha, rho)
            assert len(vertices) == p * q
            assert len(faces) == q
            assert {len(face) for face in faces} == {4 * p}
            assert genus == 1 + q * (p - 1) // 2
            loops = [d for d, e in edges if f_id[d] == f_id[e]]
            assert len(loops) == p * q
            assert all(color[d][0] == 0 for d in loops)
            phi = {d: rho[alpha[d]] for d in alpha}
            for d in alpha:
                if d[0] == 0:
                    _, i, j, s = d
                    assert phi[phi[d]] == (0, (i + s * (-1) ** j) % p,
                                            (j + s) % q, -s)
            assert p * q - q == 2 * genus - 2
            count += 1
    return {"parameter_pairs": count, "odd_p_range": [3, 21],
            "even_q_range": [2, 22]}


def mod_two_basis(vectors):
    basis = {}
    for value in vectors:
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return basis


def first_cover():
    alpha, rho, base_color = bipartite_ribbon(3, 2)
    vertices, faces, v_id, _, edges, _ = inspect(alpha, rho)
    # Build a spanning tree before reducing the cellular face relations.
    adj = [[] for _ in vertices]
    for e, (a, b) in enumerate(edges):
        adj[v_id[a]].append((v_id[b], e))
        adj[v_id[b]].append((v_id[a], e))
    tree, seen, queue = set(), {0}, deque([0])
    while queue:
        v = queue.popleft()
        for w, e in adj[v]:
            if w not in seen:
                seen.add(w)
                tree.add(e)
                queue.append(w)
    assert len(seen) == len(vertices)
    nontree = [e for e in range(len(edges)) if e not in tree]
    raw = {}
    for e, (a, b) in enumerate(edges):
        raw[a] = raw[b] = 0 if e in tree else 1 << nontree.index(e)
    relations = []
    for face in faces:
        value = 0
        for d in face:
            value ^= raw[d]
        relations.append(value)
    basis = mod_two_basis(relations)
    free = [j for j in range(len(nontree)) if j not in basis]

    def quotient(value):
        for pivot in sorted(basis, reverse=True):
            if value & (1 << pivot):
                value ^= basis[pivot]
        return sum(((value >> j) & 1) << i for i, j in enumerate(free))

    voltage = {d: quotient(raw[d]) for d in alpha}
    assert len(free) == 6
    assert len(mod_two_basis(voltage.values())) == 6
    for face in faces:
        value = 0
        for d in face:
            value ^= voltage[d]
        assert value == 0
    lifted_alpha, lifted_rho = {}, {}
    for d in alpha:
        for sheet in range(64):
            lifted_alpha[d, sheet] = (alpha[d], sheet ^ voltage[d])
            lifted_rho[d, sheet] = (rho[d], sheet)
    vertices, faces, _, f_id, edges, genus = inspect(lifted_alpha, lifted_rho)
    # Check connectedness of the covering graph, beyond the Euler count.
    start = min(lifted_alpha)
    seen, queue = {start}, deque([start])
    while queue:
        d = queue.popleft()
        for e in (lifted_alpha[d], lifted_rho[d]):
            if e not in seen:
                seen.add(e)
                queue.append(e)
    assert len(seen) == len(lifted_alpha)
    opposite = {d: lifted_rho[lifted_rho[d]] for d in lifted_alpha}
    through = {d: opposite[lifted_alpha[d]] for d in lifted_alpha}
    labels, groups = {}, Counter()
    for orbit in orbits(through):
        if orbit[0] in labels:
            continue
        name = len(set(labels.values()))
        origin = base_color[orbit[0][0]]
        groups[origin[0]] += 1
        for d in orbit + [opposite[e] for e in orbit]:
            assert d not in labels
            assert base_color[d[0]] == origin
            labels[d] = name
    crossing_pairs = []
    for vertex in vertices:
        colors = {labels[d] for d in vertex}
        assert len(colors) == 2
        crossing_pairs.append(tuple(sorted(colors)))
    assert len(set(crossing_pairs)) == len(crossing_pairs)
    degree = Counter(c for pair in crossing_pairs for c in pair)
    assert genus == 129 and len(vertices) == 384 and len(faces) == 128
    assert groups == {0: 96, 1: 64}
    assert {len(face) for face in faces} == {12}
    assert Counter(degree.values()) == {4: 96, 6: 64}
    assert all(f_id[a] != f_id[b] for a, b in edges)
    parallels, witness = {}, None
    for a, b in edges:
        key = tuple(sorted((f_id[a], f_id[b])))
        c = labels[a]
        if key in parallels and parallels[key] != c:
            witness = [list(key), parallels[key], c]
            break
        parallels[key] = c
    assert witness is not None
    return {"degree": 64, "H1_rank": 6, "connected": True,
            "genus": genus, "curves": len(degree),
            "intersections": len(vertices), "faces": len(faces),
            "face_lengths": [12], "group_sizes": dict(groups),
            "curve_degree_histogram": dict(Counter(degree.values())),
            "dual_systole": 2, "rainbow_two_cycle_witness": witness}


def subdivision_obstruction_check():
    rows = []
    for k in range(3, 9):
        originals = frozenset(range(k + 1))
        top = {originals}
        fresh = k + 1
        for _ in range(3):
            face = max(top, key=lambda x: tuple(sorted(x)))
            top.remove(face)
            top.update((face - {v}) | {fresh} for v in face)
            fresh += 1
        assert not any(originals <= face for face in top)
        assert set().union(*top) >= originals
        # A subdivision vertex joins original singletons only from its own face.
        assert max(len(face & originals) for face in top) == k
        rows.append({"dimension": k, "stellar_steps": 3,
                     "top_simplices": len(top),
                     "no_face_contains_all_original_vertices": True})
    return rows


if __name__ == "__main__":
    result = {"arithmetic": arithmetic(),
              "dense_intersection_graphs": all_dense_intersection_graphs(),
              "multigraph_lemma": multigraphs(),
              "bipartite_family": bipartite_checks(),
              "first_full_homology_cover": first_cover(),
              "subdivision_interface": subdivision_obstruction_check(),
              "status": "all finite assertions passed",
              "limits": "No finite check proves the infinite topology or homotopy statements."}
    print(json.dumps(result, ensure_ascii=False, indent=2))
