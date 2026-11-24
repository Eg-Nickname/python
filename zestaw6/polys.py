class Poly:
    """Klasa reprezentująca wielomiany."""
    def __init__(self, c=0, n=0):
        self.size = n + 1
        self.a = self.size * [0]
        self.a[self.size - 1] = c

    def __str__(self):
        return str(self.a)

    def normalize(a):
        i = len(a)
        while i > 1 and a[i - 1] == 0:
            i -= 1
        return a[:i]

    def from_list(a):
        p = Poly()
        p.a = Poly.normalize(list(a))
        p.size = len(p.a)
        return p

    def __add__(self, other):
        res = [0] * max(self.size, other.size)
        for i, a in enumerate(self.a):
            res[i] += a
        for i, a in enumerate(other.a):
            res[i] += a
        return Poly.from_list(res)

    def __sub__(self, other):
        res = [0] * max(self.size, other.size)
        for i, a in enumerate(self.a):
            res[i] += a
        for i, a in enumerate(other.a):
            res[i] -= a
        return Poly.from_list(res)

    def __mul__(self, other):
        if self.is_zero() or other.is_zero():
            return Poly() 
        res = [0] * (self.size + other.size - 1)
        for i, a1 in enumerate(self.a):
            for j, a2 in enumerate(other.a):
                res[i + j] += a1 * a2
        return Poly.from_list(res)

    def __pos__(self):
        return Poly.from_list(self.a)

    def __neg__(self):
        return Poly.from_list([-c for c in self.a])

    def __eq__(self, other):
        max_len = max(len(self.a), len(other.a))
        for i in range(max_len):
            c1 = self.a[i] if i < len(self.a) else 0
            c2 = other.a[i] if i < len(other.a) else 0
            if c1 != c2:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def eval(self, x):
        result = 0
        for c in reversed(self.a):
            result = result * x + c
        return result

    def combine(self, other):
        res = Poly.from_list([0])
        for c in reversed(self.a):
            const = Poly(c, 0)
            res = const + res * other
        return res

    def __pow__(self, n):
        if n < 0:
            raise ValueError("N must be positive!")
        if n == 0:
            return Poly(1, 0)
        res = Poly(1, 0)
        base = Poly.from_list(self.a)
        while n > 0:
            if n % 2 == 1:
                res = res * base
            if n > 1:
                base = base * base
            n //= 2
        return res

    def diff(self):
        if self.size <= 1:
            return Poly(0, 0)
        res = [i * self.a[i] for i in range(1, self.size)]
        return Poly.from_list(res)

    def integrate(self):
        res = [0] + [self.a[i] / (i + 1) for i in range(self.size)]
        return Poly.from_list(res)

    def is_zero(self):
        return all(a == 0 for a in self.a)