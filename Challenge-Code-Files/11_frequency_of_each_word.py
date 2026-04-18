# Find the frequency of each word in a sentence.


# Take sentence as input from user
sentence = input("Enter a sentence: ")

# Convert to lowercase (optional)
sentence = sentence.lower()

# Split sentence into words
words = sentence.split()

# Create dictionary to store frequencies
frequency = {}

# Count word occurrences
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

# Print the result
print("\nWord Frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")


