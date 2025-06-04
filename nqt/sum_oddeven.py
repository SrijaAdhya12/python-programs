def oddEven(num):
    new_str = str(num)
    odd_sum = 0
    even_sum = 0
    for i in range(len(new_str)):
        if i % 2 == 0:
            even_sum += int(new_str[i])
        else:
            odd_sum += int(new_str[i])
    return abs(odd_sum - even_sum)


num = int(input())
print(oddEven(num))