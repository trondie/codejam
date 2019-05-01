
def divByNine(num):
	return (num % 9) == 0

def containsNine(num):
	number = str(num)
	for i in range(0, len(number)):
		digit = number[i]
		if digit == '9':
			return True
	return False

def countRange(start, end): 
	count = 0
	for i in range(start, end +1):
		if containsNine(i) or divByNine(i):
			continue 
		count = count + 1
	return count

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
	n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
	print("Case #{}: {} ".format(i, countRange(n, m)))
