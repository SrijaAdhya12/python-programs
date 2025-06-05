

# def sumation(my_list, K, N):
#     res = []
#     for i in range(len(my_list)):
#         for j in range(i,len(my_list)):
#             subarray = my_list[i:j+1]
#             if sum(subarray) == K:
#                 res.append(i+1)
#                 res.append(j+1)
#                 return res
#     return res

#slidingwindowapproach
def find_rooms(my_list, K):
    N = len(my_list)
    start,end,current_sum = 0,0,0
    result_start, result_end = 0, float('inf')

    while end < N:
        current_sum += my_list[end]

        while current_sum > K:
            current_sum -= my_list[start]
            start += 1

        if current_sum == K:
            if end - start < result_end - result_start:
                result_start, result_end = start, end
        
        end += 1

    if result_end == float('inf'):
        return "No result found"
    else:
        return result_start + 1, result_end+1








N = int(input())
K = int(input())
my_list = list(map(int, input().split(" ")))
print(find_rooms(my_list,K))