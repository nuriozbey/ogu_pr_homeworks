# -*- coding: utf-8 -*-
"""
Created on Mon May 11 02:15:34 2020

@author: 26039982
"""

import numpy as np


X = np.array([[9,-7,6,9],[10,0,0,1],[0,-3,1,5],[-7,0,4,9],[-4,5,-7,2],[5,8,-5,-8]])



################################################
mean_x1 = np.mean(X[:,0])
mean_x2 = np.mean(X[:,1])
mean_x3 = np.mean(X[:,2])
mean_x4 = np.mean(X[:,3])

#mean_vector = np.array([[mean_x1,mean_x2,mean_x3,mean_x4]])
mean_vector = np.array([[mean_x1],[mean_x2],[mean_x3],[mean_x4]])
print('Mean Vector:\n', mean_vector)
"""
Mean Vector:
 [[ 2.16666667  0.5        -0.16666667  3.        ]]
"""
#4*4 Blank Matrix
fi_matrix = np.zeros((4,4))

#((X[0,:] - mean_vector).T).dot((X[0,:] - mean_vector))

for i in range(0,X.shape[0]):
    fi_matrix += ((X[i,:].reshape(4,1) - mean_vector)).dot((X[i,:].reshape(4,1) - mean_vector).T)

eig_val_fi, eig_vec_fi = np.linalg.eig(fi_matrix)


for i in range(len(eig_val_fi)):
    eigvec_sc = eig_vec_fi[:,i].reshape(1,4).T

    print('Eigenvector {}: \n{}'.format(i+1, eigvec_sc))
    print('Eigenvalue {} from fi-matrix: {}'.format(i+1, eig_val_fi[i]))
    
"""
Eigenvector 1: 
[[ 0.03102376]
 [-0.56346243]
 [ 0.50969079]
 [ 0.64943276]]
Eigenvalue 1 from fi-matrix: 418.8345456833661
Eigenvector 2: 
[[-0.94197829]
 [ 0.1656021 ]
 [-0.10616178]
 [ 0.27199729]]
Eigenvalue 2 from fi-matrix: 272.0843823138898
Eigenvector 3: 
[[0.29458336]
 [0.75085368]
 [0.06325661]
 [0.58773973]]
Eigenvalue 3 from fi-matrix: 5.64273322801875
Eigenvector 4: 
[[ 0.15790844]
 [-0.30216682]
 [-0.85143618]
 [ 0.39851796]]
Eigenvalue 4 from fi-matrix: 20.605005441392862

"""


transformVector = eig_vec_fi[:,:2].reshape(4,2)  #selected from 2 eigenvalues

"""
array([[ 0.03102376, -0.94197829],
       [-0.56346243,  0.1656021 ],
       [ 0.50969079, -0.10616178],
       [ 0.64943276,  0.27199729]])

"""
outarr = []
for i in range(0,6):
    outarr.append(X[i,:].dot(transformVector))
    
    
newMatrixForm = X.dot(transformVector)

# array([[ 13.1264905 ,  -7.82601432],
#        [  0.9596704 ,  -9.14778558],
#        [  5.44724189,   0.75701839],
#        [  7.66649171,   8.61717653],
#        [ -5.21037721,   5.88305069],
#        [-12.09649667,  -5.03024409]])

newMatrixForm.shape
#Out[101]: (6, 2)

