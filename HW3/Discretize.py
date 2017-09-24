from RangeManager import RangeManager
import numpy as np

def discretize_range(t, x=None):
    if (x is None):
        x = lambda y: y
    
    t_sorted = sorted(t, key=x)

    r = RangeManager();
    r.manage(t, x)

    last = 0.0
    for index, value in enumerate(t):
        value1 = x(value)
        r.now.update(value, value1)
        if (index > 0 and value1 > last and r.now.n > r.enough and r.now.span > r.epsilon):
            r.nextRange()
        last = value1
    
    return r.ranges


if __name__=="__main__":
    numbers = list(np.random.rand(100))
    r = discretize_range(numbers)
    for i, x in enumerate(r):
        print "x", i, x