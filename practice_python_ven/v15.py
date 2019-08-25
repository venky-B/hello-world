weight = int(input())
d = input("Kg - k lbs - l")
if d.upper() == "L":
    print(weight/2.2)
else:
    print(weight*2.2)