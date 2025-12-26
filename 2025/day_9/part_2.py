from collections import deque


def compute_area(point_1, point_2):
    return (abs(point_1[0] - point_2[0]) + 1) * (abs(point_1[1] - point_2[1]) + 1)


def get_rectangle_perimeter_points(corner_1, corner_2):
    top_left = (
        corner_1[0] if corner_1[0] < corner_2[0] else corner_2[0],
        corner_1[1] if corner_1[1] < corner_2[1] else corner_2[1],
    )
    bottom_right = (
        corner_1[0] if corner_1[0] > corner_2[0] else corner_2[0],
        corner_1[1] if corner_1[1] > corner_2[1] else corner_2[1],
    )

    points = []
    for x in range(top_left[0], bottom_right[0] + 1):
        points.append((x, top_left[1]))

    for y in range(top_left[1] + 1, bottom_right[1] + 1):
        points.append((bottom_right[0], y))

    if top_left[1] != bottom_right[1]:
        for x in range(bottom_right[0] - 1, top_left[0] + 1, -1):
            points.append((x, bottom_right[1]))

    if top_left[0] != bottom_right[0]:
        for y in range(bottom_right[1], top_left[1], -1):
            points.append((top_left[0], y))

    return points


def is_rectangle_inside_polygon(
    outbout_coordinates,
    corner_1,
    corner_2,
):
    perimeter = get_rectangle_perimeter_points(corner_1, corner_2)

    for point in perimeter:
        if point in outbout_coordinates:
            return False
    return True


with open("2025/day_9/input.txt", "r") as file:
    data = file.read().splitlines()


data = deque(tuple(map(int, row.split(","))) for row in data)
perimeter = set()

top_most_point = sorted(data, key=lambda x: x[1])[0]
data.rotate(-data.index(top_most_point))

for _ in range(len(data)):
    previous_point, current, next_point, after_point = (
        data[-1],
        data[0],
        data[1],
        data[2],
    )

    if current[0] == next_point[0]:
        if next_point[1] > current[1]:
            operator = 1

            max_end = 0
            min_start = 0

            if after_point[0] > next_point[0]:
                max_end = -1

            if previous_point[0] > current[0]:
                min_start = 1

        else:
            operator = -1
            max_end = 0
            min_start = 0

            if after_point[0] < next_point[0]:
                max_end = 1

            if previous_point[0] < current[0]:
                min_start = -1

        for i in range(
            current[1] + min_start,
            next_point[1] + (1 if current[1] < next_point[1] else -1) + max_end,
            1 if current[1] < next_point[1] else -1,
        ):
            perimeter.add((current[0] + operator, i))

    else:
        if next_point[0] > current[0]:
            operator = -1

            min_start = 0
            max_end = 0

            if after_point[1] < next_point[1]:
                max_end = -1

            if previous_point[1] < current[1]:
                min_start = 1

        else:
            operator = 1

            min_start = 0
            max_end = 0

            if after_point[1] > next_point[1]:
                max_end = 1

            if previous_point[1] > current[1]:
                min_start = -1

        for i in range(
            current[0] + min_start,
            next_point[0] + (1 if current[0] < next_point[0] else -1) + max_end,
            1 if current[0] < next_point[0] else -1,
        ):
            perimeter.add((i, current[1] + operator))
    data.rotate(-1)


data = list(data)

areas = []
for index, point_from in enumerate(data):
    for point_to in data[index:]:
        area = compute_area(point_from, point_to)
        areas.append((area, point_from, point_to))

areas.sort(key=lambda x: x[0], reverse=True)

max_area = 0

for index, area in enumerate(areas):
    print(f"{index}/{len(areas)}")
    if is_rectangle_inside_polygon(perimeter, area[1], area[2]):
        max_area = area
        break

print(max_area)
