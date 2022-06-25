# -*- coding: utf-8 -*-
"""assig1_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PYamD-45xbOC-A_P6TeJLvFDGY3e9ehe
"""

import numpy as np
from math import *
import cv2
import matplotlib.pyplot as plt

print("ANSWER 3:")
print()
#input matrix
#matrix = np.array([[1,2],[3,4]])
#matrix = np.array([[1,3,5],[7,9,11],[13,15,17]])
#matrix = np.eye(3)
#matrix = cv2.imread('barbara.png', 0)
matrix = cv2.imread('x5.bmp', 0)

# print(matrix)
# print()

#cmap --> This is the color mapping. If this is not used in this case matplotlib will try to plot 
#the gray images as a RGB image because it has a depth of 3 channels without the 0 passed in cv2.imread()

plt.figure(figsize=(10,10))
plt.imshow(matrix, cmap = 'gray')
plt.title('Input: matrix')
plt.show()

#cv2.imshow("matrix", matrix)
#cv2.waitkey(0)
#cv2.destroyAllWindows()

M1 = len(matrix)
N1 = len(matrix[0])

#interpolation factor
c = 0.5

print("Interpolation factor is: ", c)
print()

M2 = M1 * c
N2 = N1 * c
M2 = ceil(M2)
N2 = ceil(N2)
newmatrix = np.full((M2, N2), -1)

for i in range(M1):
	for j in range(N1):
		newmatrix[int(i * c)][int(j * c)] = matrix[i][j]

# print(newmatrix)

#range of known values
Mx = int(i * c)
My = int(j * c)

# print()
IM = np.eye(4) #identity matrix of size 4
lam = 0.0001
IM = lam * IM  #lambda = 0.0001 and multiply this constant with IM

for i in range(Mx + 1):
    for j in range(My + 1):
        if newmatrix[i][j] == -1:

            x = i / c
            y = j / c

            if ceil(x) != x:
                x1 = floor(x)
                x2 = ceil(x)
            else:
                if x == 0:
                    x1 = 0
                    x2 = 1
                else:
                    x1 = x - 1
                    x2 = x

            if ceil(y) != y:
                y1 = floor(y)
                y2 = ceil(y)
            else:
                if y == 0:
                    y1 = 0
                    y2 = 1
                else:
                    y1 = y - 1
                    y2 = y

            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            #X matrix for neighbors
            X = [
                [x1, y1, x1*y1, 1],
                [x1, y2, x1*y2, 1],
                [x2, y1, x2*y1, 1],
                [x2, y2, x2*y2, 1],
                ]
            #input 
            Y = [
                [matrix[x1][y1]],
                [matrix[x1][y2]],
                [matrix[x2][y1]],
                [matrix[x2][y2]],
                ]
            
            #if determinant of X is 0 or close to 0 then, inverse cannot be compute
            #so, add some noise to it
            if np.linalg.det(X) == 0:
                X = X + IM  

            A = np.dot(np.linalg.inv(X), Y)

            newmatrix[i][j] = np.dot(np.array([x, y, x*y, 1]), A)


# print(newmatrix)
# print()
#for last few rows and columns
for i in range(Mx + 1):
    for j in range(My + 1, len(newmatrix[0])):
        newmatrix[i][j] = newmatrix[i][j - 1]

for j in range(len(newmatrix[0])):
    for i in range(Mx + 1, len(newmatrix)):
        newmatrix[i][j] = newmatrix[i - 1][j]

# print(newmatrix)
plt.figure(figsize=(10,10))
plt.imshow(newmatrix, cmap = 'gray')
plt.title('Output: newmatrix')
plt.show()
