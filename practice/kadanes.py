def kadanes(arr):
    max_sum = arr[0]
    current_sum = 0
    for i in arr:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum


# def kadanes(arr):
#     max_sum = arr[0]
#     current_sum = 0
#     for i in arr:
#         current_sum += i
#         max_sum = max(current_sum, max_sum)
#         current_sum = max(0,current_sum)
#     return max_sum



# def kadanes(arr):
#     max_sum = arr[0]
#     start = end = s = current_sum = 0
#     for i in len(arr):
#         current_sum += i
#         if current_sum > max_sum:
#             max_sum = current_sum
#             start = s
#             end = i
#         if current_sum < 0:
#             current_sum = 0
#             s = i+1
#     return max_sum

arr = list(map(int, input().split()))
print(kadanes(arr))