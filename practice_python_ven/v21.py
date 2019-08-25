listeg = [1,2,3,4,456,2,2434,3,334,123,5443,23234,3232343,2]
j=0
for i in range(len(listeg)):
    if listeg[i] > j:
        j = listeg[i]
print(f"max value in the listeg is {j}")