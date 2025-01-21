with open("input.txt", "r") as file:
    data = file.read()

ITERATION = 75

stones = [int(stone) for stone in data.split()]

def count_for_stone(stone: int, iteration: int, mem: dict[tuple[int,int], int]):
    if iteration == ITERATION:
        return 1
    if (stone, iteration) in mem:
        return mem[(stone, iteration)]
    
    if stone == 0:
        result = count_for_stone(1, iteration + 1, mem)
    elif len(str(stone)) % 2 == 0:
        stone_to_split = str(stone)
        result = count_for_stone(int(stone_to_split[0:len(stone_to_split)//2]), iteration + 1, mem) + count_for_stone(int(stone_to_split[len(stone_to_split)//2:]), iteration + 1, mem)
    else:
        result = count_for_stone(stone*2024, iteration + 1, mem)

    mem[(stone, iteration)] = result
    return result

mem: dict[tuple[int,int], int] = {}
stone_number = 0
for stone in stones:
    stone_number += count_for_stone(stone, 0, mem)
print(stone_number)

# print(stone_number)