# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:46:28 2020

@author: 26039982
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

data = pd.read_excel("data.xlsx")

X = np.array(data[data.columns[:2]])
y = np.array(data.Class.values)


clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(X,y)

color = ['purple' if c == 0 else 'red' for c in y]

w = clf.coef_[0]
print(w)

a = -w[0] / w[1]

xx = np.linspace(1.99921,2.0013)
yy = a * xx - clf.intercept_[0] / w[1]

h0 = plt.plot(xx, yy, 'k-', label="hyper Plane")

plt.scatter(X[:, 0], X[:, 1], c = color)
plt.legend()
plt.show()