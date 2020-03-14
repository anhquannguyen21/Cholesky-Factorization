import numpy as np

def CholeskyFactorization(A):
    #A is positive definite matrix.
    n=A.shape[0]
    L=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            if(i==j):
                temp=A[i,i]-np.sum(L[i,:i]*L[i,:i])
                if temp<0.0:
                    return 0.0
                L[i][i]=np.sqrt(temp)
            else:
                L[i][j]=(A[i][j]-np.sum(L[i,:j]*L[j,:j]))/(L[j][j])
    return L

A=np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])
L=CholeskyFactorization(A)
print(L)