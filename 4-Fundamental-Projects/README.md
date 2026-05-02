# 🛠️ 4 Fundamental Python Projects

This folder contains four core Command Line Interface (CLI) applications. These projects were developed to solidify foundational Python programming skills, with a heavy emphasis on logic building, state management, and data persistence—essential prerequisites for advanced software engineering and data science pipelines.

## 📝 Project Breakdown

### 1. ATM Simulator (`ATM.py`)
A comprehensive simulation of an automated teller machine.
* **Key Features:** Secure PIN verification, balance checking, deposits, and conditional withdrawals.
* **Logic Handled:** Enforces daily limits, minimum/maximum deposit thresholds, and note multiples (e.g., must be a multiple of 500).
* **Data Handling:** Tracks transaction history and maintains user state using JSON data persistence.

### 2. Contact Book Manager (`contact_book.py`)
A robust contact management system built on Python dictionaries.
* **Key Features:** Full CRUD functionality—users can Add, View, Search, Update, and Delete contacts.
* **Logic Handled:** Prevents duplicate entries and allows partial updates (e.g., updating an email while keeping the existing phone number).
* **Data Handling:** Persists contact structures across sessions using `Contact_Book.json`.

### 3. Secure Password Generator (`Intermediate_Password_Generator.py`)
An advanced utility for generating highly secure, customizable passwords.
* **Key Features:** Generates multiple passwords at once based on user-defined lengths and character types (uppercase, lowercase, digits, symbols).
* **Logic Handled:** Utilizes the `secrets` module for cryptographic strength and guarantees at least one character from each selected pool. Includes a built-in strength checker using Regular Expressions (Regex).
* **Data Handling:** Optionally saves generated passwords to `Saved_Passwords.txt`.

### 4. CLI To-Do List (`To_Do_List(Universal).py`)
A streamlined task management application.
* **Key Features:** Add new tasks, view existing ones, mark tasks as complete, and delete entries.
* **Logic Handled:** Dynamic list indexing and error handling for user inputs.
* **Data Handling:** Demonstrates standard file I/O operations by writing to and reading from `To_Do_List.txt`.

## 💡 Key Takeaways
* **Data Persistence:** Mastered the transition from volatile memory to permanent storage using both `.json` and `.txt` formats.
* **Control Flow:** Handled complex, nested conditional statements and user input validation (try-except blocks).
* **Modular Code:** Structured applications using clean, reusable helper functions to maintain code readability and scalability.

## 🚀 How to Run
Navigate to this directory in your terminal and execute any of the scripts using Python:
```bash
python ATM.py