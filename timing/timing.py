def sum_multiples(mults, N):
    '''
    Returns the sum of the multiples of each number
    in "mults" between 1 and N.
    If a number is a multiple of several numbers in "mults",
    count it multiple times.
    '''
    # Start with an empty list
    to_sum = []
    for i in range(1, N+1):
        for test_mult in mults:
            if i % test_mult == 0:
                to_sum.append(i)
    
    total = 0
    for number in to_sum:
        total += number
    
    return total


# Testing
assert sum_multiples([2, 3], 10) == (2 + 4 + 6 + 8 + 10) + (3 + 6 + 9)
assert sum_multiples([10, 20, 4], 25) == (10 + 20) + 20 + (4 + 8 + 12 + 16 + 20 + 24)
assert sum_multiples([2, 2], 6) == 2 * (2 + 4 + 6)

# What does this test verify?
import numpy as np
rng = np.random.default_rng(1)
random_integer = rng.integers(1, 11)
print(random_integer)
assert sum_multiples([1], random_integer) == sum(range(1, random_integer + 1))





# Profilers: timeit, cProfile, line_profiler.

# timeit: how much time sum_multiples() takes to run?
import timeit
N_max = 1000
N_mult = 500

mults = rng.integers(5, N_max, size=N_mult)

# Code to time:
print(timeit.timeit('sum_multiples(mults, N_max)', globals=globals(), number=10))