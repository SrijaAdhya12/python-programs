from collections import deque


def maximum_subarray(my_list, n):
    target_sum = 0
    res = []
    for i in range(len(my_list)):
        for j in range(i,len(my_list)):
            subarray = my_list[i:j+1]
            if len(subarray) == 3:
                target_sum = max(subarray)
                res.append(target_sum)
    return res


#sliding window deque

def maximun_subarray(my_list, k):
    n = len(my_list)
    if n < k:
        return []
    
    dq = deque()
    result = []

    for i in range(n):
        while dq and dq[0] <= i-k:
            dq.popleft()

        while dq and my_list[dq[-1]] < my_list[i]:
            dp.pop()

        dq.append(i)

        if i>= k-1:
            result.append(my_list[dq[0]])
    return result



my_list = list(map(int, input().split(" ")))
n = int(input())
print(maximum_subarray(my_list, n))