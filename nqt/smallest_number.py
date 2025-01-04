#find smallest number in an array

def find_smallest_number(strng):
    my_list = list(map(int , strng.split()))
    sorted_list = sorted(my_list)
    return sorted_list[0]

my_list = input("Enter a list: ")
print(find_smallest_number(my_list))