# Reverse a string without using slicing.

def reversed_string(text):

    reversed_string = " "

    for char in text:
        reversed_string = char + reversed_string

    return reversed_string

text = input("Enter a string: ")
print("Reversed string:", reversed_string(text))



