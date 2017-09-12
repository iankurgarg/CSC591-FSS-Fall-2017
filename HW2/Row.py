from Num import Num
import ID


class Row(object):
	def __init__(self):
		self.ID = ID.create()
		self.cells = []


	def update(self, cells, table):
		self.cells = cells[:]
		assert len(cells) == len(table.all['columns'])

		for i, col in enumerate(table.all['columns']):
			col.update(cells[i])

	def distance(self, row1, row2, table):
		dist = 0
		N = 1e-32

		s = 2
		p = 1/float(s)


		for i, col in enumerate(table.X['columns']):
			try:
				d = col.distance(row1.cells[i], row2.cells[i])
				n = 1
			except:
				d = 0
				n = 0

			dist += (d**s)
			N += (n**s)

		return (dist**p)/(N**p)

	def dominate1(self, row1, row2, table):
		e = 2.71828
		n = len(table.goals)
		sum1 = 0.0
		sum2 = 0.0

		for i, col in enumerate(table.goals):
			w = col.weight
			x = col.norm(row1.cells[i])
			y = col.norm(row2.cells[i])
			sum1 = sum1 - e**(w*(x-y)/n)
			sum2 = sum2 - e**(w*(y-x)/n)

		if ((sum1/n) < (sum2/n)):
			return True
		else:
			return False

	def dominate(self, row, table, func=None):
		if (func == None):
			func = self.dominate1

		res = 0
		for row2 in table.rows:
			if (row.ID != row2.ID):
				if func(row, row2, table):
					res += 1

		return res


