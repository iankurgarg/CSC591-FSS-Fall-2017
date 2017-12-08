import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from time import time
from sklearn.model_selection import train_test_split

from individual.temporal import *
from individual.product import *
from individual.author import *


# Performs Train-test split. Called just once. To Keep out the test data
# To reproduce the results exactly, keep random state = 42
# Expects the path of the file
# returns train and test data (including the y column)
# Also saves output to files
def split_data(file = '../data/total_fixed.csv', ratio=0.20):
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
    X_train.to_csv('../data/train-test-split/train.csv', index=False)
    X_test.to_csv('../data/train-test-split/test.csv', index=False)
    return X_train, X_test


# Prepares all types features and saves them in individual files one for each category
# For both train and test data. Expects both as input as dataframe
def prepare_all_features(X_train, X_test):
    # TEMORAL FEATURES

    tf = TemporalFeatures()
    temporal_train_data = tf.fit_transform(X_train)
    temoral_test_data = tf.transform(X_test)

    print "Temporal Features Generated"

    # Concatenating temporal data features with existing data
    train_data_with_temporal = pd.concat([data, temporal_train_data], axis=1)
    test_data_with_temporal = pd.concat([X_test, temoral_test_data], axis=1)

    # Save data with temporal features
    train_data_with_temporal.to_csv('../data/individual_features/train_data_with_temporal.csv', index=False)
    test_data_with_temporal.to_csv('../data/individual_features/test_data_with_temporal.csv', index=False)


    # AUTHOR REALTED FEATURES
    af = AuthorFeatures()
    author_train_data = af.fit_transform(X_train)
    author_test_data = af.transform(X_test)

    print "Author Features Generated"
    # Save data with temporal features
    author_train_data.to_csv('../data/individual_features/train_author_features.csv', index=False)
    author_test_data.to_csv('../data/individual_features/test_author_features.csv', index=False)

    # Product Features
    # Generating Product related features for Train Data
    pf = ProductFeatures()
    prod_features = pf.fit_transform(X_train, 'Product')
    prod_features.to_csv('../data/individual_features/train_prod_features.csv', index=False)

    # Generating Product related features for Test Data
    tprod_features = pf.transform(X_train)
    tprod_features.to_csv('../data/individual_features/test_prod_features.csv', index=False)

    print "Product Features Generated"

    # Generating component related features for Training Data
    pf = ProductFeatures()
    prod_features = pf.fit_transform(X_train, 'Component')
    prod_features.to_csv('../data/individual_features/train_component_features.csv', index=False)

    # Generating component related features for Test Data
    tprod_features = pf.transform(X_test)
    tprod_features.to_csv('../data/individual_features/test_component_features.csv', index=False)

    print "Component Features Generated"


# Merge all components into single file
def merge_all_features():
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


if __name__ == '__main__':
    X_train, X_test = split_data('../data/raw/total_fixed.csv')
    # X_train= pd.read_csv('../data/train-test-split/train.csv', parse_dates=['Changed', 'Opened'])
    # X_test = pd.read_csv('../data/train-test-split/test.csv', parse_dates=['Changed', 'Opened'])
    prepare_all_features(X_train, X_test)
    merge_all_features()
