cube = lambda x: x*x*x 

def fibonacci(n):
    # return a list of fibonacci numbers
    temp1 = 0
    temp2 = 1
    nextv = 0
    listv = []
    i = 1
    while i <= n:
        
        listv.append(temp1)       
        nextv = temp1 + temp2
        temp1 = temp2
        temp2 = nextv
        i = i + 1
    
    return listv


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
