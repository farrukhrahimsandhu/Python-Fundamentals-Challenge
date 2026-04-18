# Find the sum of digits of a number.

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10        # Get the last digit
        total += digit          # Add it to total
        num //= 10              # Remove the last digit
    return total

num = int(input("Enter a number: "))
print(f"The sum of digits is {sum_of_digits(num)}")


"""
Example of concept:
    Number = 1234
    Digits = 1, 2, 3, 4
    Sum = 1 + 2 + 3 + 4 = 10
"""