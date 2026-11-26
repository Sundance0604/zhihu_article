"""Exact checks for the explicit simplicial examples used in this commentary.

Standard library only. Run from any directory. Generates verification-results.json.
Computes boundary matrices from oriented face lists, not expected homology tables.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path
import json


def boundary(triangle):
    result = {}
    for i in range(3):
        edge = triangle[:i] + triangle[i + 1:]
        sign = (-1) ** i
        if edge[0] > edge[1]:
            edge = edge[::-1]
            sign = -sign
        result[edge] = result.get(edge, 0) + sign
    return result


def rank(matrix):
    if not matrix or not matrix[0]:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    n, m = len(a), len(a[0])
    r = 0
    for c in range(m):
        pivot = next((i for i in range(r, n) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        value = a[r][c]
        a[r] = [x / value for x in a[r]]
        for i in range(r + 1, n):
            factor = a[i][c]
            if factor:
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def determinant(matrix):
    if not matrix:
        return 1
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    det = Fraction(1)
    for c in range(n):
        pivot = next((i for i in range(c, n) if a[i][c]), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            det *= -1
        value = a[c][c]
        det *= value
        for i in range(c + 1, n):
            factor = a[i][c] / value
            for j in range(c + 1, n):
                a[i][j] -= factor * a[c][j]
            a[i][c] = 0
    assert det.denominator == 1
    return int(det)


def analyze(name, faces, extra_edges=(), extra_vertices=(), expected=(1, 0, 0, 1), tree=None):
    edges = sorted(set(extra_edges) | {tuple(sorted(e)) for f in faces for e in combinations(f, 2)})
    vertices = sorted(set(extra_vertices) | {v for e in edges for v in e})
    d1 = [[(-1 if v == e[0] else 1 if v == e[1] else 0) for e in edges] for v in vertices]
    columns = [boundary(f) for f in faces]
    d2 = [[column.get(e, 0) for column in columns] for e in edges]
    for row in d1:
        for j in range(len(faces)):
            assert sum(row[k] * d2[k][j] for k in range(len(edges))) == 0, name
    parent = {v: v for v in vertices}

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    spanning = []
    for e in (tree if tree is not None else edges):
        assert e in edges
        a, b = root(e[0]), root(e[1])
        if a != b:
            parent[a] = b
            spanning.append(e)
    components = len({root(v) for v in vertices})
    assert len(spanning) == len(vertices) - components
    if tree is not None:
        assert len(tree) == len(spanning)
        assert components == 1
    non_tree = [e for e in edges if e not in spanning]
    relation = [d2[edges.index(e)] for e in non_tree]
    r1, r2 = rank(d1), rank(d2)
    assert rank(relation) == r2
    torsion_order = 1
    if r2:
        torsion_order = 0
        for rr in combinations(range(len(relation)), r2):
            for cc in combinations(range(len(faces)), r2):
                minor = [[relation[i][j] for j in cc] for i in rr]
                torsion_order = gcd(torsion_order, abs(determinant(minor)))
                if torsion_order == 1:
                    break
            if torsion_order == 1:
                break
    actual = (components, len(edges) - r1 - r2, len(faces) - r2, torsion_order)
    assert actual == expected, (name, actual, expected)
    chi_cells = len(vertices) - len(edges) + len(faces)
    chi_betti = actual[0] - actual[1] + actual[2]
    assert chi_cells == chi_betti
    return {'name': name, 'simplex_counts': [len(vertices), len(edges), len(faces)],
            'boundary_ranks_over_Q': [r1, r2], 'betti_numbers': list(actual[:3]),
            'H1_torsion_subgroup_order': torsion_order, 'euler_characteristic': chi_cells,
            'tree_edges': spanning, 'non_tree_edges': non_tree,
            'D1': d1, 'D2': d2, 'cycle_relation_matrix': relation,
            'D1_times_D2_zero': True}


def main():
    examples = [
        analyze('point', [], extra_vertices=(0,)),
        analyze('two_points', [], extra_vertices=(0, 1), expected=(2, 0, 0, 1)),
        analyze('interval', [], extra_edges=((0, 1),)),
        analyze('triangle_boundary', [], extra_edges=((0, 1), (0, 2), (1, 2)), expected=(1, 1, 0, 1)),
        analyze('filled_triangle', [(0, 1, 2)]),
        analyze('tetrahedron_surface', list(combinations(range(4), 3)), expected=(1, 0, 1, 1)),
        analyze('mobius_original_faces', [(0, 1, 2), (2, 1, 4), (2, 4, 3), (3, 4, 5), (3, 5, 1), (1, 5, 0)],
                expected=(1, 1, 0, 1), tree=[(0, 1), (0, 2), (0, 5), (1, 3), (1, 4)]),
        analyze('RP2_original_faces', [(0, 1, 2), (0, 4, 1), (0, 5, 4), (0, 3, 5), (0, 2, 3),
                (2, 4, 3), (2, 5, 4), (2, 1, 5), (1, 3, 5), (1, 4, 3)],
                expected=(1, 0, 0, 2), tree=[(0, i) for i in range(1, 6)]),
    ]
    out = Path(__file__).with_name('verification-results.json')
    out.write_text(json.dumps({'method': 'Exact rational rank and integer determinantal divisors; no floating point.',
                               'examples': examples}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    for ex in examples:
        print(ex['name'], 'b=', ex['betti_numbers'], '|torsion H1|=', ex['H1_torsion_subgroup_order'],
              'chi=', ex['euler_characteristic'])
    print('Verified 8 examples: boundary composition, Betti ranks, integer torsion orders and Euler sums.')


if __name__ == '__main__':
    main()
