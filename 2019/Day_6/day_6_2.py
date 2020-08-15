class Planet:
    def __init__(self, name):
        self.name = name
        self.orbitAround = None
        self.orbits = []

    def addOrbits(self, orbits):
        orbits.orbitAround = self
        self.orbits.append(orbits)


def route_to_com(planet):
    a = [planet]
    while a[-1].name != 'COM':
        a.append(a[-1].orbitAround)
    return a

# Return indexes of the mutal planet in route_1 and route_2
def find_nearest_mutual_node(route_1, route_2):
    for index, planet in enumerate(route_1):
        if planet in route_2:
            return index, route_2.index(planet)

world = {}

with open('day_6_input.txt','r') as f:
    for line in f.read().split('\n'):
        if line != '':
            name_planet_1, name_planet_2 = line.split(')')
            if not name_planet_1 in world:
                planet_1_object = Planet(name_planet_1)
                world[name_planet_1] = planet_1_object

            if not name_planet_2 in world:
                planet_2_object = Planet(name_planet_2)
                world[name_planet_2] = planet_2_object

            if not world[name_planet_2].orbitAround:
                planet_2_object.orbitArround = world[name_planet_1]

            world[name_planet_1].addOrbits(world[name_planet_2])

    you_to_com = route_to_com(world['YOU'])
    san_to_com = route_to_com(world['SAN'])
    indexes = find_nearest_mutual_node(you_to_com,san_to_com)
    # It works because it count the planet wich 'you' is in orbit around and doesn't count the mutual planet
    print(len(you_to_com[1:indexes[0]]) + len(san_to_com[1:indexes[1]]))
