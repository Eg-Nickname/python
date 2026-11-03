# ==========================================
# Zadanie 4.2
# ==========================================
# Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu
# zapisać w postaci funkcji, które zwracają pełny string
# przez return. Funkcje nie powinny pytać użytkownika o dane,
# tylko korzystać z argumentów.

print("=== Task 4.2 ===")

# ======== RULER ========

def make_ruler(n):
    top_line = "|" + "....|" * n
    bottom_line = "0"
    for i in range(1, n + 1):
        label = str(i)
        gap = 5 - len(label)
        bottom_line += " " * gap + label
    return top_line + "\n" + bottom_line

ruler_12 = make_ruler(12)

expected_top = "|....|....|....|....|....|....|....|....|....|....|....|....|"
expected_bottom = "0    1    2    3    4    5    6    7    8    9   10   11   12"
assert ruler_12 == expected_top + "\n" + expected_bottom

ruler_1 = make_ruler(1)
assert ruler_1 == "|....|\n0    1"

ruler_0 = make_ruler(0)
assert ruler_0 == "|\n0"

print("Tests for make_ruler passed!")

# ======== RECTANGLE ========

def make_grid(p_x, p_y):
    border_line = ("+" + "---") * p_x + "+"
    cell_line = ("|" + "   ") * p_x + "|"
    rows = []
    for _ in range(p_y):
        rows.append(border_line)
        rows.append(cell_line)
    rows.append(border_line)
    return "\n".join(rows)

rect_4_2 = make_grid(4, 2)
expected_4_2 = "\n".join([
    "+---+---+---+---+",
    "|   |   |   |   |",
    "+---+---+---+---+",
    "|   |   |   |   |",
    "+---+---+---+---+",
])
assert rect_4_2 == expected_4_2

rect_1_1 = make_grid(1, 1)
expected_1_1 = "\n".join([
    "+---+",
    "|   |",
    "+---+",
])
assert rect_1_1 == expected_1_1

rect_3_3 = make_grid(3, 3)
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

print("Tests for make_grid passed!")

print("Tests for task 4.2 passed!\n")
