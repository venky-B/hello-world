
def textc(strb,strw):
    count =1
    for i in strb:
        if count <= strw:
            print(i,end="")
            count = count + 1
            if count > strw:
                count = 1
                print("")

if __name__ == "__main__":
    name = input()
    size = int(input())
    textc(name,size)