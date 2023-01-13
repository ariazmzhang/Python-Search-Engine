def mult_scalar(matrix, scale):
	matrix_result = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix_result[i][j] = matrix[i][j] * scale
	return matrix_result


def mult_matrix(a, b):
	matrix = [[0 for j in range(len(b[0]))] for i in range(len(a))]
	if len(a[0]) != len(b):
		return None
	else:
		for i in range(len(a)):
				for j in range(len(b[0])):
					for k in range(len(b)):
						matrix[i][j] += a[i][k] * b[k][j]
		for i in range(len(a)):
			for j in range(len(b[0])):
				return matrix

import math
def euclidean_dist(a,b):
	sum = 0
	dist = 0
	for i in range(len(a[0])):
		sum += (a[0][i] - b[0][i]) ** 2
		dist = math.sqrt(sum)
	return dist
