def remove_setbit(n, i):
    return n & (n-1)

n = int(input())
i = int(input())
print(remove_setbit(n, i))
