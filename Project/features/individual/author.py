from datetime import datetime
import math
import pandas as pd
import numpy as np

import Util as util


class AuthorFeatures(object):
    def __init__(self):
        self.priority_levels = {'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4, 'P5': 5}

    def fit(self, data):
        self.author_dict =  util.generate_author_dict(data)
        print "author_dict generated"

    def transform(self, data):
        def author_feature1(x):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            a = x['Assignee']
            total = 0
            if a in self.author_dict:
                sub_data = self.author_dict[a]
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

        def author_feature2(x):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            a = x['Assignee']
            total = 0
            if a in self.author_dict:
                sub_data = self.author_dict[a]
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

        def author_feature3(x):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            a = x['Assignee']
            total = 0
            if a in self.author_dict:
                sub_data = self.author_dict[a]
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

        AUT1 = data.apply(lambda x: author_feature1(x), axis=1)
        print "first feature generated"
        AUT2 = data.apply(lambda x: author_feature2(x), axis=1)
        print "second feature generated"
        AUT3 = data.apply(lambda x: author_feature3(x), axis=1)
        print "third feature generated"
        author_cols = ['AUT1', 'AUT2', 'AUT3']
        author_features = [AUT1, AUT2, AUT3]

        author_data = pd.concat(author_features, axis=1)
        author_data.columns = author_cols
        return author_data

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)

if __name__ == '__main__':
    X_train= pd.read_csv('../data/train-test-split/train.csv', parse_dates=['Changed', 'Opened'])
    # author_dict = util.generate_author_dict(X_train)
    # print len(author_dict)

    af = AuthorFeatures()
    author_data = af.fit_transform(X_train)
    print author_data.shape
    print author_data.head()