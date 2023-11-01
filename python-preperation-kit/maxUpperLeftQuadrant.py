def max_upper_left_quadrant_sum(matrix):
	n = len(matrix)
	max_sum = 0
	
	for i in range(n // 2):
		for j in range(n//2):
			max_sum += max(matrix[i][j], matrix[i][n-1-j], matrix[n-1-i][j], matrix[n-1-i][n-1-j])

	return max_sum



