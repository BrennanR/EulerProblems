
def get_factors(n):
    """ I'm no longer capable of writing a fast enough get_factors method to solve Euler12, so I' ve borrowed a
     good one!
     From: https://stackoverflow.com/questions/6800193/
        what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    """
    return set(x for tup in ([i, n//i]
                             for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)
