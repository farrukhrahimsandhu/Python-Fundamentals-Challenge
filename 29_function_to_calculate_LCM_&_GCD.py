# Write a function to calculate the LCM and GCD of two numbers.

def gcd(a, b):
    # Euclidean algorithm for GCD
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Use relation: LCM * GCD = a * b
    return (a * b) // gcd(a, b)

# Driver code
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("GCD of", x, "and", y, "is:", gcd(x, y))
print("LCM of", x, "and", y, "is:", lcm(x, y))
