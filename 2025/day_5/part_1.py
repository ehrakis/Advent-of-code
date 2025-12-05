with open("2025/day_5/input.txt", "r") as file:
    data = file.read().splitlines()


fresh_ingredient_ranges = [
    (int(fresh_range.split("-")[0]), int(fresh_range.split("-")[1]))
    for fresh_range in data[: data.index("")]
]

ingredients = [int(num) for num in data[data.index("") + 1 :]]

fresh_ingredients_count = 0
fresh_ingredients_set = set()

for ingredient in ingredients:
    for fresh_ingredient_range in fresh_ingredient_ranges:
        if (
            ingredient >= fresh_ingredient_range[0]
            and ingredient <= fresh_ingredient_range[1]
        ):
            fresh_ingredients_set.add(ingredient)
            break

print(len(fresh_ingredients_set))
