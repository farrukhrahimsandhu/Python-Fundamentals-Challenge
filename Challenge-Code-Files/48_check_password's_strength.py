# Build a program that checks strong passwords.

import re

def password_strength(password):

    score = 0

    if len(password) > 8:
        score += 1
    if re.search(r"[A-Z]",password):
        score += 1
    if re.search(r"[a-z]",password):
        score += 1
    if re.search(r"[0-9]",password):
        score += 1
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?`~]",password):
        score += 1

    if score == 5:
        print("Your password strength is strong.")
    elif score >= 3:
        print("Your password strength is medium.")
    else:
        print("Your password strength is week.")

def main():

    print("\n-------Welcome to password strength checker----------\n")
    while True:
        password = input("Enter password to check its strength (or leave blank to quit): ")

        if password.strip():
            password_strength(password)
        else:
            print("\nYou entered nothing.")
            print("Goodbye! Have a good day.\n")
            break

# run main function
if __name__ == "__main__":
    main()