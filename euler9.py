__author__ = 'Brennan'

import itertools
import math
import time


def is__pythagorean_triplet(a, b, c):
    return a * a + b * b == c * c


def find_triplet_that_sums_to(triple_sum):
    all_triples = itertools.permutations(range(triple_sum), 3)
    all_ordered_triples = itertools.ifilter(lambda x: x[0] < x[1] < x[2], all_triples)

    for triple in all_ordered_triples:
        if is__pythagorean_triplet(triple[0], triple[1], triple[2]):
            if triple[0] + triple[1] + triple[2] == triple_sum:
                return math.sqrt(triple[0]) * math.sqrt(triple[1]) * math.sqrt(triple[2])


time1 = time.time()
print find_triplet_that_sums_to(1000)
time2 = time.time()
print("Time 2: " + str(time2))
print("Run time: " + str(time2 - time1))