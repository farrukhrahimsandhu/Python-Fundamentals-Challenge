# Write a program to simulate ATM transactions (withdraw, deposit, balance check).

import json
import os
import datetime

# ------------------ Multi-Account ATM Skeleton ------------------

ACCOUNTS_FILE = "accounts.json"

Min_Deposit = 100
Min_Withdrawal = 500
Daily_Limit = 50000
Note_withdrawal = 500
Max_Deposit = 1_000_000

# --- File Helpers ---
def load_accounts():
    """Load accounts from file or return empty dict."""
    if os.path.exists(ACCOUNTS_FILE):
        try:
            with open(ACCOUNTS_FILE,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}
        

def save_accounts(accounts):
    """Save accounts dictionary into file."""
    with open(ACCOUNTS_FILE,"w") as file:
        json.dump(accounts, file, indent=4 )

# ----------verify pin-----------------
def verify_pin(accounts):
    attempts = 3
    while attempts > 0:
        pin = input("Enter pin: ")
        if pin in accounts:
            print(f"Welcome {accounts[pin]['name']}!\n")
            return pin
        else:
            attempts -= 1
            print(f"False pin. Attempt left: {attempts}")
    return None

# ---------check balance---------------
def check_balance(account):
    print(f"Your account balance is {int(account['balance']):,}\n")

# ---------Exit program----------------
def exit_program():
    print("\nThank you for using this ATM. \nHave a good day.\n")

# ---------Show Main Menu--------------
def main_menu():
    print("===================================")
    print("---------- ATM Main Menu-----------")
    print("===================================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdrawal Money")
    print("4. View Transection History")
    print("5. Exit")
    print("===================================")

    try:
        choice = int(input("Enter your choice(1-5): "))
        return choice
    except:
        return 0
    
# ---------Deposit Money---------------
def deposit(account, accounts):
    try:
        amount = int(input("Enter amount to deposit: "))
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if amount < Min_Deposit:
            print(f"Minimum Deposit must be {Min_Deposit}\n")
            account['history'].append(
                {"type":"Failed Deposit.", "amount": amount, "reason": "Below Minimum", "date": today}
            )
        elif amount > Max_Deposit:
            print(f"Maximum Deposit must be {Max_Deposit}")
            account['history'].append(
                {"type":"Failed Deposit", "amount": amount, "reason": "Above Maximum", "date": today}
            )
        else:
            account['balance'] = int(account['balance'])
            account['balance'] += amount
            print(f"Deposit Successful! New balance is {account['balance']:,}\n")
            account['history'].append(
                {"type": "Deposit", "amount": amount, "balance": account['balance'], "date": today}
            )
        save_accounts(accounts)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

# ----------Withdrawal Money-----------
def withdrawal(account, accounts):
    try:
        amount = int(input("Enter amount to Withdraw: "))
        today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Minimum Withdrawal
        if amount < Min_Withdrawal:
            print(f"Minimum withdrawal must be {Min_Withdrawal}")
            account['history'].append(
                {"type": "Failed Withdrawal", "amount": amount, "reason": "Below Minimum", "date": today}
            )
            save_accounts(accounts)
            return
        
        # 2. Not multiple of 500
        if amount % Note_withdrawal != 0:
            print(f"Withdrawal must be multiple of {Note_withdrawal}")
            account['history'].append(
                {"type": "Failed Withdrawal", "amount": amount, "reason": "Not multiple of 500", "date": today}
            )
            save_accounts(accounts)
            return
        
        # 3. Daily limit excided
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")
        today_withdrawals = sum(
            h["amount"] for h in account['history']
            if isinstance(h,dict) and h.get("type") == "Withdrawal" and h.get("date") == today_date
        )
        if today_withdrawals + amount > Daily_Limit:
            print(f"Daily limit excided! You can only withdraw {Daily_Limit} per day.\n")
            print(f"Remaining money You can withdraw today is: '{(Daily_Limit)-(today_withdrawals)}'.")
            account['history'].append(
                {"type": "Failed Withdrawal", "amount": amount, "reason": "Daily limit excided", "date": today}
            )
            save_accounts(accounts)
            return
        
        # 4. Insufficient balance
        if amount > account['balance']:
            print(f"Insufficient balance! \nYour current balance is {account['balance']:,}")
            account['history'].append(
                {"type": "Failed Withdrawal", "amount": amount, "reason": "Insufficient balance", "date": today}
            )
            save_accounts(accounts)
            return
        
        old_balance = account['balance']
        account['balance'] = int(account['balance'])
        account['balance'] -= amount
        print(f"\nWithdrawal Successful! \nPrevious balance: {old_balance} \nAmount Withdrawal: {amount} \nNew balance: {account['balance']}\n")
        account['history'].append(
            {"type": "Withdrawal", "amount": amount, "balance": account['balance'], "date": today}
        )
        save_accounts(accounts)

    except ValueError:
        print("Invalid input! Please enter numbers only.")
        

# ----------Transection History---------
def show_history(account):
    print("-------Transection History-------\n")
    if not account['history']:
        print("No transection yet")
    else:
        for i, record in enumerate(account['history'], start=1):
            if isinstance(record,dict):
                if record["type"].startswith("Failed"):
                    print(f"{i}. {record['date']} | {record['type']} | Amount: {record['amount']} | Reason: {record['reason']}")
                else:
                    print(f"{i}. {record['date']} | {record['type']} | Amount: {record['amount']} | Balance: {record['balance']}")
            else:
                print(f"{i}. {record}")         # fallback in case old string records exist
    print("---------------------------------\n")

# -------------Main Program-------------
def main():
    accounts = load_accounts()

    for acc in accounts.values():
        acc["balance"] = int(acc.get("balance", 0))
    
    if not accounts:
        accounts = {
            "8585": {"name": "Farrukh Rahim","balance": 1_954_230 ,"history": []},
            "6094": {"name": "Boss","balance": 26_736_832,"history": []},
            "1234": {"name": "Sandhu Saab","balance": 6_139_541,"history": []}
        }
        save_accounts(accounts)

    print("Welcome to ATM.\n")

    pin = verify_pin(accounts)
    if not pin:
        print("Too many wrong attempts. Card is blocked!")
        return
    
    account = accounts[pin]

    while True:
        choice = main_menu()

        if choice == 1:
            check_balance(account)
        elif choice == 2:
            deposit(account,accounts)
        elif choice == 3:
            withdrawal(account,accounts)
        elif choice == 4:
            show_history(account)
        elif choice == 5:
            exit_program()
            break
        else:
            print("Invalid choice! Please try again.")

# Call main function
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSession ended. Goodbye!")
