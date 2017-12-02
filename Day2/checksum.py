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


#f= open('input.txt','r')

checksum = 0
#f = open('input.txt','r')

digits = []
int_list=[]
with open("input.txt") as f:
    for line in f:
        int_list = [int(x) for x in line.split()]
        checksum += max(int_list)-min(int_list)


#for i in range(0,4):
#	line = f.readline().strip()
#	print line
#	line = [line.replace("\t", "','")]
#	print line
#	print max(line)
#	checksum += int(max(line))-int(min(line))

print checksum