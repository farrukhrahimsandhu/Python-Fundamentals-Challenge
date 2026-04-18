# Print a multiplication table of any number.

num = int(input("Enter a number : "))

# By using while loop 
i = 1
while i <= 10:
    print(f"{num} * {i} = {num*i}")
    i += 1

print("\nUsing for loop\n")

# By using for loop
for i in range (1,11):
    print(f"{num} * {i} = {num*i}")


