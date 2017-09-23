from Random import Random
import math

class Sample:
	def __init__(self, most):
		self.all = []
		self.n = 0
		self.most = most

	def update(self, x):
		self.n = self.n + 1
		rand = Random.another()
		if len(self.all) < self.most:
			self.all.append(x)
		elif rand < float(len(self.all))/self.n:
			self.all[int(math.floor(rand*len(self.all)))] = x

	def updates(self, t, f=None):
		if f is None:
			f = lambda x: x
		for _, one in enumerate(t):
			self.update(f(one))

if __name__ == "__main__":
	Random.system()
	s = Sample(10);
	for i in range(20):
		s.update(i);
		print s.all

