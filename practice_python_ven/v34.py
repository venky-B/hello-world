import random
import math

instr = input()
temp = []
split_d = []
temp1 = []

for i in instr:
    temp.append(i)
split_d = [int(i) for i in temp if i.isdigit()]
'''for i in temp :
    if i.isdigit():
        split_d.append(i)'''

for i in split_d:
    if i not in temp1:
        temp1.append(i)

for index in range(math.factorial(len(temp1))):
    random.shuffle(temp1)
    print()
    for i in temp1:
        print(i,end="")

