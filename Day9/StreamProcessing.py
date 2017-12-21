# Task 1 and Task 2
score = 0
f = open('input.txt','r')
lst = f.read().strip()
ignore_next = False
garbage = False
nestled = 0
removed = 0
for char in lst:
	if garbage:
		removed += 1
	if not ignore_next:
		if char == "<":
			garbage = True
		elif char == ">":
			garbage = False
			removed -=1
		elif char == "{" and not garbage:
			nestled += 1
		elif char == "}" and not garbage:
			score += nestled
			nestled -= 1
		elif char == "!":
			ignore_next = True
			if garbage:
				removed -= 1
	else:
		ignore_next = False
		if garbage:
			removed -= 1

print ("Task 1: " + str(score))
print ("Task 2: " + str(removed))

