
def matrixMult(A, B):
	if len(A) != len(B[0]):	#incompatible multiplication
		return

	product = [[0 for row in range(len(A))],[0 for col in range(len(B[0]))]]

	for x in range(len(A)):	#iterating over rows of A
		for y in range(len(B[0])):
			for z in range(len(B)):
				product[x][y] += A[x][z] * B[z][y]

	return product




A = [ [1,3,5], 
	  [2,4,6] ]	# a 2x3 Matrix
B = [ [10,3],
	  [6,7], 
	  [4,9] ]	# a 3x2 Matrix


print(matrixMult(A,B))



