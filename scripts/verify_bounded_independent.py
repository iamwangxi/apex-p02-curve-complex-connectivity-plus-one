#!/usr/bin/env python3
"""Independent finite checks for bounded-intersection replacement.

Standard library; deterministic JSON on stdout; no file writes or project imports.
Finite experiments supplement the proofs; they do not certify infinite homotopy
statements or arbitrary isotopy classes. The four phases may be run separately.
"""
import argparse
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement, product
import json
from math import comb, isqrt
import random

SEED = 202610280811


def pop(x):
    return bin(x).count('1')


def bits(x):
    while x:
        b = x & -x
        yield b.bit_length() - 1
        x ^= b


def gf_basis(rows):
    basis = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in basis:
                row ^= basis[p]
            else:
                basis[p] = row
                break
    return basis


def gf_reduce(row, basis):
    while row:
        p = row.bit_length() - 1
        if p not in basis:
            break
        row ^= basis[p]
    return row


def components(v, edges, deleted=0):
    parent = list(range(v))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for j, (a, b) in enumerate(edges):
        if not (deleted >> j) & 1:
            a, b = root(a), root(b)
            if a != b:
                parent[a] = b
    return len({root(j) for j in range(v)})


def deletion_rank_table(v, edges):
    """Compute rank by exhaustive independent subsets, without the rank formula."""
    ranks = [0] * (1 << len(edges))
    independent = [False] * len(ranks)
    for mask in range(len(ranks)):
        independent[mask] = components(v, edges, mask) == 1
        if independent[mask]:
            ranks[mask] = pop(mask)
        elif mask:
            ranks[mask] = max(ranks[mask ^ (1 << j)] for j in bits(mask))
    return ranks, independent


def capacity_ok(mask, colors, d):
    return all(x <= d for x in Counter(colors[j] for j in bits(mask)).values())


def common_independent(m, oracle, colors, d, target=None):
    """Shortest augmenting paths for an oracle matroid and color capacities.

    Sources allow direct insertion in the first matroid; sinks in the second.
    Outside-to-inside arcs use the second exchange, and reverse arcs the first.
    Small instances are also compared with exhaustive subset optima.
    """
    chosen = 0
    full = (1 << m) - 1
    while target is None or pop(chosen) < target:
        inside, outside = list(bits(chosen)), list(bits(full ^ chosen))
        parents = {}
        queue = deque()
        for e in outside:
            if oracle(chosen | (1 << e)):
                parents[e] = None
                queue.append(e)
        end = None
        while queue and end is None:
            e = queue.popleft()
            if not ((chosen >> e) & 1):
                if capacity_ok(chosen | (1 << e), colors, d):
                    end = e
                    break
                for f in inside:
                    if f not in parents and capacity_ok((chosen ^ (1 << f)) | (1 << e), colors, d):
                        parents[f] = e
                        queue.append(f)
            else:
                for f in outside:
                    if f not in parents and oracle((chosen ^ (1 << e)) | (1 << f)):
                        parents[f] = e
                        queue.append(f)
        if end is None:
            break
        e = end
        while e is not None:
            chosen ^= 1 << e
            e = parents[e]
        assert oracle(chosen) and capacity_ok(chosen, colors, d)
    return chosen


def cap_minimum(ranks, color_masks, d):
    n = len(color_masks)
    ans = len(ranks).bit_length()
    for a in range(1 << n):
        union = 0
        for c in bits(a):
            union |= color_masks[c]
        ans = min(ans, ranks[union] + d * (n - pop(a)))
    return ans


