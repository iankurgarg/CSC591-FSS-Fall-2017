from RangeManager import RangeManager
from SuperRange import SuperRange
import numpy as np


def x(a):
    return a[0]

def y(a):
    return a[1]

def klass(z):
    v = 2*np.random.rand()/100

    if z < 0.2:
        v += 0.2
    elif z < 0.6:
        v += 0.6
    else:
        v += 0.9
    return v

if __name__=="__main__":
    numbers = list(np.random.rand(100))

    final_list = [None]*(len(numbers))

    for ind, i in enumerate(numbers):
        temp = [i, klass(i)]
        final_list[ind] = temp

    print "We have many unsupervised ranges."
    r = RangeManager()
    ranges = r.discretize(final_list, x)
    for i,v in enumerate(ranges):
        print "x", i, v
    
    s = SuperRange(final_list, x, y)
    super_ranges = s.discretize()
    print "\nWe have fewer supervised ranges."
    for i in (super_ranges):
        print "x", i, super_ranges[i]