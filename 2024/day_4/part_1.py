with open("input.txt", "r") as file:
    data = file.read().splitlines()


def look_for_xmas(table: list[list[str]], start: tuple[int, int], direction: tuple[int, int]) -> bool:
    x, y = start
    for letter in list("XMAS"):
        if not len(table[0]) > x >= 0 or not len(table) > y >= 0 or table[y][x] != letter:
            return False
        x += direction[0]
        y += direction[1]
    return True

table: list[list[str]] = [list(line) for line in data]
directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]
number_of_xmas = 0
for y in range(len(table)):
    for x in range(len(table[y])):
        if table[y][x] == "X":
            for direction in directions:
                if look_for_xmas(table, (x, y), direction):
                   number_of_xmas += 1

print(number_of_xmas)