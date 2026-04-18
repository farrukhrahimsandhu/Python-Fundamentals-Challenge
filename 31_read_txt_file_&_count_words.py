# Write a program to read a text file and count words.

with open("count31.txt","r") as f:
    text = f.read()         
    words = text.split()        #where split breaks the string in words by space
    count_words = len(words)
print("The number of words are:",count_words)

