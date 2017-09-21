import Random

class Sample:
	def __init__(self, most):
		self.all = []
		self.n = 0
		self.most = most

	def create(most):
		return Sample(512) # create a sample with 512

	def update(i, x):
		i.n = i.n+1
		if len(i._all) < i.most:
			i._all.append(x)
		elif r<len(i._all) / i.n:
			i._all[math.floor(1+Random.random()*len(i._all))] = x
		return x

	def updates(t,f,i=Sample()):
		for _, one in enumerate(t):
			update(i, f(one))
		return i

	