n, = map(int, input().split())
k = len(bin(n)) - 1
print("\n".join(["%*d%*s%*s%*s" % (k-1, i, k, oct(i)[2:], k, hex(i)[2:].upper(), k, bin(i)[2:])for i in range(1, n + 1)]))