import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')
sys.path.append('../HW3/src/')

import Config as config
from SuperRange import SuperRange
from Num import Num
from Table import Table
import copy



class Sdtree:
	def __init__(self):
		self._t = None
		self._kids = []
		self.yfun = None
		self.pos = None
		self.attr = None
		self.val = None
		self.stats = None

	def create(self, t, yfun, pos=None, attr=None, val=None):
		self._t = t
		self._kinds={}
		self.yfun = yfun
		self.pos = pos
		self.attr = attr
		self.val = val
		self.stats = Num()
		self.stats.updates(t.rows, yfun)
		return

	def order(self):
		def xpect(col):
			tmp = 0
			for _, xx in enumerate(col['nums']):
				x = col['nums'][xx]
				tmp = tmp + x.sd * x.n / col['n']
			return tmp

		def whatif(head, y):
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
				
			return {'key':xpect(col), 'val':col}

		out = []
		for _,h in enumerate(self._t.X['columns']):
			out.append(whatif(h, self.yfun))

		out = sorted(out, key=lambda a: a['key'])
		return [x['val'] for x in out]

	@staticmethod
	def grow1(above, rows, lvl, b4, pos=None, attr=None, val=None):
		if len(rows) >= 2:
			if lvl <= 10:
				if(lvl == 0):
					here = above
				else:
					here = Sdtree()
					here.create(above._t.copy(rows), above.yfun, pos, attr, val)
				if here.stats.sd < b4:
					if lvl > 0:
						above._kids.append(here)
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
							Sdtree.grow1(here, rows1, lvl + 1, here.stats.sd, cut['pos'], cut['what'], val)


	def grow(self):
		Sdtree.grow1(self, self._t.rows, 0, 1E32)

	def tprint(self, lvl=0):
		def pad():
			return "| " * (lvl)

		def left(x):
			return "%-20s" % x

		suffix = ""
		if len(self._kids) == 0 or lvl==0:
			suffix = "n=%s mu=%-.2f sd=%-.2f" % (self.stats.n, self.stats.mu, self.stats.sd)
		if lvl == 0:
			print "\n" + suffix
		else:
			print left("{}{} = {}".format(pad(), str(self.attr) or "", str(self.val) or "")), '\t:\t\t', suffix
		for j in range(len(self._kids)):
			self._kids[j].tprint(lvl+1)


if __name__=="__main__":
	filename = sys.argv[1]
	tbl = Table()
	tbl.fromCSV(filename)
	print tbl.colsToString()

	tbl2 = tbl.discretizeRows()
	print tbl2.colsToString()
	
	tree_build = Sdtree()
	tree_build.create(tbl2, yfun=tbl2.dom())
	tree_build.grow()
	tree_build.tprint()

	