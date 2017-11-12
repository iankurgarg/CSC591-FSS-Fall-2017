
# coding: utf-8

# Import libraries required

# In[52]:

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


# Read data in

# In[53]:

data = pd.read_csv('data/total_fixed.csv', parse_dates=['Changed', 'Opened'])
cols = data.columns

n_rows = len(data)
n_cols = len(cols)
bugIDs = data['Bug ID']
print data.head()
print bugIDs.head()


# In[3]:

print data['Changed'].head()
print set(data['Severity'])

severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}


# In[4]:

print data['Changed'].head()
print set(data['Severity'])

severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}


# In[5]:

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


# In[6]:

# data['Opened'].map(lambda x: tmp1(x, 7))
np_opened = np.array(data['Opened'])
np_opened[0] - np.timedelta64(7, 'D')


# In[7]:

tmp1(np_opened[0], 7)


# In[8]:

sum(np_opened < np_opened[0])[0]


# In[9]:

def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df



def multiply_columns(data):
    data['TMP1'] = data['Openend'].apply(lambda x: tmp1(x, 7))
    return data

# TMP1 = np.apply_along_axis(lambda x: tmp1(x, 7), 1, np_opened)
iris = parallelize_dataframe(iris, multiply_columns)





