def temp(num):
    strv = ""
    for i in range(2, len(num), 1):
        strv = strv + num[i]

    return strv


def print_formatted(number):
    for i in range(1, number + 1):

        o = oct(i)
        h = hex(i)
        b = bin(i)

        if i == number:
            print(f"{int(i)} {int(temp(o))} {temp(h).upper()} {int(temp(b))}", end="")
            continue

        print(f"{int(i)} {int(temp(o))} {temp(h).upper()} {int(temp(b))}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
