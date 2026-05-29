<<<<<<< HEAD
import sys

import Insertion_sort as ins_sort

Numbers = []

for i in  range(1,len(sys.argv)):
    Numbers.append(float(sys.argv[i]))

print('Numbers before sorting:',Numbers)

new_numbers = ins_sort.Insertion_sort(Numbers)

print('Numbers after sorting:',new_numbers)

''' program completed
'''

=======
import Insertion_sort as ins_sort
import sys

numbers = []

for i in range(1, len(sys.argv)):
    numbers.append(float(sys.argv[i]))

print('Numbers before sorting: \n', numbers)
ins_sort.insertion_sort(numbers)
print('Numbers after sorting:')
for i in range(len(numbers)):
    print('%-4d'%(numbers[i]), end='')
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
