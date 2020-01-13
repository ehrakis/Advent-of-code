def have_only_two_digits_number_equal(password):
    for index, digits in enumerate(password[0:-1]):
        if digits == password[index+1]:
            if (index == 0 or digits != password[index-1]) and (index==len(password)-2 or digits != password[index+2]):
                return True
    return False


def never_decreased(password):
    for index, digits in enumerate(password[0:-1]):
        if int(digits) > int(password[index+1]):
            return False
    return True


def password_math_rules(password):
    if never_decreased(str(password)) and have_only_two_digits_number_equal(str(password)):
        return True
    return False


with open("day_4_input.txt", "r") as f:
    lowest, highest = [int(value) for value in f.read().split("-")]
    print(lowest, highest)

possible_passwords = 0

for number in range(lowest, highest + 1):
    if password_math_rules(number):
        possible_passwords += 1

print(possible_passwords)
