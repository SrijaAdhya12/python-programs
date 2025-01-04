# Remove all duplicates from the input string.

def remove_duplicate(string):
    my_set= set()
    result = []
    for char in string:
        if char not in my_set:
            result.append(char)
            my_set.add(char)
    return "".join(result)

my_string = input("Enter a string: ")
print(remove_duplicate(my_string)) 