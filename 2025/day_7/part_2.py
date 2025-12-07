from pprint import pprint

with open("2025/day_7/input.txt", "r") as file:
    data = file.read().splitlines()

data = [list(row) for row in data]

S_LOCATION = (len(data[0]) - 1) // 2

time_lines_by_node = {}


def flow_down(data, x, y):
    if y + 1 >= len(data):
        return 1
    elif data[y + 1][x] == "^":
        return split(data, x, y + 1)
    else:
        return flow_down(data, x, y + 1)


def split(data, x, y):
    if (x, y) not in time_lines_by_node:
        time_lines_by_node[(x, y)] = flow_down(data, x - 1, y) + flow_down(
            data, x + 1, y
        )

    return time_lines_by_node[(x, y)]


time_lines = flow_down(data, S_LOCATION, 0)

print(time_lines)
