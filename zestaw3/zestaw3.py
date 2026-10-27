# ==========================================
# Zadanie 3.1
# ==========================================
# Czy podany kod jest poprawny składniowo w Pythonie?
# Jeśli nie, to dlaczego?

print("=== Task 3.1 ===")

# === Fragment 1 ===
# x = 2; y = 3;
# if (x > y):
#     result = x;
# else:
#     result = y;
#
# ODPOWIEDŹ: Kod jest poprawny składniowo.

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

assert result == 3
print("Fragment 1: poprawny składniowo (średniki i nawiasy są dozwolone)")

# === Fragment 2 ===
# for i in "axby": if ord(i) < 100: print(i)
#
# ODPOWIEDŹ: Kod jest niepoprawny składniowo.
# Po dwukropku w pętli for nie może wystąpić instrukcja if w tej samej linii

print("Fragment 2: niepoprawny składniowo (nie można zagnieżdżać instrukcji złożonych w jednej linii)")

# === Fragment 3 ===
# for i in "axby": print(ord(i) if ord(i) < 100 else i)
#
# ODPOWIEDŹ: Kod jest poprawny składniowo.

result_3 = []
for i in "axby": result_3.append(ord(i) if ord(i) < 100 else i)

assert result_3 == [97, "x", 98, "y"]
print("Fragment 3: poprawny składniowo")

# ==========================================
# Zadanie 3.2
# ==========================================
# Co jest złego w kodzie:

print("=== Task 3.2 ===")

# === Fragment 1 ===
# L = [3, 5, 4] ; L = L.sort()
#
# ODPOWIEDŹ: Metoda list.sort() sortuje listę in place i zwraca None.

L = [3, 5, 4]
L_wrong = L.sort()
assert L_wrong is None
assert L == [3, 4, 5]

L = sorted([3, 5, 4])
assert L == [3, 4, 5]
print("Fragment 1: L.sort() zwraca None, więc L = L.sort() przypisuje None do L")

# === Fragment 2 ===
# x, y = 1, 2, 3
#
# ODPOWIEDŹ: ValueError - za dużo wartości do rozpakowania.
# Po lewej stronie są 2 zmienne, a po prawej 3 wartości.

print("Fragment 2: ValueError - za dużo wartości do rozpakowania (2 zmienne, 3 wartości)")

# === Fragment 3 ===
# X = 1, 2, 3 ; X[1] = 4
#
# ODPOWIEDŹ: TypeError - tuple są niemodyfikowalne.
# X = 1, 2, 3 tworzy tuple (1, 2, 3), a tuple nie obsługują przypisywania elementów.

X = 1, 2, 3
assert isinstance(X, tuple)

print("Fragment 3: TypeError - tuple są niemodyfikowalne (X = 1, 2, 3 tworzy tuple)")

# === Fragment 4 ===
# X = [1, 2, 3] ; X[3] = 4
#
# ODPOWIEDŹ: IndexError - indeks poza zakresem.
# Indeks 3 nie istnieje.

X = [1, 2, 3]

print("Fragment 4: IndexError - indeks 3 poza zakresem listy")

# === Fragment 5 ===
# X = "abc" ; X.append("d")
#
# ODPOWIEDŹ: AttributeError - stringi nie mają metody append()

X = "abc"
print("Fragment 5: AttributeError - stringi nie mają metody append()")

# === Fragment 6 ===
# L = list(map(pow, range(8)))
#
# ODPOWIEDŹ: TypeError - funkcja pow() wymaga co najmniej 2 argumentów,
# a map() przekazuje tylko jeden argument z range(8).

print("Fragment 6: TypeError - pow() wymaga 2 argumentów, map() przekazuje tylko 1")

# ==========================================
# Zadanie 3.3
# ==========================================
# Wypisać w pętli liczby od 0 do 30 włącznie, z wyjątkiem liczb
# podzielnych przez 3.
# Podać dwa rozwiązania: jedno z pętlą for, drugie z pętlą while.

print("=== Task 3.3 ===")

print("For loop")
result_for = []
for i in range(31):
    if i % 3 != 0:
        print(f"{i}, ")
        result_for.append(i)

print("\nWhile loop")
result_while = []
i = 0
while i <= 30:
    if i % 3 != 0:
        print(f"{i}, ")
        result_while.append(i)
    i += 1

print(f"While loop result: {result_while}")

expected = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]
assert result_for == expected
assert result_while == expected
assert 0 not in result_for
assert 3 not in result_for
assert 30 not in result_for
assert 1 in result_for
assert 29 in result_for

print("Tests for task 3.3 passed!\n")

# ==========================================
# Zadanie 3.8
# ==========================================
# Dla dwóch sekwencji liczb lub znaków znaleźć:
# (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
# (b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

print("=== Task 3.8 ===")

seq1 = [1, 2, 3, 4, 5, 3, 2]
seq2 = [4, 5, 6, 7, 8, 5, 6]

common = list(set(seq1) & set(seq2))
common.sort()

all_elements = list(set(seq1) | set(seq2))
all_elements.sort()

print(f"Sequence 1: {seq1}")
print(f"Sequence 2: {seq2}")
print(f"Common elements: {common}")
print(f"All elements (union): {all_elements}")

assert set(common) == {4, 5}
assert set(all_elements) == {1, 2, 3, 4, 5, 6, 7, 8}

s1 = "abcde"
s2 = "defgh"
common_str = sorted(set(s1) & set(s2))
all_str = sorted(set(s1) | set(s2))
assert common_str == ['d', 'e']
assert all_str == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

assert list(set([]) & set([1, 2])) == []
assert sorted(set([]) | set([1, 2])) == [1, 2]

print("Tests for task 3.8 passed!\n")

# ==========================================
# Zadanie 3.9
# ==========================================
# Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
# Znaleźć listę zawierającą sumy liczb z tych sekwencji.
# Przykładowa sekwencja [[], [4], (1,2), [3,4], (5,6,7)],
# spodziewany wynik [0, 4, 3, 7, 18].

print("=== Task 3.9 ===")

sequences = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

result = [sum(seq) for seq in sequences]

print(f"Sequences: {sequences}")
print(f"Sums: {result}")

expected = [0, 4, 3, 7, 18]
assert result == expected

assert [sum(s) for s in []] == []
assert [sum(s) for s in [[1, 2, 3]]] == [6]
assert [sum(s) for s in [[], []]] == [0, 0]
assert [sum(s) for s in [(10,), [20], (30,)]] == [10, 20, 30]

print("Tests for task 3.9 passed!\n")
