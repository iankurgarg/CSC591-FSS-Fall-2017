import sys

from Col import Col

"""
Class to represent a Numeric Column. Inherits Col Class
"""
class Num(Col):
	def __init__(self):
		self.mu = 0
		self.m2 = 0
		self.sd = 0
		self.max = -1e32
		self.min = 1e32

	# Updates the column with a given value
	def update(self, x):
		if (isinstance(x, int) or isinstance(x, float)):
			self.n += 1
			if (x < self.min):
				self.min = x
			if (x > self.max):
				self.max = x

			delta = x - self.mu
			self.mu = self.mu + delta/self.n
			self.m2 = self.m2 + delta*(x-self.mu)
			if self.n > 1:
				self.sd = (self.m2/(self.n -1))**(0.5)
		else:
			raise ValueError('Expected Number x but received '+str(type(x)))

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
	
	# returns information about self
	def about(self):
		ret = {};
		ret['pos'] = self.pos;
		ret['txt'] = self.txt;
		ret['n'] = self.n;
		ret['mu'] = self.mu;
		ret['sd'] = self.sd;
		ret['max'] = self.max;
		ret['min'] = self.min;
		return ret;
	
	# Checks how likely is th given value in the current distribution
	def like(self, x):
		var = self.sd*self.sd;
		denom = Math.pow((2*Math.pi*var), 0.5)
		num = Math.pow(2.718281, (-1*Math.pow(x-self.mu, 2)/(2*var)))
		return num/(denom + 10e-64)

	# Calculates norm of a new value based on current statistics of the column
	def norm(self, x):
		if (isinstance(x, int) or isinstance(x, float)):
			res = (x-self.min)/(self.max - self.min + 1e-32)
			return res

		else:
			raise ValueError('Expected Number but received '+str(type(x)))

	# Calculates distance between given values based on current distribution
	def distance(self, x, y):
		if (isinstance(x, int) or isinstance(x, float)):
			if (isinstance(y, int) or isinstance(y, float)):
				x = self.norm(x)
				y = self.norm(y)
				return abs(x-y)

			else:
				raise ValueError('Expected Number y but received '+str(type(y)))

		else:
			raise ValueError('Expected Number x but received '+str(type(x)))

	def __str__(self):
		return "n = " + str(self.n) + ", mu = " + str(self.mu) + ", m2 = " + str(self.m2) + ", sd = " + str(self.sd) + ", max = " + str(self.max) + ", min = " + str(self.min)

if __name__ == '__main__':
	a = Num()
	a.updates([1,3,4,5,6,7,8,9])
	print a.norm(2)
	print a.norm(5.5)
	print (a)