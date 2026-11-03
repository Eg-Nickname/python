# ==========================================
# Zadanie 4.3
# ==========================================
# Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.

print("=== Task 4.3 ===")


def factorial(n):
    if n < 0:
        raise ValueError("n must be positive")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(f"factorial(0) = {factorial(0)}")
print(f"factorial(1) = {factorial(1)}")
print(f"factorial(5) = {factorial(5)}")
print(f"factorial(10) = {factorial(10)}")

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(10) == 3628800

try:
    factorial(-1)
    assert False, "Should have raised ValueError"
except ValueError:
    pass

print("\nTests for task 4.3 passed!\n")

