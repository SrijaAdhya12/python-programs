def set_ithbit(n, i):
    return n | (1 << i)

n = int(input())
i = int(input())
print(set_ithbit(n, i))
