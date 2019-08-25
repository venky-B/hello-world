# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = ""
b = ""
for j in range(0,n):
    str1 = input()
    for i in range(0,len(str1)):
        if i % 2 == 0:
            a = a + str1[i]
        else:
            b = b + str1[i]
    print(a, b)
    a=""
    b=""



