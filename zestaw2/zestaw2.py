# ==========================================
# Zadanie 2.10
# ==========================================
# Mamy dany string wielowierszowy line. Podać sposób obliczenia liczby wyrazów w stringu.
# Przez wyraz rozumiemy ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline). 

print("=== Task 2.10 ===")
line = "\tWlaz \t \t kotek na \t plotek i mruga ladna     to piosenka       nie dluga. \nnie dluga nie krotka lecz w sam \n raz zaspiewaj koteczku jeszcze raz."

words = line.split()
word_count = len(words)

print(f"Text:\n{line}")
print(f"Word list ({word_count}): {words}")
print(f"Word count: {word_count}")

assert word_count == 23
assert len("".split()) == 0
assert len("  slowo  \n\t".split()) == 1
assert len("  dwa  \n\t  slowo  ".split()) == 2

print("Tests for task 2.10 passed!\n")


# ==========================================
# Zadanie 2.11
# ==========================================
# Podać sposób wyświetlania stringu word tak, aby jego znaki były rozdzielone znakiem podkreślenia. 

print("=== Task 2.11 ===")
word = "python"

result = "_".join(word)

print(f"Original word: {word}")
print(f"Result using join(): {result}")

assert result == "p_y_t_h_o_n"
assert "_".join("word") == "w_o_r_d"
assert "_".join("A") == "A"
assert "_".join("") == ""

print("Tests for task 2.11 passed!\n")


# ==========================================
# Zadanie 2.12
# ==========================================
# Zbudować string stworzony z pierwszych znaków wyrazów ze stringu line.
# Zbudować napis stworzony z ostatnich znaków wyrazów ze stringu line. 

print("=== Task 2.12 ===")
line = "Wlaz puchatokosmaty kotek na plotek i mruga"

words = line.split()

first_chars = "".join(word[0] for word in words)
last_chars = "".join(word[-1] for word in words)

print(f"Input text: {line}")
print(f"First characters: {first_chars}")
print(f"Last characters: {last_chars}")

assert first_chars == "Wpknpim"
assert last_chars == "zykakia"

sample = "Ala\tma\nczarnego  kota"
assert "".join(w[0] for w in sample.split()) == "Amck"
assert "".join(w[-1] for w in sample.split()) == "aaoa"

print("Tests for task 2.12 passed!\n")


# ==========================================
# Zadanie 2.13
# ==========================================
# Znaleźć łączną długość wyrazów w stringu line. Wskazówka: można skorzystać z funkcji sum().

print("=== Task 2.13 ===")
line = "Wlaz puchatokosmaty kotek na plotek i mruga"

total_length = sum(len(word) for word in line.split())

print(f"Input text: {line}")
print(f"Words: {line.split()}")
print(f"Total word length: {total_length}")

assert total_length == 37
assert sum(len(w) for w in "kotek".split()) == 5
assert sum(len(w) for w in "".split()) == 0

print("Tests for task 2.13 passed!\n")


# ==========================================
# Zadanie 2.14
# ==========================================
# Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w stringu line. 

print("=== Task 2.14 ===")
line = "Wlaz puchatokosmaty kotek na plotek i mruga"

words = line.split()

longest_word = max(words, key=len)
longest_word_len = len(longest_word)

print(f"Input text: {line}")
print(f"(a) Longest word: {longest_word}")
print(f"(b) Length of longest word: {longest_word_len}")

assert longest_word == "puchatokosmaty"
assert longest_word_len == 14
assert max("a bb ccc".split(), key=len) == "ccc"
assert len(max("a bb ccc".split(), key=len)) == 3

print("Tests for task 2.14 passed!\n")


# ==========================================
# Zadanie 2.15
# ==========================================
# Na liście L znajdują się liczby całkowite dodatnie.
# Stworzyć string będący ciągiem cyfr kolejnych liczb z listy L. 

print("=== Task 2.15 ===")
L = [12, 345, 67, 8, 90]

result = "".join(str(x) for x in L)

print(f"List L: {L}")
print(f"Digit sequence: {result}")

assert result == "1234567890"
assert "".join(str(x) for x in [1, 2, 3]) == "123"
assert "".join(str(x) for x in []) == ""

print("Tests for task 2.15 passed!\n")


# ==========================================
# Zadanie 2.16
# ==========================================
# W tekście znajdującym się w stringu line zamienić ciąg znaków "GvR" na "Guido van Rossum". 

print("=== Task 2.16 ===")
line = "Creator of python is GvR. He created python in 1989"

result = line.replace("GvR", "Guido van Rossum")

print(f"Before replacement:\n{line}\n")
print(f"After replacement:\n{result}\n")

expected = "Creator of python is Guido van Rossum. He created python in 1989"
assert result == expected
assert "GvR".replace("GvR", "Guido van Rossum") == "Guido van Rossum"
assert "Plain text".replace("GvR", "Guido van Rossum") == "Plain text"

print("Tests for task 2.16 passed!\n")


# ==========================================
# Zadanie 2.17
# ==========================================
# Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana sorted().

print("=== Task 2.17 ===")
line = "pies kot slon zyrafa hipopotam mrowka papuga"

words = line.split()

sorted_alphabetically = sorted(words)
sorted_by_length = sorted(words, key=len)

print(f"Original string: {line}")
print(f"Words: {words}")
print(f"Alphabetical sort: {sorted_alphabetically}")
print(f"Sort by length: {sorted_by_length}")

assert sorted_alphabetically == [
    "hipopotam", "kot", "mrowka", "papuga", "pies", "slon", "zyrafa"
]
assert sorted_by_length == [
    "kot", "pies", "slon", "zyrafa", "mrowka", "papuga", "hipopotam"
]

print("Tests for task 2.17 passed!\n")


# ==========================================
# Zadanie 2.18
# ==========================================
# Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na string. 

print("=== Task 2.18 ===")
number = 123_000_456_000_789_000_101_010

count_zeros = str(number).count("0")

print(f"Number: {number}")
print(f"Number of zeros: {count_zeros}")

assert count_zeros == 12
assert str(10**100).count("0") == 100
assert str(123456789).count("0") == 0
assert str(0).count("0") == 1

print("Tests for task 2.18 passed!\n")


# ==========================================
# Zadanie 2.19
# ==========================================
# Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować string z trzycyfrowych bloków, gdzie liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill(). 

print("=== Task 2.19 ===")
L = [7, 24, 123, 5, 99, 500]

result = "".join(str(x).zfill(3) for x in L)
result_spaced = ", ".join(str(x).zfill(3) for x in L)

print(f"List L: {L}")
print(f"Result (continuous): {result}")
print(f"Result (with spaces): {result_spaced}")

assert result == "007024123005099500"
assert result_spaced == "007, 024, 123, 005, 099, 500"
assert "".join(str(x).zfill(3) for x in [1]) == "001"
assert "".join(str(x).zfill(3) for x in [12]) == "012"
assert "".join(str(x).zfill(3) for x in [123]) == "123"

print("Tests for task 2.19 passed!\n")
