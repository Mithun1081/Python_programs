# Python program explaining
# numpy.concatenate() function

# importing numpy as geek
import numpy as np

arr1 = np.array([[2, 4], [6, 8]])
arr2 = np.array([[3, 5], [7, 9]])

gfg = np.concatenate((arr1, arr2), axis=0)

print(gfg)

print()
import numpy as geek

arr1 = geek.array([[2, 4], [6, 8]])
arr2 = geek.array([[3, 5], [7, 9]])

gfg = geek.concatenate((arr1, arr2), axis=1)

print(gfg)