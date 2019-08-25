from itertools import permutations
from array import array
strv = set(input())
fc = []

newv = array('i',[])
for i in strv:
    if i.isdigit():
        fc.append(i)

perm = permutations(fc)

for i in perm:
  newv.append(int("".join(i)))

print(newv)
min = float('inf')
for i in newv:
    if min > i and (i % 2 != 0):
        min = i
if min < float("inf"):
    print("min odd arrangement is : ", min)
else:
    print("min odd arrangement is : ", -1)




