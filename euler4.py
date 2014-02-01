import itertools

def isNumberPalindrome(number):
	numberString = str(number)
	strLen = len(numberString)
	x = strLen - 1
	
	for i in itertools.count():
		if numberString[i] != numberString[x]:
			return False
		if i >= x:
			break
		
		x -= 1
	
	return True
	
def findLargestThreeDigitPalindrome():

	largestPalindrome = 0
	threeDigitValues = range(100,999)

	for threeDigitValue in threeDigitValues:
		for threeDigitValue2 in reversed(threeDigitValues):
			if isNumberPalindrome(threeDigitValue * threeDigitValue2):
				if threeDigitValue * threeDigitValue2 > largestPalindrome:
					largestPalindrome = threeDigitValue * threeDigitValue2
					
	return largestPalindrome
	
print(str(findLargestThreeDigitPalindrome()))