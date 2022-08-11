def calculate_hours(file):
	with open(file, 'r') as f:
		data = f.readlines()
	lines = []
	start = []
	end = []
	shift = []
	fire_index = ''
	for line in data[1:]:
		lines.append(line.replace('\n',''))
	for line in lines:
		nums = line.split()
		start.append(int(nums[0]))
		end.append(int(nums[1]))
	for i in range(len(start)):
		shift.append(end[i] - start[i])
	for i in range(len(start)):
		if i != len(start):
			for j in range(i+1, len(start)):
				if start[j] < start[i] and end[j] > start[i]:
					if end[j] > end[i]:
						fire_index = i
						break
				elif start[j] > start[i] and start[j] < end[i]:
					if end[j] < end[i]:
						fire_index = j
						break
			if fire_index != '':
				break
	else:
		for i in range(len(start)):
			if i != len(start):
				for j in range(i+1, len(start)):
					if start[j] < start[i] and end[j] > start[i]:
						fire_index = i
						break
					elif start[j] > start[i] and end[j] < start[i]:
						fire_index = j
						break
				if fire_index != '':
					break
	shift.remove(shift[fire_index])
	max_amount = str(sum(shift))
	with open(f'{file[0]}.out', 'w') as f:
		f.write(max_amount)


for i in range(1,11):
	calculate_hours(f'{i}.in')
