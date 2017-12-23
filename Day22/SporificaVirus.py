

mat = []
# Variables for padding the matrix
size = 475
padding = (size-25)/2

for i in range(0,padding):
	mat.append(['.']*size)


with open('input.txt') as f:
	for line in f:
		line = line.strip()
		temp =['.']*padding
		for c in line:
			temp.append(c)
		temp.extend(['.']*padding)
		mat.append(temp)

for i in range(0,padding):
	mat.append(['.']*size)

def change_direction(direction, right, flag):
	if direction == 'NORTH':
		if flag:
			return 'SOUTH'

		if right:
			return 'EAST'
		else:
			return 'WEST'
	elif direction == 'SOUTH':
		if flag:
			return 'NORTH'

		if right:
			return 'WEST'
		else:
			return 'EAST'
	elif direction == 'EAST':
		if flag:
			return 'WEST'

		if right:
			return 'SOUTH'
		else:
			return 'NORTH'
	elif direction == 'WEST':
		if flag:
			return 'EAST'
		if right:
			return 'NORTH'
		else:
			return 'SOUTH'

def new_pos(pos, direction):
	if direction == 'NORTH':
		if (pos['row'] -1) >= 0:
			pos['row'] -= 1
		else:
			print "North out of index"

	elif direction == 'SOUTH':
		if (pos['row'] +1) < len(mat):
			pos['row'] += 1
		else:
			print "South out of index"

	elif direction == 'EAST':
		if (pos['col'] +1) < len(mat[0]):
			pos['col'] += 1
		else:
			print "East out of index"

	elif direction == 'WEST':
		if (pos['col'] - 1) >= 0:
			pos['col'] -= 1
		else:
			print "West out of index"
	
	return pos


pos = {'row' : len(mat)/2, 'col' : len(mat[0])/2 }
direction = 'NORTH'

count = 0

for i in range(0,10000):

	if mat[pos['row']][pos['col']] == '.':
		# cleaned node
		direction = change_direction(direction,False, False)
		# infect the node
		mat[pos['row']][pos['col']] = '#'
		count += 1

	else:
		# infected node
		direction = change_direction(direction, True, False)
		# clean the node
		mat[pos['row']][pos['col']] = '.'

	pos = new_pos(pos,direction)



print "Task 1: " + str(count)

# Task 2

mat = []
# Variables for padding the matrix
size = 475
padding = (size-25)/2

for i in range(0,padding):
	mat.append(['.']*size)


with open('input.txt') as f:
	for line in f:
		line = line.strip()
		temp =['.']*padding
		for c in line:
			temp.append(c)
		temp.extend(['.']*padding)
		mat.append(temp)

for i in range(0,padding):
	mat.append(['.']*size)


pos = {'row' : len(mat)/2, 'col' : len(mat[0])/2 }
direction = 'NORTH'

count = 0


for i in range(0,10000000):

	if mat[pos['row']][pos['col']] == '.':
		# cleaned node
		direction = change_direction(direction,False, False)
		# weaken the node
		mat[pos['row']][pos['col']] = 'W'

	elif mat[pos['row']][pos['col']] == '#':
		# infected node
		direction = change_direction(direction, True, False)
		# flag the node
		mat[pos['row']][pos['col']] = 'F'

	elif mat[pos['row']][pos['col']] == 'F':
		# flaged node
		direction = change_direction(direction, False, True)
		# clean the node
		mat[pos['row']][pos['col']] = '.'
	else:
		# weakened node
		# no direction change
		# infect the node
		mat[pos['row']][pos['col']] = '#'
		count += 1

	pos = new_pos(pos,direction)

print "Task 2: " + str(count)
