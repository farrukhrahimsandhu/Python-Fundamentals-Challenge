# Find the second largest number in a list.

user_input = input("Enter a list : ")
my_list = list(map(int,user_input.split()))

sorted_list = list(sorted(my_list))
reversed_list = sorted_list[::-1]
largest_2nd = reversed_list[1]

print(f"2nd largest number is {largest_2nd}")

