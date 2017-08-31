import sys
import os
import argparse



class CSVReader(object):
	def __init__(self, filename):
		self.path = os.path.abspath(filename)
		assert (os.path.exists(self.path)), "file doesn't exist"
		self.main_list = []
		self.true_length = [0]
		self.filtered_length = [0]
		self.data_types = []
		self.ignore_list = []

	# test: l = 'outlook,?temp,$meta,play'
	def handle_header(self, line):
		#comment filtered out
		header_line = line.split('#')[0]
		header_line.strip()
		# if header_line[-1] == ',':
		#	header_line = header_line[0:-1]
		# store the lengths for checking the rows
		columns = header_line.split(',')
		self.true_length[0] = len(columns)
		# set the data types for each column
		for i in range(len(columns)):
			columns[i] = columns[i].strip()
			if columns[i][0] == '?':
				self.ignore_list.append(i)		# ? ==> ignore
			elif columns[i][0] == '$':
				self.data_types.append('int')
			else:
				self.data_types.append('str')
		# filter out the columns to ignore from the header
		for i in self.ignore_list:
			columns.pop(i)
		self.filtered_length[0] = len(columns)
		return columns

	def handle_row(self, line):
		# remove comments
		row_line = line.split('#')[0]
		row_line.strip()
		# check for lengths
		columns = row_line.split(',')
		if len(columns) != self.true_length[0]:
			return []
		# remove colunms to ignore
		for i in self.ignore_list:
			columns.pop(i)
		if len(columns) != self.filtered_length[0]:
			return []
		# if column is of correct length check for data types
		for i in range(len(columns)):
			columns[i] = columns[i].strip()
			if self.data_types[i] == 'int':
				try:
					columns[i] = int(columns[i])
				except:
					return []
			if self.data_types[i] == 'str':
				try:
					columns[i] = str(columns[i])
				except:
					return []
		#print columns
		return columns

	def parse(self):
		f = open(self.path)
		lines = f.readlines()
		row_start = 1
		# handle header of the file, check for merge two lines
		l = lines[0].split('#')[0].strip()
		if l[-1] == ',':			# merge two lines if line ends with ','
			l = l+lines[1]
			row_start = 2
		header = self.handle_header(l)
		if len(header) != 0:
			self.main_list.append(header)
		# handle rows of the file, check for merge two lines
		i=row_start
		while i < len(lines):
			l = lines[i].split('#')[0].strip()
			if l[-1] == ',':		# merge two lines if line ends with ','
				l = l + lines[i+1]
				i = i + 1
			row = self.handle_row(l)
			if len(row) != 0:
				self.main_list.append(row)
			i = i + 1
		f.close()
		return

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='CSV Reader')
	parser.add_argument('filename', metavar='path', type=str, help='path to the file to be processed')
	args = parser.parse_args()

	reader = CSVReader(args.filename)
	reader.parse()
	for i in reader.main_list:
		print i

