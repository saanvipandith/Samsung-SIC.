<<<<<<< HEAD
def Insertion_sort(Numbers):
    for i in range(len(Numbers)):
        element = Numbers[i]
        j = i - 1
        while j>=0 and element < Numbers[j]:
            Numbers[j+1] = Numbers[j]
            j-= 1
            Numbers[j+1] = element
    return Numbers

''' program completed
'''
=======
def insertion_sort(numbers):
    for i in  range(len(numbers)):
        element = numbers[i]
        j = i - 1
        while j>= 0 and element < numbers[j]:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = element
    return numbers
	    
>>>>>>> 66069f6eb455a4b9e2cef83ddc71312fb5caeaf0
