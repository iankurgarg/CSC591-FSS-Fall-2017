class Num:

	def __init__(self):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.hi = -1e32
        self.lo = 1e32
        self.w = 1

    def about(i):
    	dic = {'pos':i.pos,
    		'txt':i.txt,
    		'n':i.n,
    		'mu':i.mu,
    		'sd':i.sd,
    		'lo':i.lo,
    		'hi':i.hi
    		}
    	return dic

    def create():
    	return Num()

    def update(i,x):
		i.n = i.n + 1
		if x < i.lo:
			i.lo = x
		if x > i.hi:
			i.hi = x
		delta = x - i.mu
		i.mu = i.mu + delta / i.n
		i.m2 = i.m2 + delta * (x - i.mu)
		if i.n > 1:
			i.sd = (i.m2 / (i.n - 1))^0.5 end end 
		return i

	def updates(t,f,all=Num()):
		f = f or function (z) return z end
		for _,one in enumerate(t):
			update(all, f(one)) end
		return all
