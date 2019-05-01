

binaryAdjacency = {}
decimalAdjacency = {}

def getAdjacencies(adjmat, stack, i, j, n, m, flip):

	# N
	if i > 0 and adjmat[i - 1][j] == flip:
		stack.append((i-1, j))

	# W
	if j > 0 and adjmat[i][j - 1] == flip: 
		stack.append((i, j - 1))

	# S
	if i < (n - 1) and adjmat[i + 1][j] == flip: 
		stack.append((i+1, j))

	# E
	if j < (m - 1) and adjmat[i][j + 1] == flip:
		stack.append((i, j+1))


def containsLookup(pos, decimal):
	if decimal:
		if pos in decimalAdjacency:
			return True
	else:
		if pos in binaryAdjacency:
			return True
	return False

def adjacencyLookup(pos, decimal):
	if decimal:
		return decimalAdjacency[pos]
	else:
		return binaryAdjacency[pos]

def solve(adjmat, n, m, r, s, rdest, sdest, flip):

	stack = []
	visited = [[False for x in range(m)] for y in range(n)] 
	stack.append((r,s))
	while len(stack) != 0: 
		v = stack[len(stack) - 1]
		i, j = v[0], v[1]
		stack.pop()
		if not visited[i][j]:
			visited[i][j] = True
			if v == (rdest, sdest):
				return True
			if containsLookup(v, flip):
				stack.extend(adjacencyLookup(v, flip))
			else:
				tempStack = []
				getAdjacencies(adjmat, tempStack, v[0], v[1], n, m, flip)
				if adjmat[i][j]:
					decimalAdjacency[(i,j)] = tempStack
				else:
					binaryAdjacency[(i, j)] = tempStack
				stack.extend(tempStack)
				#print(stack)
	
	return False


def readMap(): 
	n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	adjmat = [[0 for x in range(m)] for y in range(n)] 
	for i in range(0, n):
		line = input()  # read a list of integers, 2 in this case
		for j in range(0, len(line)):
			adjmat[i][j] = ((line[j] == '1'))

	cases = input()

	for i in range(0, int(cases)): 
		r, s, rdest, sdest = [int(s) - 1 for s in input().split(" ")]
		if solve(adjmat, n, m, r, s, rdest, sdest, adjmat[r][s]):
			if adjmat[r][s]:
				print("decimal")
			else:
				print("binary")
		else:
			print("neither")


readMap()
#adjmat bools
	#print("Case #{}: {} ".format(i, countRange(n, m)))
