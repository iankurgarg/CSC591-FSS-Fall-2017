from RangeManager import RangeManager
import numpy as np


if __name__=="__main__":
    numbers = list(np.random.rand(100))

    print "We have many unsupervised ranges."
    r = RangeManager()
    ranges = r.discretize(numbers)
    for i,x in enumerate(ranges):
        print "x", i, x