# Write a program to read student records and display the topper.

with open("student_records_40.txt","r+") as f:
    
    records = f.readlines()   # read all lines into a list

    topper_name = ""
    topper_marks = -1   # start with a very low value

    # Process each record
    for record in records:
        # Split the line: "Name : Marks"
        name, marks = record.strip().split(" : ")
        marks = int(marks)  # convert marks to integer

    # Check for topper
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

# Display the topper
print(f"The topper is {topper_name} with {topper_marks} marks.")
