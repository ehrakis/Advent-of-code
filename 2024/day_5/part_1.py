with open("input.txt", "r") as file:
    data = file.read()

raw_rules, raw_pages_orders = [part.splitlines() for part in data.split("\n\n")]

rules = []
for raw_rule in raw_rules:
    rule = raw_rule.split("|")
    rules.append((int(rule[0]), int(rule[1])))

pages_orders = []
for raw_page_order in raw_pages_orders:
    page_order = raw_page_order.split(",")
    pages_orders.append(tuple(int(i) for i in page_order))

correct_orders = []

for page_order in pages_orders:
    right_order = True
    for rule in rules:
        try:
            first_page = page_order.index(rule[0])
            second_page = page_order.index(rule[1])
        except ValueError:
            continue
        if first_page > second_page:
            right_order = False
            break
    if right_order:
        correct_orders.append(page_order)

middle_page_sum = 0
for correct_order in correct_orders:
    middle_page_sum += correct_order[len(correct_order) // 2]

print(middle_page_sum)