
import random

def switch(step):
	if step == 'S':
		return 'E'
	return 'S'

def updateCoordinate(step, coordinate):
	if step == 'S':
		coordinate[0] += 1
		return
	coordinate[1] += 1

def samePosition(coordA, coordB):
	if (coordA[0] == coordB[0]) and (coordA[1] == coordB[1]):
		return True
	return False 

def change_char(s, p, r):
	return s[:p]+r+s[p+1:]

def finalEntry(lydiaPath):
	return lydiaPath[len(lydiaPath)-1]

def canMoveWithinBounds(myPos, direction, dim):
	if direction == 'E':
		return myPos[1] < dim-1
	return myPos[0] < dim-1
	
def getpath(lydiaPath, n, iter, dim):
	
	# Initial positions
	lydiaPosition = [0,0]
	myPosition = [0,0]

	# Set my path equal to Lydia's path at first 
	myPath = lydiaPath
	
	#Lydia's first step
	lydiaStep = lydiaPath[0]

	# The trick is to draw to the direction so that we end up in the opposite entry
	dominantDirection = finalEntry(lydiaPath)

	for i in range(0, n):
		lydiaStep = lydiaPath[i]
		if samePosition(myPosition, lydiaPosition):
			myStep = switch(lydiaStep)
		elif canMoveWithinBounds(myPosition, dominantDirection, dim):
			myStep = dominantDirection
		else:
			myStep = switch(dominantDirection)

		myPath = change_char(myPath, i, myStep)
		updateCoordinate(myStep, myPosition)
		updateCoordinate(lydiaStep, lydiaPosition)	

	#print("Case #{}: {}".format(iter, myPath))
	return myPath


### For testing ### 

def outside(coord, n):
	if coord[0] >= n or coord[1] >= n:
		return True
	return False

def acceptablePathWeight(myPath):
	s = 0
	e = 0
	for i in range(0, len(myPath)):
		if myPath[i] == 'S':
			s += 1
		else:
			e += 1
	if e == s:
		return True
	return False

def haveSameDirOrOutside(lydiaPath, myPath, length):
	lydiaPosition = [0,0]
	myPosition = [0,0]
	for i in range(0, length-1):
		lydiaStep = lydiaPath[i]
		myStep = myPath[i]
		updateCoordinate(myStep, myPosition)
		updateCoordinate(lydiaStep, lydiaPosition)	
		if outside(myPosition, length) or outside(lydiaPosition, length):
			print("ERROR : Outside")
			return True
		if (samePosition(myPosition, lydiaPosition)):
			if lydiaPath[i+1] == myPath[i+1]:
				return True
		if not acceptablePathWeight(myPath):
			print("Wrong weight")
			return True
def test():
	for dimension in range(2,11):
		d = dimension
		for i in range(0,100000):
			Sstring = "S" * (d-1)
			Estring = "E" * (d-1)
			finalString = Sstring + Estring;
			lydiaPath = ''.join(random.sample(finalString,len(finalString)))
			#print(lydiaPath)
			myPath = getpath(lydiaPath, (2 * (d-1)), 1, d)
	
			if haveSameDirOrOutside(lydiaPath, myPath, (2 * (d-1))):
				print(lydiaPath + ", " + myPath + " " + str(d))
				return False

	return True
#print(test())

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input()) 	 # Read maze dimension
  lydiaPath = input() # Read Lydia's path
  getpath(lydiaPath, (n-1)*2, i, n)