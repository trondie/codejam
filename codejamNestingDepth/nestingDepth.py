def addOpenParenthesis(delta):
	newString = ""
	for i in range(0, delta):
		newString += '('
	return newString

def addCloseParenthesis(delta):
	newString = ""
	for i in range(0, -delta):
		newString += ')'
	return newString

def parseSequence(seq): 
	newString = ""
	currentDepth = 0
	for i in range(0, len(seq)):
		num = int(seq[i])
		delta = num - currentDepth
		if num > currentDepth:
			newString += addOpenParenthesis(delta)
		elif num < currentDepth:
			newString += addCloseParenthesis(delta)
		#elif i > 0 and num != 0:
			#newString += ")("

		newString += seq[i]
		currentDepth = num
		if i == len(seq) - 1 and currentDepth > 0:
		    newString += addCloseParenthesis(-currentDepth)
	return newString
	


print(parseSequence("51111121020"))