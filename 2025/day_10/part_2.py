import numpy as np
from scipy.optimize import LinearConstraint, milp


with open("2025/day_10/input.txt", "r") as file:
    data = file.read().splitlines()


def test_switch_combinations(
    expected_output: list[bool], combination: list[tuple[int]]
) -> bool:
    blank_joltage = [0] * len(expected_output)

    for switch in combination:
        for joltage in switch:
            blank_joltage[joltage] += 1

    return blank_joltage == expected_output


nb_switch_press = 0
for index, line in enumerate(data):
    light_data = line.split()
    joltage_goal = [int(x) for x in light_data[-1][1:-1].split(",")]
    switches = [
        eval(switch) if switch[2] == "," else (int(switch[1:-1]),)
        for switch in light_data[1:-1]
    ]

    c = [1] * len(switches)
    matrix = np.zeros((len(joltage_goal), len(switches)), dtype=int)
    for switch_index, switch in enumerate(switches):
        for num in switch:
            matrix[num, switch_index] = 1
    constraints = LinearConstraint(matrix, joltage_goal, joltage_goal)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality)
    nb_switch_press += sum(res.x)


print(int(nb_switch_press))
