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

def has(branch):
	out = []
	for i in range(1,len(branch)):
		step = branch[i]
		out.append({'attr':step.attr, 'val':step.val})
	return

def have(branches):
	for _,branch in enumerate(branches): #should be a list
		branch.has = has(branch)
	return branches

def branches1(tr, out, b):
	if tr.attr:
		b.append({'attr'=tr.attr,'val'=tr.val,'_stats'=tr.stats})
	if len(b) > 0:
		out.append(b)
	for _,kid in enumerate(tr._kids):
		branches1(kid,out,copy.deepcopy(b))
	return b # list of dictonaries

def branches(tr):
	return have(branches1(tr,{},{}))

def member2(twins0, twins):
	for _,twin1 in enumerate(twins):
		if twin0.attr == twin1.attr and twin0.val == twin1.val:
			return True
	return False

def delta(t1, t2):
	out = []
	for _,twin in enumerate(t1):
		if not member2(twin,t2):
			out.append((twin.attr,twin.val))
	return out # list of tuples

def contrasts(branches, better):
	for i,branch1 in enumerate(branches):
		out = []
		for j,branch2 in enumerate(branches):
			if i!=j:
				num1 = branch1[-1]._stats
				num2 = branch2[-1]._stats
				if better(num2.mu, num1.mu):
					if not Num.same(num1,num2): # write a static function in Num.py called same, hedges, ttest1, ttest
						inc = delta(branch2.has,branch1.has)
						if len(inc) > 0:
							out.append( {'i':i,'j':j,'ninc':len(inc),'muinc':num2.mu - num1.mu,'inc':inc, 'branch1':branch1.has,'mu1':num1.mu,'branch2':branch2.has,'mu2':num2.mu} )
		print ""
		# below sorted line needs correction @Ankur
		sorted(out, key={lambda (x,y) : x.muinc < y.muinc})
		print i,'max mu',out[0]
		sorted(out, key={lambda (x,y) : x.ninc < y.ninc})
		print i,'min inc',out[1]
	return

def more(x,y):
	return x > y

def less(x,y):
	return x < y

def plans(branches):
	return contrasts(branches,more)

def monitors(branches):
	return contrasts(branches,less)

# need to figure out the main function like before
# and what is the class of branches.
# I think it is Num because we are using branch1[-1]._stats
# _stats makes sence only in Nums