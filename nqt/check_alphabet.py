#Remove characters from a string except alphabets.

def is_alphabet(strng):
    new_string = ""
    for char in strng:
        if char.isalpha():
            new_string += char
    return new_string
    

my_str = input("Enter a string: ")
print(is_alphabet(my_str))
