# Find non-repeating characters of a string.

def non_repeating(stng):
    result = []
    for char in stng:
        if stng.count(char) == 1:
            result.append(char)
    return "".join(result)

my_string = input("Enter a string: ")  
print(non_repeating(my_string))  
        
        
    