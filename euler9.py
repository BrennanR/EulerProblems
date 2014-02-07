__author__ = 'Brennan'

import itertools
import time


def is_pythagorean_triplet(a, b, c):
    return a * a + b * b == c * c


def find_triplet_that_sums_to(triple_sum):
    all_triples = itertools.permutations(range(triple_sum), 3)
    all_ordered_triples = itertools.ifilter(lambda x: x[0] < x[1] < x[2], all_triples)

    for triple in all_ordered_triples:
        if is_pythagorean_triplet(triple[0], triple[1], triple[2]):
            if triple[0] + triple[1] + triple[2] == triple_sum:
                return triple[0] * triple[1] * triple[2]


start_time = time.time()
print find_triplet_that_sums_to(1000)
end_time = time.time()
print("Run time: {0} seconds.".format(str(end_time - start_time)))