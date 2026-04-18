# Implement a simple calculator (+, -, *, /).

num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))

def sum(num1 , num2):
    return num1+num2

def subtract(num1 , num2):
    return num1-num2

def multiply(num1 , num2):
    return num1*num2

def divide(num1 , num2):
    if num2 == 0:
        raise ZeroDivisionError ("Cannot divide by zero.")
    return num1/num2
    
def power(num1 , num2):
    return num1 ** num2

def floor_division(num1 , num2):
    if num2 == 0:
        raise ZeroDivisionError ("Cannot floor-divide by zero.")
    return num1//num2

def modulus(num1 , num2):
    if num2 == 0:
        raise ZeroDivisionError ("Cannot mod by zero.")
    return num1%num2


operator = input("Enter any operation: ")

if operator == "+":
    print(f"Answer is: {sum(num1,num2)}")
elif operator == "-":
    print(f"Answer is: {subtract(num1,num2)}")
elif operator == "*":
    print(f"Answer is: {multiply(num1,num2)}")
elif operator == "/":
    print(f"Answer is: {divide(num1,num2)}")
elif operator == "**":
    print(f"Answer is: {power(num1,num2)}")
elif operator == "//":
    print(f"Answer is: {floor_division(num1,num2)}")
elif operator == "%":
    print(f"Answer is: {modulus(num1,num2)}")
else:
    raise ValueError