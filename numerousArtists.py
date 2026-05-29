l1 = []
l2 = []
missing_list = []
size_l1 = int(input("Enter the size of the l1: "))
size_l2 = int(input("Enter the size of l2: "))
for i in range(size_l1):
    e1 = int(input("Enter the elements: "))
    l1.append(e1)
for i in range(size_l2):
    e2 = int(input("Enter the elements: "))
    l2.append(e2)
print("List after: ",l1)
print("List before: ",l2)
min2, max2 = min(l2), max(l2)
for i in l1:
    if i not in l2:
        missing_list.append(i)
        l2.append(i)
    elif l1.count(i) == l2.count(i):
        l1.remove(i)
    else:
        l2.append(i)
        missing_list.append(i)
l2.sort()
print("list after: ",l2)

