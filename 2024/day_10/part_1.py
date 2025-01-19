with open("input.txt", "r") as file:
    data = file.read()

island_map = [[int(i) for i in line] for line in data.splitlines()]

DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]

def get_number_of_valid_path(coord: tuple[int,int], island_map: list[list[int]], reached_trail_end: set[tuple[int,int]]) -> int:
    x, y = coord
    if island_map[y][x] == 9 and not coord in reached_trail_end:
        reached_trail_end.add(coord)
        return 1
    
    nb_valid_paths = 0

    for direction in DIRECTIONS:
        new_x, new_y = x + direction[0], y + direction[1]
        if (
            0 <= new_x < len(island_map[0]) 
            and 0 <= new_y < len(island_map) 
            and island_map[new_y][new_x] - island_map[y][x] == 1
        ):
            nb_valid_paths += get_number_of_valid_path((new_x, new_y), island_map, reached_trail_end)
    
    return nb_valid_paths

trail_path_counter = 0

for y, line in enumerate(island_map):
    for x, value in enumerate(line):
        if value == 0:
            number_of_path = get_number_of_valid_path((x,y), island_map, set())
            trail_path_counter += number_of_path

print(trail_path_counter)