import sys

from Col import Col
import numpy as np


"""
Class to represent a Symbolic Column. Inherits Col Class
"""
class Sym(Col):

	def __init__(self):
		self.nk = 0
		self.counts = {}
		self.most = 0
		self.mode = None
		self._ent = None
		self.bins = None

	# Updates the column with a given value
	def update(self, x):
		if (isinstance(x, str)):
			self.n += 1
			if (not x in self.counts):
				self.counts[x] = 1
				self.nk += 1
			else:
				self.counts[x] += 1

			if (self.counts[x] > self.most):
				self.most = self.counts[x]
				self.mode = x
		else:
			raise ValueError('Expected String x but received '+str(type(x)))

	# Updates the column with multiple values. Applies function if given
	def updates(self, xs, f=None):
		if f is None:
			f = lambda x: x
		if (isinstance(xs, list)):
			for i in range(len(xs)):
				x = xs[i]
				self.update(f(x))
		else:
			raise ValueError('Expected List but received '+str(type(xs)))

	# This function finds a label for a given value based on the stored bins
	def discretize(self, x):
		r = None
		if not self.bins:
			return x
		for b in self.bins:
			r = b.label
			if x < b.most:
				break
		return r

	# Calculates norm of a new value based on current statistics of the column
	def norm(self, x):
		if (isinstance(x, str)):
			return x
		else:
			raise ValueError('Expected String but received '+str(type(x)))
	
	# Calcuales entropy of the column and returns it
	def ent(self):
		if (self._ent is None):
			e = 0
			for i, x in enumerate(self.counts):
				e = e - ((float(x)/self.n)*(np.log((float(f)/self.n), 2)))
			self._ent = e
		
		return self._ent

	# Calculates distance between two Sym values
	def distance(self, x, y):
		if (isinstance(x, str) and isinstance(y, str)):
			if (x == y):
				return 0
			else:
				return 1
		else:
			raise ValueError('Expected String in x & y but received '+str(type(x)) + " and " +str(type(y)))

	def __str__(self):
		return "n = " + str(self.n) + ", unique_n = " + str(self.nk) + ", counts = " + str(self.counts) + ", mode = " + str(self.mode) + ", most = " + str(self.most)

if __name__ == '__main__':
	a = Sym()
	a.updates(['a', 'b', 'c', 'd', 'e', 'a'])
	
	print a.distance('a', 'b')
	print (a)
	print a.txt