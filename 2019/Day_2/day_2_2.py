import copy
with open("day_2_input.txt", "r") as f:
	a = [int(ship) for ship in  f.read().split(",")]
	save = copy.deepcopy(a)

	for noun in range(len(a)):
		for verb in range(len(a)):
			
			try:
				a = copy.deepcopy(save)
				a[1] = noun
				a[2] = verb

				for index in range(0,len(a),4):
					if a[index] == 1:
						a[a[index+3]] = a[a[index+1]] + a[a[index+2]]
					elif a[index] == 2:
						a[a[index+3]] = a[a[index+1]] * a[a[index+2]]
					elif a[index] == 99:
						break
				
				if a[0] == 19690720:
					print(100*noun+verb)
					
			except:
				pass
				
