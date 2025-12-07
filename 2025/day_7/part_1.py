with open("2025/day_7/input.txt", "r") as file:
    data = file.read().splitlines()

data = [list(row) for row in data]


def flow_down(data, x, y):
    data[y + 1][x] = "|"


def split(data, x, y):
    # We assume splitter won't be side by side.
    # We also know from the input that there no splitter on the first and last column
    data[y + 1][x - 1] = "|"
    data[y + 1][x + 1] = "|"


time_splitted = 0

for y in range(len(data) - 1):  # No need to compute last row
    for x in range(len(data[0])):
        if data[y][x] in [".", "^"]:
            continue
        elif data[y][x] in ["S", "|"]:
            if data[y + 1][x] == "^":
                split(data, x, y)
                time_splitted += 1
            else:
                flow_down(data, x, y)

print(time_splitted)
