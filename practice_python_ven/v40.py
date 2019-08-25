numc = input("enter the string containing only numbers")
temp = []
temp2 = []

for index in numc:
    temp.append(int(index))
    temp2.append(index)

for i in temp2:
    strv += i

print(temp)
print(temp2)
print(strv)