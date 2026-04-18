# Create a simple contact book using dictionary.


import json
import os

FILENAME = "contacts.json"


#------------ Helper Functions ------------
def load_contacts():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

def save_contacts(contacts):
    with open(FILENAME,"w") as file:
        json.dump(contacts, file, indent=4)

#------------ CRUD Functions --------------
def add_contact(contacts):
    name = input("\nEnter name: ")
    key = name.lower()

    if key in contacts:
        print("Contact already exist in the Contact book.")
        return 
    
    number = input("Enter number: ")
    email = input("Enter email: ")

    contacts[key] = {
        "name" : name,
        "number" : number,
        "email" : email
    }
    save_contacts(contacts)
    print("\nContact is saved Successfully.")

def view_contact(contacts):
    if not contacts:
        print("No contact found.")
    else:
        print("\n------ Your Contacts List ------")
        for i, details in enumerate(contacts.values(),start=1):
            print(f"\n{i}. Name: {details['name']}")
            print(f"    Number: {details['number']}")
            print(f"    Email: {details['email']} ")

def search_contact(contacts):
    name = input("Enter name to search contact: ")
    key = name.lower()

    if key in contacts:
        details = contacts[key]
        print(f"\nDetails of {details['name']}:")
        print(f"    Number: {details['number']}")
        print(f"    Email: {details['email']}")
    else:
        print("No Contact founded with this name.")

def update_contact(contacts):
    name = input("Enter name to update contact: ")
    key = name.lower()

    if key in contacts:
        details = contacts[key]
        print(f"\nCurrent Details of {details['name']}:")
        print(f"    Number: {details['number']}")
        print(f"    Email: {details['email']}")

        new_number = input("\nEnter new number (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")

        if new_number.strip():
            details['number'] = new_number
        if new_email.strip():
            details['email'] = new_email

        contacts[key] = details

        save_contacts(contacts)
        print("Contact updated Successfully.")
    else:
        print("No contact found with this name.")

def delete_contact(contacts):
    name = input("Enter name: ")
    key = name.lower()

    if key in contacts:
        details = contacts[key]
        print(f"\nCurrent details of {details['name']}:")
        print(f"    Number: {details['number']}")
        print(f"    Email: {details['email']}")

        conform = input(f"\nAre you sure you want to delete {details['name']}? (y/n): ").lower()
        if conform == "y":
            del contacts[key]
            save_contacts(contacts)
            print(f"\nContact '{details['name']}' is deleted Successfully.")
        else:
            print("\nDeletion is canceled.")
    else:
        print("No contact found with this name.")

#------------ Main Function ---------------
def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("\nExiting Contact Manager... Goodbye!\n")
            break
        else:
            print("Invalid choice. Try again.")


# Call main function 
if __name__ == "__main__":
    main()

