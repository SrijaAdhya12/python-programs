def print_duplicate(strng):
    my_set = set()  
    my_dict = {}
    
    for char in strng:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    for char, count in my_dict.items():
        if count > 1:
            my_set.add(char)

    if my_set:
        print(", ".join(my_set))
    else:
        print("No duplicates found")

my_string = input("Enter a string: ")
print_duplicate(my_string)
