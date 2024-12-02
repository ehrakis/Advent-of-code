def is_report_safe(report: list[int]):
    if int(report[0]) - int(report[1]) == 0:
        return False
    else:
        if int(report[1]) - int(report[0]) > 0:
            i = 1
            j = 0
        else:
            i = 0
            j = 1

    while j < len(report) and i < len(report):
        if int(report[i]) - int(report[j]) not in [1, 2, 3]:
            return False
        i += 1
        j += 1
    return True


with open("input.txt", "r") as file:
    data = file.read().splitlines()

safe_reports = 0

for line in data:
    report_data = [int(i) for i in line.split(" ")]

    if is_report_safe(report_data):
        safe_reports += 1
    else:
        for i in range(len(report_data)):  # Completely not optimal but it works for the data quantity
            sliced_report = report_data[::]
            sliced_report.pop(i)
            if is_report_safe(sliced_report):
                safe_reports += 1
                break


print(safe_reports)
