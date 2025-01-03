# Return maximum occurring character in the input string.

def maximum_count(strng):
    max_count = 0
    max_char=""
    for char in strng:
        count = strng.count(char)
        if count > max_count:
            max_count = count
            max_char = char
    return max_char

my_string = input("Enter a string: ")
print(maximum_count(my_string))
            