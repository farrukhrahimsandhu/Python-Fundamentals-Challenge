# Write a program to store student records (name, marks) in a file.

with open("student_records_39,txt","w+") as f:
    n = int(input("Enter the number of the students: "))

    for i in range(n):
        name = input(f"Enter the Name of student{i+1}: ")
        marks = input(f"Enter the Marks of student{i+1}: ")

        f.write(f"{name} : {marks}")
        f.write("\n")


print("Student records have been saved to 'student_records_39.txt'")