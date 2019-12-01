def get_fuel_amount(ship_weight):
    return (ship_weight//3)-2

with open("day_1_input.txt", "r") as f:
    print(
        sum(
            [get_fuel_amount(int(ship)) for ship in  f.read().split("\n")]
            )
        )
