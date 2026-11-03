# ==========================================
# Zadanie 4.6
# ==========================================
# Napisać funkcję sum_seq(sequence) obliczającą sumę liczb
# zawartych w sekwencji, która może zawierać zagnieżdżone podsekwencje.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element
# jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

print("=== Task 4.6 ===")


def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
    return result


print(f"sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) = {sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]])}")

assert sum_seq([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == 45
assert sum_seq([]) == 0
assert sum_seq([1, 2, 3]) == 6
assert sum_seq([[1, [2, [3]]]]) == 6
assert sum_seq([(1,), (2,), (3,)]) == 6
assert sum_seq([0]) == 0
assert sum_seq([[[[5]]]]) == 5
assert sum_seq([1, [2, [3, [4, [5]]]]]) == 15

print("Tests for task 4.6 passed!\n")

