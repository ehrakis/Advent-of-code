with open("input.txt", "r") as file:
    data = file.read().splitlines()

left_list = []
right_list = []
for line in data:
    left, right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()
total = 0
for i,j in zip(left_list, right_list):
    total += abs(i-j)

print(total)