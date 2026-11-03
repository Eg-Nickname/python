# ==========================================
# Zadanie 4.5
# ==========================================
# Napisać funkcję odwracanie(L, left, right) odwracającą
# kolejność elementów na liście od numeru left do right włącznie.
# Lista jest modyfikowana w miejscu (in place).
# Rozważyć wersję iteracyjną i rekurencyjną.

print("=== Task 4.5 ===")

def reverse_iterative(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

def reverse_recursive(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        reverse_recursive(L, left + 1, right - 1)


L1 = [1, 2, 3, 4, 5]
reverse_iterative(L1, 0, 4)
print(f"Iteracyjne [1,2,3,4,5] reverse(0,4) = {L1}")
assert L1 == [5, 4, 3, 2, 1]

L2 = [1, 2, 3, 4, 5]
reverse_iterative(L2, 1, 3)
print(f"Iteracyjne [1,2,3,4,5] reverse(1,3) = {L2}")
assert L2 == [1, 4, 3, 2, 5]

L3 = [1, 2, 3]
reverse_iterative(L3, 0, 0)
assert L3 == [1, 2, 3]

L4 = [1]
reverse_iterative(L4, 0, 0)
assert L4 == [1]

L5 = [1, 2, 3, 4, 5]
reverse_recursive(L5, 0, 4)
print(f"Recursive [1,2,3,4,5] reverse(0,4) = {L5}")
assert L5 == [5, 4, 3, 2, 1]

L6 = [1, 2, 3, 4, 5]
reverse_recursive(L6, 1, 3)
print(f"Recursive [1,2,3,4,5] reverse(1,3) = {L6}")
assert L6 == [1, 4, 3, 2, 5]

L7 = [1, 2, 3]
reverse_recursive(L7, 0, 0)
assert L7 == [1, 2, 3]

L8 = [10, 20, 30, 40, 50, 60]
reverse_recursive(L8, 2, 5)
assert L8 == [10, 20, 60, 50, 40, 30]

print("Tests for task 4.5 passed!\n")

