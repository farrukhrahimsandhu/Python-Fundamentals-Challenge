# Write a program to search for a word in a file.

user_input = input("Enter a word to search it from a txt file: ")
user_input = user_input.lower()

with open("search_word_33.txt","r") as f:
    data = f.read()
    words = data.split()
    
    if user_input in words:
        print("Word Found in file.")
    else:
        print("Not found in the file.")


