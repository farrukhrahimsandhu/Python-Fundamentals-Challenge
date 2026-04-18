# Find common elements in two lists.

input_1 = input("Enter 1st list : ")
list_1 = list(map(int,input_1.split()))

input_2 = input("Enter 2nd list : ")
list_2 = list(map(int, input_2.split()))

common_elements = list(set(list_1) & set(list_2))

print(f"Common Elements are : {common_elements}")





