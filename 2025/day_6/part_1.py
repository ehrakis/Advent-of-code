from math import prod
import re

LENGTH_OF_OPERATION = 4

with open("2025/day_6/input.txt", "r") as file:
    data = file.read().splitlines()

data = [re.split(r" {1,}", row.strip()) for row in data]

full_sum = 0

for index in range(len(data[0])):
    if data[-1][index] == "+":
        operation = sum
    else:
        operation = prod
    full_sum += operation([int(data[x][index]) for x in range(LENGTH_OF_OPERATION)])

print(full_sum)
