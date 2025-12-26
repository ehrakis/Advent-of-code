def compute_area(point_1, point_2):
    return abs(point_1[0] - point_2[0] + 1) * abs(point_1[1] - point_2[1] + 1)


with open("2025/day_9/input.txt", "r") as file:
    data = file.read().splitlines()

data = [tuple([int(coord) for coord in row.split(",")]) for row in data]

max_area = 0
areas = []

for index, point_from in enumerate(data):
    for point_to in data[index:]:
        area = compute_area(point_from, point_to)
        areas.append((area, point_from, point_to))
        if area > max_area:
            max_area = area

print(max_area)
