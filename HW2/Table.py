import sys
sys.path.append('../HW1/src/')

from Row import Row
from Col import Col
from Num import Num
from Sym import Sym
from CSVReader import CSVReader

class Table(object):
	def __init__(self):
		self.rows = []
		self.spec = []
		self.goals = []
		self.less = []
		self.more = []
		self.name = []
		self.all = {'nums': [], 'syms': [], 'columns': []}
		self.X = {'nums': [], 'syms': [], 'columns': []}
		self.Y = {'nums': [], 'syms': [], 'columns': []}

	def categories(self, txt, pos):
		if (txt.startsWith("$")):
			col = Num()
			col.txt = txt
			col.weight = 1
			col.pos = pos
			self.name[col.txt] = col
			


	def header(self, cells):
		self.spec = cells
		for i, cell in enumerate(cells):
			what, weight, where = self.categories(cell)


