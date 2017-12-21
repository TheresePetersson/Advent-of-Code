

factor_A = 16807
factor_B = 48271

divider = 2147483647
i = 0
f = open('input.txt','r')
for line in f:
	if i == 0:
		start_value_a = line.strip()[-3::]
		i += 1
	else:
		start_value_b = line.strip()[-3::]

start_value_a = 591
start_value_b = 393

value_a = int(start_value_a)
value_b = int(start_value_b)
count = 0

for i in range(0,40000000) : #40000000):
	value_a = (value_a * factor_A) % divider
	value_b = (value_b * factor_B) % divider

	bit_a = bin(value_a)[-16:]
	bit_b = bin(value_b)[-16:]
	if bit_b == bit_a:
		count += 1


print "Task 1: " + str(count)