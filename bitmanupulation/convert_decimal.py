def binary_to_decimal(n):
    p2 = 1
    num = 0
    for i in range(len(n)-1,-1,-1):
        if n[i] == '1':
            num = num + p2
        p2 = p2*2
    return num


n = input()
print(binary_to_decimal(n))