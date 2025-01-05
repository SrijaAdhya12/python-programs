# Count the frequency of each element in an array

def count_frequency(strng):
    my_list = strng.split()
    my_dict = {}
    for char in my_list:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
            
    return my_dict

my_string = input("Enter a list: ")
print(count_frequency(my_string))
    