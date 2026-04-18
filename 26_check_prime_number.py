# Write a function to check if a number is prime.

num = input("Enter a number to check if it is prime: ")

def is_prime(n):
    n = int(n)
    if n <= 1:   # 0, 1, and negative numbers are not prime
        return False
    
    for i in range(2, int(n**0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False
    
    return True

print(is_prime(num))


