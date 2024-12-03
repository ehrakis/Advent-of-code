import re

with open("input.txt", "r") as file:
    data = file.read()

multiplications_re = "(mul\\([0-9]{1,3},[0-9]{1,3}\\))"
split_data = data.split("don't()")

segments = [split_data.pop(0)] + ["".join(dont_segment.split("do()")[1:]) for dont_segment in split_data]

score = 0
for segment in segments:
    multiplications = re.findall(multiplications_re, segment)
    for multiplication in multiplications:
        x, y = [int(i) for i in multiplication[4:-1].split(",")]
        score += x * y

print(score)
