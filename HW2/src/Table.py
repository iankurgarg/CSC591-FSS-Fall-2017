import sys
sys.path.append('../HW1/src/')

from Row import Row
from Col import Col
from Num import Num
from Sym import Sym
from CSVReader import CSVReader

"""
Class Table. Used for representation of a csv file in a table
It uses CSVReader Class to read and parse a csv file. Then maintains a table.
On Addition of each row, the mean, std, var and other parameters for the column are udpated.
It maintains separate columns for independent and dependent columns.
"""
class Table(object):
	def __init__(self):
		self.rows = []
		self.spec = []
		self.goals = []
		self.less = []
		self.more = []
		self.name = {}
		self.all = {'nums': [], 'syms': [], 'columns': []}
		self.X = {'nums': [], 'syms': [], 'columns': []}
		self.Y = {'nums': [], 'syms': [], 'columns': []}

	"""
	This function gets input the name of the column and its position.
	Based on the magic characters in the column name, it identifies its type 
	and adds it to appropriate lists
	"""
	def categories(self, txt, pos):
		if (txt.startswith("$")):
			col = Num()
			col.txt = txt
			col.weight = 1
			col.pos = pos
			self.name[col.txt] = col
			self.all['columns'].append(col)
			self.X['columns'].append(col)
			self.all['nums'].append(col)
			self.X['nums'].append(col)
		elif (txt.startswith("<")):
			col = Num()
			col.txt = txt
			col.weight = -1
			col.pos = pos
			self.name[col.txt] = col
			self.all['columns'].append(col)
			self.Y['columns'].append(col)
			self.all['nums'].append(col)
			self.goals.append(col)
			self.less.append(col)
			self.Y['nums'].append(col)
		elif (txt.startswith(">")):
			col = Num()
			col.txt = txt
			col.weight = 1
			col.pos = pos
			self.name[col.txt] = col
			self.all['columns'].append(col)
			self.Y['columns'].append(col)
			self.all['nums'].append(col)
			self.goals.append(col)
			self.more.append(col)
			self.Y['nums'].append(col)
		elif (txt.startswith("!")):
			col = Sym()
			col.txt = txt
			col.weight = 1
			col.pos = pos
			self.name[col.txt] = col
			self.all['columns'].append(col)
			self.Y['syms'].append(col)
			self.Y['columns'].append(col)
			self.all['syms'].append(col)
		elif (txt.startswith("")):
			col = Sym()
			col.txt = txt
			col.weight = 1
			col.pos = pos
			self.name[col.txt] = col
			self.all['columns'].append(col)
			self.X['columns'].append(col)
			self.all['syms'].append(col)
			self.X['syms'].append(col)
		return


	"""
	This functions takes input a list of column names. It uses categories function to add each column to the table
	"""
	def header(self, cells):
		self.spec = cells
		for i, cell in enumerate(cells):
			self.categories(cell, i)

	"""
	This function add a new row to the table. If 'old' param is not None, it updates an existing row with same ID. 
	"""
	def data(self, cells, old=None):
		row = Row()
		row.update(cells, self)
		self.rows.append(row)
		if old:
			row.ID = old.ID

		return row

	"""
	This function takes input a list of cells and updates columns and rows of the table
	"""
	def update(self, cells):
		if (len(self.spec) == 0):
			self.header(cells)
		else:
			self.data(cells)

	"""
	This function takes input a csv file path and uses CSVReader Class to parse that file. 
	It uses the output of the CSVReader to create this table
	"""
	def fromCSV(self, f):
		reader = CSVReader(f)
		reader.parse()
		for row in reader.output:
			self.update(row)

	"""
	This generates a string format output of the column names
	"""
	def colsToString(self):
		res = ""
		for col in self.all['columns']:
			res += col.txt +","
		return res


	"""
	This function returns a list of dom scores for each in order using the function dom_func
	If dom_func is None, it uses the default dom function defined in Row Class
	"""
	def dom(self, dom_func=None):
		res = []
		for row in self.rows:
			res.append(row.dominate(self, dom_func))
		return res


if __name__ == '__main__':
	filename = sys.argv[1]
	tbl = Table()
	tbl.fromCSV(filename)
	scores = tbl.dom()


	sortes_scores_keys = sorted(enumerate(scores), key=lambda x: x[1])

	print tbl.spec
	n = len(scores)
	
	#for i in range(4, -1, -1):
	for i in range(5):
		ind = sortes_scores_keys[n-i-1][0]
		print tbl.rows[ind]

	print ""
	for i in range(4, -1, -1):
		ind = sortes_scores_keys[i][0]
		print tbl.rows[ind]

