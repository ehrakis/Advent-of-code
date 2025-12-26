from pprint import pprint

with open("2025/day_12/input.txt", "r") as file:
    # with open("2025/day_12/sample.txt", "r") as file:
    data = file.read().split("\n\n")


def matrix_to_coordinate(
    matrix: list[list[int, int, int]],
) -> tuple[tuple[int, int]]:
    result_matrix = []
    for row_index, row in enumerate(matrix):
        for column_index, column in enumerate(row):
            if column:
                result_matrix.append((column_index, row_index))
    return tuple(result_matrix)


def shape_to_matrix(shape: list[list[str]]):
    result_matrix = []
    for row_index, row in enumerate(shape):
        result_matrix.append([])
        for column in row:
            result_matrix[row_index].append(1 if column == "#" else 0)
    return result_matrix


def rotate_matrix(matrix: list[list[int, int, int]]) -> list[list[int, int, int]]:
    rotated_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            rotated_matrix[col_index][len(matrix[0]) - 1 - row_index] = col
    return rotated_matrix


def flip_matrix(matrix: list[list[int, int, int]]) -> list[list[int, int, int]]:
    flipped_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            flipped_matrix[row_index][len(matrix[0]) - 1 - col_index] = col
    return flipped_matrix


def area_to_coordinates(height, width):
    return {(j, i) for i in range(height) for j in range(width)}


def generate_coordinates_from_offset(starting_point, offset_coordinates):
    coordinates = set()
    x_start, y_start = starting_point
    for coord_offset in offset_coordinates:
        x_offset, y_offset = coord_offset
        coordinates.add((x_start + x_offset, y_start + y_offset))
    return coordinates


def coordinates_are_available(coordinates, starting_point, shape_coordinates_offset):
    shape_cordinates = generate_coordinates_from_offset(
        starting_point, shape_coordinates_offset
    )
    return shape_cordinates.issubset(coordinates)


def fit(
    available_coordinates,
    shapes_options,
    shapes_to_fit: list[int],
    already_tried_placement=None,
):
    # print(f"available coordinates: {available_coordinates}")
    # print(f"Remaining shapes to fit: {shapes_to_fit}")

    if len(shapes_to_fit) == 0:
        return True

    if already_tried_placement is None:
        already_tried_placement = {}

    shape = shapes_to_fit.pop()

    for shape_option in shapes_options[shape]:
        # print(f"    Trying to fit:{shape_option}")
        for coordinate in available_coordinates:
            # print(f"        At coordinates:{coordinate}")
            # If a higher priority similar piece has already tried that location
            # it is useless to try again.
            if (
                shape_option in already_tried_placement
                and coordinate in already_tried_placement[shape_option]
                and already_tried_placement[shape_option][coordinate]
                > len(shapes_to_fit)
            ):
                # print("skipping")
                continue

            if coordinates_are_available(
                available_coordinates, coordinate, shape_option
            ):
                # print("            Coordinates are availables")
                coordinates_to_remove = generate_coordinates_from_offset(
                    coordinate, shape_option
                )
                # print(f"            Removing coordinates:{coordinates_to_remove}")
                if fit(
                    available_coordinates - coordinates_to_remove,
                    shapes_options,
                    shapes_to_fit,
                ):
                    return True
                # Here len(shape) is used as a priority to only retry if the
                # priority is higher (meaning have been tried before but in a
                # different situation).
                if shape_option in already_tried_placement:
                    if coordinate in already_tried_placement[
                        shape_option
                    ] and already_tried_placement[shape_option][coordinate] < len(
                        shape
                    ):
                        already_tried_placement[shape_option][coordinate] = len(
                            shapes_to_fit
                        )
                else:
                    already_tried_placement[shape_option] = {
                        coordinate: len(shapes_to_fit)
                    }
                # print(already_tried_placement)

    shapes_to_fit.insert(0, shape)
    return False


def total_area_for_shapes(shapes_to_fit, shapes_options):
    area = 0
    for shape in shapes_to_fit:
        area += len(shapes_options[shape][0])
    return area


shapes = [[list(row) for row in line.split()[1:]] for line in data[:-1]]
areas = data[-1].split("\n")

shapes_options = {}
for shape_index, shape in enumerate(shapes):
    matrix_shapes = [shape_to_matrix(shape)]
    last_matrix_state = matrix_shapes[0]
    for _ in range(3):
        last_matrix_state = rotate_matrix(last_matrix_state)
        if last_matrix_state not in matrix_shapes:
            matrix_shapes.append(last_matrix_state)

    last_matrix_state = flip_matrix(matrix_shapes[0])
    if last_matrix_state not in matrix_shapes:
        matrix_shapes.append(last_matrix_state)

    for _ in range(3):
        last_matrix_state = rotate_matrix(last_matrix_state)
        if last_matrix_state not in matrix_shapes:
            matrix_shapes.append(last_matrix_state)

    shapes_options[shape_index] = [
        matrix_to_coordinate(matrix) for matrix in matrix_shapes
    ]

impossible = 0
possible = 0
for index, area in enumerate(areas):
    dimensions, raw_shapes_to_fit = area.split(": ")
    height, width = map(int, dimensions.split("x"))

    shapes_to_fit = [
        index
        for index, number in enumerate(map(int, raw_shapes_to_fit.split()))
        for _ in range(number)
    ]
    shapes_area = total_area_for_shapes(shapes_to_fit, shapes_options)
    area_coordinates = area_to_coordinates(height, width)

    if shapes_area > len(area_coordinates):
        impossible += 1
    elif (height // 3) * (width // 3) >= len(shapes_to_fit):
        possible += 1
    else:
        if fit(area_coordinates, shapes_options, shapes_to_fit):
            possible += 1
        else:
            impossible += 1

print(possible)
