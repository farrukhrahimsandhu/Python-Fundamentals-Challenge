# Print a number pyramid.

row = int(input("Enter number of rows : "))

for i in range(1, row+1):     # loop for rows
    for j in range(1, i+1):   # loop for numbers in each row
        print(j, end= " ")
    print()                 # move to next line



