# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 21:15:27 2020

@author: 34603956488ana
"""


import pandas as pd


x1 = pd.read_excel("quiz4data.xlsx",sheet_name="x1")
x2 = pd.read_excel("quiz4data.xlsx",sheet_name="x2")


covMatrixX1 = pd.DataFrame.cov(x1)
covMatrixX2 = pd.DataFrame.cov(x2)
covMatrixX1X2 = covMatrixX1+covMatrixX2

import numpy as np

# x2Trans = x2.T

# x2Trans = x2Trans.reset_index(drop=True)

# covMatrixX1 = covMatrixX1.reset_index(drop=True)
# covMatrixX1.columns = [0,1,2,3]


covarianceMAtrix = np.array([[2.66666667],[-5],[9.66666667],[4.33333333]]).dot(np.array([[[2.66666667,-5,9.66666667,4.33333333]]]))

cov_matrix = np.array([covarianceMAtrix[0][0],covarianceMAtrix[1][0],covarianceMAtrix[2][0],covarianceMAtrix[3][0]])


CovMatrixSwSb = np.dot(np.linalg.inv(covMatrixX1X2) , cov_matrix)


eigVal, eigVec = np.linalg.eig(CovMatrixSwSb)

W1 = eigVec[:,1]

for i in range(0,6):
    print(x1.iloc[i].dot(W1))
    
for i in range(0,6):
    print(x2.iloc[i].dot(W1))



#####################################################################
#################### SVM TEST     ##############################
####################################################################

from sklearn.svm import SVC

clf = SVC(C=9999999,gamma='auto',kernel='linear')

Y = [0,0,0,0,0,0,1,1,1,1,1,1]
all_feat = pd.concat([x1,x2])
all_feat = all_feat.reset_index(drop=True)

X_train = np.array(all_feat)
Y_train = np.array(Y)

clf.fit(X_train,Y_train)


clf.predict(X_train)

####################################################################
#################### LDA TEST  ##################################
####################################################################

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()

clf.fit(X_train,Y_train)

clf.predict(X_train)





