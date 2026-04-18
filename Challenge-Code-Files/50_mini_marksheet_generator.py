# Build a mini marksheet generator: input student data → calculate percentage & grade → save to file.

import json
import os

FileName = "MarkSheets.json"

# ------------Load data--------------
def load_data():
    """Load all students data from json file"""
    if os.path.exists(FileName):
        try:
            with open(FileName,"r") as file:
                data = json.load(file)
                return data
        except json.JSONDecodeError:
            return []
    return []

# --------Input Student data---------
def input_student_data():
    """Input student info and subject wise marks."""
    
    Name = input("Enter name of student: ").lower().strip()
    Roll_No = input("Enter Roll No: ").strip()
    num_subjects = int(input("Enter number of subjects: "))

    marks = {}
    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ").strip()
        score = float(input(f"Enter marks obtained in {subject}: "))
        marks[subject] = score
    
    student = {
        "name": Name,
        "roll_no": Roll_No,
        "marks": marks
    }
    return student

# -------Calculate results-----------
def calculate_results(student):
    """Calculate total, percentage, and grade."""
    marks = student["marks"]
    Max_marks_per_subject = 100
    Total_marks = sum(marks.values())
    num_subjects = len(marks)
    
    percentage = ((Total_marks)/(num_subjects * Max_marks_per_subject)) * 100

    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"
    
    student["total"] = Total_marks
    student["percentage"] = round(percentage, 2)
    student["grade"] = grade

# --------Display marksheet-----------
def display_marksheet(student):
    """Print the marksheet in formated style"""
    print("\n=========== STUDENT MARKSHEET ============")
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")
    print("------------------------------------------")

    for subject, score in student["marks"].items():
        print(f"{subject:<15}: {score}")
    
    print("------------------------------------------")
    print(f"Total Marks     :   {student['total']}")
    print(f"Percentage      :   {student['percentage']}")
    print(f"Grade           :   {student['grade']}")
    print("==========================================\n")

# --------Save data to file----------
def save_to_file(student):
    """Save all student data in json file."""
    data = load_data()
    data.append(student)

    with open(FileName,"w") as file:
        json.dump(data, file, indent=4)
        print(f"Record saved successfully to '{FileName}'.\n")

# --------Display all data-----------
def view_all_students(student):
    data = load_data()
    if not data:
        print("No Stydent records available.\n")
        return
    
    print("\n==========All Student MarkSheets==========\n")
    for i, student in enumerate(data, start=1):
        print(f"Record # {i}")
        print(f"Name    : {student['name']}")
        print(f"Roll No : {student['roll_no']}")
        print(f"Marks:")
        for subject, score in student["marks"].items():
            print(f"    {subject:<12}: {score}")
        print(f"Total Marks :   {student['total']}")
        print(f"Percentage  :   {student['percentage']}")
        print(f"Grade       :   {student['grade']}")
        print("--------------------------------------------")
    print("==============================================\n")

# -------Find any student-------------
def search_student_by_Roll_No():
    """Search for a student by roll number and display their marksheet."""
    data = load_data()
    if not data:
        print("No student records available.\n")
        return
    
    roll = input("Enter Roll No to search: ")
    for student in data:
        if student["roll_no"] == roll:
            display_marksheet(student)
            return
    print(f"No Student found with Roll No '{roll}'.\n")

# ------------ Main Program ------------
def main():
    print("\n--------- Welcome Mini MarkSheet Generator --------\n")

    while True:
        print("--------- Main Menu --------")
        print("1. Add new student marksheet")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            student = input_student_data()
            calculate_results(student)
            display_marksheet(student)
            save_to_file(student)

        elif choice == "2":
            view_all_students(student)
        
        elif choice == "3":
            search_student_by_Roll_No(student)
        
        elif choice == "4":
            print("\nThanks for using the marksheet generator!")
            break

        else:
            print("Invalid input! Try again.\n")


# ------------- Entry point ---------------
if __name__ == "__main__":
    main()


