# Day 8 - I Heard You Like Registers
# 
####### Task 1 #######
# Each instruction consists of several parts: the register to modify,
# whether to increase or decrease that register's value, the amount 
# by which to increase or decrease it, and a condition. If the condition 
# fails, skip the instruction without modifying the register. 
# The registers all start at 0. The instructions look like this:
#
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
# These instructions would be processed as follows:
#
# Because a starts at 0, it is not greater than 1, and so b is not modified.
# a is increased by 1 (to 1) because b is less than 5 (it is 0).
# c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
# c is increased by -20 (to -10) because c is equal to 10.
# After this process, the largest value in any register is 1.
#
# You might also encounter <= (less than or equal to) or != (not equal to). 
# However, the CPU doesn't have the bandwidth to tell you what all the 
# registers are named, and leaves that to you to determine.

####### Task 2 #######
# To be safe, the CPU also needs to know the highest value held in any register 
# during this process so that it can decide how much memory to allocate to these 
# operations. For example, in the above instructions, the highest value ever held 
# was 10 (in register c after the third instruction was evaluated).

# Task 1 and task 2
largest_value = -1
largest_value_ever = -1
dct_reg = {}
lst_ins = []
with open("input.txt") as f:
    for line in f:
        lst_ins.append([x for x in line.split()])

for lst in lst_ins:
	if not lst[0] in dct_reg:
		dct_reg[lst[0]] = 0
	if not lst[-3] in dct_reg:
		dct_reg[lst[-3]] = 0

	execute = False

	if lst[-2] == ">":
		if dct_reg[lst[-3]] > int(lst[-1]):
			execute = True
	elif lst[-2] == "<":
		if dct_reg[lst[-3]] < int(lst[-1]):
			execute = True
	elif lst[-2] == ">=":
		if dct_reg[lst[-3]] >= int(lst[-1]):
			execute = True
	elif lst[-2] == "<=":
		if dct_reg[lst[-3]] <= int(lst[-1]):
			execute = True
	elif lst[-2] == "==":
		if dct_reg[lst[-3]] == int(lst[-1]):
			execute = True
	else:
		if dct_reg[lst[-3]] != int(lst[-1]):
			execute = True

	if execute:
		if lst[1] == "inc":
			dct_reg[lst[0]] += int(lst[2])
		else:
			dct_reg[lst[0]] -= int(lst[2])

	temp = max(dct_reg.values())
	if temp > largest_value_ever:
		largest_value_ever = temp

largest_value = max(dct_reg.values())

print "Task 1: " + str(largest_value)
print "Task 2: " + str(largest_value_ever)