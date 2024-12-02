with open("input.txt", "r") as file:
    data = file.read().splitlines()

unsafe_reports = 0

for line in data:
    report_data = line.split(" ")
    length = len(report_data)
    if int(report_data[0]) - int(report_data[1]) == 0:
        unsafe_reports += 1
        continue
    else:
        if int(report_data[1]) - int(report_data[0]) > 0:
            i = 1
            j = 0
        else:
            i = 0
            j = 1

    while j < length and i < length:
        if int(report_data[i]) - int(report_data[j]) not in [1, 2, 3]:
            unsafe_reports += 1
            break
        i += 1
        j += 1

print(len(data)-unsafe_reports)
