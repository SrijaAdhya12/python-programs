def cal_difference(lst):
    n = len(lst)
    prefix_sum = [0] * (n+1)
    suffix_sum = [0] * (n+1)

    min_diff = float('inf')

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + lst[i]
        suffix_sum[n-i-1] = suffix_sum[n-i] + lst[n-i-1]

    for i in range(n):
        alex_sum = prefix_sum[i]
        bob_sum = suffix_sum[i]
        diff = abs(alex_sum - bob_sum)
        min_diff = min(min_diff, diff)
    
    return min_diff



arr = list(map(int, input().split(" ")))
print(cal_difference(arr))
