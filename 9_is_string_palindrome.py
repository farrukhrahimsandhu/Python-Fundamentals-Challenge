# Check if a string is a palindrome.

text = input("Enter a string: ")
text = text.lower()

if text.strip(" ") == text[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
