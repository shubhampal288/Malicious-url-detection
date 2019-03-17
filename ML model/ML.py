#Import libraries for ML model
import pandas as pd
import os
import pandas
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import numpy
from sklearn import svm
from sklearn import cross_validation as cv
import matplotlib.pylab as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#From dataset using only those column that are used as feature vector in ML

def return_nonstring_col(data_cols):
    cols_to_keep=[]
    train_cols=[]
    for col in data_cols:
        if col!='url' and col!='host' and col!='path':
            cols_to_keep.append(col)
            if col!='malicious':
                train_cols.append(col)
    return [cols_to_keep,train_cols]


#This part is user specific so modify this according to your need.
"""
fila="featurenow.csv"
base="C:\Users\SHUBHAM\Desktop\Minor\data"
filen=os.path.join(base,fila)
training=pd.read_csv(filen)
col_to_keep,train_col= return_nonstring_col(training.columns)
training[train_col]=training[train_col].replace('',np.nan,regex=True)
"""

#Random Forest classifier

rf=RandomForestClassifier(n_estimators=15)
train_x, test_x, train_y, test_y = train_test_split(training[train_col], training['malicious'], train_size=0.8, random_state=42)
print rf.fit(train_x,train_y)

#Output recieved
"""
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=15, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)
"""

predict=rf.predict(test_x)
from sklearn.metrics import accuracy_score
score=accuracy_score(test_y,predict)
print score*100

#Accuracy from above method
"""
98.62517185351831
"""


clf = svm.SVC()
print clf.fit(train_x, train_y)
#Output recieved
"""
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
"""
predict=clf.predict(test_x)
#querycsv.to_csv("output.csv",index=False)
#print querycsv[['URL','result']]
from sklearn.metrics import accuracy_score
score=accuracy_score(test_y,predict)
print score*100
#Accuracy from above method
"""
78.69822485207101
"""

#Removing those feature whose contribution is low

def return_nonstring_col(data_cols):
    cols_to_keep=[]
    train_cols=[]
    for col in data_cols:
        if col!='URL' and col!='host' and col!='path':
            cols_to_keep.append(col)
            if col!='malicious' and col!='ASNno' and col!='IPaddress_presence' and col!='whoisinfo' and col!='rank_country' and col!='rank_host' and col!='numTld':
                train_cols.append(col)
    return [cols_to_keep,train_cols]
"""
fila="featurenow.csv"
base="C:\Users\SHUBHAM\Desktop\Minor\data"
filen=os.path.join(base,fila)
training=pd.read_csv(filen)
"""
col_to_keep,train_col= return_nonstring_col(training.columns)
training[train_col]=training[train_col].replace('',np.nan,regex=True)
rf=RandomForestClassifier(n_estimators=15)
train_x, test_x, train_y, test_y = train_test_split(training[train_col], training['malicious'], train_size=0.8, random_state=42)
print rf.fit(train_x,train_y)


predict=rf.predict(test_x)
from sklearn.metrics import accuracy_score
score=accuracy_score(test_y,predict)
print score*100
#Accuracy remain same even after removinf certain features and this is what we want to proove
"""
98.60017497812773
"""

