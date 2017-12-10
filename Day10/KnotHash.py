
from functools import reduce


# Task 1
lst = range (0,256)
f = open('input.txt','r')
instructions = f.read().strip().split(",")
instructions = [int(e) for e in instructions]

current_pos = 0
skip_size = 0

for ins in instructions:
	if ins <= len(lst):
		if (current_pos + ins) < len(lst):
			temp = lst[current_pos:(current_pos+ins)]
			temp.reverse()
			lst[current_pos:(current_pos+ins)] = temp
		else:
			temp = lst[current_pos:]
			len_temp = len(temp)
			ending = ins - len_temp
			temp.extend(lst[0:ending])
			temp.reverse()
			lst[current_pos:]=temp[0:len_temp]
			lst[0:ending] = temp[len_temp:]

		current_pos += (ins + skip_size)
		current_pos = current_pos % len(lst)
		skip_size += 1

mult = lst[0]*lst[1]

print "Task 1: " + str(mult)


# Task 2
lst = range (0,256)
f = open('input.txt','r')
instructions = f.read().strip()
instructions = [ord(e) for e in instructions]

instructions.extend([17, 31, 73, 47, 23])

current_pos = 0
skip_size = 0
print instructions

for i in range(0,64):
	for ins in instructions:
		if ins <= len(lst):
			if (current_pos + ins) < len(lst):
				temp = lst[current_pos:(current_pos+ins)]
				temp.reverse()
				lst[current_pos:(current_pos+ins)] = temp
			else:
				temp = lst[current_pos:]
				len_temp = len(temp)
				ending = ins - len_temp
				temp.extend(lst[0:ending])
				temp.reverse()
				lst[current_pos:]=temp[0:len_temp]
				lst[0:ending] = temp[len_temp:]

		current_pos += (ins + skip_size)
		current_pos = current_pos % len(lst)
		skip_size += 1

# Time for XOR
xor_lst = []

for i in range(0,16):
	start_index = i*16
	xor = reduce((lambda x,y: x ^ y), lst[start_index:start_index+16])
	xor_lst.extend([xor])
print xor_lst

hex_string =""
for e in xor_lst:
	if len(hex(e)) > 3:
		hex_string += hex(e)[2:]
	else:
		hex_string += ('0' + hex(e)[2:])


print "Task 2: " + hex_string