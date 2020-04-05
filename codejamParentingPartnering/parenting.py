import numpy as np 
import operator

def startpoint(R):
	return R[0]

def endpoint(R):
	return R[1]

def updateResource(resource, activity):
	resource[0] = activity[0]
	resource[1] = activity[1]

def activitySelection(sf):

	'''
	Performs activity selections shared between two resources 
	'''	

	# Sort wrt increasing endtime
	sf = sorted(sf, key=lambda t: t[1])

	# set of activities that can be performed, divided between two sets
	S1 = [] 
	S2 = [] 

	# Resource 1, to hold our sentinels, initialized to negative
	R1 = [-1, -1] 
	R2 = [-1, -1]

	# Go through all activites and divided them. Greedy approach.
	for i in range(0, len(sf)):
		if sf[i][0] < endpoint(R1) and sf[i][0] < endpoint(R2):
			continue
		if endpoint(R1) >= endpoint(R2):
			if endpoint(R1) <= startpoint(sf[i]):
				updateResource(R1, sf[i])
				S1.append(sf[i])
			else:
				if endpoint(R2) <= startpoint(sf[i]):
					updateResource(R2, sf[i])
					S2.append(sf[i])
		
		elif endpoint(R2) <= startpoint(sf[i]):
			updateResource(R2, sf[i])
			S2.append(sf[i])
		elif endpoint(R1) <= startpoint(sf[i]):
			updateResource(R1, sf[i])
			S1.append(sf[i])

	return S1, S2


def schedule(sf):
	
	# Assign to "J" and "C", like "Jamie" and "Cameron" in the problem statement.
	J, C = activitySelection(sf)

	if len(J) + len(C) < len(sf):
		return "IMPOSSIBLE"
	for i in range(0, len(J)):
		J[i] = (J[i][0], J[i][1], J[i][2], "J") # Let´s mark each tuple with a new one
	for i in range(0, len(C)):
		C[i] = (C[i][0], C[i][1], C[i][2], "C")

	# Concatenate the lists. Important, because we need to go in an order (we have the indices)
	JC = J + C 

	# Sort on the index it was added so that we get the right order
	JC = sorted(JC, key=lambda t: t[2]) 

	# We return the string sequence and map only to the last tuple string : "J" or "C" 
	return ''.join(map(str, map(lambda x : x[3], JC)))




t = int(input())  # read a line with a single integer
for i in range(1, t + 1): # test cases
  sf = []
  n = int(input()) 	# Read N 
  for j in range(0, n):
      row = np.fromstring(input(), dtype=int, sep=' ')
      sf.append((row[0], row[1], j))
  print("Case #"+str(i)+": " + schedule(sf))