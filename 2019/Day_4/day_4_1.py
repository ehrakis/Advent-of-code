def have_two_digits_number_equal(password):
    for index, digits in enumerate(password[0:-1]):
        if digits == password[index+1]:
            return True
    return False


def never_decreased(password):
    for index, digits in enumerate(password[0:-1]):
        if int(digits) > int(password[index+1]):
            return False
    return True


def password_math_rules(password):
    if never_decreased(str(password)) and have_two_digits_number_equal(str(password)):
        return True
    return False


with open("day_4_input.txt", "r") as f:
    lowest, highest = [int(value) for value in f.read().split("-")]
    print(lowest, highest)

# We may need value for part 2 so I will store in a list but I could just use a counter.
possible_passwords = []

for number in range(lowest, highest + 1):
    if password_math_rules(number):
        possible_passwords.append(number)

print(len(possible_passwords))
