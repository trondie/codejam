
# Algorithmic outline of solution

# For each digit, starting from the last digit, go from right to left, starting from k = 0 to k = n 
# Set all digits in number from position k = s to k = 0 to zero
# If digit is a 4, subtract 10^k from number. Store subtracted number and resulting number separately

# Number #1 : Take the original number, and subtract each of the accumulated subtrahends from the number
# Number #2 : Add all subtrahends


def getSubtrahend(k):
	#magic
	return 10**k
	
def identify(numParameter):

	num = numParameter
	
	# A to return (the minuend)
	A = -1
	# B to return (subtrahends)
	B = -1

	subtrahends = []

	k = 0
	referenceNum = num
	while num >= 1: 
		remainder = num % 10
		referenceNum -= remainder
		if remainder == 4:
			subtrahends.append(getSubtrahend(k))
		num = int(num / 10)
		k += 1

	B = sum(subtrahends)
	A = numParameter - B

	return [A,B]

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n = int(input()) 	 # read a list of integers, 2 in this case
  answer = identify(n)
  print("Case #{}: {} {}".format(i, answer[0], answer[1]))
  # check out .format's specification for more formatting options