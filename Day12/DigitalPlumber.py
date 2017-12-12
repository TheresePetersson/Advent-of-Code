dct = {}
dct_group = {}
in_group_already = []

def add_to_group(prog, group):
	if prog not in dct_group[group] and prog not in in_group_already:
		dct_group[group].append(prog)
		in_group_already.append(prog)
		for p in dct[prog]:
			add_to_group(p, group)

# Read input file
with open("input.txt") as f:
    for line in f:
    	line = line.strip()
    	key = int(line.split("<->")[0])
    	value = line.split("<->")[1].split(',')
    	value = [int(x) for x in value]
        dct[key] = value

# Task 1 and 2
for key in dct:
	if key not in in_group_already and key not in dct_group:
		dct_group[key] = []
		in_group_already.append(key)
		for p in dct[key]:
			add_to_group(p,key)


no_of_prog = len(dct_group[0]) + 1
no_of_group = len(dct_group)


print "Task 1: " + str(no_of_prog)
print "Task 2: " + str(no_of_group)