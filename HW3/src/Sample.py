from Random import Random
import math
import Config as config

class Sample:
	def __init__(self, most=None):
		self.all = []
		self.n = 0
		if most:
			self.most = most
		else:
			self.most = config.sample['most']

	def update(self, x):
		self.n = self.n + 1

		if len(self.all) < self.most:
			self.all.append(x)
		else:
			rand = Random.another()
			if rand < float(len(self.all))/self.n:
				print int(rand*len(self.all))
				self.all[int(rand*len(self.all))] = x

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

