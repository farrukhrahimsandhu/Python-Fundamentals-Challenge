# Print Pascal’s triangle.

"""
Concept:

   1. It starts with 1 at the top.
   2. Each number in the triangle is the sum of the two numbers directly above it 
    (one from the left and one from the right).
   3. The edges of the triangle are always 1.

"""


rows = int(input("Enter number of rows: "))

triangle = []  # to store all rows

for i in range(rows):
    row = [1]
    if i > 0:
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
    triangle.append(row)

# print the triangle in centered form
for i in range(rows):
    print(" " * (rows - i), end="")  # spaces for alignment
    for num in triangle[i]:
        print(num, end=" ")
    print()


