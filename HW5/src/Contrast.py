import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')
sys.path.append('../HW3/src/')
sys.path.append('../HW4/src/')

import Config as config
from Num import Num
from Table import Table
from Sdtree import Sdtree # I don't think this is used
import copy

# class Contrast: No class structure required
# 	def __init__(self):
# 		return

class Branch(object):
	_has = None
	lst = []

	def member2(self, twin0):
		for _, twin1 in enumerate(self.has):
			if twin0['attr'] == twin1['attr'] and twin0['val'] == twin1['val']:
				return True
		return False

	def delta(self, t2):
		print "here"
		out = []
		for _, twin in enumerate(t2):
			if not self.member2(twin):
				out.append((twin['attr'], twin['val']))
		return out # list of tuples

	def has(self):
		if (self._has is None):
			out = []
			for i in range(len(self.lst)):
				step = self.lst[i]
				out.append({'attr':step['attr'], 'val':step['val']})

			self._has = out
		return self._has

def have(branches):
	for _, branch in enumerate(branches): #should be a list
		branch.has()
	return branches

def branches1(tr, out, b):
	if tr.attr:
		b.lst.append({'attr': tr.attr,'val' : tr.val, '_stats': tr.stats})
	if len(b.lst) > 0:
		out.append(b)
	for _,kid in enumerate(tr._kids):
		branches1(kid, out, copy.deepcopy(b))
	return out # list of dictonaries

def branches(tr):
	return have(branches1(tr,[],Branch()))

def contrasts(branches, better):
	for i, branch1 in enumerate(branches):
		out = []
		for j, branch2 in enumerate(branches):
			if i != j:
				num1 = branch1.lst[-1]['_stats']
				num2 = branch2.lst[-1]['_stats']
				print "num1 = ", num1.mu, ", num2 = ", num2.mu
				if better(num2.mu, num1.mu):
					print "1"
					if not num1.same(num2):
						inc = branch1.delta(branch2)
						if len(inc) > 0:
							out.append( {'i':i,'j':j,'ninc':len(inc),'muinc':num2.mu - num1.mu,'inc':inc, 'branch1':branch1.has,'mu1':num1.mu,'branch2':branch2.has,'mu2':num2.mu} )
		print ""
		# below sorted line needs correction @Ankur
		sorted(out, key=lambda x, y : x['muinc'] < y['muinc'])
		print i, 'max mu', out[0]
		sorted(out, key=lambda x, y : x['ninc'] < y['ninc'])
		print i, 'min inc', out[0]
	return

def more(x,y):
	return x > y

def less(x,y):
	return x < y

def plans(branches):
	return contrasts(branches, more)

def monitors(branches):
	return contrasts(branches, less)

if __name__ == '__main__':
	filename = sys.argv[1]
	tbl = Table()
	tbl.fromCSV(filename)
	discretized_table = tbl.discretizeRows()
	
	tree_build = Sdtree(discretized_table, yfun=discretized_table.dom())
	tree_build.grow()
	tree_build.treePrint()
	b = branches(tree_build)
	# print b

	plans = plans(b)

# need to figure out the main function like before
# and what is the class of branches.
# I think it is Num because we are using branch1[-1]._stats
# _stats makes sence only in Nums