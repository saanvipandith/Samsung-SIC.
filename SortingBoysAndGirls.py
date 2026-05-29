boys_height_str = input("Enter boys heights (space-separated): ")
girls_height_str = input("Enter girls heights (space-separated): ")

b_height = [int(h) for h in boys_height_str.split() if h.strip()]
g_height = [int(h) for h in girls_height_str.split() if h.strip()]


merged_list = b_height + g_height
merged_list.sort()

if merged_list[0] in b_height:
    for i in merged_list:
        if merged_list[i +1] not in g_height:
            flag = 1
            break

if merged_list[0] in g_height:
    for i in range(len(merged_list)):
        if merged_list[i +1] not in b_height:
            flag = 1
            break

print(merged_list)

if flag == 1:
    print("No")

else:
    print("Yes")
