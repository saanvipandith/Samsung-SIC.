import quick_sort as qs
import sys
numbers = [1, 50, 23, 25, 52, 19, 19, 91, 7, 15, 43, 71]
print('Numbers before Sort: \n', numbers)
qs.quick_sort(numbers, 0, len(numbers)-1)
print('Numbers after Sort: \n', numbers)
