# Write a program to find the longest word in a text file.

with open("Find_largest_word_36.txt","r") as f:
    text = f.read()

    words = text.split()

longest_word = max(words, key=len)

print(f"The longest word is: {longest_word}")
print(f"The lenght of this word is {len(longest_word)}")

