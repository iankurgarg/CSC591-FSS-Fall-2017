import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')
sys.path.append('../HW3/src/')

import Config as config
from Num import Num
from Random import Random
from Table import Table
import copy

"""
Class to create a Regression Tree
"""
class Sdtree:
	def __init__(self, t, yfun, pos=None, attr=None, val=None):
		self._t = t
		self._kids=[]
		self.yfun = yfun
		self.pos = pos
		self.attr = attr
		self.val = val
		self.stats = Num()
		self.stats.updates(t.rows, yfun)

	# Orders the rows of the table based on yfun function
	def order(self):
		out = []
		for _,h in enumerate(self._t.X['columns']):
			out.append(self.whatif(h, self.yfun))

		out = sorted(out, key=lambda a: a['key'])
		return [x['val'] for x in out]

	# Utility function. used by order()
	def whatif(self, head, y):
		col = {'pos': head.pos, 'what': head.txt, 'nums': {}, 'n':0}
		for _, row in enumerate(self._t.rows):
			x = row.cells[col['pos']]
			col['n'] = col['n'] + 1
			if (x in col['nums']):
				a = col['nums'][x]
			else:
				a = Num()
			a.update(y(row))
			col['nums'][x] = a
			
		return {'key':SdtreeUtil.xpect(col), 'val':col}

	# Recursive function used to create cuts and create a tree using max Depth and min number of rows in the leaf node
	def grow1(self, rows, lvl, b4, pos=None, attr=None, val=None):
		if len(rows) >= config.tree['min']:
			if lvl <= config.tree['maxDepth']:
				if(lvl == 0):
					here = self
				else:
					here = Sdtree(self._t.copy(rows), self.yfun, pos, attr, val)
				if here.stats.sd < b4:
					if lvl > 0:
						self._kids.append(here)
					cuts = here.order()
					cut = cuts[0]
					kids = {}
					for _, r in enumerate(rows):
						val = r.cells[cut['pos']]
						rows1 = kids.get(val) if val in kids else []
						rows1.append(r)
						kids[val] = (rows1)
					for val, rows1 in kids.items():
						if len(rows1) < len(rows):
							here.grow1(rows1, lvl + 1, here.stats.sd, cut['pos'], cut['what'], val)

	# Main function grow. To be called from outside the class. Uses grow1
	def grow(self):
		self.grow1(self._t.rows, 0, 1E32)

	# Function to print the created tree in proper formatting (Calls itself recursively)
	def treePrint(self, lvl=0):
		suffix = ""
		if len(self._kids) == 0 or lvl==0:
			suffix = "n=%s mu=%-.2f sd=%-.2f" % (self.stats.n, self.stats.mu, self.stats.sd)
		if lvl == 0:
			print "\n" + suffix
		else:
			print SdtreeUtil.left("{}{} = {}".format(SdtreeUtil.pad(lvl), str(self.attr) or "", str(self.val) or "")), '\t:  ', suffix
		for j in range(len(self._kids)):
			self._kids[j].treePrint(lvl+1)


"""
Utility Class. Contains a few static function used by Sdtree Class
"""
class SdtreeUtil(object):
	@staticmethod
	def pad(lvl):
		return "| " * (lvl)
	
	@staticmethod
	def left(x):
		return "%-20s" % x

	@staticmethod
	def xpect(col):
		tmp = 0
		for _, xx in enumerate(col['nums']):
			x = col['nums'][xx]
			tmp = tmp + x.sd * x.n / col['n']
		return tmp


if __name__=="__main__":
	Random.rseed(2)
	filename = sys.argv[1]
	tbl = Table()
	tbl.fromCSV(filename)
	discretized_table = tbl.discretizeRows()

	for _, head in enumerate(discretized_table.X['columns']):
		if (head.bins):
			print len(head.bins), head.txt
	
	tree_build = Sdtree(discretized_table, yfun=discretized_table.dom())
	tree_build.grow()
	tree_build.treePrint()

	