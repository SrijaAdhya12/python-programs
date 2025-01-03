# Count number of vowels, consonants, spaces in a string

def counting(str):
    vowel = 0
    consonants = 0
    spaces = 0
    for letter in str:
        if letter in "aeiou":
            vowel+= 1
        elif letter in " ":
            spaces += 1
        else:
            consonants += 1
    return f"The number of vowels are {vowel} , the number of consonants are {consonants} and the number of spaces are {spaces}"

my_str = input("Enter a string: ")
print(counting(my_str))