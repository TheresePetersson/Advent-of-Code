# Task 1

def knot_has(s):
	lst = range (0,256)
	instructions = [ord(e) for e in s]
	instructions.extend([17, 31, 73, 47, 23])
	current_pos = 0
	skip_size = 0

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

	hex_string =""
	for e in xor_lst:
		if len(hex(e)) > 3:
			hex_string += hex(e)[2:]
		else:
			hex_string += ('0' + hex(e)[2:])

	return hex_string


key = "oundnydw-"
used_squares = 0
regions = 0
removed_regions = 0
region_lst = [0]*128
for j in range(0,128):
	temp_reg = [0]*128
	int_lst = knot_has(key + str(j))
	temp = bin(int(int_lst, 16))[2:]
	for i in range(0,len(temp)):
		if temp[i] == "1":
			used_squares += 1
			if i != 0:
				if region_lst[i] != 0 and temp_reg[i-1] == 0:
					temp_reg[i] = region_lst[i]
				elif temp_reg[i-1] != 0 and region_lst[i] == 0:
					temp_reg[i] = temp_reg[i-1]
				elif temp_reg[i-1] == 0 and region_lst[i] == 0:
					regions += 1
					temp_reg[i] = regions
					
				else:
					min_val = min(region_lst[i],temp_reg[i-1])
					temp_reg[i] = min_val
					if temp_reg[i-1] != region_lst[i]:
						for j in range(0,i-1):
							if temp_reg[j] == temp_reg[i-1]:
								temp_reg[j]= min_val
						for j in range(i+1,128):
							if region_lst[j] == region_lst[i]:
								region_lst[j] = min_val
						removed_regions += 1
						temp_reg[i-1] = min_val
						region_lst[i] = min_val
			else:
				if region_lst[i] != 0:
					temp_reg[i] = region_lst[i]
				else:
					regions += 1
					temp_reg[i] = regions
					


	region_lst = temp_reg


print "Task 1: " + str(used_squares)

print removed_regions
print "task 2: " + str(regions - removed_regions)
	