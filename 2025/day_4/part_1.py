with open("2025/day_4/input.txt", "r") as file:
    data = file.read().splitlines()

roll_grid = [list(line) for line in data]


def less_than_4_roll_around(x: int, y: int, grid: list[list[str]]) -> int:
    min_x = x - 1 if x >= 1 else 0
    max_x = x + 1 if x < len(grid[0]) - 1 else len(grid[0]) - 1
    min_y = y - 1 if y >= 1 else 0
    max_y = y + 1 if y < len(grid) - 1 else len(grid) - 1
    roll_number = 0
    for x_target in range(min_x, max_x + 1):
        for y_target in range(min_y, max_y + 1):
            if x_target == x and y_target == y:
                continue
            if grid[y_target][x_target] == "@":
                roll_number += 1
                if roll_number >= 4:
                    return False
    return True


available_rolls = 0

for y in range(0, len(roll_grid)):
    for x in range(0, len(roll_grid[0])):
        if roll_grid[y][x] == "@" and less_than_4_roll_around(x, y, roll_grid):
            available_rolls += 1

print(available_rolls)
