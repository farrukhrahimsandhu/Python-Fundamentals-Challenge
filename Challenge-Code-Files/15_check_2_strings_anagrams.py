# Check if two strings are anagrams.
"""
In Python, two strings are considered anagrams if they contain the same characters 
with the same frequencies, but possibly in a different order. 
Example usage: 
print(are_anagrams_sorted("listen", "silent"))  # Output: True
print(are_anagrams_sorted("Race", "Care"))    # Output: True
print(are_anagrams_sorted("hello", "world"))  # Output: False

"""


def string_anagrams_check(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)
    


str_1 = input("Enter 1st string : ")
str_2 = input("Enter 2nd string : ")

Answer = string_anagrams_check(str_1 , str_2)

if Answer == True:
    print("\nStrings are anagrams.\n")
else:
    print("\nStrings are not anagrams.\n")
