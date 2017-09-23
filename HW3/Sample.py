import Random

class Sample:
	def __init__(self, most):
		self.all = []
		self.n = 0
		self.most = most

	def update(self, x):
		self.n = self.n+1
		if len(self.all) < self.most:
			self.all.append(x)
		elif r<len(i._all) / i.n:
			i._all[math.floor(1+Random.random()*len(i._all))] = x
		return x

	def updates(t,f,i=Sample()):
		for _, one in enumerate(t):
			update(i, f(one))
		return i

	