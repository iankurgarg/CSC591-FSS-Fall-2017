from datetime import datetime
import math
import pandas as pd
import numpy as np

import Util as util


class TemporalFeatures(object):
    def __init__(self):
        self.severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}
        self.severity_levels = ['enhancement', 'trivial', 'minor', 'normal', 'major', 'critical', 'blocker']

    def fit(self, data):
        self.temporal_dict =  util.generate_temporal_dict(data)
        print "temporal_dict generated"

    def transform(self, data):
        def temporal_feature1(x, n):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            total = 0
            for t in range(d-n, d+1):
                if t in self.temporal_dict:
                    total += sum(self.temporal_dict[t].values())
            return total

        def temporal_feature2(x, n):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            s = x['Severity']
            total = 0
            for t in range(d-n, d+1):
                if t in self.temporal_dict:
                    if s in self.temporal_dict[t]:
                        total += (self.temporal_dict[t][s])
            return total

        def temporal_feature3(x, n):
            d = (x['Opened'].date() - datetime(1970,1,1).date()).days
            sev = x['Severity']
            ind = self.severity_levels.index(sev)
            greater_s = self.severity_levels[ind:]
            total = 0
            for t in range(d-n, d+1):
                if t in self.temporal_dict:
                    for s in greater_s:
                        if s in self.temporal_dict[t]:
                            total += (self.temporal_dict[t][s])
            return total

        TMP1 = data.apply(lambda x: temporal_feature1(x, 7), axis=1)
        TMP2 = data.apply(lambda x: temporal_feature2(x, 7), axis=1)
        TMP3 = data.apply(lambda x: temporal_feature3(x, 7), axis=1)
        TMP4 = data.apply(lambda x: temporal_feature1(x, 30), axis=1)
        TMP5 = data.apply(lambda x: temporal_feature2(x, 30), axis=1)
        TMP6 = data.apply(lambda x: temporal_feature3(x, 30), axis=1)
        TMP7 = data.apply(lambda x: temporal_feature1(x, 1), axis=1)
        TMP8 = data.apply(lambda x: temporal_feature2(x, 1), axis=1)
        TMP9 = data.apply(lambda x: temporal_feature3(x, 1), axis=1)
        TMP10 = data.apply(lambda x: temporal_feature1(x, 3), axis=1)
        TMP11 = data.apply(lambda x: temporal_feature2(x, 3), axis=1)
        TMP12 = data.apply(lambda x: temporal_feature3(x, 3), axis=1)
        temporal_cols = ['TMP1', 'TMP2', 'TMP3', 'TMP4', 'TMP5', 'TMP6', 'TMP7', 'TMP8', 'TMP9', 'TMP10', 'TMP11', 'TMP12']
        temporal_features = [TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, TMP9, TMP10, TMP11, TMP12]

        temporal_data = pd.concat(temporal_features, axis=1)
        temporal_data.columns = temporal_cols
        return temporal_data

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)


if __name__ == '__main__':
    X_train= pd.read_csv('../data/train-test-split/train.csv', parse_dates=['Changed', 'Opened'])
    # temporal_dict = generate_temporal_dict(X_train)
    # print len(temporal_dict)

    tf = TemporalFeatures()
    temporal_data = tf.fit_transform(X_train)
    print temporal_data.head()
    print temporal_data.shape