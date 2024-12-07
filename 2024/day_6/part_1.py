with open("input.txt", "r") as file:
    data = file.read().splitlines()


class Guard:
    def __init__(self, location: tuple[int,int], direction: tuple[int,int]):
        """

        :param location: a tuple of two integers representing the location of the guard, (x,y), where x is the column and y is the row.
        :param direction: a tuple of two integers representing the direction the guard is facing, (x,y), where x is the column and y is the row. Possible values are (-1,0), (1,0), (0,-1), (0,1).
        """
        self.location = location
        self.direction = direction
        self.visited = 0

    def move(self, map: list[list[str]]):
        """
        Move the guard in the direction it is facing. If the guard is facing a wall, turn right and move forward. The
        guard will turn right as long as it is facing a wall.

        """
        if map[self.location[1]][self.location[0]] == ".":
                map[self.location[1]][self.location[0]] = "X"
                self.visited += 1

        new_location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])
        if new_location[0] >= len(map[0]) or new_location[0] < 0 or new_location[1] >= len(map) or new_location[1] < 0:
            return False

        if map[new_location[1]][new_location[0]] == "#":
            self.direction = (-self.direction[1], self.direction[0])
            return self.move(map)

        self.location = (self.location[0] + self.direction[0], self.location[1] + self.direction[1])
        return True

map = []

for line in data:
    map.append(list(line))

guard = None
for y in range(len(map)):
    found_guard = False
    for x in range(len(map[y])):
        if map[y][x] == "^":
            guard = Guard((x,y), (0,-1))
            map[y][x] = "."
            found_guard = True
            break
    if found_guard:
        break

while guard.move(map):
    pass

print(guard.visited)