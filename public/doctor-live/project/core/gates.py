from itertools import combinations

def verify_gates_integrity():
    gates = list(combinations(range(22), 2))
    blocks = (
        len(list(combinations(range(3), 2)))
        + len(list(combinations(range(7), 2)))
        + len(list(combinations(range(12), 2)))
        + 3 * 7 + 3 * 12 + 7 * 12
    )
    ok = len(gates) == 231 and blocks == 231 and 3 * 7 * 11 == 231
    return {
        "C22_2": len(gates) == 231,
        "orientations_462": len(gates) * 2 == 462,
        "produit_offsets_3_7_11": 3 * 7 * 11 == 231,
        "blocs_somme_231": blocks == 231,
        "global": ok,
    }

def coverage_from_ring_offsets():
    return {
        "portes_couvertes_23_par_cycle": 23 * 3,
        "C22_2": 231,
        "C23_2": 253,
        "couverture_69_est_definition": True,
    }
