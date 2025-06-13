def binary_search(my_list):
    l,r = 0, len(my_list) - 1

    while l <= r:
        mid = (l+r) //2
        if num[mid] > target:
            r = mid -1
        elif num[mid] < target:
            l = mid+1
        else:
            return mid
    return -1  














my_list = list(int, input().split(" "))
target = int(input())
print(binary_search(my_list))
