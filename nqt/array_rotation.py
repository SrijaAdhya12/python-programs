def rotation(my_list,n, indices):
    new_list = []
    for _ in range(n):
        num = my_list.pop()
        my_list.insert(0,num)
    for i in indices:
        new_list.append(my_list[i])
    return new_list


def optimised_rotation(my_list,n, indices):
    k = n % len(my_list)
    return my_list[-k:] + my_list[:-k]

my_list = list(map(int, input().split(" ")))
n = int(input())
indices = list(map(int, input().split(" ")))
print(rotation(my_list, n, indices))
print(optimised_rotation(my_list, n, indices))