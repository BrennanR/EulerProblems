def sum_fibonnacis(ceiling):
    sum_of_fibs = 0
    fib1 = 1
    fib2 = 2

    while fib2 < ceiling:
        sum_of_fibs += fib1 if fib1 % 2 == 0 else 0
        sum_of_fibs += fib2 if fib2 % 2 == 0 else 0

        fib1 += fib2
        fib2 += fib1

    print(sum_of_fibs)


sum_fibonnacis(4000000)
