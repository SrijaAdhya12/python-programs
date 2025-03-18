# move by zero, move the zeros at last without changing the order of rest of the list 

def move_by_zero(my_list):
    zero_list = []
    num_list = []
    for num in my_list:
        if num == 0:
            zero_list.append(num)
        else:
            num_list.append(num)
    return num_list + zero_list

my_list = list(map(int, input().split()))
print(move_by_zero(my_list))