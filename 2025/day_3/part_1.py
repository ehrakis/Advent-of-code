with open("2025/day_3/input.txt", "r") as file:
    data = file.read().splitlines()


def get_max_joltage(bank: str) -> int:
    bank_joltage_list = [int(x) for x in list(bank)]
    max_num = 0
    max_index = 0
    for index, num in enumerate(bank_joltage_list[:-1]):
        if num > max_num:
            max_num = num
            max_index = index
    return str(max_num) + str(max(bank_joltage_list[max_index + 1 :]))


joltage_sum = 0

for bank in data:
    joltage_sum += int(get_max_joltage(bank))


print(joltage_sum)
