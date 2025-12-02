with open("2025/day_2/input.txt", "r") as file:
    data = file.read().splitlines()

ranges = data[0].split(",")


def is_invalid(number: int) -> bool:
    number_as_string = str(number)
    if len(number_as_string) % 2 != 0:
        return False

    return (
        number_as_string[0 : len(number_as_string) // 2]
        == number_as_string[len(number_as_string) // 2 :]
    )


invalid_ids = []

for id_range in ranges:
    lower, higher = [int(num) for num in id_range.split("-")]
    for id in range(lower, higher + 1):
        if is_invalid(id):
            invalid_ids.append(id)

print(sum(invalid_ids))
