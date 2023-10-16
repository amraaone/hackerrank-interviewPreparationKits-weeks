def diagonalDifference(arr):
	n = len(arr)
	
	diagonal1 = 0
	diagonal2 = 0

	for i in range(n):
		diagonal1 += arr[i][i]
		diagonal2 += arr[i][n-1-i]
	
	return abs(diagonal1 - diagonal2)
	
	

diagonalDifference([[11,2,4],[4,5,6],[10,8,-12]])
