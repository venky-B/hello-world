arr = [1,2,3,4,5,6,7,5,7,32,3]
print(arr)
for i in arr:
    cnt = arr.count(i)
    if cnt > 1:
        arr.remove(i)
arr.sort()
arr.reverse()
print(arr)