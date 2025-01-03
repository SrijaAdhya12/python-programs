# remove spaces from a string

def remove_space(strng):
    return strng.replace(" ", "")

my_str = input("Enter a string: ")
print(remove_space(my_str))

# Find non-repeating characters of a string.

def non_repeating(strg):
    non_repeating_list = []
    for char in strg:
        if strg.count(char) == 1:
            non_repeating_list.append(char)
    return non_repeating_list


my_str = input("Enter a string: ")
print(non_repeating(my_str)) 

# Calculate frequency of characters in a string.

def frequency_calculator(strg):
    frequency  = {}
    for char in strg:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

my_str = input("Enter a string: ")
print(frequency_calculator(my_str))

# Return maximum occurring character in the input string.

def max_char(strng):
    max_count = 0
    max_char = ""
    for char in strng:
        count = strng.count(char)
        if count > max_count:
            max_count = count
            max_char = char
            
    return max_char

my_str = input("Enter a string: ") 
print(max_char(my_str))
        