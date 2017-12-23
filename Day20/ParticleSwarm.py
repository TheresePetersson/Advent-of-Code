

dct = []


with open('input.txt') as f:
	for line in f:
		[p, v, a] = line.strip().split(', ')
		p, v, a = p[3:-1].split(','), v[3:-1].split(','), a[3:-1].split(',')
		p= [int (x) for x in p]
		a= [int (x) for x in a]
		v= [int (x) for x in v]
		dct_temp = {'p' : p, 'v': v, 'a' : a} 
		dct.append(dct_temp)


for i in range(0,1000):
	# 1000 and 10000 both gives 308 as the closest particle
	collision = []
	collision_2 = []
	for k in range(0,len(dct)):
		part = dct[k]
		# Move the particle
		for j in range(0,3):
			part['v'][j] += part['a'][j]
			part['p'][j] += part['v'][j]

		# Check for collision with already moved particles
		for m in range(0,k):
			part_2 = dct[m]
			if part['p'] == part_2['p']:
				if part['p'] not in collision_2:
					collision.append(m)
					collision_2.append(part['p'])
				collision.append(k)
				break

	index_adjust = 0
	for k in collision:
		dct.pop(k - index_adjust)
		index_adjust += 1



closest_part = -1
closest_distance = 1000000000

for part in dct:
	distance = 0
	for j in range(0,3):
		distance += abs(part['p'][j])
	if distance < closest_distance:
		closest_distance = distance
		closest_part = dct.index(part)

print "Task 1: " + str(308)
print "Task 2: " + str(len(dct))

# 519 to high, 602 (?)
# 500 to low