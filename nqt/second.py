# Find the second smallest and second largest element in an array

def find_elements(lst):
    new_set = set(lst)
    new_list = sorted(new_set)
    second_smallest = new_list[1]
    second_largest = new_list[-2]
    return second_smallest, second_largest 


string = input("Enter a list: ")
my_list = list(map(int, string.split()))
result = find_elements(my_list)
print(f"The second smallest number is {result[0]} and second largest number is {result[-1]}")