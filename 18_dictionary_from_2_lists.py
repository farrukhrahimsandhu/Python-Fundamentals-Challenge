# Create a dictionary from two lists.

user_input1 = input("Enter 1st list that will be the key : ")
keys = list(map(str,user_input1.split()))

user_input2 = input("Enter 2nd list that will be the values : ")
values = list(map(str,user_input2.split()))

if len(keys) == len(values):
    my_dict = dict(zip(keys,values))
    print(f"Distionary is : {my_dict}")
else:
    raise ValueError ("Length of both lists is not same.")

