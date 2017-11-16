import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from time import time
from sklearn.model_selection import train_test_split


def train_test_split(file = '../data/total_fixed.csv', ratio=0.20):
    df = pd.read_csv(file, parse_dates=['Changed', 'Opened'])
    cols = df.columns

    #Train / Test Split - 80:20

    X_train, X_test, y_train, y_test = train_test_split(df.drop('Priority', axis=1), df.Priority, 
                                        test_size=ratio, random_state=42, stratify=df.Priority)


    X_train['Priority'] = y_train
    X_test['Priority'] = y_test

    print "Train shape = ",  X_train.shape
    print "Test Shape = ", X_test.shape

    # Save Splitted data to disk
    X_train.to_csv('../data/train.csv', index=False)
    X_test.to_csv('../data/test.csv', index=False)
    return X_train, X_test


# severity_levels = ['enhancement', 'trivial', 'minor', 'normal', 'major', 'critical', 'blocker']
from individual.temporal import *
from individual.product import *
from individual.author import *

X_train= pd.read_csv('../data/train.csv', parse_dates=['Changed', 'Opened'])
X_test = pd.read_csv('../data/test.csv', parse_dates=['Changed', 'Opened'])


# TEMORAL FEATURES
temporal_train_data = generate_temporal_features(X_train)
temoral_test_data = generate_temporal_features(X_test)

print temporal_train_data.shape
print temoral_test_data.shape

# Concatenating temporal data features with existing data
train_data_with_temporal = pd.concat([data, temporal_train_data], axis=1)
test_data_with_temporal = pd.concat([X_test, temoral_test_data], axis=1)

# Save data with temporal features
train_data_with_temporal.to_csv('../data/train_data_with_temporal.csv', index=False)
test_data_with_temporal.to_csv('../data/test_data_with_temporal.csv', index=False)


# ### Author Realted Feature Generation
print len(set(data['Assignee']))
print data.shape


priority_levels = {'P1': 1, 'P2': 2, 'P3': 3, 'P4': 4, 'P5': 5}


# AUTHOR REALTED FEATURES

author_train_data = generate_author_features(X_train)
author_test_data = generate_author_features(X_test)

print author_train_data.head()
print author_test_data.head()

# Save data with temporal features
author_train_data.to_csv('../data/train_author_features.csv', index=False)
author_test_data.to_csv('../data/test_author_features.csv', index=False)


# ## Product Features
# 
# - This has a total of 22 features.
# - 11 are for 'Product' Feature and 11 are for 'Component' Feature


# ### Generating Product related features for Train Data

prod1 = generate_product_features1(data, 'Product')
prod2 = generate_product_features2(data, 'Product')
prod_features = pd.concat([prod1, prod2], axis=1)
prod_features.to_csv('../data/train_prod_features.csv', index=False)

# Generating Product related features for Test Data

tprod1 = generate_product_features1(X_test, 'Product') 
tprod2 = generate_product_features2(X_test, 'Product') `
tprod_features = pd.concat([tprod1, tprod2], axis=1)
tprod_features.to_csv('../data/test_prod_features.csv', index=False)


# ### Generating component related features for Training Data
prod3 = generate_product_features1(data, 'Component')
prod4 = generate_product_features2(data, 'Component')
prod_features = pd.concat([prod3, prod4], axis=1)
prod_features.columns = ['PRO12', 'PRO13', 'PRO14', 'PRO15', 'PRO16', 'PRO17', 'PRO18', 'PRO19', 'PRO20', 'PRO21', 'PRO22']
prod_features.to_csv('../data/train_component_features.csv', index=False)


# ### Generating component related features for Test Data
tprod3 = generate_product_features1(X_test, 'Component')
tprod4 = generate_product_features2(X_test, 'Component')
tprod_features = pd.concat([tprod3, tprod4], axis=1)
tprod_features.shape
tprod_features.columns = ['PRO12', 'PRO13', 'PRO14', 'PRO15', 'PRO16', 'PRO17', 'PRO18', 'PRO19', 'PRO20', 'PRO21', 'PRO22']
tprod_features.to_csv('../data/test_component_features.csv', index=False)


# Merge all components into single file

# Original Training and testing data. For getting columns, priority, severity, bugID
train_original= pd.read_csv('../data/train-test-split/train.csv', parse_dates=['Changed', 'Opened'])
test_original = pd.read_csv('../data/train-test-split/test.csv', parse_dates=['Changed', 'Opened'])

# Temporal Features
train_temporal = pd.read_csv('../data/individual_features/train_data_with_temporal.csv')
test_temporal = pd.read_csv('../data/individual_features/test_data_with_temporal.csv')

# author Features
train_author = pd.read_csv('../data/individual_features/train_author_features.csv')
test_author = pd.read_csv('../data/individual_features/test_author_features.csv')

# Product Features
train_prod = pd.read_csv('../data/individual_features/train_prod_features.csv')
test_prod = pd.read_csv('../data/individual_features/test_prod_features.csv')

# Component Features
train_comp = pd.read_csv('../data/individual_features/train_component_features.csv')
test_comp = pd.read_csv('../data/individual_features/test_component_features.csv')

tmp_cols = list(train_temporal.columns)[13:]

train_final = [train_original.loc[:,['Bug ID', 'Severity', 'Priority', 'Summary']], train_temporal.loc[:, tmp_cols], 
               train_author,  train_prod, train_comp]

train_final = pd.concat(train_final, axis=1)
train_final.to_csv('../data/processed/train_processed.csv', index=False)


test_final = [test_original.loc[:,['Bug ID', 'Severity', 'Priority', 'Summary']], test_temporal.loc[:, tmp_cols], 
               test_author,  test_prod, test_comp]

test_final = pd.concat(test_final, axis=1)
test_final.to_csv('../data/processed/test_processed.csv', index=False)

