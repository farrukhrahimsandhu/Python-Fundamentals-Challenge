# Create a simple "To-Do List" app (CLI).

import os

File_Name = "To_Do_List.txt"

def load_tasks():

    # Return list of tasks loaded from File_Name.

    if not os.path.exists("To_Do_List.txt"):
        return []
    else:
        with open("To_Do_List.txt","r") as f:
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    
def save_tasks(tasks):

    # Write tasks list to File_Name (one per line).

    with open("To_Do_List.txt","w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):

    # Prompt user and add task, then save.

    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):

    # Print tasks with numbers, or a message if empty.

    if not tasks:
        print("No Task Found.")
    else:
        print("\n---Your Tasks---")
        for i, task in  enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):

    # Prompt for index, remove if valid, save.

    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Enter task to ve deleted: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num-1)
                save_tasks(tasks)
                print(f"Task '{removed}' is deleted.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter valid number.")

def mark_done(tasks):

    # Prompt for index, mark as done, save.

    view_tasks(tasks)

    if tasks:
        try:
            num = int(input("Enter a task to be marked as Done: "))
            if 0 < num <= len(tasks):
                tasks[num - 1] = "[Done]" + tasks[num - 1]
                save_tasks(tasks)
                print("Task marked as done!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter valid number.")

def main():

    tasks = load_tasks()
    
    while True:
        # print menu and dispatch to functions above
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            print("Goodbye! Have a productive day.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


 