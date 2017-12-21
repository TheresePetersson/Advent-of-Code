steps = 376
current_pos = 0
lst = [0]

for i in range(1, 2018):
	current_pos = (current_pos + steps) % len(lst)
	current_pos += 1
	if current_pos == len(lst):
		lst.append(i)
	else:
		lst.insert(current_pos, i)

value = lst[current_pos + 1]
print "Task 1: " + str(value)

lst = [0]
current_pos = 0
i= 1

while i <= 50000000 :
	current_pos = (current_pos + steps) % i
	current_pos += 1
	if current_pos == 1:
		lst.insert(current_pos,i)

	rest = i - current_pos
	if rest >= steps:
		no = rest/steps
		while (current_pos + no*(steps + 1)) >= i:
			no -=1
		current_pos += (no)*(steps + 1)
		i += no

	i += 1


value = lst[1]

print "Task 2: " + str(value)

