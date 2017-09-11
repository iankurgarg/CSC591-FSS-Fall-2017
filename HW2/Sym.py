import sys
sys.path.append('../HW1/src/')

import Config as config


class Sym(object):
	def __init__(self):
		self.n = 0
		self.nk = 0
		self.counts = {}
		self.most = 0
		self.mode = None

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

	def updates(self, xs):
		if (isinstance(xs, list)):
			for i in range(len(xs)):
				x = xs[i]
				self.update(x)
		else:
			raise ValueError('Expected List but received '+str(type(xs)))


	def norm(self, x):
		if (isinstance(x, str)):
			return x
		else:
			raise ValueError('Expected String but received '+str(type(x)))

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