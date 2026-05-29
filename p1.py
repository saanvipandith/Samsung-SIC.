import numpy as np
a = np.zeros(3)
b = np.ones((2,5))
try:
    print(b[1][3])
    print(a[0][6])
    print(a[0])
except IndexError:
    print("Index error.")
