import sys

input_list = []

for i in range(1,len(sys.argv)):
    input_list.append(int(sys.argv[i]))

print('Input list =', input_list)

for i in range(0,len(input_list)-2):
    sorted = True
    for j in range(0,len(input_list)-2-i):
        if input_list[j] > input_list[j +1]:
           input_list[j], input_list[j + 1] = input_list[j+1], input_list[j]
           sorted = False
    if sorted:
        break
    
print('Input list after sorting:',input_list)
''' program completed
'''
