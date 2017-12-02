# Day 2 -Checksum
####### Task 1 #######
# The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process
# is on the right track, they need you to calculate the spreadsheet's checksum. For each row, 
# determine the difference between the largest value and the smallest value; the checksum is the 
# sum of all of these differences.
#
# For example, given the following spreadsheet:
#
# 5 1 9 5
# 7 5 3
# 2 4 6 8
# The first row's largest and smallest values are 9 and 1, and their difference is 8.
# The second row's largest and smallest values are 7 and 3, and their difference is 4.
# The third row's difference is 6.
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

# Task 1
checksum = 0
int_list=[]
with open("input.txt") as f:
    for line in f:
        int_list = [int(x) for x in line.split()]
        checksum += max(int_list)-min(int_list)

print "Task 1: " + str(checksum)



####### Task 2 #######
# It sounds like the goal is to find the only two numbers in each row where one evenly 
# divides the other - that is, where the result of the division operation is a whole 
# number. They would like you to find those numbers on each line, divide them, and add 
# up each line's result.
#
# For example, given the following spreadsheet:
#
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
# In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
# In the second row, the two numbers are 9 and 3; the result is 3.
# In the third row, the result is 2.
# In this example, the sum of the results would be 4 + 3 + 2 = 9.

# Task 2
checksum = 0
int_list=[]
with open("input.txt") as f:
    for line in f:
        int_list = [int(x) for x in line.split()]
        for i in range(0,len(int_list)):
        	current_int= int_list[i]
        	# Create a list with the all integers modulus current_int
        	newList = [ j % current_int for j in int_list]
        	# The current_int % current_int will be 0 and place at index i, we do not want to include
        	# this result so we change the value to 1.
        	newList[i] = 1
        	if 0 in newList:
				checksum += int_list[newList.index(0)] / current_int
				break
print "Task 2: " + str(checksum)










