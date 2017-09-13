import sys
import os
import argparse
import Config as config
from time import time


# CSVReader Class for parsing csv files
class CSVReader(object):
	def __init__(self, filename):
		self.path = os.path.abspath(filename)
		assert (os.path.exists(self.path)), "file doesn't exist"
		self.output = []
		self.columns = []
		self.original_columns = []
		self.data_types = []
		self.ignore_list = []


 	# Function to cleanup a line, removes whitespace and removes comments
	def cleanupLine(self, line):
		res = line.split(config.comment)[0]
		return res.strip()

	# Function to filter unwanted columns from a list. removes the elements based on ignore_list
	def filter_unwanted_cols(self, cells):
		res = cells
		for i in self.ignore_list:
			res.pop(i)

		return res

	# Function to detect data_types based on first character of header column names
	def detect_data_types(self):
		self.data_types = []
		for i in range(len(self.columns)):
			if self.columns[i][0] == '$' or self.columns[i][0] == '<' or self.columns[i][0] == '>':
				self.data_types.append(float)
			else:
				self.data_types.append(str)

	# Function to parse header
	def parseHeader(self, line):
		header_line = self.cleanupLine(line)
		
		self.columns = [x.strip() for x in header_line.split(config.sep)]
		
		self.ignore_list = [i for i,x in enumerate(self.columns) if x[0] == config.ignore]

		self.detect_data_types();
		
		self.original_columns = self.columns[:]

		self.columns = self.filter_unwanted_cols(self.columns)
		self.data_types = self.filter_unwanted_cols(self.data_types)

	# Function to parse a single row  
	def parseRow(self, line):
		row_line = self.cleanupLine(line)
		
		cells = row_line.split(config.sep)
		
		if len(cells) != len(self.original_columns):
			return None

		cells = self.filter_unwanted_cols(cells)
		
		if len(cells) != len(self.columns):
			return None

		for i in range(len(cells)):
			cells[i] = cells[i].strip()
			try:
				cells[i] = self.data_types[i](cells[i])
			except:
				return None		
		
		return cells

	# Main function to parse file. To be called from outside the class
	def parse(self):
		start_time = time()
		f = open(self.path)
		lines = f.readlines()
		i = 0

		l = self.cleanupLine(lines[i])
		
		if l[-1] == config.sep:
			l = l+lines[i+1]
			i += 1
		
		self.parseHeader(l)

		if self.columns:
			self.output.append(self.columns)

		# Skipping Header Line
		i += 1
		
		while i < len(lines):
			l = self.cleanupLine(lines[i])
			if l[-1] == ',':
				l = l + lines[i+1]
				i += 1
			row = self.parseRow(l)
			if row:
				self.output.append(row)
			else:
				print 'error: Invalid Line:'+str(i+1)+' Skipping'
			i += 1
		f.close()
		end_time = time() - start_time
		print "File Processed. Time Taken: ", end_time, " seconds"


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='CSV Reader')
	parser.add_argument('filename', metavar='path', type=str, help='path to the file to be processed')
	args = parser.parse_args()

	reader = CSVReader(args.filename)
	reader.parse()

	for i in reader.output:
		print i

