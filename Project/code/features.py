import pandas as pd
import numpy as np
from datetime import datetime, timedelta


data = pd.read_csv('../data/total_fixed.csv', parse_dates=['Changed', 'Opened'])
cols = data.columns

n_rows = len(data)
n_cols = len(cols)
bugIDs = data['Bug ID']
print data.head()
print bugIDs.head()

print data['Changed'].head()
print set(data['Severity'])

severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}

print data['Changed'].head()
print set(data['Severity'])

severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}


# Generating Temporal Features
def tmp1(x, n):
    return sum(np_opened < x) - sum (np_opened < (x - np.timedelta64(n, 'D')))

def tmp2(x, n):
    subdata = data[data['Severity'] == x['Severity']]
    return sum(subdata['Opened'] < x['Opened']) - sum (subdata['Opened'] < (x['Opened'] - timedelta(days=n)))

def subdatagen(x, severity):
    if severity_levels[x['Severity']] >= severity_levels[severity]:
        return True
    else:
        return False

def tmp3(i, n):
    condn = data.apply(lambda x: subdatagen(x, i['Severity']), axis=1)
    subdata = data[condn]
    return sum(subdata['Opened'] < x['Opened']) - sum (subdata['Opened'] < (x['Opened'] - timedelta(days=n)))


def parallelize(data, func);
	