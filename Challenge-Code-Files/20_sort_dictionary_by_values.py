# Sort a dictionary by values.

import ast

user_input = input("Enter a dictionary: ")
my_dict = ast.literal_eval(user_input)

sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(f"Dictioary after Sorting : {sorted_dict}")


