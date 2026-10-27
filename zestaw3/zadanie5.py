# ==========================================
# Zadanie 3.5
# ==========================================
# Napisać program rysujący "miarkę" o zadanej długości.
# Długość miarki (x) ma być zapisana w osobnej zmiennej jako parametr programu.
# Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
# (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
# Należy zbudować pełny string, a potem go wypisać.
#
# |....|....|....|....|....|....|....|....|....|....|....|....|   (x = 12)
# 0    1    2    3    4    5    6    7    8    9   10   11   12

print("=== Task 3.5 ===")

# PARAM ===============
ruler_x = 12
# =====================

def make_ruler(p_x):
    top_line = "|" + "....|" * p_x
    bottom_line = "0"
    for i in range(1, p_x + 1):
        label = str(i)
        gap = 5 - len(label)
        bottom_line += " " * gap + label
    return top_line + "\n" + bottom_line


ruler_x_str = make_ruler(ruler_x)
print(ruler_x_str, "\n")

ruler_12 = make_ruler(12)
expected_top = "|....|....|....|....|....|....|....|....|....|....|....|....|"
expected_bottom = "0    1    2    3    4    5    6    7    8    9   10   11   12"
assert ruler_12 == expected_top + "\n" + expected_bottom

ruler_1 = make_ruler(1)
assert ruler_1 == "|....|\n0    1"

ruler_0 = make_ruler(0)
assert ruler_0 == "|\n0"

print("Tests for task 3.5 passed!\n")
