
instructions = []
with open("input.txt") as f:
	for line in f:
		ins = line.strip().split(" ")
		instructions.append(ins)


dct = {'p': 0, 'a' : 0, 'i' : 0, 'b' : 0, 'f' : 0} 
current_ind = 0
sound = 0
rec_sound = 0

while current_ind < len(instructions):
	ins = instructions[current_ind]

	if ins[0] == 'snd':
		sound = dct[ins[1]]

	elif ins[0] == 'rcv':
		if dct[ins[1]] != 0 and sound != 0:
			rec_sound = sound
			break

	elif ins[0] == 'set':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] = int(ins[2])
		else:
			dct[ins[1]] = dct[ins[2]]

	elif ins[0] == 'add':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] += int(ins[2])
		else:
				dct[ins[1]] += dct[ins[2]]


	elif ins[0] == 'mul':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] *= int(ins[2])
		else:
			dct[ins[1]] *= dct[ins[2]]

	elif ins[0] == 'mod':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] %= int(ins[2])
		else:
			dct[ins[1]] %= dct[ins[2]]

	elif ins[0] == 'jgz':
		if ins[1].isdigit():
			if int(ins[1]) > 0:
				current_ind += int(ins[2])
		else:
			if dct[ins[1]] > 0:
				if ins[2].lstrip('-').isdigit():
					current_ind += int(ins[2]) - 1
				else:
					current_ind += dct[ins[2]] - 1

	current_ind += 1

print "Task 1: " + str(rec_sound)



# TASK 2

prog_A = {"dict" : {'p': 0, 'a' : 0, 'i' : 0, 'b' : 0, 'f' : 0}, "index": 0, "queue" : [], "wait" : False  }
prog_B = {"dict" : {'p': 1, 'a' : 0, 'i' : 0, 'b' : 0, 'f' : 0}, "index": 0, "queue" : [], "wait" : False }

prog = 0
prog_next = 1
count = 0

while (prog_A["index"] < len(instructions) or progA["index"] < 0) and (prog_B["index"] < len(instructions) or prog_B["index"] <0 ):
	
	if prog == 0:
		dct = prog_A["dict"]
		current_ind = prog_A["index"]
		queue_rec = prog_A["queue"]
		queue_send = []
		wait = prog_A["wait"]
	else:
		dct = prog_B["dict"]
		current_ind = prog_B["index"]
		queue_rec = prog_B["queue"]
		queue_send = []
		wait = prog_B["wait"]

	ins = instructions[current_ind]

	if ins[0] == 'snd':
		queue_send.append(dct[ins[1]])
		if prog == 1:
			count += 1

	elif ins[0] == 'rcv':
		if len(queue_rec) == 0:
			if prog_A["wait"] and prog_B["wait"]:
				print "DEADLOCK"
				break
			else:
				wait = True
		else:
			dct[ins[1]] = queue_rec.pop(0)


	elif ins[0] == 'set':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] = int(ins[2])
		else:
			dct[ins[1]] = dct[ins[2]]

	elif ins[0] == 'add':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] += int(ins[2])
		else:
			dct[ins[1]] += dct[ins[2]]

	elif ins[0] == 'mul':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] *= int(ins[2])
		else:
			dct[ins[1]] *= dct[ins[2]]

	elif ins[0] == 'mod':
		if ins[2].lstrip('-').isdigit():
			dct[ins[1]] %= int(ins[2])
		else:
			dct[ins[1]] %= dct[ins[2]]

	elif ins[0] == 'jgz':
		if ins[1].lstrip('-').isdigit():
			if int(ins[1]) > 0:
				current_ind += int(ins[2]) - 1
		else:
			if dct[ins[1]] > 0:
				if ins[2].lstrip('-').isdigit():
					current_ind += int(ins[2]) - 1
				else:
					current_ind += dct[ins[2]] - 1

	current_ind += 1

	if wait or current_ind >= len(instructions):
		prog_next = (prog + 1) % 2

	if prog == 0:
		prog_A["dict"] = dct
		prog_A["index"] = current_ind
		prog_A["queue"] = queue_rec
		prog_A["wait"] = wait

		prog_B["queue"].extend(queue_send)
		if len(queue_send) != 0 and prog_B["wait"] and prog_B["index"] < len(instructions):
			prog_B["wait"] = False
			prog_B["dict"][instructions[prog_B["index"]-1][1]] = prog_B["queue"].pop(0) 
	else:
		prog_B["dict"] = dct
		prog_B["index"] = current_ind
		prog_B["queue"] = queue_rec
		prog_B["wait"] = wait

		prog_A["queue"].extend(queue_send) 
		if len(queue_send) != 0 and prog_A["wait"] and prog_A["index"] < len(instructions):
			prog_A["wait"] = False
			prog_A["dict"][instructions[prog_A["index"]-1][1]] = prog_A["queue"].pop(0) 

	prog = prog_next


print "Task 2: " + str(count)


