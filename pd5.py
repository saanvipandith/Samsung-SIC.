import numpy as np

arr1 = np.arange(1, 10) #arange always generates 1D array
arr2 = np.arange(2, 25, 2)
arr3 = arr1.reshape(3, -1) # Reshape generates 1D, 2D and 3D arrays and so on
arr4 = arr2.reshape(4, -1)
arr5 = arr2.reshape(2, -1)
arr6 = arr2.reshape(3, -1)
arr7 = arr2.reshape(-1, 4) # Numpy predicts and fixes number of rows
arr8 = arr2.reshape(-1, -1) #ValueError. Can only specify one unknown dimension

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)
print('Arr7:\n', arr7)
print('Arr8:\n', arr8)
