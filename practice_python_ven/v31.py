numb = int(input("enter the no"))
a = []
count = 0
ven = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six"
}
temp =numb
while(1):
    if temp == 0:
        break
    temp = int(temp / 10)
    count = count + 1

for i in range(0,count):
    a.append(numb % 10)
    numb = int(numb / 10)

a.reverse()
for i in a:
    print(ven[i],end=" ")
