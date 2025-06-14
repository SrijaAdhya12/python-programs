def toogle_bit(n,i):
    return n ^ (1 << i)



n = int(input())
i = int(input())
print(toogle_bit(n,i))