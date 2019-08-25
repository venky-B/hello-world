n = int(5)
i = int(1)
while i<=n:
    val = 0
    j = i
    while j <= n:
        val = val +j
        j = j+i
    else:
        print(val)
        i= i+1
else:
    print("exit")
