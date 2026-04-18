# Create a simple "To-Do List" app (CLI). 


import os

FileName = "ToDo.txt"

def load_task():
    if os.path.exists(FileName):
        with open(FileName,"r") as f:
            return [line.split() for line in f.readlines()]
    return []

def view_task(tasks):
    if not tasks:
        print("No Task Found.")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_task(tasks)
    print("Task added Successfully.")

def save_task(tasks):
    with open(FileName,"w") as f:
        for task in tasks:
            f.write(task + "\n")

def remove_task(tasks):

    view_task(tasks)
    if tasks:
        try:
            num = int(input("Enter number of task you want to remove: "))
            if 1<= num <= len(tasks):
                removed  = tasks.pop(num-1)
                save_task(tasks)
                print(f"The task '{removed}' is removed.")
            else:
                print("Invalid number.")
        except:
            raise ValueError ("Please enter a valid number.")

def main():

    tasks = load_task()

    while True:

        print("\n--- To-Do List Menu ---")
        print("1. View task")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye! Have a productive day.")
            break
        else:
            print("InValid choice. Try again")

# Call main Function 
if __name__ == "__main__":
    main()
