import numpy as np

A=np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])
x=np.array([1,-2,3])
b=A.dot(x)
print(b)

print(np.linalg.cholesky(A))

#Using Cholesky Fractorization for solving Linear Equation.
#Ax=b --> L.dot(L.transpose()).x=b
#Solving Ly=b
#After solving L.transpose().x=y
#Fast way for solving linear equation.
#A must be a positive definite matrix.

def CholeskyLinearEquation(A,b):
    #Find x with Ax=b
    L=np.linalg.cholesky(A)
    y=(np.linalg.inv(L)).dot(b)
    x=(np.linalg.inv(np.transpose(L))).dot(y)
    return x


c=np.array([-68,-191,364])
x=CholeskyLinearEquation(A,b)
print(x)

