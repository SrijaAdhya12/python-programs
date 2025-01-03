# Remove all vowels from the string.

def remove_vowel(strg):
    new_string=""
    for char in strg:
        if char not in "aeiou":
            new_string += char
    return new_string
    
my_string = input("Enter a string: ")
print(remove_vowel(my_string))

# using lambda function

def rem_vowel(strg):
    new_string = ''.join(char for char in strg if char not in "aeiou")
    return new_string
    

my_str= input("Enter a string")
print(rem_vowel(my_str))
