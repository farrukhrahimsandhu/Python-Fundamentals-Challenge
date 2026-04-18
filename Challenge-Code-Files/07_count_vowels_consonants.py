# Count vowels and consonants in a string.

def vowel_cost_count(test):
    # define vowels 
    vowels = "aeiouAEIOU"

    vowel_count = 0
    const_count = 0

    for char in test:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                const_count += 1

    return vowel_count,const_count

text = input("Enter a string: ")
vowels , constants = vowel_cost_count(text)

print(f"The total number of Vowels in this String are {vowels}")
print(f"The total number of Constants in this String are {constants}")