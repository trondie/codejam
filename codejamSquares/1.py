
import operator 

def checkMultiples(points): 

	leastX = 1000000
	leastY = 1000000
	timesX = 0
	timesY = 0
	iposx = 0
	iposy = 0

	for i in range(0, len(points)):
		if leastX == points[i][0]:
			leastY = points[i][1]
			timesX += 1
			iposx = i
		if leastY == points[i][1]:
			leastX = points[i][0]
			timesY += 1
			iposy = i


	if timesX >= 1: 
		return (0, leastY)
	if timesY >= 1:
		return (leastX, 0)

	return (points[iposx])

def getPoint(xi,yi, direction): 
	x = int(xi)
	y = int(yi)
	if direction == 'N':
		return (x, y + 1)
	if direction == 'S':
		return (x, y - 1)
	if direction == 'W':
		return (x - 1, y)
	if direction == 'E':
		return (x + 1, y)

def getPoints(tripletList): 
	result = []
	for i in range(0, len(tripletList)):
		result.append(tripletList[i])
	return result 

accumulation = {}

def solve():
	cases = input()  # test cases
	for i in range(0, int(cases)):
		accumulation = {}
		people, Q = [int(s) for s in input().split(" ")] # n,m
		for i in range(0, people):
			x, y, direction = [str(s) for s in input().split(" ")] # x, y, direction
			point = getPoint(x, y, direction)
			#triplet = (x,y,direction)
		
			if point in accumulation:
				accumulation[point] += 1
			else:
				accumulation[point] = 1

		bestPoint = max(accumulation.items(), key=operator.itemgetter(1))[0]
		bestStack = []
		bestStack.extend([k for k,v in accumulation.items() if v == accumulation[bestPoint]])
		print(bestStack)
		print(accumulation)
		bestPoints = []
		bestPoints.extend(getPoints(bestStack))
	
		print(checkMultiples(bestPoints))
		
		

solve()



