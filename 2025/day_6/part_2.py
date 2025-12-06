from math import prod

LENGTH_OF_OPERATION = 4


def compute_block(data, block_start_index, block_end_index):
    numbers = [
        int(
            "".join(
                [
                    data[number_index][operation_index]
                    for number_index in range(LENGTH_OF_OPERATION)
                ]
            )
        )
        for operation_index in range(block_start_index, block_end_index + 1)
    ]

    operation = sum if data[-1][block_start_index] == "+" else prod
    return operation(numbers)


with open("2025/day_6/input.txt", "r") as file:
    data = file.read().splitlines()

data = [list(row) for row in data]

full_sum = 0

operation_start_index = 0
operation_end_index = 1

while operation_start_index < len(data[0]):
    if operation_end_index < len(data[0]) and data[-1][operation_end_index] == " ":
        operation_end_index += 1
        continue
    # handle the last block behaviour
    elif operation_end_index == len(data[0]):
        operation_end_index += 1

    # -2 because operation_end_index is on the next operation sign
    full_sum += compute_block(data, operation_start_index, operation_end_index - 2)

    operation_start_index = operation_end_index
    operation_end_index += 1


print(full_sum)
