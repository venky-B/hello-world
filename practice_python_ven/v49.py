
if __name__ == "__main__":
    num = int(input())
    nl = []
    for i in range(num):
        cmd,*p = input().split()
        np = list(map(int, p))

        if cmd == 'insert':
            nl.insert(np[0],np[1])
        elif cmd == 'print':
            print(nl)
        elif cmd == 'remove':
            nl.remove(np[0])
        elif cmd == 'append':
            nl.append(np[0])
        elif cmd == 'sort':
            nl.sort()
        elif cmd == 'pop':
            nl.pop()
        elif cmd == 'reverse':
            nl.sort(reverse = True)




