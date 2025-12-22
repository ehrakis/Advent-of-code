from itertools import combinations


with open("2025/day_10/input.txt", "r") as file:
    data = file.read().splitlines()


def all_switch_combinations(switches: list[tuple[int]]):
    for length in range(len(switches)):
        for combination in combinations(switches, length):
            yield combination


def test_switch_combinations(
    expected_output: list[bool], combination: list[tuple[int]]
) -> bool:
    blank_lights = [False] * len(expected_output)

    for switch in combination:
        for ligth in switch:
            blank_lights[ligth] = not blank_lights[ligth]

    return blank_lights == expected_output


switches_used = 0

for line in data:
    light_data = line.split()
    light_goal = [True if x == "#" else False for x in light_data[0][1:-1]]
    switches = [
        eval(switch) if switch[2] == "," else (int(switch[1:-1]),)
        for switch in light_data[1:-1]
    ]

    for combination in all_switch_combinations(switches):
        if test_switch_combinations(light_goal, combination):
            switches_used += len(combination)
            break

print(switches_used)
