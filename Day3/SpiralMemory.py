# Day 3 - Spiral Memory 
#
# Task 1
# Each square on the grid is allocated in a spiral pattern starting at a location
# marked 1 and then counting up while spiraling outward. For example, the first 
# few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
# While this is very space-efficient (no squares are skipped), requested data must 
# be carried back to square 1 (the location of the only access port for this memory
# system) by programs that can only move up, down, left, or right. They always 
# take the shortest path: the Manhattan Distance between the location of the data and square 1.
#
# For example:
#
# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.

import math
import numpy

num = 325489

# Task 1
sqrtNum = math.sqrt(num)
if sqrtNum % 1 != 0:
	sqrtNum = int(sqrtNum)
	# Choose the next odd number
	if sqrtNum % 2 == 0:
		sqrtNum += 1
	else:
		sqrtNum += 2
	# create all possible distances to the root
	distancesAscending = range((sqrtNum-1)/2, sqrtNum-1)	
	distances = range((sqrtNum-1)/2+1, sqrtNum)
	distances.reverse()
	distances.extend(distancesAscending)
	# Calculate the distance from the maximum number in the current square
	dist = (sqrtNum*sqrtNum) - num
	dist = dist % (len(distances))
	print "Distance: " + str(distances[dist])
else:
	dist = int(sqrtNum-1)
	print "Distance: " +  str(dist)


# Task 2
# As a stress test on the system, the programs here clear the grid and then 
# store the value 1 in square 1. Then, in the same allocation order as shown
# above, they store the sum of the values in all adjacent squares, including diagonals.
#
# So, the first few squares' values are chosen as follows:
#
# Square 1 starts with the value 1.
# Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
# Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
# Square 4 has all three of the aforementioned squares as neighbors and stores the sum of 
# their values, 4.
# Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
# Once a square is written, its value does not change. Therefore, the first few squares 
# would receive the following values:
#
# 147  142  133  122   59
# 304    5    4    2   57
# 330   10    1    1   54
# 351   11   23   25   26
# 362  747  806--->   ...

# Task 2
def sum_all_neighbours(x_cord, j_cord, matrix):
	value = 0
	value += matrix[x_cord-1][y_cord]
	value += matrix[x_cord][y_cord-1]
	value += matrix[x_cord-1][y_cord-1]
	value += matrix[x_cord+1][y_cord]
	value += matrix[x_cord][y_cord+1]
	value += matrix[x_cord+1][y_cord+1]
	value += matrix[x_cord+1][y_cord-1]
	value += matrix[x_cord-1][y_cord+1]
	return value

# Unnecessary to generate a to large matrix 
sqrtNum /=2
matrix = numpy.zeros((sqrtNum, sqrtNum))
start_index = sqrtNum/2
matrix[start_index][start_index] = 1
value = 0
y_cord = start_index 
x_cord = start_index + 1
# NORTH = 1, WEST = 2, SOUTH = 3, EAST = 4 
direction =  4
while value < num:
	value = sum_all_neighbours(x_cord, y_cord, matrix)
	matrix[x_cord][y_cord] = value
	if direction == 1:
		# Turn west if the element is free in matrix otherwise keep going north
		if matrix[x_cord-1,y_cord] == 0:
			x_cord -= 1
			direction = 2
		else:
			y_cord -= 1
	elif direction == 2:
		# Turn south if the element is free in matrix otherwise keep going west
		if matrix[x_cord,y_cord+1] == 0:
			y_cord += 1
			direction = 3
		else:
			x_cord -= 1
	elif direction == 3:
		# Turn east if the element is free in matrix otherwise keep going south
		if matrix[x_cord+1,y_cord] == 0:
			x_cord += 1
			direction = 4
		else:
			y_cord += 1
	else:
		# Turn north if the element is free in matrix otherwise keep going east
		if matrix[x_cord,y_cord-1] == 0:
			y_cord -= 1
			direction = 1
		else:
			x_cord += 1

print "Task 2: " + str(value)



