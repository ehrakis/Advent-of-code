with open("input.txt", "r") as file:
    data = file.read()

disk = []

# Recreate disk
for index, block in enumerate(data):
    if index % 2 == 0:
        disk += [index // 2] * int(block)
    else:
        disk += ["."] * int(block)

# Index free space and files
free_space = []
files = []
index = 0
while index < len(disk):
    if disk[index] == ".":
        starting_index = index
        final_index = index
        while disk[final_index] == ".":
            final_index += 1
        free_space.append((final_index-starting_index, starting_index, final_index))
        index = final_index
    else:
        current_file = disk[index]
        starting_index = index
        final_index = index
        while final_index < len(disk) and disk[final_index] == current_file:
            final_index += 1
        files.append((final_index-starting_index, starting_index, final_index, current_file))
        index = final_index

# Compacting disk
files.reverse()
for file in files:
    for index, space in enumerate(free_space):
        if space[1] > file[1]:
            break
        if file[0] <= space[0]:
            disk[space[1]:space[1]+file[0]] = [file[3]] * file[0]
            disk[file[1]:file[2]] = ["."] * file[0]
            if file[0] < space[0]:
                free_space[index] = (space[0] - file[0], space[1] + file[0], space[2])
            else:
                free_space.pop(index)
            break

checksum = 0
for index, block in enumerate(disk):
    if block != ".":
        checksum += index * block

print(checksum)
