with open("input.txt", "r") as file:
    data = file.read().splitlines()


def is_x_mas(table: list[list[str]], start: tuple[int, int]) -> bool:
    x, y = start
    if not len(table[0]) - 1 > x > 0 or not len(table) - 1 > y > 0:
        return False
    def is_upper_left_to_bottom_right_x_mas(table, x, y):
        if table[y - 1][x - 1] == "M" and table[y + 1][x + 1] == "S" or table[y - 1][x - 1] == "S" and table[y + 1][x + 1] == "M":
            return True
        return False
    def is_bottom_left_to_upper_right_x_mas(table, x, y):
        if table[y + 1][x - 1] == "M" and table[y - 1][x + 1] == "S" or table[y + 1][x - 1] == "S" and table[y - 1][ x + 1] == "M":
            return True
        return False
    return is_bottom_left_to_upper_right_x_mas(table, x, y) and is_upper_left_to_bottom_right_x_mas(table, x, y)


table: list[list[str]] = [list(line) for line in data]

number_of_xmas = 0
for y in range(len(table)):
    for x in range(len(table[y])):
        if table[y][x] == "A":
            if is_x_mas(table, (x, y)):
               number_of_xmas += 1

print(number_of_xmas)
