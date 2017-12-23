import math
import numpy.matlib 
import numpy as np
rules = {} # string of input map to vector of output

with open('input.txt') as f:
	for line in f:
		l = line.strip().split(' => ')
		inp = l[0]
		outp = l[1].split('/')
		rules[inp] = outp


mat = np.chararray((1,3))
print mat
t= ['.#.','..#','###']


for i in range(0,1):
	#size = math.sqrt(len(mat.replace('/','')))
	size = math.sqrt(len(mat))
	new_mat = ""

	if  size % 3 == 0:
		# split into 3x3
		pass
	else:
		# split into 2x2 
		k = 0
		for j in range(0,len(mat), 2):


			#temp = mat[j] + mat[j+1] + mat[j+size] + mat[j + size +1]

			temp_2 = rules[temp]

			new_mat = new_mat + temp_2

	mat = new_mat