import sys
sys.path.append('../HW1/src/')
sys.path.append('../HW2/src/')
sys.path.append('../HW3/src/')

import Config as the
import Num as num
import Table as t

class Sdtree:
	def __init__(self):
		self._t = None
		self._kids = []
		self.yfun = None
		self.pos = None
		self.attr = None
		self.val = None
		self.stats = None

	def create(self,t,yfun,pos,attr,val):
		self._t = t
		self._kinds={}
		self.yfun = yfun
		self.pos = pos
		self.attr = attr
		self.val = val
		self.stats = num.updates(t.rows, yfun)
		return

	def order(self,t,y):
		
		def xpect(col):
			tmp = 0
			for _,x in enumerate(cols.nums):
				tmp = tmp + x.sd * x.n / col.n
		return tmp

		def whatif(head, y):
			col = {'pos':head.pos, 'what'=head.txt, 'nums'={}, 'n'=0}
			for _,row in enumerate(t.rows):
				x = row.cells[col['pos']]
				col['n'] = col['n'] + 1
				col['nums']['x'] = num.update(col['nums']['x'], y(row))
			return {'key':xpect(col), 'val':col}
		out = []
		for _,h in enumerate(t.x.cols):
			out.append(whatif(h,y))
		# how to write function (x,y) return x.key < y.key
		# sorted(out) ?
		table.sort(out,x.key<y.key)
		# the last line too
		return lst.collect(out, x.val)

	def grow1(self,above,yfun,rows,lvl,b4,pos,attr,val):
		def pad():
			# is the below statement str('| '+lvl).format("%-20s")
			return str.fmt("%-20s",string.rep('| ',lvl))

		def likeAbove():
			# what is our version of tbl.copy? Table.py does not have a copy function. Shoud we just return
			# rows = copy.copy(above._t)
			# return rows
			return tbl.copy(above._t, rows)

		if len(rows) >= the.tree.min:
			if lvl <= the.tree.maxDepth:
				# This line looks unfamiliar
				here = (lvl==0 and above or create(likeAbove(), yfun, pos, attr, val)
				if here.stats.sd < b4:
					if lvl > 0:
						above._kids.append(here)
					cuts = order(here._t, yfun)
					cut = cuts[1]
					kids=[]
					rows1 = []
					for _,r in enumerate(rows):
						val = r.cells[cut.pos]
						if len(kids) > 0:
							rows1.append(kids[val])
						rows1.append(r)
						kids[val] = rows1
					for val,rows1 in enumerate(kids):
						if len(rows) < len(row):
							grow1(here,yfun,rows1,lvl+1,here.stats.sd,cut.pos,cut.what,val)

	def grow(self,t,y):
		yfun = tbl[y](t)
		root = create(t,yfun)
		grow1(root,yfun,t.rows,0,10^32)
		return root

	def tprint(self,tr, lvl=0):
		def pad():
			return '| '+str(lvl-1)
		def left(x):
			return str('%-20s',x)
		suffix=""
		if len(tr._kinds) ==- or lvl==0:
			suffix = str("n=%s mu=%-.2f sd=%-.2f", tr.stats.n, tr.stats.mu, tr.stats.sd)
		if lvl = 0:
			print "\n" + suffix
		else:
			print left(pad())+tr.attr+"="+tr.val+"\t:"+suffix
		for j in range(1,len(tr._kinds)):
			tprint(tr._kinds[j],lvl+1)
		return

	def leaf(self,tr,cells,lvl=0):
		for j,kid in enumerate(tr._kids):
			pos,val = kid.pos, kid.val
			if cells[kid.pos] == kid.val:
				# don't know where this bins is coming from
				return leaf(kid, cells, bins,lvl+1)
		return tr

if __name__=="__main__":
	# Main function call to run the script
	tree_build = Sdtree()
	tree_build.create()
	
