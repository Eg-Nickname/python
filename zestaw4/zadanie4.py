# ==========================================
# Zadanie 4.4
# ==========================================
# Napisać iteracyjną wersję funkcji fibonacci(n)
# obliczającej n-ty wyraz ciągu Fibonacciego.

print("=== Task 4.4 ===")


def fibonacci(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        tmp = a
        a = b
        b = b + tmp
    return b


print(f"fibonacci(0) = {fibonacci(0)}")
print(f"fibonacci(1) = {fibonacci(1)}")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(10) = {fibonacci(10)}")

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(10) == 55
assert fibonacci(20) == 6765

try:
    fibonacci(-1)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

print("Tests for task 4.4 passed!\n")

