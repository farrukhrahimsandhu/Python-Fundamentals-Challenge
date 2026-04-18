# Swap two numbers without using a third variable.

a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

print(f"Numbers before swipe are: a={a} , b={b}")

a, b = b ,a 

print(f"Numbers after swipe are: a={a} , b={b}")
