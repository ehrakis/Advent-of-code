with open("input.txt", "r") as file:
    data = file.read()

ITERATION = 25

stones = [int(stone) for stone in data.split()]

stone_number = 0
for stone in stones:
    current_stones = [stone]
    for _ in range(ITERATION):
        index = 0
        while index < len(current_stones):
            if current_stones[index] == 0:
                current_stones[index] +=1
            elif len(str(current_stones[index])) % 2 == 0:
                stone_to_split = str(current_stones[index])
                new_stone_left, new_stone_right = int(stone_to_split[0:len(stone_to_split)//2]), int(stone_to_split[len(stone_to_split)//2:])
                current_stones[index] = new_stone_right
                current_stones.insert(index, new_stone_left)
                index += 1
            else:
                current_stones[index] *=2024
            index += 1
    stone_number += len(current_stones)

print(stone_number)