# Merge two dictionaries into one.

import ast

user_1 = input("Enter a dictionary: ")
word_dict_1= ast.literal_eval(user_1)


user_2 = input("Enter a dictionary: ")
word_dict_2 = ast.literal_eval(user_2)

new_dict  = {**word_dict_1,**word_dict_2}

print(f"Merged Dictionary: {new_dict} ")