g = []
b = []
mix = []
temp = []
size = int(input("Enter the size: "))
for i in range(size):
    girl = int(input("Enter the height(girl): "))
    g.append(girl)
    boy = int(input("Enter the height(boy): "))
    b.append(boy)
for i in range(size):
    if g[i] <= b[i]:     
        mix.append(g[i])
        mix.append(b[i])
    else:
        mix.append(b[i])
        mix.append(g[i])
print(mix)
temp = mix
temp.sort()
print(temp)
for i in range(len(mix)):
    if mix[i] == temp[i]:
        print("YES")
    else:
        print("NO")
