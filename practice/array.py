# Count the number of elements in an array which are smaller than next consecutive element

def count_elements(num_list):
    count = 0
    for i in range(len(num_list)-1):
        if num_list[i+1] > num_list[i]:
            count += 1
    return count


my_list = input("Enter items in a list: ")
num_list = list(map(int, my_list.split()))
print(count_elements(num_list))