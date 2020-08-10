def get_value(instructions, mode, index):
    if mode == "1":
        return instructions[index]
    elif mode == "0":
        return instructions[instructions[index]]
    else:
        raise ValueError("The mode", mode, "doesn't exist.") 


with open("day_5_input.txt", "r") as f:
    a = [int(ship) for ship in  f.read().split(",")]

    index = 0
    a_length = len(a)
    
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
            a[a[index+1]] = int(input())
            index += 2
        
        # Output
        elif op_code[-2:] == "04":
            print(a[a[index+1]])
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


















