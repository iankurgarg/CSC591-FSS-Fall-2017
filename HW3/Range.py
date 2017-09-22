import Num as num
import Sample as sample

class Range:
	self._all = []
	self.n = 0
	self.high = -2^63
	self.lo =  2^63,
	slef.span = 2^64

	def __init__(self):
		return Range()

	def create(self):
		return Range()

	def update(i, one, x):
		#SOME.update(i._all, one) need to convert this line
		sample.update(i._all, one)
		i.n = i.n + 1
		if x > i.hi:
			i.hi = x  end
		if x < i.lo:
			i.lo = x  end
		i.span = i.hi - i.lo
		return x

	def nextRange(i) :
		i.now  = create()
		i.ranges.append(i.now)

	# There is something weird going on with this class with 
	# .now and .ranges are not declared in the class variables.
	# Need to figure out what is going on. 

	"""
	local function rangeManager(t, x)  
	local _ = { 
	x     = x,
	cohen = the.chop.cohen,
	m     = the.chop.m,
	size  = #t,
	ranges= {} -- list of all known ranges 
	}
	nextRange(_)
	_.num = NUM.updates(t, _.x)
	_.hi  = _.num.hi

	_._.enough = _.size^_.m
	_._.epsilon= _.num.sd * _.cohen
	return _ end
	"""

	# This is what I don't understand. Please check