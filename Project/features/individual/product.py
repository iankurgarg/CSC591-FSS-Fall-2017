from datetime import datetime
import math
from Util import *


X_train= pd.read_csv('../data/train.csv', parse_dates=['Changed', 'Opened'])
product_dict = generate_product_dict(X_train, 'Product')
print len(product_dict)
product_dict_priority = generate_product_dict_priority(X_train, 'Product')
print len(product_dict_priority)


def product_feature1(x, f='Product'):
    return x[f]

def product_feature2(x, f='Product'):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    p = x[f]
    sev = x['Severity']
    sub_data = product_dict[p]
    
    total = 0
    for s in sub_data:
        for t in sub_data[s]:
            if (t <= d):
                total += sub_data[s][t]
    return total

def product_feature3(x, f):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    p = x[f]
    sev = x['Severity']
    sub_data = product_dict[p]
    
    total = 0
    if sev in sub_data:
        for t in sub_data[sev]:
            if (t <= d):
                total += sub_data[sev][t]
    return total

def product_feature4(x, f):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    p = x[f]
    sev = x['Severity']
    sub_data = product_dict[p]
    
    total = 0
    for s in sub_data:
        if (severity_levels[s] >= severity_levels[sev]):
            for t in sub_data[s]:
                if (t <= d):
                    total += sub_data[s][t]
    return total

def product_feature5to9(x, f, P):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    prod = x[f]
    sev = x['Priority']
    sub_data = product_dict_priority[prod]

    total = 0
    N = 0
    if P in sub_data:
        for t in sub_data[P]:
            if (t <= d):
                total += sub_data[P][t]
    for P in sub_data:
        for t in sub_data[P]:
            if (t <= d):
                N += sub_data[P][t]
    
    if N == 0:
        return 0.0
    return float(total)/N

def product_feature11(x, f):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    p = x[f]
    total = 0
    if p in product_dict_priority:
        sub_data = product_dict_priority[p]
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

def product_feature10(x, f):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    a = x[f]
    total = 0
    if a in product_dict_priority:
        sub_data = product_dict_priority[a]
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

def generate_product_features1(data2, f):
    product_features= []
    PRO1 = data2.apply(lambda x: product_feature1(x, f), axis=1)
    product_features.append(PRO1)
    PRO2 = data2.apply(lambda x: product_feature2(x, f), axis=1)
    product_features.append(PRO2)
    PRO3 = data2.apply(lambda x: product_feature3(x, f), axis=1)
    product_features.append(PRO3)
    PRO4 = data2.apply(lambda x: product_feature4(x, f), axis=1)
    product_features.append(PRO4)
    PRO5 = data2.apply(lambda x: product_feature5to9(x, f, 'P1'), axis=1)
    product_features.append(PRO5)
    
    product_cols = ['PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5']

    product_data = pd.concat(product_features, axis=1)
    product_data.columns = product_cols
    return product_data


def generate_product_features2(data2, f):
    product_features= []
    PRO6 = data2.apply(lambda x: product_feature5to9(x, f, 'P2'), axis=1)
    product_features.append(PRO6)
    PRO7 = data2.apply(lambda x: product_feature5to9(x, f, 'P3'), axis=1)
    product_features.append(PRO7)
    PRO8 = data2.apply(lambda x: product_feature5to9(x, f, 'P4'), axis=1)
    product_features.append(PRO8)
    PRO9 = data2.apply(lambda x: product_feature5to9(x, f, 'P5'), axis=1)
    product_features.append(PRO9)
    PRO10 = data2.apply(lambda x: product_feature10(x, f), axis=1)
    product_features.append(PRO10)
    PRO11 = data2.apply(lambda x: product_feature11(x, f), axis=1)
    product_features.append(PRO11)
    
    product_cols = ['PRO6', 'PRO7', 'PRO8', 'PRO9', 'PRO10', 'PRO11']

    product_data = pd.concat(product_features, axis=1)
    product_data.columns = product_cols
    return product_data