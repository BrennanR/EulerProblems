def sum_threes_and_fives(ceiling):
    sum_of_threes_and_fives = 0

    for num in range(ceiling):
        if num % 3 == 0:
            sum_of_threes_and_fives += num
        elif num % 5 == 0:
            sum_of_threes_and_fives += num

    print(sum_of_threes_and_fives)


sum_threes_and_fives(1000)