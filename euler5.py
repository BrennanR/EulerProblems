from __future__ import division
import itertools


def is_evenly_divisible(divisor, dividend):
    #Exceptional cases.
    if (dividend / divisor) < 1:
        return False

    if dividend / divisor % 1 == 0:
        return True

    return False


def smallest_num_evenly_divisible_by_all(divisors):
    possible_dividends = itertools.count(2, 2)
    for i in possible_dividends:
        if i % 100000 == 0:
            print("curVal: " + str(i))

        divisible_by_all = False
        for divisor in divisors:
            if is_evenly_divisible(divisor, i):
                #print(str(i) + " / " + str(divisor) + ", evenly.")
                divisible_by_all = True
            else:
                #print(str(i) + " / " + str(divisor) + ", not evenly.")
                divisible_by_all = False
                break

        if divisible_by_all:
            return i

#Check the largest values first, don't check values under 20 that evenly divide
# into a value we've already checked (1-10).
to_check = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
print(str(smallest_num_evenly_divisible_by_all(to_check)))