with open("input.txt", "r") as file:
    data = file.read().splitlines()


class Guard:
    def __init__(self, location: tuple[int,int], direction: tuple[int,int], personal_map: list[list[str]]):
        """

        :param location: a tuple of two integers representing the location of the guard, (x,y), where x is the column and y is the row.
        :param direction: a tuple of two integers representing the direction the guard is facing, (x,y), where x is the column and y is the row. Possible values are (-1,0), (1,0), (0,-1), (0,1).
        """
        self.location = location
        self.direction = direction
        self.personal_map = [row.copy() for row in personal_map]
        self.visited = 0
        self.visited_locations = set()
        self.visited_locations_with_directions = set()

    def move(self):
        """
        Move the guard in the direction it is facing. If the guard is facing a wall, turn right and move forward. The
        guard will turn right as long as it is facing a wall.

        """
        if self.personal_map[self.location[1]][self.location[0]] == ".":
            self.personal_map[self.location[1]][self.location[0]] = "X"
            self.visited_locations.add(self.location)
            self.visited += 1

        if (self.location, self.direction) in self.visited_locations_with_directions:
            return "LOOP"
        else:
            self.visited_locations_with_directions.add((self.location, self.direction))

        new_location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])
        if new_location[0] >= len(self.personal_map[0]) or new_location[0] < 0 or new_location[1] >= len(self.personal_map) or new_location[1] < 0:
            return "OUT_OF_BOUNDS"

        if self.personal_map[new_location[1]][new_location[0]] == "#":
            self.direction = (-self.direction[1], self.direction[0])
            return self.move()

        self.location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])
        return "MOVED"


original_map = []

for line in data:
    original_map.append(list(line))

start_location = None
for y in range(len(original_map)):
    found_guard = False
    for x in range(len(original_map[y])):
        if original_map[y][x] == "^":
            start_location = (x,y)
            original_map[y][x] = "."
            found_guard = True
            break
    if found_guard:
        break


guard = Guard(start_location, (0,-1), original_map)

# First iteration to get visited tiles
while True:
    result = guard.move()
    if result == "LOOP" or result == "OUT_OF_BOUNDS":
        break

visited_tiles = guard.visited_locations
loops = 0

for tile in visited_tiles:
    if tile == start_location:
        continue
    original_map[tile[1]][tile[0]] = "#"
    new_guard = Guard(start_location, (0,-1), original_map)
    result = new_guard.move()
    while result == "MOVED":
        result = new_guard.move()
    if result == "LOOP":
        loops += 1
    original_map[tile[1]][tile[0]] = "."

print(loops)
