import math
import cmath
import numpy as np
import time


def mgen(r, c):
    return np.random.randint(10, size=(r, c))


def msum(M1, M2):
    return np.add(M1, M2)

def mcom(M1, M2):
    return np.dot(M1, M2)

def mdet(M):
    return np.linalg.det(M)

def minv(M):
    st = time.time()
    inverse = np.linalg.inv(M)
    et = time.time()
    return inverse, et-st

def msave(M, filename):
    np.savetxt(filename,M)

def save(M, filename):
    f = open(filename, "w")
    f.write(str(np.round(M)))
    f.close()

def mload(filename):
    return np.loadtxt(filename)

c = int(input("1-random\n2-from file\n"))
if c == 1:
    a = int(input('r:'))
    b = int(input('c:'))
    M1 = mgen(a, b) + mgen(a,b)*1j
    M2 = mgen(a, b) + mgen(a,b)*2j
else:
    M1 = mload("MATRIX1.txt")
    M2 = mload("MATRIX2.txt")


M3 = msum(M1, M2)
M4 = mcom(M1, M2)
M51 = mdet(M1)
M52 = mdet(M2)
M61, T61 = minv(M1)
M62, T62 = minv(M2)

print("Matrix 1:\n", M1)
print("Matrix 2:\n", M2)
print("Sum=\n", M3)
print("Comp=\n", M4)
print("Matrix 1 determinant=\n", np.round(M51))
print("Matrix 2 determinant=\n", np.round(M52))
print("Matrix 1 inversed=\n", M61)
print("Matrix 1 inversed=\n", M62)
print("Inverse time 1, 2:", T61, T62)
msave(M3, 'MATRIXSUM.txt')
msave(M4, 'MATRIXCOMP.txt')
save(M51, 'MATRIX1DET.txt')
save(M52, 'MATRIX2DET.txt')
msave(M61, 'MATRIX1INV.txt')
msave(M62, 'MATRIX2INV.txt')