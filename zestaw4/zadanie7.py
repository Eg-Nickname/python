# ==========================================
# Zadanie 4.7
# ==========================================
# Mamy daną sekwencję, w której niektóre z elementów mogą
# okazać się podsekwencjami, a takie zagnieżdżenia mogą się
# nakładać do nieograniczonej głębokości.
# Napisać funkcję flatten(sequence), która zwróci
# spłaszczoną listę wszystkich elementów sekwencji.
# Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element
# jest sekwencją, wykonać przez isinstance(item, (list, tuple)).

print("=== Task 4.7 ===")

def flatten(sequence):
    flattened = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flattened = flattened + flatten(item)
        else:
            flattened.append(item)
    return flattened


sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(f"flatten({sequence}) = {flatten(sequence)}")

assert flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([]) == []
assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([[1, [2, [3, [4]]]]]) == [1, 2, 3, 4]
assert flatten([(), [], ()]) == []
assert flatten([(1,), [2], (3,)]) == [1, 2, 3]
assert flatten([[[[[5]]]]]) == [5]
assert flatten([1, [2, 3], [4, [5, [6, [7, [8, [9]]]]]]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Tests for task 4.7 passed!\n")
