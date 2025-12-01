with open("2025/day_1/input.txt", "r") as file:
    data = file.read().splitlines()

number_of_zeros = 0

position = 50

for line in data:
    if line[0] == "L":
        position = (position + (100 - int(line[1:]))) % 100
    else:
        position = (position + int(line[1:])) % 100
    if position == 0:
        number_of_zeros += 1

print(number_of_zeros)
