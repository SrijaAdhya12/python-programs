# Capitalize first and last character of each word.


def capitalize(strng):
    return strng[0].upper() + strng[1: len(strng) - 1] + strng[len(strng) - 1].upper()

my_str = input("Enter a string: ")
print(capitalize(my_str))
