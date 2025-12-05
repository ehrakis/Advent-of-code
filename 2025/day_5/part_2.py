with open("2025/day_5/input.txt", "r") as file:
    data = file.read().splitlines()


fresh_ingredient_ranges = [
    (int(fresh_range.split("-")[0]), int(fresh_range.split("-")[1]))
    for fresh_range in data[: data.index("")]
]
fresh_ingredient_ranges.sort()

concatenated_ranges = []


def is_in_range(num, num_range):
    return num >= num_range[0] and num <= num_range[1]


# Range concatenation
for index, fresh_range in enumerate(fresh_ingredient_ranges):
    if index == 0:
        concatenated_ranges.append(fresh_range)

    # No overlap
    elif not is_in_range(fresh_range[0], concatenated_ranges[-1]):
        concatenated_ranges.append(fresh_range)

    # fresh_range overlap and we need to update the range
    elif not is_in_range(fresh_range[1], concatenated_ranges[-1]):
        concatenated_ranges[-1] = (concatenated_ranges[-1][0], fresh_range[-1])

    # else fresh_range is contained inside previous range

fresh_ids_available = 0
for fresh_range in concatenated_ranges:
    fresh_ids_available += fresh_range[-1] - fresh_range[0] + 1

print(fresh_ids_available)
