import math
import itertools

#Naive method.
def getLargestPrimeFactor(number):

	possibleFactors = itertools.count(2)
	squareRootNum = math.sqrt(number)
	
	for num in possibleFactors:
	
		if num > squareRootNum:
			break
		
		if num >= number:
			break
			
		while number / num % 1 == 0:
			if number / num != 1:
				number /= num
				
	return number
	
#print(str(int(getLargestPrimeFactor(9007199254740992))))
print(str(int(getLargestPrimeFactor(600851475143))))