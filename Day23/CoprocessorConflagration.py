

instructions = []
with open("input.txt") as f:
	for line in f:
		ins = line.strip().split(" ")
		instructions.append(ins)


dct = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0} 
current_ind = 0
count = 0

while current_ind < len(instructions) and current_ind >= 0:
	ins = instructions[current_ind]

	if ins[0] == 'set':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] = int(ins[2])
		else:
			dct[ins[1]] = dct[ins[2]]

	elif ins[0] == 'sub':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] -= int(ins[2])
		else:
			dct[ins[1]] -= dct[ins[2]]

	elif ins[0] == 'mul':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] *= int(ins[2])
		else:
			dct[ins[1]] *= dct[ins[2]]
		count += 1

	elif ins[0] == 'jnz':
		if ins[1].isdigit():
			if int(ins[1]) != 0:
				current_ind += int(ins[2]) -1
		else:
			if dct[ins[1]] != 0:
				if ins[2].lstrip('-').isdigit():
					current_ind += int(ins[2])
				else:
					current_ind += dct[ins[2]]
				current_ind -= 1


	current_ind += 1


print "Task 1: " + str(count)


# Task 2

h = 0
# b takes a value in between the limits
lower_limit = 57*100 + 100000
upper_limit = 122700 +1

# Check if "b" is composite, if yes, h will be increased with one (sub -1)
for x in range(lower_limit, upper_limit, 17):
	for i in range(2,x):
		if x % i == 0:
			h += 1
			break


print "Task 2: " + str(h)