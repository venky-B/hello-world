def sec(arr,arr_size):

    if arr_size < 2:
        return -2
    f = s = -24343
    for i in range(arr_size):
        if arr[i] > f:
            s = f
            f = arr[i]

        elif arr[i] > s and arr[i] != f:
            s = arr[i]

    if s == -24343:
        return -1

    return s

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    art = list(arr)

    temp = []
    for i in range(n):
        temp.append(art[i])

    print(temp)
