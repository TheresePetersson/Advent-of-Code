
instructions = []
with open("input.txt") as f:
	for line in f:
		ins = line.strip().split(" ")
		instructions.append(ins)


dct = {} # register -> value
current_ind = 0
sound = 0
rec_sound = 0

while current_ind < len(instructions):
	ins = instructions[current_ind]

	if ins[0] == 'snd':
		sound = dct[ins[1]]

	elif ins[0] == 'rcv':
		if ins[1] not in dct:
			dct[ins[1]] == 0
		if dct[ins[1]] != 0 and sound != 0:
			rec_sound = sound
			break

	elif ins[0] == 'set':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] = int(ins[2])
		else:
			if ins[2] not in dct:
				dct[ins[2]] = 0
			dct[ins[1]] = dct[ins[2]]

	elif ins[0] == 'add':
		if ins[2].lstrip('-').isdigit():
			if ins[1] in dct:
				dct[ins[1]] += int(ins[2])
			else:
				dct[ins[1]] = int(ins[2])
		else:
			if ins[2] not in dct:
				dct[ins[2]] = 0
			if ins[1] in dct:
				dct[ins[1]] += dct[ins[2]]
			else:
				dct[ins[1]] = dct[ins[2]]

	elif ins[0] == 'mul':
		if ins[2].lstrip('-').isdigit():
			if ins[1] in dct:
				dct[ins[1]] *= int(ins[2])
			else:
				dct[ins[1]] = 0
		else:
			if ins[2] not in dct:
				dct[ins[2]] = 0
			if ins[1] in dct:
				dct[ins[1]] *= dct[ins[2]]
			else:
				dct[ins[1]] = 0

	elif ins[0] == 'mod':
		if ins[2].lstrip('-').isdigit():
			if ins[1] in dct:
				dct[ins[1]] %= int(ins[2])
			else:
				dct[ins[1]] = 0
		else:
			if ins[2] not in dct:
				dct[ins[2]] = 0
			if ins[1] in dct:
				dct[ins[1]] %= dct[ins[2]]
			else:
				dct[ins[1]] = 0

	elif ins[0] == 'jgz':
		if ins[1].isdigit():
			if int(ins[1]) > 0:
				current_ind += int(ins[2])
		else:
			if ins[1] in dct:
				if dct[ins[1]] > 0:
					if ins[2].lstrip('-').isdigit():
						current_ind += int(ins[2]) - 1
					else:
						if ins[2] not in dct:
							dct[ins[2]] = 0
						current_ind += dct[ins[2]] - 1

			else:
				dct[ins[1]] = 0

	current_ind += 1

print "Task 1: " + str(rec_sound)