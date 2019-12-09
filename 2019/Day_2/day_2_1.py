with open("day_2_input.txt", "r") as f:
	a = [int(ship) for ship in  f.read().split(",")]
	for index in range(0,len(a),4):
		if a[index] == 1:
			a[a[index+3]] = a[a[index+1]] + a[a[index+2]]
		elif a[index] == 2:
			a[a[index+3]] = a[a[index+1]] * a[a[index+2]]
		elif a[index] == 99:
			break
	print(a[0])