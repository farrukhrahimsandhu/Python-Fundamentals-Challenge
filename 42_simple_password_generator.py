# Simple Password Generator 
"""
Simple Password Generator (Beginner Features)

    1.Generate a random password of fixed length.
    2.Use basic character sets (letters + digits).
    3.Let the user choose the password length.
    4.Output the password on the screen.
"""

import random
import string


alphabets = string.ascii_letters + string.digits


print("--- Password Generator ---.")
length_of_passsword = int(input("Enter the length of password: "))

password = "".join(random.choice(alphabets) for _ in range(length_of_passsword))
print(f"Your password is: {password}")

