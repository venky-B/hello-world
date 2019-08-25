# fizzbuzz

def fizzbuzz(val):
    if (val % 3 == 0 and val % 5 == 0) or (val % 3 != 0 and val % 5 != 0):
        print("fizzbuzz")
    elif val % 3 == 0:
        print("fizz")
    elif val % 5 == 0:
        print("buzz")
    else:
        pass

if __name__ == "__main__":
    val = int(input("Enter the value "))
    fizzbuzz(val)