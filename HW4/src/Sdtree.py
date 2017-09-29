import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')
sys.path.append('../HW3/src/')

import Config as config
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

	def create(self,t,yfun,pos=None,attr=None,val=None):
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
			for _,x in enumerate(cols.nums):
				tmp = tmp + x.sd * x.n / col.n
		return tmp

		def whatif(head, y):
			col = {'pos': head.pos, 'what': head.txt, 'nums': {}, 'n':0}
			for _, row in enumerate(self._t.rows):
				x = row.cells[col['pos']]
				col['n'] = col['n'] + 1
				col['nums']['x'] = num.update(col['nums']['x'], y(row))
			return {'key':xpect(col), 'val':col}

		out = []
		for _,h in enumerate(self._t.x.cols):
			out.append(whatif(h, self.yfun))

		out = sorted(out, key=lambda a: a['key'])
		return [x['val'] for x in out]

	@staticmethod
	def grow1(above, rows, lvl, b4, pos=None, attr=None, val=None):
		def pad():
			# is the below statement str('| '+lvl).format("%-20s")
			#return str.fmt("%-20s",string.rep('| ',lvl))
			return str('| '+lvl).format("%-20s")

		def likeAbove():
			# what is our version of tbl.copy? Table.py does not have a copy function. Shoud we just return
			#return tbl.copy(above._t, rows)
			rows_t = copy.deepcopy(above._t)
			return rows_t
			
		here = None
		if len(rows) >= config.tree.min:
			if lvl <= config.tree.maxDepth:
				if lvl==0:
					here=above
				else:
					here = Sdtree()
					here.create(likeAbove(), above.yfun, pos, attr, val)
				if here.stats.sd < b4:
					if lvl > 0:
						above._kids.append(here)
					cuts = here.order()
					cut = cuts[0]
					kids=[]
					rows1 = []
					for _, r in enumerate(rows):
						val = r.cells[cut.pos] # this works because cut is a col
						if (kids!=None) and (len(kids) > 0):
							rows1 = kids[val]
						rows1.append(r)
						kids[val] = rows1
					for val, rows1 in enumerate(kids):
						if len(rows1) < len(row):
							grow1(here, rows1, lvl+1, here.stats.sd, cut.pos, cut.what, val)

	def grow(self):
		# ?? first line change karna hai
		Sdtree.grow1(self, t.rows, 0, 1E32)

	def tprint(self, tr, lvl=0):
		def pad():
			return '| ' + str(lvl-1)
		def left(x):
			return str(x).format('%-20s')
		suffix=""
		if len(tr._kinds) == 0 or lvl==0:
			suffix = str("n=%s mu=%-.2f sd=%-.2f", tr.stats.n, tr.stats.mu, tr.stats.sd)
		if lvl == 0:
			print "\n" + suffix
		else:
			print left(pad())+tr.attr+"="+tr.val+"\t:"+suffix
		for j in range(1,len(tr._kinds)):
			tprint(tr._kinds[j],lvl+1)
		return

	def leaf(self, tr, cells, lvl=0):
		for j,kid in enumerate(tr._kids):
			pos,val = kid.pos, kid.val
			if cells[kid.pos] == kid.val:
				# don't know where this bins is coming from
				return leaf(kid, cells, bins,lvl+1)
		return tr

if __name__=="__main__":
	# Main function call to run the script
	filename = sys.argv[1]
	tree_build = Sdtree()
	tbl = Table()
	tbl.fromCSV(filename)
	print tbl.colsToString()
	# print "something here"
	yfunc = lambda y: y
	pos = 0



	#tree_build.create()
	
