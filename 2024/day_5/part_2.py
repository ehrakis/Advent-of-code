with open("input.txt", "r") as file:
    data = file.read()


def get_unvalidated_rules(page_order, rules):
    new_rules = []
    for rule in rules:
        try:
            first_page = page_order.index(rule[0])
            second_page = page_order.index(rule[1])
        except ValueError:
            continue
        if first_page > second_page:
            new_rules.append(rule)
    return new_rules

raw_rules, raw_pages_orders = [part.splitlines() for part in data.split("\n\n")]

rules = []
for raw_rule in raw_rules:
    rule = raw_rule.split("|")
    rules.append((int(rule[0]), int(rule[1])))

pages_orders = []
for raw_page_order in raw_pages_orders:
    page_order = raw_page_order.split(",")
    pages_orders.append([int(i) for i in page_order])

wrong_orders = []

for page_order in pages_orders:
    wrong_rules = []
    for rule in rules:
        try:
            first_page = page_order.index(rule[0])
            second_page = page_order.index(rule[1])
        except ValueError:
            continue
        if first_page > second_page:
            wrong_rules.append(rule)
    if wrong_rules:
        wrong_orders.append((page_order, wrong_rules))

reordered_orders = []

for wrong_order in wrong_orders:
    is_ordered = False
    page_order = wrong_order[0]
    broken_rules = wrong_order[1]
    while not is_ordered:
        for rule in broken_rules:
            first_page = page_order.index(rule[0])
            second_page = page_order.index(rule[1])
            if first_page > second_page:
                page_order[first_page], page_order[second_page] = page_order[second_page], page_order[first_page]
        broken_rules = get_unvalidated_rules(page_order, rules)  # Doing this tests every rules even those that don't apply to this page order
        if not broken_rules:
            is_ordered = True
    reordered_orders.append(page_order)

middle_page_sum = 0
for reordered_order in reordered_orders:
    middle_page_sum += reordered_order[len(reordered_order) // 2]

print(middle_page_sum)