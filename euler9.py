__author__ = 'Brennan'

import math
import itertools


def is_pythagorean_triplet(a, b, c):
    return math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)


def find_triplet_that_sums_to(triple_sum):
    for triple in itertools.ifilter(lambda x: x[0] < x[1] < x[2], itertools.permutations(range(triple_sum), 3)):

        # print("triple 0: " + str(triple[0]) + ", triple 1: " + str(triple[1]) + ", triple 2: " + str(triple[2]))

        if is_pythagorean_triplet(triple[0], triple[1], triple[2]):
            if triple[0] + triple[1] + triple[2] == triple_sum:
                return triple[0] * triple[1] * triple[2]


print(find_triplet_that_sums_to(1000))