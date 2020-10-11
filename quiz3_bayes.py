# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:37:27 2020

@author: 34603956488ana
"""



import pandas as pd


data = pd.read_excel("quiz2data.xlsx",sheet_name="train_set")

train_data = data.loc[:472]

##  bazı tarih girilmiş death değerleri 1 yapıldı.

# train_data.death.value_counts() # veriseti dağılımı
# Out[25]: 
# 0    441
# 1     32

train_data.gender = train_data["gender"].replace({'male': 1, 'female': 0})
train_data = train_data.fillna(0)



test_data = pd.read_excel("quiz2data.xlsx",sheet_name="test_set")
test_data = test_data[data.columns[:5]]
test_data.gender = test_data["gender"].replace({'male': 1, 'female': 0})
test_data = test_data.fillna(0)


all_loc = pd.concat([test_data.location,train_data.location])
locationDF = pd.DataFrame(all_loc.value_counts().index)

train_data.location = train_data.location.replace(locationDF.values,locationDF.index)
test_data.location = test_data.location.replace(locationDF.values,locationDF.index)

# import numpy as np
# import matplotlib.pyplot as plt


X_train = train_data.iloc[:, 2:-1].values # son 3 sütün alındı 
y_train = train_data.iloc[:, 5].values # label değerleri

X_test = test_data.iloc[:,2:].values # son 3 sütün alındı 

from sklearn.naive_bayes import CategoricalNB

#Create a Gaussian Classifier
model = CategoricalNB() # caterogical naive bayes algoritması kullanıldı

# Train the model using the training sets
model.fit(X_train,y_train)


testResult = model.predict_proba(X_test) # 2 class için sonuclar 0 yaşıyor 1 ölüm


testResultDF = pd.DataFrame(columns=["0 yaşam","1 ölüm"],data=testResult)

DeathEstimation = []
for i in range(0,len(testResultDF)):
    if testResultDF["1 ölüm"][i] > 0.50 :
        DeathEstimation.append(1)
    else:
        DeathEstimation.append(0)
testResultDF.insert(0,"death_estimation value",DeathEstimation)

writer = pd.ExcelWriter('quiz3_bayes_classification_out_nuriozbey.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
train_data.to_excel(writer, sheet_name='trainDataVectorized',index=False)
test_data.to_excel(writer, sheet_name='testDataVectorized',index=False)
testResultDF.to_excel(writer, sheet_name='test_data_probablty',index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()

