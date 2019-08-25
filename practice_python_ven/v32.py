stringv = input()
templist =[]
numb = []
for ch in stringv:
    templist.append(str(ch))
for i in templist:
    if i =="-":
        numb.append(i)
res = [int(i) for i in templist if i.isdigit()]
for i in res:
    numb.append(i)
print(numb)
