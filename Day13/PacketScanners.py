
dct ={}

with open("input.txt") as f:
    for line in f:
    	line = line.strip()
        lst = [int(x) for x in line.split(':')]
        dct[lst[0]] = lst[-1]

severity = 0
scanner_pos = 0
for key in dct:
	scanner_pos = key % (2*(dct[key]-1))
	if scanner_pos == 0:
		severity += key*dct[key]


print "Task 1: " + str(severity)

delay = 1
caught = False
while not caught:
	delay += 1
	caught = True
	for key in dct:
		scanner_pos = (delay+key) % (2*(dct[key]-1))
		if scanner_pos == 0:
			caught = False
			break
	

print "Task 2: " + str(delay)