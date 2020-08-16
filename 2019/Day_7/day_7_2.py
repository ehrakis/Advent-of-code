import itertools

def get_value(instructions, mode, index):
    if mode == "1":
        return instructions[index]
    elif mode == "0":
        return instructions[instructions[index]]
    else:
        raise ValueError("The mode", mode, "doesn't exist.")


# a -> instructions list
# setting -> the setting to apply to the program
# input_param -> the input parameter send by other amplifiers

def run_code(a, setting, input_param):
    index = 0
    a_length = len(a)
    is_setup = False

    while a[index] != 99:

        op_code = str(a[index]).zfill(5)

        # Addition
        if op_code[-2:] == "01":
            a[a[index+3]] = get_value(a,op_code[2],index+1) + get_value(a,op_code[1],index+2)
            index += 4

        # Multiplication
        elif op_code[-2:] == "02":
            a[a[index+3]] = get_value(a,op_code[2],index+1) * get_value(a,op_code[1],index+2)
            index += 4

        # Input
        elif op_code[-2:] == "03":
            if is_setup:
                a[a[index+1]] = input_param
            else:
                a[a[index+1]] = setting
                is_setup = True
            index += 2

        # Output
        elif op_code[-2:] == "04":
            #print(a[a[index+1]])
            input_param = (yield a[a[index+1]])
            index += 2

        # Jump if true
        elif op_code[-2:] == "05":
            if get_value(a, op_code[2], index+1):
                index = get_value(a, op_code[1], index + 2)
            else:
                index += 3

        # Jump if false
        elif op_code[-2:] == "06":
            if not get_value(a, op_code[2], index + 1):
                index = get_value(a, op_code[1], index + 2)
            else:
                index += 3

        # Less than
        elif op_code[-2:] == "07":
            a[a[index + 3]] = 1 if get_value(a, op_code[2], index + 1) < get_value(a, op_code[1], index + 2) else 0
            index += 4

        # Equal
        elif op_code[-2:] == "08":
            a[a[index + 3]] = 1 if get_value(a, op_code[2], index + 1) == get_value(a, op_code[1], index + 2) else 0
            index += 4


def run_amplification(instructions, settings):
    input_value = 0

    # Amplifiers initialization
    amplifier_1 = run_code(instructions[:], settings[0], 0)
    amplifier_2 = run_code(instructions[:], settings[1], next(amplifier_1))
    amplifier_3 = run_code(instructions[:], settings[2], next(amplifier_2))
    amplifier_4 = run_code(instructions[:], settings[3], next(amplifier_3))
    amplifier_5 = run_code(instructions[:], settings[4], next(amplifier_4))
    ampli_1_output = amplifier_1.send(next(amplifier_5))

    while True:
        ampli_2_output = amplifier_2.send(ampli_1_output)
        ampli_3_output = amplifier_3.send(ampli_2_output)
        ampli_4_output = amplifier_4.send(ampli_3_output)
        ampli_5_output = amplifier_5.send(ampli_4_output)
        try:
            ampli_1_output = amplifier_1.send(ampli_5_output)
        except StopIteration:
            return ampli_5_output


with open("day_7_input.txt", "r") as f:
    base_instruction_list = [int(ship) for ship in  f.read().split(",")]
    print(
        max(
            [
                run_amplification(base_instruction_list, permut)
                for permut in itertools.permutations(list(range(5,10)))
            ]
        )
    )

