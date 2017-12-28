

ports = {0:[0]}

with open('input.txt') as f:
	for line in f:
		l = line.strip().split('/')
		l1 = int(l[0])
		l2 = int(l[1])
		if l1 in ports:
			ports[l1].append(l2)
		else:
			ports[l1] = [l2]
		if l1 != l2:
			if l2 in ports:
				ports[l2].append(l1)
			else:
				ports[l2] = [l1]




def generate_bridges(current_port, bridges):
	temp = list(bridges[-1])
	for port in ports[current_port]:
		if (current_port, port) in temp or (port, current_port) in temp:
			pass
		else:
			bridges[-1].append((current_port, port))
			bridges = generate_bridges(port, bridges)
			bridges.append(list(temp))

	return bridges


bridges = [[(0,0)]]

bridge = generate_bridges(0, bridges)

result = []
for bri in bridge:
	result.append((len(bri), sum(a+b for a,b in bri)))

res1 = sorted(result, key = lambda x: x[1])[-1][1]
res2 = sorted(result)[-1][1]

print "Task 1: " + str(res1)
print "Task 2: " + str(res2)

# 1772 to low