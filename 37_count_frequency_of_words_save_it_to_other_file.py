# Write a program that counts the frequency of words in a file and saves it to another file.

from collections import Counter

with open("frequency_count_from_37.txt","r") as f:
    text = f.read()
    text = text.lower()


words = text.split()
freq = Counter(words)

with open("frequency_stored_in_37.txt","w+") as g:

    for word, Count in freq.items():
        g.write(f"{word} : {Count}\n")

print("Word frequencies have been written to 'frequency_stored_in_37.txt'")

