# Find the largest number in an array

def print_largest_number(strng):
    my_list = list(map(int, strng.split()))
    sorted_list = sorted(my_list, reverse=True)
    return sorted_list[0]

my_list = input("Enter a list: ")
print(print_largest_number(my_list))
    