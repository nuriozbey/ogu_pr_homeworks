# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:56:55 2020

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


X_train = train_data.iloc[:, :-1].values
y_train = train_data.iloc[:, 5].values

X_test = test_data.iloc[:,:].values

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3,metric="euclidean")


classifier.fit(X_train, y_train)

death_estimation_value = classifier.predict(X_test)
knn_index = classifier.kneighbors(X_test)[1]

out_data = test_data.copy()

out_data.insert(5,'death_estimation value',death_estimation_value)
out_data.insert(6,'knn_index_1',pd.DataFrame(knn_index)[0])
out_data.insert(7,'knn_index_2',pd.DataFrame(knn_index)[1])
out_data.insert(8,'knn_index_3',pd.DataFrame(knn_index)[2])

out_data.location = out_data.location.replace(locationDF.index,locationDF.values)
out_data.gender = out_data.gender.replace({1:'male' , 0 : 'female'})


trainDataVectorized = train_data.copy()
testDataVectorized = test_data.copy()

train_data.location = train_data.location.replace(locationDF.index,locationDF.values)
train_data.gender = train_data.gender.replace({1:'male' , 0 : 'female'})

test_data.location = test_data.location.replace(locationDF.index,locationDF.values)
test_data.gender = test_data.gender.replace({1:'male' , 0 : 'female'})

writer = pd.ExcelWriter('quiz2_out_nuriozbey.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
trainDataVectorized.to_excel(writer, sheet_name='trainDataVectorized',index=False)
testDataVectorized.to_excel(writer, sheet_name='testDataVectorized',index=False)
train_data.to_excel(writer, sheet_name='train_data',index=False)
out_data.to_excel(writer, sheet_name='test_data',index=False)
# Close the Pandas Excel writer and output the Excel file.
writer.save()


