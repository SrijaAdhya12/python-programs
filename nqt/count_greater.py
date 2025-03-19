# Find element greater than all their previous element


def count_element(my_list):
    max_element = my_list[0]
    count = 0
    new_list = []
    for n in my_list:
        if n > max_element:
            new_list.append(n)
    return len(new_list) + 1
        

my_list = list(map(int,input().split()))
print(count_element(my_list))
