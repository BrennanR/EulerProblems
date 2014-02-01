
def sumThreesAndFives(ceiling):

	sum = 0
	
	for num in range(ceiling):
		if num % 3 == 0:
			sum += num
		elif num % 5 == 0:
			sum += num
	
	print(sum)
	
sumThreesAndFives(1000)