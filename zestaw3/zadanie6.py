# ==========================================
# Zadanie 3.6
# ==========================================
# Napisać program rysujący prostokąt zbudowany z małych kratek.
# Należy zbudować pełny string, a potem go wypisać.
# Liczby kratek w wierszach (y) i kolumnach (x) mają być zapisane
# w osobnych zmiennych jako parametry programu.
# Przykładowy prostokąt składający się 2 × 4 pól ma postać:
#
# +---+---+---+---+   (x = 4, y = 2)
# |   |   |   |   |
# +---+---+---+---+
# |   |   |   |   |
# +---+---+---+---+

print("=== Task 3.6 ===")


# PARAM ===============
x, y = 4, 4
# =====================

def make_rectangle(p_x, p_y):
    border_line = ("+" + "---") * p_x + "+"
    cell_line = ("|" + "   ") * p_x + "|"
    rows = []
    for _ in range(p_y):
        rows.append(border_line)
        rows.append(cell_line)
    rows.append(border_line)
    return "\n".join(rows)

rect_x_y = make_rectangle(x, y)
print(rect_x_y)
print()

rect_4_2 = make_rectangle(4, 2)
expected_4_2 = "\n".join([
    "+---+---+---+---+",
    "|   |   |   |   |",
    "+---+---+---+---+",
    "|   |   |   |   |",
    "+---+---+---+---+",
])
assert rect_4_2 == expected_4_2

rect_1_1 = make_rectangle(1, 1)
expected_1_1 = "\n".join([
    "+---+",
    "|   |",
    "+---+",
])
assert rect_1_1 == expected_1_1

rect_3_3 = make_rectangle(3, 3)
expected_3_3 = "\n".join([
    "+---+---+---+",
    "|   |   |   |",
    "+---+---+---+",
    "|   |   |   |",
    "+---+---+---+",
    "|   |   |   |",
    "+---+---+---+",
])
assert rect_3_3 == expected_3_3

print("Tests for task 3.6 passed!\n")
