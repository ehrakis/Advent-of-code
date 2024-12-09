with open("input.txt", "r") as file:
    data = file.read()

disk = []

# Recreate disk
for index, block in enumerate(data):
    if index % 2 == 0:
        disk += [index // 2] * int(block)
    else:
        disk += ["."] * int(block)

index = -1
while data[index] == ".":
    index -= 1
if index != -1:
    disk = disk[:index]

# Compacting disk
index = 0
while index < len(disk):
    while disk[index] == ".":
        disk[index] = disk[-1]
        disk = disk[:-1]
    index += 1

checksum = 0
for index, block in enumerate(disk):
    checksum += index * block

print(checksum)
