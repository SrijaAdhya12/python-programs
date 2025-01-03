# Remove spaces from a string.

def remove_spaces(strng):
    return strng.replace(" " , "")
    

my_string = input("Enter a string: ")
print(remove_spaces(my_string))