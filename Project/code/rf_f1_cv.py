## Measuring Per Class F1 scores as per the paper using KFold RF
import data_preprocessing
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
import numpy as np

inputDF,df = data_preprocessing.preprocess_data()

clf = RandomForestClassifier(class_weight="balanced", n_jobs=-1)
kf = KFold(n_splits=10)

cvscores = []
for train,test in kf.split(inputDF):
    train_input = inputDF[train]
    test_input = inputDF[test]
    train_output = df['Priority'][train]
    test_output = df['Priority'][test]
    clf.fit(train_input,train_output)
    prediction = clf.predict(test_input)
    scores = f1_score(test_output, prediction, average=None)
    print scores
    cvscores.append(scores)
return cvscores
print np.mean(cvscores)

print '\tP1\t\tP2\t\tP3\t\tP4\tP5'
print '\t',np.mean(cvscores,axis=0)
print cvscores