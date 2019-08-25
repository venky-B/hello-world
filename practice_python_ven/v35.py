'''def raju(*num1):
    print("hello")
    return num1

print(raju(3,2,5,7,8,4))

if __name__ == "__main__":
    def sample(**raju):
        print(raju)
    sample(id="aju", age=18)

    '''

msg = 20


def change1():
    global msg
    msg =30
    return msg
print(change1())
print(msg)


