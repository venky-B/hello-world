def swap_case(s):
    for i in range(0,len(s)):
        if(s[i].islower() == True):
            s[i].upper()
        elif(s[i].isupper() == True):
            s[i].lower()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)