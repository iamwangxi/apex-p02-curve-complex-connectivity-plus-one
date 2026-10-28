#!/usr/bin/env python3
"""Offline ribbon-graph checks for the iterated-replacement proof.

The program prints JSON to standard output and writes no files. It is a finite
error check, not the proof of the uniform theorem or the covering tower.
"""

from collections import Counter, deque
from itertools import combinations
import json
import random


def cycles(perm):
    assert set(perm) == set(perm.values())
    seen, result = set(), []
    for start in perm:
        if start in seen:
            continue
        orbit, x = [], start
        while x not in seen:
            seen.add(x)
            orbit.append(x)
            x = perm[x]
        assert x == start
        result.append(orbit)
    return result


def make_ribbon(colors, crossing_pairs, orders, signs):
    edge, rotation, label = {}, {}, {}
    for i in colors:
        order = orders[i]
        for j, k in zip(order, order[1:] + order[:1]):
            a, b = (i, j, 1), (i, k, -1)
            edge[a], edge[b] = b, a
            label[a] = label[b] = i
    for (i, j), sign in zip(crossing_pairs, signs):
        around = [(i, j, 1), (j, i, sign), (i, j, -1), (j, i, -sign)]
        rotation.update(zip(around, around[1:] + around[:1]))
    return edge, rotation, label


def complete_ribbon(n, alternating=True):
    pairs = list(combinations(range(n), 2))
    orders = {i: [j for j in range(n) if i != j] for i in range(n)}
    signs = [(-1) ** (i + j) if alternating else 1 for i, j in pairs]
    return make_ribbon(range(n), pairs, orders, signs)


def inspect(state):
    edge, rot, label = state
    assert set(edge) == set(rot) == set(label)
    assert all(edge[edge[d]] == d and edge[d] != d for d in edge)
    vertices = cycles(rot)
    assert all(len(v) == 4 for v in vertices)
    pairs = []
    for v in vertices:
        colors = sorted({label[d] for d in v})
        assert len(colors) == 2
        assert all(label[rot[rot[d]]] == label[d] for d in v)
        pairs.append(tuple(colors))
    assert len(set(pairs)) == len(pairs)
    faces = cycles({d: rot[edge[d]] for d in edge})
    degree = Counter(x for pair in pairs for x in pair)
    genus_twice = len(vertices) + 2 - len(faces)
    assert genus_twice % 2 == 0
    return {
        "I": len(vertices), "F": len(faces), "genus": genus_twice // 2,
        "faces": faces, "degree": degree, "colors": sorted(degree),
    }


def dual_data(state, data):
    edge, rot, label = state
    face_id = {d: i for i, face in enumerate(data["faces"]) for d in face}
    representatives, seen = [], set()
    for d in edge:
        if d in seen:
            continue
        seen.update((d, edge[d]))
        representatives.append((face_id[d], face_id[edge[d]], label[d], d))
    return face_id, representatives


def shortest_cycle(edges, vertex_count):
    """Return ordered (from-face, to-face, color, primal-dart) edges."""
    best = None
    for excluded, (a, b, color, dart) in enumerate(edges):
        if a == b:
            return [(a, b, color, dart)]
        adj = [[] for _ in range(vertex_count)]
        for k, (x, y, c, d) in enumerate(edges):
            if k == excluded:
                continue
            adj[x].append((y, k))
            adj[y].append((x, k))
        queue, parent = deque([b]), {b: None}
        while queue and a not in parent:
            x = queue.popleft()
            for y, k in adj[x]:
                if y not in parent:
                    parent[y] = (x, k)
                    queue.append(y)
        if a not in parent:
            continue
        reverse_path, x = [], a
        while x != b:
            prev, k = parent[x]
            e = edges[k]
            reverse_path.append((prev, x, e[2], e[3]))
            x = prev
        cycle = [(a, b, color, dart)] + list(reversed(reverse_path))
        if best is None or len(cycle) < len(best):
            best = cycle
    assert best is not None
    return best


