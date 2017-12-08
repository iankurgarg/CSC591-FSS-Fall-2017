# Author: Sanket Shahane
import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
import re
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import CountVectorizer


class DataProcessor(object):
    def __init__(self):
        self.tokenizer = RegexpTokenizer(r'\w+')
        self.stopwords = set(nltk.corpus.stopwords.words('english'))
        self.stemmer = PorterStemmer()

        def tokenize_stop_stem(text):
            try:
                tokens = self.tokenizer.tokenize(text)
                # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation) and stem
                filtered_tokens = []
                for token in tokens:
                    token = token.lower()
                    if token not in self.stopwords:
                        if not re.search('[0-9]', token):
                            try:
                                token = self.stemmer.stem(token)
                                filtered_tokens.append(token)
                            except UnicodeDecodeError:
                                print 'illeagal token ignored:',token
                                pass
            except UnicodeDecodeError:
                print 'illeagal token ignored:',token
                pass
            return filtered_tokens

        self.countVect = CountVectorizer(input='content',lowercase=False, max_features=395996, 
                            tokenizer=tokenize_stop_stem, decode_error='ignore')

    def dropColumns(self, data):
        df = data.drop('Bug ID', axis=1, inplace=False)
        df.dropna(inplace=True)
        df.reset_index(inplace = True, drop = True)
        return df

    def categoricalCols(self):
        return ['Severity', 'PRO1', 'PRO12']

    def binaryCols(self):
        categorical_cols = self.categoricalCols()
        other_cols = self.all_cols[:]
        for c in categorical_cols:
            other_cols.remove(c)
        other_cols.remove('Priority')
        other_cols.remove('Summary')
        return other_cols

    # expected a pandas dataframe
    def fit(self, train):
        data = self.dropColumns(train)
        print "removed nan values"
        self.all_cols = list(data.columns)
        self.countVect.fit(data.Summary)
        print "count vectorizer finished fitting"

    def transform(self, df):
        data = self.dropColumns(df)
        countVector = self.countVect.transform(data.Summary)
        print "count vector finished transforming"
        dummy_df = pd.get_dummies( data[self.categoricalCols()] )
        print "dummy variables created"
        dummy_sparse = sparse.csr_matrix(dummy_df.values)
        other_features = data[self.binaryCols()]

        other_sparse = sparse.csr_matrix(other_features.values)
        inputDF = sparse.hstack((dummy_sparse,countVector),format="csr")
        inputDF = sparse.hstack((other_features,countVector),format="csr")
        print "created a sparse matrix of all features"
        return inputDF, data

    def fit_transform(self, df):
        self.fit(df)
        return self.transform(df)
