class Planet:
    def __init__(self, name):
        self.name = name
        self.orbitAround = None
        self.orbits = []

    def addOrbits(self, orbits):
        self.orbits.append(orbits)


def count_orbits(planet, tree_level=0):
    orbits = tree_level
    for sub_planet in planet.orbits:
        if sub_planet.orbits:
            orbits += count_orbits(sub_planet, tree_level + 1)
        else:
            orbits += tree_level + 1
    return orbits

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

    print(count_orbits(world['COM']))