def choose_curve(state, actual_genus):
    data = inspect(state)
    n, I, F = len(data["colors"]), data["I"], data["F"]
    B = 2 * actual_genus - 2
    assert n >= 4 and (n - 1) * (n - 2) // 2 <= B < I
    assert data["genus"] == actual_genus
    face_id, dual = dual_data(state, data)
    assert F == I - B and all(d >= F for d in data["degree"].values())
    chosen = None
    if F == 1:
        leaves = [c for c, d in data["degree"].items() if d == 1]
        assert len(leaves) <= 1
        chosen = [next(e for e in dual if not leaves or e[2] == leaves[0])]
    elif F == 2 and min(data["degree"].values()) == 2:
        loops = [e for e in dual if e[0] == e[1]]
        # A degree-two vertex leaves a complete graph; it has an odd-degree
        # vertex. The written parity argument therefore forces a dual loop.
        if (n * (n - 1) // 2 - B) == n - 1:
            assert any(d % 2 for d in data["degree"].values())
            assert loops
        if loops:
            chosen = [loops[0]]
    if chosen is None:
        one_per_color = {}
        for item in dual:
            one_per_color.setdefault(item[2], item)
        assert len(one_per_color) == n > F
        chosen = shortest_cycle(list(one_per_color.values()), F)
        if F >= 3:
            assert len(chosen) <= F - 1
    colors = {e[2] for e in chosen}
    assert len(colors) == len(chosen)
    r = len(chosen)
    child_intersections = {
        c: I - data["degree"][c] + r - int(c in colors)
        for c in data["colors"]
    }
    assert all(x < I for x in child_intersections.values())
    return data, chosen, child_intersections


def insert_dual_cycle(state, cycle, new_color):
    old_edge, old_rot, old_label = state
    edge, rot, label = old_edge.copy(), old_rot.copy(), old_label.copy()
    info = inspect(state)
    face_id, _ = dual_data(state, info)
    incoming, outgoing = [], []
    serial = max((d[1] for d in edge if isinstance(d[0], str)), default=-1) + 1
    for t, (first, second, color, dart) in enumerate(cycle):
        other = old_edge[dart]
        if face_id[dart] != first:
            dart, other = other, dart
        assert face_id[dart] == first and face_id[other] == second
        ident = serial + t
        a, b, ci, co = [("insert", ident, k) for k in range(4)]
        edge[dart], edge[a] = a, dart
        edge[other], edge[b] = b, other
        around = [a, ci, b, co]
        rot.update(zip(around, around[1:] + around[:1]))
        label[a] = label[b] = color
        label[ci] = label[co] = new_color
        incoming.append(ci)
        outgoing.append(co)
    for t, co in enumerate(outgoing):
        ci = incoming[(t + 1) % len(incoming)]
        edge[co], edge[ci] = ci, co
    result = edge, rot, label
    after = inspect(result)
    assert after["I"] == info["I"] + len(cycle)
    assert after["F"] == info["F"] + len(cycle)
    assert after["genus"] == info["genus"]
    return result


def remove_curve(state, color):
    edge, rot, label = (x.copy() for x in state)
    vertices = cycles(rot)
    removed = {d for v in vertices if color in {label[x] for x in v} for d in v}
    for v in vertices:
        if color not in {label[x] for x in v}:
            continue
        rest = [d for d in v if label[d] != color]
        assert len(rest) == 2
        a, b = (edge[d] for d in rest)
        if a in removed or b in removed:
            # An isolated surviving curve implies the child is already safe.
            return None
        edge[a], edge[b] = b, a
    for d in removed:
        edge.pop(d)
        rot.pop(d)
        label.pop(d)
    return edge, rot, label


def descent_tree(state, genus, stats, depth=0):
    data = inspect(state)
    B = 2 * genus - 2
    stats["visited"] += 1
    stats["maximum_depth"] = max(stats["maximum_depth"], depth)
    if data["I"] <= B:
        stats["safe_leaves"] += 1
        return
    assert data["genus"] <= genus
    if data["genus"] < genus:
        # The old subsystem has essential neighborhood boundary; its cone
        # facets contain n-1 old curves and one disjoint new curve, hence safe.
        stats["nonfilling_terminal_cones"] += 1
        return
    data, cycle, children = choose_curve(state, genus)
    stats["stellar_steps"] += 1
    stats["cycle_length_histogram"][len(cycle)] += 1
    new_color = max(data["colors"]) + 1
    augmented = insert_dual_cycle(state, cycle, new_color)
    for old in data["colors"]:
        if children[old] <= B:
            stats["safe_leaves"] += 1
            continue
        child = remove_curve(augmented, old)
        assert child is not None
        child_data = inspect(child)
        assert child_data["I"] == children[old] < data["I"]
        assert len(child_data["colors"]) == len(data["colors"])
        descent_tree(child, genus, stats, depth + 1)


def random_dense_ribbon(n, rng):
    all_pairs = list(combinations(range(n), 2))
    missing = set(rng.sample(all_pairs, rng.randrange(n - 1)))
    pairs = [p for p in all_pairs if p not in missing]
    orders = {}
    for i in range(n):
        order = [b if a == i else a for a, b in pairs if i in (a, b)]
        rng.shuffle(order)
        orders[i] = order
    return make_ribbon(range(n), pairs, orders, [rng.choice((-1, 1)) for _ in pairs])


def chord_cross(a, b, length):
    if len(set(a + b)) < 4:
        return None
    inside = lambda x: 0 < (x - a[0]) % length < (a[1] - a[0]) % length
    if inside(b[0]) == inside(b[1]):
        return 0
    return 1 if inside(b[0]) else -1


def star_failure_certificate():
    edge, rot, label = complete_ribbon(5)
    data = inspect((edge, rot, label))
    faces = data["faces"]
    central = max(range(len(faces)), key=lambda k: len(faces[k]))
    pos = {d: (f, i) for f, face in enumerate(faces) for i, d in enumerate(face)}
    ds = [(0, 2, -1), (4, 1, -1), (1, 0, -1), (3, 0, -1)]
    leaf = pos[ds[0]][0]
    assert all(pos[d][0] == leaf and pos[edge[d]][0] == central for d in ds)
    leaf_positions = [pos[d][1] for d in ds]
    central_positions = [pos[edge[d]][1] for d in ds]
    first = chord_cross(tuple(leaf_positions[:2]), tuple(leaf_positions[2:]), len(faces[leaf]))
    second = chord_cross((central_positions[1], central_positions[0]),
                         (central_positions[3], central_positions[2]), len(faces[central]))
    assert abs(first + second) == 2
    return {"n": 5, "genus": 4, "leaf_darts": ds,
            "complete_face_cycles": faces,
            "leaf_endpoint_positions": leaf_positions,
            "central_endpoint_positions": central_positions,
            "oriented_intersection_contributions": [first, second],
            "geometric_intersection": 2,
            "meaning": "Two legal sparse neighbors of the original simplex need not be adjacent."}


def bipartite_ribbon(p, q):
    pairs = [(i, p + j) for i in range(p) for j in range(q)]
    orders = {i: list(range(p, p + q)) for i in range(p)}
    orders.update({p + j: list(range(p)) for j in range(q)})
    return make_ribbon(range(p + q), pairs, orders,
                       [(-1) ** (j - p) for i, j in pairs])


def first_homology_cover():
    """Construct the actual 64-sheeted first cover, using graph voltages."""
    edge, rot, old_label = bipartite_ribbon(3, 2)
    vertices = cycles(rot)
    vertex = {d: i for i, orbit in enumerate(vertices) for d in orbit}
    parent = list(range(len(vertices)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    seen, primal_edges, tree = set(), [], set()
    for d in edge:
        if d in seen:
            continue
        seen.update((d, edge[d]))
        k = len(primal_edges)
        primal_edges.append((d, edge[d]))
        a, b = find(vertex[d]), find(vertex[edge[d]])
        if a != b:
            parent[a] = b
            tree.add(k)
    assert len(tree) == len(vertices) - 1
    non_tree = [k for k in range(len(primal_edges)) if k not in tree]
    raw = {}
    for k, (d, other) in enumerate(primal_edges):
        raw[d] = raw[other] = 0 if k in tree else 1 << non_tree.index(k)
    base_faces = cycles({d: rot[edge[d]] for d in edge})
    relations = []
    for face in base_faces:
        value = 0
        for d in face:
            value ^= raw[d]
        relations.append(value)
    assert len(base_faces) == 2 and relations[0] == relations[1] != 0
    relation = relations[0]
    pivot = relation.bit_length() - 1
    positions = [k for k in range(len(non_tree)) if k != pivot]
    assert len(positions) == 6

    def quotient(value):
        if value & (1 << pivot):
            value ^= relation
        return sum(((value >> bit) & 1) << k for k, bit in enumerate(positions))

    voltage = {d: quotient(raw[d]) for d in edge}
    for face in base_faces:
        value = 0
        for d in face:
            value ^= voltage[d]
        assert value == 0
    base_darts = list(edge)
    index = {d: k for k, d in enumerate(base_darts)}
    lifted_edge, lifted_rot = {}, {}
    sheets = 1 << len(positions)
    for d in base_darts:
        for sheet in range(sheets):
            name = (index[d], sheet, 0)
            lifted_edge[name] = (index[edge[d]], sheet ^ voltage[d], 0)
            lifted_rot[name] = (index[rot[d]], sheet, 0)
    through = {d: lifted_rot[lifted_rot[lifted_edge[d]]] for d in lifted_edge}
    labels, origins, color = {}, {}, 0
    for orbit in cycles(through):
        if orbit[0] in labels:
            continue
        opposite = [lifted_rot[lifted_rot[d]] for d in orbit]
        original = old_label[base_darts[orbit[0][0]]]
        for d in orbit + opposite:
            assert d not in labels
            labels[d] = color
            assert old_label[base_darts[d[0]]] == original
        origins[color] = original
        color += 1
    state = lifted_edge, lifted_rot, labels
    data = inspect(state)
    assert data["genus"] == 129 and data["I"] == 384 and data["F"] == 128
    assert len(data["colors"]) == 160
    assert sorted({len(face) for face in data["faces"]}) == [12]
    group_counts = Counter("A" if origins[c] < 3 else "B" for c in data["colors"])
    assert group_counts == {"A": 96, "B": 64}
    degree_hist = Counter(data["degree"].values())
    assert degree_hist == {4: 96, 6: 64}
    _, dual = dual_data(state, data)
    assert all(a != b for a, b, _, _ in dual)
    parallel = {}
    essential_two_cycle = None
    for a, b, c, d in dual:
        key = tuple(sorted((a, b)))
        if key in parallel and parallel[key][2] != c:
            essential_two_cycle = [parallel[key][:3], (a, b, c)]
            break
        parallel[key] = (a, b, c, d)
    assert essential_two_cycle is not None
    return {"cover_degree": sheets, "homology_rank": len(positions),
            "genus": data["genus"], "curves": len(data["colors"]),
            "intersections": data["I"], "faces": data["F"],
            "face_lengths": [12], "group_counts": dict(group_counts),
            "intersection_degree_histogram": dict(degree_hist),
            "dual_systole": 2, "essential_two_cycle": essential_two_cycle}


def main():
    rng = random.Random(20261023)
    stats = {"visited": 0, "maximum_depth": 0, "safe_leaves": 0,
             "nonfilling_terminal_cones": 0, "stellar_steps": 0,
             "cycle_length_histogram": Counter()}
    inputs = []
    for n in range(4, 11):
        accepted = 0
        for attempt in range(2000):
            state = random_dense_ribbon(n, rng)
            data = inspect(state)
            if data["genus"] < 3 or (n - 1) * (n - 2) // 2 > 2 * data["genus"] - 2:
                continue
            if data["I"] <= 2 * data["genus"] - 2:
                continue
            initial = data["I"] - (2 * data["genus"] - 2)
            descent_tree(state, data["genus"], stats)
            accepted += 1
            assert initial <= n - 1
            if accepted == 30:
                break
        assert accepted
        inputs.append({"n": n, "accepted_dense_ribbon_inputs": accepted})
    square_rows = []
    for m in range(2, 16):
        state = complete_ribbon(2 * m + 1)
        data = inspect(state)
        _, dual = dual_data(state, data)
        center = max(range(len(data["faces"])), key=lambda i: len(data["faces"][i]))
        assert all((a == center) != (b == center) for a, b, _, _ in dual)
        assert all(len({state[2][d] for d in f}) == 2 * m + 1
                   for i, f in enumerate(data["faces"]) if i != center)
        _, cycle, children = choose_curve(state, m * m)
        square_rows.append({"m": m, "genus": m * m, "F": data["F"],
                            "dual_loops": 0, "selected_cycle_length": len(cycle),
                            "maximum_child_intersections": max(children.values())})
        if m <= 5:
            descent_tree(state, m * m, stats)
    benchmark = []
    for p in range(3, 16, 2):
        for q in range(2, 17, 2):
            state = bipartite_ribbon(p, q)
            data = inspect(state)
            _, dual = dual_data(state, data)
            loops = [item for item in dual if item[0] == item[1]]
            assert len(loops) == p * q
            assert all(item[2] < p for item in loops)
            assert data["F"] == q
            assert data["genus"] == 1 + q * (p - 1) // 2
            assert data["I"] - q == 2 * data["genus"] - 2
            benchmark.append({"p": p, "q": q, "same_face_A_edges": len(loops)})
    stats["cycle_length_histogram"] = dict(sorted(stats["cycle_length_histogram"].items()))
    result = {"status": "finite assertions passed", "random_inputs": inputs,
              "actual_ribbon_descent_statistics": stats, "square_genus_family": square_rows,
              "coface_adjacency_failure": star_failure_certificate(),
              "bipartite_benchmark": benchmark,
              "first_full_homology_cover": first_homology_cover(),
              "limitations": ["No formal verification or proof of a new leading asymptotic constant.",
                              "Nonfilling terminal cones are justified by the written surface lemma."]}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
