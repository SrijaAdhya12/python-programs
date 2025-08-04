def sum_xor(num_list):
    odd_sum = 0
    even_xor = 0
    for k,v in enumerate(num_list):
        if k % 2 != 0:
            odd_sum += v
        else:
            even_xor ^= v 
    return odd_sum - even_xor


num_list = list(map(int, input().split(" ")))
print(sum_xor(num_list))
