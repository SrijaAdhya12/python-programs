# Calculate frequency of characters in a string.

def count_frequency(stng):
    dict = {}
    for char in stng:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict
            

my_string = input("Enter a string: ")
print(count_frequency(my_string))