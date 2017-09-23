import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')

import Num as num
from Sample import Sample
import Config as config

class Range(object):
	def __init__(self):
		self._all = Sample()
		self.n = 0
		self.high = -float("inf")
		self.low =  float("inf"),
		self.span = float("inf")

	def update(self, one, x):
		#SOME.update(i._all, one) need to convert this line
		self._all.update(one);
		self.n = self.n + 1
		if x > self.high:
			self.high = x
		if x < self.low:
			self.low = x
		self.span = self.high - self.low
	
	def __str__(self):
		return "{span="+str(self.span)+", low="+str(self.low)+", n="+str(self.n)+", high="+str(self.high)+"}";


if __name__=="__main__":
	r = Range();
	r.update(1,1)
	print r