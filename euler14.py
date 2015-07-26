
import itertools


even = lambda x: x/2
odd = lambda x: 3*x + 1


def next_collatz_sequence_value(x):
    if x % 2 == 0:
        return even(x)
    else:
        return odd(x)


def length_of_sequence_for_value(x):
    length = 2  # One for our starting number and one for the last one, which we don't iterate over.
    next_value = next_collatz_sequence_value(x)
    while next_value != 1:
        length += 1
        next_value = next_collatz_sequence_value(next_value)
    return length


def longest_sequence_under_one_million():
    max_length = 0
    max_length_number = 0
    for i in itertools.count(1):
        if i < 1000000:
            length = length_of_sequence_for_value(i)
            if length > max_length:
                print "new max for start: %d, max is: %d" % (i, length)
                max_length = length
                max_length_number = i
        else:
            break

    return max_length_number

print longest_sequence_under_one_million()
