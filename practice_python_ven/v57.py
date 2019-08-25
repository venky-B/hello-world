
strv = input()
print(strv)
for i in range(len(strv)):
    if(i == 0  and strv[i].isalpha()):
        print(strv[0].upper(),end="")
        continue
    if(strv[i-1] == ' '):
        print(strv[i].upper(),end="")
        continue
    print(strv[i],end="")
