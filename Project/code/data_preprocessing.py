# Author: Sanket Shahane

import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import re
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer


def preprocess_data(filename = '../data/processed/train_processed.csv'):
    print 'reading file...'
    df = pd.read_csv(filename)
    len(np.unique(df['Bug ID']))
    df.drop('Bug ID',axis=1,inplace=False).describe()
    #df.loc[df.Summary.isnull(),:]
    #df.iloc[[257,258],:]
    #df.columns
    df.dropna(inplace=True)
    df.isnull().sum()
    df.drop(['Bug ID'], axis=1, inplace=True)
    df.reset_index(inplace=True, drop=True)
    categorical_cols = ['Severity', 'PRO1', 'PRO12']
    other_cols = list(df.columns)
    for c in categorical_cols:
        other_cols.remove(c)
    other_cols.remove('Priority')
    other_cols.remove('Summary')
    tokenizer = RegexpTokenizer(r'\w+')
    stopwords = set(nltk.corpus.stopwords.words('english'))
    stemmer = PorterStemmer()

    def tokenize_stop_stem(text):
        try:
            tokens = tokenizer.tokenize(text)
            # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation) and stem
            filtered_tokens = []
            for token in tokens:
                token = token.lower()
                if token not in stopwords:
                    if not re.search('[0-9]', token):
                        try:
                            token = stemmer.stem(token)
                            filtered_tokens.append(token)
                        except UnicodeDecodeError:
                            print 'illeagal token ignored:',token
                            pass
        except UnicodeDecodeError:
            print 'illeagal token ignored:',token
            pass
        return filtered_tokens

    print 'Tokenizing Summary'
    countVect = CountVectorizer(input='content',lowercase=False, max_features=395996, tokenizer=tokenize_stop_stem, decode_error='ignore')
    countVector = countVect.fit_transform(df.Summary)
    countVector
    countVector.shape
    dummy_df = pd.get_dummies( df[categorical_cols] )
    dummy_df.head()
    dummy_sparse = sparse.csr_matrix(dummy_df.values)
    other_features = df[other_cols]
    for i in range(len(other_cols)):
        try:
            test = other_features.iloc[:,i].astype(float)
        except:
            print "problem is in column - ", i, other_cols[i]

    print 'Combining...'
    other_sparse = sparse.csr_matrix(other_features.values)
    inputDF = sparse.hstack((dummy_sparse,countVector),format="csr")
    inputDF = sparse.hstack((other_features,countVector),format="csr")
    print 'Preprocessing done!'
    return inputDF,df
