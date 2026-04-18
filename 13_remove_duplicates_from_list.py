# Remove duplicates from a list without using set().

user_input = input("Enter a list : ")
list_1 = list(map(int,user_input.split()))


def remove_duplicate(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list

print(f"After removing Duplication: {remove_duplicate(list_1)}")

