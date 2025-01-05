# Find the second smallest and second largest element in an array

def find_element(strng):
    my_list = list(map(int, strng.split()))
    new_list = set(my_list)
    new_list1 = list(new_list)
    return f"The second smallest element is {new_list1[1]} and the second largest element {new_list1[len(new_list) - 2]}"

my_string = input("Enter a list: ")
print(find_element(my_string))