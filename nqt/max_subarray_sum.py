def sum_subarray(nums):
    current_sum = 0
    max_sum = nums[0]
    start = 0
    max_start = 0
    max_end = 0
    for i,n in enumerate(nums):
        current_sum += n
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = i
        
        if current_sum < 0:
            current_sum = 0
            start = i+1
    return max_sum , nums[max_start: max_end+1]


my_list = list(map(int,input().split()))
print(sum_subarray(my_list))