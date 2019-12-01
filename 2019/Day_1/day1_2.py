def get_fuel_amount_for_weight(weight):
    return (weight//3)-2

def get_ship_total_fuel_amount(weight):
    needed_fuel = get_fuel_amount_for_weight(weight)
    if needed_fuel <= 0:
        return 0
    else:
        return needed_fuel + get_ship_total_fuel_amount(needed_fuel)

with open("day_1_input.txt", "r") as f:
    print(
        sum(
            [get_ship_total_fuel_amount(int(ship)) for ship in  f.read().split("\n")]
            )
        )