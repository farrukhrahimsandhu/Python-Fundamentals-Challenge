# Rotate a list left and right.

user_input = input("Enter a list to rotate : ")
my_list = list(map(int,user_input.split()))

if len(my_list) == 0:
    raise ValueError ("Empty list.")

steps = int(input("Enter how many steps you want to rotate: "))

direction_of_rotation = str(input("Enter direction of rotation: "))


def rotate_left(lst,steps):
    steps = steps % len(lst)            # to handle complete rotations
    return lst[steps:] + lst[:steps]


def rotate_right(lst,steps):
    steps = steps % len(lst)           # to handle complete rotations
    return lst[steps:] + lst[:steps]

direction_of_rotation = direction_of_rotation.lower()

if direction_of_rotation == "left":
    print("Original List:", my_list)
    print(f"Left Rotate by {steps}: {rotate_left(my_list,steps)}")
elif direction_of_rotation == "right":
    print("Original List:", my_list)
    print(f"Right Rotate by {steps}: {rotate_right(my_list,steps)}")
else:
    raise ValueError ("Invalid input")