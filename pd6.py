import numpy as np

import numpy as np
def f(x, y):
	return 10 * x + y

my_array = np.fromfunction(f, (5, 4), dtype = int)

my_array[[0, 1, -1], :] = 0 #For 1st row and last row, set all elements to 0

#After:
print(f'After:\n {my_array}')

def f(x, y):
	return 10 * x + y

my_array = np.fromfunction(f, (5, 4), dtype = int)

print(f'Before:\n {my_array}')
#my_array[:, [0, -1]] = 0  #For all Rows, set 0 to 1st and last columns
my_array[[0, -1], :] = 0 #For 1st row and last row, set all elements to 0

#After:
print(f'After:\n {my_array}')

def f(x, y):
	return 10 * x + y

my_aaray = np.fromfunction(f, (5, 4), dtype = int)

# Slicing the Numpy Arrays:
print(my_aaray[2, 3]) # my_array[2][3]
print(my_aaray[0:5, 1]) # From Row-1 to Row-5, print the 2nd element
print(my_aaray[ : , 1]) # From all rows, print 2nd element
print(my_aaray[1:3, : ]) # From Row-2 to Row-3, print all elements
