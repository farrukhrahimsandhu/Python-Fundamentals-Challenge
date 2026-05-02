# Intermediate Password Generator 
"""
Intermediate Password Generator (More Features)

    1.Allow user to include/exclude character types (uppercase, lowercase, digits, symbols). [done]
    2.Add option to generate multiple passwords at once. 
    3.Ensure at least one character from each selected type is included. [done]
    4.Provide basic password strength feedback (e.g., Weak / Medium / Strong).
    5.Add option to save generated passwords to a file.
"""

import secrets   # Module to generate secure password
import string    # Module to chose lowwer case and upper case letters, digits,symbols.
import random    # Module to select random number from each selected type.
import os        # Module to check if a file exists or not by giving its path.
import re        # Module to check strength of password.

File_Name = "Saved_Passwords.txt"   # File name where the passwords will store.

# Generate password 
def Generate_Password():
    
    password_length = int(input("Enter length of password : "))
    no_of_passwords = int(input("Enter the number of passwords you want to generate : "))

    
    use_lower = input("Include Lower Case Letters (y/n) : ").lower() == "y"
    use_upper = input("Include Upper case Letters (y/n) : ").lower() == "y"
    use_digits = input("Include Digits (y/n) : ").lower() == "y"
    use_symbol = input("Include Symbols (y/n) : ").lower() == "y"

    if not (use_lower or use_upper or use_digits or use_symbol):
        print("Error: You must select at least one option!")
        return []   # return empty list if no option chosen
    
    generated_passwords = []

    for _ in range(no_of_passwords):
        pool = []
        guaranteed = []
        
        if use_lower:
            pool.append(string.ascii_lowercase)
            guaranteed.append(random.choice(string.ascii_lowercase))
        if use_upper:
            pool.append(string.ascii_uppercase)
            guaranteed.append(random.choice(string.ascii_uppercase))
        if use_digits:
            pool.append(string.digits)
            guaranteed.append(random.choice(string.digits))
        if use_symbol:
            pool.append(string.punctuation)
            guaranteed.append(random.choice(string.punctuation))

        all_characters = "".join(pool)
        remaining_length = password_length - len(guaranteed)

        if remaining_length < 0:
            print("Error: Password length too short for selected options.")
            return []

        
        password = guaranteed + [secrets.choice(all_characters) for _ in range(remaining_length)]

        random.shuffle(password)
        generated_passwords.append("".join(password))
    return generated_passwords


# Check Password Strength 
def Strength_check(password):

    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]",password):
        score += 1
    else:
        remarks.append("Password should contain at least one upper case letter.")

    if re.search(r"[a-z]",password):
        score += 1
    else:
        remarks.append("Password should contain at least one lower case letter.")

    if re.search(r"[0-9]",password):
        score += 1
    else:
        remarks.append("Password should contain at least one digit.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?`~]",password):
        score += 1
    else:
        remarks.append("Password should contain at least one symbol.")

    # Determine strength of Password 
    if score == 5:
        print(f"Strong ✅")
    elif score >= 3:
        print(f"Medium ⚠️")
    else:
        print(f"Weak ❌")
    
    if remarks:
        print("Suggestions:")
        for r in remarks:
            print("-", r)

# the functions are given to save selected password and view password 
def load_file():
    """Return list of tasks loaded from FILE_NAME."""
    if not os.path.exists(File_Name):
        return []
    else:
        with open(File_Name,"r") as f:
            passwords = [line.strip() for line in f.readlines()]
        return passwords
def save_password(passwords):
    """Write tasks list to FILE_NAME (one per line)."""
    with open(File_Name,"a") as f:
        for password in passwords:
            f.write(password + "\n")
def add_password(passwords):
    """Prompt user and add task, then save."""
    password = input("Enter a new password: ")
    passwords.append(password)
    save_password(passwords)
    print("Password saved successfully!")
def view_password(passwords):
    """Print passwords with numbers, or a message if empty."""
    if not passwords:
        print("No Password Found.")
    else:
        print("\n---Your Passwords---")
        for i, password in  enumerate(passwords, start=1):
            print(f"{i}. {password}")

# Main Function 
def main():

    passwords = load_file()
    
    while True:
        # print menu and dispatch to functions above
        print("\n--- Password Generator MENU ---")
        print("1. Generate Password.")
        print("2. Save Password")
        print("3. View saved Passwords")
        print("4. Check Strength of Password")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")


        if choice == "1":
            generated = Generate_Password()
            if generated:
                print("\nGenerated Passwords:")
                for p in generated:
                    print("\t",p)
        elif choice == "2":
            add_password(passwords)
        elif choice == "3":
            view_password(passwords)
        elif choice == "4":
            user_password = input("Enter a password to check its strength: ")
            Strength_check(user_password)
        elif choice == "5":
            print("Goodbye! Have a good day.")
            break
        else:
            print("Invalid choice. Try again.")


# Call the main function 
if __name__ == "__main__":
    main()

