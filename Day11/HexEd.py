# Task 1

f = open('input.txt','r')
steps = f.read().strip().split(",")

north = 0
east = 0
max_step = 0

for step in steps:
	if "n" in step:
		north +=1
	elif "s" in step:
		north -=1
	if "e" in step:
		east += 1
	elif "w" in step:
		east -=1
	no_step = max(abs(north),abs(east))
	max_step = max(max_step,no_step)


no_step = max(abs(north),abs(east))
print "Task 1: " + str(no_step)
print "Task 2: " + str(max_step)
