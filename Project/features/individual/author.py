from datetime import datetime
import math


priority_levels = {'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4, 'P5': 5}

def generate_author_dict(data):
	author_dict = {}

	# Generates temporal dict which is used to generate temporal functions
	for i in range(len(data)):
	    row = data.iloc[i]
	    t = (row['Opened'].date() - datetime(1970,1,1).date()).days
	    a = row['Assignee']
	    p = row['Priority']
	    if (a not in author_dict):
	        author_dict[a] = {}
	    if (p not in author_dict[a]):
	        author_dict[a][p] = {}
	    if (t not in author_dict[a][p]):
	        author_dict[a][p][t] = 0
	    author_dict[a][p][t] += 1
	return author_dict


X_train= pd.read_csv('../data/train.csv', parse_dates=['Changed', 'Opened'])
author_dict = generate_author_dict(X_train)
print len(author_dict)


def author_feature1(x):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    a = x['Assignee']
    total = 0
    if a in author_dict:
        sub_data = author_dict[a]
    else:
        return 5
    
    pcount = {}
    
    for p in sub_data:
        s = 0
        for k in sub_data[p]:
            if k <= d:
                s += sub_data[p][k]
        
        pcount[p] = s
    
    N = 0;
    S = 0.0;
    for p in pcount:
        N += pcount[p]
        S += priority_levels[p]*pcount[p]
    
    if (N == 0):
        return 5
    return int(math.ceil(S/N))

def author_feature2(x):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    a = x['Assignee']
    total = 0
    if a in author_dict:
        sub_data = author_dict[a]
    else:
        return 5
    
    pcount = {}
    
    for p in sub_data:
        s = 0
        for k in sub_data[p]:
            if k <= d:
                s += sub_data[p][k]
        
        pcount[p] = s
    
    plist = []
    for p in pcount:
        plist += [priority_levels[p]]*pcount[p]

    med = np.median(plist)
    if np.isnan(med):
        return 5
    return int(med)

def author_feature3(x):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    a = x['Assignee']
    total = 0
    if a in author_dict:
        sub_data = author_dict[a]
    else:
        return 5
    
    pcount = 0
    
    for p in sub_data:
        s = 0
        for k in sub_data[p]:
            if k <= d:
                s += sub_data[p][k]
        
        pcount += s
        
    return pcount

def generate_author_features(data2):
    AUT1 = data2.apply(lambda x: author_feature1(x), axis=1)
    AUT2 = data2.apply(lambda x: author_feature2(x), axis=1)
    AUT3 = data2.apply(lambda x: author_feature3(x), axis=1)
    author_cols = ['AUT1', 'AUT2', 'AUT3']
    author_features = [AUT1, AUT2, AUT3]

    author_data = pd.concat(author_features, axis=1)
    author_data.columns = author_cols
    return author_data