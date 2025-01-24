import numpy as np
import time

# Classical Gram-Schmidt process, following code similar to
# https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process#Numerical_stability
def gramschmidt(mat):
    U = np.zeros(len(mat),len(mat[0]))
    U[:][0] = mat[:][0] / norm(mat[:][0])
    for i in range(1,len(mat(0))):
        U[:][i] = mat[:][i]
        for j in range(0,i-1):
            U[:][i] = U[:][i] - np.dot(U[:][j],U[:][i])*U[:][j]
        U[:][i] = U[:][i] / np.linalg.norm(U[:][i])
    return U

# Projection of v onto u:
def projsub(v,u):
    return (v - np.matmul((np.dot(v,u)/np.dot(u,u)),u))


def stablergramschmidt(mat):
    U = np.zeros(len(mat), len(mat[0]))
    U[:][0] = mat[:][0] / norm(mat[:][0])
    for i in range(1, len(mat)):
        for j in range(0,len(mat[0])):
            U[i][j] = mat[]
    for i in range(0,len(mat(0))):
        U[:][i] = U[:][i] / np.linalg.norm(U[:][i])
    return U

def svd(mat):

    veigval, vtranspose = np.linalg.eig(np.matmul(np.transpose(mat),mat))
    sigma = np.diag(np.sqrt(veigval))
