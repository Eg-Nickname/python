# ==========================================
# Zadanie 3.10
# ==========================================
# Stworzyć słownik tłumaczący liczby zapisane w systemie
# rzymskim (z literami I, V, X, L, C, D, M jako stringami)
# na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
# Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

print("=== Task 3.10 ===")

roman_dict_1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
roman_dict_2 = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])
roman_dict_3 = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

assert roman_dict_1 == roman_dict_2 == roman_dict_3

def roman2int(roman_str):
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(roman_str)):
        if i + 1 < len(roman_str) and roman_values[roman_str[i]] < roman_values[roman_str[i + 1]]:
            result -= roman_values[roman_str[i]]
        else:
            result += roman_values[roman_str[i]]
    return result


print(f"\nroman2int('XIV') = {roman2int('XIV')}")
print(f"roman2int('MCMXCIX') = {roman2int('MCMXCIX')}")
print(f"roman2int('MMXXVI') = {roman2int('MMXXVI')}")

assert roman2int("I") == 1
assert roman2int("IV") == 4
assert roman2int("IX") == 9
assert roman2int("XIV") == 14
assert roman2int("XL") == 40
assert roman2int("XC") == 90
assert roman2int("CD") == 400
assert roman2int("CM") == 900
assert roman2int("MCMXCIX") == 1999
assert roman2int("MMXXVI") == 2026
assert roman2int("MMMCMXCIX") == 3999
assert roman2int("LVIII") == 58

print("Tests for task 3.10 passed!\n")
