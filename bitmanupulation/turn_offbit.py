def turn_offbit(n,i):
    return n & ~(1 << i)



n = int(input())
i = int(input())
print(turn_offbit(n,i))