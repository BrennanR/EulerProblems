__author__ = 'Brennan'

import euler7
import time


def find_sum_of_primes(ceiling):
    sum_of_primes = 0
    for i in range(ceiling):
        if euler7.is_prime(i):
            sum_of_primes += i

    return sum_of_primes


start_time = time.time()
print(str(find_sum_of_primes(2000000)))
end_time = time.time()
print("Run time: {0} seconds.".format(str(end_time - start_time)))