from itertools import permutations

if __name__ == "__main__":
    strv = input("enter the string : ")

    plist = permutations(strv)


    for i in plist:
        print("".join(i))
