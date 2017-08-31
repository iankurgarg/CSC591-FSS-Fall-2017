# Take filename as input or hardcode!
filename = 'test.csv'
# Declare List variables
true_length = [0]
filtered_length = [0]
data_types = []
ignore_list = []
main_list = []

# test: l = 'outlook,?temp,$meta,play'
def handle_header(line,data_types,ignore_list,main_list,true_length,filtered_length):
	#comment filtered out
	header_line = line.split('#')[0]
	header_line.strip()
	# if header_line[-1] == ',':
	#	header_line = header_line[0:-1]
	# store the lengths for checking the rows
	columns = header_line.split(',')
	true_length[0] = len(columns)
	# set the data types for each column
	for i in range(len(columns)):
		columns[i] = columns[i].strip()
		if columns[i][0] == '?':
			ignore_list.append(i)		# ? ==> ignore
		elif columns[i][0] == '$':
			data_types.append('int')
		else:
			data_types.append('str')
	# filter out the columns to ignore from the header
	for i in ignore_list:
		columns.pop(i)
	filtered_length[0] = len(columns)
	return columns

def handle_row(line,data_types,ignore_list,main_list):
	# remove comments
	row_line = line.split('#')[0]
	row_line.strip()
	# check for lengths
	columns = row_line.split(',')
	if len(columns) != true_length[0]:
		return []
	# remove colunms to ignore
	for i in ignore_list:
		columns.pop(i)
	if len(columns) != filtered_length[0]:
		return []
	# if column is of correct length check for data types
	for i in range(len(columns)):
		columns[i] = columns[i].strip()
		if data_types[i] == 'int':
			try:
				columns[i] = int(columns[i])
			except:
				return []
		if data_types[i] == 'str':
			try:
				columns[i] = str(columns[i])
			except:
				return []
	print columns
	return columns

def handle_file(filename):
	f = open(filename)
	lines = f.readlines()
	row_start = 1
	# handle header of the file, check for merge two lines
	l = lines[0].split('#')[0].strip()
	if l[-1] == ',':			# merge two lines if line ends with ','
		l = l+lines[1]
		row_start = 2
	header = handle_header(l,data_types,ignore_list,main_list,true_length,filtered_length)
	if len(header) != 0:
		main_list.append(header)
	# handle rows of the file, check for merge two lines
	i=row_start
	while i < len(lines):
		l = lines[i].split('#')[0].strip()
		if l[-1] == ',':		# merge two lines if line ends with ','
			l = l + lines[i+1]
			i = i + 1
		row = handle_row(l,data_types,ignore_list,main_list)
		if len(row) != 0:
			main_list.append(row)
		i = i + 1
	return

handle_file(filename)

for i in main_list:
	print i