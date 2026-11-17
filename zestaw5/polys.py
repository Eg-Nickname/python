# Helper function removing redundant zero parameters
def normalize_poly(poly):
    i = len(poly)
    while i > 1 and poly[i - 1] == 0:
        i -= 1
    return poly[:i]

def add_poly(poly1, poly2):
    res = [0] * max(len(poly1), len(poly2))
    for i, a in enumerate(poly1):
        res[i] += a

    for i, a in enumerate(poly2):
        res[i] += a
    return normalize_poly(res)

def sub_poly(poly1, poly2):
    res = [0] * max(len(poly1), len(poly2))
    for i, a in enumerate(poly1):
        res[i] += a

    for i, a in enumerate(poly2):
        res[i] -= a
    return normalize_poly(res)

def mul_poly(poly1, poly2):
    if is_zero(poly1) or is_zero(poly2):
        return [0]

    res = [0] * (len(poly1) + len(poly2) - 1)
    for i, c1 in enumerate(poly1):
        for j, c2 in enumerate(poly2):
            res[i + j] += c1 * c2
    return normalize_poly(res)

def is_zero(poly):
    return all(c == 0 for c in poly)

def eq_poly(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    for i in range(max_len):
        c1 = poly1[i] if i < len(poly1) else 0
        c2 = poly2[i] if i < len(poly2) else 0
        if c1 != c2:
            return False
    return True

def eval_poly(poly, x0):
    result = 0
    for c in reversed(poly):
        result = result * x0 + c
    return result

def combine_poly(poly1, poly2):
    res = [0]
    for c in reversed(poly1):
        res = add_poly([c], mul_poly(res, poly2))
    return res

def pow_poly(poly, n):
    if n < 0:
        raise ValueError("N must be positive!")
    if n == 0:
        return [1]
    
    res = [1]
    base = list(poly)
    while n > 0:
        if n % 2 == 1:
            res = mul_poly(res, base)
        if n > 1:
            base = mul_poly(base, base)
        n //= 2
    return res

def diff_poly(poly):
    if len(poly) <= 1:
        return [0]
    res = [i * poly[i] for i in range(1, len(poly))]
    return normalize_poly(res)