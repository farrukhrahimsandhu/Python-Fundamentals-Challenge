# Write a function to count the number of uppercase and lowercase letters in a string.

def count_case(s):
    upper = 0
    lower = 0
    
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    
    return upper, lower


# Driver code
text = input("Enter a string: ")
upper_count, lower_count = count_case(text)

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
