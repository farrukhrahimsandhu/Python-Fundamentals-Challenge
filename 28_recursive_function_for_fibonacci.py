# Write a recursive function for Fibonacci.


def fibonacci(n):
    if n <= 0:         # base case 1
        return 0
    elif n == 1:       # base case 2
        return 1
    else:              # recursive case
        return fibonacci(n-1) + fibonacci(n-2)


# Driver code to print Fibonacci sequence
terms = int(input("Enter number of terms: "))

print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")


