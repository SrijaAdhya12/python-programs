# Sum of unique elements in an array


def sum_unique_elements(nums):
    my_set = set(nums)
    return sum(my_set)

my_list = list(map(int,input().split()))
print(sum_unique_elements(my_list))