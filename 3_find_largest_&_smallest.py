# Find the largest and smallest number among three numbers.

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
c = input("Enter 3rd number: ")

if a>b and a>c:
    print(f"The largest number is {a}")
    if b>c:
        print(f"The smallest number is {c}")
    else:
        print(f"The smallest number is {b}")
elif b>c and b>a:
    print(f"The largest number is {b}")
    if a>c:
        print(f"The smallest number is {c}")
    else:
        print(f"The smallest number is {a}")
elif c>a and c>b:
    print(f"The largest number is {c}")
    if a>b:
        print(f"The smallest number is {b}")
    else:
        print(f"The smallest number is {a}")

