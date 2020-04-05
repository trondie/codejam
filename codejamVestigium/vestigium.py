import numpy as np

def isLatinRow(X : np.ndarray, rowIndex):
	row = X[rowIndex]
	for i in range(0, len(row) - 1):
		if np.any(row[i + 1:] == row[i]):
			return False
	return True
		
def isLatinCol(X : np.ndarray, colIndex):
	col = X[:,colIndex]
	for i in range(0, len(col) - 1):
		if np.any(col[i + 1:] == col[i]):
			return False
	return True

def countLatinNN(N : np.ndarray):
	r,c = 0, 0
	for i in range(0, N.shape[0]):
		index = i
		if not isLatinRow(N, index):
			r += 1
		if not isLatinCol(N, index):
			c += 1

	ret = str(N.trace()) +  " " + str(r) + " " + str(c)
	return ret


t = int(input())  # read a line with a single integer
for i in range(1, t + 1): # test cases
  n = int(input()) 	# Read N 
  mat = []
  for i in range(0, n):
      mat.append(np.fromstring(input(), dtype=int, sep=' '))
  mat = np.asarray(mat)
  print("Case #"+str(i)+": " + countLatinNN(mat))