num = int(input("Enter the value of num : "))
mylist = list()
list_three = list()

for i in range(num):
    value = input()
    mylist.append(int(value))
    if len(value) == 3:
        list_three.append(value)
        
        
#sort
list_three.sort()

pos = int(input("Enter the value of position : "))

        
print(list_three[pos-1])
