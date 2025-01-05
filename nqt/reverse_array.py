# Reverse a given array

def reverse_array(array):
    return array[::-1]

def reverse_array1(array):
    index = 0
    while index != len(array)//2 -1:
        array[index], array[len(array) - 1]   = array[len(array) - 1], array[index]
        index += 1

def reverse_array2(array):
    for i in range(0, len(array)-1):
        array[i], array[len(array) - 1]   = array[len(array) - 1], array[i]
    
my_list = input("Enter a list: ").split()
print(reverse_array(my_list))
    
    
