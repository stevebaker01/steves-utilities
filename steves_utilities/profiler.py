import time
from functools import reduce
from operator import mul

def profile(method):
    def profiled(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print('{} ({}, {}) {:2.6f} sec'.format(method.__name__, args, kwargs, te - ts))
        return result
    return profiled

@profile
def waste_time(x):
    reduce(mul, range(x), 1)