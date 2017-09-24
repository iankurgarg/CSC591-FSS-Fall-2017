import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')

import math
from Num import Num
import Config as config
from Range import Range


class RangeManager(object):
    def __init__(self):
        self.now = None
        self.ranges = []
        self.nums = Num()
        self.cohen = config.chop['cohen']
        self.m = config.chop['m']
        self.size = len(self.ranges)
        self.high = None
        self.low = None
        self.enough = None
        self.epsilon = None
        self.func = None
    
    def nextRange(self):
        self.now = Range()
        self.ranges.append(self.now)
    
    def manage(self, t, f):
        self.ranges = []
        self.nextRange()
        self.func = f
        self.size = len(t)
        self.nums.updates(t, f)
        self.high = self.nums.max
        self.low = self.nums.min
        self.enough = math.pow(self.size, self.m)
        self.epsilon = self.nums.sd * self.cohen
    
    def discretize(self, t, x=None):
        if (x is None):
            x = lambda y: y
        
        t_sorted = sorted(t, key=x)

        self.manage(t_sorted, x)

        last = 0.0
        for index, value in enumerate(t_sorted):
            value1 = x(value)
            self.now.update(value, value1)
            if (index > 0 and value1 > last and self.now.n > self.enough and self.now.span > self.epsilon):
                    #and (self.now.n-index)>self.enough:
                self.nextRange()
            last = value1
        
        return self.ranges

if __name__=="__main__":
    r = RangeManager();
    r.manage([1,2,3,4,5], None)
    print r.nums