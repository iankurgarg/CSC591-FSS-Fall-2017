import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')

from Num import Num
from Sym import Sym
import Config as config
from Range import Range
from Label import Label
from RangeManager import RangeManager
import copy

# Class for supervised discretization of data
class SuperRange(object):
    def __init__(self, things, x, y, nump=True, lessp=True):
        self.x = x;
        self.y = y;
        self.nump = nump;
        self.lessp = lessp;
        if (self.lessp):
            self.better = SuperRange.below
        else:
            self.better = SuperRange.above
        
        if (self.nump):
            self.z = SuperRange.sd
        else:
            self.z = SuperRange.ent
        
        r = RangeManager();
        self.ranges = r.discretize(things, self.x)
        self.breaks = {}

    @staticmethod
    def below(x, y):
        return x < y
    
    @staticmethod
    def above(x, y):
        return x > y
    
    @staticmethod
    def sd(x):
        return x.sd
    
    @staticmethod
    def ent(x):
        return x.ent()
    
    @staticmethod
    def labels(nums):
        out = []
        for i in (nums):
            l = Label(nums[i], i)
            out.append(l)
        
        return out

    def memo(self, here, stop, _memo):
        inc = 1;
        if (stop > here):
            inc = 1
        else:
            inc = -1
        
        b4 = None
        if (here != stop):
            b4 = copy.deepcopy(self.memo(here+inc, stop, _memo))
        if (b4 is None):
            if (self.nump):
                b4 = Num()
            else:
                b4 = Sym()
        b4.updates(self.ranges[here]._all.all, self.y)
        _memo[here] = b4
        return _memo[here]
    
    def combine(self, lo, hi, all, bin, lvl):
        best = self.z(all)
        
        lmemo = [None]*(hi+1)
        rmemo = [None]*(hi+1)
        
        self.memo(hi, lo, lmemo)
        self.memo(lo, hi, rmemo)
        
        cut = None
        lbest = None
        rbest = None
        for j in range (lo,hi):
            l = lmemo[j]
            r = rmemo[j+1]
            tmp = float(l.n)/all.n*self.z(l) + float(r.n)/all.n*self.z(r)
            if self.better(tmp, best):
                cut = j
                best = tmp
                lbest = copy.deepcopy(l)
                rbest = copy.deepcopy(r)
        
        if cut:
            bin = self.combine(lo, cut, lbest, bin, lvl+1) + 1
            bin = self.combine(cut+1, hi, rbest, bin, lvl+1)
        else: # no cut found, mark everything "lo" to "hi" as "bin"
            if (not bin in self.breaks):
                self.breaks[bin] = -10E32
            if self.ranges[hi].high > self.breaks[bin]:
                self.breaks[bin] = self.ranges[hi].high  
        
        return bin
    
    def discretize(self):
        temp = [None]*(len(self.ranges))
        memo_output = self.memo(0, len(self.ranges)-1, temp)
        
        self.combine(0, len(self.ranges)-1, memo_output, 0, 0)
        return SuperRange.labels(self.breaks)

if __name__=="__main__":
    numbers = list(np.random.rand(100))

    print "We have many unsupervised ranges."
    r = RangeManager()
    ranges = r.discretize(numbers)
    for i,x in enumerate(ranges):
        print "x", i, x

    s = SuperRange()
