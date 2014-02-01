
def sumFibonnacis(ceiling):
	
	sum = 0;
	fib1 = 1;
	fib2 = 2;
	
	while fib2 < ceiling:

		sum += fib1 if fib1 % 2 == 0 else 0;
		sum += fib2 if fib2 % 2 == 0 else 0;
		
		fib1 = fib1 + fib2
		fib2 = fib1 + fib2
	
	print(sum)
	
sumFibonnacis(4000000)
