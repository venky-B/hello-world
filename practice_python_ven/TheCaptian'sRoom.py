k = int(input())

arr = list(map(int, input().split()))   #comments is used for testing github so don't mind

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))
