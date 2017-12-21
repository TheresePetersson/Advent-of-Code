

f = open('input.txt','r')
instructions = f.read().strip().split(",")

programs_start = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
programs = ["".join(programs_start)]
program = programs_start
# FIND A CYCLE!!!
for i in range(1,100):
	for ins in instructions:
		if ins[0] == 's':
			no = int(ins[1:])
			program = program[-no:] + program[:-no]
		
		elif ins[0] == 'x':
			index_1, index_2 = map(int, ins[1:].split("/"))
			program[index_1], program[index_2] = program[index_2], program[index_1]
		
		elif ins[0] == 'p': 
			i_1, i_2 =  ins[1:].split("/")
			index_1 = program.index(i_1)
			index_2 = program.index(i_2)
			program[index_1], program[index_2] = program[index_2], program[index_1]


	if "".join(program) in programs:
		print "Copy found "
		break
	programs.append("".join(program))

result = ""
for x in programs[1]:
	result = result + x

print "Task 1: " + result


result = ""
for x in programs[10000000000 % i]:
	result = result + x

print "Task 2: " + result

