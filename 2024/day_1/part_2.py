def count_number_from_index(my_list, index):
    i = 0
    list_length = len(my_list)
    while index+i < list_length and my_list[index+i] == my_list[index]:
        i += 1
    return i

with open("input.txt", "r") as file:
    data = file.read().splitlines()

left_list = []
right_list = []
for line in data:
    left, right = line.split("   ")
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()
similarity_score = 0

while left_list and right_list:
    right_index = 0
    while right_list:
        if left_list[0] == right_list[right_index]:
            presence_in_right_list = count_number_from_index(right_list, right_index)
            presence_in_left_list = count_number_from_index(left_list, 0)
            similarity_score += left_list[0] * presence_in_right_list * presence_in_left_list
            left_list = left_list[presence_in_left_list:] if presence_in_left_list < len(left_list) else []
            right_list = right_list[right_index+presence_in_right_list:] if right_index+presence_in_right_list < len(right_list) else []
            break
        elif left_list[0] > right_list[right_index]:
            right_index += 1
            if right_index >= len(right_list):
                right_list = []
                left_list = []
        else:
            presence_in_left_list = count_number_from_index(left_list, 0)
            left_list = left_list[presence_in_left_list:] if presence_in_left_list < len(left_list) else []
            if right_index:
                right_list = right_list[right_index:] if right_index < len(right_list) else []
            break

print(similarity_score)
