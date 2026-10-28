#!/usr/bin/env python3
"""Finite checks for bounded-intersection replacement. Standard library; stdout only.

These checks do not prove the infinite theorem. The manuscript proves the
selection theorem, essentiality, compatible homotopies, and termination.
No imports of project modules, file writes, subprocesses, or network access.
"""
import collections
import itertools
import json
import math
import random


def popcount(value):
    return bin(value).count('1')


def components(vertex_count, edges, removed=0):
    parent = list(range(vertex_count))

    def root(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for j, (a, b) in enumerate(edges):
        if not (removed >> j) & 1:
            a, b = root(a), root(b)
            parent[a] = b
    return len({root(a) for a in range(vertex_count)})


def bridges(vertex_count, edges, removed):
    adj = [[] for _ in range(vertex_count)]
    for e, (a, b) in enumerate(edges):
        if e not in removed:
            adj[a].append((b, e))
            adj[b].append((a, e))
    discovery = [-1] * vertex_count
    low = [-1] * vertex_count
    found = set()
    timer = 0

    def visit(a, incoming=-1):
        nonlocal timer
        discovery[a] = low[a] = timer
        timer += 1
        for b, e in adj[a]:
            if e == incoming:
                continue
            if discovery[b] == -1:
                visit(b, e)
                low[a] = min(low[a], low[b])
                if low[b] > discovery[a]:
                    found.add(e)
            else:
                low[a] = min(low[a], discovery[b])

    for a in range(vertex_count):
        if discovery[a] == -1:
            visit(a)
    return found


def select_edges(vertex_count, edges, colors, capacity, target=None, order=None):
    """Cographic/partition matroid intersection by shortest augmenting paths.

    The finite implementation is independently compared with exhaustive maxima.
    The mathematical proof does not depend on this algorithm.
    """
    if order is None:
        order = list(range(len(edges)))
    selected = set()
    while target is None or len(selected) < target:
        outside = [e for e in order if e not in selected]
        count = collections.Counter(colors[e] for e in selected)
        forbidden = bridges(vertex_count, edges, selected)
        starts = [e for e in outside if e not in forbidden]
        predecessor = {e: None for e in starts}
        queue = collections.deque(starts)
        end = None
        swap_bridges = {}
        while queue:
            e = queue.popleft()
            if e not in selected:
                if count[colors[e]] < capacity:
                    end = e
                    break
                neighbors = [f for f in order if f in selected and colors[f] == colors[e]]
            else:
                if e not in swap_bridges:
                    swap_bridges[e] = bridges(vertex_count, edges, selected - {e})
                neighbors = [f for f in outside if f not in swap_bridges[e]]
            for f in neighbors:
                if f not in predecessor:
                    predecessor[f] = e
                    queue.append(f)
        if end is None:
            break
        path = set()
        while end is not None:
            path.add(end)
            end = predecessor[end]
        previous_size = len(selected)
        selected.symmetric_difference_update(path)
        assert len(selected) == previous_size + 1
        removed = sum(1 << e for e in selected)
        assert components(vertex_count, edges, removed) == 1
        assert max(collections.Counter(colors[e] for e in selected).values(), default=0) <= capacity
    return selected


def shortest_cycle(vertex_count, edges, available=None):
    if available is None:
        available = list(range(len(edges)))
    available = sorted(available)
    best = None
    adj = [[] for _ in range(vertex_count)]
    for e in available:
        a, b = edges[e]
        if a == b:
            return [e]
        adj[a].append((b, e))
        adj[b].append((a, e))
    for e in available:
        start, end = edges[e]
        pred = {start: None}
        queue = collections.deque([start])
        while queue and end not in pred:
            a = queue.popleft()
            for b, f in adj[a]:
                if f != e and b not in pred:
                    pred[b] = (a, f)
                    queue.append(b)
        if end in pred:
            cycle = [e]
            a = end
            while a != start:
                a, f = pred[a]
                cycle.append(f)
            if best is None or len(cycle) < len(best):
                best = cycle
                if len(best) == 2:
                    break
    return best


def small_multigraphs():
    graph_count = partition_cases = algorithm_cases = rank_cases = 0
    for vertex_count in range(1, 5):
        edge_types = list(itertools.combinations_with_replacement(range(vertex_count), 2))
        for edge_count in range(6):
            for edges in itertools.combinations_with_replacement(edge_types, edge_count):
                if components(vertex_count, edges) != 1:
                    continue
                graph_count += 1
                size = 1 << edge_count
                independent = [m for m in range(size) if components(vertex_count, edges, m) == 1]
                rank = []
                for a in range(size):
                    formula = popcount(a) - components(vertex_count, edges, a) + 1
                    brute = max(popcount(m) for m in independent if m & ~a == 0)
                    assert formula == brute
                    rank.append(formula)
                    rank_cases += 1
                color_numbers = [2] + ([3] if vertex_count <= 3 and edge_count <= 4 else [])
                for color_number in color_numbers:
                    for colors in itertools.product(range(color_number), repeat=edge_count):
                        parts = [sum(1 << e for e in range(edge_count) if colors[e] == a)
                                 for a in range(color_number)]
                        for capacity in (1, 2):
                            brute = max(
                                popcount(m) for m in independent
                                if all(popcount(m & part) <= capacity for part in parts)
                            )
                            bounds = []
                            for a in range(1 << color_number):
                                union = 0
                                for color in range(color_number):
                                    if (a >> color) & 1:
                                        union |= parts[color]
                                bounds.append(rank[union] + capacity * (color_number - popcount(a)))
                            assert brute == min(bounds)
                            partition_cases += 1
                            if edge_count <= 3 or partition_cases % 31 == 0:
                                actual = select_edges(vertex_count, edges, colors, capacity)
                                assert len(actual) == brute
                                algorithm_cases += 1
    return dict(connected_multigraphs=graph_count, rank_checks=rank_cases,
                partition_capacity_cases=partition_cases, augmenting_algorithm_checks=algorithm_cases)


def color_components(n, pairs, weights, subset):
    indices = [a for a in range(n) if (subset >> a) & 1]
    lookup = {a: j for j, a in enumerate(indices)}
    edges = [(lookup[a], lookup[b]) for (a, b), w in zip(pairs, weights)
             if w and a in lookup and b in lookup]
    return components(len(indices), edges) if indices else 0


def weighted_graphs():
    inputs = [(n, 1) for n in range(2, 7)]
    inputs += [(n, 2) for n in range(2, 6)]
    inputs += [(n, 3) for n in range(2, 5)]
    scanned = admissible = rank_checks = 0
    face_cases = collections.Counter()
    exceptional = collections.Counter()
    for n, d in inputs:
        pairs = list(itertools.combinations(range(n), 2))
        lower = max(2, d * math.comb(n - 1, 2))
        lower += lower % 2
        for weights in itertools.product(range(d + 1), repeat=len(pairs)):
            scanned += 1
            total = sum(weights)
            if total <= lower:
                continue
            degree = [sum(w for (a, b), w in zip(pairs, weights) if a == v or b == v)
                      for v in range(n)]
            subset_info = {}
            for u in range(1, (1 << n) - 1):
                intersections = sum(w for (a, b), w in zip(pairs, weights)
                                    if (u >> a) & 1 and (u >> b) & 1)
                subset_info[u] = (intersections, color_components(n, pairs, weights, u))
            for bound in range(lower, total, 2):
                admissible += 1
                face_number = total - bound
                face_cases[str(face_number)] += 1
                assert min(degree) >= face_number
                assert face_number <= d * (n - 1) < d * n
                assert total + 1 >= face_number + 1
                for u, (intersections, component_count) in subset_info.items():
                    assert intersections <= bound
                    rank = total - intersections - component_count + 1
                    assert rank + d * popcount(u) >= face_number + 1
                    rank_checks += 1
                if face_number == 1:
                    leaves = [v for v in range(n) if degree[v] == 1]
                    assert len(leaves) <= 1
                    crossing = [0] * n
                    crossing[leaves[0] if leaves else 0] = 1
                    cost = 1
                    if leaves:
                        exceptional['one_face_degree_one'] += 1
                elif face_number == 2:
                    low = [v for v in range(n) if degree[v] == 2]
                    assert len(low) <= 2
                    selected_colors = low + [v for v in range(n) if v not in low]
                    crossing = [int(v in selected_colors[:2]) for v in range(n)]
                    cost = 2
                    if low:
                        exceptional['two_face_degree_two'] += 1
                    if len(low) == 2:
                        exceptional['two_face_two_low_colors'] += 1
                else:
                    cost = face_number - 1
                    crossing = [0] * n  # worst-case upper bound; not a constructed curve
                assert all(total - degree[v] + cost - crossing[v] < total for v in range(n))
    return dict(scanned_weighted_graphs=scanned, admissible_even_bound_cases=admissible,
                color_subset_rank_inequalities=rank_checks, face_distribution=dict(sorted(face_cases.items(), key=lambda a: int(a[0]))),
                low_degree_cases=dict(exceptional))


def cycle_bound_checks():
    count = 0
    for vertices in range(1, 6):
        types = list(itertools.combinations_with_replacement(range(vertices), 2))
        for edges in itertools.combinations_with_replacement(types, vertices + 1):
            cycle = shortest_cycle(vertices, edges)
            assert cycle is not None
            assert len(cycle) <= (vertices - 1 if vertices >= 3 else vertices)
            count += 1
    return dict(multigraph_cycle_bound_cases=count)


def orbits(permutation):
    unseen = set(range(len(permutation)))
    result = []
    while unseen:
        a = min(unseen)
        cycle = []
        while a in unseen:
            unseen.remove(a)
            cycle.append(a)
            a = permutation[a]
        assert a == cycle[0]
        result.append(cycle)
    return result


def build_ribbon(n, weights, seed):
    rng = random.Random(seed)
    pairs = list(itertools.combinations(range(n), 2))
    vertex_pairs = [pair for pair, w in zip(pairs, weights) for _ in range(w)]
    count = len(vertex_pairs)
    alpha = [-1] * (4 * count)
    rho = [4 * v + (j + 1) % 4 for v in range(count) for j in range(4)]
    color = [a for i, j in vertex_pairs for a in (i, j, i, j)]
    sign = [1, 1, -1, -1] * count
    vertex = [v for v in range(count) for _ in range(4)]
    for a in range(n):
        occurrences = [(v, 0 if i == a else 1) for v, (i, j) in enumerate(vertex_pairs)
                       if i == a or j == a]
        assert occurrences
        rng.shuffle(occurrences)
        for current, following in zip(occurrences, occurrences[1:] + occurrences[:1]):
            plus = 4 * current[0] + current[1]
            minus = 4 * following[0] + following[1] + 2
            alpha[plus], alpha[minus] = minus, plus
    assert all(alpha[alpha[a]] == a and alpha[a] != a for a in range(len(alpha)))
    return dict(n=n, alpha=alpha, rho=rho, color=color, sign=sign, vertex=vertex)


def ribbon_data(ribbon):
    alpha, rho = ribbon['alpha'], ribbon['rho']
    faces = orbits([rho[alpha[a]] for a in range(len(alpha))])
    face_of = {a: j for j, face in enumerate(faces) for a in face}
    plus = [a for a in range(len(alpha)) if ribbon['sign'][a] == 1]
    edge_of = {h: j for j, a in enumerate(plus) for h in (a, alpha[a])}
    edges = [(ribbon['vertex'][a], ribbon['vertex'][alpha[a]]) for a in plus]
    dual = [(face_of[a], face_of[alpha[a]]) for a in plus]
    colors = [ribbon['color'][a] for a in plus]
    vertices = len(set(ribbon['vertex']))
    assert len(edges) == 2 * vertices
    assert components(vertices, edges) == 1
    genus_twice = vertices - len(faces) + 2
    assert genus_twice % 2 == 0
    return dict(faces=faces, plus=plus, edge_of=edge_of, edges=edges,
                dual=dual, colors=colors, vertices=vertices, genus=genus_twice // 2)


def binary_basis(rows):
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = row
                break
            row ^= basis[pivot]
    return basis


def reduces_to_zero(row, basis):
    while row:
        pivot = row.bit_length() - 1
        if pivot not in basis:
            return False
        row ^= basis[pivot]
    return True


def repair_certificate(ribbon, d, seed):
    data = ribbon_data(ribbon)
    n, total, face_number = ribbon['n'], data['vertices'], len(data['faces'])
    bound = 2 * data['genus'] - 2
    if bound < 2 or d * math.comb(n - 1, 2) > bound:
        return None
    degree = [data['colors'].count(a) for a in range(n)]
    assert min(degree) >= face_number
    selected = None
    if face_number >= 3:
        order = list(range(len(data['edges'])))
        random.Random(seed).shuffle(order)
        selected = select_edges(total, data['edges'], data['colors'], d,
                                target=face_number + 1, order=order)
        assert len(selected) >= face_number + 1
        cycle = shortest_cycle(face_number, data['dual'], selected)
        assert cycle is not None and len(cycle) <= face_number - 1
    elif face_number == 1:
        leaves = [a for a in range(n) if degree[a] == 1]
        assert len(leaves) <= 1
        color = leaves[0] if leaves else 0
        cycle = [data['colors'].index(color)]
    else:
        low = [a for a in range(n) if degree[a] == 2]
        assert len(low) <= 2
        loops = [e for e, (a, b) in enumerate(data['dual']) if a == b]
        if loops:
            cycle = loops[:1]
        else:
            chosen = (low + [a for a in range(n) if a not in low])[:2]
            cycle = [data['colors'].index(a) for a in chosen]
    multiplicity = collections.Counter(data['colors'][e] for e in cycle)
    assert max(multiplicity.values()) <= d
    cost = len(cycle)
    assert all(total - degree[a] + cost - multiplicity[a] < total for a in range(n))
    dual_boundary = [0] * face_number
    for e in cycle:
        a, b = data['dual'][e]
        dual_boundary[a] ^= 1
        dual_boundary[b] ^= 1
    assert not any(dual_boundary)
    # Independent mod-two cellular homology calculation: boundaries of dual
    # 2-cells are primal vertex cuts, not merely the selected-graph cycle test.
    rows = [0] * total
    for e, (a, b) in enumerate(data['edges']):
        rows[a] ^= 1 << e
        rows[b] ^= 1 << e
    assert not reduces_to_zero(sum(1 << e for e in cycle), binary_basis(rows))
    if selected is not None:
        assert components(total, data['edges'], sum(1 << e for e in selected)) == 1
    return dict(genus=data['genus'], n=n, d=d, I=total, F=face_number,
                cost=cost, repeated_color=max(multiplicity.values()) > 1,
                multiplicities=dict(sorted(multiplicity.items())))


def nullspace(rows, columns, prime):
    matrix = [[x % prime for x in row] for row in rows]
    pivots = []
    line = 0
    for column in range(columns):
        hit = next((j for j in range(line, len(matrix)) if matrix[j][column]), None)
        if hit is None:
            continue
        matrix[line], matrix[hit] = matrix[hit], matrix[line]
        inverse = pow(matrix[line][column], prime - 2, prime)
        matrix[line] = [(a * inverse) % prime for a in matrix[line]]
        for j in range(len(matrix)):
            if j != line and matrix[j][column]:
                coefficient = matrix[j][column]
                matrix[j] = [(a - coefficient * b) % prime
                             for a, b in zip(matrix[j], matrix[line])]
        pivots.append(column)
        line += 1
        if line == len(matrix):
            break
    result = []
    for free in range(columns):
        if free not in pivots:
            vector = [0] * columns
            vector[free] = 1
            for j, pivot in enumerate(pivots):
                vector[pivot] = (-matrix[j][free]) % prime
            result.append(vector)
    return result


def cyclic_cover(base, prime, seed):
    data = ribbon_data(base)
    rows = []
    for face in data['faces']:
        row = [0] * len(data['edges'])
        for h in face:
            row[data['edge_of'][h]] += base['sign'][h]
        rows.append(row)
    basis = nullspace(rows, len(data['edges']), prime)
    rng = random.Random(seed)
    for _ in range(10000):
        coefficients = [rng.randrange(prime) for _ in basis]
        voltage = [sum(c * b[e] for c, b in zip(coefficients, basis)) % prime
                   for e in range(len(data['edges']))]
        period = [sum(voltage[e] for e, a in enumerate(data['colors']) if a == color) % prime
                  for color in range(base['n'])]
        if all(period):
            break
    else:
        raise AssertionError('no nonzero curve periods found')
    assert all(sum(a * b for a, b in zip(row, voltage)) % prime == 0 for row in rows)
    alpha, rho, color, sign, vertex = [], [], [], [], []
    for h in range(len(base['alpha'])):
        for sheet in range(prime):
            movement = base['sign'][h] * voltage[data['edge_of'][h]]
            alpha.append(base['alpha'][h] * prime + (sheet + movement) % prime)
            rho.append(base['rho'][h] * prime + sheet)
            color.append(base['color'][h])
            sign.append(base['sign'][h])
            vertex.append(base['vertex'][h] * prime + sheet)
    cover = dict(n=base['n'], alpha=alpha, rho=rho, color=color, sign=sign, vertex=vertex)
    cover_data = ribbon_data(cover)
    assert cover_data['genus'] - 1 == prime * (data['genus'] - 1)
    assert len(cover_data['faces']) == prime * len(data['faces'])
    # Straight-through orbits in the positive orientation are the input curves.
    straight = [rho[rho[alpha[h]]] for h in range(len(alpha))]
    positive_orbits = [orbit for orbit in orbits(straight) if sign[orbit[0]] == 1]
    assert len(positive_orbits) == base['n']
    assert all(len({color[h] for h in orbit}) == 1 for orbit in positive_orbits)
    assert all(len({vertex[h] for h in orbit}) == len(orbit) for orbit in positive_orbits)
    intersections = collections.Counter()
    for h in range(len(rho)):
        if h % (4 * prime) < prime:  # one chosen dart per lifted base vertex
            a, b = color[h], color[rho[h]]
            intersections[tuple(sorted((a, b)))] += 1
    assert set(intersections.values()) == {prime}
    return cover


def ribbon_checks():
    certificates = []
    attempted = 0
    for n in range(2, 9):
        for d in range(1, 7):
            for trial in range(8):
                attempted += 1
                seed = 202610280000 + n * 1000 + d * 20 + trial
                ribbon = build_ribbon(n, [d] * math.comb(n, 2), seed)
                result = repair_certificate(ribbon, d, seed + 1)
                if result:
                    certificates.append(result)
    base = None
    for trial in range(100):
        candidate = build_ribbon(4, [1] * 6, 202610289000 + trial)
        if ribbon_data(candidate)['genus'] == 3:
            base = candidate
            base_trial = trial
            break
    assert base is not None
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    covers = []
    for prime in primes:
        for trial in range(4):
            seed = 2026102800000 + 100 * prime + trial
            cover = cyclic_cover(base, prime, seed)
            result = repair_certificate(cover, prime, seed + 33)
            assert result is not None
            covers.append(result)
    certificates += covers
    repeated = [a for a in certificates if a['repeated_color']]
    return dict(complete_ribbon_attempts=attempted, admissible_ribbon_certificates=len(certificates) - len(covers),
                cyclic_cover_certificates=len(covers), base_genus=3, base_n=4,
                base_seed=202610289000 + base_trial, cover_primes=primes,
                repeated_color_cycles=len(repeated),
                face_counts_at_least_number_of_colors=sum(a['F'] >= a['n'] for a in certificates),
                cycle_cost_distribution=dict(sorted(collections.Counter(a['cost'] for a in certificates).items())),
                repeated_color_examples=repeated[:8],
                largest_cover=max(covers, key=lambda a: a['I']))


def parameter_checks():
    count = 0
    for g in range(2, 1001):
        bound = 2 * g - 2
        for d in range(1, 501):
            root_floor = math.isqrt((d + 8 * bound) // d)
            old = (root_floor - 1) // 2
            new = old + 1
            assert d * math.comb(old + 1, 2) <= bound
            assert d * math.comb(old + 2, 2) > bound
            assert d * math.comb(new, 2) <= bound
            assert new <= bound - 1 or (g == 2 and new == 2 and d in (1, 2))
            count += 1
    return dict(genus_intersection_parameter_cases=count)


def main():
    if not __debug__:
        raise SystemExit("Run without -O; these checks rely on assertions.")
    report = {}
    for name, function in [('small_multigraphs', small_multigraphs),
                           ('weighted_intersection_graphs', weighted_graphs),
                           ('cycle_bound', cycle_bound_checks),
                           ('ribbon_and_cover_models', ribbon_checks),
                           ('parameters', parameter_checks)]:
        report[name] = function()
    report['all_passed'] = True
    print(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
