from datetime import datetime

def generate_product_dict(data, f):
	product_dict = {}

	# Generates temporal dict which is used to generate temporal functions
	for i in range(len(data)):
	    row = data.iloc[i]
	    t = (row['Opened'].date() - datetime(1970,1,1).date()).days
	    p = row[f] # f = 'Component' or 'Product'
	    s = row['Severity']
	    
	    if p not in product_dict:
	        product_dict[p] = {}
	    if s not in product_dict[p]:
	        product_dict[p][s] = {}
	    if t not in product_dict[p][s]:
	        product_dict[p][s][t] = 0
	    product_dict[p][s][t] += 1
	return product_dict


def generate_product_dict_priority(data, f):
	product_dict_priority = {}
	for i in range(len(data)):
	    row = data.iloc[i]
	    t = (row['Opened'].date() - datetime(1970,1,1).date()).days
	    p = row[f] # f = 'Component' or 'Product'
	    s = row['Priority']
	    
	    if p not in product_dict_priority:
	        product_dict_priority[p] = {}
	    if s not in product_dict_priority[p]:
	        product_dict_priority[p][s] = {}
	    if t not in product_dict_priority[p][s]:
	        product_dict_priority[p][s][t] = 0
	    product_dict_priority[p][s][t] += 1
	return product_dict_priority