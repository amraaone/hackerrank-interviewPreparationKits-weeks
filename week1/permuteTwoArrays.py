def toArrays(k,A,B):
	A.sort()
	B.sort(reverse=True)

	container = [] 

	for i in range(len(A)):
		if A[i] + B[i] < k:
			return 'NO'
	return 'YES'	


print(toArrays(10,[2,1,3],[7,8,9]))
