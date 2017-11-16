from datetime import datetime


severity_levels = {'enhancement': 0, 'trivial' : 1, 'minor' : 2, 'normal' : 3, 'major' : 4, 'critical' : 5, 'blocker' : 6}

def generate_temporal_dict(data):
    temporal_dict = {}

    # Generates temporal dict which is used to generate temporal functions
    # This should be based only on training data
    for i in range(len(data)):
        row = data.iloc[i]
        t = (row['Opened'].date() - datetime(1970,1,1).date()).days
        s = row['Severity']
        if (t not in temporal_dict):
            temporal_dict[t] = {}
        if (s not in temporal_dict[t]):
            temporal_dict[t][s] = 0
        temporal_dict[t][s] += 1
    return temporal_dict


X_train= pd.read_csv('../data/train.csv', parse_dates=['Changed', 'Opened'])
temporal_dict = generate_temporal_dict(X_train)
print len(temporal_dict)

# Function for generating temporal features (Fast version)
def temporal_feature1(x, n):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    total = 0
    for t in range(d-n, d+1):
        if t in temporal_dict:
            total += sum(temporal_dict[t].values())
    return total

def temporal_feature2(x, n):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    s = x['Severity']
    total = 0
    for t in range(d-n, d+1):
        if t in temporal_dict:
            if s in temporal_dict[t]:
                total += (temporal_dict[t][s])
    return total

def temporal_feature3(x, n):
    d = (x['Opened'].date() - datetime(1970,1,1).date()).days
    sev = x['Severity']
    ind = severity_levels.index(sev)
    greater_s = severity_levels[ind:]
    total = 0
    for t in range(d-n, d+1):
        if t in temporal_dict:
            for s in greater_s:
                if s in temporal_dict[t]:
                    total += (temporal_dict[t][s])
    return total



## Overall function to generate temporal features

def generate_temporal_features(data2):
    TMP1 = data2.apply(lambda x: temporal_feature1(x, 7), axis=1)
    TMP2 = data2.apply(lambda x: temporal_feature2(x, 7), axis=1)
    TMP3 = data2.apply(lambda x: temporal_feature3(x, 7), axis=1)
    TMP4 = data2.apply(lambda x: temporal_feature1(x, 30), axis=1)
    TMP5 = data2.apply(lambda x: temporal_feature2(x, 30), axis=1)
    TMP6 = data2.apply(lambda x: temporal_feature3(x, 30), axis=1)
    TMP7 = data2.apply(lambda x: temporal_feature1(x, 1), axis=1)
    TMP8 = data2.apply(lambda x: temporal_feature2(x, 1), axis=1)
    TMP9 = data2.apply(lambda x: temporal_feature3(x, 1), axis=1)
    TMP10 = data2.apply(lambda x: temporal_feature1(x, 3), axis=1)
    TMP11 = data2.apply(lambda x: temporal_feature2(x, 3), axis=1)
    TMP12 = data2.apply(lambda x: temporal_feature3(x, 3), axis=1)
    temporal_cols = ['TMP1', 'TMP2', 'TMP3', 'TMP4', 'TMP5', 'TMP6', 'TMP7', 'TMP8', 'TMP9', 'TMP10', 'TMP11', 'TMP12']
    temporal_features = [TMP1, TMP2, TMP3, TMP4, TMP5, TMP6, TMP7, TMP8, TMP9, TMP10, TMP11, TMP12]

    temporal_data = pd.concat(temporal_features, axis=1)
    temporal_data.columns = temporal_cols
    return temporal_data