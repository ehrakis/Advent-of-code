import re

with open("input.txt", "r") as file:
    data = file.read()

score = 0
multiplications = re.findall("(mul\\([0-9]{1,3},[0-9]{1,3}\\))", data)
for multiplication in multiplications:
    x, y = [int(i) for i in multiplication[4:-1].split(",")]
    score += x*y

print(score)