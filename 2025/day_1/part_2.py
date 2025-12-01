with open("2025/day_1/input.txt", "r") as file:
    data = file.read().splitlines()

number_of_zeros = 0

position = 50

for line in data:
    direction = line[0]
    clicks = int(line[1:])

    if direction == "L":
        raw_position = position - clicks
    else:
        raw_position = position + clicks

    position = raw_position % 100
    number_of_zeros += abs(raw_position // 100)

print(number_of_zeros)
