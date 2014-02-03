__author__ = 'Brennan'
import math
import itertools


def get_sum_of_squares(values):
    squares = itertools.imap(math.pow, values, itertools.repeat(2, len(values)))
    return sum(squares)


def get_square_of_sum(values):
    sum_of_values = sum(values)
    return math.pow(sum_of_values, 2)


ceiling = 100
top_of_range = ceiling + 1

square_of_sum = get_square_of_sum(range(1, top_of_range))
sum_of_square = get_sum_of_squares(range(1, top_of_range))
difference = int(square_of_sum - sum_of_square)

print(str(difference))