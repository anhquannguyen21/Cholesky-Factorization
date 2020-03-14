import numpy as np

A=np.array([[1,-2j],[2j,5]])
print(A)

#A=L.dot(L^H) with A is positive definite matrix and L is lower triangular matrix.

L=np.linalg.cholesky(A)
print(L)
print(L.dot(L.T.conj()))

a=np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])

L=np.linalg.cholesky(a)
print(L)
L_T=L.transpose()
print(L.dot(L_T))

