import math


def find_bricks(n):
    ans = n*(3*n+1)/2
    return math.floor(ans)



n = int(input())
print(find_bricks(n))
