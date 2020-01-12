# The code I wrote for this day is just disgusting.
# It does the job but not in a really nice way.
# I suggest you to NOT read this or your eyes could burn.

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"


def dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def get_lowest_max_axis_values(wire):
    """
    Find the lowest and maximum values on the x and y axis
    :param wire:
    :return: a tuple with 4 integer in the following format (lowest y value, loweest x value, max y value, max x value)
    """
    min_y = 0
    max_y = 0
    min_x = 0
    max_x = 0

    # As the start cell is not included in the count we need to 1 to the first value
    # For example if the first instruction is R8 the matrix need to be at least 9 cell width because the first cell
    # will be the start cell and the 8 cells on the right will be the wire.

    wire[0] = wire[0][0] + str(int(wire[0][1:])+1)

    current_x, current_y = 0, 0

    for instruction in wire:
        direction = instruction[0]
        value = int(instruction[1:])

        if direction == RIGHT:
            current_x += value
            if current_x > max_x:
                max_x = current_x

        elif direction == LEFT:
            current_x -= value
            if current_x < min_x:
                min_x = current_x

        elif direction == UP:
            current_y += value
            if current_y > max_y:
                max_y = current_y

        elif direction == DOWN:
            current_y -= value
            if current_y < min_y:
                min_y = current_y

        else:
            raise Exception()

    # Set the first instruction to its original value
    wire[0] = wire[0][0] + str(int(wire[0][1:]) - 1)

    return min_y, min_x, max_y, max_x


with open("day_3_input.txt", "r") as f:
    content = f.read()
    wire_1, wire_2 = [wire.split(',') for wire in content.split('\n')]

# Wires will be drawn in a 2 dimension array, for that we need to find the grid size
wire_1_min_y, wire_1_min_x, wire_1_max_y, wire_1_max_x = get_lowest_max_axis_values(wire_1)
wire_2_min_y, wire_2_min_x, wire_2_max_y, wire_2_max_x = get_lowest_max_axis_values(wire_2)

min_y = min(wire_1_min_y, wire_2_min_y)
min_x = min(wire_1_min_x, wire_2_min_x)
max_y = max(wire_1_max_y, wire_2_max_y) + 10
max_x = max(wire_1_max_x, wire_2_max_x) + 10

y_size = abs(min_y) + max_y
x_size = abs(min_x) + max_x

start_position = (abs(min_x), abs(min_y))

# Build the matrix
matrix = [[(0, 0) for _ in range(x_size)] for _ in range(y_size)]

# Draw the first wire
current_x, current_y = start_position[0], start_position[1]

# Cell where the wire 1 is will be set to 1.
step_number = 0
for instruction in wire_1:
    direction = instruction[0]
    value = int(instruction[1:])

    if direction == RIGHT:
        for x_value in range(current_x + 1, current_x + value + 1):
            matrix[current_y][x_value] = (1, step_number + x_value - current_x)
        current_x += value

    elif direction == LEFT:
        for x_value in range(current_x - 1, current_x - value - 1, -1):
            matrix[current_y][x_value] = (1, step_number - x_value + current_x)
        current_x -= value

    elif direction == UP:
        for y_value in range(current_y + 1, current_y + value + 1):
            matrix[y_value][current_x] = (1, step_number + y_value - current_y)
        current_y += value

    elif direction == DOWN:
        for y_value in range(current_y - 1, current_y - value - 1, -1):
            matrix[y_value][current_x] = (1, step_number - y_value + current_y)
        current_y -= value

    else:
        raise Exception()

    step_number += value

min_distance = max(y_size, x_size)
intersections = []


step_number = 0
current_x, current_y = start_position[0], start_position[1]
for instruction in wire_2:
    direction = instruction[0]
    value = int(instruction[1:])
    if direction == RIGHT:
        for x_value in range(current_x + 1, current_x + value + 1):
            if matrix[current_y][x_value][0] == 1:
                distance = dist(start_position[0], start_position[1], x_value, current_y)
                intersections.append(((x_value, current_y), step_number + x_value - current_x, matrix[current_y][x_value][1]))
                if distance < min_distance:
                    min_distance = distance
                # The value 3 will represent the intersection
                matrix[current_y][x_value] = (3, step_number + x_value - current_x + matrix[current_y][x_value][1])
            # No need to draw it in the matrix but still do it in case this feature is needed to debug
            else:
                matrix[current_y][x_value] = (2, step_number + x_value - current_x)
        current_x += value

    elif direction == LEFT:
        for x_value in range(current_x - 1, current_x - value - 1, -1):
            if matrix[current_y][x_value][0] == 1:
                distance = dist(start_position[0], start_position[1], x_value, current_y)
                intersections.append(((x_value, current_y), step_number - x_value + current_x, matrix[current_y][x_value][1]))
                if distance < min_distance:
                    min_distance = distance
                matrix[current_y][x_value] = (3, step_number - x_value + current_x + matrix[current_y][x_value][1])
            else:
                matrix[current_y][x_value] = (2, step_number - x_value + current_x)
        current_x -= value

    elif direction == UP:
        for y_value in range(current_y + 1, current_y + value + 1):
            if matrix[y_value][current_x][0] == 1:
                distance = dist(start_position[0], start_position[1], current_x, y_value)
                intersections.append(((x_value, current_y), step_number + y_value - current_y, matrix[y_value][current_x][1]))
                if distance < min_distance:
                    min_distance = distance
                matrix[y_value][current_x] = (3, step_number + y_value - current_y + matrix[y_value][current_x][0])
            else:
                matrix[y_value][current_x] = (2, step_number + y_value - current_y)
        current_y += value

    elif direction == DOWN:
        for y_value in range(current_y - 1, current_y - value - 1, -1):
            if matrix[y_value][current_x][0] == 1:
                distance = dist(start_position[0], start_position[1], current_x, y_value)
                intersections.append(((x_value, current_y), step_number - y_value + current_y, matrix[y_value][current_x][1]))
                if distance < min_distance:
                    min_distance = distance
                matrix[y_value][current_x] = (3, step_number - y_value + current_y + matrix[y_value][current_x][1])
            else:
                matrix[y_value][current_x] = (2, step_number - y_value + current_y)
        current_y -= value

    else:
        raise Exception()
    step_number += value

min_step_value = intersections[0][1]+intersections[0][2]
for intersection in intersections:
    steps = intersection[1] + intersection[2]
    if steps < min_step_value:
        min_step_value = steps

print(min_step_value)
