# Print a hollow square pattern.

n = int(input("Enter size of square: "))

for i in range(n):              # loop for rows
    for j in range(n):          # loop for columns
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")  # print * at borders
        else:
            print(" ", end=" ")  # print space inside
    print()  # move to next line

