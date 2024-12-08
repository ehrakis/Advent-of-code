with open("input.txt", "r") as file:
    data = file.read().splitlines()


def compute_operation_result(numbers, signs):
    result = numbers[0]
    for number, sign in zip(numbers[1:], signs):
        if sign == "+":
            result += number
        else:
            result *= number
    return result


def get_initial_signs(numbers):
    return ["+"] * (len(numbers) - 1)


def set_next_signs(signs):
    for i in range(len(signs) - 1, -1, -1):
        if signs[i] == "+":
            signs[i] = "*"
            return True
        else:
            signs[i] = "+"
    return False


calibration_result = 0

for operation in data:
    operation = operation.split(": ")
    expected_result = int(operation[0])
    numbers = [int(i) for i in operation[1].split(" ")]
    signs = get_initial_signs(numbers)
    while True:
        result = compute_operation_result(numbers, signs)
        if result == expected_result:
            calibration_result += expected_result
            break
        if not set_next_signs(signs):
            break

print(calibration_result)