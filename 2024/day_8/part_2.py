from collections import defaultdict

with open("input.txt", "r") as file:
    data = file.read().splitlines()

map_size = (len(data[0]), len(data))
antinode_map = [[0] * map_size[0] for _ in range(map_size[1])]

node_dict = defaultdict(list)

# Create a dictionary of nodes with their coordinates
for y in range(map_size[1]):
    for x in range(map_size[0]):
        if data[y][x] != ".":
            node_dict[data[y][x]].append((x, y))

for node in node_dict:
    if len(node_dict[node]) == 1:
        continue

    for antenna in node_dict[node]:
        antinode_map[antenna[1]][antenna[0]] = 1

        for second_antenna in node_dict[node]:
            if antenna != second_antenna:
                vector = (antenna[0] - second_antenna[0], antenna[1] - second_antenna[1])
                antinode_coordinates = (antenna[0] + vector[0], antenna[1] + vector[1])
                while 0 <= antinode_coordinates[0] < map_size[0] and 0 <= antinode_coordinates[1] < map_size[1]:
                    antinode_map[antinode_coordinates[1]][antinode_coordinates[0]] = 1
                    antinode_coordinates = (antinode_coordinates[0] + vector[0], antinode_coordinates[1] + vector[1])

number_of_unique_location_with_antinode = sum([sum(row) for row in antinode_map])
print(number_of_unique_location_with_antinode)