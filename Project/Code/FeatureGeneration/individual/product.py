from datetime import datetime
import math
import pandas as pd
import numpy as np

import Util as util


class ProductFeatures(object):
    def __init__(self):
        self.severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}
        self.priority_levels = {'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4, 'P5': 5}

    def fit(self, data, f):
        self.f = f
        if f != 'Product' and f != 'Component':
            raise ValueError('Invalid Input: f can be either Product or Component')
        self.product_dict = util.generate_product_dict(X_train, f)
        self.product_dict_priority = util.generate_product_dict_priority(X_train, f)

        if f == 'Product':
            self.product_cols = ['PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5'] + ['PRO6', 'PRO7', 'PRO8', 'PRO9', 'PRO10', 'PRO11']
        else:
            self.product_cols = ['PRO12', 'PRO13', 'PRO14', 'PRO15', 'PRO16'] + ['PRO17', 'PRO18', 'PRO19', 'PRO20', 'PRO21', 'PRO22']
        print "product_dict generated"

    def transform(self, data):
        def product_feature1(x, f):
            return x[f]

        def product_feature2(x, f):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            p = x[f]
            sev = x['Severity']
            sub_data = self.product_dict[p]
            
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
            sub_data = self.product_dict[p]
            
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
            sub_data = self.product_dict[p]
            
            total = 0
            for s in sub_data:
                if (self.severity_levels[s] >= self.severity_levels[sev]):
                    for t in sub_data[s]:
                        if (t <= d):
                            total += sub_data[s][t]
            return total

        def product_feature5to9(x, f, P):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            prod = x[f]
            sev = x['Priority']
            sub_data = self.product_dict_priority[prod]

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
            if p in self.product_dict_priority:
                sub_data = self.product_dict_priority[p]
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
                plist += [self.priority_levels[p]]*pcount[p]

            med = np.median(plist)
            if np.isnan(med):
                return 5
            return int(med)

        def product_feature10(x, f):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            a = x[f]
            total = 0
            if a in self.product_dict_priority:
                sub_data = self.product_dict_priority[a]
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
                S += self.priority_levels[p]*pcount[p]
            
            if (N == 0):
                return 5
            return int(math.ceil(S/N))

        product_features= []
        PRO1 = data.apply(lambda x: product_feature1(x, self.f), axis=1)
        product_features.append(PRO1)
        PRO2 = data.apply(lambda x: product_feature2(x, self.f), axis=1)
        product_features.append(PRO2)
        print "2 features generated"
        PRO3 = data.apply(lambda x: product_feature3(x, self.f), axis=1)
        product_features.append(PRO3)
        PRO4 = data.apply(lambda x: product_feature4(x, self.f), axis=1)
        product_features.append(PRO4)
        PRO5 = data.apply(lambda x: product_feature5to9(x, self.f, 'P1'), axis=1)
        product_features.append(PRO5)
        print "5 features generated"
        PRO6 = data.apply(lambda x: product_feature5to9(x, self.f, 'P2'), axis=1)
        product_features.append(PRO6)
        PRO7 = data.apply(lambda x: product_feature5to9(x, self.f, 'P3'), axis=1)
        product_features.append(PRO7)
        print "7 features generated"
        PRO8 = data.apply(lambda x: product_feature5to9(x, self.f, 'P4'), axis=1)
        product_features.append(PRO8)
        PRO9 = data.apply(lambda x: product_feature5to9(x, self.f, 'P5'), axis=1)
        product_features.append(PRO9)
        print "9 features generated"
        PRO10 = data.apply(lambda x: product_feature10(x, self.f), axis=1)
        product_features.append(PRO10)
        PRO11 = data.apply(lambda x: product_feature11(x, self.f), axis=1)
        product_features.append(PRO11)
        print "all features generated"
        
        product_cols = ['PRO1', 'PRO2', 'PRO3', 'PRO4', 'PRO5'] + ['PRO6', 'PRO7', 'PRO8', 'PRO9', 'PRO10', 'PRO11']

        product_data = pd.concat(product_features, axis=1)
        product_data.columns = self.product_cols
        return product_data

    def fit_transform(self, data, f):
        # f can be 'Product' or 'Component' only
        self.fit(data, f)
        return self.transform(data)


if __name__ == '__main__':
    X_train= pd.read_csv('../data/train-test-split/train.csv', parse_dates=['Changed', 'Opened'])
    pf = ProductFeatures()
    pf.fit(X_train, 'Product')
    product_data = pf.transform(X_train)
    print product_data.head()
    print product_data.shape