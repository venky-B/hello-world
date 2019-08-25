'''if __name__ == '__main__':
    strv = input()
    strn = ""
    for i in strv:
        if i.isupper():
            strn = strn + i.lower()
        elif i.islower():
            strn = strn + i.upper()
    print(strn)'''


def swap_case(s):
    strn = ""
    for i in s:
        if i.isupper():
            strn = strn + i.lower()
        elif i.islower():
            strn = strn + i.upper()
        else:
            strn = strn + i

    return strn


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)