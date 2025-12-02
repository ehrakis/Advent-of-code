with open("2025/day_2/input.txt", "r") as file:
    data = file.read().splitlines()

ranges = data[0].split(",")

known_divisors = {}


def is_invalid(number: int) -> bool:
    number_length = len(str(number))

    if number_length not in known_divisors:
        dividers = [
            num for num in range(1, number_length // 2 + 1) if number_length % num == 0
        ]
        known_divisors[number_length] = dividers

    length_divisor = known_divisors[number_length]

    for divisor in length_divisor:
        splitted_num = list(map("".join, zip(*[iter(str(number))] * divisor)))
        if len(set(splitted_num)) == 1:
            return True
    return False


invalid_ids = []

for id_range in ranges:
    lower, higher = [int(num) for num in id_range.split("-")]
    for id in range(lower, higher + 1):
        if is_invalid(id):
            invalid_ids.append(id)

print(sum(invalid_ids))
