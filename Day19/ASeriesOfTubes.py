
mat = [] # Matrix, mat[row][coloumn]

with open('input.txt') as f:
	for line in f:
		mat.append(line)


on_going = True
s = ""

SOUTH = 1
NORTH = 2
WEST = 3
EAST = 4
NONE = 0

direction = SOUTH
next_direction = NONE
row = 0
column = 1
count = 0


def end_of_line(direction, row, column):
	if row < 0 or row >= len(mat) or column < 0 or column >= len(mat[0]):
		return True
	if mat[row][column] == '+':
		if direction == SOUTH:
			row += 1
		if direction == NORTH:
			row -= 1
		if direction == WEST:
			column -= 1
		if direction == EAST:
			column += 1
		return end_of_line(direction, row, column)
	elif mat[row][column] == " ":
		return True
	return False


def walking (direction, row, column, s, count):
	if row < 0:
		return [direction, 0, column]
	elif row >= len(mat):
		return [direction, len(mat)-1, column]
	elif column < 0 :
		return [direction, row, 0]
	elif column == len(mat[0]):
		return [direction, row, len(mat[0])]


	if mat[row][column].isalpha():
		s = s + mat[row][column]


	if not end_of_line(direction, row, column):
		count += 1
		if direction == SOUTH:
			row += 1
			return walking (direction, row, column,s, count)
		if direction == NORTH:
			row -= 1
			return walking (direction, row, column,s, count)
		if direction == WEST:
			column -= 1
			return walking (direction, row, column,s, count)
		if direction == EAST:
			column += 1
			return walking (direction, row, column,s, count)

	return [direction, row, column, s, count]

while on_going:
	[direction, row, column,s, count] = walking(direction, row, column,s, count)
	if direction == NORTH or direction == SOUTH:
		# Check west, east
		if mat[row][column+1] != " ":
			direction = EAST
		elif mat[row][column-1] != " ":
			direction = WEST
		if direction == NORTH or direction == SOUTH:
			on_going = False

	else:
		# Check North, south
		if mat[row+1][column] != " ":
			direction = SOUTH
		elif mat[row-1][column] != " ":
			direction = NORTH
		if direction == EAST or direction == WEST:
			on_going = False


print "Task 1: " + s
print "Task 2: " + str(count)



