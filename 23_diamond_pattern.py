# Print a diamond pattern using *.

rows = int(input("Enter number of rows: "))

# Upper half of diamond
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

# Lower half of diamond
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
