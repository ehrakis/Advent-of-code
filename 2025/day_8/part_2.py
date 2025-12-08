from math import sqrt

with open("2025/day_8/input.txt", "r") as file:
    data = file.read().splitlines()

data = [tuple([int(coord) for coord in row.split(",")]) for row in data]

distances = []


def compute_distance(point_1, point_2):
    return sqrt(
        (point_1[0] - point_2[0]) ** 2
        + (point_1[1] - point_2[1]) ** 2
        + (point_1[2] - point_2[2]) ** 2
    )


for index, coord_from in enumerate(data[:-1]):
    for coord_to in data[index + 1 :]:
        distance = compute_distance(coord_from, coord_to)
        distances.append((distance, coord_from, coord_to))

distances.sort(key=lambda x: x[0])

circuits = {}
node_to_circuits = {}
index = 0

while len(circuits) != 1 or len(circuits[next(iter(circuits))]) != len(data):
    _, node_1, node_2 = distances[index]
    node_1_is_connected = node_1 in node_to_circuits
    node_2_is_connected = node_2 in node_to_circuits

    if node_1_is_connected and not node_2_is_connected:
        circuits[node_to_circuits[node_1]].append(node_2)
        node_to_circuits[node_2] = node_to_circuits[node_1]

    elif node_2_is_connected and not node_1_is_connected:
        circuits[node_to_circuits[node_2]].append(node_1)
        node_to_circuits[node_1] = node_to_circuits[node_2]

    elif not node_1_is_connected and not node_2_is_connected:
        circuits[index] = [node_1, node_2]
        node_to_circuits[node_1] = index
        node_to_circuits[node_2] = index

    elif node_to_circuits[node_1] != node_to_circuits[node_2]:
        node_2_circuit = node_to_circuits[node_2]
        circuits[node_to_circuits[node_1]] += circuits[node_to_circuits[node_2]]
        for node in circuits[node_2_circuit]:
            node_to_circuits[node] = node_to_circuits[node_1]
        del circuits[node_2_circuit]

    index += 1

print(node_1[0] * node_2[0])
