
import itertools
import utilities


class TriangleNumberSolver:
    current_triangle_number = 0
    current_triangle_number_index = 0

    def __init__(self):
        self.find_first_triangle_number_with_five_hundred_divisors()

    @classmethod
    def get_next_triangle_number(cls):
        cls.current_triangle_number_index += 1
        cls.current_triangle_number += TriangleNumberSolver.current_triangle_number_index
        return cls.current_triangle_number

    @staticmethod
    def get_number_of_divisors_of_number(number):
        return len(utilities.get_factors(number))

    def find_first_triangle_number_with_five_hundred_divisors(self):
        current_max = 0
        for i in itertools.count():
            next_triangle_number = self.get_next_triangle_number()
            number_of_divisors = TriangleNumberSolver.get_number_of_divisors_of_number(next_triangle_number)

            if number_of_divisors > 500:
                print "index: %s, number: %s" % (TriangleNumberSolver.current_triangle_number_index,
                                                 TriangleNumberSolver.current_triangle_number)
                return TriangleNumberSolver.current_triangle_number
            else:
                if number_of_divisors > current_max:
                    current_max = number_of_divisors
                    print "new max divisors: %d, for: %d" % (number_of_divisors, next_triangle_number)
                elif i % 50 == 0:
                    print "number: %d, divisor count: %d" % (next_triangle_number, number_of_divisors)


TriangleNumberSolver()