def numeric():
    stats = Counter()
    witnesses = {}
    ranges = [(2, range(1, 21)), (3, range(1, 11)), (4, range(1, 7)),
              (5, range(1, 4)), (6, [1]), (7, [1])]
    for n, ds in ranges:
        pairs = list(combinations(range(n), 2))
        for d in ds:
            minimum_B = max(2, d * comb(n - 1, 2))
            minimum_B += minimum_B % 2
            for ws in product(range(d + 1), repeat=len(pairs)):
                stats['weighted_graphs_scanned'] += 1
                total = sum(ws)
                if total <= minimum_B:
                    continue
                degrees = [0] * n
                weighted = []
                for (a, b), w in zip(pairs, ws):
                    degrees[a] += w
                    degrees[b] += w
                    if w:
                        weighted.append((a, b, w))
                for B in range(minimum_B, total, 2):
                    stats['admissible_even_B_instances'] += 1
                    F = total - B
                    assert min(degrees) >= F
                    assert 1 <= F <= d * (n - 1) < d * n
                    assert F + 1 <= d * n
                    assert total + 1 >= F + 1
                    assert F <= d * comb(n, 2) - B <= d * (n - 1)
                    for u in range(1, (1 << n) - 1):
                        vertices = list(bits(u))
                        local = {v: j for j, v in enumerate(vertices)}
                        iu, es = 0, []
                        for a, b, w in weighted:
                            if a in local and b in local:
                                iu += w
                                es.append((local[a], local[b]))
                        h = components(len(vertices), es)
                        rho = total - iu - h + 1
                        lhs = rho + d * len(vertices)
                        assert iu <= B and h <= len(vertices) <= d * len(vertices)
                        assert lhs >= F + 1
                        stats['proper_color_subset_inequalities'] += 1
                        if lhs == F + 1:
                            stats['tight_color_subset_inequalities'] += 1
                    key = 'F1' if F == 1 else 'F2' if F == 2 else 'F_ge_3'
                    stats[key] += 1
                    if F == 1:
                        leaves = [a for a in range(n) if degrees[a] == 1]
                        assert len(leaves) <= 1
                        a = leaves[0] if leaves else 0
                        choices = [[int(j == a) for j in range(n)]]
                        if leaves:
                            stats['F1_degree_one'] += 1
                            assert total - 1 == B == d * comb(n - 1, 2)
                            assert all(degrees[j] >= 2 for j in range(n) if j != a)
                    elif F == 2:
                        T = {a for a in range(n) if degrees[a] == 2}
                        assert len(T) <= 2
                        stats['F2_degree_two_' + str(len(T))] += 1
                        if T:
                            assert total - 2 == B == d * comb(n - 1, 2)
                        choices = []
                        for a, b in pairs:
                            if T <= {a, b}:
                                choices.append([int(j in (a, b)) for j in range(n)])
                        assert choices
                        # A cost-one loop must also decrease every facet strictly.
                        choices.extend([[int(j == a) for j in range(n)] for a in range(n)])
                    else:
                        # Even ignoring -m_a, the worst integer upper bound decreases strictly.
                        assert all(total - deg + F - 1 <= total - 1 for deg in degrees)
                        choices = []
                    for ms in choices:
                        assert max(ms) <= d
                        r = sum(ms)
                        qs = [total - degrees[a] + r - ms[a] for a in range(n)]
                        assert all(0 <= q <= total - 1 for q in qs)
                        stats['small_face_candidate_vectors'] += 1
                    witness_key = key + ('_degree_one' if F == 1 and min(degrees) == 1 else '')
                    if witness_key not in witnesses:
                        witnesses[witness_key] = dict(n=n, d=d, B=B, I=total, F=F,
                                                       weights=list(ws), degrees=degrees)
    for g in range(2, 1001):
        B = 2 * g - 2
        for d in range(1, 1001):
            new = (1 + isqrt((d + 8 * B) // d)) // 2
            old = 0
            while d * comb(old + 2, 2) <= B:
                old += 1
            assert new == old + 1
            assert d * comb(new, 2) <= B < d * comb(new + 1, 2)
            if g >= 3:
                assert new <= B - 1
            elif new > B - 1:
                assert new == 2 and d in (1, 2)
                stats['genus_two_conditional_parameters'] += 1
            stats['rounding_and_Harer_parameters'] += 1
    rng = random.Random(SEED)
    for _ in range(10000):
        B = 2 * rng.randrange(1, 10**60)
        d = rng.randrange(1, 10**62)
        new = (1 + isqrt((d + 8 * B) // d)) // 2
        assert d * comb(new, 2) <= B < d * comb(new + 1, 2)
        stats['large_integer_parameters'] += 1
    return dict(stats=stats, witnesses=witnesses,
                scope='Weighted graphs need not be realizable on the specified surface; this phase checks intersection inequalities and low-face classifications.')


def shortest_cycle(v, edges, allowed=None):
    allowed = list(range(len(edges))) if allowed is None else list(allowed)
    adj = [[] for _ in range(v)]
    for j in allowed:
        a, b = edges[j]
        if a == b:
            return [j]
        adj[a].append((b, j))
        adj[b].append((a, j))
    best = None
    for removed in allowed:
        source, goal = edges[removed]
        queue = deque([source])
        parent = {source: None}
        while queue and goal not in parent:
            a = queue.popleft()
            for b, j in adj[a]:
                if j != removed and b not in parent:
                    parent[b] = (a, j)
                    queue.append(b)
        if goal in parent:
            path = [removed]
            x = goal
            while x != source:
                x, j = parent[x]
                path.append(j)
            if best is None or len(path) < len(best):
                best = path
    return best


def graphs():
    stats = Counter()
    rng = random.Random(SEED + 1)
    for v in range(1, 5):
        types = list(combinations_with_replacement(range(v), 2))
        for m in range(7):
            for js in combinations_with_replacement(range(len(types)), m):
                edges = [types[j] for j in js]
                if components(v, edges) != 1:
                    continue
                stats['connected_multigraphs'] += 1
                ranks, independent = deletion_rank_table(v, edges)
                for mask in range(1 << m):
                    assert ranks[mask] == pop(mask) - components(v, edges, mask) + 1
                    stats['rank_formula_comparisons'] += 1
                schemes = [(1, [0] * m), (4, [j % 3 for j in range(m)]),
                           (4, [rng.randrange(4) for _ in range(m)])]
                for n, colors in schemes:
                    cms = [sum(1 << j for j in range(m) if colors[j] == a) for a in range(n)]
                    for d in (1, 2, 3):
                        brute = max(pop(x) for x in range(1 << m)
                                    if independent[x] and capacity_ok(x, colors, d))
                        assert brute == cap_minimum(ranks, cms, d)
                        stats['capacity_optimum_comparisons'] += 1
                        if m <= 4 or stats['connected_multigraphs'] % 19 == 0:
                            found = common_independent(m, independent.__getitem__, colors, d)
                            assert pop(found) == brute
                            stats['augmenting_algorithm_vs_bruteforce'] += 1
    for F in range(1, 6):
        types = list(combinations_with_replacement(range(F), 2))
        for js in combinations_with_replacement(range(len(types)), F + 1):
            edges = [types[j] for j in js]
            cycle = shortest_cycle(F, edges)
            assert cycle and len(cycle) <= (F if F <= 2 else F - 1)
            stats['girth_exhaustive_graphs'] += 1
    for _ in range(20000):
        F = rng.randrange(6, 31)
        edges = [(rng.randrange(F), rng.randrange(F)) for _ in range(F + 1)]
        cycle = shortest_cycle(F, edges)
        assert cycle and len(cycle) <= F - 1
        stats['girth_seeded_large_graphs'] += 1
    return dict(stats=stats, scope='Loops, parallel edges and isolated vertices are retained; ranks are exhaustive independent-subset maxima.')


def matroids():
    rng = random.Random(SEED + 2)
    stats = Counter()
    for _ in range(10000):
        size = rng.randrange(1, 9)
        dimension = rng.randrange(1, 5)
        vectors = [rng.randrange(1 << dimension) for _ in range(size)]
        rank = [len(gf_basis(vectors[j] for j in bits(mask))) for mask in range(1 << size)]
        t = rng.randrange(1, 7)
        sets = [rng.randrange(1 << size) for _ in range(t)]
        hall = True
        for J in range(1 << t):
            union = 0
            for j in bits(J):
                union |= sets[j]
            hall &= rank[union] >= pop(J)

        def search(slot, chosen):
            if slot == t:
                return True
            for j in bits(sets[slot] & ~chosen):
                new = chosen | (1 << j)
                if rank[new] == slot + 1 and search(slot + 1, new):
                    return True
            return False

        exists = search(0, 0)
        assert exists == hall
        stats['independent_transversal_cases'] += 1
        stats['transversal_exists' if exists else 'transversal_absent'] += 1
        n = rng.randrange(1, 5)
        colors = [rng.randrange(n) for _ in range(size)]
        cms = [sum(1 << j for j in range(size) if colors[j] == a) for a in range(n)]
        for d in (1, 2, 3):
            brute = max(pop(x) for x in range(1 << size)
                        if rank[x] == pop(x) and capacity_ok(x, colors, d))
            assert brute == cap_minimum(rank, cms, d)
            found = common_independent(size, lambda x: rank[x] == pop(x), colors, d)
            assert pop(found) == brute
            stats['binary_matroid_capacity_comparisons'] += 1
    return dict(stats=stats, scope='Finite seeded binary-matroid tests do not replace the general inductive proof.')


def cycles_of_permutation(perm):
    seen, cycles = set(), []
    for a in range(len(perm)):
        if a in seen:
            continue
        cyc, x = [], a
        while x not in seen:
            seen.add(x)
            cyc.append(x)
            x = perm[x]
        assert x == a
        cycles.append(cyc)
    return cycles


def ribbon_model(n, weights, rng):
    """Each input pair has crossings of one sign, so absolute algebraic and actual counts agree.

    Four darts meet at each crossing; opposite darts of one color form a curve.
    Capping every ribbon boundary gives an actual closed orientable surface.
    """
    vertices, crossing_signs, orders = [], {}, [[] for _ in range(n)]
    for (a, b), w in zip(combinations(range(n), 2), weights):
        sign = rng.choice((-1, 1))
        crossing_signs[(a, b)] = sign
        for _ in range(w):
            j = len(vertices)
            vertices.append((a, b, sign))
            orders[a].append(j)
            orders[b].append(j)
    if any(not order for order in orders):
        return None
    for order in orders:
        rng.shuffle(order)
    dart_info, dart_id = [], {}
    for v, (a, b, sign) in enumerate(vertices):
        for color in (a, b):
            for direction in (1, -1):
                dart_id[v, color, direction] = len(dart_info)
                dart_info.append((v, color, direction))
    alpha = [-1] * len(dart_info)
    sigma = [-1] * len(dart_info)
    for color, order in enumerate(orders):
        for j, v in enumerate(order):
            w = order[(j + 1) % len(order)]
            p, q = dart_id[v, color, 1], dart_id[w, color, -1]
            alpha[p], alpha[q] = q, p
    for v, (a, b, sign) in enumerate(vertices):
        cyclic = [dart_id[v, a, 1], dart_id[v, b, sign],
                  dart_id[v, a, -1], dart_id[v, b, -sign]]
        for p, q in zip(cyclic, cyclic[1:] + cyclic[:1]):
            sigma[p] = q
    assert sorted(alpha) == list(range(len(alpha)))
    assert all(alpha[alpha[j]] == j and alpha[j] != j for j in range(len(alpha)))
    faces = cycles_of_permutation([sigma[alpha[j]] for j in range(len(alpha))])
    face_of = {}
    for j, face in enumerate(faces):
        for dart in face:
            face_of[dart] = j
    edge_darts, edges, dual, colors = [], [], [], []
    edge_of = {}
    for p, q in enumerate(alpha):
        if p < q:
            edge_of[p] = edge_of[q] = len(edges)
            edge_darts.append((p, q))
            edges.append((dart_info[p][0], dart_info[q][0]))
            dual.append((face_of[p], face_of[q]))
            assert dart_info[p][1] == dart_info[q][1]
            colors.append(dart_info[p][1])
    if components(len(vertices), edges) != 1:
        return None
    I, F = len(vertices), len(faces)
    assert (I - F) % 2 == 0
    g = (2 + I - F) // 2
    signed = [[0] * n for _ in range(n)]
    for a, b, s in vertices:
        signed[a][b] += s
        signed[b][a] -= s
    # Nonzero pairings certify essentiality; distinct rows up to sign distinguish unoriented classes.
    if any(not any(row) for row in signed):
        return None
    for a, b in combinations(range(n), 2):
        if signed[a] == signed[b] or signed[a] == [-x for x in signed[b]]:
            return None
    cuts = []
    for v in range(I):
        mask = 0
        for j, (a, b) in enumerate(edges):
            if (a == v) != (b == v):
                mask ^= 1 << j
        cuts.append(mask)
    # Independently generate dual two-cell boundaries from vertex rotations.
    dual_two_boundaries = [0] * I
    for rotation in cycles_of_permutation(sigma):
        mask = 0
        for dart in rotation:
            mask ^= 1 << edge_of[dart]
        dual_two_boundaries[dart_info[rotation[0]][0]] = mask
    assert dual_two_boundaries == cuts
    for mask in dual_two_boundaries:
        boundary = 0
        for e in bits(mask):
            a, b = dual[e]
            boundary ^= (1 << a) ^ (1 << b)
        assert boundary == 0
    face_boundaries = []
    for face in faces:
        mask = 0
        for dart in face:
            mask ^= 1 << edge_of[dart]
        face_boundaries.append(mask)
    assert len(gf_basis(cuts)) == I - 1
    assert len(gf_basis(face_boundaries)) == F - 1
    assert len(edges) - F + 1 - len(gf_basis(cuts)) == 2 * g
    assert len(edges) - I + 1 - len(gf_basis(face_boundaries)) == 2 * g
    return dict(n=n, weights=list(weights), vertices=vertices, orders=orders,
                alpha=alpha, sigma=sigma, faces=faces, edge_darts=edge_darts,
                edges=edges, dual=dual, colors=colors, signed=signed,
                I=I, F=F, g=g, cuts=cuts)


def enumerate_short_simple_cycles(v, edges, allowed, max_length):
    """Enumerate short simple cycles separately from shortest-cycle search."""
    adj = [[] for _ in range(v)]
    seen = set()
    for j in allowed:
        a, b = edges[j]
        adj[a].append((b, j))
        if a != b:
            adj[b].append((a, j))
    for start in range(v):
        stack = [(start, [start], [])]
        while stack:
            at, visited, path = stack.pop()
            for nxt, e in adj[at]:
                if e in path:
                    continue
                new = path + [e]
                if nxt == start:
                    key = tuple(sorted(new))
                    if key not in seen:
                        seen.add(key)
                        yield new
                elif len(new) < max_length and nxt >= start and nxt not in visited:
                    stack.append((nxt, visited + [nxt], new))


def verify_dual_cycle(model, cycle, d, stats):
    n, I, F = model['n'], model['I'], model['F']
    ms = [0] * n
    dual_boundary = 0
    mask = 0
    for j in cycle:
        mask ^= 1 << j
        a, b = model['dual'][j]
        dual_boundary ^= (1 << a) ^ (1 << b)
        ms[model['colors'][j]] += 1
    assert mask and not dual_boundary
    assert max(ms) <= d
    # Eliminate against the dual two-boundary matrix, independently of deletion connectivity.
    reduced = gf_reduce(mask, gf_basis(model['cuts']))
    assert reduced != 0
    # Orient the simple cycle and compute its signed input crossings, up to overall sign.
    signed_crossings = [0] * n
    at = model['dual'][cycle[0]][0]
    start = at
    remaining = set(cycle)
    while remaining:
        e = next(e for e in remaining if at in model['dual'][e])
        a, b = model['dual'][e]
        orientation = 1 if at == a else -1
        dart = model['edge_darts'][e][0]
        input_orientation = 1 if dart % 2 == 0 else -1
        signed_crossings[model['colors'][e]] += orientation * input_orientation
        at = b if at == a else a
        remaining.remove(e)
    assert at == start
    assert all((a - b) % 2 == 0 for a, b in zip(signed_crossings, ms))
    degrees = [sum(abs(x) for x in row) for row in model['signed']]
    Q = [I - degrees[a] + len(cycle) - ms[a] for a in range(n)]
    assert all(q < I for q in Q)
    # Equality with an input class would force its row sum to equal the geometric crossings with the others.
    assert all(sum(abs(model['signed'][a][b]) for b in range(n) if b != a)
               > sum(ms[b] for b in range(n) if b != a) for a in range(n))
    stats['embedded_cycle_patterns_checked'] += 1
    if max(ms) > 1:
        stats['repeated_color_cycles'] += 1
        if all(m % 2 == 0 for m in ms):
            stats['all_input_color_parities_even'] += 1
        if not any(signed_crossings):
            stats['all_signed_input_intersections_zero'] += 1
    return dict(cycle_edges=cycle, multiplicities=ms, signed_input_intersections=signed_crossings,
                Q=Q, homology_remainder=hex(reduced))


def surfaces():
    stats = Counter()
    rng = random.Random(SEED + 3)
    witnesses = {}
    tests = []
    for n in range(2, 7):
        for d in range(1, 6):
            for _ in range(60):
                # Include dense and sparse systems, with one crossing sign per input pair.
                ws = [rng.randrange(d + 1) if rng.random() < .4 else d
                      for _ in combinations(range(n), 2)]
                tests.append((n, d, ws))
    for d in range(6, 41):
        for _ in range(30):
            tests.append((2, d, [d]))
    for n, d, ws in tests:
        stats['rotation_system_attempts'] += 1
        model = ribbon_model(n, ws, rng)
        if model is None:
            continue
        I, F, g = model['I'], model['F'], model['g']
        B = 2 * g - 2
        if g < 2 or d * comb(n - 1, 2) > B:
            continue
        assert I > B and I - B == F
        stats['certified_admissible_surfaces'] += 1
        if d >= 2:
            stats['d_ge_2_surfaces'] += 1
        if F >= n:
            stats['faces_at_least_number_of_colors'] += 1
        if n == 2:
            stats['two_curve_surfaces'] += 1
        for a in range(n):
            assert sum(abs(x) for x in model['signed'][a]) >= F
        # Compare equation (11) for all proper color subsets with actual deletion components.
        for A in range(1, (1 << n) - 1):
            U = [a for a in range(n) if not ((A >> a) & 1)]
            ea = sum(1 << j for j, c in enumerate(model['colors']) if (A >> c) & 1)
            iu = sum(abs(model['signed'][a][b]) for a, b in combinations(U, 2))
            local = {a: j for j, a in enumerate(U)}
            es = [(local[a], local[b]) for a, b in combinations(U, 2) if model['signed'][a][b]]
            hu = components(len(U), es)
            observed_rank = pop(ea) - components(I, model['edges'], ea) + 1
            assert observed_rank == I - iu - hu + 1
            assert observed_rank + d * len(U) >= F + 1
            stats['surface_rank_formula_checks'] += 1
        X = common_independent(len(model['edges']),
                               lambda x: components(I, model['edges'], x) == 1,
                               model['colors'], d, target=F + 1)
        assert pop(X) >= F + 1 and capacity_ok(X, model['colors'], d)
        assert components(I, model['edges'], X) == 1
        stats['selected_connected_deletions'] += 1
        # Check every nonzero mod-two cycle of the selected subgraph against Proposition 4.2.
        selected = list(bits(X))
        for subset in range(1, 1 << len(selected)):
            chain, boundary = 0, 0
            for t in bits(subset):
                e = selected[t]
                chain ^= 1 << e
                a, b = model['dual'][e]
                boundary ^= (1 << a) ^ (1 << b)
            if boundary == 0:
                assert gf_reduce(chain, gf_basis(model['cuts'])) != 0
                stats['all_selected_nonzero_cycles_checked'] += 1
        degrees = [sum(abs(x) for x in row) for row in model['signed']]
        if F >= 3:
            cycle = shortest_cycle(F, model['dual'], bits(X))
            assert cycle and len(cycle) <= F - 1
        elif F == 1:
            leaves = [a for a, degree in enumerate(degrees) if degree == 1]
            assert len(leaves) <= 1
            c = leaves[0] if leaves else 0
            cycle = [next(j for j, color in enumerate(model['colors']) if color == c)]
        else:
            loops = [j for j, (a, b) in enumerate(model['dual']) if a == b]
            if loops:
                cycle = [loops[0]]
            else:
                T = [a for a, degree in enumerate(degrees) if degree == 2]
                assert len(T) <= 2
                colors = T + [a for a in range(n) if a not in T]
                cycle = [next(j for j, c in enumerate(model['colors']) if c == a) for a in colors[:2]]
                stats['F2_no_loop_two_color_cases'] += 1
        result = verify_dual_cycle(model, cycle, d, stats)
        stats['F_' + str(F)] += 1
        if F >= 3:
            # Exclude loops and seek repeated colors, including cycles of even input parity.
            candidates = [j for j in bits(X) if model['dual'][j][0] != model['dual'][j][1]]
            for extra in enumerate_short_simple_cycles(F, model['dual'], candidates, min(F - 1, 6)):
                counts = Counter(model['colors'][j] for j in extra)
                if max(counts.values()) <= 1:
                    continue
                extra_result = verify_dual_cycle(model, extra, d, stats)
                key = 'all_even_repeated' if all(x % 2 == 0 for x in extra_result['multiplicities']) else 'repeated'
                if key not in witnesses:
                    witnesses[key] = dict(model=model, d=d, X_edges=list(bits(X)), result=extra_result)
                if not any(extra_result['signed_input_intersections']) and 'signed_zero_repeated' not in witnesses:
                    witnesses['signed_zero_repeated'] = dict(model=model, d=d, X_edges=list(bits(X)), result=extra_result)
                break
        key = ('F1_degree_one' if F == 1 and min(degrees) == 1 else
               'F2_no_loop' if F == 2 and not any(a == b for a, b in model['dual']) else
               'shortest_repeated' if max(result['multiplicities']) >= 2 else None)
        if key and key not in witnesses:
            witnesses[key] = dict(model=model, d=d, X_edges=list(bits(X)), result=result)
    assert stats['d_ge_2_surfaces'] > 0
    assert stats['repeated_color_cycles'] > 0
    assert stats['all_input_color_parities_even'] > 0
    return dict(stats=stats, witnesses=witnesses,
                scope='Actual closed orientable surfaces; same-sign pairings certify input minimality. New-curve crossing counts are upper bounds only.')


def main():
    if not __debug__:
        raise SystemExit("Run without -O; these checks rely on assertions.")
    parser = argparse.ArgumentParser()
    parser.add_argument('--phase', choices=['numeric', 'graphs', 'matroids', 'surfaces', 'all'], default='all')
    args = parser.parse_args()
    phases = ['numeric', 'graphs', 'matroids', 'surfaces'] if args.phase == 'all' else [args.phase]
    report = {'seed': SEED, 'all_passed': True}
    for phase in phases:
        report[phase] = globals()[phase]()
    print(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
